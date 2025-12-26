# pe-03: SLO/SLI Management

## Overview

Define and track Service Level Objectives (SLOs), manage error budgets, instrument SLIs, and create SLO-based alerting.

## Key Capabilities

- **SLO Definition**: Availability, latency, error rate targets
- **Error Budget Management**: Track remaining error budget
- **SLI Instrumentation**: Collect service-level indicators
- **SLO-Based Alerting**: Alert on error budget burn
- **SLO Dashboards**: Visualize SLO compliance

## Implementation

```yaml
# SLO definition (Sloth)
version: prometheus/v1
service: customer-api
slos:
  - name: requests-availability
    objective: 99.9
    description: 99.9% of requests successful
    sli:
      events:
        error_query: |
          sum(rate(http_requests_total{job="customer-api",code=~"5.."}[5m]))
        total_query: |
          sum(rate(http_requests_total{job="customer-api"}[5m]))
    alerting:
      name: CustomerAPIHighErrorRate
      labels:
        severity: page
      annotations:
        summary: High error rate on customer API
```

```python
# Error budget calculation
def calculate_error_budget(slo_target, time_window_days=30):
    """Calculate remaining error budget"""
    total_minutes = time_window_days * 24 * 60
    allowed_downtime = total_minutes * (1 - slo_target/100)

    actual_downtime = get_actual_downtime(time_window_days)
    remaining_budget = allowed_downtime - actual_downtime

    return {
        'allowed_downtime_minutes': allowed_downtime,
        'actual_downtime_minutes': actual_downtime,
        'remaining_budget_minutes': remaining_budget,
        'budget_consumed_percent': (actual_downtime / allowed_downtime) * 100
    }
```

## Integration

**Connects with:** do-08 (Monitoring), pe-01 (IDP), pe-05 (Incident Management)
