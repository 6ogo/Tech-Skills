# Tech Hub Skills - Complete Role Documentation

This document provides detailed information about all available roles and their skills.

For installation instructions, see [../README.md](../README.md).

## Quick Reference

Use skills in Claude Code with `@` mentions:

```bash
# Start with the orchestrator (routes to all skills)
@orchestrator "Build a customer churn prediction model"

# Or invoke specific roles
@ai-engineer "Create a RAG pipeline"
@security-architect "Review this code for PII"
@data-engineer "Design a lakehouse architecture"

# Enterprise mode (mandatory security + governance)
@project-starter --enterprise "Build a customer data platform"
```

## Available Roles & Skills

### Core Engineering (34 skills)
| Role | Skills | Focus |
|------|--------|-------|
| **AI Engineer** | 8 | LLMs, RAG, Agents, Guardrails, Embeddings |
| **Data Engineer** | 9 | Lakehouse, ETL/ELT, Streaming, Quality |
| **ML Engineer** | 9 | MLOps, Training, Serving, Monitoring |
| **Data Scientist** | 8 | EDA, Modeling, Analytics, Experimentation |

### Architecture & Security Roles (15 skills)
| Role | Skills | Focus |
|------|--------|-------|
| **Security Architect** | 7 | PII, Threat Modeling, IAM, Secrets |
| **System Design** | 8 | Architecture, Scalability, HA/DR, APIs |

### Platform & Operations Roles (45 skills)
| Role | Skills | Focus |
|------|--------|-------|
| **Platform Engineer** | 6 | IDP, Self-Service, SLOs |
| **Data Governance** | 6 | Catalog, Lineage, Quality, Compliance |
| **DevOps** | 9 | CI/CD, Containers, IaC, GitOps |
| **MLOps** | 9 | Experiments, Registry, Deployment |
| **FinOps** | 8 | Cost Visibility, Optimization |
| **Docker** | 5 | Containers, Security, Optimization |

### Enterprise Governance Roles (10+ skills)
| Role | Skills | FocRoles us |
|------|--------|-------|
| **Code Review** | 5 | PR Automation, Quality Gates, Analytics |
| **Compliance** | Integrated | SOC 2, GDPR, HIPAA, Audit Trails |
| **Dashboard** | Integrated | Security, Compliance, DORA Metrics |

### Product & Design Roles (6 skills)
| Role | Skills | Focus |
|------|--------|-------|
| **Product Designer** | 6 | Requirements, Research, UX, Brainstorming |

### Cloud Platform Roles (12 skills)
| Role | Skills | Focus |
|------|--------|-------|
| **Azure** | 12 | All Azure services |

## Directory Structure

```
.claude/
├── skills/                 # Role skill files (invoke with @role-name)
│   ├── orchestrator.md     # Main orchestrator - routes to all skills
│   ├── ai-engineer.md
│   ├── data-engineer.md
│   ├── security-architect.md
│   ├── code-review.md
│   ├── compliance-automation.md
│   └── ...
├── roles/                  # Detailed skill implementations
│   ├── ai-engineer/
│   │   └── skills/
│   │       ├── 01-prompt-engineering/README.md
│   │       ├── 02-rag-pipeline/README.md
│   │       └── ...
│   ├── security-architect/
│   │   └── skills/
│   │       ├── 01-pii-detection/README.md
│   │       ├── 02-threat-modeling/README.md
│   │       └── ...
│   └── ...
└── README.md               # This file
```

## Skill ID Reference

| Role | Prefix | Skills |
|------|--------|--------|
| AI Engineer | `ai-` | ai-01 to ai-08 |
| Data Engineer | `de-` | de-01 to de-09 |
| ML Engineer | `ml-` | ml-01 to ml-09 |
| Data Scientist | `ds-` | ds-01 to ds-08 |
| Security Architect | `sa-` | sa-01 to sa-07 |
| System Design | `sd-` | sd-01 to sd-08 |
| Platform Engineer | `pe-` | pe-01 to pe-06 |
| Data Governance | `dg-` | dg-01 to dg-06 |
| DevOps | `do-` | do-01 to do-09 |
| MLOps | `mo-` | mo-01 to mo-09 |
| FinOps | `fo-` | fo-01 to fo-08 |
| Azure | `az-` | az-01 to az-12 |
| Code Review | `cr-` | cr-01 to cr-05 |
| Product Designer | `pd-` | pd-01 to pd-06 |

## Enterprise Mode

For production applications, use Enterprise Mode to ensure security and governance:

```bash
@project-starter --enterprise "Build a production API"
```

Enterprise Mode **automatically includes**:
- Security Architect (sa-01 to sa-07)
- Data Governance (dg-01 to dg-06)
- Code Review (cr-01 to cr-05)
- Compliance Automation

### Enterprise Workflow
```
Requirements → Security Assessment → Data Classification
     ↓
Architecture → Security Review → Governance Review
     ↓
Development → Code Review → Compliance Check
     ↓
Deployment → Security Scan → Production Approval
     ↓
Monitoring → Continuous Compliance
```

### Enterprise Quality Gates
- No critical/high vulnerabilities
- 80%+ code coverage
- All compliance controls passing
- Security architect sign-off
- Data governance sign-off

## Examples

### AI/ML Project
```bash
@orchestrator "Build a customer churn prediction model with GDPR compliance"
```
Auto-includes: sa-01 (PII), dg-01 (catalog), ml-01-05, mo-01-06

### RAG Application
```bash
@ai-engineer ai-02 "Create a RAG pipeline for internal docs"
```

### Security Review
```bash
@security-architect "Audit this codebase for security vulnerabilities"
```

### Enterprise Platform
```bash
@project-starter --enterprise "Build a customer data platform"
```
Auto-includes: ALL security + governance + compliance skills

## Integration Options

### Claude Code (Primary)
Skills are designed for Claude Code's `@` mention system.

### CrewAI
```python
from crewai import Agent, Task, Crew

orchestrator = Agent(
    role="Tech Hub Orchestrator",
    goal="Coordinate skills for optimal project execution",
    backstory=open(".claude/skills/orchestrator.md").read()
)
```

### LangGraph
```python
from langgraph.graph import StateGraph

# Load skills as node definitions
skills = load_skills(".claude/skills/")
```

## Integration Options

### Claude Code (Primary)
Skills are designed for Claude Code's `@` mention system.

### CrewAI
```python
from crewai import Agent, Task, Crew

orchestrator = Agent(
    role="Tech Hub Orchestrator",
    goal="Coordinate skills for optimal project execution",
    backstory=open(".claude/skills/orchestrator.md").read()
)
```

### LangGraph
```python
from langgraph.graph import StateGraph

# Load skills as node definitions
skills = load_skills(".claude/skills/")
```

## Repository Structure

```
.claude/
├── skills/                 # Role skill files (invoke with @role-name)
│   ├── orchestrator.md     # Main orchestrator - routes to all skills
│   ├── ai-engineer.md
│   ├── data-engineer.md
│   ├── security-architect.md
│   └── ...
├── roles/                  # Detailed skill implementations
│   ├── ai-engineer/
│   │   └── skills/
│   │       ├── 01-prompt-engineering/README.md
│   │       ├── 02-rag-pipeline/README.md
│   │       └── ...
│   └── ...
└── README.md               # This file
```

## Contributing

1. Fork the repository
2. Add skills to `roles/{role}/skills/{skill-id}/`
3. Update `skills/{role}.md`
4. Submit PR

For publishing instructions (maintainers only), see [../PUBLISHING.md](../PUBLISHING.md).

## License

MIT
