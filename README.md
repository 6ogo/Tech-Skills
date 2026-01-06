# Tech Hub Skills

**200+ production-ready AI agent skills** for **Claude Code** and **GitHub Copilot**.

[![npm version](https://img.shields.io/npm/v/tech-hub-skills.svg)](https://www.npmjs.com/package/tech-hub-skills)
[![npm downloads](https://img.shields.io/npm/dm/tech-hub-skills.svg)](https://www.npmjs.com/package/tech-hub-skills)
[![License](https://img.shields.io/npm/l/tech-hub-skills.svg)](https://github.com/6ogo/Tech-Skills/blob/main/LICENSE)

Features a **hierarchical multi-agent system** with a **Brainstorm → Plan → Implement** workflow, 95% token efficiency, advanced domain expertise, and **comprehensive safety guardrails** for damage control.

## Quick Install

### For Claude Code (CLI)

```bash
npx tech-hub-skills install
```

### For GitHub Copilot (VSCode)

```bash
npx tech-hub-skills install --copilot
```

_This creates `.github/copilot-instructions.md` with all expert skills._

---

## v2.2: Hierarchical Agent Architecture

**95% token reduction** with on-demand skill loading and intelligent coordination.

### Multi-Agent Hierarchy

1.  **Orchestrator Agent** (visible) - The master coordinator. Analyzes requests, brainstorms approaches, and creates execution plans.
2.  **5 Lead Agents** (visible) - Domain experts for AI/ML, Platform, Security, Data, and Product development.
3.  **25 Specialist Agents** (internal) - Deep technical specialists (e.g., AI Engineer, MLOps, SRE) loaded dynamically by Leads.

### Workflow: Brainstorm → Plan → Implement

- **Brainstorm**: Understands requirements, constraints, and risks BEFORE acting.
- **Plan**: Scans registries to select ONLY the needed skills (typically 3-7 per task).
- **Implement**: Executes step-by-step with validation checkpoints and adaptive planning.

---

## What's Included

- **200+ Skills**: LLMs, RAG, MLOps, DevSecOps, Lakehouse, Cloud (AWS/Azure/GCP), and more.
- **Lazy-Loading**: Significant token savings via internal skill registries.
- **Security First**: Built-in PII detection, security hardening, and compliance automation.
- **Safety Guardrails**: File deletion protection, database safety, credential protection, automatic backups, and audit logging.
- **Cost Aware**: AI/ML cost optimization and efficient tool usage.

## Usage

### Claude Code - Slash Commands

Route directly to the master coordinator or domain leads:

```bash
# Recommended entry point (Full Workflow)
/orchestrator "Build a customer churn prediction model"

# Domain specific
/ai       # AI, ML, and Data Science
/platform # DevOps and Cloud Infrastructure
/security # Security and Compliance
/data     # Data Engineering
/product  # Full-stack Development
```

### GitHub Copilot

Copilot automatically applies expert knowledge via instructions. Reference roles in comments to steer:

```python
# Using AI Engineer approach for RAG pipeline
def build_rag_system():
    pass

# Apply Security Architect best practices
def handle_user_upload(file_data):
    pass
```

## Available Lead Roles

| Lead              | Domain                 | Specialists                                               |
| ----------------- | ---------------------- | --------------------------------------------------------- |
| **AI/ML Lead**    | AI, ML, Data Science   | AI Engineer, ML Engineer, Data Scientist, MLOps           |
| **Platform Lead** | Infrastructure, DevOps | DevOps, SRE, Platform Eng, Network, Docker, Cloud, FinOps |
| **Security Lead** | Security, Compliance   | Security Architect, Compliance Officer, Security Hardener |
| **Data Lead**     | Data Engineering       | Data Engineer, Data Governance, Database Admin            |
| **Product Lead**  | Product Development    | Product Designer, Frontend/Backend Dev, QA, Tech Writer   |

## Documentation

- **Full System**: [AGENTS.md](https://github.com/6ogo/Tech-Skills/blob/main/.claude/AGENTS.md)
- **Safety Guardrails**: [SAFETY-GUARDRAILS.md](https://github.com/6ogo/Tech-Skills/blob/main/SAFETY-GUARDRAILS.md)
- **GitHub Copilot Guide**: [GITHUB_COPILOT.md](https://github.com/6ogo/Tech-Skills/blob/main/GITHUB_COPILOT.md)
- **Changelog**: [CHANGELOG.md](https://github.com/6ogo/Tech-Skills/blob/main/CHANGELOG.md)

## License

MIT
