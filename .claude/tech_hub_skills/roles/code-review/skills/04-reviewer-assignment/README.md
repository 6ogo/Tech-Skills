# cr-04: Reviewer Assignment

Intelligent reviewer selection with CODEOWNERS, load balancing, and expertise matching.

## Overview

Effective reviewer assignment ensures the right people review the right code. This skill provides automated assignment based on code ownership, expertise, availability, and workload balancing.

## Capabilities

### CODEOWNERS Management
- File and directory ownership rules
- Team-based ownership
- Fallback reviewers
- Wildcard patterns

### Intelligent Assignment
- Expertise matching based on history
- Workload balancing across team
- Availability awareness
- Timezone considerations

### Assignment Rules
- Required vs optional reviewers
- Minimum review count
- Escalation paths
- Conflict of interest detection

## Implementation

### CODEOWNERS File

```
# CODEOWNERS - GitHub/GitLab code ownership
# Syntax: pattern @user-or-team

# Default: core team reviews everything not otherwise specified
* @org/core-team

# ============================================
# FRONTEND
# ============================================
/src/components/** @org/frontend-team
/src/pages/** @org/frontend-team
/src/hooks/** @org/frontend-team
*.tsx @org/frontend-team
*.css @org/frontend-team
*.scss @org/frontend-team
/public/** @org/frontend-team

# ============================================
# BACKEND
# ============================================
/src/api/** @org/backend-team
/src/services/** @org/backend-team
/src/models/** @org/backend-team
*.py @org/python-team
/src/server/** @org/backend-team

# ============================================
# DATA
# ============================================
/src/data/** @org/data-team
/pipelines/** @org/data-team
*.sql @org/data-team
/dbt/** @org/data-team

# ============================================
# INFRASTRUCTURE & DEVOPS
# ============================================
/terraform/** @org/platform-team @org/security-team
/kubernetes/** @org/platform-team
/.github/workflows/** @org/platform-team
/docker/** @org/platform-team
Dockerfile* @org/platform-team
docker-compose*.yml @org/platform-team

# ============================================
# SECURITY-SENSITIVE FILES (Require security review)
# ============================================
**/auth/** @org/security-team
**/security/** @org/security-team
**/crypto/** @org/security-team
**/*secret* @org/security-team
**/*password* @org/security-team
**/*token* @org/security-team
.env* @org/security-team
**/iam/** @org/security-team

# ============================================
# DATABASE MIGRATIONS (Require DBA review)
# ============================================
**/migrations/** @org/dba-team @org/backend-team
*.migration.* @org/dba-team

# ============================================
# API CONTRACTS
# ============================================
**/openapi/** @org/api-governance
*.openapi.yaml @org/api-governance
**/graphql/schema/** @org/api-governance

# ============================================
# DOCUMENTATION
# ============================================
*.md @org/docs-team
/docs/** @org/docs-team
README* @org/docs-team

# ============================================
# DEPENDENCIES & CONFIGURATION
# ============================================
package.json @org/core-team @org/security-team
package-lock.json @org/core-team
requirements.txt @org/core-team @org/security-team
pyproject.toml @org/core-team

# ============================================
# CRITICAL FILES (Require lead approval)
# ============================================
/.github/CODEOWNERS @org/engineering-leads
/src/core/** @org/engineering-leads
```

### Auto-Assignment Configuration

```yaml
# .github/auto-assign.yml
# GitHub Auto-Assign Action configuration

# Add reviewers to pull requests
addReviewers: true

# Add assignees to pull requests
addAssignees: true

# Strategy: round-robin, random, or load-balance
reviewersStrategy: load-balance

# Number of reviewers to assign
numberOfReviewers: 2

# Review groups - assign from specific teams
reviewGroups:
  frontend:
    - frontend-dev-1
    - frontend-dev-2
    - frontend-dev-3

  backend:
    - backend-dev-1
    - backend-dev-2
    - backend-dev-3

  fullstack:
    - fullstack-1
    - fullstack-2

# Assign from groups based on file patterns
useReviewGroups: true

# File pattern to group mapping
filterLabels:
  frontend:
    - "*.tsx"
    - "*.css"
    - "src/components/**"
  backend:
    - "*.py"
    - "src/api/**"
    - "src/services/**"

# Skip if author is the only team member
skipIfAlreadyReviewing: true

# Don't assign author as reviewer
skipAssigneesForAuthor: true

# Skip if PR is draft
skipDraft: true

# Max reviews per person (load balancing)
maxReviewsPerPerson: 5
```

### Intelligent Assignment System

```python
#!/usr/bin/env python3
"""Intelligent reviewer assignment system."""

from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional
from datetime import datetime, timedelta
from collections import defaultdict
import random

@dataclass
class Developer:
    """Represents a developer for review assignment."""
    username: str
    teams: List[str]
    expertise: List[str]  # File patterns they're expert in
    timezone: str
    active_reviews: int = 0
    max_reviews: int = 5
    on_vacation: bool = False
    last_assigned: Optional[datetime] = None

@dataclass
class PullRequest:
    """Represents a PR needing reviewers."""
    number: int
    author: str
    files_changed: List[str]
    labels: List[str] = field(default_factory=list)
    is_security_sensitive: bool = False
    is_database_change: bool = False

class ReviewerAssigner:
    """Assigns reviewers based on multiple factors."""

    def __init__(self, developers: List[Developer], codeowners: Dict[str, List[str]]):
        self.developers = {d.username: d for d in developers}
        self.codeowners = codeowners
        self.assignment_history: Dict[str, List[datetime]] = defaultdict(list)

    def assign_reviewers(
        self,
        pr: PullRequest,
        min_reviewers: int = 2,
        require_codeowner: bool = True
    ) -> List[str]:
        """Assign reviewers to a PR."""
        candidates = self._get_candidates(pr)
        assigned = []

        # 1. Must include CODEOWNER if required
        if require_codeowner:
            codeowner = self._select_codeowner(pr, candidates)
            if codeowner:
                assigned.append(codeowner)
                candidates.remove(codeowner)

        # 2. Add security reviewer if needed
        if pr.is_security_sensitive:
            security_reviewer = self._select_from_team("security-team", candidates, pr)
            if security_reviewer:
                assigned.append(security_reviewer)
                candidates.discard(security_reviewer)

        # 3. Add DBA if database change
        if pr.is_database_change:
            dba = self._select_from_team("dba-team", candidates, pr)
            if dba:
                assigned.append(dba)
                candidates.discard(dba)

        # 4. Fill remaining slots with load-balanced selection
        while len(assigned) < min_reviewers and candidates:
            reviewer = self._select_load_balanced(candidates, pr)
            if reviewer:
                assigned.append(reviewer)
                candidates.discard(reviewer)
            else:
                break

        # Update assignment tracking
        for reviewer in assigned:
            self.developers[reviewer].active_reviews += 1
            self.developers[reviewer].last_assigned = datetime.now()
            self.assignment_history[reviewer].append(datetime.now())

        return assigned

    def _get_candidates(self, pr: PullRequest) -> Set[str]:
        """Get all eligible candidates for review."""
        candidates = set()

        for dev in self.developers.values():
            # Exclude author
            if dev.username == pr.author:
                continue

            # Exclude unavailable
            if dev.on_vacation:
                continue

            # Exclude overloaded
            if dev.active_reviews >= dev.max_reviews:
                continue

            candidates.add(dev.username)

        return candidates

    def _select_codeowner(self, pr: PullRequest, candidates: Set[str]) -> Optional[str]:
        """Select a CODEOWNER for the changed files."""
        owners = set()

        for file in pr.files_changed:
            for pattern, owner_list in self.codeowners.items():
                if self._matches_pattern(file, pattern):
                    owners.update(owner_list)

        # Filter to available candidates
        available_owners = owners & candidates

        if not available_owners:
            return None

        # Select least loaded owner
        return self._select_load_balanced(available_owners, pr)

    def _select_from_team(
        self,
        team: str,
        candidates: Set[str],
        pr: PullRequest
    ) -> Optional[str]:
        """Select a reviewer from a specific team."""
        team_members = {
            username for username, dev in self.developers.items()
            if team in dev.teams and username in candidates
        }

        if not team_members:
            return None

        return self._select_load_balanced(team_members, pr)

    def _select_load_balanced(
        self,
        candidates: Set[str],
        pr: PullRequest
    ) -> Optional[str]:
        """Select reviewer with lowest load, with expertise tiebreaker."""
        if not candidates:
            return None

        scored = []
        for username in candidates:
            dev = self.developers[username]
            score = self._calculate_score(dev, pr)
            scored.append((username, score))

        # Sort by score (lower is better), with randomization for ties
        scored.sort(key=lambda x: (x[1], random.random()))

        return scored[0][0] if scored else None

    def _calculate_score(self, dev: Developer, pr: PullRequest) -> float:
        """Calculate assignment score (lower is better)."""
        score = 0.0

        # Active review load (major factor)
        score += dev.active_reviews * 10

        # Recent assignments (avoid assigning same person repeatedly)
        recent = sum(
            1 for dt in self.assignment_history.get(dev.username, [])
            if dt > datetime.now() - timedelta(days=7)
        )
        score += recent * 5

        # Expertise match (negative = good)
        for pattern in dev.expertise:
            for file in pr.files_changed:
                if self._matches_pattern(file, pattern):
                    score -= 3

        return score

    def _matches_pattern(self, file: str, pattern: str) -> bool:
        """Check if file matches CODEOWNERS pattern."""
        import fnmatch
        # Handle directory patterns
        if pattern.endswith("/**"):
            dir_pattern = pattern[:-3]
            return file.startswith(dir_pattern.lstrip("/"))
        return fnmatch.fnmatch(file, pattern.lstrip("/"))

    def get_reviewer_load(self) -> Dict[str, Dict]:
        """Get current reviewer load statistics."""
        return {
            username: {
                "active_reviews": dev.active_reviews,
                "max_reviews": dev.max_reviews,
                "utilization": f"{(dev.active_reviews / dev.max_reviews) * 100:.0f}%",
                "recent_assignments": len([
                    dt for dt in self.assignment_history.get(username, [])
                    if dt > datetime.now() - timedelta(days=7)
                ])
            }
            for username, dev in self.developers.items()
        }


# GitHub Action for auto-assignment
GITHUB_ACTION = """
name: Auto Assign Reviewers
on:
  pull_request:
    types: [opened, ready_for_review]

jobs:
  assign:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Get changed files
        id: files
        uses: tj-actions/changed-files@v41

      - name: Assign reviewers
        uses: actions/github-script@v7
        with:
          script: |
            const changedFiles = '${{ steps.files.outputs.all_changed_files }}'.split(' ');

            // Determine required reviewers based on files
            const reviewers = new Set();
            const teams = new Set();

            for (const file of changedFiles) {
              if (file.includes('/auth/') || file.includes('/security/')) {
                teams.add('security-team');
              }
              if (file.includes('/migrations/') || file.endsWith('.sql')) {
                teams.add('dba-team');
              }
              if (file.startsWith('terraform/') || file.startsWith('kubernetes/')) {
                teams.add('platform-team');
              }
            }

            // Request team reviews
            if (teams.size > 0) {
              await github.rest.pulls.requestReviewers({
                owner: context.repo.owner,
                repo: context.repo.repo,
                pull_number: context.issue.number,
                team_reviewers: Array.from(teams)
              });
            }
"""
```

### Escalation Configuration

```yaml
# .github/review-escalation.yml
escalation:
  # Escalate if no review after X hours
  no_review_timeout: 24
  escalation_chain:
    - level: 1
      after_hours: 24
      action: remind_reviewers
      message: "Reminder: PR #{pr_number} needs review"

    - level: 2
      after_hours: 48
      action: add_team_lead
      teams: ["engineering-leads"]
      message: "Escalation: PR #{pr_number} unreviewed for 48 hours"

    - level: 3
      after_hours: 72
      action: notify_manager
      slack_channel: "#engineering-escalations"
      message: "Critical: PR #{pr_number} blocked for 72 hours"

  # Conflict of interest rules
  conflict_rules:
    - author_reports_to_reviewer: warn
    - same_team_only: require_external
    - self_approval: block
```

## Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| Assignment accuracy | > 90% | Right expertise assigned |
| Load balance variance | < 20% | Even distribution |
| Escalation rate | < 5% | Reviews happening on time |
| CODEOWNER coverage | 100% | All files have owners |

## Connections

- **Inputs from**: PR creation event
- **Outputs to**: Review workflow (cr-02), analytics (cr-05)
- **Integrates with**: Team management, PTO calendars

## Best Practices

1. Keep CODEOWNERS up to date as team changes
2. Set reasonable max review limits (5-7)
3. Account for timezone differences
4. Automate vacation/OOO detection
5. Review assignment patterns quarterly
6. Balance between expertise and load
