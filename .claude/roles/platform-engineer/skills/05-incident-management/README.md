# pe-05: Incident Management

## Overview

On-call management, incident response procedures, postmortem templates, runbook automation, and alert routing.

## Key Capabilities

- **On-Call Management**: Rotation schedules
- **Incident Response**: Clear escalation procedures
- **Postmortem Templates**: Blameless retrospectives
- **Runbook Automation**: Auto-remediation
- **Alert Routing**: Intelligent alert distribution

## Implementation

```yaml
# PagerDuty incident response
services:
  - name: customer-api
    escalation_policy: platform-team
    alert_grouping: intelligent
    incident_urgency_rule:
      type: constant
      urgency: high

# Runbook automation
runbooks:
  - name: high-memory-usage
    trigger: memory_usage > 90%
    actions:
      - restart_pod
      - scale_replicas: 2
      - notify_oncall
```

```python
# Postmortem template generator
def create_postmortem(incident_id):
    """Generate postmortem document"""
    incident = get_incident(incident_id)

    template = f"""
# Incident Postmortem: {incident.title}

## Incident Summary
- **Date**: {incident.date}
- **Duration**: {incident.duration}
- **Severity**: {incident.severity}
- **Responders**: {incident.responders}

## Timeline
{incident.timeline}

## Root Cause
[To be filled]

## Resolution
{incident.resolution}

## Action Items
- [ ] TODO 1
- [ ] TODO 2

## Lessons Learned
[To be filled]
"""
    return template
```

## Integration

**Connects with:** pe-03 (SLO), do-08 (Monitoring), pe-01 (IDP)
