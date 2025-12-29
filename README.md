# Tech Hub Skills

[![npm version](https://img.shields.io/npm/v/tech-hub-skills.svg)](https://www.npmjs.com/package/tech-hub-skills)
[![npm downloads](https://img.shields.io/npm/dm/tech-hub-skills.svg)](https://www.npmjs.com/package/tech-hub-skills)
[![npm total downloads](https://img.shields.io/npm/dt/tech-hub-skills.svg)](https://www.npmjs.com/package/tech-hub-skills)
[![License](https://img.shields.io/npm/l/tech-hub-skills.svg)](https://github.com/6ogo/Tech-Skills/blob/main/LICENSE)


**Over 30 expert roles and 200+ production-ready AI agent skills for Claude Code and GitHub Copilot.**

Enterprise-grade: security, governance, and compliance built-in.

## Quick Install

### For Claude Code

```bash
# npm/npx
npx tech-hub-skills install
```

### For GitHub Copilot (VSCode)

```bash
# npm/npx
npx tech-hub-skills install --copilot
```

This creates `.github/copilot-instructions.md` with all expert skills.
See [GITHUB_COPILOT.md](https://github.com/6ogo/Tech-Skills/blob/main/GITHUB_COPILOT.md) for usage guide.

### Global Install (Claude Code only)

```bash
# Install globally for all projects
npx tech-hub-skills install --global
```

### Manual Installation

```bash
# Clone and copy .claude folder to your project
git clone https://github.com/6ogo/Tech-Skills.git
cp -r tech-hub-skills/.claude your-project/
```


## What's Included

- **30+ Expert Roles**: AI Engineer, Data Engineer, Security Architect, DevOps, SRE, QA, Product Designer, Technical Writer, and more
- **200+ Detailed Skills**: Step-by-step, production-ready implementations for each role
- **Enterprise Mode**: Security, governance, and compliance by default
- **Cross-Platform**: Windows, macOS, Linux


## Available Roles (2025)

| Role                   | Skills | Focus                                       |
|------------------------|--------|---------------------------------------------|
| **AI Engineer**        | 8      | LLMs, RAG, Agents, Guardrails, Embeddings   |
| **Data Engineer**      | 9      | Lakehouse, ETL/ELT, Streaming, Quality      |
| **ML Engineer**        | 9      | MLOps, Training, Serving, Monitoring        |
| **Data Scientist**     | 8      | EDA, Modeling, Analytics, Experimentation   |
| **Frontend Developer** | 7      | React/Vue/Angular, TypeScript, A11y         |
| **Backend Developer**  | 7      | REST, GraphQL, Microservices, Caching       |
| **Security Architect** | 7      | PII, Threat Modeling, IAM, Secrets          |
| **System Design**      | 8      | Architecture, Scalability, HA/DR, APIs      |
| **Network Engineer**   | 7      | Topology, VPN/VPC, Load Balancers, CDN      |
| **Platform Engineer**  | 6      | IDP, Self-Service, SLOs                     |
| **SRE**                | 7      | Incident Response, Chaos Engineering, SLOs  |
| **Database Admin**     | 7      | Query Optimization, Replication, Migrations |
| **Data Governance**    | 6      | Catalog, Lineage, Quality, Compliance       |
| **DevOps**             | 9      | CI/CD, Containers, IaC, GitOps              |
| **Docker**             | 5      | Dockerfile, Security, Optimization          |
| **MLOps**              | 9      | Experiments, Registry, Deployment           |
| **FinOps**             | 8      | Cost Visibility, Optimization               |
| **Azure**              | 12     | All Azure services                          |
| **AWS**                | 12     | EC2, Lambda, S3, RDS, VPC, EKS              |
| **GCP**                | 12     | Compute, BigQuery, GKE, Pub/Sub             |
| **Code Review**        | 5      | PR Automation, Quality Gates                |
| **Compliance Officer** | 7      | SOC 2, GDPR, HIPAA, PCI-DSS                 |
| **QA Engineer**        | 7      | Test Strategy, Automation, Performance      |
| **Technical Writer**   | 6      | API Docs, ADRs, Runbooks                    |
| **Product Designer**   | 6      | Requirements, Research, UX                  |
| **Project Starter**    | 3      | Guided project setup, enterprise onboarding |
| **Process Automation** | 4      | Changelog, Kanban, Versioning, Docs         |
| **Optimization Advisor**| 3     | Cost, performance, architecture             |
| **Enterprise Dashboard**| 2     | Reporting, metrics, visualization           |

See [.claude/README.md](https://github.com/6ogo/Tech-Skills/blob/main/.claude/README.md) for detailed role documentation.

## Usage

### Claude Code

Use `/` mentions to invoke specific expert roles:

```bash
# Start with the orchestrator
/orchestrator "Build a customer churn prediction model"

# Or use specific roles
/ai-engineer "Create a RAG pipeline"
/security-architect "Review this code for PII"
/data-engineer "Design a lakehouse architecture"
```

### GitHub Copilot

Copilot automatically applies expert knowledge. Reference roles in comments:

```python
# Using AI Engineer approach for RAG pipeline
def build_rag():
    # Copilot suggests best practices

# Apply Security Architect principles
def process_data(user_input):
    # Copilot adds input validation, PII scanning
```

See [GITHUB_COPILOT.md](https://github.com/6ogo/Tech-Skills/blob/main/GITHUB_COPILOT.md) for complete guide.

## Updating

### Method 1 (Clone/ZIP)

```bash
# Pull latest changes
cd path/to/tech-hub-skills
git pull

# Copy updated files
cp -r .claude your-project/
```

After installation, use skills with `/` mentions:

```bash
# Start with the orchestrator (routes to all skills)
/orchestrator "Build a customer churn prediction model"

# Or invoke specific roles
/ai-engineer "Create a RAG pipeline"
/security-architect "Review this code for PII"
/data-engineer "Design a lakehouse architecture"

# Enterprise mode (mandatory security + governance)
/project-starter --enterprise "Build a customer data platform"
```

## Examples

**AI/ML Project**

```bash
/orchestrator "Build a customer churn prediction model with GDPR compliance"
```

**RAG Application**

```bash
/ai-engineer "Create a RAG pipeline for internal docs"
```

**Security Review**

```bash
/security-architect "Audit this codebase for security vulnerabilities"
```

**Enterprise Platform**

```bash
/project-starter --enterprise "Build a customer data platform"
```

## Documentation

- **All Roles**: See [.claude/README.md](https://github.com/6ogo/Tech-Skills/blob/main/.claude/README.md) for complete role documentation

## Contributing

1. Fork the repository
2. Add skills to `.claude/roles/{role}/skills/{skill-id}/`
3. Update `.claude/skills/{role}.md`
4. Submit PR

## License

MIT
