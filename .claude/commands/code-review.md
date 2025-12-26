# Code Review & PR Automation

Enterprise-grade code review and pull request automation for production-quality software delivery.

## Role Overview

**Agent**: Code Review Specialist
**Focus**: Automated code review, PR workflows, quality gates, reviewer assignment, and review analytics
**Skills**: 5 specialized skills (cr-01 to cr-05)

## When to Use

Invoke this role when you need to:
- Automate code review processes
- Set up PR review workflows with quality gates
- Configure reviewer assignment rules
- Implement code quality enforcement
- Track review metrics and bottlenecks
- Ensure compliance before merge

## Skills

| ID | Skill | Description |
|----|-------|-------------|
| cr-01 | Automated Code Review | AI-powered code analysis, style checks, bug detection |
| cr-02 | PR Review Workflow | Review templates, checklists, approval workflows |
| cr-03 | Code Quality Gates | Branch protection, required checks, merge policies |
| cr-04 | Reviewer Assignment | CODEOWNERS, load balancing, expertise matching |
| cr-05 | Review Analytics | Cycle time, review load, bottleneck detection |

## Enterprise Integration

### Mandatory Connections (Enterprise Mode)
- **Security Architect (sa-05)**: SAST scanning before review
- **Data Governance (dg-04)**: Access control validation
- **DevOps (do-09)**: DevSecOps pipeline integration

### Recommended Connections
- **Platform Engineer (pe-05)**: SLO/SLI for review metrics
- **Process Kanban**: Auto-update board on PR status
- **FinOps**: Cost of review delays

## Quick Start

```bash
# In Claude Code
@code-review "Set up automated PR review for our Node.js project"
@code-review cr-01 "Configure AI code review with security focus"
@code-review cr-03 "Implement quality gates for production branch"
```

## Skill Details

### cr-01: Automated Code Review

**Purpose**: AI-powered automated code analysis

**Capabilities**:
- Static analysis with ESLint, Pylint, RuboCop, etc.
- AI-powered code suggestions (GitHub Copilot, Amazon CodeWhisperer)
- Security vulnerability detection (Snyk, SonarQube, Semgrep)
- Code complexity analysis (cyclomatic, cognitive)
- Duplicate code detection
- Dependency vulnerability scanning
- Type safety checking
- Performance anti-pattern detection

**GitHub Actions Integration**:
```yaml
name: Automated Code Review
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run ESLint
        run: npx eslint . --format=json > eslint-report.json
      - name: SonarQube Scan
        uses: SonarSource/sonarqube-scan-action@v2
      - name: Semgrep Security Scan
        uses: returntocorp/semgrep-action@v1
      - name: Comment PR with results
        uses: actions/github-script@v7
```

**Azure DevOps Integration**:
```yaml
trigger: none
pr:
  branches:
    include: [main, develop]
stages:
  - stage: CodeReview
    jobs:
      - job: StaticAnalysis
        steps:
          - task: SonarQubePrepare@5
          - task: SonarQubeAnalyze@5
          - task: SonarQubePublish@5
```

---

### cr-02: PR Review Workflow

**Purpose**: Structured review process with templates and checklists

**Capabilities**:
- PR templates with required sections
- Review checklists (functionality, security, performance)
- Multi-stage approval workflows
- Automated reviewer notifications
- Review reminders and escalation
- Stale PR management
- Draft PR handling

**PR Template** (`.github/pull_request_template.md`):
```markdown
## Summary
<!-- Brief description of changes -->

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No secrets committed
- [ ] Security review if needed
- [ ] Breaking changes documented

## Security Considerations
<!-- Any security implications? -->

## Testing Done
<!-- How was this tested? -->
```

**Review Workflow States**:
```
Draft → Ready → In Review → Changes Requested → Approved → Merged
                    ↓
            Needs Security Review → Security Approved
```

---

### cr-03: Code Quality Gates

**Purpose**: Enforce quality standards before merge

**Capabilities**:
- Branch protection rules
- Required status checks
- Minimum reviewer count
- Code coverage thresholds
- No merge with failing tests
- Signed commits requirement
- Linear history enforcement
- Auto-merge when checks pass

**GitHub Branch Protection** (API):
```bash
gh api repos/{owner}/{repo}/branches/main/protection -X PUT \
  -F required_status_checks='{"strict":true,"contexts":["build","test","lint","security"]}' \
  -F enforce_admins=true \
  -F required_pull_request_reviews='{"required_approving_review_count":2,"require_code_owner_reviews":true}' \
  -F restrictions=null
```

**Quality Gate Configuration**:
```yaml
# .quality-gates.yml
gates:
  coverage:
    minimum: 80%
    block_merge: true
  complexity:
    max_cyclomatic: 15
    max_cognitive: 20
  security:
    critical: 0
    high: 0
    medium_max: 5
  duplication:
    max_percentage: 5%
  tests:
    required: true
    minimum_pass_rate: 100%
```

---

### cr-04: Reviewer Assignment

**Purpose**: Intelligent reviewer selection and load balancing

**Capabilities**:
- CODEOWNERS file management
- Expertise-based assignment
- Round-robin load balancing
- Availability-aware assignment
- Team-based review pools
- Escalation paths
- Conflict of interest detection
- Review load monitoring

**CODEOWNERS File**:
```
# Default reviewers
* @org/core-team

# Frontend
/src/components/** @org/frontend-team
*.tsx @org/frontend-team

# Backend
/src/api/** @org/backend-team
*.py @org/python-team

# Security-sensitive files
**/auth/** @org/security-team
**/secrets/** @org/security-team
*.env* @org/security-team

# Infrastructure
/terraform/** @org/platform-team
/kubernetes/** @org/platform-team
*.tf @org/platform-team
```

**Auto-Assignment Rules**:
```yaml
# .github/auto-assign.yml
reviewers:
  defaults:
    - team-core
  groups:
    frontend:
      - user1
      - user2
    backend:
      - user3
      - user4
  load_balancing: round-robin
  max_reviews_per_person: 5
  skip_if_author_is_reviewer: true
```

---

### cr-05: Review Analytics

**Purpose**: Metrics and insights for review process optimization

**Capabilities**:
- Review cycle time tracking
- Time to first review
- Time to approval
- Review load per developer
- Bottleneck identification
- Trend analysis
- SLO tracking for reviews
- Quality correlation analysis

**Key Metrics**:
```python
class ReviewMetrics:
    """Enterprise review metrics tracking."""

    METRICS = {
        "time_to_first_review": "< 4 hours (SLO)",
        "time_to_approval": "< 24 hours (SLO)",
        "review_iterations": "< 3 rounds average",
        "reviewer_load": "< 5 active reviews per person",
        "stale_prs": "0 PRs > 7 days without activity",
        "merge_time": "< 48 hours from open to merge",
        "defect_escape_rate": "< 1% bugs in reviewed code",
    }

    def calculate_cycle_time(self, pr_data):
        """Calculate end-to-end review cycle time."""
        opened = pr_data["created_at"]
        merged = pr_data["merged_at"]
        return (merged - opened).total_seconds() / 3600  # hours
```

**GitHub Analytics Query**:
```graphql
query ReviewMetrics($owner: String!, $repo: String!) {
  repository(owner: $owner, name: $repo) {
    pullRequests(last: 100, states: MERGED) {
      nodes {
        createdAt
        mergedAt
        reviews(first: 10) {
          nodes {
            submittedAt
            state
            author { login }
          }
        }
        timelineItems(first: 50, itemTypes: [REVIEW_REQUESTED_EVENT]) {
          nodes {
            ... on ReviewRequestedEvent {
              createdAt
              requestedReviewer { ... on User { login } }
            }
          }
        }
      }
    }
  }
}
```

---

## Enterprise Workflow

### Complete PR Pipeline
```
1. Developer creates PR
   ↓
2. Auto-assign reviewers (cr-04)
   ↓
3. Automated checks run (cr-01)
   - Linting, tests, security scan
   ↓
4. Quality gates validate (cr-03)
   - Coverage, complexity, security
   ↓
5. Human review with checklist (cr-02)
   ↓
6. Security review if flagged (@security-architect)
   ↓
7. Governance review if data changes (@data-governance)
   ↓
8. Approval and merge
   ↓
9. Analytics captured (cr-05)
   ↓
10. Board updated (@process-kanban)
```

### Enterprise Mode Requirements

When `--enterprise` flag is set:
- **Mandatory**: Security scan must pass (cr-01 + sa-05)
- **Mandatory**: 2 approvals minimum including CODEOWNER
- **Mandatory**: All quality gates pass (cr-03)
- **Mandatory**: No critical/high vulnerabilities
- **Mandatory**: Signed commits required
- **Mandatory**: Linear history (no merge commits)
- **Recommended**: Data governance review for data model changes

---

## Integration with Other Skills

| Skill | Integration |
|-------|-------------|
| @security-architect sa-05 | SAST results feed into review |
| @devops do-09 | DevSecOps pipeline gates |
| @data-governance dg-04 | Access control for sensitive files |
| @process-kanban | Auto-update board on PR events |
| @platform-engineer pe-05 | SLO monitoring for review times |

---

## Best Practices

1. **Keep PRs small**: < 400 lines of changes for effective review
2. **Automate the boring stuff**: Let tools catch style/lint issues
3. **Focus human review on**: Logic, architecture, security implications
4. **Set clear SLOs**: First review < 4 hours, merge < 48 hours
5. **Balance review load**: No one should have > 5 active reviews
6. **Escalate stale PRs**: Auto-ping after 24 hours, escalate after 48
7. **Measure and improve**: Track cycle time, aim for continuous reduction

---

## Quick Reference

```bash
# Set up complete PR automation
@code-review "Configure enterprise PR workflow for [project]"

# Individual skills
@code-review cr-01 "Set up automated code analysis"
@code-review cr-02 "Create PR template and review checklist"
@code-review cr-03 "Configure branch protection and quality gates"
@code-review cr-04 "Set up CODEOWNERS and reviewer assignment"
@code-review cr-05 "Build review analytics dashboard"
```
