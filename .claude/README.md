# Tech Hub Skills

**180+ production-ready AI agent skills for Claude Code and GitHub Copilot**

[![npm version](https://badge.fury.io/js/tech-hub-skills.svg)](https://www.npmjs.com/package/tech-hub-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 v2.0: Agentic Architecture

**93% token reduction** - Only ~5-6k tokens at session start vs ~70k previously.

### Key Files

| File                      | Purpose                               | Tokens    |
| ------------------------- | ------------------------------------- | --------- |
| `skills/orchestrator.md`  | Single auto-loaded orchestrator skill | ~3k       |
| `skills-index.md`         | Compact index of all 200+ skills      | ~3-4k     |
| `skill-docs/*.md`         | Skill files (loaded on-demand)        | ~500 each |
| `templates/`              | Externalized code examples            | On-demand |

### How It Works

1. **ANALYZE** - Identify domain, compliance needs, complexity
2. **SELECT** - Match keywords to skills from index
3. **LOAD** - Read skill files from `skill-docs/` only when executing
4. **EXECUTE** - Apply guidance, reference templates

## Installation

```bash
# Install the package
npm install tech-hub-skills

# Install skills to your project's .claude folder
npx tech-hub-skills install

# Or install globally to ~/.claude
npx tech-hub-skills install --global

# With GitHub Copilot integration
npx tech-hub-skills install --copilot
```

## Quick Start

After installation, use the orchestrator in Claude Code:

```bash
# The orchestrator is the single entry point - it loads skills on-demand
/orchestrator "Build a customer churn prediction model"

# Examples:
/orchestrator "Create a RAG pipeline"
/orchestrator "Review this code for PII"
/orchestrator "Design a lakehouse architecture"

# Enterprise mode (mandatory security + governance)
/orchestrator --enterprise "Build a customer data platform"
```

The orchestrator will automatically:
1. Analyze your request
2. Select the appropriate skills
3. Load only the needed skill files (saving context)
4. Execute with full guidance

## Available Roles & Skills

### Core Engineering (48 skills)

| Role                   | Skills | Focus                                     |
| ---------------------- | ------ | ----------------------------------------- |
| **AI Engineer**        | 8      | LLMs, RAG, Agents, Guardrails, Embeddings |
| **Data Engineer**      | 9      | Lakehouse, ETL/ELT, Streaming, Quality    |
| **ML Engineer**        | 9      | MLOps, Training, Serving, Monitoring      |
| **Data Scientist**     | 8      | EDA, Modeling, Analytics, Experimentation |
| **Frontend Developer** | 7      | React/Vue/Angular, TypeScript, A11y       |
| **Backend Developer**  | 7      | REST, GraphQL, Microservices, Caching     |

### Architecture & Security (22 skills)

| Role                   | Skills | Focus                                  |
| ---------------------- | ------ | -------------------------------------- |
| **Security Architect** | 7      | PII, Threat Modeling, IAM, Secrets     |
| **System Design**      | 8      | Architecture, Scalability, HA/DR, APIs |
| **Network Engineer**   | 7      | Topology, VPN/VPC, Load Balancers, CDN |

### Platform & Operations (59 skills)

| Role                  | Skills | Focus                                 |
| --------------------- | ------ | ------------------------------------- |
| **Platform Engineer** | 6      | IDP, Self-Service, SLOs               |
| **SRE**               | 7      | Incident Response, Chaos Engineering  |
| **Database Admin**    | 7      | Query Optimization, Replication       |
| **Data Governance**   | 6      | Catalog, Lineage, Quality, Compliance |
| **DevOps**            | 9      | CI/CD, Containers, IaC, GitOps        |
| **MLOps**             | 9      | Experiments, Registry, Deployment     |
| **FinOps**            | 8      | Cost Visibility, Optimization         |
| **Docker**            | 5      | Containers, Security, Optimization    |

### Cloud Platforms (36 skills)

| Role      | Skills | Focus                           |
| --------- | ------ | ------------------------------- |
| **Azure** | 12     | All Azure services              |
| **AWS**   | 12     | EC2, Lambda, S3, RDS, VPC, EKS  |
| **GCP**   | 12     | Compute, BigQuery, GKE, Pub/Sub |

### Enterprise Governance (17 skills)

| Role                      | Skills     | Focus                               |
| ------------------------- | ---------- | ----------------------------------- |
| **Code Review**           | 5          | PR Automation, Quality Gates        |
| **Compliance Officer**    | 7          | SOC 2, GDPR, HIPAA, PCI-DSS         |
| **Compliance Automation** | Integrated | Policy-as-Code, Evidence Collection |

### Product, Design & Quality (19 skills)

| Role                 | Skills | Focus                      |
| -------------------- | ------ | -------------------------- |
| **Product Designer** | 6      | Requirements, Research, UX |
| **QA Engineer**      | 7      | Test Strategy, Automation  |
| **Technical Writer** | 6      | API Docs, ADRs, Runbooks   |

## CLI Commands

```bash
# Install skills to current project
npx tech-hub-skills install

# Install with GitHub Copilot integration
npx tech-hub-skills install --copilot

# Install globally
npx tech-hub-skills install --global

# Force overwrite existing installation
npx tech-hub-skills install --force

# Initialize with enterprise mode
npx tech-hub-skills init --enterprise

# List all available roles
npx tech-hub-skills list

# Show help
npx tech-hub-skills help
```

## Directory Structure (After Installation)

```
your-project/
└── .claude/
    ├── skills/                 # Auto-loaded skills (minimal)
    │   └── orchestrator.md     # Single entry point (~3k tokens)
    ├── skill-docs/             # On-demand skill files
    │   ├── ai-engineer.md
    │   ├── data-engineer.md
    │   ├── security-architect.md
    │   └── ... (40 role files)
    ├── skills-index.md         # Compact skill reference
    ├── roles/                  # Detailed skill implementations
    │   ├── ai-engineer/skills/
    │   ├── security-architect/skills/
    │   └── ...
    ├── templates/              # Code templates
    └── commands/               # CLI commands
        └── orchestrator.md     # /orchestrator command
```

## Enterprise Mode

For production applications, use Enterprise Mode:

```bash
/orchestrator --enterprise "Build a production API"
```

Enterprise Mode automatically includes:

- Security Architect (sa-01 to sa-07)
- Data Governance (dg-01 to dg-06)
- Code Review (cr-01 to cr-05)
- Compliance Automation

### Enterprise Quality Gates

- No critical/high vulnerabilities
- 80%+ code coverage
- All compliance controls passing
- Security architect sign-off
- Data governance sign-off

## Examples

### AI/ML Project

```bash
/orchestrator "Build a customer churn prediction model with GDPR compliance"
```

### RAG Application

```bash
/orchestrator "Create a RAG pipeline for internal docs"
```

### Security Review

```bash
/orchestrator "Audit this codebase for security vulnerabilities"
```

### Enterprise Platform

```bash
/orchestrator --enterprise "Build a customer data platform"
```

## Links

- [GitHub Repository](https://github.com/6ogo/Tech-Skills)
- [Issues](https://github.com/6ogo/Tech-Skills/issues)
- [Full Documentation](https://github.com/6ogo/Tech-Skills/blob/main/README.md)

## License

MIT
