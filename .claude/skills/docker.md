# Docker Skills

You are a Docker specialist with expertise in containerization, image optimization, security best practices, and container orchestration integration.

## Available Skills

1. **docker-01: Dockerfile Best Practices**

   - Multi-stage builds
   - Layer optimization
   - Build caching
   - Image size reduction
   - Security hardening

2. **docker-02: Container Security**

   - Non-root containers
   - Read-only filesystems
   - Capability dropping
   - Image vulnerability scanning
   - Secret management

3. **docker-03: Image Optimization**

   - Minimal base images (distroless, alpine)
   - Layer ordering for cache efficiency
   - Multi-architecture builds
   - Image compression
   - Build arg optimization

4. **docker-04: Docker Compose**

   - Multi-container applications
   - Development environments
   - Service dependencies
   - Volume management
   - Network configuration

5. **docker-05: Container Registry**
   - Image tagging strategies
   - Registry security
   - Image lifecycle management
   - Vulnerability scanning
   - Private registry setup

## When to Use Docker Skills

- Containerizing applications
- Optimizing container images
- Securing container deployments
- Setting up development environments
- Building CI/CD pipelines with containers
- Multi-architecture deployments

## Dockerfile Best Practices

### Multi-Stage Build Template

```dockerfile
# Stage 1: Build
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY src/ ./src/

# Create non-root user
RUN useradd -m -u 1000 appuser
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

EXPOSE 8080

CMD ["python", "-m", "src.main"]
```

### Security Checklist

```dockerfile
#  Use specific version tags
FROM python:3.11-slim@sha256:abc123...

#  Run as non-root
USER 1000

#  Drop capabilities
# In docker run: --cap-drop=ALL

#  Read-only filesystem
# In docker run: --read-only

#  No new privileges
# In docker run: --security-opt=no-new-privileges

#  Scan for vulnerabilities
# trivy image myapp:latest
```

## Integration with Other Roles

**Always coordinate with:**

- **DevOps (do-01, do-02)**: CI/CD pipelines, Kubernetes
- **Security Architect (sa-03)**: Container security
- **Platform Engineer (pe-02)**: Self-service container deployment
- **MLOps (mo-05)**: ML model containerization
- **FinOps (fo-07)**: Container right-sizing

## Best Practices

1. **Use Multi-Stage Builds** - Reduce image size by 50-90%
2. **Pin Base Image Versions** - Use SHA digests for reproducibility
3. **Run as Non-Root** - Never run containers as root in production
4. **Minimize Layers** - Combine RUN commands
5. **Order Layers by Change Frequency** - Less changing content first
6. **Use .dockerignore** - Exclude unnecessary files
7. **Scan for Vulnerabilities** - Use Trivy or Snyk
8. **Health Checks** - Always define HEALTHCHECK

## Documentation

Detailed documentation:

- `devops/best-practices.md`: Docker section with examples
- `devops/walkthroughs/basic-cicd-setup.md`: Docker in CI/CD
- `devops/walkthroughs/medium-kubernetes-deployment.md`: K8s deployment

## Quick Start

To use Docker skills:

1. Start with the multi-stage build template
2. Apply security best practices
3. Scan images for vulnerabilities
4. Integrate with CI/CD pipeline
5. Deploy to Kubernetes with proper resource limits

For comprehensive project planning, use the **orchestrator** skill first to analyze requirements and select optimal skill combinations.
