# Changelog

All notable changes to Tech Hub Skills will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-01-02

### 🚀 BREAKING CHANGE: Agentic Architecture - 93% Token Reduction

This major release completely redesigns the skill loading architecture to reduce session startup from **~70k tokens to ~5-6k tokens** (93% reduction) while maintaining access to all 200+ skills.

### The Problem (v1.x)

Previous versions loaded all skill files at session start, consuming significant context window:
- ~50 agent/skill files loaded upfront
- ~70,000 tokens consumed before any work began
- Limited context remaining for actual tasks

### The Solution (v2.0)

New **on-demand loading architecture**:
- Only orchestrator + skills index loaded at startup (~5-6k tokens)
- Skills loaded dynamically when needed
- Code templates externalized to separate files

### Added

#### Core Architecture Files

- **skills/orchestrator.md** - Single entry point with ANALYZE→SELECT→LOAD→EXECUTE workflow
- **skills-index.md** - Compact keyword-based index of all 200+ skills (~3-4k tokens)
- **skill-docs/** - 40 role skill files loaded on-demand (~500 tokens each)

#### Externalized Templates

- **templates/compliance/** - checker.py, policies.yml, workflow.yml
- **templates/dashboard/** - grafana.json, alerts.yml, generator.py

### Changed

#### Massive File Reduction

| Category | Before | After | Reduction |
|----------|--------|-------|-----------|
| Agent definitions | 25 files | 0 files | -100% |
| Command files | 40+ files | 1 file | -97% |
| Skill files | Inline | External | -88% avg |
| **Total lines** | ~25,000 | ~2,500 | **-90%** |

#### Specific Files

- `compliance-automation.md`: 748 → 80 lines (89% reduction)
- `enterprise-dashboard.md`: 614 → 75 lines (88% reduction)
- `orchestrator.md`: Consolidated from 600+ lines across multiple files

### Removed

- `.claude/agents/` - All 25 individual agent definitions
- `.claude/agents/leads/` - 5 lead agent files
- `.claude/agents/specialists/` - 24 specialist agent files
- `.claude/commands/*.md` - 40+ heavyweight command files
- `.claude/AGENTS.md` - Replaced by skills-index.md
- `.claude/QUICKSTART.md` - Replaced by README.md
- `.claude/settings.json` - No longer needed

### How It Works

```
Session Start (~5-6k tokens)
├── skills/orchestrator.md     # Core workflow
└── skills-index.md            # Compact skill lookup

On-Demand (when skill invoked)
├── skill-docs/{role}.md       # Skill guidance
└── templates/{category}/      # Code examples
```

**Workflow:**
1. **ANALYZE** - Orchestrator identifies domain, complexity, compliance needs
2. **SELECT** - Matches keywords to skills from compact index
3. **LOAD** - Reads full skill files only when executing
4. **EXECUTE** - Applies guidance, references templates

### Migration from v1.x

No action required. The new architecture is backward compatible:
- Same `/orchestrator` command works
- All 200+ skills still available
- Skills load transparently when needed

### Usage

```bash
# Install/update
npx tech-hub-skills install

# Use orchestrator (recommended)
/orchestrator "Build a customer churn prediction model"

# Direct role commands still work
/ai-engineer "Create a RAG pipeline"
/security-architect "Review for PII"
```

---

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

[2.0.0]: https://github.com/6ogo/Tech-Skills/releases/tag/v2.0.0
[1.8.1]: https://github.com/6ogo/Tech-Skills/releases/tag/v1.8.1
[1.8.0]: https://github.com/6ogo/Tech-Skills/releases/tag/v1.8.0
[1.7.0]: https://github.com/6ogo/Tech-Skills/releases/tag/v1.7.0
[1.6.0]: https://github.com/6ogo/Tech-Skills/releases/tag/v1.6.0
[1.5.0]: https://github.com/6ogo/Tech-Skills/releases/tag/v1.5.0
