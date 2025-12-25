# Tech Hub Skills for Claude Code

110+ production-ready AI agent skills for Claude Code. Enterprise-grade with security, governance, and compliance built-in.

## Quick Install

### npm / npx (Recommended)
```bash
# Install to current project
npx tech-hub-skills install

# Install globally for all projects
npx tech-hub-skills install --global

# Enterprise mode setup
npx tech-hub-skills init --enterprise
```

### pip
```bash
pip install tech-hub-skills
tech-hub-skills install
```

### Manual Installation

```bash
# Clone and copy .claude folder to your project
git clone https://github.com/6ogo/tech-hub-skills.git
cp -r tech-hub-skills/.claude your-project/
```

## What's Included

- **26 Role Skills**: AI Engineer, Data Engineer, Security Architect, DevOps, and more
- **110+ Detailed Implementations**: Step-by-step guides for each skill
- **Enterprise Mode**: Built-in security, governance, and compliance
- **Cross-Platform**: Works on Windows, macOS, Linux

## Available Roles

| Role | Skills | Focus |
|------|--------|-------|
| **AI Engineer** | 8 | LLMs, RAG, Agents, Guardrails, Embeddings |
| **Data Engineer** | 9 | Lakehouse, ETL/ELT, Streaming, Quality |
| **ML Engineer** | 9 | MLOps, Training, Serving, Monitoring |
| **Data Scientist** | 8 | EDA, Modeling, Analytics, Experimentation |
| **Security Architect** | 7 | PII, Threat Modeling, IAM, Secrets |
| **System Design** | 8 | Architecture, Scalability, HA/DR, APIs |
| **Platform Engineer** | 6 | IDP, Self-Service, SLOs |
| **Data Governance** | 6 | Catalog, Lineage, Quality, Compliance |
| **DevOps** | 9 | CI/CD, Containers, IaC, GitOps |
| **MLOps** | 9 | Experiments, Registry, Deployment |
| **FinOps** | 8 | Cost Visibility, Optimization |
| **Azure** | 12 | All Azure services |
| **Code Review** | 5 | PR Automation, Quality Gates |
| **Product Designer** | 6 | Requirements, Research, UX |

See [.claude/README.md](.claude/README.md) for detailed role documentation.

## Usage in Claude Code

1. Open your project in Claude Code
2. Use `@` mentions to invoke skills:

```bash
# Start with the orchestrator
@orchestrator "Build a customer churn prediction model"

# Or use specific roles
@ai-engineer "Create a RAG pipeline"
@security-architect "Review this code for PII"
@data-engineer "Design a lakehouse architecture"
```

## Updating

### Method 1 (Clone/ZIP)
```bash
# Pull latest changes
cd path/to/tech-hub-skills
git pull

# Copy updated files
cp -r .claude your-project/
```

After installation, use skills with `@` mentions:

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

## Examples

**AI/ML Project**
```bash
@orchestrator "Build a customer churn prediction model with GDPR compliance"
```

**RAG Application**
```bash
@ai-engineer "Create a RAG pipeline for internal docs"
```

**Security Review**
```bash
@security-architect "Audit this codebase for security vulnerabilities"
```

**Enterprise Platform**
```bash
@project-starter --enterprise "Build a customer data platform"
```

## Documentation

- **All Roles**: See [.claude/README.md](.claude/README.md) for complete role documentation
- **Publishing**: See [PUBLISHING.md](PUBLISHING.md) for maintainer instructions

## Contributing

1. Fork the repository
2. Add skills to `.claude/roles/{role}/skills/{skill-id}/`
3. Update `.claude/skills/{role}.md`
4. Submit PR

## License

MIT