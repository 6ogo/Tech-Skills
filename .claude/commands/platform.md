# Platform Lead Command

Route to the Platform Lead Agent for infrastructure, DevOps, and cloud tasks.

## Usage

```
/platform [your request]
```

## Examples

```
/platform create CI/CD pipeline
/platform deploy to kubernetes
/platform set up AWS infrastructure
/platform configure monitoring
```

## What Happens

1. **Orchestrator** receives your request
2. **Platform Lead** takes ownership and analyzes
3. **Specialists** are assigned based on need:
   - DevOps (CI/CD, containers, IaC)
   - SRE (reliability, SLOs, incidents)
   - Platform Engineer (developer platform)
   - Network Engineer (VPC, load balancers)
   - Docker Specialist (containers)
   - Cloud Specialists (AWS/Azure/GCP)
   - FinOps (cost optimization)

## Available Skills

| Agent  | Skills                                                                                                 |
| ------ | ------------------------------------------------------------------------------------------------------ |
| DevOps | do-01 to do-09 (CI/CD, containers, IaC, GitOps, environments, testing, release, monitoring, DevSecOps) |
| SRE    | sr-01 to sr-07 (incidents, chaos, SLOs, errors, on-call, reliability, DR)                              |
| Docker | docker-01 to docker-05 (Dockerfile, security, optimization, compose, registry)                         |
| AWS    | aws-01 to aws-12 (all AWS services)                                                                    |
| Azure  | az-01 to az-12 (all Azure services)                                                                    |
| GCP    | gcp-01 to gcp-12 (all GCP services)                                                                    |
| FinOps | fo-01 to fo-08 (costs, tagging, budgets, reserved, spot, storage, compute, chargeback)                 |

## Mandatory Collaborations

- **Security Lead** → Always for production deployments
- **FinOps** → Always for cloud resources
