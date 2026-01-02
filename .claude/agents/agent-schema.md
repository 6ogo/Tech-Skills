# Agent Definition Schema

This document defines the standard structure for all agents in the Tech Hub Skills system.

## Agent Template

```yaml
# Agent Definition Template
name: "[Agent Name]"
type: "lead" | "specialist"
domain: "[Primary domain]"
version: "1.0"

# Agent Identity
persona: |
  You are [Agent Name], an expert in [domain].
  Your role is to [primary responsibility].

# Capabilities
skills:
  - skill_id: "xx-01"
    name: "Skill Name"
    auto_execute: true | false
    approval_required: "never" | "high_risk" | "always"

# Delegation Rules
delegates_to:
  - agent: "other-agent"
    when: "condition for delegation"

reports_to:
  - agent: "lead-agent-name"

# Collaboration
collaborates_with:
  - agent: "partner-agent"
    skills: ["skill-ids"]
    mandatory: true | false

# Automation Thresholds
automation:
  auto_execute:
    - "read-only analysis"
    - "generate documentation"
    - "code generation (new files)"
  require_approval:
    - "modify existing code"
    - "security changes"
    - "destructive operations"
    - "production deployments"
```

## Automation Decision Logic

Agents use this decision matrix to determine when to auto-execute vs. request approval:

### Risk Assessment

| Factor            | Low Risk      | Medium Risk     | High Risk            |
| ----------------- | ------------- | --------------- | -------------------- |
| **Scope**         | Single file   | Multiple files  | Cross-system         |
| **Reversibility** | Easy undo     | Moderate effort | Difficult/impossible |
| **Data Impact**   | Read-only     | Modify config   | Delete/corrupt       |
| **Security**      | No secrets    | Access control  | Credentials/PII      |
| **Production**    | Dev/test only | Staging         | Production           |

### Action Matrix

```
Risk Score = sum of risk factors (0-15)

Score 0-3:   Auto-execute silently
Score 4-7:   Show plan, then execute
Score 8-11:  Request confirmation
Score 12+:   Require explicit approval
```

## Agent Communication Protocol

### Request Format

```json
{
  "from": "orchestrator-agent",
  "to": "ai-ml-lead",
  "task": "Build RAG chatbot for internal docs",
  "context": {
    "project_type": "new",
    "has_pii": true,
    "target_env": "production"
  },
  "urgency": "normal",
  "approval_mode": "auto" | "confirm" | "manual"
}
```

### Response Format

```json
{
  "from": "ai-ml-lead",
  "status": "completed" | "needs_input" | "delegated",
  "result": "...",
  "delegated_to": ["ai-engineer-agent", "security-architect-agent"],
  "artifacts": ["file paths created/modified"],
  "recommendations": ["follow-up actions"]
}
```

## Lead Agent Responsibilities

1. **Receive tasks** from Orchestrator
2. **Analyze complexity** and break down into sub-tasks
3. **Select specialists** for each sub-task
4. **Coordinate execution** across specialists
5. **Handle cross-domain** dependencies (call other leads)
6. **Synthesize results** and report back to Orchestrator
7. **Escalate** when approval needed

## Specialist Agent Responsibilities

1. **Execute skills** within their domain
2. **Follow anti-patterns** (never skip mandatory collaborations)
3. **Report completion** to Lead Agent
4. **Request help** from partner specialists when needed
5. **Document actions** taken and artifacts created
