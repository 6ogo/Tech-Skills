# Tech Hub Orchestrator Command

Invoke the Tech Hub Orchestrator to analyze your request and load the appropriate skills on-demand.

## Usage

```
/orchestrator [your request]
```

## What This Command Does

1. **Analyzes** your request to identify domains, complexity, and requirements
2. **Selects** optimal skills from 200+ available across 31+ roles
3. **Loads** only the specific skill documentation needed (saving context)
4. **Executes** with loaded guidance

## Example

```
/orchestrator Build a RAG chatbot for internal knowledge base
```

This will:
1. Load `skill-docs/ai-engineer.md` (RAG, prompts, guardrails)
2. Load `skill-docs/security-architect.md` (PII detection)
3. Load `skill-docs/devops.md` (deployment)
4. Execute the implementation with full guidance

## How It Works

The orchestrator references `.claude/skills-index.md` to match your request keywords to skill IDs, then uses the Read tool to load only the needed skill files from `.claude/skill-docs/`.

This keeps your context lean while giving you access to the full 200+ skill library.
