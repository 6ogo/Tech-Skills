# Changelog

All notable changes to Tech Hub Skills will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.8.1] - 2024-12-30

### 🚀 Context-Efficient Loading & New Skills

This release adds **MCP server management**, **lazy-loading registries**, and **24 new advanced skills** to make agents more efficient and expert-level.

### Added

#### MCP Server Management (NEW)

- **mcp-management.md** - 5 skills for dynamic MCP server lifecycle
- **mcp-manager-agent.md** - Specialist agent for tool management
- `/mcp` command - Activate/deactivate servers, optimize context
- Agents now activate MCP servers on-demand and deactivate immediately after use

#### Lazy-Loading Registries (NEW)

- **SKILL-REGISTRY.md** - Lightweight index of ALL ~175 skills by keyword
- **ROLE-REGISTRY.md** - Lightweight index of ALL 25 roles by keyword
- Agents scan registries (~200 tokens) instead of loading all skills (~50,000 tokens)
- **95%+ token savings** while maintaining expert knowledge

#### Advanced AI Skills (ai-09 to ai-13)

- **ai-09: Fine-Tuning** - LoRA, QLoRA, PEFT, custom models
- **ai-10: Multimodal AI** - Vision, audio, video, document understanding
- **ai-11: AI Agents 2.0** - MCP integration, advanced planning, memory
- **ai-12: Local LLMs** - Ollama, vLLM, on-prem deployment
- **ai-13: Synthetic Data** - Training data generation

#### Advanced Security Skills (sa-08 to sa-11)

- **sa-08: API Security** - OAuth2, OIDC, JWT, API gateways
- **sa-09: Supply Chain Security** - SBOM, Sigstore, SLSA
- **sa-10: Zero Trust** - Never trust, always verify architecture
- **sa-11: CSPM** - Cloud security posture management

#### Advanced Data Engineering Skills (de-10 to de-13)

- **de-10: Reverse ETL** - Warehouse → operational systems
- **de-11: Data Contracts** - Schema enforcement, SLAs
- **de-12: Semantic Layer** - Consistent metrics definitions
- **de-13: Data Mesh** - Domain ownership, federation

#### Context Optimization Skills (ctx-01 to ctx-06)

- **ctx-01: Lazy Loading** - File/code reading efficiency
- **ctx-02: Database Optimization** - Minimal SQL queries
- **ctx-03: API Optimization** - Paginate, filter, cache
- **ctx-04: MCP Efficiency** - Server activation patterns
- **ctx-05: Caching Strategies** - Reduce repeated fetches
- **ctx-06: Progressive Disclosure** - Load incrementally

### Changed

- Updated **orchestrator-agent.md** with context-efficient loading instructions
- Updated **AGENTS.md** with registry references
- Updated **SKILL-REFERENCE.md** with all new skills

### Skill Count Update

| Category           | Previous | New | Total    |
| ------------------ | -------- | --- | -------- |
| AI/ML Skills       | 8        | 5   | 13       |
| Security Skills    | 7        | 4   | 11       |
| Data Eng Skills    | 9        | 4   | 13       |
| MCP/Context Skills | 0        | 11  | 11       |
| **Total Skills**   | ~150     | +24 | **~175** |

---

## [1.8.0] - 2024-12-30

### 🎯 Major Feature: Hierarchical Multi-Agent System

This release introduces a complete **multi-agent architecture** where expert agents collaborate to solve complex problems. The system works like a professional engineering team with clear roles, delegation, and expertise areas.

### Added

#### Agent System (34 new files)

- **Orchestrator Agent** - Master coordinator that analyzes requests and routes to appropriate leads
- **5 Lead Agents**:
  - 🤖 AI/ML Lead - Coordinates AI Engineer, ML Engineer, Data Scientist, MLOps
  - ⚙️ Platform Lead - Coordinates DevOps, SRE, Platform Engineer, Network, Docker, AWS/Azure/GCP, FinOps
  - 🔒 Security Lead - Coordinates Security Architect, Compliance Officer, Security Hardener
  - 📊 Data Lead - Coordinates Data Engineer, Data Governance, Database Admin
  - 📦 Product Lead - Coordinates Product Designer, Frontend/Backend Dev, QA, Technical Writer
- **24 Specialist Agents** - One per role with skills, collaborations, and automation thresholds
- **EXECUTION.md** - Agent coordination protocol with cross-agent communication
- **SKILL-REFERENCE.md** - Complete skill lookup table (~150 skills)

#### Integration

- **settings.json** - Configuration for Claude Code
- **QUICKSTART.md** - Usage guide for the agent system
- **5 Slash Commands** for direct agent routing:
  - `/ai` - Route to AI/ML Lead
  - `/platform` - Route to Platform Lead
  - `/security` - Route to Security Lead
  - `/data` - Route to Data Lead
  - `/product` - Route to Product Lead
- Updated **copilot.js** with agent system architecture for GitHub Copilot

#### Smart Automation

- Agents automatically decide when to auto-execute vs. ask for approval
- Mandatory collaboration rules enforced:
  - Security Lead for ALL PII/production work
  - FinOps for ALL cloud resources
  - QA for ALL code changes

### How to Use

**Claude Code:**

```
/ai build a RAG chatbot
/security scan for PII
/platform deploy to kubernetes
```

**GitHub Copilot:**

```bash
npx tech-hub-skills install --copilot
```

### Skill Count

- Total Skills: **200+**
- Total Agents: **30** (1 orchestrator, 5 leads, 24 specialists)
- Total Roles: **24**

---

## [1.7.0] - 2024-12-26

### Added

- Project lifecycle agents: Project Guardian, Code Hardener, Security Hardener, Maintenance Engineer, Development Accelerator
- Enhanced skill triggers and anti-patterns for all roles
- Improved collaboration rules between agents

## [1.6.0] - 2024-12-25

### Added

- Process management skills: Kanban, Documentation, Changelog, Versioning
- FinOps specialist with 8 cost optimization skills
- Enterprise dashboard and compliance automation

## [1.5.0] - 2024-12-24

### Added

- Initial npm and PyPI publishing
- GitHub Copilot integration via copilot-instructions.md
- CLI tools for installation

---

[1.8.1]: https://github.com/6ogo/Tech-Skills/releases/tag/v1.8.1
[1.8.0]: https://github.com/6ogo/Tech-Skills/releases/tag/v1.8.0
[1.7.0]: https://github.com/6ogo/Tech-Skills/releases/tag/v1.7.0
[1.6.0]: https://github.com/6ogo/Tech-Skills/releases/tag/v1.6.0
[1.5.0]: https://github.com/6ogo/Tech-Skills/releases/tag/v1.5.0
