# Security Lead Command

Route to the Security Lead Agent for security, compliance, and governance tasks.

## Usage

```
/security [your request]
```

## Examples

```
/security scan for PII in dataset
/security review application security
/security prepare SOC 2 audit
/security implement IAM
```

## What Happens

1. **Orchestrator** receives your request
2. **Security Lead** takes ownership (HIGHEST PRIORITY)
3. **Specialists** are assigned:
   - Security Architect (PII, threats, IAM, AppSec, secrets)
   - Compliance Officer (SOC 2, GDPR, HIPAA, PCI-DSS)
   - Security Hardener (vulnerabilities, configuration)

## Available Skills

| Agent              | Skills                                                                       |
| ------------------ | ---------------------------------------------------------------------------- |
| Security Architect | sa-01 to sa-07 (PII, threats, infra, IAM, AppSec, secrets, SIEM)             |
| Compliance Officer | co-01 to co-07 (SOC 2, GDPR, HIPAA, PCI-DSS, ISO 27001, audit, policies)     |
| Security Hardener  | sh-01 to sh-05 (vulnerabilities, config, attack surface, testing, incidents) |

## ⚠️ Security Lead is MANDATORY For:

- **ALL** personal/customer data processing
- **ALL** production deployments
- **ALL** authentication/authorization
- **ALL** API key/credential handling

Security Lead is automatically invoked even if you don't call this command when these conditions are detected.
