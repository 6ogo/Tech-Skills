# Tech Hub Skills

[![npm version](https://img.shields.io/npm/v/tech-hub-skills.svg)](https://www.npmjs.com/package/tech-hub-skills)
[![npm downloads](https://img.shields.io/npm/dm/tech-hub-skills.svg)](https://www.npmjs.com/package/tech-hub-skills)
[![License](https://img.shields.io/npm/l/tech-hub-skills.svg)](https://github.com/6ogo/Tech-Skills/blob/main/LICENSE)

**200+ production-ready AI agent skills** for **Claude Code** and **GitHub Copilot**.

Features a **hierarchical multi-agent system** with a **Brainstorm → Plan → Implement** workflow, 95% token efficiency, and advanced domain expertise.

## Quick Install

### For Claude Code (CLI)

```bash
# Install to your current project
npx tech-hub-skills install
```

### For GitHub Copilot (VSCode)

```bash
# Install with VSCode instructions
npx tech-hub-skills install --copilot
```

This creates `.github/copilot-instructions.md` with all expert skills.

### Global Install (Optional)

```bash
# Install globally for all projects
npx tech-hub-skills install --global
```

## 🧠 v2.2: Hierarchical Agent Architecture

**95% token reduction** with on-demand skill loading and intelligent coordination.

### Multi-Agent Hierarchy

1.  **Orchestrator Agent** (visible) - The master coordinator. Analyzes requests, brainstorms approaches, and creates execution plans.
2.  **5 Lead Agents** (visible) - Domain experts for AI/ML, Platform, Security, Data, and Product development.
3.  **25 Specialist Agents** (internal) - Deep technical specialists (e.g., AI Engineer, MLOps, SRE) loaded dynamically by Leads.

### Workflow: Brainstorm → Plan → Implement

- **Brainstorm**: Understands requirements, constraints, and risks BEFORE acting.
- **Plan**: Scans registries to select ONLY the needed skills (typically 3-7 per task).
- **Implement**: Executes step-by-step with validation checkpoints and adaptive planning.

## What's Included

- **200+ Skills**: LLMs, RAG, MLOps, DevSecOps, Lakehouse, Cloud (AWS/Azure/GCP), and more.
- **Lazy-Loading**: Significant token savings via [SKILL-REGISTRY.md](.claude/agents/SKILL-REGISTRY.md) and [ROLE-REGISTRY.md](.claude/agents/ROLE-REGISTRY.md).
- **Security First**: Built-in PII detection, security hardening, and compliance automation.
- **Cost Aware**: AI/ML cost optimization (fo-07) and efficient tool usage.

## Usage

### Claude Code - Slash Commands

Route directly to the master coordinator or domain leads:

```bash
# Recommend entry point (Full Workflow)
/orchestrator "Build a customer churn prediction model with GDPR compliance"

# Domain specific (Interactive)
/ai "Create a RAG pipeline for internal documentation"
/platform "Deploy current service to Production GKE with CI/CD"
/security "Scan the workspace for PII and vulnerabilities"
/data "Design a Medallion architecture for raw telemetry data"
/product "Build a React dashboard with full unit tests"
```

### GitHub Copilot

Copilot automatically applies expert knowledge via instructions. Reference roles in comments to steer:

```python
# Using AI Engineer approach for RAG pipeline
def build_rag_system():
    # Copilot suggests: adaptive chunking, hybrid search, etc.
    pass

# Apply Security Architect best practices
def handle_user_upload(file_data):
    # Copilot adds: PII scan, malware check, sanitization
    pass
```

## Available Lead Roles

| Lead              | Domain                 | Specialists                                                       |
| ----------------- | ---------------------- | ----------------------------------------------------------------- |
| **AI/ML Lead**    | AI, ML, Data Science   | AI Engineer, ML Engineer, Data Scientist, MLOps                   |
| **Platform Lead** | Infrastructure, DevOps | DevOps, SRE, Platform Eng, Network, Docker, AWS/Azure/GCP, FinOps |
| **Security Lead** | Security, Compliance   | Security Architect, Compliance Officer, Security Hardener         |
| **Data Lead**     | Data Engineering       | Data Engineer, Data Governance, Database Admin                    |
| **Product Lead**  | Product Development    | Product Designer, Frontend/Backend Dev, QA, Tech Writer           |

## Directory Structure

```
your-project/
└── .claude/
    ├── agents/
    │   ├── orchestrator-agent.md     # Master coordinator
    │   ├── ai-ml-lead.md             # Visible Lead
    │   ├── ...                       # Other visible Leads (5 total)
    │   ├── SKILL-REGISTRY.md         # Lazy-load index
    │   ├── ROLE-REGISTRY.md          # Role lookup
    │   └── specialists/              # 25 Specialists (internal)
    ├── skills/                       # Skill summaries
    ├── skill-docs/                   # Full skill documentation
    ├── commands/                     # Slash command definitions
    └── settings.json                 # System configuration
```

## Documentation

- **Agent System**: [.claude/AGENTS.md](.claude/AGENTS.md)
- **GitHub Copilot**: [GITHUB_COPILOT.md](GITHUB_COPILOT.md)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)

## License

MIT
