# pe-04: Developer Experience

## Overview

Improve developer velocity through automated onboarding, documentation-as-code, CLI tools, and DORA metrics tracking.

## Key Capabilities

- **Automated Onboarding**: Zero-to-commit in < 1 hour
- **Documentation-as-Code**: Docs in git, versioned
- **Developer CLI**: Unified command-line tools
- **DORA Metrics**: Deployment frequency, lead time, MTTR, change fail rate
- **Feedback Collection**: Regular developer surveys

## Implementation

```bash
# Developer CLI
#!/bin/bash
# platform-cli

case $1 in
  create-service)
    backstage scaffold $2 --template python-fastapi
    ;;
  deploy)
    kubectl apply -f k8s/ --namespace=$2
    ;;
  logs)
    kubectl logs -f deployment/$2 -n $3
    ;;
  metrics)
    open "https://grafana.company.com/d/dora-metrics"
    ;;
esac
```

```python
# DORA metrics collection
def calculate_dora_metrics(team_name, days=30):
    """Calculate DORA metrics"""
    deployments = get_deployments(team_name, days)
    incidents = get_incidents(team_name, days)

    metrics = {
        'deployment_frequency': len(deployments) / days,
        'lead_time_hours': sum(d.lead_time for d in deployments) / len(deployments),
        'mttr_hours': sum(i.resolution_time for i in incidents) / len(incidents) if incidents else 0,
        'change_fail_rate': len([d for d in deployments if d.failed]) / len(deployments)
    }

    return metrics
```

## Integration

**Connects with:** pe-01 (IDP), do-01 (CI/CD), pe-05 (Incident Management)
