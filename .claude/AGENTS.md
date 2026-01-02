# Tech Hub Skills - Agent System

This directory contains the **hierarchical multi-agent system** for Tech Hub Skills. Agents act as expert personas that coordinate work, delegate tasks, and execute skills.

## Architecture Overview

```

                    ORCHESTRATOR AGENT                       
         Analyzes requests, routes to Lead Agents            

                             
        
                                                
                                                
      
  AI/ML Lead        Platform          Security     
                      Lead              Lead       
      
                                              
                                              
      
  Data Lead         Product                        
                      Lead           (Specialists) 
      
        
        
  [24 Specialists]
```

## Quick Start

### 1. Ask the Orchestrator

Simply describe what you need:

```
"Build a RAG chatbot for our documentation"
"Deploy a machine learning model to production"
"Create a secure REST API with authentication"
```

### 2. Orchestrator Routes to Leads

The orchestrator analyzes your request and identifies:

- Primary Lead Agent (owns the deliverable)
- Supporting Lead Agents (provide expertise)

### 3. Leads Delegate to Specialists

Each lead breaks down the task and assigns specialists:

- ai-engineer, ml-engineer, data-scientist, etc.

### 4. Specialists Execute Skills

Specialists use their skills (ai-01, de-02, etc.) to complete work.

## Directory Structure

```
agents/
 agent-schema.md           # Template for all agents
 orchestrator-agent.md     # Master orchestrator
 EXECUTION.md              # How agents work together
 SKILL-REFERENCE.md        # Complete skill lookup table
 ROLE-REGISTRY.md          # Lightweight role index
 SKILL-REGISTRY.md         # Lightweight skill index
 ai-ml-lead.md             # AI, ML, Data Science Lead
 platform-lead.md          # DevOps, SRE, Cloud Lead
 security-lead.md          # Security, Compliance Lead
 data-lead.md              # Data Engineering, Governance Lead
 product-lead.md           # Product, Frontend, Backend, QA Lead
 specialists/              # 25 Specialist agents (loaded on demand)
     ai-engineer-agent.md
     ml-engineer-agent.md
     ... (25 total)
```

| File                                                                                                 | Purpose                                  |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [SKILL-REGISTRY.md](file:///Users/g/Documents/GitHub/Tech-Skills/.claude/agents/SKILL-REGISTRY.md)   | Lightweight skill index for lazy loading |
| [ROLE-REGISTRY.md](file:///Users/g/Documents/GitHub/Tech-Skills/.claude/agents/ROLE-REGISTRY.md)     | Lightweight role index for lazy loading  |
| [EXECUTION.md](file:///Users/g/Documents/GitHub/Tech-Skills/.claude/agents/EXECUTION.md)             | How agents coordinate and communicate    |
| [SKILL-REFERENCE.md](file:///Users/g/Documents/GitHub/Tech-Skills/.claude/agents/SKILL-REFERENCE.md) | Complete skill lookup (all ~175 skills)  |

## Context-Efficient Loading

**Agents NEVER load all skills at once.** They use lazy loading:

```yaml
1. Scan SKILL-REGISTRY.md for keywords (~200 tokens)
2. Identify needed skill IDs (e.g., ai-02, sa-01)
3. Load ONLY those skill files when executing
4. Unload after task complete

Result: 95%+ token savings while maintaining expert knowledge
```

## Lead Agents (5)

| Lead              | Domain                 | Specialists                                                        |
| ----------------- | ---------------------- | ------------------------------------------------------------------ |
| **AI/ML Lead**    | AI, ML, Data Science   | ai-engineer, ml-engineer, data-scientist, mlops                    |
| **Platform Lead** | Infrastructure, DevOps | devops, sre, platform, network, docker, aws, azure, gcp, finops    |
| **Security Lead** | Security, Compliance   | security-architect, compliance-officer, security-hardener          |
| **Data Lead**     | Data Engineering       | data-engineer, data-governance, database-admin                     |
| **Product Lead**  | Product Development    | product-designer, frontend, backend, qa-engineer, technical-writer |

## Automation Levels

Agents automatically decide when to proceed vs. ask for approval:

| Action Type      | Behavior                                                           |
| ---------------- | ------------------------------------------------------------------ |
| **Auto-execute** | Read-only analysis, generate new files, documentation              |
| **Confirm**      | Modify existing code, create resources, add dependencies           |
| **Approval**     | Production deploy, delete resources, security changes, credentials |

## Quick Commands

| Command     | Routes To     | Use For                          |
| ----------- | ------------- | -------------------------------- |
| `/ai`       | AI/ML Lead    | Chatbots, RAG, LLMs, ML models   |
| `/platform` | Platform Lead | DevOps, CI/CD, cloud, containers |
| `/security` | Security Lead | Security, compliance, audits     |
| `/data`     | Data Lead     | Pipelines, databases, governance |
| `/product`  | Product Lead  | Features, UI, APIs, testing      |
| `/analyze`  | Orchestrator  | Full project analysis            |

## How Agents Work with Skills

Each specialist has access to specific **skills** (the building blocks):

```
Agent: AI Engineer
Skills: ai-01, ai-02, ai-03, ai-04, ai-05, ai-06, ai-07, ai-08

When you ask: "Build a RAG system"
Agent uses: ai-02 (RAG Pipeline), ai-04 (Guardrails), ai-07 (Production API)
```

Skills are documented in `.claude/skills/` and `.claude/commands/`.

## Cross-Domain Collaboration

Agents automatically collaborate when needed:

**Always Security Lead for:**

- PII or personal data
- Production deployments
- Authentication systems

**Always Platform Lead for:**

- Any deployment
- Cloud resources
- CI/CD pipelines

**Always FinOps for:**

- Cloud costs
- AI/ML workloads
