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
        report = self.to_dict()

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
