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
