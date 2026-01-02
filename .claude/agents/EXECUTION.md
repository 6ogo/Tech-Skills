# Agent Execution Instructions

These instructions ensure all agents work together as a cohesive team of experts.

## How Agents Execute

When Claude (or GitHub Copilot) receives a request:

### 1. Orchestrator Activation

The orchestrator automatically activates and:

- Analyzes the request keywords
- Identifies required domains
- Routes to appropriate Lead Agent(s)

### 2. Lead Agent Takes Ownership

The lead agent:

- Breaks down the task
- Identifies required specialists
- Checks for mandatory collaborations (security, cost, etc.)
- Delegates to specialists in correct order

### 3. Specialists Execute Skills

Each specialist:

- Loads skill documentation from `.claude/skills/{role}.md`
- Applies best practices from `.claude/roles/{role}/`
- Executes the skill
- Reports results back to lead

### 4. Result Synthesis

- Specialists → Lead → Orchestrator → User

---

## Skill Execution Protocol

When a specialist executes a skill, they follow this protocol:

```
SKILL EXECUTION: [skill-id] ([skill-name])
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📖 Loading: .claude/skills/{role}.md
📋 Section: {skill-id} description
🔧 Applying: Best practices and templates

⚠️ Mandatory Checks:
- [ ] Security requirements (sa-01 if PII)
- [ ] Cost tracking (fo-01 if cloud)
- [ ] Quality gates (if applicable)

🎯 Executing...
[actual work happens here]

✅ Complete. Reporting to lead agent.
```

---

## Cross-Agent Communication

### Agent References

Use @ mentions to invoke agents:

- `@orchestrator-agent` - Master coordinator
- `@ai-ml-lead` - AI/ML domain lead
- `@platform-lead` - Platform/DevOps domain lead
- `@security-lead` - Security/Compliance domain lead
- `@data-lead` - Data Engineering domain lead
- `@product-lead` - Product Development domain lead
- `@{specialist}-agent` - Specific specialist

### Handoff Format

```yaml
FROM: @ai-ml-lead
TO: @security-architect-agent
TASK: Execute sa-01 (PII Detection)
CONTEXT:
  data_source: "customer_records.csv"
  urgency: high
  blocking: true
RETURN_TO: @ai-ml-lead when complete
```

### Status Updates

```yaml
FROM: @security-architect-agent
TO: @ai-ml-lead
STATUS: complete
RESULT:
  pii_detected: true
  fields: ["email", "phone", "address"]
  recommendation: "Apply masking in Silver layer"
```

---

## Mandatory Collaboration Rules

These rules are ENFORCED across all agents:

### Security First (ALWAYS)

```
IF task involves:
  - Personal data, PII, customer info
  - Production deployment
  - Authentication/authorization
  - API keys, secrets, credentials
THEN:
  @security-lead MUST be involved FIRST
```

### Cost Tracking (ALWAYS)

```
IF task involves:
  - Cloud resources (AWS/Azure/GCP)
  - AI/ML workloads
  - Data storage
THEN:
  @finops-engineer-agent MUST be involved
```

### Quality Assurance (ALWAYS)

```
IF task involves:
  - Code changes
  - API modifications
  - User-facing features
THEN:
  @qa-engineer-agent MUST review before completion
```

---

## Workflow Execution Order

For any multi-agent workflow, follow this order:

1. **Security Assessment** (if applicable)
   - PII detection, threat modeling
2. **Data Preparation** (if applicable)
   - Pipelines, quality checks, cataloging
3. **Core Implementation**
   - Primary domain work
4. **Quality & Testing**
   - Unit, integration, E2E tests
5. **Deployment Preparation**
   - CI/CD, containers, infrastructure
6. **Monitoring Setup**
   - Observability, alerts, dashboards
7. **Documentation**
   - API docs, ADRs, user guides

---

## Error Handling

### When a Specialist Needs Help

```yaml
FROM: @backend-developer-agent
TO: @product-lead
STATUS: blocked
ISSUE: "Database schema requires DBA input"
REQUESTING: @database-admin-agent
```

### When Approval is Needed

```yaml
FROM: @platform-lead
TO: @orchestrator-agent
STATUS: awaiting_approval
ACTION: "Production deployment"
RISK_LEVEL: high
USER_APPROVAL_REQUIRED: true
```

### When Cross-Domain Help is Needed

```yaml
FROM: @ai-ml-lead
TO: @orchestrator-agent
STATUS: needs_coordination
REQUIRES: [@security-lead, @platform-lead]
REASON: "Production AI deployment needs security review and CI/CD"
```

---

## Verification Checklist

Before completing any task, agents verify:

- [ ] All mandatory collaborations satisfied
- [ ] Security requirements addressed
- [ ] Cost tracking in place (if cloud)
- [ ] Tests written/updated
- [ ] Documentation updated
- [ ] No high-risk actions without approval
