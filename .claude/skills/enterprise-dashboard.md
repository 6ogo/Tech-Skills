# Enterprise Dashboard & Monitoring

Centralized visibility into security, compliance, governance, and operational metrics for enterprise applications.

## Role Overview

**Agent**: Enterprise Dashboard Specialist
**Focus**: Real-time monitoring, alerting, dashboards, and operational visibility
**Integration**: Aggregates data from all enterprise skills

## When to Use

- Create unified dashboards for enterprise metrics
- Set up alerting for security and compliance events
- Monitor SLOs across the platform
- Track governance and audit metrics
- Visualize data lineage and access patterns

## Dashboard Components

| Dashboard           | Metrics                                                         |
| ------------------- | --------------------------------------------------------------- |
| **Security**        | Posture score, vulnerabilities, events, secrets exposure        |
| **Compliance**      | Framework scores, control status, audit trail, findings         |
| **Data Governance** | Catalog coverage, quality score, PII locations, access requests |
| **Code Review**     | Cycle time, SLO compliance, reviewer load, quality gates        |
| **DORA Metrics**    | Deployment frequency, lead time, change failure rate, MTTR      |

## Templates

All dashboard templates are in `.claude/templates/dashboard/`:

| Template                                            | Purpose                               |
| --------------------------------------------------- | ------------------------------------- |
| [grafana.json](../templates/dashboard/grafana.json) | Enterprise overview Grafana dashboard |
| [alerts.yml](../templates/dashboard/alerts.yml)     | Prometheus/Grafana alerting rules     |
| [generator.py](../templates/dashboard/generator.py) | Python dashboard generator script     |

## Alert Categories

### Security Alerts

- Critical vulnerability detected
- Secrets exposed
- Unusual access pattern

### Compliance Alerts

- Control failed
- Audit log gap

### Code Review Alerts

- PR review SLO breach
- Reviewer overloaded

### Data Governance Alerts

- Data quality degraded
- PII access anomaly

## Integration

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
@enterprise-dashboard "Create security monitoring dashboard"
@enterprise-dashboard "Set up compliance alerting"
@enterprise-dashboard "Generate DORA metrics dashboard"
```
