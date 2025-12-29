# Changelog

All notable changes to Tech Hub Skills will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.7.0] - 2024-12-29

### Added

#### 5 New Project Lifecycle Agents (25 new skills)

This release introduces a complete project lifecycle management suite to help developers maintain, strengthen, and secure their projects throughout their entire lifecycle.

##### Project Guardian (`@project-guardian`) - 5 skills
Your project health watchdog that monitors and tracks project quality over time.

| Skill | ID | Description |
|-------|----|-------------|
| Project Health Check | pg-01 | Comprehensive health scoring (0-100) with trend analysis |
| Dependency Management | pg-02 | Vulnerability scanning, outdated detection, license compliance |
| Technical Debt Analysis | pg-03 | Debt quantification, prioritization, and remediation planning |
| Continuous Improvement | pg-04 | Performance, scalability, and best practice recommendations |
| Security Posture Assessment | pg-05 | Security audit with OWASP compliance checking |

##### Code Hardener (`@code-hardener`) - 5 skills
Transform working code into bulletproof production-ready code.

| Skill | ID | Description |
|-------|----|-------------|
| Performance Hardening | ch-01 | Memory, CPU, I/O optimization, caching strategies |
| Error Resilience | ch-02 | Retry logic, circuit breakers, graceful degradation |
| Input Validation | ch-03 | Comprehensive validation, sanitization, injection prevention |
| Defensive Coding | ch-04 | Null safety, immutability, guard clauses, contracts |
| Code Fortification | ch-05 | Rate limiting, resource limits, attack surface reduction |

##### Maintenance Engineer (`@maintenance-engineer`) - 5 skills
Long-term project sustainability and modernization.

| Skill | ID | Description |
|-------|----|-------------|
| Dependency Updates | me-01 | Safe update strategies, semantic versioning, rollback planning |
| Refactoring Advisor | me-02 | Code smell detection, safe refactoring patterns |
| Legacy Migration | me-03 | Strangler fig pattern, technology modernization |
| Documentation Sync | me-04 | Doc drift detection, changelog maintenance, API docs |
| Breaking Change Management | me-05 | Deprecation strategies, migration guides, compatibility |

##### Security Hardener (`@security-hardener`) - 5 skills
Proactive security hardening and vulnerability management.

| Skill | ID | Description |
|-------|----|-------------|
| Vulnerability Scanning | sh-01 | CVE tracking, CVSS/EPSS prioritization, SLA enforcement |
| Secure Configuration | sh-02 | CIS benchmarks, security headers, TLS configuration |
| Attack Surface Reduction | sh-03 | Service minimization, port hardening, least privilege |
| Security Testing | sh-04 | SAST, DAST, OWASP Top 10 testing, pen test guidance |
| Incident Preparation | sh-05 | Response playbooks, logging, forensics readiness |

##### Development Accelerator (`@dev-accelerator`) - 5 skills
Speed up development with automation and code generation.

| Skill | ID | Description |
|-------|----|-------------|
| Project Scaffolding | da-01 | Multi-language templates, directory structure, CI/CD setup |
| Code Generation | da-02 | CRUD operations, models, types, migrations |
| Test Automation | da-03 | Test case generation, fixtures, mocks, coverage optimization |
| Rapid API Development | da-04 | OpenAPI generation, REST/GraphQL scaffolding |
| Integration Patterns | da-05 | Webhooks, events, OAuth, third-party API clients |

#### New Skill Chains

Added project lifecycle skill chains to the orchestrator:

| Goal | Skill Chain |
|------|-------------|
| New Project Setup | `da-01` → `do-01` → `pg-01` → `sh-02` → `ch-04` |
| Production Hardening | `pg-01` → `ch-01` → `ch-02` → `sh-01` → `sh-02` → `ch-05` |
| Security Hardening | `pg-05` → `sh-01` → `sh-02` → `sh-03` → `sh-04` → `sh-05` |
| Monthly Maintenance | `pg-01` → `pg-02` → `me-01` → `pg-03` → `me-02` → `me-04` |
| Legacy Migration | `pg-01` → `pg-03` → `me-03` → `ch-02` → `da-03` → `me-05` |
| Feature Development | `da-01` → `da-02` → `da-03` → `da-04` → `ch-03` → `ch-04` → `pg-01` |

#### New Mandatory Skill Conditions

| Condition | Mandatory Skills | Reason |
|-----------|-----------------|--------|
| New project | `da-01` + `pg-01` | Scaffolding + health baseline |
| Production hardening | `ch-01` + `ch-02` + `sh-02` | Performance + resilience + security |
| Before release | `pg-01` + `sh-01` + `ch-03` | Health + vulns + validation |
| Monthly maintenance | `pg-02` + `me-01` + `pg-03` | Dependencies + debt tracking |
| Security critical | `sh-01` + `sh-02` + `sh-04` | Scan + config + testing |

### Changed

- Updated skill count from 180+ to 200+
- Updated role count from 26 to 31
- Enhanced orchestrator with project lifecycle decision tree
- Updated README with new agents documentation
- Updated GitHub Copilot integration documentation

### Migration Guide

No breaking changes. Simply update to use the new agents:

```bash
# Update
npx tech-hub-skills install --force

# Use new agents
/project-guardian "Run health check"
/code-hardener "Harden for production"
/security-hardener "Security assessment"
/maintenance-engineer "Plan maintenance"
/dev-accelerator "Scaffold new project"
```

---

## [1.6.9] - 2024-12-28

### Changed

- Bumped version and updated copilot instructions

## [1.6.8] - 2024-12-27

### Fixed

- Updated package.json path in cli.js
- Automated installation fixes

## [1.6.7] - 2024-12-26

### Changed

- Synced __init__.py version

---

## Version History

| Version | Date | Highlights |
|---------|------|------------|
| 1.7.0 | 2024-12-29 | 5 new project lifecycle agents (25 skills) |
| 1.6.9 | 2024-12-28 | Copilot instructions update |
| 1.6.8 | 2024-12-27 | Installation fixes |
| 1.6.7 | 2024-12-26 | Version sync |
