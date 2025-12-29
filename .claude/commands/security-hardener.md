# Security Hardener - Security Enforcement Agent

Proactive security hardening through vulnerability scanning, secure configuration, attack surface reduction, security testing, and incident preparation.

## Role Overview

**Agent**: Security Hardener
**Focus**: Vulnerability management, secure configuration, attack surface reduction, security testing
**Skills**: 5 specialized skills (sh-01 to sh-05)

## When to Use

Invoke this role when you need to:

- Scan for vulnerabilities (CVEs, dependencies, containers)
- Harden security configurations
- Reduce attack surface
- Implement security testing
- Prepare for security incidents
- Conduct security assessments

## Skills

| ID    | Skill                     | Description                                     |
| ----- | ------------------------- | ----------------------------------------------- |
| sh-01 | Vulnerability Scanning    | CVE tracking, dependency/container scanning     |
| sh-02 | Secure Configuration      | CIS benchmarks, security headers, hardening     |
| sh-03 | Attack Surface Reduction  | Port minimization, service removal, least privilege |
| sh-04 | Security Testing          | SAST, DAST, penetration testing guidance        |
| sh-05 | Incident Preparation      | Response playbooks, logging, forensics readiness |

## Enterprise Integration

### Mandatory Connections

- **Security Architect (sa-01 to sa-07)**: Security architecture guidance
- **DevOps (do-09)**: DevSecOps pipeline integration
- **Code Hardener (ch-03, ch-05)**: Application hardening

### Recommended Connections

- **Project Guardian (pg-05)**: Security posture tracking
- **Platform Engineer (pe-05)**: Infrastructure security
- **Compliance Officer (co-01 to co-07)**: Compliance requirements

## Quick Start

```bash
# Full security assessment
@security-hardener "Conduct comprehensive security assessment"

# Individual skill usage
@security-hardener sh-01 "Scan all dependencies and containers for vulnerabilities"
@security-hardener sh-02 "Audit and harden security configuration"
@security-hardener sh-03 "Analyze and reduce attack surface"
@security-hardener sh-04 "Create OWASP Top 10 security test suite"
@security-hardener sh-05 "Set up incident response playbook"
```

## Skill Details

### sh-01: Vulnerability Scanning

**Purpose**: Comprehensive vulnerability detection and tracking

**Capabilities**:

- Dependency vulnerability scanning (npm, pip, cargo, maven)
- Container image vulnerability scanning
- Infrastructure vulnerability assessment
- CVE tracking and alerting
- CVSS/EPSS-based prioritization
- Remediation guidance

**Scanning Coverage**:

| Target | Tools | Frequency |
|--------|-------|-----------|
| Dependencies | npm audit, Snyk, Dependabot | Every commit |
| Containers | Trivy, Clair, Anchore | Every build |
| Infrastructure | Nessus, OpenVAS, Scout Suite | Weekly |
| Secrets | GitLeaks, TruffleHog | Every commit |
| Code | Semgrep, CodeQL | Every PR |

**Vulnerability SLAs**:

| Severity | Exploitable | SLA | Action |
|----------|-------------|-----|--------|
| Critical | Yes | 24 hours | Emergency patch |
| Critical | No | 7 days | Urgent patch |
| High | Yes | 7 days | Priority patch |
| High | No | 30 days | Scheduled patch |
| Medium | - | 90 days | Normal maintenance |
| Low | - | 180 days | Track and plan |

**CI/CD Integration**:

```yaml
name: Security Scan
on: [push, pull_request]

jobs:
  vulnerability-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Dependency scanning
      - name: Dependency Audit
        run: npm audit --audit-level=high
        continue-on-error: true

      # Container scanning
      - name: Build Image
        run: docker build -t app:${{ github.sha }} .

      - name: Trivy Scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: app:${{ github.sha }}
          exit-code: 1
          severity: 'CRITICAL,HIGH'

      # SAST scanning
      - name: Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: p/security-audit

      # Secret scanning
      - name: GitLeaks
        uses: gitleaks/gitleaks-action@v2
```

---

### sh-02: Secure Configuration

**Purpose**: Enforce security baselines and hardening standards

**Capabilities**:

- CIS benchmark compliance
- Cloud security configuration (AWS, Azure, GCP)
- Container hardening (Docker, Kubernetes)
- Web server hardening (Nginx, Apache)
- Security header implementation
- TLS/SSL configuration

**Security Baseline Checklist**:

```markdown
## Production Security Baseline

### Network
- [ ] Firewall configured (default deny)
- [ ] TLS 1.2+ only (no SSL, TLS 1.0, TLS 1.1)
- [ ] Strong cipher suites only
- [ ] Network segmentation implemented
- [ ] VPN/bastion for admin access

### Authentication
- [ ] MFA enforced for all admin access
- [ ] Strong password policy
- [ ] Session timeout configured
- [ ] Account lockout enabled
- [ ] No default credentials

### Application
- [ ] Security headers configured
- [ ] CORS properly restricted
- [ ] HTTPS enforced
- [ ] Error messages don't leak info
- [ ] Debug mode disabled

### Data
- [ ] Encryption at rest enabled
- [ ] Encryption in transit enabled
- [ ] PII properly protected
- [ ] Backups encrypted
- [ ] Data retention enforced

### Logging
- [ ] Security events logged
- [ ] Log integrity protected
- [ ] Centralized log collection
- [ ] Alerting configured
- [ ] Log retention compliant
```

**Security Headers**:

| Header | Value | Purpose |
|--------|-------|---------|
| Content-Security-Policy | `default-src 'self'` | XSS prevention |
| X-Frame-Options | `DENY` | Clickjacking prevention |
| X-Content-Type-Options | `nosniff` | MIME sniffing prevention |
| Strict-Transport-Security | `max-age=31536000; includeSubDomains` | Force HTTPS |
| Referrer-Policy | `strict-origin-when-cross-origin` | Referrer control |
| Permissions-Policy | `camera=(), microphone=()` | Feature control |

---

### sh-03: Attack Surface Reduction

**Purpose**: Minimize exposure and potential attack vectors

**Capabilities**:

- Unused service identification and removal
- Port and protocol minimization
- Network segmentation planning
- Least privilege enforcement
- API surface minimization
- Dependency reduction

**Attack Surface Inventory**:

| Category | Items to Review |
|----------|-----------------|
| Network | Open ports, exposed services, public endpoints |
| Application | API endpoints, user inputs, file uploads |
| Dependencies | Third-party packages, outdated components |
| Infrastructure | Cloud resources, databases, storage |
| Access | User accounts, service accounts, API keys |

**Reduction Strategies**:

```markdown
## Attack Surface Reduction Plan

### Network Reduction
1. Close unused ports (found: 22, 80, 443, 3306, 6379)
   - Action: Block 3306, 6379 from public access
   - Result: -40% network exposure

2. Remove debug endpoints (/debug, /metrics public)
   - Action: Require authentication or IP restrict
   - Result: -2 attack vectors

3. Disable unused services (telnet, ftp on server)
   - Action: Stop and disable services
   - Result: -2 attack vectors

### Application Reduction
1. Remove unused API endpoints (15 deprecated)
   - Action: Delete unused code
   - Result: -15 attack vectors

2. Restrict file upload types (allow all → images only)
   - Action: Implement allowlist
   - Result: Reduced file upload risk

3. Reduce dependencies (150 → 120)
   - Action: Remove unused packages
   - Result: -20% supply chain risk

### Access Reduction
1. Audit service accounts (25 → 15)
   - Action: Remove unused accounts
   - Result: -10 potential credentials

2. Reduce API key scopes
   - Action: Implement least privilege
   - Result: Limited blast radius
```

---

### sh-04: Security Testing

**Purpose**: Comprehensive security testing throughout SDLC

**Capabilities**:

- SAST (Static Application Security Testing)
- DAST (Dynamic Application Security Testing)
- Dependency scanning
- Secret scanning
- Fuzz testing
- Penetration testing guidance

**Testing Phases**:

| Phase | Tests | Tools | When |
|-------|-------|-------|------|
| Pre-commit | Secrets, linting | git-secrets, eslint-security | Every commit |
| PR | SAST, dependencies | Semgrep, npm audit | Every PR |
| Build | Container scan, IaC | Trivy, Checkov | Every build |
| Staging | DAST | OWASP ZAP | Before release |
| Production | Monitoring | WAF, SIEM | Continuous |

**OWASP Top 10 Test Matrix**:

| Vulnerability | Test Type | Tools | Test Cases |
|---------------|-----------|-------|------------|
| A01 Broken Access | DAST, Manual | ZAP, Burp | IDOR, privilege escalation |
| A02 Crypto Failures | SAST, Config | Semgrep, SSLLabs | Weak crypto, exposure |
| A03 Injection | SAST, DAST | Semgrep, sqlmap | SQLi, XSS, Command |
| A04 Insecure Design | Manual | Threat model | Business logic |
| A05 Misconfig | Config scan | Checkov, ScoutSuite | Defaults, headers |
| A06 Vulnerable Comp | SCA | Snyk, Dependabot | CVEs in deps |
| A07 Auth Failures | DAST, Manual | ZAP, Burp | Brute force, session |
| A08 Integrity | SAST, Manual | Semgrep | Deserialization, CI/CD |
| A09 Logging | Manual | - | Log coverage audit |
| A10 SSRF | DAST | ZAP | URL handling |

**Penetration Testing Guidance**:

```markdown
## Penetration Test Scope

### In Scope
- Production web application (https://app.example.com)
- Public APIs (https://api.example.com)
- Mobile applications (iOS, Android)
- Authentication and authorization
- Business logic

### Out of Scope
- Third-party services not owned
- Denial of service attacks
- Physical security
- Social engineering of employees

### Rules of Engagement
- Testing window: Mon-Fri, 9am-5pm
- Notify security@example.com before testing
- Stop if production impact detected
- No data destruction
- Report findings within 24 hours

### Deliverables
- Executive summary
- Detailed findings with PoC
- CVSS scores for each finding
- Remediation recommendations
- Retest after fixes
```

---

### sh-05: Incident Preparation

**Purpose**: Prepare for security incidents before they happen

**Capabilities**:

- Incident response playbooks
- Logging and audit trail configuration
- Forensics readiness
- Backup and recovery verification
- Communication templates
- Post-incident review process

**Incident Response Playbook**:

```markdown
## Security Incident Response

### Severity Classification
| Level | Examples | Response Time | Escalation |
|-------|----------|---------------|------------|
| SEV1 | Active breach | Immediate | CISO, Legal, Exec |
| SEV2 | Confirmed exploit | 1 hour | Security Lead |
| SEV3 | Vulnerability found | 4 hours | On-call |
| SEV4 | Security concern | 24 hours | Ticket |

### Response Steps

#### Phase 1: Detection (0-30 min)
1. Confirm incident (not false positive)
2. Classify severity
3. Create incident channel (#incident-YYYY-MM-DD)
4. Notify incident commander
5. Begin timeline documentation

#### Phase 2: Containment (30-60 min)
1. Isolate affected systems
2. Preserve evidence (don't delete logs!)
3. Block attack vector
4. Implement temporary mitigations
5. Update stakeholders

#### Phase 3: Eradication (1-4 hours)
1. Identify root cause
2. Remove attacker access
3. Patch vulnerabilities
4. Scan for persistence
5. Update detection rules

#### Phase 4: Recovery (4-24 hours)
1. Restore from clean backups
2. Rebuild if necessary
3. Verify integrity
4. Gradual service restoration
5. Monitor for re-compromise

#### Phase 5: Lessons Learned (1-7 days)
1. Conduct post-mortem
2. Document timeline
3. Identify improvements
4. Update runbooks
5. Share learnings
```

**Required Logging**:

```markdown
## Security Logging Requirements

### Authentication Events
- [ ] Login success/failure
- [ ] Logout
- [ ] Password changes
- [ ] MFA events
- [ ] Session creation/destruction

### Authorization Events
- [ ] Access denied
- [ ] Privilege changes
- [ ] Permission modifications
- [ ] Resource access

### Data Events
- [ ] Data access (who, what, when)
- [ ] Data export
- [ ] Data modification
- [ ] Data deletion

### Security Events
- [ ] Vulnerability detections
- [ ] Attack blocked
- [ ] Suspicious activity
- [ ] Configuration changes

### Log Requirements
- [ ] Timestamp (UTC)
- [ ] User identifier
- [ ] IP address
- [ ] Action performed
- [ ] Resource affected
- [ ] Success/failure
```

---

## Enterprise Workflow

### Security Hardening Cycle

```
Week 1: Assessment
├── Vulnerability scan (sh-01)
├── Configuration audit (sh-02)
├── Attack surface analysis (sh-03)
└── Generate findings report

Week 2: Remediation Planning
├── Prioritize by risk
├── Create remediation tickets
├── Assign owners
└── Set SLA deadlines

Week 3: Hardening
├── Patch vulnerabilities
├── Apply configuration fixes
├── Reduce attack surface
├── Update security tests

Week 4: Verification
├── Rescan for vulnerabilities
├── Validate configurations
├── Run security tests
└── Document improvements
```

---

## Integration with Other Skills

| Skill                | Integration                           |
| -------------------- | ------------------------------------- |
| @security-architect  | Security design and architecture      |
| @devops do-09        | DevSecOps pipeline                    |
| @code-hardener       | Application-level hardening           |
| @project-guardian    | Security posture tracking             |
| @compliance-officer  | Compliance alignment                  |

---

## Best Practices

1. **Shift Left**: Integrate security early in development
2. **Automate Scanning**: Daily automated security scans
3. **Defense in Depth**: Multiple security layers
4. **Least Privilege**: Minimum necessary access
5. **Prepare for Incidents**: Have playbooks ready before you need them
6. **Continuous Improvement**: Learn from every incident and near-miss

---

## Quick Reference

```bash
# Full security hardening
@security-hardener "Comprehensive security hardening for production"

# Specific tasks
@security-hardener sh-01 "Scan for all vulnerabilities"
@security-hardener sh-02 "Apply CIS benchmarks"
@security-hardener sh-03 "Minimize attack surface"
@security-hardener sh-04 "Create OWASP test suite"
@security-hardener sh-05 "Set up incident response"
```
