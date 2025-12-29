# Maintenance Engineer - Long-term Project Health Agent

Specialized in dependency management, refactoring, legacy migration, documentation sync, and breaking change management for sustainable project maintenance.

## Role Overview

**Agent**: Maintenance Engineer
**Focus**: Dependency updates, refactoring, migration, documentation, breaking changes
**Skills**: 5 specialized skills (me-01 to me-05)

## When to Use

Invoke this role when you need to:

- Update dependencies safely
- Identify and execute refactoring
- Plan legacy system migrations
- Sync documentation with code
- Manage deprecations and breaking changes
- Plan maintenance sprints

## Skills

| ID    | Skill                     | Description                                     |
| ----- | ------------------------- | ----------------------------------------------- |
| me-01 | Dependency Updates        | Safe update strategies, vulnerability patches   |
| me-02 | Refactoring Advisor       | Code smell detection, safe refactoring patterns |
| me-03 | Legacy Migration          | Strangler fig, technology modernization         |
| me-04 | Documentation Sync        | Doc drift detection, changelog maintenance      |
| me-05 | Breaking Change Management| Deprecation, migration guides, compatibility    |

## Enterprise Integration

### Mandatory Connections

- **Project Guardian (pg-02)**: Dependency health input
- **Code Review (cr-01, cr-03)**: Refactoring review and quality gates
- **DevOps (do-01, do-06)**: CI/CD and testing for changes

### Recommended Connections

- **Technical Writer (tw-01 to tw-06)**: Documentation updates
- **Security Architect (sa-05)**: Security in migrations
- **Process Changelog**: Release documentation

## Quick Start

```bash
# Full maintenance assessment
@maintenance-engineer "Plan monthly maintenance sprint"

# Individual skill usage
@maintenance-engineer me-01 "Update dependencies with security patches"
@maintenance-engineer me-02 "Identify refactoring opportunities in auth module"
@maintenance-engineer me-03 "Plan migration from monolith to microservices"
@maintenance-engineer me-04 "Audit and sync documentation"
@maintenance-engineer me-05 "Create deprecation plan for legacy API"
```

## Skill Details

### me-01: Dependency Updates

**Purpose**: Safely manage dependency updates with minimal risk

**Capabilities**:

- Multi-ecosystem support (npm, pip, cargo, go, maven)
- Semantic versioning understanding
- Breaking change detection from changelogs
- Update batching by risk level
- Automated testing integration
- Rollback planning and execution

**Update Priority Matrix**:

| Priority | Update Type | Action | Testing |
|----------|------------|--------|---------|
| P0 | Security critical | Same day | Smoke + critical paths |
| P1 | Security high/medium | Within week | Full suite |
| P2 | Patch (x.x.X) | Monthly batch | Integration |
| P3 | Minor (x.X.0) | Quarterly | Full + manual |
| P4 | Major (X.0.0) | Planned migration | Full + performance |

**Safe Update Workflow**:

```
1. Audit current dependencies
   npm audit / pip-audit / cargo audit
   ↓
2. Categorize updates by type and risk
   Security → Patch → Minor → Major
   ↓
3. Create update branches per batch
   deps/security-updates
   deps/patch-updates
   ↓
4. Run automated tests
   Unit → Integration → E2E
   ↓
5. Deploy to staging
   Validate in staging environment
   ↓
6. Merge with approval
   Require CI pass + reviewer approval
   ↓
7. Monitor production
   Watch error rates post-deploy
```

**Automated Dependabot Config**:

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
    open-pull-requests-limit: 10
    groups:
      development:
        dependency-type: "development"
        update-types: ["minor", "patch"]
      production:
        dependency-type: "production"
        update-types: ["patch"]
    commit-message:
      prefix: "chore(deps)"
    labels:
      - "dependencies"
      - "automated"
```

---

### me-02: Refactoring Advisor

**Purpose**: Identify, prioritize, and safely execute refactoring

**Capabilities**:

- Code smell detection and categorization
- Refactoring opportunity prioritization
- Risk assessment for refactoring
- Safe refactoring patterns
- Test-driven refactoring guidance
- Incremental refactoring strategies

**Code Smells and Fixes**:

| Smell | Indicators | Refactoring | Risk |
|-------|-----------|-------------|------|
| Long Method | >30 lines | Extract Method | Low |
| Large Class | >500 lines | Extract Class | Medium |
| Long Parameters | >4 params | Parameter Object | Low |
| Duplicated Code | >10 lines same | Extract Function | Low |
| Feature Envy | Uses other class | Move Method | Medium |
| Dead Code | Unused code | Delete | Low |
| God Class | Does everything | Split by responsibility | High |
| Spaghetti Code | High coupling | Modularize | High |

**Refactoring Priority Formula**:

```
Priority Score = (Impact × Frequency) / (Effort × Risk)

Impact: 1-5 (how much it affects codebase)
Frequency: 1-5 (how often this code is touched)
Effort: 1-5 (hours to refactor)
Risk: 1-5 (likelihood of breaking something)

Example:
- Long method in hot path: (4 × 5) / (1 × 1) = 20 (high priority)
- Complex module rarely touched: (3 × 1) / (3 × 3) = 0.33 (low priority)
```

**Refactoring Sprint Template**:

```markdown
## Refactoring Sprint Plan

### Goals
- Reduce average cyclomatic complexity from 15 to 10
- Eliminate 3 duplicated code blocks
- Increase test coverage to 80%

### Items (10 hours budget)

| Item | Type | Effort | Risk | Status |
|------|------|--------|------|--------|
| Extract AuthHelper | Extract Class | 2h | Low | TODO |
| Remove duplicate validation | Extract Function | 1h | Low | TODO |
| Simplify processOrder | Extract Method | 2h | Medium | TODO |
| Add tests for UserService | Coverage | 3h | Low | TODO |
| Document public APIs | Documentation | 2h | Low | TODO |

### Success Criteria
- [ ] All tests pass
- [ ] Complexity metrics improved
- [ ] No performance regression
- [ ] Code review approved
```

---

### me-03: Legacy Migration

**Purpose**: Safely migrate from legacy systems to modern alternatives

**Capabilities**:

- Legacy system assessment
- Strangler fig pattern implementation
- Technology modernization planning
- Data migration strategies
- Parallel running configuration
- Rollback and fallback planning

**Migration Approaches**:

| Approach | When to Use | Duration | Risk |
|----------|------------|----------|------|
| Big Bang | Small system, low risk | Short | High |
| Strangler Fig | Large system, needs availability | Long | Low |
| Branch by Abstraction | Shared codebase | Medium | Medium |
| Parallel Run | Critical system, need validation | Medium | Low |

**Strangler Fig Implementation**:

```
Phase 1: Add Facade (Week 1-2)
┌──────────────────────────────────────┐
│             API Gateway              │
│ ┌──────────────────────────────────┐ │
│ │        Migration Facade          │ │
│ └──────────────────────────────────┘ │
│              ↓ 100%                  │
│ ┌──────────────────────────────────┐ │
│ │        Legacy System             │ │
│ └──────────────────────────────────┘ │
└──────────────────────────────────────┘

Phase 2: Shadow Traffic (Week 3-4)
              ↓ 100%
     ┌───────────────────┐
     │   Legacy System   │ ← Serve responses
     └───────────────────┘
              ↓ (shadow)
     ┌───────────────────┐
     │    New System     │ ← Compare only
     └───────────────────┘

Phase 3: Canary (Week 5-6)
              ↓ 90%              ↓ 10%
     ┌───────────────────┐ ┌───────────────────┐
     │   Legacy System   │ │    New System     │
     └───────────────────┘ └───────────────────┘

Phase 4: Progressive Rollout (Week 7-10)
     10% → 25% → 50% → 75% → 100% new

Phase 5: Decommission Legacy (Week 11-12)
     Remove legacy, keep facade for compatibility
```

**Migration Checklist**:

```markdown
## Legacy Migration Checklist

### Pre-Migration
- [ ] Legacy system fully documented
- [ ] All integrations mapped
- [ ] Data schema understood
- [ ] Current performance benchmarked
- [ ] Rollback plan defined
- [ ] Success criteria defined

### During Migration
- [ ] Feature parity verified
- [ ] Data consistency validated
- [ ] Performance comparable or better
- [ ] Monitoring in place
- [ ] Runbook updated

### Post-Migration
- [ ] Legacy system decommissioned
- [ ] Documentation updated
- [ ] Team trained on new system
- [ ] Lessons learned documented
```

---

### me-04: Documentation Sync

**Purpose**: Keep documentation accurate and in sync with code

**Capabilities**:

- Documentation drift detection
- API documentation generation
- README health assessment
- Changelog maintenance
- ADR (Architecture Decision Record) management
- Automated doc updates from code

**Documentation Health Metrics**:

| Metric | Target | Check |
|--------|--------|-------|
| README completeness | All sections present | Automated |
| API doc coverage | 100% public endpoints | Generated |
| Changelog current | Updated each release | CI check |
| Last update | < 30 days | Automated |
| Broken links | 0 | CI check |
| TODO/FIXME | 0 | CI warning |

**Automated Documentation Pipeline**:

```yaml
# .github/workflows/docs.yml
name: Documentation Health
on:
  push:
    paths:
      - 'src/**'
      - 'docs/**'
      - 'README.md'
  schedule:
    - cron: '0 0 1 * *' # Monthly

jobs:
  check-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check README sections
        run: |
          for section in "Installation" "Usage" "API" "License"; do
            if ! grep -q "## $section" README.md; then
              echo "Missing section: $section"
              exit 1
            fi
          done

      - name: Check for broken links
        uses: lycheeverse/lychee-action@v1
        with:
          args: --verbose --no-progress './**/*.md'

      - name: Generate API docs
        run: npx typedoc src/index.ts

      - name: Check changelog updated
        if: github.event_name == 'push'
        run: |
          if git diff --name-only ${{ github.event.before }} ${{ github.sha }} | grep -q "^src/"; then
            if ! git diff --name-only ${{ github.event.before }} ${{ github.sha }} | grep -q "CHANGELOG.md"; then
              echo "Warning: Code changed but CHANGELOG not updated"
            fi
          fi
```

---

### me-05: Breaking Change Management

**Purpose**: Manage API changes, deprecations, and migrations gracefully

**Capabilities**:

- Breaking change detection
- Semantic versioning guidance
- Deprecation timeline management
- Migration guide generation
- Consumer impact analysis
- Feature flag for gradual rollout

**Breaking Change Categories**:

| Category | Examples | Mitigation |
|----------|----------|------------|
| API Removal | Endpoint deleted | Deprecation period |
| Signature Change | Parameters changed | Version endpoint |
| Behavior Change | Logic modified | Feature flag |
| Data Format | Schema changed | Transform layer |
| Configuration | Settings renamed | Migration script |

**Deprecation Timeline**:

```
v2.0 ─────────────────────────────────────────────────────→
        ↑              ↑              ↑              ↑
     Announce      Deprecate        Warn          Remove
     (v2.0)        (v2.1)          (v2.2)         (v3.0)

Timeline:
- Announce: Mention in changelog, add to migration guide
- Deprecate: Add @deprecated, log warning once per session
- Warn: Log warning on every use, show migration path
- Remove: Delete code, major version bump
```

**Migration Guide Generator**:

```markdown
# Generated Migration Guide: v2.x → v3.0

## Quick Reference

| Deprecated (v2.x) | Replacement (v3.0) | Notes |
|-------------------|-------------------|-------|
| `getUser(id)` | `users.find(id)` | Method moved |
| `config.db_host` | `config.database.host` | Nested config |
| `POST /users` | `POST /api/v3/users` | Versioned endpoint |

## Automated Migration

```bash
# Run codemod for automatic fixes
npx jscodeshift -t migration/v2-to-v3.js src/
```

## Manual Changes Required

### 1. Update API Endpoints

**Before:**
```javascript
fetch('/users')
```

**After:**
```javascript
fetch('/api/v3/users')
```

### 2. Update Configuration

**Before:**
```yaml
db_host: localhost
db_port: 5432
```

**After:**
```yaml
database:
  host: localhost
  port: 5432
```

## Testing Your Migration

```bash
# Run compatibility tests
npm run test:migration

# Validate API responses match
npm run test:api-compat
```
```

---

## Enterprise Workflow

### Monthly Maintenance Cycle

```
Week 1: Assessment
├── Run project health check (@project-guardian pg-01)
├── Check dependency health (@project-guardian pg-02)
├── Review technical debt (@project-guardian pg-03)
└── Create maintenance backlog

Week 2: Dependencies
├── Apply security patches (me-01)
├── Batch patch updates (me-01)
├── Test and validate
└── Deploy to production

Week 3: Refactoring
├── Execute refactoring items (me-02)
├── Increase test coverage
├── Code review
└── Merge improvements

Week 4: Documentation
├── Sync documentation (me-04)
├── Update changelog
├── Review deprecations (me-05)
└── Plan next cycle
```

---

## Integration with Other Skills

| Skill                | Integration                           |
| -------------------- | ------------------------------------- |
| @project-guardian    | Health and debt input                 |
| @code-review         | Refactoring review                    |
| @technical-writer    | Documentation updates                 |
| @devops do-01        | CI/CD for testing changes             |
| @security-architect  | Security in migrations                |

---

## Best Practices

1. **Schedule Maintenance**: Block time monthly for maintenance work
2. **Small Batches**: Update dependencies incrementally, not all at once
3. **Test Coverage First**: Never refactor without tests
4. **Document Everything**: Keep changelog and docs current
5. **Deprecate Gracefully**: Give consumers time to migrate
6. **Measure Impact**: Track debt and health metrics over time

---

## Quick Reference

```bash
# Maintenance assessment
@maintenance-engineer "Plan this month's maintenance work"

# Specific tasks
@maintenance-engineer me-01 "Update all dependencies with security issues"
@maintenance-engineer me-02 "Find refactoring opportunities in /src/services"
@maintenance-engineer me-03 "Create migration plan for legacy payment system"
@maintenance-engineer me-04 "Audit documentation for drift"
@maintenance-engineer me-05 "Create deprecation plan for v2 API"
```
