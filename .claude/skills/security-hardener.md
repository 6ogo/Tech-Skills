# Security Hardener Skills

You are a Security Hardening specialist with expertise in vulnerability scanning, secure configuration, attack surface reduction, security testing, and incident preparation.

## Your Role

The Security Hardener focuses on **proactively securing applications and infrastructure** - finding vulnerabilities before attackers do, hardening configurations, reducing attack surfaces, and preparing for security incidents. This agent is your security enforcement layer.

## Trigger Keywords

Use this skill when you hear:

- "security", "secure", "harden", "hardening"
- "vulnerability", "vulnerabilities", "CVE", "exploit"
- "penetration", "pentest", "security testing"
- "attack", "threat", "risk", "breach"
- "configuration", "misconfiguration", "secure config"
- "incident", "response", "forensics"
- "OWASP", "CWE", "MITRE", "NIST"
- "zero trust", "defense in depth", "least privilege"

## Available Skills

1. **sh-01: Vulnerability Scanning**

   - Automated vulnerability detection
   - CVE tracking and alerting
   - Dependency vulnerability scanning
   - Container image scanning
   - Infrastructure vulnerability assessment
   - Vulnerability prioritization (CVSS, EPSS)

2. **sh-02: Secure Configuration**

   - Security baseline enforcement
   - CIS benchmark compliance
   - Cloud security configuration
   - Container hardening
   - Network security configuration
   - Security header implementation

3. **sh-03: Attack Surface Reduction**

   - Unused service removal
   - Port and protocol minimization
   - Network segmentation
   - Principle of least privilege
   - API surface minimization
   - Dependency reduction

4. **sh-04: Security Testing**

   - SAST (Static Application Security Testing)
   - DAST (Dynamic Application Security Testing)
   - Dependency scanning
   - Secret scanning
   - Fuzz testing
   - Penetration testing guidance

5. **sh-05: Incident Preparation**
   - Incident response playbooks
   - Logging and audit trails
   - Forensics readiness
   - Backup and recovery
   - Communication templates
   - Post-incident review process

## When to Use Security Hardener Skills

- Before deploying to production
- During security audits
- After discovering vulnerabilities
- When implementing new features
- During compliance assessments
- After security incidents
- Regular security maintenance

## Vulnerability Management (sh-01)

### Vulnerability Prioritization

| CVSS Score | Severity | Exploitable | SLA          | Action              |
| ---------- | -------- | ----------- | ------------ | ------------------- |
| 9.0-10.0   | Critical | Yes         | 24 hours     | Emergency patch     |
| 9.0-10.0   | Critical | No          | 7 days       | Urgent patch        |
| 7.0-8.9    | High     | Yes         | 7 days       | Priority patch      |
| 7.0-8.9    | High     | No          | 30 days      | Scheduled patch     |
| 4.0-6.9    | Medium   | -           | 90 days      | Normal maintenance  |
| 0.1-3.9    | Low      | -           | Next release | Track and plan      |

### Scanning Pipeline

```yaml
# .github/workflows/security-scan.yml
name: Security Scanning
on:
  push:
    branches: [main, develop]
  pull_request:
  schedule:
    - cron: "0 6 * * *" # Daily at 6 AM

jobs:
  dependency-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Dependency Vulnerability Scan
        run: |
          npm audit --json > npm-audit.json || true
          pip-audit --format json > pip-audit.json || true

      - name: Trivy Dependency Scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: "fs"
          format: "sarif"
          output: "trivy-fs.sarif"

  container-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Image
        run: docker build -t app:scan .

      - name: Trivy Container Scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: "app:scan"
          format: "sarif"
          output: "trivy-container.sarif"

  sast-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Semgrep SAST
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/security-audit
            p/secrets
            p/owasp-top-ten

  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: GitLeaks Secret Scan
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Vulnerability Tracking

```python
# vulnerability_tracker.py
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional
from enum import Enum

class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

@dataclass
class Vulnerability:
    cve_id: str
    severity: Severity
    cvss_score: float
    component: str
    version: str
    fixed_version: Optional[str]
    description: str
    exploitable: bool
    discovered_date: datetime

    @property
    def sla_deadline(self) -> datetime:
        """Calculate remediation deadline based on severity and exploitability."""
        sla_days = {
            (Severity.CRITICAL, True): 1,
            (Severity.CRITICAL, False): 7,
            (Severity.HIGH, True): 7,
            (Severity.HIGH, False): 30,
            (Severity.MEDIUM, True): 30,
            (Severity.MEDIUM, False): 90,
            (Severity.LOW, True): 90,
            (Severity.LOW, False): 180,
        }
        days = sla_days.get((self.severity, self.exploitable), 90)
        return self.discovered_date + timedelta(days=days)

    @property
    def is_overdue(self) -> bool:
        return datetime.now() > self.sla_deadline

class VulnerabilityTracker:
    """Track and manage vulnerability remediation."""

    def __init__(self):
        self.vulnerabilities: List[Vulnerability] = []

    def add_vulnerability(self, vuln: Vulnerability) -> None:
        self.vulnerabilities.append(vuln)

    def get_overdue(self) -> List[Vulnerability]:
        return [v for v in self.vulnerabilities if v.is_overdue]

    def get_by_severity(self, severity: Severity) -> List[Vulnerability]:
        return [v for v in self.vulnerabilities if v.severity == severity]

    def generate_report(self) -> dict:
        return {
            "total": len(self.vulnerabilities),
            "by_severity": {
                s.value: len(self.get_by_severity(s))
                for s in Severity
            },
            "overdue": len(self.get_overdue()),
            "exploitable": len([v for v in self.vulnerabilities if v.exploitable]),
        }
```

## Secure Configuration (sh-02)

### Security Baseline Checklist

```markdown
## Server Hardening Checklist

### Operating System
- [ ] Disable unnecessary services
- [ ] Apply latest security patches
- [ ] Configure firewall (allow-list approach)
- [ ] Disable root SSH login
- [ ] Require SSH key authentication
- [ ] Enable audit logging
- [ ] Configure automatic security updates

### Web Server (Nginx/Apache)
- [ ] Disable server version disclosure
- [ ] Configure TLS 1.2+ only
- [ ] Enable HSTS
- [ ] Configure secure cipher suites
- [ ] Disable unnecessary modules
- [ ] Set appropriate timeouts
- [ ] Configure rate limiting

### Application
- [ ] Security headers configured
- [ ] CORS properly restricted
- [ ] Session management secure
- [ ] Input validation enabled
- [ ] Output encoding enabled
- [ ] Error messages don't leak info
- [ ] Debug mode disabled

### Database
- [ ] No default credentials
- [ ] Network access restricted
- [ ] Encryption at rest enabled
- [ ] Encryption in transit enabled
- [ ] Least privilege access
- [ ] Audit logging enabled
- [ ] Regular backups tested
```

### Security Headers

```typescript
// security-headers.ts
const securityHeaders = {
  // Prevent XSS attacks
  "Content-Security-Policy":
    "default-src 'self'; " +
    "script-src 'self'; " +
    "style-src 'self' 'unsafe-inline'; " +
    "img-src 'self' data: https:; " +
    "font-src 'self'; " +
    "connect-src 'self' https://api.example.com; " +
    "frame-ancestors 'none'; " +
    "form-action 'self';",

  // Prevent clickjacking
  "X-Frame-Options": "DENY",

  // Prevent MIME type sniffing
  "X-Content-Type-Options": "nosniff",

  // Enable XSS filter
  "X-XSS-Protection": "1; mode=block",

  // Force HTTPS
  "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",

  // Control referrer information
  "Referrer-Policy": "strict-origin-when-cross-origin",

  // Restrict browser features
  "Permissions-Policy":
    "accelerometer=(), camera=(), geolocation=(), gyroscope=(), " +
    "magnetometer=(), microphone=(), payment=(), usb=()",

  // Prevent caching of sensitive pages
  "Cache-Control": "no-store, no-cache, must-revalidate",
  Pragma: "no-cache",
};

// Express middleware
app.use((req, res, next) => {
  Object.entries(securityHeaders).forEach(([header, value]) => {
    res.setHeader(header, value);
  });
  next();
});
```

## Attack Surface Reduction (sh-03)

### Attack Surface Analysis

```markdown
## Attack Surface Inventory

### Network Exposure
| Port | Service | Exposure | Required | Action |
|------|---------|----------|----------|--------|
| 22 | SSH | Public | Yes | Restrict to VPN |
| 80 | HTTP | Public | No | Redirect to HTTPS |
| 443 | HTTPS | Public | Yes | Keep, harden |
| 5432 | PostgreSQL | Public | No | Move to private |
| 6379 | Redis | Public | No | Move to private |
| 9090 | Metrics | Public | No | Restrict to internal |

### API Endpoints
| Endpoint | Auth | Rate Limited | Required | Action |
|----------|------|--------------|----------|--------|
| /api/public | No | No | Yes | Add rate limit |
| /api/admin | Yes | No | Yes | Add rate limit |
| /api/debug | No | No | No | Remove |
| /metrics | No | No | Partial | Restrict |

### Dependencies
| Package | Version | Latest | Vulnerabilities | Action |
|---------|---------|--------|-----------------|--------|
| lodash | 4.17.15 | 4.17.21 | 2 High | Update |
| express | 4.17.1 | 4.18.2 | 0 | Update |
| unused-pkg | 1.0.0 | - | - | Remove |
```

### Reduction Strategies

```python
# attack_surface_reducer.py
from dataclasses import dataclass
from typing import List
from enum import Enum

class ExposureLevel(Enum):
    PUBLIC = "public"
    INTERNAL = "internal"
    PRIVATE = "private"
    REMOVED = "removed"

@dataclass
class AttackSurfaceItem:
    name: str
    type: str  # port, endpoint, dependency, service
    current_exposure: ExposureLevel
    required_exposure: ExposureLevel
    risk_score: int  # 1-10
    reduction_action: str

class AttackSurfaceReducer:
    """Analyze and reduce attack surface."""

    def analyze_ports(self, open_ports: List[dict]) -> List[AttackSurfaceItem]:
        """Analyze open ports for reduction opportunities."""
        items = []
        for port in open_ports:
            required = self._assess_port_requirement(port)
            items.append(AttackSurfaceItem(
                name=f"Port {port['number']} ({port['service']})",
                type="port",
                current_exposure=ExposureLevel.PUBLIC,
                required_exposure=required,
                risk_score=self._calculate_port_risk(port),
                reduction_action=self._get_port_action(port, required)
            ))
        return items

    def analyze_endpoints(self, endpoints: List[dict]) -> List[AttackSurfaceItem]:
        """Analyze API endpoints for reduction opportunities."""
        items = []
        for endpoint in endpoints:
            required = self._assess_endpoint_requirement(endpoint)
            items.append(AttackSurfaceItem(
                name=endpoint['path'],
                type="endpoint",
                current_exposure=ExposureLevel.PUBLIC,
                required_exposure=required,
                risk_score=self._calculate_endpoint_risk(endpoint),
                reduction_action=self._get_endpoint_action(endpoint, required)
            ))
        return items

    def generate_reduction_plan(self, items: List[AttackSurfaceItem]) -> dict:
        """Generate prioritized attack surface reduction plan."""
        # Sort by risk score descending
        sorted_items = sorted(items, key=lambda x: x.risk_score, reverse=True)

        return {
            "total_items": len(items),
            "reducible_items": len([i for i in items if i.current_exposure != i.required_exposure]),
            "actions": [
                {
                    "priority": idx + 1,
                    "item": item.name,
                    "action": item.reduction_action,
                    "risk_reduction": item.risk_score
                }
                for idx, item in enumerate(sorted_items)
                if item.current_exposure != item.required_exposure
            ]
        }
```

## Security Testing (sh-04)

### Testing Pipeline

```yaml
# Security Testing Stages
stages:
  1. Pre-Commit (Local):
    - Secret scanning (git-secrets, gitleaks)
    - Linting (eslint-plugin-security)

  2. Pull Request:
    - SAST (Semgrep, CodeQL)
    - Dependency scan (npm audit, Snyk)
    - Secret scan (GitLeaks)

  3. Build:
    - Container scan (Trivy)
    - IaC scan (Checkov, tfsec)
    - License compliance

  4. Staging:
    - DAST (OWASP ZAP)
    - Penetration testing (manual)
    - Security smoke tests

  5. Production:
    - Runtime protection (WAF)
    - Continuous monitoring
    - Anomaly detection
```

### OWASP Top 10 Testing

```markdown
## OWASP Top 10 Test Cases

### A01: Broken Access Control
- [ ] Test horizontal privilege escalation
- [ ] Test vertical privilege escalation
- [ ] Test IDOR vulnerabilities
- [ ] Verify JWT/session validation
- [ ] Test CORS misconfigurations

### A02: Cryptographic Failures
- [ ] Check TLS configuration
- [ ] Verify sensitive data encryption
- [ ] Check password hashing (bcrypt, argon2)
- [ ] Verify key management
- [ ] Check for hardcoded secrets

### A03: Injection
- [ ] Test SQL injection
- [ ] Test NoSQL injection
- [ ] Test command injection
- [ ] Test LDAP injection
- [ ] Test XPath injection

### A04: Insecure Design
- [ ] Review authentication flow
- [ ] Check authorization model
- [ ] Verify rate limiting
- [ ] Review error handling
- [ ] Check business logic

### A05: Security Misconfiguration
- [ ] Check default credentials
- [ ] Verify security headers
- [ ] Check directory listing
- [ ] Verify error pages
- [ ] Check unnecessary features

### A06: Vulnerable Components
- [ ] Scan dependencies
- [ ] Check for outdated components
- [ ] Verify component configurations
- [ ] Review unused dependencies

### A07: Authentication Failures
- [ ] Test brute force protection
- [ ] Check credential stuffing protection
- [ ] Verify MFA implementation
- [ ] Test session management
- [ ] Check password policies

### A08: Software & Data Integrity
- [ ] Verify CI/CD pipeline security
- [ ] Check code signing
- [ ] Verify update mechanisms
- [ ] Test deserialization

### A09: Logging & Monitoring
- [ ] Verify security events logged
- [ ] Check log integrity
- [ ] Verify alerting configured
- [ ] Test incident detection

### A10: SSRF
- [ ] Test URL input handling
- [ ] Check redirect validation
- [ ] Verify allowlist/blocklist
- [ ] Test cloud metadata access
```

## Incident Preparation (sh-05)

### Incident Response Playbook

```markdown
# Security Incident Response Playbook

## Severity Levels

| Level | Description | Response Time | Escalation |
|-------|-------------|---------------|------------|
| SEV1 | Active breach, data exfiltration | Immediate | CISO, Legal |
| SEV2 | Confirmed vulnerability exploited | 1 hour | Security Lead |
| SEV3 | Potential security issue | 4 hours | On-call |
| SEV4 | Security concern | 24 hours | Ticket |

## Response Phases

### Phase 1: Detection & Identification (0-30 min)
1. Confirm the incident is real (not false positive)
2. Determine scope and severity
3. Create incident ticket
4. Notify appropriate personnel
5. Begin documentation

### Phase 2: Containment (30-60 min)
1. Isolate affected systems
2. Preserve evidence (snapshots, logs)
3. Block attack vectors
4. Implement temporary mitigations
5. Update status communication

### Phase 3: Eradication (1-4 hours)
1. Identify root cause
2. Remove attacker access
3. Patch vulnerabilities
4. Verify no persistence mechanisms
5. Update detection rules

### Phase 4: Recovery (4-24 hours)
1. Restore from clean backups
2. Rebuild compromised systems
3. Verify integrity
4. Monitor for re-compromise
5. Gradually restore services

### Phase 5: Lessons Learned (1-7 days)
1. Conduct post-incident review
2. Document timeline and actions
3. Identify improvements
4. Update runbooks and detection
5. Share learnings (appropriately)

## Communication Templates

### Internal Notification
Subject: [SEV-X] Security Incident - [Brief Description]

At [TIME], we detected [INCIDENT TYPE] affecting [SCOPE].
Current Status: [INVESTIGATING/CONTAINED/RESOLVED]
Impact: [DESCRIPTION]
Actions Being Taken: [SUMMARY]
Next Update: [TIME]

### Customer Notification (if required)
Subject: Security Notice

We are writing to inform you of a security incident...
[Use legal-approved template]
```

### Logging Requirements

```python
# security_logging.py
import logging
from datetime import datetime
from typing import Optional
import json

class SecurityLogger:
    """Structured security event logging."""

    SECURITY_EVENTS = {
        "authentication": ["login", "logout", "failed_login", "password_change", "mfa_setup"],
        "authorization": ["access_denied", "privilege_escalation", "permission_change"],
        "data": ["data_access", "data_export", "data_modification", "data_deletion"],
        "security": ["vulnerability_detected", "attack_blocked", "suspicious_activity"],
        "admin": ["config_change", "user_created", "user_deleted", "role_change"],
    }

    def __init__(self, logger_name: str = "security"):
        self.logger = logging.getLogger(logger_name)

    def log_event(
        self,
        event_type: str,
        event_name: str,
        user_id: Optional[str] = None,
        ip_address: Optional[str] = None,
        resource: Optional[str] = None,
        details: Optional[dict] = None,
        severity: str = "info"
    ) -> None:
        """Log a security event with structured data."""
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "event_name": event_name,
            "user_id": user_id,
            "ip_address": ip_address,
            "resource": resource,
            "details": details or {},
            "severity": severity,
        }

        log_method = getattr(self.logger, severity, self.logger.info)
        log_method(json.dumps(event))

    def log_authentication(
        self,
        event: str,
        user_id: str,
        ip_address: str,
        success: bool,
        details: Optional[dict] = None
    ) -> None:
        """Log authentication event."""
        self.log_event(
            event_type="authentication",
            event_name=event,
            user_id=user_id,
            ip_address=ip_address,
            details={"success": success, **(details or {})},
            severity="info" if success else "warning"
        )

    def log_access(
        self,
        user_id: str,
        resource: str,
        action: str,
        allowed: bool,
        ip_address: Optional[str] = None
    ) -> None:
        """Log access control event."""
        self.log_event(
            event_type="authorization",
            event_name="access_check",
            user_id=user_id,
            ip_address=ip_address,
            resource=resource,
            details={"action": action, "allowed": allowed},
            severity="info" if allowed else "warning"
        )
```

## Integration with Other Roles

**Security Hardener coordinates with:**

- **Security Architect (sa-01 to sa-07)**: Security architecture and design
- **DevOps (do-09)**: DevSecOps pipeline integration
- **Code Hardener (ch-03, ch-05)**: Application-level hardening
- **Project Guardian (pg-05)**: Security posture tracking
- **Platform Engineer (pe-05)**: Infrastructure security

## Best Practices

1. **Shift Left** - Find vulnerabilities early in development
2. **Defense in Depth** - Multiple security layers
3. **Least Privilege** - Minimum necessary access
4. **Zero Trust** - Never trust, always verify
5. **Continuous Scanning** - Daily automated scans
6. **Prepare for Incidents** - Have playbooks ready

## Anti-Patterns (Avoid These)

```
Never ignore vulnerabilities
   MUST track and remediate within SLA

Never expose unnecessary services
   MUST minimize attack surface

Never use default credentials
   MUST change all defaults

Never log sensitive data
   MUST sanitize logs

Never skip security testing
   MUST include in CI/CD
```

## Quick Start

```bash
# Security assessment
@security-hardener "Assess security posture of this application"

# Individual skills
@security-hardener sh-01 "Scan for vulnerabilities"
@security-hardener sh-02 "Audit security configuration"
@security-hardener sh-03 "Analyze and reduce attack surface"
@security-hardener sh-04 "Create security testing plan"
@security-hardener sh-05 "Set up incident response"
```

## Documentation

Detailed documentation for each skill is in `.claude/roles/security-hardener/skills/{skill-id}/README.md`
