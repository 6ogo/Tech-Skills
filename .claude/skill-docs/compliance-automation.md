# Compliance Automation

Automated compliance checking, audit trails, and regulatory requirement validation for enterprise software delivery.

## Role Overview

**Agent**: Compliance Automation Specialist
**Focus**: Regulatory compliance, audit trails, policy enforcement, certification readiness

## When to Use

- Automate compliance checks in CI/CD
- Generate audit trails and evidence
- Validate against regulatory frameworks (GDPR, SOC 2, HIPAA, PCI-DSS)
- Prepare for compliance audits
- Implement policy-as-code

## Supported Frameworks

| Framework | Focus              | Key Requirements                              |
| --------- | ------------------ | --------------------------------------------- |
| SOC 2     | Security Controls  | Access control, encryption, monitoring        |
| GDPR      | Data Privacy       | Consent, data rights, breach notification     |
| HIPAA     | Healthcare Data    | PHI protection, access logs, encryption       |
| PCI-DSS   | Payment Data       | Cardholder data protection, network security  |
| ISO 27001 | InfoSec Management | Risk assessment, security controls            |
| FedRAMP   | Government Cloud   | Security authorization, continuous monitoring |

## Templates

All code templates for compliance automation are in `.claude/templates/compliance/`:

| Template                                             | Purpose                             |
| ---------------------------------------------------- | ----------------------------------- |
| [checker.py](../templates/compliance/checker.py)     | Python compliance checker for CI/CD |
| [policies.yml](../templates/compliance/policies.yml) | Policy-as-code configuration        |
| [workflow.yml](../templates/compliance/workflow.yml) | GitHub Actions compliance workflow  |

## Key Controls

### SOC 2 Type II

- **CC6.1**: Access control - no hardcoded credentials, MFA, least privilege
- **CC6.7**: Encryption - TLS 1.2+, data at rest encryption
- **CC7.2**: Monitoring - audit logging, 1-year retention
- **CC8.1**: Change management - PR reviews, deployment approvals

### GDPR

- PII detection and handling
- Data retention policies
- Consent management
- Breach notification procedures

## Integration

### Mandatory Connections

- **Security Architect (sa-\*)**: Security control verification
- **Data Governance (dg-\*)**: Data handling compliance
- **DevOps (do-09)**: CI/CD pipeline integration

### Recommended Connections

- **Code Review (cr-03)**: Quality gates for compliance
- **Platform Engineer (pe-\*)**: Infrastructure compliance

## Best Practices

1. **Automate everything** - Manual compliance is unsustainable
2. **Fail fast** - Block non-compliant changes in CI/CD
3. **Evidence collection** - Maintain audit trails automatically
4. **Continuous monitoring** - Don't wait for audits
5. **Policy as code** - Version control your compliance rules
6. **Remediation guidance** - Always provide fix instructions

## Quick Reference

```bash
@compliance-automation "Set up SOC 2 compliance checks for our CI/CD"
@compliance-automation "Generate GDPR compliance evidence for audit"
@compliance-automation "Check license compliance for our dependencies"
```
