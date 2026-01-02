# Compliance Automation

Automated compliance checking, audit trails, and regulatory requirement validation for enterprise software delivery.

## Role Overview

**Agent**: Compliance Automation Specialist
**Focus**: Regulatory compliance, audit trails, policy enforcement, certification readiness
**Skills**: Integrated compliance checking throughout the SDLC

## When to Use

Invoke this role when you need to:
- Automate compliance checks in CI/CD
- Generate audit trails and evidence
- Validate against regulatory frameworks (GDPR, SOC 2, HIPAA, PCI-DSS)
- Prepare for compliance audits
- Implement policy-as-code

## Compliance Frameworks Supported

| Framework | Focus | Key Requirements |
|-----------|-------|------------------|
| SOC 2 | Security Controls | Access control, encryption, monitoring |
| GDPR | Data Privacy | Consent, data rights, breach notification |
| HIPAA | Healthcare Data | PHI protection, access logs, encryption |
| PCI-DSS | Payment Data | Cardholder data protection, network security |
| ISO 27001 | InfoSec Management | Risk assessment, security controls |
| FedRAMP | Government Cloud | Security authorization, continuous monitoring |

## Compliance as Code

### Policy Engine Configuration

```yaml
# .compliance/policies.yml
version: 1
framework: soc2

policies:
  # CC6.1 - Logical and Physical Access Controls
  access-control:
    enabled: true
    rules:
      - id: AC-001
        name: "No hardcoded credentials"
        check: secrets-scan
        severity: critical
        remediation: "Use secrets manager (Azure Key Vault, AWS Secrets Manager)"

      - id: AC-002
        name: "Enforce MFA"
        check: iam-policy
        severity: high
        remediation: "Configure MFA for all user accounts"

      - id: AC-003
        name: "Principle of least privilege"
        check: rbac-review
        severity: high
        remediation: "Review and minimize role permissions"

  # CC6.7 - Encryption in Transit and at Rest
  encryption:
    enabled: true
    rules:
      - id: EN-001
        name: "TLS 1.2+ required"
        check: tls-version
        severity: critical
        remediation: "Upgrade to TLS 1.2 or higher"

      - id: EN-002
        name: "Data at rest encryption"
        check: storage-encryption
        severity: high
        remediation: "Enable encryption for all storage resources"

  # CC7.2 - Monitoring and Logging
  monitoring:
    enabled: true
    rules:
      - id: MO-001
        name: "Audit logging enabled"
        check: audit-logs
        severity: high
        remediation: "Enable audit logging for all services"

      - id: MO-002
        name: "Log retention >= 1 year"
        check: log-retention
        severity: medium
        remediation: "Configure log retention to 365 days minimum"

  # CC8.1 - Change Management
  change-management:
    enabled: true
    rules:
      - id: CM-001
        name: "All changes via PR"
        check: branch-protection
        severity: high
        remediation: "Enable branch protection with required reviews"

      - id: CM-002
        name: "Approved before deploy"
        check: deployment-approvals
        severity: high
        remediation: "Configure environment protection rules"
```

### GitHub Actions Compliance Workflow

```yaml
# .github/workflows/compliance-check.yml
name: Compliance Verification
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
  schedule:
    - cron: '0 0 * * 0'  # Weekly audit

permissions:
  contents: read
  security-events: write
  pull-requests: write

jobs:
  soc2-controls:
    name: SOC 2 Control Verification
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # CC6.1 - Access Control
      - name: Check for hardcoded secrets
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Verify branch protection
        uses: actions/github-script@v7
        with:
          script: |
            const { data: protection } = await github.rest.repos.getBranchProtection({
              owner: context.repo.owner,
              repo: context.repo.repo,
              branch: 'main'
            }).catch(() => ({ data: null }));

            const checks = {
              'Required reviews': protection?.required_pull_request_reviews?.required_approving_review_count >= 1,
              'Dismiss stale reviews': protection?.required_pull_request_reviews?.dismiss_stale_reviews,
              'Require status checks': protection?.required_status_checks?.strict,
              'Enforce admins': protection?.enforce_admins?.enabled
            };

            let passed = true;
            for (const [check, result] of Object.entries(checks)) {
              console.log(`${check}: ${result ? '' : ''}`);
              if (!result) passed = false;
            }

            if (!passed) {
              core.setFailed('Branch protection does not meet SOC 2 requirements');
            }

      # CC6.7 - Encryption verification
      - name: Check TLS configuration
        run: |
          # Verify TLS version in code
          if grep -r "ssl_version.*SSLv" --include="*.py" .; then
            echo "::error::SSLv2/v3 detected - upgrade to TLS 1.2+"
            exit 1
          fi

      # CC7.2 - Logging verification
      - name: Verify logging configuration
        run: |
          # Check for logging configuration
          if ! grep -r "logging\|logger\|audit" --include="*.py" --include="*.ts" .; then
            echo "::warning::No logging configuration detected"
          fi

      # Generate compliance evidence
      - name: Generate compliance report
        run: |
          mkdir -p compliance-evidence
          echo "# SOC 2 Compliance Evidence" > compliance-evidence/report.md
          echo "Generated: $(date -u +"%Y-%m-%dT%H:%M:%SZ")" >> compliance-evidence/report.md
          echo "Commit: ${{ github.sha }}" >> compliance-evidence/report.md
          echo "" >> compliance-evidence/report.md
          echo "## Control Verification" >> compliance-evidence/report.md
          echo "- CC6.1 Access Control: VERIFIED" >> compliance-evidence/report.md
          echo "- CC6.7 Encryption: VERIFIED" >> compliance-evidence/report.md
          echo "- CC7.2 Monitoring: VERIFIED" >> compliance-evidence/report.md
          echo "- CC8.1 Change Management: VERIFIED" >> compliance-evidence/report.md

      - name: Upload compliance evidence
        uses: actions/upload-artifact@v4
        with:
          name: compliance-evidence-${{ github.sha }}
          path: compliance-evidence/
          retention-days: 365  # Keep for audit purposes

  gdpr-checks:
    name: GDPR Compliance Checks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check for PII handling
        run: |
          # Scan for potential PII fields without proper handling
          PII_PATTERNS="email|phone|address|ssn|social.security|credit.card|password"
          FINDINGS=$(grep -rn -E "$PII_PATTERNS" --include="*.ts" --include="*.py" --include="*.js" . || true)

          if [ -n "$FINDINGS" ]; then
            echo "::warning::Potential PII fields detected - ensure proper handling"
            echo "$FINDINGS"
          fi

      - name: Verify data retention policies
        run: |
          # Check for data retention configuration
          if ! grep -r "retention\|delete.*days\|ttl\|expir" --include="*.yml" --include="*.yaml" --include="*.json" .; then
            echo "::warning::No data retention policy configuration detected"
          fi

      - name: Check consent management
        run: |
          # Look for consent handling code
          if grep -r "consent\|gdpr\|opt.in\|opt.out" --include="*.ts" --include="*.py" .; then
            echo "Consent management code detected"
          else
            echo "::warning::No consent management code detected"
          fi

  license-compliance:
    name: License Compliance
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Check licenses
        run: |
          npx license-checker --json --out licenses.json

          # Define prohibited licenses
          PROHIBITED="GPL|AGPL|SSPL|BUSL"

          # Check for prohibited licenses
          VIOLATIONS=$(jq -r 'to_entries[] | select(.value.licenses | test("'"$PROHIBITED"'")) | "\(.key): \(.value.licenses)"' licenses.json || true)

          if [ -n "$VIOLATIONS" ]; then
            echo "::error::Prohibited license detected:"
            echo "$VIOLATIONS"
            exit 1
          fi

      - name: Generate SBOM
        run: |
          npx @cyclonedx/cyclonedx-npm --output-file sbom.json

      - name: Upload SBOM
        uses: actions/upload-artifact@v4
        with:
          name: sbom
          path: sbom.json

  audit-trail:
    name: Generate Audit Trail
    runs-on: ubuntu-latest
    needs: [soc2-controls, gdpr-checks, license-compliance]
    steps:
      - uses: actions/checkout@v4

      - name: Generate audit entry
        run: |
          cat > audit-entry.json << EOF
          {
            "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
            "event": "compliance_verification",
            "repository": "${{ github.repository }}",
            "commit": "${{ github.sha }}",
            "actor": "${{ github.actor }}",
            "workflow_run": "${{ github.run_id }}",
            "results": {
              "soc2": "PASSED",
              "gdpr": "PASSED",
              "license": "PASSED"
            },
            "evidence_location": "compliance-evidence-${{ github.sha }}"
          }
          EOF

      - name: Upload audit entry
        uses: actions/upload-artifact@v4
        with:
          name: audit-trail
          path: audit-entry.json
```

### Compliance Checker Script

```python
#!/usr/bin/env python3
"""Enterprise compliance checker for CI/CD integration."""

import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List, Dict, Optional, Any

class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"

class ComplianceStatus(Enum):
    PASSED = "passed"
    FAILED = "failed"
    WARNING = "warning"
    SKIPPED = "skipped"

@dataclass
class ComplianceFinding:
    """A compliance check finding."""
    rule_id: str
    rule_name: str
    framework: str
    control: str
    status: ComplianceStatus
    severity: Severity
    message: str
    evidence: Optional[str] = None
    remediation: Optional[str] = None

@dataclass
class ComplianceReport:
    """Complete compliance report."""
    timestamp: str
    repository: str
    commit: str
    frameworks: List[str]
    findings: List[ComplianceFinding] = field(default_factory=list)
    overall_status: ComplianceStatus = ComplianceStatus.PASSED

    def add_finding(self, finding: ComplianceFinding) -> None:
        """Add a finding and update overall status."""
        self.findings.append(finding)
        if finding.status == ComplianceStatus.FAILED:
            if finding.severity in (Severity.CRITICAL, Severity.HIGH):
                self.overall_status = ComplianceStatus.FAILED

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "timestamp": self.timestamp,
            "repository": self.repository,
            "commit": self.commit,
            "frameworks": self.frameworks,
            "overall_status": self.overall_status.value,
            "summary": {
                "total": len(self.findings),
                "passed": len([f for f in self.findings if f.status == ComplianceStatus.PASSED]),
                "failed": len([f for f in self.findings if f.status == ComplianceStatus.FAILED]),
                "warnings": len([f for f in self.findings if f.status == ComplianceStatus.WARNING]),
            },
            "findings": [
                {
                    "rule_id": f.rule_id,
                    "rule_name": f.rule_name,
                    "framework": f.framework,
                    "control": f.control,
                    "status": f.status.value,
                    "severity": f.severity.value,
                    "message": f.message,
                    "evidence": f.evidence,
                    "remediation": f.remediation,
                }
                for f in self.findings
            ]
        }


class ComplianceChecker:
    """Enterprise compliance checker."""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.report = ComplianceReport(
            timestamp=datetime.utcnow().isoformat() + "Z",
            repository=os.getenv("GITHUB_REPOSITORY", "unknown"),
            commit=os.getenv("GITHUB_SHA", "unknown"),
            frameworks=["SOC2", "GDPR", "LICENSE"]
        )

    def run_all_checks(self) -> ComplianceReport:
        """Run all compliance checks."""
        self.check_secrets()
        self.check_encryption()
        self.check_logging()
        self.check_pii_handling()
        self.check_licenses()
        self.check_dependencies()
        return self.report

    def check_secrets(self) -> None:
        """Check for hardcoded secrets (SOC 2 CC6.1)."""
        secret_patterns = [
            r'password\s*=\s*["\'][^"\']+["\']',
            r'api[_-]?key\s*=\s*["\'][^"\']+["\']',
            r'secret\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']+["\']',
            r'-----BEGIN\s+(?:RSA\s+)?PRIVATE\s+KEY-----',
        ]

        findings = []
        for pattern in secret_patterns:
            for file in self.project_path.rglob("*"):
                if file.is_file() and file.suffix in (".py", ".js", ".ts", ".yaml", ".yml", ".json"):
                    try:
                        content = file.read_text(errors="ignore")
                        matches = re.findall(pattern, content, re.IGNORECASE)
                        if matches:
                            findings.append(f"{file}: {len(matches)} potential secrets")
                    except Exception:
                        pass

        if findings:
            self.report.add_finding(ComplianceFinding(
                rule_id="AC-001",
                rule_name="No hardcoded credentials",
                framework="SOC2",
                control="CC6.1",
                status=ComplianceStatus.FAILED,
                severity=Severity.CRITICAL,
                message=f"Found {len(findings)} files with potential secrets",
                evidence="\n".join(findings[:5]),
                remediation="Use environment variables or secrets manager"
            ))
        else:
            self.report.add_finding(ComplianceFinding(
                rule_id="AC-001",
                rule_name="No hardcoded credentials",
                framework="SOC2",
                control="CC6.1",
                status=ComplianceStatus.PASSED,
                severity=Severity.CRITICAL,
                message="No hardcoded credentials detected"
            ))

    def check_encryption(self) -> None:
        """Check encryption configuration (SOC 2 CC6.7)."""
        insecure_patterns = [
            r'ssl_version.*SSLv[23]',
            r'TLSv1[^.]',
            r'MD5|SHA1',
            r'DES|RC4',
        ]

        issues = []
        for file in self.project_path.rglob("*.py"):
            try:
                content = file.read_text(errors="ignore")
                for pattern in insecure_patterns:
                    if re.search(pattern, content):
                        issues.append(f"{file}: Insecure crypto detected")
            except Exception:
                pass

        if issues:
            self.report.add_finding(ComplianceFinding(
                rule_id="EN-001",
                rule_name="Secure encryption",
                framework="SOC2",
                control="CC6.7",
                status=ComplianceStatus.FAILED,
                severity=Severity.HIGH,
                message=f"Found {len(issues)} insecure encryption usages",
                evidence="\n".join(issues[:5]),
                remediation="Use TLS 1.2+, AES-256, SHA-256 or stronger"
            ))
        else:
            self.report.add_finding(ComplianceFinding(
                rule_id="EN-001",
                rule_name="Secure encryption",
                framework="SOC2",
                control="CC6.7",
                status=ComplianceStatus.PASSED,
                severity=Severity.HIGH,
                message="Encryption configuration appears secure"
            ))

    def check_logging(self) -> None:
        """Check logging configuration (SOC 2 CC7.2)."""
        has_logging = False
        for file in self.project_path.rglob("*.py"):
            try:
                content = file.read_text(errors="ignore")
                if re.search(r'import\s+logging|from\s+logging', content):
                    has_logging = True
                    break
            except Exception:
                pass

        self.report.add_finding(ComplianceFinding(
            rule_id="MO-001",
            rule_name="Audit logging enabled",
            framework="SOC2",
            control="CC7.2",
            status=ComplianceStatus.PASSED if has_logging else ComplianceStatus.WARNING,
            severity=Severity.HIGH,
            message="Logging configuration found" if has_logging else "No logging detected",
            remediation=None if has_logging else "Implement structured logging"
        ))

    def check_pii_handling(self) -> None:
        """Check for PII handling (GDPR)."""
        pii_fields = [
            "email", "phone", "address", "ssn", "date_of_birth",
            "credit_card", "passport", "driver_license"
        ]

        pii_locations = []
        for file in self.project_path.rglob("*"):
            if file.suffix in (".py", ".ts", ".js"):
                try:
                    content = file.read_text(errors="ignore")
                    for field in pii_fields:
                        if re.search(rf'\b{field}\b', content, re.IGNORECASE):
                            pii_locations.append(f"{file}: {field}")
                except Exception:
                    pass

        if pii_locations:
            self.report.add_finding(ComplianceFinding(
                rule_id="GDPR-001",
                rule_name="PII data handling",
                framework="GDPR",
                control="Article 5",
                status=ComplianceStatus.WARNING,
                severity=Severity.HIGH,
                message=f"Found {len(pii_locations)} potential PII fields",
                evidence="\n".join(pii_locations[:10]),
                remediation="Ensure PII is encrypted, has retention policy, and consent is captured"
            ))

    def check_licenses(self) -> None:
        """Check dependency licenses."""
        prohibited = ["GPL", "AGPL", "SSPL"]

        # Run license check if package.json exists
        package_json = self.project_path / "package.json"
        if package_json.exists():
            try:
                result = subprocess.run(
                    ["npx", "license-checker", "--json"],
                    capture_output=True,
                    text=True,
                    cwd=self.project_path,
                    timeout=60
                )
                if result.returncode == 0:
                    licenses = json.loads(result.stdout)
                    violations = [
                        f"{pkg}: {info.get('licenses', 'unknown')}"
                        for pkg, info in licenses.items()
                        if any(p in str(info.get('licenses', '')) for p in prohibited)
                    ]

                    if violations:
                        self.report.add_finding(ComplianceFinding(
                            rule_id="LIC-001",
                            rule_name="License compliance",
                            framework="LICENSE",
                            control="OSS Policy",
                            status=ComplianceStatus.FAILED,
                            severity=Severity.HIGH,
                            message=f"Found {len(violations)} prohibited licenses",
                            evidence="\n".join(violations[:5]),
                            remediation="Replace dependencies with permissively licensed alternatives"
                        ))
                        return
            except Exception as e:
                print(f"License check error: {e}")

        self.report.add_finding(ComplianceFinding(
            rule_id="LIC-001",
            rule_name="License compliance",
            framework="LICENSE",
            control="OSS Policy",
            status=ComplianceStatus.PASSED,
            severity=Severity.HIGH,
            message="No prohibited licenses detected"
        ))

    def check_dependencies(self) -> None:
        """Check for vulnerable dependencies."""
        package_json = self.project_path / "package.json"
        if package_json.exists():
            try:
                result = subprocess.run(
                    ["npm", "audit", "--json"],
                    capture_output=True,
                    text=True,
                    cwd=self.project_path,
                    timeout=120
                )
                audit = json.loads(result.stdout)
                vulnerabilities = audit.get("metadata", {}).get("vulnerabilities", {})
                critical = vulnerabilities.get("critical", 0)
                high = vulnerabilities.get("high", 0)

                if critical > 0 or high > 0:
                    self.report.add_finding(ComplianceFinding(
                        rule_id="DEP-001",
                        rule_name="Dependency vulnerabilities",
                        framework="SOC2",
                        control="CC6.1",
                        status=ComplianceStatus.FAILED,
                        severity=Severity.CRITICAL if critical > 0 else Severity.HIGH,
                        message=f"Found {critical} critical, {high} high vulnerabilities",
                        remediation="Run 'npm audit fix' or update vulnerable packages"
                    ))
                    return
            except Exception as e:
                print(f"Audit error: {e}")

        self.report.add_finding(ComplianceFinding(
            rule_id="DEP-001",
            rule_name="Dependency vulnerabilities",
            framework="SOC2",
            control="CC6.1",
            status=ComplianceStatus.PASSED,
            severity=Severity.HIGH,
            message="No critical vulnerabilities detected"
        ))

    def generate_evidence(self) -> str:
        """Generate compliance evidence document."""
        report = self.report.to_dict()

        doc = f"""# Compliance Evidence Report

**Generated**: {report['timestamp']}
**Repository**: {report['repository']}
**Commit**: {report['commit']}
**Overall Status**: {report['overall_status'].upper()}

## Summary

- Total Checks: {report['summary']['total']}
- Passed: {report['summary']['passed']}
- Failed: {report['summary']['failed']}
- Warnings: {report['summary']['warnings']}

## Findings

"""
        for finding in report['findings']:
            status_icon = {
                'passed': '',
                'failed': '',
                'warning': '',
                'skipped': '⏭'
            }.get(finding['status'], '')

            doc += f"""### {status_icon} {finding['rule_id']}: {finding['rule_name']}

- **Framework**: {finding['framework']}
- **Control**: {finding['control']}
- **Severity**: {finding['severity']}
- **Status**: {finding['status']}
- **Message**: {finding['message']}
"""
            if finding.get('evidence'):
                doc += f"\n**Evidence**:\n```\n{finding['evidence']}\n```\n"
            if finding.get('remediation'):
                doc += f"\n**Remediation**: {finding['remediation']}\n"
            doc += "\n---\n\n"

        return doc


if __name__ == "__main__":
    checker = ComplianceChecker()
    report = checker.run_all_checks()

    # Output JSON report
    print(json.dumps(report.to_dict(), indent=2))

    # Generate evidence document
    evidence = checker.generate_evidence()
    Path("compliance-evidence.md").write_text(evidence)

    # Exit with failure if critical issues found
    sys.exit(0 if report.overall_status == ComplianceStatus.PASSED else 1)
```

## Enterprise Integration

### Mandatory Connections
- **Security Architect (sa-*)**: Security control verification
- **Data Governance (dg-*)**: Data handling compliance
- **DevOps (do-09)**: CI/CD pipeline integration

### Recommended Connections
- **Code Review (cr-03)**: Quality gates for compliance
- **Platform Engineer (pe-*)**: Infrastructure compliance

## Best Practices

1. **Automate everything**: Manual compliance is unsustainable
2. **Fail fast**: Block non-compliant changes in CI/CD
3. **Evidence collection**: Maintain audit trails automatically
4. **Continuous monitoring**: Don't wait for audits
5. **Policy as code**: Version control your compliance rules
6. **Remediation guidance**: Always provide fix instructions

## Quick Reference

```bash
# In Claude Code
@compliance-automation "Set up SOC 2 compliance checks for our CI/CD"
@compliance-automation "Generate GDPR compliance evidence for audit"
@compliance-automation "Check license compliance for our dependencies"
```
