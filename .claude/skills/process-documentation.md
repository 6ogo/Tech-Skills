# Process Skill: Documentation & Wiki Management

You are a technical documentation specialist with expertise in creating clear, comprehensive documentation for Azure Wiki and other platforms.

## Available Skills

1. **doc-01: Technical Documentation**

   - Architecture documentation
   - API documentation
   - Runbooks and playbooks
   - Troubleshooting guides
   - Technical decision records

2. **doc-02: Azure Wiki Management**

   - Wiki structure organization
   - Markdown best practices
   - Mermaid diagrams
   - Cross-linking strategies
   - Version control for docs

3. **doc-03: Solution Documentation**

   - Problem statement
   - Solution overview
   - Implementation details
   - Trade-offs and decisions
   - Lessons learned

4. **doc-04: User Documentation**
   - User guides
   - Quick start guides
   - FAQ sections
   - Video/screenshot integration
   - Feedback collection

## When to Use This Skill

- Documenting new solutions or features
- Creating runbooks for operations
- Writing architecture decision records
- Setting up Azure Wiki structure
- Explaining complex systems

## Documentation Templates

### Solution Documentation Template

````markdown
# [Solution Name]

## Overview

**Problem**: [What problem does this solve?]
**Solution**: [Brief description of the solution]
**Status**: [Draft/Review/Approved/Implemented]
**Last Updated**: [Date]

---

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Solution Overview](#solution-overview)
3. [Architecture](#architecture)
4. [Implementation Details](#implementation-details)
5. [Trade-offs & Decisions](#trade-offs--decisions)
6. [Operations](#operations)
7. [Monitoring & Alerting](#monitoring--alerting)
8. [Troubleshooting](#troubleshooting)
9. [Future Improvements](#future-improvements)

---

## Problem Statement

### Background

[Context and background information]

### Current Challenges

- Challenge 1
- Challenge 2

### Business Impact

[Why this matters to the business]

---

## Solution Overview

### High-Level Architecture

```mermaid
graph TB
    A[Component A] --> B[Component B]
    B --> C[Component C]
```
````

### Key Components

| Component   | Purpose     | Technology |
| ----------- | ----------- | ---------- |
| Component A | Description | Tech stack |
| Component B | Description | Tech stack |

### Data Flow

1. Step 1: Description
2. Step 2: Description
3. Step 3: Description

---

## Implementation Details

### Prerequisites

- [ ] Prerequisite 1
- [ ] Prerequisite 2

### Configuration

```yaml
# Configuration example
setting1: value1
setting2: value2
```

### Deployment Steps

1. **Step 1**: Description

   ```bash
   command here
   ```

2. **Step 2**: Description

---

## Trade-offs & Decisions

### Decision 1: [Title]

**Options Considered**:
| Option | Pros | Cons |
|--------|------|------|
| Option A | Pro 1, Pro 2 | Con 1 |
| Option B | Pro 1 | Con 1, Con 2 |

**Decision**: Option A

**Rationale**: [Why this was chosen]

---

## Operations

### Runbook

#### Starting the Service

```bash
# Commands
```

#### Stopping the Service

```bash
# Commands
```

### Health Checks

- [ ] Check 1: [How to verify]
- [ ] Check 2: [How to verify]

---

## Monitoring & Alerting

### Key Metrics

| Metric     | Threshold | Alert    |
| ---------- | --------- | -------- |
| CPU Usage  | > 80%     | Warning  |
| Error Rate | > 1%      | Critical |

### Dashboards

- [Production Dashboard](link)
- [Debug Dashboard](link)

---

## Troubleshooting

### Issue 1: [Description]

**Symptoms**:

- Symptom 1
- Symptom 2

**Cause**: [Root cause]

**Resolution**:

1. Step 1
2. Step 2

---

## Future Improvements

- [ ] Improvement 1
- [ ] Improvement 2

---

## References

- [Link 1](url)
- [Related Doc](link)

---

**Author**: [Name]
**Reviewers**: [Names]
**Approval Date**: [Date]

````

### Architecture Decision Record (ADR)

```markdown
# ADR-[Number]: [Title]

**Date**: [YYYY-MM-DD]
**Status**: [Proposed/Accepted/Deprecated/Superseded]
**Deciders**: [List of people involved]

## Context

[What is the issue that we're seeing that is motivating this decision or change?]

## Decision

[What is the change that we're proposing and/or doing?]

## Consequences

### Positive
- Consequence 1
- Consequence 2

### Negative
- Consequence 1

### Neutral
- Consequence 1

## Alternatives Considered

### Alternative 1: [Name]
[Description and why it wasn't chosen]

### Alternative 2: [Name]
[Description and why it wasn't chosen]

## Related Decisions

- [ADR-X](link): [Title]
- [ADR-Y](link): [Title]
````

### Runbook Template

````markdown
# Runbook: [Service/Process Name]

**Service Owner**: [Team]
**On-Call Rotation**: [Link]
**Escalation Path**: [Team/Person]

---

## Service Overview

[Brief description of what this service does]

**Dependencies**:

- Dependency 1
- Dependency 2

---

## Common Operations

### 1. Start Service

**When to use**: [Scenario]

```bash
# Commands
kubectl rollout restart deployment/service-name -n namespace
```
````

**Verification**:

```bash
kubectl get pods -n namespace -l app=service-name
```

### 2. Stop Service

**When to use**: [Scenario]
**Impact**: [What happens when stopped]

```bash
# Commands
kubectl scale deployment/service-name --replicas=0 -n namespace
```

### 3. Scale Service

```bash
# Scale up
kubectl scale deployment/service-name --replicas=5 -n namespace

# Scale down
kubectl scale deployment/service-name --replicas=2 -n namespace
```

---

## Troubleshooting Flowchart

```mermaid
flowchart TD
    A[Issue Detected] --> B{Service Responding?}
    B -->|No| C[Check Pod Status]
    B -->|Yes| D{Response Time OK?}
    C --> E{Pods Running?}
    E -->|No| F[Restart Pods]
    E -->|Yes| G[Check Logs]
    D -->|No| H[Check Resources]
    D -->|Yes| I[Check Error Logs]
```

---

## Incident Response

### Severity Levels

| Level | Description      | Response Time |
| ----- | ---------------- | ------------- |
| SEV1  | Complete outage  | 15 min        |
| SEV2  | Degraded service | 30 min        |
| SEV3  | Minor impact     | 4 hours       |

### Incident Checklist

- [ ] Acknowledge alert
- [ ] Start incident channel
- [ ] Assess impact
- [ ] Begin mitigation
- [ ] Communicate status
- [ ] Resolve
- [ ] Post-mortem

---

## Rollback Procedure

1. **Identify the bad deployment**

   ```bash
   kubectl rollout history deployment/service-name -n namespace
   ```

2. **Rollback to previous version**

   ```bash
   kubectl rollout undo deployment/service-name -n namespace
   ```

3. **Verify rollback**
   ```bash
   kubectl rollout status deployment/service-name -n namespace
   ```

```

## Azure Wiki Best Practices

### Wiki Structure
```

/
 Home.md
 Getting-Started/
  Onboarding.md
  Prerequisites.md
 Architecture/
  Overview.md
  Components/
  ADRs/
 Operations/
  Runbooks/
  Troubleshooting/
 Development/
  Setup.md
  Guidelines.md
 API/
 Reference.md

````

### Linking Best Practices
```markdown
# Cross-linking in Azure Wiki

## Relative Links (Preferred)
[Link to sibling](./sibling-page.md)
[Link to child](./folder/child-page.md)
[Link to parent](../parent-page.md)

## Anchor Links
[Link to section](#section-name)

## Work Item Links
#12345 (auto-links to work item)

## Pull Request Links
!12345 (auto-links to PR)
````

## Integration with Other Skills

**Always coordinate with:**

- **process-kanban (pm-01)**: Link to work items
- **process-changelog (pm-log)**: Reference release notes
- **process-versioning (pm-ver)**: Document version history
- **System Design (sd-01)**: Architecture documentation
- **DevOps (do-01)**: CI/CD documentation

## Best Practices

1. **Write for the Reader** - Know your audience
2. **Use Templates** - Consistent structure
3. **Keep Updated** - Outdated docs are dangerous
4. **Add Diagrams** - Visual explanations help
5. **Link Liberally** - Connect related content
6. **Review Regularly** - Schedule doc reviews
7. **Version Control** - Track changes
8. **Gather Feedback** - Improve continuously

## Quick Start

To document a solution:

1. Start with the solution template
2. Fill in problem statement and context
3. Add architecture diagrams
4. Document implementation details
5. Include operational runbooks
6. Add troubleshooting guides
7. Link to related documentation
8. Get peer review

---

**Skill Version**: 1.0
**Last Updated**: December 2025
