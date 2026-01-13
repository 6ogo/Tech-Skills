# Orchestrator Overview: How Agents Are Assembled

This document explains how the Orchestrator works, how it dynamically assembles agents, and how skills and skill documentation are fetched on-demand.

## Table of Contents

1. [System Architecture](#system-architecture)
2. [The Orchestrator Workflow](#the-orchestrator-workflow)
3. [Agent Assembly Process](#agent-assembly-process)
4. [Skill Loading Protocol](#skill-loading-protocol)
5. [Token Efficiency Strategy](#token-efficiency-strategy)
6. [Real-World Examples](#real-world-examples)

---

## System Architecture

### Three-Tier Hierarchy

```
                    ┌─────────────────────────┐
                    │      ORCHESTRATOR       │
                    │   (Master Coordinator)  │
                    │    model: sonnet        │
                    └───────────┬─────────────┘
                                │
        ┌───────────┬───────────┼───────────┬───────────┐
        │           │           │           │           │
        ▼           ▼           ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
   │ AI/ML   │ │Platform │ │Security │ │  Data   │ │ Product │
   │  Lead   │ │  Lead   │ │  Lead   │ │  Lead   │ │  Lead   │
   │ sonnet  │ │ sonnet  │ │ sonnet  │ │ sonnet  │ │ sonnet  │
   └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘
        │           │           │           │           │
        ▼           ▼           ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
   │Specialist│ │Specialist│ │Specialist│ │Specialist│ │Specialist│
   │ Agents  │ │ Agents  │ │ Agents  │ │ Agents  │ │ Agents  │
   │  haiku  │ │  haiku  │ │  haiku  │ │  haiku  │ │  haiku  │
   └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
```

**Tier 1: Orchestrator** - Master coordinator that receives all requests, thinks strategically, and routes to appropriate leads.

**Tier 2: Lead Agents (5)** - Domain experts that own their area, coordinate specialists, and ensure quality.

**Tier 3: Specialist Agents (25)** - Focused executors that perform specific skills within their domain.

### Key Files

| File | Purpose | Token Cost |
|------|---------|------------|
| `SKILL-REGISTRY.md` | Lightweight keyword → skill ID mapping | ~200 tokens |
| `ROLE-REGISTRY.md` | Lightweight role → lead mapping | ~150 tokens |
| `skill-docs/*.md` | Expert guidance per role | ~500-800 tokens each |
| `roles/*/skills/*/README.md` | Detailed implementation guides | ~1000+ tokens each |

---

## The Orchestrator Workflow

### Brainstorm → Plan → Implement

Every request follows this three-phase approach:

```
┌──────────────────────────────────────────────────────────────────┐
│                         USER REQUEST                              │
└──────────────────────────────────────────┬───────────────────────┘
                                           │
                                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  PHASE 1: BRAINSTORM                                             │
│                                                                  │
│  • Understand the request deeply                                 │
│  • Identify constraints, risks, and opportunities                │
│  • Consider alternative approaches                               │
│  • Ask clarifying questions if needed                            │
└──────────────────────────────────────────┬───────────────────────┘
                                           │
                                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  PHASE 2: PLAN                                                   │
│                                                                  │
│  • Scan SKILL-REGISTRY.md for matching keywords                  │
│  • Select ONLY the roles/skills needed (usually 3-7)             │
│  • Define clear milestones and deliverables                      │
│  • Present plan for user approval                                │
└──────────────────────────────────────────┬───────────────────────┘
                                           │
                                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  PHASE 3: IMPLEMENT                                              │
│                                                                  │
│  • Execute step-by-step, loading skills on-demand                │
│  • Validate each step before proceeding                          │
│  • Adapt plan if blockers arise                                  │
│  • Synthesize results and document learnings                     │
└──────────────────────────────────────────────────────────────────┘
```

---

## Agent Assembly Process

### Step 1: Request Analysis

When a request arrives, the Orchestrator:

1. **Extracts keywords** from the user's request
2. **Scans registries** (SKILL-REGISTRY.md + ROLE-REGISTRY.md)
3. **Matches keywords** to skill IDs and roles

```yaml
request: "Build a RAG chatbot with security for customer data"

extracted_keywords:
  - RAG
  - chatbot
  - security
  - customer data

matched_skills:
  - ai-02: RAG Pipeline
  - ai-04: LLM Guardrails
  - sa-01: PII Detection (MANDATORY - customer data)

identified_leads:
  - @ai-ml-lead (primary)
  - @security-lead (mandatory collaboration)
```

### Step 2: Lead Agent Selection

The Orchestrator routes to the appropriate Lead Agent(s):

```
                     ORCHESTRATOR
                          │
           ┌──────────────┼──────────────┐
           │                             │
           ▼                             ▼
      @ai-ml-lead                @security-lead
      (Primary Owner)            (Mandatory Collaboration)
```

### Step 3: Specialist Delegation

Each Lead Agent:

1. **Analyzes the task** within their domain
2. **Identifies required specialists** from `agents/specialists/`
3. **Loads expert guidance** from `skill-docs/*.md`
4. **Delegates to specialists** with specific skill IDs

```yaml
ai_ml_lead:
  loads: .claude/skill-docs/ai-engineer.md
  delegates_to:
    - @ai-engineer-agent
      skills: [ai-02, ai-04]

security_lead:
  loads: .claude/skill-docs/security-architect.md
  delegates_to:
    - @security-architect-agent
      skills: [sa-01]
```

### Step 4: Specialist Execution

Each Specialist Agent:

1. **Receives skill IDs** from their Lead
2. **Loads detailed implementation** from `roles/*/skills/*/README.md`
3. **Executes the skill** with best practices
4. **Reports results** back to Lead
5. **Unloads skill docs** to free context

```
┌─────────────────────────────────────────────────────────┐
│  SPECIALIST EXECUTION                                   │
│                                                         │
│  @ai-engineer-agent executing skill ai-02               │
│                                                         │
│  1. Load: .claude/roles/ai-engineer/skills/             │
│           02-rag-pipeline/README.md                     │
│                                                         │
│  2. Apply:                                              │
│     • Document chunking strategy                        │
│     • Embedding model selection                         │
│     • Vector store configuration                        │
│     • Retrieval pipeline setup                          │
│                                                         │
│  3. Report: Complete with artifacts                     │
│                                                         │
│  4. Unload: Free context for next skill                 │
└─────────────────────────────────────────────────────────┘
```

### Step 5: Result Synthesis

Results flow back through the hierarchy:

```
Specialist → Lead Agent → Orchestrator → User

@ai-engineer-agent
    │
    ├── RAG pipeline implemented
    │   └── Vector store: Pinecone
    │   └── Chunking: 512 tokens
    │
    └── Reports to @ai-ml-lead
            │
            ├── Validates implementation
            │
            └── Reports to @orchestrator
                    │
                    └── Synthesizes all results
                        │
                        └── Presents to User
```

---

## Skill Loading Protocol

### The 6-Step Lazy Loading Process

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1: SCAN REGISTRIES (~350 tokens)                          │
│                                                                 │
│  read_file('.claude/agents/SKILL-REGISTRY.md')  → ~200 tokens   │
│  read_file('.claude/agents/ROLE-REGISTRY.md')   → ~150 tokens   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 2: MATCH KEYWORDS (0 tokens - just pattern matching)      │
│                                                                 │
│  Request keywords: "RAG", "chatbot", "security"                 │
│  Matched skill IDs: ai-02, ai-04, sa-01                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 3: ROUTE TO LEADS (0 tokens - just routing decision)      │
│                                                                 │
│  ai-02, ai-04 → @ai-ml-lead                                     │
│  sa-01        → @security-lead                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 4: LOAD EXPERT GUIDANCE (~500-800 tokens per role)        │
│                                                                 │
│  read_file('.claude/skill-docs/ai-engineer.md')                 │
│  read_file('.claude/skill-docs/security-architect.md')          │
│                                                                 │
│  Contains: Skill triggers, best practices, anti-patterns        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 5: LOAD DETAILED IMPLEMENTATION (on-demand per skill)     │
│                                                                 │
│  read_file('.claude/roles/ai-engineer/skills/                   │
│            02-rag-pipeline/README.md')                          │
│                                                                 │
│  Contains: Tools, templates, code examples, deep best practices │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 6: EXECUTE & UNLOAD                                       │
│                                                                 │
│  • Apply skill knowledge to complete task                       │
│  • Summarize what was done                                      │
│  • Discard detailed docs from context                           │
│  • Ready for next skill                                         │
└─────────────────────────────────────────────────────────────────┘
```

### Three Layers of Skill Documentation

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: SKILL REGISTRY (Always Loaded)                        │
│  File: .claude/agents/SKILL-REGISTRY.md                         │
│  Size: ~200 tokens                                              │
│  Contains: Keyword → Skill ID mappings                          │
│  Example: "RAG, retrieval, knowledge base: → ai-02, ai-05"      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 2: EXPERT GUIDANCE (Loaded per role)                     │
│  Directory: .claude/skill-docs/                                 │
│  Files: ai-engineer.md, security-architect.md, etc.             │
│  Size: ~500-800 tokens each                                     │
│  Contains: All skills for role, triggers, anti-patterns         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 3: DETAILED IMPLEMENTATION (Loaded per skill)            │
│  Directory: .claude/roles/[role]/skills/[id]/README.md          │
│  Size: ~1000+ tokens each                                       │
│  Contains: Templates, code, tools, deep-dive best practices     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Token Efficiency Strategy

### Why Lazy Loading?

Loading all 200+ skills upfront would consume **50,000+ tokens**, leaving little room for actual work. Lazy loading achieves **95% token savings**.

### Token Usage Comparison

| Approach | Tokens Used | Context Available |
|----------|-------------|-------------------|
| Load Everything Upfront | ~50,000 | ~10% remaining |
| Lazy Loading (3 skills) | ~2,500 | ~97% remaining |
| **Savings** | **95%** | **87% more context** |

### Token Budget Per Request

```yaml
typical_request:
  registries: 350 tokens      # Always loaded
  expert_guidance: 1,200 tokens   # 2 roles × 600 avg
  detailed_skills: 2,000 tokens   # 2 skills × 1000 avg
  ─────────────────────────────
  total: ~3,550 tokens        # vs 50,000+ if all loaded

context_remaining: ~196,000 tokens  # For actual work!
```

---

## Real-World Examples

### Example 1: RAG Chatbot with Security

```yaml
USER REQUEST: "Build a RAG chatbot with security for customer data"

ORCHESTRATOR:
  phase: brainstorm
  keywords: [RAG, chatbot, security, customer data]

  phase: plan
  scan: SKILL-REGISTRY.md
  matches:
    - ai-02: RAG Pipeline
    - ai-04: LLM Guardrails
    - sa-01: PII Detection [MANDATORY - customer data]

  routing:
    primary: @ai-ml-lead
    mandatory: @security-lead

SECURITY LEAD (executes first - security first rule):
  loads: .claude/skill-docs/security-architect.md
  skill: sa-01
  action: Scan for PII in customer data
  result: Email, phone detected → masking required

AI/ML LEAD (executes after security approval):
  loads: .claude/skill-docs/ai-engineer.md
  skills: [ai-02, ai-04]

  @ai-engineer-agent:
    skill: ai-02
    loads: .claude/roles/ai-engineer/skills/02-rag-pipeline/README.md
    action: Build retrieval pipeline with masked data

    skill: ai-04
    loads: .claude/roles/ai-engineer/skills/04-llm-guardrails/README.md
    action: Add content filtering and output validation

RESULT:
  tokens_used: ~3,200
  tokens_saved: ~47,000 (94%)
  deliverable: Secure RAG chatbot with PII protection
```

### Example 2: ML Model Deployment

```yaml
USER REQUEST: "Deploy our churn prediction model to production"

ORCHESTRATOR:
  keywords: [deploy, model, production, prediction, churn]

  matches:
    - ml-04: Model Serving
    - mo-03: Model Registry
    - do-01: CI/CD Pipeline
    - sa-01: PII Detection [MANDATORY - production]
    - fo-01: Cost Visibility [MANDATORY - cloud]

  routing:
    primary: @ai-ml-lead
    mandatory: [@security-lead, @platform-lead]

EXECUTION ORDER:
  1. @security-lead → sa-01 (PII check)
  2. @ai-ml-lead → mo-03 (register model)
  3. @ai-ml-lead → ml-04 (serving setup)
  4. @platform-lead → do-01 (CI/CD integration)

RESULT:
  tokens_used: ~4,500
  skills_applied: 5
  deliverable: Production-deployed ML model with full pipeline
```

---

## Agent Communication Format

### Request Format (Lead → Specialist)

```yaml
FROM: @ai-ml-lead
TO: @ai-engineer-agent
TASK: Execute skill ai-02 (RAG Pipeline)
CONTEXT:
  data_source: "masked_customer_docs/"
  vector_store: "pinecone"
  embedding_model: "text-embedding-3-small"
BLOCKING: true
RETURN_TO: @ai-ml-lead
```

### Response Format (Specialist → Lead)

```yaml
FROM: @ai-engineer-agent
TO: @ai-ml-lead
STATUS: complete
SKILL: ai-02
RESULT:
  pipeline_created: true
  chunks: 2,847
  index_name: "customer-docs-v1"
  retrieval_tested: true
ARTIFACTS:
  - src/rag/pipeline.py
  - config/pinecone.yaml
```

---

## Summary

The Orchestrator system achieves expert-level task execution through:

1. **Strategic Thinking** - Brainstorm → Plan → Implement workflow
2. **Hierarchical Delegation** - Orchestrator → Leads → Specialists
3. **Lazy Loading** - Load only what's needed, when needed
4. **Token Efficiency** - 95% reduction in context usage
5. **Mandatory Collaborations** - Security, cost, and quality built-in

This architecture enables complex, multi-domain tasks while maintaining:
- Expert-level knowledge application
- Minimal context footprint
- Comprehensive safety guardrails
- Clear audit trail

---

_Generated for Tech Hub Skills v2.3.1_
