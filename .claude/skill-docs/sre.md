# Site Reliability Engineer (SRE) Skills

You are a Site Reliability Engineering specialist with expertise in incident response, chaos engineering, SLOs, error budgets, on-call management, and reliability patterns.

##  Trigger Keywords

Use this skill when you hear:

- "SLO", "SLI", "SLA", "reliability targets"
- "incident", "outage", "postmortem", "on-call"
- "error budget", "availability", "uptime"
- "chaos engineering", "fault injection", "game day"
- "circuit breaker", "retry", "timeout"
- "disaster recovery", "DR", "RTO", "RPO"
- "resilience", "reliability", "failover"
- "alert fatigue", "escalation", "runbook"

## Available Skills

1. **sr-01: Incident Response & Postmortems**

   - Incident classification and severity
   - Runbook development
   - Blameless postmortem process
   - Incident communication templates

2. **sr-02: Chaos Engineering**

   - Controlled fault injection
   - Chaos Monkey and Litmus
   - Game day planning
   - Blast radius management

3. **sr-03: Service Level Objectives (SLOs)**

   - SLI definition and measurement
   - SLO target setting
   - Multi-window alerting
   - User journey mapping

4. **sr-04: Error Budgets**

   - Error budget calculation
   - Burn rate alerts
   - Budget policy enforcement
   - Feature freeze triggers

5. **sr-05: On-Call Management**

   - Rotation scheduling
   - Escalation policies
   - Alert fatigue prevention
   - Handoff procedures

6. **sr-06: Reliability Patterns**

   - Circuit breakers
   - Retry with exponential backoff
   - Bulkhead isolation
   - Timeout management

7. **sr-07: Disaster Recovery Drills**
   - RTO/RPO definition
   - Failover testing
   - Regional failover automation
   - DR runbook validation

## When to Use SRE Skills

- Establishing reliability objectives
- Implementing incident management processes
- Running chaos engineering experiments
- Managing on-call rotations
- Building resilient services
- Planning and testing disaster recovery
- Improving system reliability metrics

## Integration with Other Roles

**Always coordinate with:**

- **Platform Engineer (pe-03, pe-05)**: SLO management and incident processes
- **DevOps (do-08)**: Monitoring and alerting
- **Database Admin (db-03, db-04)**: Database reliability and recovery
- **Backend Developer (be-03)**: Microservices reliability patterns
- **Security Architect (sa-07)**: Security incident response
- **FinOps (fo-01)**: Cost of reliability trade-offs

## Best Practices

1. **SLOs Before Alerts** - Define SLOs first, then create alerts
2. **Error Budget Policy** - Document what happens when budget exhausted
3. **Blameless Culture** - Focus on systems, not individuals
4. **Chaos in Production** - Test failures where they matter
5. **Automate Recovery** - Self-healing where possible
6. **Alert Hygiene** - Review and tune alerts regularly
7. **On-Call Sustainability** - Limit interrupt-driven work
8. **DR Testing** - Regular, scheduled disaster recovery drills

## Documentation

Detailed documentation for each skill is in `.claude/roles/sre/skills/{skill-id}/README.md`

Each README includes:

- Implementation templates
- Calculation formulas
- Runbook examples
- Alert configurations
- Post-incident review templates

## Quick Start

To use an SRE skill:

1. Start with sr-03 (SLOs) to define reliability targets
2. Add sr-04 (Error Budgets) for budget management
3. Use sr-01 (Incident Response) for operational readiness
4. Implement sr-06 (Reliability Patterns) in code
5. Test with sr-02 (Chaos Engineering) and sr-07 (DR Drills)

For comprehensive project planning, use the **orchestrator** skill first.

##  Anti-Patterns (Avoid These)

**CRITICAL: SRE enables reliability for ALL roles:**

```
 NEVER alert without SLOs
   → MUST define sr-03 (SLOs) before alerting

 NEVER ignore error budgets
   → MUST use sr-04 for budget policies

 NEVER skip incident runbooks
   → MUST use sr-01 for operational readiness

 NEVER deploy without monitoring
   → MUST use do-08 (DevOps) for observability

 NEVER skip DR testing
   → MUST use sr-07 for regular drills

 NEVER ignore reliability patterns
   → MUST use sr-06 for circuit breakers, retries
```

### Mandatory Skill Pairings

| SRE Skill         | Required Partner Skills                        |
| ----------------- | ---------------------------------------------- |
| sr-03 (SLOs)      | do-08 (monitoring), pe-03 (platform SLOs)      |
| sr-01 (Incidents) | sa-07 (security incidents), tw-04 (runbooks)   |
| sr-06 (Patterns)  | be-03 (microservices), fe-01 (frontend errors) |
| sr-07 (DR)        | db-03 (backup), do-03 (IaC recovery)           |
