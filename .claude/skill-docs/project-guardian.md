# Project Guardian

Project health monitoring through health checks, dependency management, technical debt tracking, and security posture assessment.

## Trigger Keywords

- "health check", "assessment", "audit"
- "dependencies", "outdated", "vulnerabilities"
- "technical debt", "tech debt", "code quality"
- "improvement", "roadmap"
- "security posture", "security assessment"

## Available Skills

| ID    | Skill                  | Focus                              |
| ----- | ---------------------- | ---------------------------------- |
| pg-01 | Health Check           | Overall project assessment         |
| pg-02 | Dependency Management  | Outdated packages, vulnerabilities |
| pg-03 | Technical Debt         | Code smells, complexity, coverage  |
| pg-04 | Continuous Improvement | Roadmap, prioritization            |
| pg-05 | Security Posture       | Security health assessment         |

## Health Check Categories

| Category      | Metrics                                         |
| ------------- | ----------------------------------------------- |
| Dependencies  | Outdated count, vulnerability count, update age |
| Code Quality  | Coverage %, complexity, lint issues             |
| Security      | CVE count, secrets exposure, config issues      |
| Documentation | README, API docs, architecture docs             |
| CI/CD         | Pipeline status, test pass rate                 |

## When to Run

- **Weekly**: pg-02 (dependencies)
- **Monthly**: pg-01 (full health check)
- **Quarterly**: pg-03 (tech debt analysis)
- **Before release**: pg-05 (security posture)

## Best Practices

1. **Baseline first** - Run pg-01 to establish starting point
2. **Track trends** - Monitor improvement over time
3. **Prioritize fixes** - Critical security first
4. **Budget for maintenance** - Allocate time for pg-02/pg-03
5. **Document decisions** - Track why debt exists

## Integration

### Works with

- **Maintenance Engineer (me-\*)**: Fixing issues found
- **Security Hardener (sh-\*)**: Security improvements
- **Code Hardener (ch-\*)**: Quality improvements

## Quick Reference

```bash
@project-guardian "Run full health check"
@project-guardian "Check for outdated dependencies"
@project-guardian "Analyze technical debt"
@project-guardian "Assess security posture"
```
