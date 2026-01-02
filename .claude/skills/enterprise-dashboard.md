# Enterprise Dashboard & Monitoring

Centralized visibility into security, compliance, governance, and operational metrics for enterprise applications.

## Role Overview

**Agent**: Enterprise Dashboard Specialist
**Focus**: Real-time monitoring, alerting, dashboards, and operational visibility
**Integration**: Aggregates data from all enterprise skills

## When to Use

Invoke this role when you need to:
- Create unified dashboards for enterprise metrics
- Set up alerting for security and compliance events
- Monitor SLOs across the platform
- Track governance and audit metrics
- Visualize data lineage and access patterns

## Dashboard Components

### 1. Security Dashboard

```yaml
# security-dashboard.yml
panels:
  - title: "Security Posture Score"
    type: gauge
    metrics:
      - vulnerability_count
      - compliance_score
      - incident_count
    thresholds:
      critical: 60
      warning: 80
      healthy: 95

  - title: "Active Vulnerabilities"
    type: stat
    breakdown:
      - critical
      - high
      - medium
      - low

  - title: "Security Events (24h)"
    type: timeseries
    metrics:
      - authentication_failures
      - authorization_denials
      - suspicious_activities

  - title: "Secrets Exposure"
    type: stat
    metrics:
      - exposed_secrets_count
      - secrets_rotation_due

  - title: "Container Security"
    type: table
    columns:
      - image_name
      - vulnerability_count
      - last_scanned
```

### 2. Compliance Dashboard

```yaml
# compliance-dashboard.yml
panels:
  - title: "Compliance Score by Framework"
    type: barchart
    frameworks:
      - SOC2
      - GDPR
      - HIPAA
      - PCI-DSS

  - title: "Control Status"
    type: piechart
    statuses:
      - passed
      - failed
      - warning
      - not_applicable

  - title: "Audit Trail Activity"
    type: timeseries
    metrics:
      - audit_events_per_hour
      - compliance_checks_run

  - title: "Open Findings"
    type: table
    columns:
      - finding_id
      - severity
      - framework
      - age_days
      - owner

  - title: "Evidence Collection"
    type: stat
    metrics:
      - evidence_artifacts_count
      - last_evidence_generated
```

### 3. Data Governance Dashboard

```yaml
# governance-dashboard.yml
panels:
  - title: "Data Catalog Coverage"
    type: gauge
    target: 100%

  - title: "Data Quality Score"
    type: stat
    dimensions:
      - completeness
      - accuracy
      - timeliness
      - consistency

  - title: "PII Data Locations"
    type: geomap
    data: pii_distribution

  - title: "Access Requests"
    type: timeseries
    metrics:
      - approved_requests
      - denied_requests
      - pending_requests

  - title: "Data Lineage"
    type: flowchart
    show: critical_data_flows
```

### 4. Code Review Dashboard

```yaml
# code-review-dashboard.yml
panels:
  - title: "Review Cycle Time"
    type: timeseries
    metrics:
      - avg_time_to_first_review
      - avg_time_to_approval
      - avg_cycle_time

  - title: "SLO Compliance"
    type: gauge
    slos:
      - first_review_4h
      - approval_24h
      - merge_48h

  - title: "Reviewer Load"
    type: barchart
    by: reviewer

  - title: "PR Size Distribution"
    type: piechart
    categories: [XS, S, M, L, XL]

  - title: "Quality Gate Pass Rate"
    type: stat
    breakdown_by: gate_type
```

## Implementation

### Grafana Dashboard as Code

```json
{
  "dashboard": {
    "title": "Enterprise Overview",
    "uid": "enterprise-overview",
    "tags": ["enterprise", "overview"],
    "timezone": "browser",
    "refresh": "5m",
    "rows": [
      {
        "title": "Executive Summary",
        "panels": [
          {
            "title": "Overall Health Score",
            "type": "gauge",
            "datasource": "prometheus",
            "targets": [
              {
                "expr": "(security_score + compliance_score + quality_score) / 3"
              }
            ],
            "fieldConfig": {
              "defaults": {
                "thresholds": {
                  "steps": [
                    {"color": "red", "value": null},
                    {"color": "yellow", "value": 70},
                    {"color": "green", "value": 90}
                  ]
                },
                "min": 0,
                "max": 100
              }
            }
          },
          {
            "title": "Active Incidents",
            "type": "stat",
            "datasource": "prometheus",
            "targets": [
              {"expr": "sum(active_incidents)"}
            ],
            "fieldConfig": {
              "defaults": {
                "thresholds": {
                  "steps": [
                    {"color": "green", "value": null},
                    {"color": "yellow", "value": 1},
                    {"color": "red", "value": 5}
                  ]
                }
              }
            }
          },
          {
            "title": "Compliance Status",
            "type": "stat",
            "datasource": "prometheus",
            "targets": [
              {"expr": "compliance_passing_controls / compliance_total_controls * 100"}
            ]
          },
          {
            "title": "Open PRs Awaiting Review",
            "type": "stat",
            "datasource": "github",
            "targets": [
              {"query": "count(open_prs where status = 'awaiting_review')"}
            ]
          }
        ]
      },
      {
        "title": "Security",
        "panels": [
          {
            "title": "Vulnerabilities by Severity",
            "type": "barchart",
            "datasource": "security-scanner",
            "targets": [
              {"expr": "vulnerabilities_count by (severity)"}
            ]
          },
          {
            "title": "Security Events Timeline",
            "type": "timeseries",
            "datasource": "prometheus",
            "targets": [
              {"expr": "rate(security_events_total[5m])", "legendFormat": "Events/min"}
            ]
          }
        ]
      },
      {
        "title": "Delivery Metrics",
        "panels": [
          {
            "title": "Deployment Frequency",
            "type": "stat",
            "datasource": "prometheus",
            "targets": [
              {"expr": "sum(increase(deployments_total[7d]))"}
            ]
          },
          {
            "title": "Lead Time for Changes",
            "type": "gauge",
            "datasource": "prometheus",
            "targets": [
              {"expr": "avg(lead_time_hours)"}
            ]
          },
          {
            "title": "Change Failure Rate",
            "type": "stat",
            "datasource": "prometheus",
            "targets": [
              {"expr": "failed_deployments / total_deployments * 100"}
            ]
          },
          {
            "title": "MTTR",
            "type": "stat",
            "datasource": "prometheus",
            "targets": [
              {"expr": "avg(incident_recovery_time_minutes)"}
            ]
          }
        ]
      }
    ]
  }
}
```

### Alerting Rules

```yaml
# alerting-rules.yml
groups:
  - name: security-alerts
    rules:
      - alert: CriticalVulnerabilityDetected
        expr: vulnerabilities_critical > 0
        for: 0m
        labels:
          severity: critical
          team: security
        annotations:
          summary: "Critical vulnerability detected"
          description: "{{ $value }} critical vulnerabilities found"

      - alert: SecretsExposed
        expr: exposed_secrets_count > 0
        for: 0m
        labels:
          severity: critical
          team: security
        annotations:
          summary: "Exposed secrets detected"
          runbook: "https://wiki/runbooks/secrets-exposure"

      - alert: UnusualAccessPattern
        expr: access_anomaly_score > 0.9
        for: 5m
        labels:
          severity: high
          team: security
        annotations:
          summary: "Unusual access pattern detected"

  - name: compliance-alerts
    rules:
      - alert: ComplianceControlFailed
        expr: compliance_control_status == 0
        for: 0m
        labels:
          severity: high
          team: compliance
        annotations:
          summary: "Compliance control failed: {{ $labels.control }}"

      - alert: AuditLogGap
        expr: time() - audit_last_event_timestamp > 3600
        for: 5m
        labels:
          severity: medium
        annotations:
          summary: "No audit events in the last hour"

  - name: code-review-alerts
    rules:
      - alert: PRReviewSLOBreach
        expr: pr_time_without_review_hours > 24
        for: 0m
        labels:
          severity: medium
          team: engineering
        annotations:
          summary: "PR #{{ $labels.pr_number }} waiting > 24h for review"

      - alert: ReviewerOverloaded
        expr: reviewer_active_prs > 7
        for: 0m
        labels:
          severity: low
        annotations:
          summary: "Reviewer {{ $labels.reviewer }} has too many active reviews"

  - name: data-governance-alerts
    rules:
      - alert: DataQualityDegraded
        expr: data_quality_score < 0.8
        for: 15m
        labels:
          severity: medium
          team: data
        annotations:
          summary: "Data quality below threshold for {{ $labels.dataset }}"

      - alert: PIIAccessAnomaly
        expr: pii_access_anomaly_score > 0.8
        for: 5m
        labels:
          severity: high
          team: security
        annotations:
          summary: "Unusual PII access pattern detected"
```

### Dashboard Generator Script

```python
#!/usr/bin/env python3
"""Generate enterprise dashboards from configuration."""

import json
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Panel:
    """Dashboard panel configuration."""
    title: str
    panel_type: str
    datasource: str
    queries: List[str]
    thresholds: Dict[str, int] = None
    position: Dict[str, int] = None

@dataclass
class Dashboard:
    """Complete dashboard configuration."""
    title: str
    uid: str
    panels: List[Panel]
    refresh: str = "5m"

class DashboardGenerator:
    """Generate Grafana dashboards from templates."""

    def __init__(self):
        self.templates = {
            "security": self._security_template,
            "compliance": self._compliance_template,
            "code-review": self._code_review_template,
            "governance": self._governance_template,
        }

    def generate(self, template_name: str) -> Dict[str, Any]:
        """Generate dashboard from template."""
        if template_name not in self.templates:
            raise ValueError(f"Unknown template: {template_name}")

        return self.templates[template_name]()

    def _security_template(self) -> Dict:
        """Generate security dashboard."""
        return {
            "dashboard": {
                "title": "Security Overview",
                "uid": "security-overview",
                "panels": [
                    {
                        "title": "Security Score",
                        "type": "gauge",
                        "gridPos": {"x": 0, "y": 0, "w": 6, "h": 8},
                        "targets": [{"expr": "security_posture_score"}],
                    },
                    {
                        "title": "Vulnerabilities",
                        "type": "stat",
                        "gridPos": {"x": 6, "y": 0, "w": 6, "h": 4},
                        "targets": [{"expr": "sum(vulnerabilities_count)"}],
                    },
                    {
                        "title": "Security Events",
                        "type": "timeseries",
                        "gridPos": {"x": 12, "y": 0, "w": 12, "h": 8},
                        "targets": [
                            {"expr": "rate(security_events_total[5m])", "legendFormat": "Events"}
                        ],
                    },
                ]
            }
        }

    def _compliance_template(self) -> Dict:
        """Generate compliance dashboard."""
        return {
            "dashboard": {
                "title": "Compliance Status",
                "uid": "compliance-status",
                "panels": [
                    {
                        "title": "SOC 2 Compliance",
                        "type": "gauge",
                        "gridPos": {"x": 0, "y": 0, "w": 6, "h": 6},
                        "targets": [{"expr": "soc2_compliance_score"}],
                    },
                    {
                        "title": "GDPR Compliance",
                        "type": "gauge",
                        "gridPos": {"x": 6, "y": 0, "w": 6, "h": 6},
                        "targets": [{"expr": "gdpr_compliance_score"}],
                    },
                    {
                        "title": "Open Findings",
                        "type": "table",
                        "gridPos": {"x": 0, "y": 6, "w": 24, "h": 10},
                        "targets": [{"expr": "compliance_findings"}],
                    },
                ]
            }
        }

    def _code_review_template(self) -> Dict:
        """Generate code review dashboard."""
        return {
            "dashboard": {
                "title": "Code Review Metrics",
                "uid": "code-review-metrics",
                "panels": [
                    {
                        "title": "Avg Time to First Review",
                        "type": "stat",
                        "gridPos": {"x": 0, "y": 0, "w": 6, "h": 4},
                        "targets": [{"expr": "avg(pr_time_to_first_review_hours)"}],
                    },
                    {
                        "title": "Review Cycle Time Trend",
                        "type": "timeseries",
                        "gridPos": {"x": 6, "y": 0, "w": 18, "h": 8},
                        "targets": [
                            {"expr": "avg(pr_cycle_time_hours)", "legendFormat": "Cycle Time"}
                        ],
                    },
                    {
                        "title": "Reviewer Load",
                        "type": "barchart",
                        "gridPos": {"x": 0, "y": 8, "w": 12, "h": 8},
                        "targets": [{"expr": "reviews_per_person by (reviewer)"}],
                    },
                ]
            }
        }

    def _governance_template(self) -> Dict:
        """Generate data governance dashboard."""
        return {
            "dashboard": {
                "title": "Data Governance",
                "uid": "data-governance",
                "panels": [
                    {
                        "title": "Data Catalog Coverage",
                        "type": "gauge",
                        "gridPos": {"x": 0, "y": 0, "w": 8, "h": 6},
                        "targets": [{"expr": "catalog_coverage_percent"}],
                    },
                    {
                        "title": "Data Quality Score",
                        "type": "gauge",
                        "gridPos": {"x": 8, "y": 0, "w": 8, "h": 6},
                        "targets": [{"expr": "data_quality_score"}],
                    },
                    {
                        "title": "PII Distribution",
                        "type": "piechart",
                        "gridPos": {"x": 16, "y": 0, "w": 8, "h": 6},
                        "targets": [{"expr": "pii_count by (classification)"}],
                    },
                ]
            }
        }

    def export_all(self, output_dir: str = "dashboards") -> None:
        """Export all dashboards to JSON files."""
        import os
        os.makedirs(output_dir, exist_ok=True)

        for name, template_fn in self.templates.items():
            dashboard = template_fn()
            with open(f"{output_dir}/{name}.json", "w") as f:
                json.dump(dashboard, f, indent=2)
            print(f"Generated: {output_dir}/{name}.json")


if __name__ == "__main__":
    generator = DashboardGenerator()
    generator.export_all()
```

## Enterprise Integration

### Connected Skills
- **Security Architect (sa-07)**: Security monitoring data
- **Data Governance (dg-01-06)**: Governance metrics
- **Code Review (cr-05)**: Review analytics
- **Compliance Automation**: Compliance status

### Data Sources
- Prometheus/Grafana for metrics
- GitHub API for code review data
- Security scanners (Snyk, SonarQube)
- Audit log systems

## Quick Reference

```bash
# In Claude Code
@enterprise-dashboard "Create security monitoring dashboard"
@enterprise-dashboard "Set up compliance alerting"
@enterprise-dashboard "Generate DORA metrics dashboard"
```
