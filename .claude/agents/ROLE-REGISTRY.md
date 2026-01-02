# Role Registry - Lightweight Index

**Purpose**: Agents reference this compact index to understand all roles. Load FULL role docs ONLY when needed.

## How This Works

```yaml
1. Agent receives task
2. Scan this INDEX for relevant roles
3. Identify which specialists to involve
4. Load ONLY those role files when delegating
5. Unload after task complete
```

---

## Role Index

### AI/ML Domain (Lead: @ai-ml-lead)

| Role               | Expertise                     | When to Invoke           |
| ------------------ | ----------------------------- | ------------------------ |
| **AI Engineer**    | LLMs, RAG, Agents, Embeddings | Chatbots, AI apps, GenAI |
| **ML Engineer**    | Training, Serving, MLOps      | ML models, predictions   |
| **Data Scientist** | Analytics, Statistics, EDA    | Analysis, experiments    |
| **MLOps Engineer** | Pipelines, Tracking, Registry | ML infrastructure        |

### Platform Domain (Lead: @platform-lead)

| Role                  | Expertise                    | When to Invoke         |
| --------------------- | ---------------------------- | ---------------------- |
| **DevOps Engineer**   | CI/CD, IaC, Containers       | Deployments, pipelines |
| **SRE**               | Reliability, Incidents, SLOs | Uptime, incidents      |
| **Platform Engineer** | IDP, Self-service, DX        | Developer platforms    |
| **Network Engineer**  | VPC, Load balancers, CDN     | Networking             |
| **Docker Specialist** | Containers, Images, Compose  | Containerization       |
| **AWS Specialist**    | All AWS services             | AWS infrastructure     |
| **Azure Specialist**  | All Azure services           | Azure infrastructure   |
| **GCP Specialist**    | All GCP services             | GCP infrastructure     |
| **FinOps Engineer**   | Costs, Budgets, Optimization | Cloud costs            |

### Security Domain (Lead: @security-lead)

| Role                   | Expertise                 | When to Invoke      |
| ---------------------- | ------------------------- | ------------------- |
| **Security Architect** | PII, IAM, Threats, AppSec | Security design     |
| **Compliance Officer** | SOC 2, GDPR, HIPAA, PCI   | Compliance, audits  |
| **Security Hardener**  | Vulnerabilities, Config   | Hardening, scanning |

### Data Domain (Lead: @data-lead)

| Role                | Expertise                 | When to Invoke      |
| ------------------- | ------------------------- | ------------------- |
| **Data Engineer**   | Pipelines, Lakehouse, ETL | Data movement       |
| **Data Governance** | Catalog, Lineage, Quality | Data governance     |
| **Database Admin**  | SQL, Optimization, Backup | Database operations |

### Product Domain (Lead: @product-lead)

| Role                   | Expertise                  | When to Invoke     |
| ---------------------- | -------------------------- | ------------------ |
| **Product Designer**   | Requirements, UX, Research | Product design     |
| **Frontend Developer** | React, Vue, TypeScript     | UI development     |
| **Backend Developer**  | APIs, Microservices, DB    | Server development |
| **QA Engineer**        | Testing, Automation        | Quality assurance  |
| **Technical Writer**   | Docs, ADRs, Runbooks       | Documentation      |

### Infrastructure (Lead: @orchestrator)

| Role            | Expertise                | When to Invoke  |
| --------------- | ------------------------ | --------------- |
| **MCP Manager** | Server lifecycle, Tokens | Tool management |

---

## Keyword → Role Mapping

```yaml
# Quick lookup: What keyword maps to which role?

AI_keywords: chatbot, LLM, RAG, agent, prompt → AI Engineer
  model, training, inference → ML Engineer
  analytics, statistics, experiment → Data Scientist
  pipeline, tracking, registry → MLOps Engineer

Platform_keywords: deploy, CI/CD, pipeline → DevOps Engineer
  incident, SLO, reliability → SRE
  kubernetes, container, docker → Docker Specialist
  AWS, EC2, Lambda, S3 → AWS Specialist
  Azure, AKS, Functions → Azure Specialist
  GCP, GKE, BigQuery → GCP Specialist
  cost, budget, optimization → FinOps Engineer

Security_keywords: PII, security, IAM, threat → Security Architect
  SOC 2, GDPR, compliance → Compliance Officer
  vulnerability, hardening → Security Hardener

Data_keywords: pipeline, ETL, lakehouse → Data Engineer
  catalog, lineage, quality → Data Governance
  SQL, query, database → Database Admin

Product_keywords: requirements, UX, design → Product Designer
  React, frontend, UI → Frontend Developer
  API, backend, server → Backend Developer
  test, QA, automation → QA Engineer
  docs, documentation → Technical Writer
```

---

All roles and skills are in `.claude/agents/`:

```
.claude/agents/
 ai-ml-lead.md        # AI/ML Lead
 platform-lead.md     # Platform Lead
 security-lead.md     # Security Lead
 data-lead.md         # Data Lead
 product-lead.md      # Product Lead
 specialists/         # 25 Specialist Agents
     ai-engineer-agent.md
     devops-engineer-agent.md
     ...
```

Expert guidance is in `.claude/skill-docs/`:

```
.claude/skill-docs/
 ai-engineer.md       # Full expert guidance
 devops.md           # Full expert guidance
 ... (one per role)
```

---

## Loading Protocol

```yaml
when_task_arrives:
  step_1:
    action: "Match keywords to roles in this index"
    tokens: ~100

  step_2:
    action: "Identify needed roles"
    example: "'Build RAG chatbot' → AI Engineer, Security Architect"

  step_3:
    action: "Route to appropriate Lead"
    example: "@ai-ml-lead, @security-lead"

  step_4:
    action: "Lead loads EXPERT GUIDANCE"
    example: "read_file('.claude/skill-docs/ai-engineer.md')"

  step_5:
    action: "Lead loads IMPLEMENTATION DETAILS"
    example: "read_file('.claude/roles/ai-engineer/skills/02-rag-pipeline/README.md')"

  step_5:
    action: "Execute task with specialist"

  step_6:
    action: "Unload files, report results"
```

---

## Cross-Domain Collaboration

Some tasks require multiple domains. Use this matrix:

| If Task Involves  | Always Include                 |
| ----------------- | ------------------------------ |
| Personal data     | @security-lead (sa-01)         |
| Production deploy | @platform-lead (do-01)         |
| Cloud resources   | @finops-engineer-agent (fo-01) |
| Data processing   | @data-lead (de-02, dg-02)      |
| API changes       | @qa-engineer-agent (qa-03)     |

---

## Example: Lazy Loading in Action

```yaml
task: "Deploy ML model to production"

step_1_index_scan:
  keywords: ["ML", "model", "deploy", "production"]
  matched_roles:
    - ML Engineer (model)
    - MLOps (deployment)
    - DevOps (production deploy)
    - Security (production = mandatory)
  tokens_used: 100

step_2_route:
  primary: @ai-ml-lead
  supporting: @platform-lead, @security-lead

step_3_load_skills:
  - Load ml-engineer.md (ml-04 section only) → 200 tokens
  - Load mlops.md (mo-05 section only) → 150 tokens
  - Load devops.md (do-01 section only) → 150 tokens
  - Load security-architect.md (sa-02 section only) → 100 tokens
  TOTAL: 600 tokens

step_4_execute:
  - Apply skills to complete deployment

step_5_unload:
  - Clear skill files from context
  - Report completion

result:
  task_complete: true
  tokens_for_skills: 600 (vs 30,000+ if all loaded)
  quality: Expert-level for the 4 relevant skills
```
