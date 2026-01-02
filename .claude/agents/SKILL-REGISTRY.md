# Skill Registry - Lightweight Index

**Purpose**: Agents reference this compact index to find skills. Load FULL skill docs ONLY when executing.

## 🎯 How Agents Use This

```yaml
1. Agent receives task
2. Scan this INDEX for relevant skills (by keyword/trigger)
3. Identify skill IDs needed
4. Load ONLY those skill files when executing
5. Unload after task complete
```

---

## Quick Lookup Tables

### By Domain

| Domain       | Lead           | Skill Files                                     | Skill IDs              |
| ------------ | -------------- | ----------------------------------------------- | ---------------------- |
| AI/ML        | @ai-ml-lead    | `ai-engineer.md`, `ai-engineer-advanced.md`     | ai-01 to ai-13         |
| ML           | @ai-ml-lead    | `ml-engineer.md`                                | ml-01 to ml-09         |
| Data Science | @ai-ml-lead    | `data-scientist.md`                             | ds-01 to ds-08         |
| MLOps        | @ai-ml-lead    | `mlops.md`                                      | mo-01 to mo-09         |
| DevOps       | @platform-lead | `devops.md`                                     | do-01 to do-09         |
| SRE          | @platform-lead | `sre.md`                                        | sr-01 to sr-07         |
| Docker       | @platform-lead | `docker.md`                                     | docker-01 to docker-05 |
| AWS          | @platform-lead | `aws.md`                                        | aws-01 to aws-12       |
| Azure        | @platform-lead | `azure.md`                                      | az-01 to az-12         |
| GCP          | @platform-lead | `gcp.md`                                        | gcp-01 to gcp-12       |
| Security     | @security-lead | `security-architect.md`, `security-advanced.md` | sa-01 to sa-11         |
| Compliance   | @security-lead | `compliance-officer.md`                         | co-01 to co-07         |
| Data Eng     | @data-lead     | `data-engineer.md`, `data-engineer-advanced.md` | de-01 to de-13         |
| Data Gov     | @data-lead     | `data-governance.md`                            | dg-01 to dg-06         |
| Database     | @data-lead     | `database-admin.md`                             | db-01 to db-07         |
| Product      | @product-lead  | `product-designer.md`                           | pd-01 to pd-06         |
| Frontend     | @product-lead  | `frontend-developer.md`                         | fe-01 to fe-07         |
| Backend      | @product-lead  | `backend-developer.md`                          | be-01 to be-07         |
| QA           | @product-lead  | `qa-engineer.md`                                | qa-01 to qa-07         |
| Tech Writer  | @product-lead  | `technical-writer.md`                           | tw-01 to tw-06         |
| FinOps       | @platform-lead | `finops.md`                                     | fo-01 to fo-08         |
| MCP          | @orchestrator  | `mcp-management.md`                             | mcp-01 to mcp-05       |
| Context      | @orchestrator  | `context-optimization.md`                       | ctx-01 to ctx-06       |

---

## Keyword → Skill Mapping

### AI & LLM Keywords

```yaml
chatbot, LLM, GPT, Claude: → ai-01, ai-02, ai-03
RAG, retrieval, knowledge base: → ai-02, ai-05
fine-tune, LoRA, custom model: → ai-09
multimodal, vision, audio: → ai-10
agent, MCP, tool use, planning: → ai-11
local LLM, Ollama, on-prem: → ai-12
synthetic data, generate training: → ai-13
```

### Data Keywords

```yaml
pipeline, ETL, lakehouse: → de-01, de-02
streaming, Kafka, real-time: → de-04
data quality, validation: → de-03, dg-03
reverse ETL, activation: → de-10
data contract, schema: → de-11
metrics, semantic layer: → de-12
data mesh, federation: → de-13
```

### Security Keywords

```yaml
PII, personal data, privacy: → sa-01
threat model, STRIDE: → sa-02
IAM, RBAC, permissions: → sa-04
OWASP, AppSec: → sa-05
secrets, vault, keys: → sa-06
OAuth, OIDC, JWT, API auth: → sa-08
SBOM, supply chain, Sigstore: → sa-09
zero trust: → sa-10
CSPM, cloud security: → sa-11
```

### DevOps Keywords

```yaml
CI/CD, pipeline, deploy: → do-01
Kubernetes, K8s, containers: → do-02
Terraform, IaC, Bicep: → do-03
GitOps, ArgoCD: → do-04
monitoring, alerting: → do-08
security scan, DevSecOps: → do-09
```

### Platform Keywords

```yaml
SRE, incident, reliability: → sr-01 to sr-07
SLO, error budget: → sr-03, sr-04
cost, FinOps, optimization: → fo-01 to fo-08
```

---

## Loading Protocol

### When task arrives:

```yaml
step_1_scan_keywords:
  action: "Match task keywords to this index"
  context_cost: "~200 tokens (this file only)"

step_2_identify_skills:
  action: "List matching skill IDs"
  example: "Task mentions 'RAG chatbot' → ai-02, ai-04, sa-01"

step_3_load_on_demand:
  action: "Load ONLY needed skill files"
  command: "read_file('.claude/skills/ai-engineer.md')"

step_4_execute:
  action: "Apply skill knowledge to task"

step_5_unload:
  action: "Don't retain full skill docs in memory"
  why: "Save context for next task"
```

### What NOT to do:

```yaml
❌ WRONG: Load all skill files at start
   → Wastes 50,000+ tokens

❌ WRONG: Keep skill files loaded after use
   → Fills context unnecessarily

❌ WRONG: Guess skill IDs without checking index
   → May miss relevant skills

✅ RIGHT: Scan index → identify → load → execute → unload
```

---

## File Paths

All skills are in `.claude/skills/`:

```
.claude/skills/
├── ai-engineer.md          # ai-01 to ai-08
├── ai-engineer-advanced.md  # ai-09 to ai-13
├── ml-engineer.md          # ml-01 to ml-09
├── data-scientist.md       # ds-01 to ds-08
├── data-engineer.md        # de-01 to de-09
├── data-engineer-advanced.md # de-10 to de-13
├── security-architect.md   # sa-01 to sa-07
├── security-advanced.md    # sa-08 to sa-11
├── devops.md              # do-01 to do-09
├── mcp-management.md      # mcp-01 to mcp-05
├── context-optimization.md # ctx-01 to ctx-06
├── ... (all other skills)
```

---

## Agent Responsibilities

### Orchestrator

- Maintains awareness of this index
- Routes to appropriate leads
- Never loads all skills at once

### Lead Agents

- Know their domain's skill files
- Load only when specialists need them
- Coordinate cross-domain loading

### Specialists

- Request specific skills via ID
- Load → Execute → Report → Unload
- Minimize context footprint

---

## Example Flow

```yaml
task: "Build a RAG chatbot with security"

orchestrator:
  1. Scan index for: "RAG", "chatbot", "security"
  2. Match: ai-02, ai-04, sa-01
  3. Route to: @ai-ml-lead, @security-lead

ai_ml_lead:
  1. Load: ai-engineer.md (only ai-02, ai-04 sections)
  2. Delegate to @ai-engineer-agent
  3. Execute skills
  4. Unload skill file

security_lead:
  1. Load: security-architect.md (only sa-01 section)
  2. Delegate to @security-architect-agent
  3. Execute PII detection
  4. Unload skill file

result:
  - Context used: ~1,500 tokens (vs 50,000+ if all loaded)
  - Skills applied: 3 specific skills
  - Knowledge: Expert-level for those 3 skills
```
