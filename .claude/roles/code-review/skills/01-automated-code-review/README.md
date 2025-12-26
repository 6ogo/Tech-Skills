# cr-01: Automated Code Review

AI-powered automated code analysis for consistent quality enforcement.

## Overview

Automated code review integrates static analysis, security scanning, and AI-powered suggestions to catch issues before human review. This reduces review burden and ensures consistent quality standards.

## Capabilities

### Static Analysis
- **Linting**: ESLint, Pylint, RuboCop, golangci-lint
- **Formatting**: Prettier, Black, gofmt
- **Type checking**: TypeScript, mypy, Pyright
- **Complexity**: Cyclomatic, cognitive complexity metrics

### Security Scanning
- **SAST**: SonarQube, Semgrep, CodeQL
- **Dependency scanning**: Snyk, Dependabot, npm audit
- **Secret detection**: GitLeaks, TruffleHog
- **Container scanning**: Trivy, Grype

### AI-Powered Analysis
- Code suggestions and improvements
- Bug prediction and detection
- Performance anti-pattern identification
- Documentation gap detection

## Implementation

### GitHub Actions Workflow

```yaml
name: Automated Code Review
on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read
  pull-requests: write
  security-events: write

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run ESLint
        run: |
          npx eslint . --format=json --output-file=eslint-report.json || true

      - name: Annotate PR with ESLint results
        uses: ataylorme/eslint-annotate-action@v2
        with:
          report-json: "eslint-report.json"

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: p/security-audit p/secrets

      - name: Run Snyk
        uses: snyk/actions/node@master
        continue-on-error: true
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: snyk.sarif

  complexity:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check complexity
        run: |
          npx complexity-report --format json --output complexity.json src/

      - name: Comment complexity report
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const report = JSON.parse(fs.readFileSync('complexity.json'));
            const high = report.filter(f => f.complexity > 15);
            if (high.length > 0) {
              const body = '## Complexity Warning\n\n' +
                high.map(f => `- \`${f.file}\`: ${f.complexity}`).join('\n');
              github.rest.issues.createComment({
                issue_number: context.issue.number,
                owner: context.repo.owner,
                repo: context.repo.repo,
                body
              });
            }
```

### Azure DevOps Pipeline

```yaml
trigger: none
pr:
  branches:
    include:
      - main
      - develop

pool:
  vmImage: 'ubuntu-latest'

stages:
  - stage: AutomatedReview
    displayName: 'Automated Code Review'
    jobs:
      - job: StaticAnalysis
        displayName: 'Static Analysis'
        steps:
          - task: NodeTool@0
            inputs:
              versionSpec: '20.x'

          - script: npm ci
            displayName: 'Install dependencies'

          - script: |
              npx eslint . --format stylish --output-file $(Build.ArtifactStagingDirectory)/eslint.txt
            displayName: 'Run ESLint'
            continueOnError: true

          - task: PublishBuildArtifacts@1
            inputs:
              pathToPublish: '$(Build.ArtifactStagingDirectory)'
              artifactName: 'code-review'

      - job: SecurityScan
        displayName: 'Security Scanning'
        steps:
          - task: SonarQubePrepare@5
            inputs:
              SonarQube: 'SonarQube-Connection'
              scannerMode: 'CLI'
              configMode: 'manual'
              cliProjectKey: '$(Build.Repository.Name)'

          - task: SonarQubeAnalyze@5

          - task: SonarQubePublish@5
            inputs:
              pollingTimeoutSec: '300'

          - task: sonar-buildbreaker@8
            inputs:
              SonarQube: 'SonarQube-Connection'
```

### Python Analysis Script

```python
#!/usr/bin/env python3
"""Automated code review analyzer."""

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any

@dataclass
class ReviewFinding:
    """Represents a code review finding."""
    file: str
    line: int
    severity: str  # critical, high, medium, low, info
    category: str  # security, quality, performance, style
    message: str
    rule: str
    suggestion: str = ""

class AutomatedReviewer:
    """Enterprise automated code reviewer."""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.findings: List[ReviewFinding] = []

    def run_eslint(self) -> List[ReviewFinding]:
        """Run ESLint for JavaScript/TypeScript."""
        result = subprocess.run(
            ["npx", "eslint", ".", "--format=json"],
            capture_output=True,
            text=True,
            cwd=self.project_path
        )

        findings = []
        if result.stdout:
            data = json.loads(result.stdout)
            for file_result in data:
                for msg in file_result.get("messages", []):
                    findings.append(ReviewFinding(
                        file=file_result["filePath"],
                        line=msg.get("line", 0),
                        severity=self._map_severity(msg.get("severity", 1)),
                        category="style" if "style" in msg.get("ruleId", "") else "quality",
                        message=msg.get("message", ""),
                        rule=msg.get("ruleId", ""),
                        suggestion=msg.get("fix", {}).get("text", "") if msg.get("fix") else ""
                    ))
        return findings

    def run_semgrep(self) -> List[ReviewFinding]:
        """Run Semgrep for security analysis."""
        result = subprocess.run(
            ["semgrep", "--config=auto", "--json", "."],
            capture_output=True,
            text=True,
            cwd=self.project_path
        )

        findings = []
        if result.stdout:
            data = json.loads(result.stdout)
            for finding in data.get("results", []):
                findings.append(ReviewFinding(
                    file=finding["path"],
                    line=finding["start"]["line"],
                    severity=finding.get("extra", {}).get("severity", "medium"),
                    category="security",
                    message=finding["extra"].get("message", ""),
                    rule=finding["check_id"],
                    suggestion=finding.get("extra", {}).get("fix", "")
                ))
        return findings

    def run_complexity_check(self) -> List[ReviewFinding]:
        """Check code complexity."""
        # Implementation depends on language
        # This is a placeholder for complexity analysis
        return []

    def _map_severity(self, eslint_severity: int) -> str:
        """Map ESLint severity to standard levels."""
        return {1: "low", 2: "medium"}.get(eslint_severity, "info")

    def run_all_checks(self) -> Dict[str, Any]:
        """Run all automated checks."""
        self.findings.extend(self.run_eslint())
        self.findings.extend(self.run_semgrep())
        self.findings.extend(self.run_complexity_check())

        return {
            "total_findings": len(self.findings),
            "by_severity": self._count_by_severity(),
            "by_category": self._count_by_category(),
            "blocking": self._get_blocking_issues(),
            "findings": [f.__dict__ for f in self.findings]
        }

    def _count_by_severity(self) -> Dict[str, int]:
        """Count findings by severity."""
        counts = {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0}
        for f in self.findings:
            counts[f.severity] = counts.get(f.severity, 0) + 1
        return counts

    def _count_by_category(self) -> Dict[str, int]:
        """Count findings by category."""
        counts = {}
        for f in self.findings:
            counts[f.category] = counts.get(f.category, 0) + 1
        return counts

    def _get_blocking_issues(self) -> List[Dict]:
        """Get issues that should block merge."""
        blocking = [f for f in self.findings
                   if f.severity in ("critical", "high") or f.category == "security"]
        return [f.__dict__ for f in blocking]

    def generate_pr_comment(self) -> str:
        """Generate a PR comment with findings."""
        counts = self._count_by_severity()
        blocking = self._get_blocking_issues()

        comment = "## Automated Code Review Results\n\n"

        if blocking:
            comment += "### Blocking Issues\n"
            for issue in blocking[:10]:  # Limit to 10
                comment += f"- **{issue['severity'].upper()}** [{issue['rule']}] "
                comment += f"`{issue['file']}:{issue['line']}` - {issue['message']}\n"
            comment += "\n"

        comment += "### Summary\n"
        comment += f"- Critical: {counts['critical']}\n"
        comment += f"- High: {counts['high']}\n"
        comment += f"- Medium: {counts['medium']}\n"
        comment += f"- Low: {counts['low']}\n"

        if not blocking:
            comment += "\n All automated checks passed.\n"
        else:
            comment += "\n Please address blocking issues before merge.\n"

        return comment


if __name__ == "__main__":
    reviewer = AutomatedReviewer()
    results = reviewer.run_all_checks()
    print(json.dumps(results, indent=2))
```

## Configuration

### ESLint Configuration (.eslintrc.json)
```json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:security/recommended"
  ],
  "plugins": ["security", "@typescript-eslint"],
  "rules": {
    "complexity": ["error", 15],
    "max-depth": ["error", 4],
    "max-lines-per-function": ["error", 100],
    "no-eval": "error",
    "security/detect-eval-with-expression": "error",
    "security/detect-non-literal-regexp": "warn"
  }
}
```

### Semgrep Configuration (.semgrep.yml)
```yaml
rules:
  - id: hardcoded-secret
    patterns:
      - pattern-regex: (password|secret|key|token)\s*=\s*["'][^"']+["']
    message: "Potential hardcoded secret detected"
    severity: ERROR
    languages: [python, javascript, typescript]

  - id: sql-injection
    patterns:
      - pattern: $QUERY = "..." + $INPUT + "..."
      - pattern: f"SELECT ... {$INPUT} ..."
    message: "Potential SQL injection vulnerability"
    severity: ERROR
    languages: [python, javascript]
```

## Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| False positive rate | < 10% | Minimize noise |
| Detection rate | > 90% | Catch real issues |
| Scan time | < 5 min | Fast feedback |
| Coverage | 100% changed files | Review all changes |

## Connections

- **Inputs from**: Developer push, PR creation
- **Outputs to**: PR comments, quality gates (cr-03)
- **Integrates with**: Security Architect (sa-05), DevOps (do-09)

## Best Practices

1. Run automated checks on every push, not just PRs
2. Fix tool configuration issues quickly to maintain trust
3. Suppress false positives with inline comments, not config
4. Review and update rules quarterly
5. Track false positive rate and tune accordingly
