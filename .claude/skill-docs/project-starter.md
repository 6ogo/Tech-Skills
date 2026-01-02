# Project Starter

Guided project setup with Enterprise Mode for security, governance, and compliance requirements.

## Trigger Keywords

- "new project", "start project", "initialize"
- "enterprise", "production-ready"
- "scaffold", "bootstrap", "setup"

## When to Use

- Starting a new project from scratch
- Analyzing an existing project
- Setting up enterprise-grade applications

## Modes

### Standard Mode

Quick project setup with sensible defaults:

- Project structure
- Configuration files
- Basic CI/CD
- README and docs

### Enterprise Mode

Production-ready with mandatory security and governance:

- Security Architect review (sa-01 to sa-07)
- Data Governance (dg-01 to dg-06)
- Code Review automation (cr-01 to cr-05)
- Compliance checks

## Enterprise Checklist

| Category   | Requirements                                       |
| ---------- | -------------------------------------------------- |
| Security   | Threat modeling, PII detection, secrets management |
| Governance | Data catalog, lineage, access control              |
| Quality    | Code review, quality gates, testing                |
| Compliance | SOC 2, GDPR checks as needed                       |

## Quality Gates (Enterprise)

- No critical/high vulnerabilities
- 80%+ code coverage
- All compliance controls passing
- Security architect sign-off
- Data governance sign-off

## Integration

### Standard Mode uses

- **DevOps (do-01)**: CI/CD setup
- **Dev Accelerator (da-01)**: Scaffolding

### Enterprise Mode adds

- **Security Architect (sa-\*)**: Security review
- **Data Governance (dg-\*)**: Data management
- **Compliance Automation**: Compliance checks

## Quick Reference

```bash
# Standard mode
@project-starter "Create a new Node.js API project"

# Enterprise mode
@project-starter --enterprise "Build a customer data platform"
```
