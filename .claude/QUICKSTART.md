# Claude Code Quick Reference

## 🚀 How to Use the Agent System

### Option 1: Natural Language (Automatic Routing)

Simply describe what you need:

```
"Build a RAG chatbot for our documentation"
"Deploy this to production with CI/CD"
"Scan this data for PII"
```

The **Orchestrator Agent** automatically:

1. Analyzes your request
2. Routes to the appropriate Lead Agent
3. Coordinates specialists to complete the work

### Option 2: Slash Commands (Direct Routing)

Use these commands to route directly to Lead Agents:

| Command         | Routes To     | Use For                           |
| --------------- | ------------- | --------------------------------- |
| `/orchestrator` | Orchestrator  | Full analysis, multi-domain tasks |
| `/ai`           | AI/ML Lead    | Chatbots, RAG, LLMs, ML models    |
| `/platform`     | Platform Lead | DevOps, CI/CD, cloud, containers  |
| `/security`     | Security Lead | Security, compliance, audits      |
| `/data`         | Data Lead     | Pipelines, databases, governance  |
| `/product`      | Product Lead  | Features, UI, APIs, testing       |

**Example usage:**

```
/ai build a RAG pipeline for knowledge base
/security check this code for vulnerabilities
/platform deploy to kubernetes with CI/CD
```

### Option 3: Role-Specific Commands

Call specific roles directly:

```
/ai-engineer implement prompt caching
/devops create github actions pipeline
/security-architect run PII detection
```

## 📁 Key Files

| File                                | Purpose               |
| ----------------------------------- | --------------------- |
| `.claude/AGENTS.md`                 | Agent system overview |
| `.claude/agents/EXECUTION.md`       | How agents coordinate |
| `.claude/agents/SKILL-REFERENCE.md` | All skills lookup     |
| `.claude/skills/*.md`               | Individual skill docs |

## 🔄 How It Works

```
Your Request
    ↓
🎯 Orchestrator (analyzes, routes)
    ↓
👔 Lead Agent (coordinates domain)
    ↓
🔧 Specialist Agents (execute skills)
    ↓
📄 Results + Artifacts
```

## ⚡ Quick Examples

### Build AI Application

```
/ai create a chatbot with:
- RAG for documentation
- Guardrails for safety
- Cost optimization
```

**Routes to:** AI/ML Lead → AI Engineer, Security Architect

### Deploy to Production

```
/platform deploy to production with:
- CI/CD pipeline
- Docker containers
- Kubernetes
- Monitoring
```

**Routes to:** Platform Lead → DevOps, Docker Specialist, SRE

### Secure Data Pipeline

```
/data build a customer pipeline with:
- PII detection
- Data quality checks
- Governance compliance
```

**Routes to:** Security Lead (first) → Data Lead → Data Engineer

## 🛡️ Automatic Safety

These are **always enforced**:

- **Security Lead** consulted for ALL PII/production work
- **FinOps** involved for ALL cloud resources
- **Approvals required** for destructive/production actions
