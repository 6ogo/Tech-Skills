# Project Guardian - Health & Improvement Agent

Comprehensive project health monitoring, dependency management, technical debt analysis, and continuous improvement recommendations.

## Role Overview

**Agent**: Project Guardian
**Focus**: Project health monitoring, dependency security, technical debt tracking, continuous improvement
**Skills**: 5 specialized skills (pg-01 to pg-05)

## When to Use

Invoke this role when you need to:

- Assess overall project health and quality
- Scan dependencies for vulnerabilities
- Analyze and quantify technical debt
- Get improvement recommendations
- Evaluate security posture
- Plan maintenance activities

## Skills

| ID    | Skill                      | Description                                     |
| ----- | -------------------------- | ----------------------------------------------- |
| pg-01 | Project Health Check       | Comprehensive health assessment with scoring    |
| pg-02 | Dependency Management      | Vulnerability scanning, outdated detection      |
| pg-03 | Technical Debt Analysis    | Debt quantification, refactoring opportunities  |
| pg-04 | Continuous Improvement     | Performance, scalability, best practice recs    |
| pg-05 | Security Posture Assessment| Security audit, OWASP compliance, secrets check |

## Enterprise Integration

### Mandatory Connections

- **Security Architect (sa-01 to sa-07)**: Security posture details
- **DevOps (do-08, do-09)**: CI/CD and monitoring health
- **Code Review (cr-03)**: Quality gate status

### Recommended Connections

- **FinOps (fo-01)**: Cost optimization opportunities
- **Platform Engineer (pe-03)**: SLO/SLI health metrics
- **Data Governance (dg-03)**: Data quality health

## Quick Start

```bash
# Full project health assessment
@project-guardian "Run comprehensive health check and provide improvement roadmap"

# Individual skill usage
@project-guardian pg-01 "Assess project health with detailed scoring"
@project-guardian pg-02 "Scan all dependencies for vulnerabilities and updates"
@project-guardian pg-03 "Analyze technical debt and prioritize fixes"
@project-guardian pg-04 "Suggest improvements for performance and reliability"
@project-guardian pg-05 "Evaluate security posture and compliance"
```

## Skill Details

### pg-01: Project Health Check

**Purpose**: Comprehensive project health assessment with actionable scoring

**Capabilities**:

- Overall health score calculation (0-100)
- Code quality metrics aggregation
- Test coverage analysis
- Documentation completeness check
- Build and CI/CD health status
- Trend analysis over time

**Health Score Components**:

| Component         | Weight | Excellent | Good  | Fair  | Poor  |
| ----------------- | ------ | --------- | ----- | ----- | ----- |
| Code Quality      | 25%    | A         | B     | C     | D/F   |
| Test Coverage     | 20%    | >80%      | >60%  | >40%  | <40%  |
| Dependency Health | 20%    | 0 vulns   | <3    | <10   | 10+   |
| Security Posture  | 20%    | A         | B     | C     | D/F   |
| Documentation     | 10%    | Complete  | Good  | Partial | Missing |
| CI/CD Health      | 5%     | Green     | Yellow | Red   | None  |

**Output Example**:

```markdown
## Project Health Report

**Overall Score**: 78/100 (Grade: C+)
**Trend**: +5 from last check

### Component Scores

- Code Quality: 82/100 (B)
- Test Coverage: 65% (C)
- Dependencies: 90/100 (A) - 2 medium vulns
- Security: 75/100 (C) - secrets exposure detected
- Documentation: 60/100 (D) - API docs incomplete
- CI/CD: 95/100 (A) - all pipelines green

### Priority Actions

1. [CRITICAL] Rotate exposed secrets (security)
2. [HIGH] Increase test coverage to 80%
3. [MEDIUM] Complete API documentation
4. [LOW] Update 5 outdated dependencies
```

---

### pg-02: Dependency Management

**Purpose**: Comprehensive dependency security and health management

**Capabilities**:

- Multi-ecosystem vulnerability scanning (npm, pip, cargo, go, maven)
- Outdated package detection with update recommendations
- License compliance checking
- Supply chain security analysis
- Breaking change detection for updates
- Automated update PRs preparation

**Supported Package Managers**:

- **JavaScript/TypeScript**: npm, yarn, pnpm
- **Python**: pip, poetry, pipenv
- **Rust**: cargo
- **Go**: go mod
- **Java**: maven, gradle
- **Ruby**: bundler
- **PHP**: composer
- **.NET**: nuget

**GitHub Actions Integration**:

```yaml
name: Dependency Health
on:
  schedule:
    - cron: "0 6 * * 1" # Weekly Monday 6 AM
  workflow_dispatch:

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Dependency Vulnerability Scan
        run: |
          npm audit --json > npm-audit.json || true
          pip-audit --format json > pip-audit.json || true
      - name: Check Outdated
        run: |
          npm outdated --json > npm-outdated.json || true
          pip list --outdated --format json > pip-outdated.json || true
      - name: Generate Report
        run: python scripts/dependency_report.py
      - name: Create Issue
        if: failure()
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: 'Dependency Health Alert',
              body: 'Vulnerabilities detected. See workflow run for details.'
            })
```

---

### pg-03: Technical Debt Analysis

**Purpose**: Quantify, prioritize, and plan technical debt remediation

**Capabilities**:

- Code complexity analysis (cyclomatic, cognitive complexity)
- Duplicate code detection and grouping
- Dead code identification
- Anti-pattern detection
- Debt effort estimation in hours
- Priority-based remediation roadmap
- Trend tracking over time

**Debt Categories**:

| Priority | Category          | Examples                          |
| -------- | ----------------- | --------------------------------- |
| Critical | Security Debt     | Vulnerabilities, exposed secrets  |
| High     | Architecture Debt | Tight coupling, circular deps     |
| Medium   | Code Debt         | High complexity, duplication      |
| Medium   | Test Debt         | Low coverage, flaky tests         |
| Low      | Documentation     | Missing docs, outdated comments   |

**Debt Quantification Output**:

```markdown
## Technical Debt Report

**Total Debt**: ~45 hours of remediation work
**Debt Ratio**: 12% (debt hours / feature hours)

### By Priority

| Priority | Items | Hours | % of Total |
| -------- | ----- | ----- | ---------- |
| Critical | 2     | 4h    | 9%         |
| High     | 5     | 15h   | 33%        |
| Medium   | 12    | 20h   | 45%        |
| Low      | 8     | 6h    | 13%        |

### Top 5 Items to Address

1. **[Critical]** SQL injection in user input handler (2h)
   - Location: src/api/users.py:145
   - Fix: Parameterize queries

2. **[High]** Circular dependency between modules (4h)
   - Location: src/services/auth <-> src/services/user
   - Fix: Extract shared interface

3. **[High]** Function with complexity 35 (2h)
   - Location: src/utils/parser.js:89
   - Fix: Extract helper functions

...
```

---

### pg-04: Continuous Improvement

**Purpose**: Identify and recommend improvements for project strengthening

**Capabilities**:

- Performance bottleneck identification
- Scalability recommendations
- Best practice enforcement suggestions
- Architecture improvement opportunities
- Developer experience enhancements
- Automation opportunity detection
- Modern pattern adoption suggestions

**Improvement Categories**:

| Category    | Focus Area                                         |
| ----------- | -------------------------------------------------- |
| Performance | Query optimization, caching, lazy loading          |
| Scalability | Horizontal scaling, async processing, CDN          |
| Reliability | Error handling, retry logic, circuit breakers      |
| Security    | Input validation, output encoding, auth hardening  |
| DevEx       | Tooling, docs, onboarding, local dev experience    |
| Automation  | CI/CD, testing, deployment, monitoring             |

---

### pg-05: Security Posture Assessment

**Purpose**: Comprehensive security evaluation and compliance checking

**Capabilities**:

- Security configuration audit
- Secrets exposure detection
- Access control review
- Security header validation
- OWASP Top 10 compliance check
- Security score calculation
- Remediation prioritization

**Security Score Components**:

| Component              | Weight | Checks                                |
| ---------------------- | ------ | ------------------------------------- |
| Secrets Management     | 25%    | No hardcoded secrets, vault usage     |
| Input Validation       | 20%    | Sanitization, parameterized queries   |
| Authentication         | 20%    | Strong auth, session management       |
| Authorization          | 15%    | RBAC, least privilege                 |
| Security Headers       | 10%    | CSP, HSTS, X-Frame-Options            |
| Dependency Security    | 10%    | No known vulnerabilities              |

---

## Enterprise Workflow

### Monthly Maintenance Cycle

```
Week 1: Health Check (pg-01)
  ↓
Identify priorities and create improvement tickets
  ↓
Week 2: Dependency Updates (pg-02)
  ↓
Update non-breaking dependencies, plan major updates
  ↓
Week 3: Debt Paydown (pg-03)
  ↓
Address 2-3 high-priority debt items
  ↓
Week 4: Security Review (pg-05)
  ↓
Address any security findings, rotate credentials
```

### Integration with CI/CD

Add Project Guardian checks to your pipeline:

```yaml
# .github/workflows/project-health.yml
name: Project Health Gate
on: [pull_request]

jobs:
  health-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Code quality check
      - name: Lint & Complexity
        run: |
          npm run lint
          npx complexity-report --format json src/

      # Dependency check
      - name: Security Scan
        run: npm audit --audit-level=high

      # Test coverage
      - name: Tests with Coverage
        run: npm test -- --coverage --coverageThreshold='{"global":{"lines":70}}'

      # Block if health score below threshold
      - name: Health Gate
        run: |
          if [ $HEALTH_SCORE -lt 70 ]; then
            echo "Health score $HEALTH_SCORE below threshold 70"
            exit 1
          fi
```

---

## Integration with Other Skills

| Skill                | Integration                           |
| -------------------- | ------------------------------------- |
| @security-architect  | Detailed security findings            |
| @devops do-08        | Monitoring and observability health   |
| @code-review cr-03   | Quality gate enforcement              |
| @finops fo-01        | Cost optimization in improvements     |
| @maintenance-engineer| Remediation execution                 |

---

## Best Practices

1. **Regular cadence**: Run health checks at least weekly
2. **Trend over snapshots**: Track scores over time, not just current state
3. **Prioritize ruthlessly**: Focus on critical/high items first
4. **Automate detection**: Integrate into CI/CD for continuous monitoring
5. **Budget for maintenance**: Allocate 15-20% of sprint for health work
6. **Celebrate improvements**: Track and share health score improvements

---

## Quick Reference

```bash
# Comprehensive project analysis
@project-guardian "Full health assessment with improvement roadmap"

# Specific checks
@project-guardian pg-01 "Health score with trend analysis"
@project-guardian pg-02 "Dependency security scan"
@project-guardian pg-03 "Technical debt quantification"
@project-guardian pg-04 "Improvement recommendations"
@project-guardian pg-05 "Security posture audit"

# Combined workflows
@project-guardian "Pre-release health gate check"
@project-guardian "Monthly maintenance report"
```
