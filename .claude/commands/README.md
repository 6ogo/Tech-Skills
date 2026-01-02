# Tech Hub Commands

This directory contains Claude Code commands for the Tech Hub skills library.

## Architecture: On-Demand Skill Loading

The Tech Hub uses an **agentic orchestrator pattern** that dramatically reduces context usage:

```
Session Start: ~5-6k tokens (orchestrator only)
vs
Old Pattern: ~70k+ tokens (all skills loaded)
= 93% token reduction
```

## Available Command

### `/orchestrator` - The Single Entry Point

Use this command for ALL requests. It will:

1. **Analyze** your request to identify domains and requirements
2. **Select** optimal skills from 200+ available across 31+ roles
3. **Load** only the specific skill files needed (via Read tool)
4. **Execute** with the loaded guidance

```
/orchestrator Build a RAG chatbot for our knowledge base
```

## How It Works

```
User Request
    ↓
Orchestrator (always loaded)
    ↓
References skills-index.md (compact index)
    ↓
Loads ONLY needed skills on-demand:
    - Read .claude/skill-docs/ai-engineer.md
    - Read .claude/skill-docs/security-architect.md
    ↓
Execute with loaded guidance
```

## File Structure

```
.claude/
 skills/
    orchestrator.md          ← Single auto-loaded skill
 commands/
    orchestrator.md          ← This command
    README.md                ← This file
 skills-index.md              ← Compact skill reference
 skill-docs/                  ← On-demand skill files (40 files)
    ai-engineer.md
    data-engineer.md
    security-architect.md
    ... (all role skills)
 templates/                   ← Code templates
 roles/                       ← Deep documentation
```

## Why This Architecture?

- **Context Efficiency**: Only load what you need
- **Full Access**: Still have access to all 200+ skills
- **Smart Selection**: Orchestrator knows which skills to load
- **Cost Effective**: Less tokens = lower API costs

## Examples

### AI/ML Project
```
/orchestrator Build a customer churn prediction model
```
Loads: ai-engineer, data-engineer, ml-engineer, mlops, devops, finops

### Data Pipeline
```
/orchestrator Create an ETL pipeline with data quality checks
```
Loads: data-engineer, data-governance, devops

### Security Assessment
```
/orchestrator Audit our application for security vulnerabilities
```
Loads: security-architect, security-hardener, code-review

### New Project Setup
```
/orchestrator Bootstrap a new Python API project with CI/CD
```
Loads: project-starter, backend-developer, devops, docker

---

**Always start with `/orchestrator` - it's your intelligent guide to the complete Tech Hub!**
