# Code Review Skills

Automated code review, PR workflows, quality gates, and review analytics.

## Trigger Keywords

- "code review", "PR", "pull request"
- "review automation", "CODEOWNERS"
- "quality gate", "coverage", "lint"
- "review metrics", "cycle time"

## Available Skills

| ID    | Skill                 | Focus                          |
| ----- | --------------------- | ------------------------------ |
| cr-01 | Automated Code Review | SAST, lint, style checks       |
| cr-02 | PR Workflows          | Branch protection, templates   |
| cr-03 | Quality Gates         | Coverage, security, complexity |
| cr-04 | Reviewer Assignment   | CODEOWNERS, load balancing     |
| cr-05 | Review Analytics      | Metrics, SLOs, improvements    |

## Quality Gates

| Gate          | Threshold        |
| ------------- | ---------------- |
| Test Coverage | ≥80%             |
| Security Scan | No critical/high |
| Complexity    | <15 cyclomatic   |
| Lint          | Zero errors      |

## PR SLOs

| Metric               | Target    |
| -------------------- | --------- |
| Time to first review | <4 hours  |
| Time to approval     | <24 hours |
| Merge after approval | <48 hours |

## Best Practices

1. **Small PRs** - <400 lines for better reviews
2. **Automate checks** - Let CI catch obvious issues
3. **CODEOWNERS** - Route to domain experts
4. **Templates** - Standardize PR descriptions
5. **Track metrics** - Improve cycle time

## Integration

### Works with

- **DevOps (do-01)**: CI/CD pipeline
- **Security Architect (sa-05)**: Security review
- **Enterprise Dashboard**: Review metrics

## Quick Reference

```bash
@code-review "Set up automated PR checks"
@code-review "Configure quality gates"
@code-review "Create CODEOWNERS file"
@code-review "Analyze review metrics"
```
