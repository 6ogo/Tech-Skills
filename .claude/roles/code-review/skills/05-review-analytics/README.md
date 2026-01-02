# cr-05: Review Analytics

Metrics and insights for review process optimization and bottleneck detection.

## Overview

Review analytics provides visibility into your code review process, helping identify bottlenecks, balance workloads, and continuously improve team velocity. Track SLOs, measure cycle time, and make data-driven decisions.

## Capabilities

### Time Metrics
- Time to first review
- Time to approval
- Total cycle time (open to merge)
- Time in each review state

### Load Metrics
- Reviews per developer
- Review comments given/received
- Approval rate
- Change request rate

### Quality Metrics
- Defect escape rate
- Review iteration count
- PR size distribution
- Security findings per review

### Process Insights
- Bottleneck identification
- Trend analysis
- SLO compliance
- Prediction analytics

## Implementation

### Review Analytics Dashboard

```python
#!/usr/bin/env python3
"""Review analytics and metrics collection."""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from collections import defaultdict
import json

@dataclass
class ReviewEvent:
    """A single review event."""
    pr_number: int
    event_type: str  # opened, review_requested, reviewed, approved, merged
    timestamp: datetime
    actor: str
    details: Dict = field(default_factory=dict)

@dataclass
class PRMetrics:
    """Metrics for a single PR."""
    pr_number: int
    author: str
    opened_at: datetime
    merged_at: Optional[datetime] = None
    first_review_at: Optional[datetime] = None
    approved_at: Optional[datetime] = None
    lines_added: int = 0
    lines_removed: int = 0
    files_changed: int = 0
    review_iterations: int = 0
    reviewers: List[str] = field(default_factory=list)
    comments_count: int = 0

    @property
    def time_to_first_review(self) -> Optional[float]:
        """Hours until first review."""
        if self.first_review_at:
            return (self.first_review_at - self.opened_at).total_seconds() / 3600
        return None

    @property
    def time_to_approval(self) -> Optional[float]:
        """Hours until approval."""
        if self.approved_at:
            return (self.approved_at - self.opened_at).total_seconds() / 3600
        return None

    @property
    def cycle_time(self) -> Optional[float]:
        """Hours from open to merge."""
        if self.merged_at:
            return (self.merged_at - self.opened_at).total_seconds() / 3600
        return None

    @property
    def pr_size(self) -> str:
        """Categorize PR size."""
        total_lines = self.lines_added + self.lines_removed
        if total_lines < 50:
            return "XS"
        elif total_lines < 200:
            return "S"
        elif total_lines < 500:
            return "M"
        elif total_lines < 1000:
            return "L"
        else:
            return "XL"


class ReviewAnalytics:
    """Analyze review metrics and generate insights."""

    # SLO definitions
    SLOS = {
        "time_to_first_review": 4,      # hours
        "time_to_approval": 24,         # hours
        "cycle_time": 48,               # hours
        "max_review_iterations": 3,
        "max_pr_size": 400,             # lines
    }

    def __init__(self):
        self.prs: Dict[int, PRMetrics] = {}
        self.events: List[ReviewEvent] = []

    def add_pr(self, pr: PRMetrics) -> None:
        """Add PR metrics."""
        self.prs[pr.pr_number] = pr

    def add_event(self, event: ReviewEvent) -> None:
        """Add review event."""
        self.events.append(event)

    def calculate_team_metrics(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> Dict:
        """Calculate team-wide metrics for date range."""
        prs_in_range = [
            pr for pr in self.prs.values()
            if start_date <= pr.opened_at <= end_date
        ]

        if not prs_in_range:
            return {"error": "No PRs in date range"}

        merged_prs = [pr for pr in prs_in_range if pr.merged_at]

        return {
            "summary": {
                "total_prs": len(prs_in_range),
                "merged_prs": len(merged_prs),
                "merge_rate": f"{len(merged_prs) / len(prs_in_range) * 100:.1f}%",
            },
            "time_metrics": {
                "avg_time_to_first_review": self._avg([
                    pr.time_to_first_review for pr in merged_prs
                    if pr.time_to_first_review
                ]),
                "avg_time_to_approval": self._avg([
                    pr.time_to_approval for pr in merged_prs
                    if pr.time_to_approval
                ]),
                "avg_cycle_time": self._avg([
                    pr.cycle_time for pr in merged_prs
                    if pr.cycle_time
                ]),
                "p90_cycle_time": self._percentile([
                    pr.cycle_time for pr in merged_prs
                    if pr.cycle_time
                ], 90),
            },
            "quality_metrics": {
                "avg_review_iterations": self._avg([
                    pr.review_iterations for pr in merged_prs
                ]),
                "avg_comments_per_pr": self._avg([
                    pr.comments_count for pr in merged_prs
                ]),
            },
            "size_distribution": self._size_distribution(prs_in_range),
            "slo_compliance": self._calculate_slo_compliance(merged_prs),
        }

    def calculate_reviewer_metrics(self) -> Dict[str, Dict]:
        """Calculate per-reviewer metrics."""
        reviewer_stats = defaultdict(lambda: {
            "reviews_given": 0,
            "comments_given": 0,
            "approvals": 0,
            "change_requests": 0,
            "avg_response_time": [],
        })

        for event in self.events:
            if event.event_type == "reviewed":
                reviewer = event.actor
                reviewer_stats[reviewer]["reviews_given"] += 1

                state = event.details.get("state", "")
                if state == "APPROVED":
                    reviewer_stats[reviewer]["approvals"] += 1
                elif state == "CHANGES_REQUESTED":
                    reviewer_stats[reviewer]["change_requests"] += 1

        # Convert to final format
        return {
            reviewer: {
                "reviews_given": stats["reviews_given"],
                "approval_rate": (
                    f"{stats['approvals'] / stats['reviews_given'] * 100:.1f}%"
                    if stats["reviews_given"] > 0 else "N/A"
                ),
                "change_request_rate": (
                    f"{stats['change_requests'] / stats['reviews_given'] * 100:.1f}%"
                    if stats["reviews_given"] > 0 else "N/A"
                ),
            }
            for reviewer, stats in reviewer_stats.items()
        }

    def identify_bottlenecks(self) -> List[Dict]:
        """Identify review process bottlenecks."""
        bottlenecks = []

        # Check for slow first reviews
        slow_first_review = [
            pr for pr in self.prs.values()
            if pr.time_to_first_review and
               pr.time_to_first_review > self.SLOS["time_to_first_review"]
        ]
        if len(slow_first_review) > len(self.prs) * 0.2:
            bottlenecks.append({
                "type": "slow_first_review",
                "severity": "high",
                "message": f"{len(slow_first_review)} PRs ({len(slow_first_review)/len(self.prs)*100:.0f}%) "
                          f"exceed first review SLO of {self.SLOS['time_to_first_review']}h",
                "recommendation": "Add more reviewers or enable auto-assignment"
            })

        # Check for too many iterations
        high_iteration_prs = [
            pr for pr in self.prs.values()
            if pr.review_iterations > self.SLOS["max_review_iterations"]
        ]
        if high_iteration_prs:
            bottlenecks.append({
                "type": "high_iterations",
                "severity": "medium",
                "message": f"{len(high_iteration_prs)} PRs required >{self.SLOS['max_review_iterations']} review iterations",
                "recommendation": "Improve PR guidelines and automated checks"
            })

        # Check for oversized PRs
        large_prs = [
            pr for pr in self.prs.values()
            if pr.lines_added + pr.lines_removed > self.SLOS["max_pr_size"]
        ]
        if len(large_prs) > len(self.prs) * 0.3:
            bottlenecks.append({
                "type": "large_prs",
                "severity": "medium",
                "message": f"{len(large_prs)} PRs exceed {self.SLOS['max_pr_size']} lines",
                "recommendation": "Encourage smaller, focused PRs"
            })

        # Check reviewer load imbalance
        reviewer_loads = self.calculate_reviewer_metrics()
        if reviewer_loads:
            loads = [r["reviews_given"] for r in reviewer_loads.values()]
            if max(loads) > 3 * min(loads) if min(loads) > 0 else False:
                bottlenecks.append({
                    "type": "unbalanced_load",
                    "severity": "medium",
                    "message": "Review load is unbalanced across team",
                    "recommendation": "Enable load-balanced reviewer assignment"
                })

        return bottlenecks

    def _calculate_slo_compliance(self, prs: List[PRMetrics]) -> Dict:
        """Calculate SLO compliance rates."""
        if not prs:
            return {}

        first_review_compliant = sum(
            1 for pr in prs
            if pr.time_to_first_review and
               pr.time_to_first_review <= self.SLOS["time_to_first_review"]
        )

        approval_compliant = sum(
            1 for pr in prs
            if pr.time_to_approval and
               pr.time_to_approval <= self.SLOS["time_to_approval"]
        )

        cycle_compliant = sum(
            1 for pr in prs
            if pr.cycle_time and
               pr.cycle_time <= self.SLOS["cycle_time"]
        )

        return {
            "first_review_slo": f"{first_review_compliant / len(prs) * 100:.1f}%",
            "approval_slo": f"{approval_compliant / len(prs) * 100:.1f}%",
            "cycle_time_slo": f"{cycle_compliant / len(prs) * 100:.1f}%",
        }

    def _size_distribution(self, prs: List[PRMetrics]) -> Dict[str, int]:
        """Calculate PR size distribution."""
        dist = defaultdict(int)
        for pr in prs:
            dist[pr.pr_size] += 1
        return dict(dist)

    def _avg(self, values: List[float]) -> Optional[float]:
        """Calculate average, handling empty lists."""
        if not values:
            return None
        return round(sum(values) / len(values), 2)

    def _percentile(self, values: List[float], p: int) -> Optional[float]:
        """Calculate percentile."""
        if not values:
            return None
        sorted_values = sorted(values)
        idx = int(len(sorted_values) * p / 100)
        return round(sorted_values[min(idx, len(sorted_values) - 1)], 2)

    def generate_report(self, start_date: datetime, end_date: datetime) -> str:
        """Generate markdown analytics report."""
        metrics = self.calculate_team_metrics(start_date, end_date)
        bottlenecks = self.identify_bottlenecks()

        report = f"""# Code Review Analytics Report

**Period**: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}

## Summary
- Total PRs: {metrics['summary']['total_prs']}
- Merged PRs: {metrics['summary']['merged_prs']}
- Merge Rate: {metrics['summary']['merge_rate']}

## Time Metrics
| Metric | Value | SLO | Status |
|--------|-------|-----|--------|
| Avg Time to First Review | {metrics['time_metrics']['avg_time_to_first_review']}h | {self.SLOS['time_to_first_review']}h | {'' if metrics['time_metrics']['avg_time_to_first_review'] and metrics['time_metrics']['avg_time_to_first_review'] <= self.SLOS['time_to_first_review'] else ''} |
| Avg Time to Approval | {metrics['time_metrics']['avg_time_to_approval']}h | {self.SLOS['time_to_approval']}h | {'' if metrics['time_metrics']['avg_time_to_approval'] and metrics['time_metrics']['avg_time_to_approval'] <= self.SLOS['time_to_approval'] else ''} |
| Avg Cycle Time | {metrics['time_metrics']['avg_cycle_time']}h | {self.SLOS['cycle_time']}h | {'' if metrics['time_metrics']['avg_cycle_time'] and metrics['time_metrics']['avg_cycle_time'] <= self.SLOS['cycle_time'] else ''} |
| P90 Cycle Time | {metrics['time_metrics']['p90_cycle_time']}h | - | - |

## SLO Compliance
{chr(10).join(f"- {k}: {v}" for k, v in metrics['slo_compliance'].items())}

## PR Size Distribution
{chr(10).join(f"- {size}: {count} PRs" for size, count in sorted(metrics['size_distribution'].items()))}

## Identified Bottlenecks
"""

        if bottlenecks:
            for b in bottlenecks:
                report += f"""
### {b['type'].replace('_', ' ').title()}
- **Severity**: {b['severity']}
- **Issue**: {b['message']}
- **Recommendation**: {b['recommendation']}
"""
        else:
            report += "\nNo significant bottlenecks identified.\n"

        return report


# GitHub Action for weekly metrics
WEEKLY_METRICS_ACTION = """
name: Weekly Review Metrics
on:
  schedule:
    - cron: '0 9 * * 1'  # Monday 9 AM
  workflow_dispatch:

jobs:
  metrics:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Collect PR metrics
        uses: actions/github-script@v7
        id: metrics
        with:
          script: |
            const oneWeekAgo = new Date();
            oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);

            const { data: prs } = await github.rest.pulls.list({
              owner: context.repo.owner,
              repo: context.repo.repo,
              state: 'all',
              sort: 'created',
              direction: 'desc',
              per_page: 100
            });

            const weeklyPRs = prs.filter(pr =>
              new Date(pr.created_at) >= oneWeekAgo
            );

            const metrics = {
              total: weeklyPRs.length,
              merged: weeklyPRs.filter(pr => pr.merged_at).length,
              open: weeklyPRs.filter(pr => pr.state === 'open').length
            };

            return metrics;

      - name: Post to Slack
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "Weekly Review Metrics",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Weekly Code Review Metrics*\\n• Total PRs: ${{ fromJSON(steps.metrics.outputs.result).total }}\\n• Merged: ${{ fromJSON(steps.metrics.outputs.result).merged }}\\n• Open: ${{ fromJSON(steps.metrics.outputs.result).open }}"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
"""
```

### Grafana Dashboard Configuration

```json
{
  "dashboard": {
    "title": "Code Review Analytics",
    "panels": [
      {
        "title": "Time to First Review (hours)",
        "type": "stat",
        "targets": [
          {
            "expr": "avg(github_pr_time_to_first_review_hours)",
            "legendFormat": "Avg"
          }
        ],
        "thresholds": {
          "steps": [
            {"color": "green", "value": null},
            {"color": "yellow", "value": 4},
            {"color": "red", "value": 8}
          ]
        }
      },
      {
        "title": "Cycle Time Trend",
        "type": "timeseries",
        "targets": [
          {
            "expr": "avg(github_pr_cycle_time_hours) by (week)",
            "legendFormat": "Cycle Time"
          }
        ]
      },
      {
        "title": "Reviewer Load",
        "type": "barchart",
        "targets": [
          {
            "expr": "sum(github_reviews_given) by (reviewer)",
            "legendFormat": "{{reviewer}}"
          }
        ]
      },
      {
        "title": "PR Size Distribution",
        "type": "piechart",
        "targets": [
          {
            "expr": "count(github_pr_lines_changed) by (size_category)"
          }
        ]
      },
      {
        "title": "SLO Compliance",
        "type": "gauge",
        "targets": [
          {
            "expr": "github_review_slo_compliance_percent"
          }
        ],
        "thresholds": {
          "steps": [
            {"color": "red", "value": null},
            {"color": "yellow", "value": 80},
            {"color": "green", "value": 95}
          ]
        }
      }
    ]
  }
}
```

## Key Metrics Reference

| Metric | Formula | Target | Why It Matters |
|--------|---------|--------|----------------|
| Time to First Review | first_review_at - opened_at | < 4 hours | Fast feedback enables iteration |
| Time to Approval | approved_at - opened_at | < 24 hours | Prevents context switching |
| Cycle Time | merged_at - opened_at | < 48 hours | Overall delivery speed |
| Review Iterations | count(change_requests) | < 3 | Quality of initial submission |
| Review Load | reviews_per_person / team_avg | 0.8 - 1.2 | Balanced workload |
| Defect Escape Rate | bugs_in_reviewed_code / total_bugs | < 1% | Review effectiveness |

## Connections

- **Inputs from**: All review activities (cr-01 to cr-04)
- **Outputs to**: Dashboards, reports, alerts
- **Integrates with**: Platform (pe-05 SLOs), FinOps (cost of delays)

## Best Practices

1. Track metrics weekly, analyze monthly, set goals quarterly
2. Focus on trends, not individual data points
3. Share metrics transparently with team
4. Use data to improve process, not blame individuals
5. Set realistic SLOs based on baseline, then improve
6. Correlate review metrics with production quality
