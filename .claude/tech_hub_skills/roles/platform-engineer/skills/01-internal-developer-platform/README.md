# pe-01: Internal Developer Platform (IDP)

## Overview

Build developer portals using Backstage for service catalog, golden path templates, self-service provisioning, and platform documentation.

## Key Capabilities

- **Developer Portal**: Centralized platform UI (Backstage)
- **Service Catalog**: All services, APIs, documentation
- **Golden Path Templates**: Scaffolding for new services
- **Self-Service Provisioning**: One-click infrastructure
- **Platform Documentation**: Unified docs portal

## Tools & Technologies

- **Backstage**: Open-source developer portal
- **Port**: Developer portal platform
- **Humanitec**: Platform orchestrator
- **Kratix**: Platform-as-a-product framework

## Implementation

### 1. Backstage Setup

```yaml
# app-config.yaml
app:
  title: Tech Hub Platform
  baseUrl: http://localhost:3000

organization:
  name: Tech Innovation Hub

backend:
  baseUrl: http://localhost:7007
  listen:
    port: 7007
  database:
    client: pg
    connection:
      host: ${POSTGRES_HOST}
      port: ${POSTGRES_PORT}

catalog:
  providers:
    github:
      organization: 'your-org'
      catalogPath: '/catalog-info.yaml'
```

### 2. Service Catalog

```yaml
# catalog-info.yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: customer-api
  description: Customer management API
  annotations:
    github.com/project-slug: your-org/customer-api
    sonarqube.org/project-key: customer-api
spec:
  type: service
  lifecycle: production
  owner: team-platform
  system: customer-domain
  providesApis:
    - customer-api
  consumesApis:
    - auth-api
```

### 3. Golden Path Template

```yaml
# template.yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: python-fastapi-service
  title: Python FastAPI Service
  description: Create a new Python FastAPI microservice
spec:
  owner: platform-team
  type: service

  parameters:
    - title: Service Information
      required:
        - name
        - owner
      properties:
        name:
          title: Service Name
          type: string
          description: Unique name for the service
        owner:
          title: Owner
          type: string
          description: Team that owns this service

  steps:
    - id: fetch-template
      name: Fetch Template
      action: fetch:template
      input:
        url: ./skeleton
        values:
          name: ${{ parameters.name }}
          owner: ${{ parameters.owner }}

    - id: publish
      name: Publish to GitHub
      action: publish:github
      input:
        repoUrl: github.com?owner=your-org&repo=${{ parameters.name }}

    - id: register
      name: Register Component
      action: catalog:register
      input:
        repoContentsUrl: ${{ steps.publish.output.repoContentsUrl }}
        catalogInfoPath: '/catalog-info.yaml'
```

## Best Practices

1. **Start Small**: Begin with service catalog, add features iteratively
2. **Golden Paths**: Create templates for 80% of use cases
3. **Self-Service**: Minimize manual ticket workflows
4. **Measure Adoption**: Track active users and template usage
5. **Documentation**: Keep docs updated and searchable

## Cost Optimization

- Host Backstage on Kubernetes spot instances
- Use PostgreSQL managed service (cheaper than self-hosted)
- Cache plugin data to reduce API calls
- Right-size backend resources

## Integration

**Connects with:**
- do-01 (CI/CD): Link to deployment pipelines
- do-02 (Kubernetes): Service deployment info
- pe-03 (SLO): Display SLO status
- dg-01 (Catalog): Link to data catalog

## Quick Win

Deploy Backstage with GitHub integration, import 5 services to catalog, show team the unified view of their services.
