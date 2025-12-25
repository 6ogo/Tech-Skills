# cr-02: PR Review Workflow

Structured pull request review process with templates, checklists, and approval workflows.

## Overview

A well-defined PR review workflow ensures consistent quality, faster reviews, and clear expectations for both authors and reviewers. This skill provides templates, checklists, and automation for enterprise PR management.

## Capabilities

### PR Templates
- Standard change template
- Feature template with design docs
- Bug fix template with root cause
- Security-sensitive change template
- Database migration template

### Review Checklists
- Functionality verification
- Security considerations
- Performance impact
- Test coverage
- Documentation updates

### Workflow Automation
- Auto-labeling based on changes
- Draft to ready transitions
- Review reminders
- Stale PR management
- Merge queue handling

## Implementation

### PR Template (.github/pull_request_template.md)

```markdown
## Summary
<!-- Describe your changes in 2-3 sentences -->

## Type of Change
<!-- Check all that apply -->
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Refactoring (no functional changes)
- [ ] Documentation update
- [ ] Configuration change
- [ ] Security fix

## Related Issues
<!-- Link any related issues: Fixes #123, Relates to #456 -->

## Changes Made
<!-- List the main changes -->
-
-
-

## Testing Done
<!-- Describe testing performed -->
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed
- [ ] Test coverage maintained/increased

## Security Checklist
<!-- For all changes, verify -->
- [ ] No secrets or credentials committed
- [ ] No new dependencies with known vulnerabilities
- [ ] Input validation added where needed
- [ ] Authentication/authorization unchanged or reviewed
- [ ] Logging does not expose sensitive data

## Performance Impact
<!-- Describe any performance implications -->
- [ ] No performance impact expected
- [ ] Performance tested (describe results)
- [ ] New database queries are optimized
- [ ] No N+1 queries introduced

## Documentation
- [ ] README updated if needed
- [ ] API documentation updated
- [ ] Changelog entry added
- [ ] Architecture docs updated if needed

## Rollback Plan
<!-- How to rollback if issues are found -->

## Screenshots (if applicable)
<!-- Add screenshots for UI changes -->

## Reviewer Notes
<!-- Any specific areas you'd like reviewers to focus on -->
```

### Security-Sensitive PR Template

```markdown
## Security Change Request

### Summary
<!-- Describe the security-related change -->

### Security Impact Assessment

**Risk Level**: [ ] Critical [ ] High [ ] Medium [ ] Low

**Affected Areas**:
- [ ] Authentication
- [ ] Authorization
- [ ] Data encryption
- [ ] Input validation
- [ ] Session management
- [ ] Logging/Audit
- [ ] API security
- [ ] Infrastructure

### Threat Model Update
<!-- Link to updated threat model or describe changes -->

### Security Review Checklist
- [ ] OWASP Top 10 considered
- [ ] STRIDE analysis performed
- [ ] Security architect reviewed (required for High/Critical)
- [ ] Pen testing scheduled if needed
- [ ] Security scanning passed

### Compliance Impact
- [ ] No compliance impact
- [ ] GDPR implications reviewed
- [ ] SOC 2 controls affected
- [ ] PCI-DSS requirements considered

### Required Approvers
- [ ] Security team member
- [ ] Code owner
- [ ] Platform team (if infrastructure)
```

### Review Checklist Automation

```yaml
# .github/workflows/pr-checklist.yml
name: PR Review Checklist
on:
  pull_request:
    types: [opened, edited, synchronize]

jobs:
  validate-checklist:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check PR template completion
        uses: actions/github-script@v7
        with:
          script: |
            const body = context.payload.pull_request.body || '';

            const requiredSections = [
              'Summary',
              'Type of Change',
              'Testing Done',
              'Security Checklist'
            ];

            const missingSections = requiredSections.filter(
              section => !body.includes(`## ${section}`)
            );

            if (missingSections.length > 0) {
              core.setFailed(
                `Missing required sections: ${missingSections.join(', ')}`
              );
            }

            // Check for unchecked security items
            const securitySection = body.match(/## Security Checklist[\s\S]*?(?=##|$)/);
            if (securitySection) {
              const unchecked = (securitySection[0].match(/- \[ \]/g) || []).length;
              const checked = (securitySection[0].match(/- \[x\]/gi) || []).length;

              if (unchecked > 0 && checked === 0) {
                core.warning('Security checklist not completed');
              }
            }

      - name: Label PR based on changes
        uses: actions/labeler@v5
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
```

### Auto-Labeling Configuration

```yaml
# .github/labeler.yml
frontend:
  - changed-files:
      - any-glob-to-any-file:
          - 'src/components/**'
          - 'src/pages/**'
          - '**/*.tsx'
          - '**/*.css'

backend:
  - changed-files:
      - any-glob-to-any-file:
          - 'src/api/**'
          - 'src/services/**'
          - '**/*.py'

database:
  - changed-files:
      - any-glob-to-any-file:
          - '**/migrations/**'
          - '**/*.sql'

infrastructure:
  - changed-files:
      - any-glob-to-any-file:
          - 'terraform/**'
          - 'kubernetes/**'
          - '.github/workflows/**'
          - 'Dockerfile*'

security:
  - changed-files:
      - any-glob-to-any-file:
          - '**/auth/**'
          - '**/security/**'
          - '**/*secret*'
          - '**/*password*'

documentation:
  - changed-files:
      - any-glob-to-any-file:
          - '**/*.md'
          - 'docs/**'

tests:
  - changed-files:
      - any-glob-to-any-file:
          - '**/*.test.*'
          - '**/*.spec.*'
          - '**/tests/**'
```

### Review Reminder Workflow

```yaml
# .github/workflows/pr-reminders.yml
name: PR Review Reminders
on:
  schedule:
    - cron: '0 9 * * 1-5'  # 9 AM weekdays
  workflow_dispatch:

jobs:
  remind-reviewers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v7
        with:
          script: |
            const { data: prs } = await github.rest.pulls.list({
              owner: context.repo.owner,
              repo: context.repo.repo,
              state: 'open'
            });

            const now = new Date();
            const ONE_DAY = 24 * 60 * 60 * 1000;

            for (const pr of prs) {
              if (pr.draft) continue;

              const created = new Date(pr.created_at);
              const age = (now - created) / ONE_DAY;

              // Remind after 24 hours
              if (age > 1 && age < 2) {
                await github.rest.issues.createComment({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pr.number,
                  body: ' **Reminder**: This PR has been awaiting review for over 24 hours.'
                });
              }

              // Escalate after 48 hours
              if (age > 2) {
                await github.rest.issues.addLabels({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pr.number,
                  labels: ['needs-attention']
                });
              }
            }
```

### Review States Machine

```python
"""PR Review workflow state machine."""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

class ReviewState(Enum):
    DRAFT = "draft"
    READY_FOR_REVIEW = "ready_for_review"
    IN_REVIEW = "in_review"
    CHANGES_REQUESTED = "changes_requested"
    APPROVED = "approved"
    NEEDS_SECURITY_REVIEW = "needs_security_review"
    SECURITY_APPROVED = "security_approved"
    READY_TO_MERGE = "ready_to_merge"
    MERGED = "merged"

@dataclass
class PRWorkflow:
    """Manages PR review workflow state."""

    pr_number: int
    state: ReviewState = ReviewState.DRAFT
    reviewers: List[str] = None
    approvals: List[str] = None
    security_review_required: bool = False
    created_at: datetime = None
    last_activity: datetime = None

    def __post_init__(self):
        self.reviewers = self.reviewers or []
        self.approvals = self.approvals or []
        self.created_at = self.created_at or datetime.now()
        self.last_activity = self.last_activity or datetime.now()

    def transition(self, new_state: ReviewState) -> bool:
        """Transition to new state if valid."""
        valid_transitions = {
            ReviewState.DRAFT: [ReviewState.READY_FOR_REVIEW],
            ReviewState.READY_FOR_REVIEW: [ReviewState.IN_REVIEW, ReviewState.DRAFT],
            ReviewState.IN_REVIEW: [
                ReviewState.CHANGES_REQUESTED,
                ReviewState.APPROVED,
                ReviewState.NEEDS_SECURITY_REVIEW
            ],
            ReviewState.CHANGES_REQUESTED: [ReviewState.IN_REVIEW],
            ReviewState.APPROVED: [
                ReviewState.READY_TO_MERGE,
                ReviewState.NEEDS_SECURITY_REVIEW
            ],
            ReviewState.NEEDS_SECURITY_REVIEW: [
                ReviewState.SECURITY_APPROVED,
                ReviewState.CHANGES_REQUESTED
            ],
            ReviewState.SECURITY_APPROVED: [ReviewState.READY_TO_MERGE],
            ReviewState.READY_TO_MERGE: [ReviewState.MERGED],
        }

        if new_state in valid_transitions.get(self.state, []):
            self.state = new_state
            self.last_activity = datetime.now()
            return True
        return False

    def add_approval(self, reviewer: str) -> None:
        """Add reviewer approval."""
        if reviewer not in self.approvals:
            self.approvals.append(reviewer)
            self.last_activity = datetime.now()

    def is_ready_to_merge(self) -> bool:
        """Check if PR meets merge criteria."""
        min_approvals = 2
        has_approvals = len(self.approvals) >= min_approvals

        if self.security_review_required:
            return (has_approvals and
                    self.state == ReviewState.SECURITY_APPROVED)

        return has_approvals and self.state == ReviewState.APPROVED

    def get_blockers(self) -> List[str]:
        """Get list of merge blockers."""
        blockers = []

        if len(self.approvals) < 2:
            blockers.append(f"Need {2 - len(self.approvals)} more approval(s)")

        if self.security_review_required and self.state != ReviewState.SECURITY_APPROVED:
            blockers.append("Security review required")

        if self.state == ReviewState.CHANGES_REQUESTED:
            blockers.append("Changes requested by reviewer")

        return blockers
```

## Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| Template compliance | 100% | All PRs use templates |
| Checklist completion | > 90% | Security checklist done |
| Review SLA | < 24 hours | First review time |
| Stale PR count | 0 | No PRs > 7 days |

## Connections

- **Inputs from**: Developer creates PR
- **Outputs to**: Reviewers, quality gates (cr-03)
- **Triggers**: Auto-labeling, reviewer assignment (cr-04)

## Best Practices

1. Keep PR templates concise but comprehensive
2. Make security checklist mandatory, not optional
3. Use auto-labeling to route reviews efficiently
4. Set up reminders to prevent stale PRs
5. Track template usage and iterate based on feedback
