# pe-02: Self-Service Infrastructure

## Overview

Enable developers to provision namespaces, databases, secrets, and environments through self-service automation.

## Key Capabilities

- **Namespace Provisioning**: Auto-create K8s namespaces
- **Database Provisioning**: Self-service DB creation
- **Secret Management**: Automated secret injection
- **Resource Quotas**: Automatic quota management
- **Environment Management**: Dev/staging/prod provisioning

## Implementation

```python
# Self-service namespace provisioning
from kubernetes import client, config

def provision_namespace(team_name, environment):
    """Create namespace with quotas and RBAC"""
    config.load_kube_config()
    v1 = client.CoreV1Api()

    # Create namespace
    namespace = client.V1Namespace(
        metadata=client.V1ObjectMeta(
            name=f"{team_name}-{environment}",
            labels={
                "team": team_name,
                "environment": environment
            }
        )
    )
    v1.create_namespace(namespace)

    # Apply resource quota
    quota = client.V1ResourceQuota(
        metadata=client.V1ObjectMeta(name="default-quota"),
        spec=client.V1ResourceQuotaSpec(
            hard={
                "requests.cpu": "10",
                "requests.memory": "20Gi",
                "pods": "50"
            }
        )
    )
    v1.create_namespaced_resource_quota(
        namespace=namespace.metadata.name,
        body=quota
    )
```

## Integration

**Connects with:** do-02 (Kubernetes), sa-06 (Secrets), pe-01 (IDP)
