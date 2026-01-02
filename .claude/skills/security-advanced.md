# Security - Advanced Skills

Extended security skills covering supply chain, API security, zero trust, and cloud security posture.

##  Trigger Keywords

- "SBOM", "software bill of materials", "supply chain"
- "API security", "OAuth", "OIDC", "JWT"
- "zero trust", "never trust", "always verify"
- "CSPM", "cloud security", "misconfiguration"
- "sigstore", "provenance", "signing"

---

## sa-08: API Security

### When to Use

- Designing authentication for APIs
- Implementing OAuth2/OIDC
- Securing API gateways
- JWT handling and validation

### Skills

```yaml
api_security:
  authentication:
    - OAuth 2.0 flows (auth code, client credentials)
    - OIDC (OpenID Connect)
    - API keys (with rotation)
    - mTLS (mutual TLS)

  authorization:
    - RBAC (Role-Based Access Control)
    - ABAC (Attribute-Based Access Control)
    - Scope-based permissions
    - Policy engines (OPA, Cedar)

  token_management:
    - JWT best practices
    - Token validation
    - Refresh token rotation
    - Token revocation

  api_gateway:
    - Rate limiting
    - Request validation
    - Response filtering
    - WAF integration

  threats:
    - BOLA (Broken Object Level Auth)
    - BFLA (Broken Function Level Auth)
    - Injection attacks
    - Mass assignment
```

### Best Practices

```yaml
jwt:
  - Use short expiration (15 min access, 7 day refresh)
  - Validate all claims (iss, aud, exp, iat)
  - Use RS256+ (asymmetric) not HS256
  - Never store sensitive data in JWT payload

api_keys:
  - Hash stored keys (like passwords)
  - Implement rotation
  - Scope keys to minimum permissions
  - Rate limit per key

oauth:
  - Use PKCE for public clients
  - Validate redirect URIs strictly
  - Implement state parameter
  - Use short-lived auth codes
```

### Integration

```
→ sa-04 (IAM): Identity management
→ sa-06 (Secrets): Key storage
→ be-06 (Backend): Rate limiting
→ do-08 (DevOps): Monitoring auth failures
```

---

## sa-09: Supply Chain Security

### When to Use

- Securing build pipelines
- Validating dependencies
- Creating SBOMs
- Signing artifacts

### Skills

```yaml
supply_chain:
  sbom:
    description: "Software Bill of Materials"
    formats:
      - SPDX
      - CycloneDX
      - SWID tags
    generators:
      - Syft
      - Trivy
      - cdxgen
    uses:
      - Vulnerability tracking
      - License compliance
      - Dependency visibility

  signing:
    - Sigstore (keyless signing)
    - cosign (container signing)
    - Notary v2
    - GPG for packages

  provenance:
    - SLSA framework (levels 1-4)
    - Build attestations
    - In-toto layouts
    - GitHub artifact attestation

  dependency_security:
    - Dependabot
    - Renovate
    - Snyk
    - Socket.dev (supply chain attacks)

  build_security:
    - Hermetic builds
    - Reproducible builds
    - Minimal base images
    - Build provenance
```

### SLSA Levels

```yaml
slsa_levels:
  level_1:
    - Build process documented
    - Automated build

  level_2:
    - Version control
    - Hosted build service
    - Signed provenance

  level_3:
    - Hardened build platform
    - Non-falsifiable provenance

  level_4:
    - Hermetic, reproducible
    - Two-person review
```

### Integration

```
→ do-01 (DevOps): CI/CD pipeline
→ do-09 (DevSecOps): Security scanning
→ docker-02 (Docker): Container security
→ co-06 (Compliance): Audit trails
```

---

## sa-10: Zero Trust Architecture

### When to Use

- Designing modern security architectures
- Moving away from perimeter security
- Implementing microsegmentation
- Continuous verification

### Skills

```yaml
zero_trust:
  principles:
    - Never trust, always verify
    - Assume breach
    - Least privilege access
    - Explicit verification

  pillars:
    identity:
      - Strong authentication (MFA)
      - Continuous validation
      - Just-in-time access
      - Identity governance

    device:
      - Device health checks
      - Endpoint detection (EDR)
      - Certificate-based auth
      - Mobile device management

    network:
      - Microsegmentation
      - Software-defined perimeter
      - Encrypted communications
      - Network access control

    application:
      - API security
      - Runtime protection
      - Application-level auth
      - Service mesh (mTLS)

    data:
      - Data classification
      - Encryption everywhere
      - DLP controls
      - Access logging

  implementation:
    - Beyond Corp (Google)
    - Azure AD Conditional Access
    - AWS IAM Identity Center
    - Cloudflare Access
```

### Migration Path

```yaml
zero_trust_journey:
  phase_1:
    - Inventory assets and identities
    - Implement strong MFA
    - Classify data

  phase_2:
    - Microsegmentation start
    - Conditional access policies
    - Device compliance

  phase_3:
    - Full microsegmentation
    - Continuous verification
    - Automated response
```

### Integration

```
→ sa-04 (IAM): Identity management
→ ne-04 (Network): Microsegmentation
→ do-08 (DevOps): Monitoring
→ sr-01 (SRE): Incident response
```

---

## sa-11: Cloud Security Posture Management (CSPM)

### When to Use

- Auditing cloud configurations
- Detecting misconfigurations
- Compliance verification
- Multi-cloud security

### Skills

```yaml
cspm:
  tools:
    open_source:
      - Prowler (AWS, Azure, GCP)
      - ScoutSuite
      - CloudSploit
      - Steampipe

    commercial:
      - Wiz
      - Prisma Cloud
      - Orca Security
      - AWS Security Hub

  checks:
    - Public S3 buckets
    - Unencrypted storage
    - Overly permissive IAM
    - Missing MFA
    - Exposed secrets
    - Network exposure

  compliance_mappings:
    - CIS Benchmarks
    - SOC 2
    - PCI-DSS
    - HIPAA
    - NIST
    - ISO 27001

  remediation:
    - Automated fixes (IaC)
    - Policy enforcement
    - Drift detection
    - Continuous monitoring
```

### Common Misconfigurations

```yaml
critical_checks:
  aws:
    - S3 bucket public access
    - Security group 0.0.0.0/0
    - Root account usage
    - Missing CloudTrail
    - Unencrypted RDS

  azure:
    - Storage account public
    - NSG allow all
    - No diagnostic settings
    - Missing Azure Policy

  gcp:
    - Public Cloud Storage
    - Default service account
    - Missing audit logs
    - Overly permissive IAM
```

### Integration

```
→ do-03 (DevOps): IaC templates
→ co-01 to co-05 (Compliance): Frameworks
→ aws/azure/gcp: Cloud-specific
→ fo-01 (FinOps): Cost of security
```

---

## Skill Dependencies

| Skill                | Requires     | Enables         |
| -------------------- | ------------ | --------------- |
| sa-08 (API Security) | sa-04, sa-06 | Secure APIs     |
| sa-09 (Supply Chain) | do-01, do-09 | Secure builds   |
| sa-10 (Zero Trust)   | sa-04, ne-04 | Modern security |
| sa-11 (CSPM)         | cloud skills | Cloud security  |

## Quick Reference

```yaml
# When to use which skill
api_security: "I need to secure my APIs/auth"
supply_chain: "I need to secure my build pipeline"
zero_trust: "I need modern security architecture"
cspm: "I need to audit cloud configurations"
```
