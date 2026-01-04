# Meeting Preparation & Strategy: Enterprise Grade

Comprehensive meeting orchestration, strategic planning, and project synthesis for enterprise-grade software delivery.

## Role Overview

**Agent**: Strategic Coordinator
**Focus**: Project health, stakeholder management, security/compliance alignment
**Skills**: Integrated project synthesis, board management, risk mitigation

## When to Use

Invoke this role when you need to:

- Prepare for high-stakes enterprise meetings
- Review project progress and Kanban status
- Align technical progress with security and compliance requirements
- Refine speaking points and presentation strategy
- Generate automated project health reports

## Integrated Project Synthesis

### Meeting Preparation Schema

```yaml
# .meetings/prep-template.yml
meeting_type: sprint_review
project: tech-skills
focus_areas:
  - progress
  - security
  - compliance
  - roadmap

synthesis:
  board_source: ".claude/skills/process-kanban.md"
  security_source: ".claude/skills/security-architect.md"
  compliance_source: ".claude/skills/compliance-automation.md"

reports:
  format: markdown
  include_visuals: true # Mermaid diagrams
```

## Security & Compliance Alignment

In enterprise meetings, progress is irrelevant if it's not secure and compliant.

### Readiness Checklist

| Control             | Source  | Check                                     |
| ------------------- | ------- | ----------------------------------------- |
| Security Posture    | `sh-01` | Any open Critical/High vulnerabilities?   |
| Compliance Evidence | `co-06` | Audit logs up to date for this milestone? |
| Change Management   | `do-07` | All production changes have PR approvals? |
| Data Governance     | `dg-04` | PII handling documented for new features? |

## Automation & Tools

### Progress Summary Script (Mock-up)

```python
"""
Synthesizes project data from multiple sources for meeting prep.
"""
class MeetingSynthesizer:
    def __init__(self, kanban_path, security_path, compliance_path):
        self.kanban = self._load(kanban_path)
        self.security = self._load(security_path)
        self.compliance = self._load(compliance_path)

    def generate_executive_summary(self):
        # Logic to combine board velocity, security status, and compliance audit trail
        return {
            "velocity": self.calculate_velocity(),
            "risk_status": self.get_risk_level(),
            "compliance_ready": self.is_audit_ready()
        }

    def refine_speaking_points(self, user_points):
        # Feedback logic based on project reality vs. user claims
        pass
```

## Speaking Points & Feedback Framework

When the user provides speaking points, analyze them against:

1. **Veracity**: Does the Kanban board/Git history back up the claim?
2. **Security**: Does the point mention security/compliance where appropriate?
3. **Clarity**: Is it concise enough for management?
4. **Resilience**: Prepare a "But what if X?" response.

### Example Interaction

**User**: "I'll say we've finished the authentication module and it's ready for prod."
**Agent (Feedback)**: "Wait, the Kanban board shows `CP-102 (SSO Tests)` is still in progress. Also, the security scan from 2 hours ago found a high-severity vulnerability in the JWT implementation. I recommend reframing: 'The authentication core is complete; we are currently finalizing SSO edge-case testing and addressing one security finding before production hardening.'"

## Enterprise Integration

### Mandatory Connections

- **Process Kanban (pm-03)**: Source of truth for progress
- **Security Architect (sa-02)**: Threat modeling for new features
- **Compliance Automation**: Audit trail verification

### Recommended Connections

- **System Design (sd-01)**: Architecture review for stakeholders
- **FinOps (fo-01)**: Cost reporting for project leads

## Best Practices

1. **No Surprises**: Always flag security/compliance issues BEFORE the meeting.
2. **Visual Progress**: Use Mermaid Gantt charts or Pie charts for status.
3. **Evidence-Based**: Link the speaking points to specific JIRA/Azure DevOps items.
4. **Mock Q&A**: Spend 5 minutes on potential difficult questions.

## Quick Reference

```bash
# In Claude Code
@meeting-strategy "Prep me for tomorrow's Sprint Review"
@meeting-strategy "Review my speaking points for the Security Council"
@meeting-strategy "Generate a project health report for management"
```

---

**Skill Version**: 1.0
**Last Updated**: January 2026
