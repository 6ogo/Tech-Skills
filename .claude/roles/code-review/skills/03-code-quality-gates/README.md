# cr-03: Code Quality Gates

Enforce quality standards with branch protection, required checks, and merge policies.

## Overview

Quality gates are automated checkpoints that code must pass before merging. They ensure consistent standards, prevent regressions, and protect production branches from unsafe changes.

## Capabilities

### Branch Protection
- Protected branch configuration
- Required status checks
- Required reviewers
- Signed commits enforcement
- Linear history requirement

### Merge Policies
- Squash and merge only
- Require up-to-date branches
- Auto-merge when checks pass
- Merge queue management

### Quality Thresholds
- Code coverage minimums
- Complexity limits
- Security vulnerability blocks
- Performance regression detection

## Implementation

### GitHub Branch Protection (via API)

```bash
#!/bin/bash
# setup-branch-protection.sh

OWNER="your-org"
REPO="your-repo"
BRANCH="main"

gh api repos/${OWNER}/${REPO}/branches/${BRANCH}/protection -X PUT \
  -H "Accept: application/vnd.github+json" \
  --input - << EOF
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "build",
      "test",
      "lint",
      "security-scan",
      "coverage"
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismissal_restrictions": {
      "users": [],
      "teams": ["security-team"]
    },
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "required_approving_review_count": 2,
    "require_last_push_approval": true
  },
  "restrictions": null,
  "required_linear_history": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_conversation_resolution": true,
  "required_signatures": true
}
EOF

echo "Branch protection configured for ${BRANCH}"
```

### Quality Gate Workflow

```yaml
# .github/workflows/quality-gates.yml
name: Quality Gates
on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main, develop]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  # Gate 1: Build must succeed
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run build

  # Gate 2: All tests must pass
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm test -- --coverage
      - uses: actions/upload-artifact@v4
        with:
          name: coverage
          path: coverage/

  # Gate 3: Coverage threshold
  coverage:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: coverage
          path: coverage/

      - name: Check coverage threshold
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const coverage = JSON.parse(
              fs.readFileSync('coverage/coverage-summary.json')
            );

            const thresholds = {
              lines: 80,
              statements: 80,
              functions: 75,
              branches: 70
            };

            const total = coverage.total;
            const failures = [];

            for (const [metric, threshold] of Object.entries(thresholds)) {
              const actual = total[metric].pct;
              if (actual < threshold) {
                failures.push(
                  `${metric}: ${actual}% < ${threshold}% required`
                );
              }
            }

            if (failures.length > 0) {
              core.setFailed(
                `Coverage below threshold:\n${failures.join('\n')}`
              );
            } else {
              core.info('Coverage thresholds met');
            }

  # Gate 4: Linting
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint -- --max-warnings 0

  # Gate 5: Type checking
  typecheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run typecheck

  # Gate 6: Security scan
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Snyk
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high

      - name: Check for secrets
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  # Gate 7: Complexity check
  complexity:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci

      - name: Check complexity
        run: |
          npx es6-plato -r -d report src/
          MAX_COMPLEXITY=$(cat report/report.json | jq '[.reports[].complexity.cyclomatic] | max')
          if [ "$MAX_COMPLEXITY" -gt 15 ]; then
            echo "Cyclomatic complexity too high: $MAX_COMPLEXITY (max: 15)"
            exit 1
          fi

  # Final gate: All checks must pass
  quality-gate:
    needs: [build, test, coverage, lint, typecheck, security, complexity]
    runs-on: ubuntu-latest
    steps:
      - name: All gates passed
        run: echo "All quality gates passed successfully"
```

### Quality Gate Configuration

```yaml
# .quality-gates.yml
version: 1

gates:
  # Coverage requirements
  coverage:
    enabled: true
    thresholds:
      lines: 80
      statements: 80
      functions: 75
      branches: 70
    block_merge: true
    trend: "no_decrease"  # Coverage cannot decrease

  # Complexity limits
  complexity:
    enabled: true
    max_cyclomatic: 15
    max_cognitive: 20
    max_lines_per_function: 100
    max_parameters: 5
    block_merge: true

  # Security requirements
  security:
    enabled: true
    vulnerabilities:
      critical: 0      # No critical vulns allowed
      high: 0          # No high vulns allowed
      medium_max: 5    # Max 5 medium vulns
    secrets_detection: true
    sast_required: true
    block_merge: true

  # Code quality
  quality:
    enabled: true
    max_duplications: 3%
    max_code_smells: 10
    maintainability_rating: "A"  # SonarQube rating
    block_merge: true

  # Test requirements
  tests:
    enabled: true
    required: true
    minimum_pass_rate: 100
    new_code_coverage: 80
    block_merge: true

  # Documentation
  documentation:
    enabled: true
    require_pr_description: true
    require_changelog: true  # For releases
    block_merge: false  # Warning only

  # Performance (optional)
  performance:
    enabled: false
    max_bundle_increase: 5%  # KB
    max_response_time_increase: 10%  # ms
    block_merge: false

notifications:
  slack:
    channel: "#code-quality"
    on_failure: true
    on_success: false

  email:
    recipients: ["leads@company.com"]
    on_failure: true

exceptions:
  # Files/patterns excluded from quality checks
  exclude_patterns:
    - "**/*.test.ts"
    - "**/*.spec.ts"
    - "**/fixtures/**"
    - "**/mocks/**"
```

### Quality Gate Status Check

```python
#!/usr/bin/env python3
"""Quality gate status checker."""

import json
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum

class GateStatus(Enum):
    PASSED = "passed"
    FAILED = "failed"
    WARNING = "warning"
    SKIPPED = "skipped"

@dataclass
class GateResult:
    """Result of a quality gate check."""
    name: str
    status: GateStatus
    message: str
    details: Optional[Dict] = None
    blocking: bool = True

class QualityGateChecker:
    """Checks all quality gates and reports status."""

    def __init__(self, config_path: str = ".quality-gates.yml"):
        self.config = self._load_config(config_path)
        self.results: List[GateResult] = []

    def _load_config(self, path: str) -> Dict:
        """Load quality gate configuration."""
        import yaml
        with open(path) as f:
            return yaml.safe_load(f)

    def check_coverage(self, coverage_report: Dict) -> GateResult:
        """Check coverage thresholds."""
        config = self.config.get("gates", {}).get("coverage", {})
        if not config.get("enabled", True):
            return GateResult("coverage", GateStatus.SKIPPED, "Coverage check disabled")

        thresholds = config.get("thresholds", {})
        failures = []

        for metric, threshold in thresholds.items():
            actual = coverage_report.get("total", {}).get(metric, {}).get("pct", 0)
            if actual < threshold:
                failures.append(f"{metric}: {actual}% < {threshold}%")

        if failures:
            return GateResult(
                "coverage",
                GateStatus.FAILED,
                f"Coverage below threshold: {', '.join(failures)}",
                {"failures": failures},
                blocking=config.get("block_merge", True)
            )

        return GateResult("coverage", GateStatus.PASSED, "Coverage thresholds met")

    def check_security(self, scan_results: Dict) -> GateResult:
        """Check security scan results."""
        config = self.config.get("gates", {}).get("security", {})
        if not config.get("enabled", True):
            return GateResult("security", GateStatus.SKIPPED, "Security check disabled")

        vuln_config = config.get("vulnerabilities", {})
        vulns = scan_results.get("vulnerabilities", {})

        failures = []

        if vulns.get("critical", 0) > vuln_config.get("critical", 0):
            failures.append(f"Critical vulnerabilities: {vulns['critical']}")

        if vulns.get("high", 0) > vuln_config.get("high", 0):
            failures.append(f"High vulnerabilities: {vulns['high']}")

        if vulns.get("medium", 0) > vuln_config.get("medium_max", 999):
            failures.append(f"Too many medium vulnerabilities: {vulns['medium']}")

        if failures:
            return GateResult(
                "security",
                GateStatus.FAILED,
                f"Security issues found: {', '.join(failures)}",
                {"vulnerabilities": vulns},
                blocking=True  # Security always blocks
            )

        return GateResult("security", GateStatus.PASSED, "No security issues")

    def check_complexity(self, complexity_report: Dict) -> GateResult:
        """Check code complexity."""
        config = self.config.get("gates", {}).get("complexity", {})
        if not config.get("enabled", True):
            return GateResult("complexity", GateStatus.SKIPPED, "Complexity check disabled")

        max_cyclomatic = config.get("max_cyclomatic", 15)
        actual_max = complexity_report.get("max_cyclomatic", 0)

        if actual_max > max_cyclomatic:
            return GateResult(
                "complexity",
                GateStatus.FAILED,
                f"Cyclomatic complexity {actual_max} exceeds max {max_cyclomatic}",
                {"max_found": actual_max, "threshold": max_cyclomatic},
                blocking=config.get("block_merge", True)
            )

        return GateResult("complexity", GateStatus.PASSED, "Complexity within limits")

    def check_all(self, reports: Dict) -> bool:
        """Run all quality gate checks."""
        self.results = [
            self.check_coverage(reports.get("coverage", {})),
            self.check_security(reports.get("security", {})),
            self.check_complexity(reports.get("complexity", {})),
        ]

        blocking_failures = [r for r in self.results
                           if r.status == GateStatus.FAILED and r.blocking]

        return len(blocking_failures) == 0

    def generate_report(self) -> str:
        """Generate markdown report."""
        report = "## Quality Gate Results\n\n"

        status_icons = {
            GateStatus.PASSED: "",
            GateStatus.FAILED: "",
            GateStatus.WARNING: "",
            GateStatus.SKIPPED: ""
        }

        for result in self.results:
            icon = status_icons[result.status]
            report += f"- {icon} **{result.name}**: {result.message}\n"

        passed = all(r.status in (GateStatus.PASSED, GateStatus.SKIPPED, GateStatus.WARNING)
                    or not r.blocking for r in self.results)

        report += f"\n**Overall**: {'PASSED' if passed else 'FAILED'}\n"

        return report


if __name__ == "__main__":
    checker = QualityGateChecker()

    # Example reports (would come from actual tools)
    reports = {
        "coverage": {"total": {"lines": {"pct": 85}, "branches": {"pct": 72}}},
        "security": {"vulnerabilities": {"critical": 0, "high": 0, "medium": 2}},
        "complexity": {"max_cyclomatic": 12}
    }

    passed = checker.check_all(reports)
    print(checker.generate_report())
    sys.exit(0 if passed else 1)
```

## Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| Gate pass rate | > 95% | PRs passing first time |
| False positive rate | < 5% | Incorrect failures |
| Gate execution time | < 10 min | Total check time |
| Bypass rate | 0% | No bypasses allowed |

## Connections

- **Inputs from**: Automated review (cr-01), PR workflow (cr-02)
- **Outputs to**: Merge decision, analytics (cr-05)
- **Integrates with**: Security (sa-05), DevOps (do-01)

## Best Practices

1. Start with lenient thresholds, tighten gradually
2. Never allow bypasses for security gates
3. Keep gate execution fast (< 10 minutes)
4. Provide clear failure messages with fix guidance
5. Track gate failures to identify common issues
6. Review and update thresholds quarterly
