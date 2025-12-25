# pd-01: Product Requirements & Discovery

> **Find the Perfect Product**: Systematic approach to discovering, defining, and prioritizing product requirements that solve real user problems.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Skill ID** | pd-01 |
| **Role** | Product Designer |
| **Complexity** | Medium |
| **Dependencies** | None (foundational skill) |
| **Outputs** | PRD, Feature Specs, Prioritized Backlog |

---

## Core Capabilities

### 1. Problem Space Exploration

```yaml
problem_discovery:
  techniques:
    - "5 Whys Analysis"
    - "Problem Statement Canvas"
    - "Opportunity Mapping"
    - "Root Cause Analysis"

  problem_statement_template: |
    ## Problem Statement

    **Who**: [Target user segment]
    **What**: [The problem they face]
    **When**: [Context/situation when it occurs]
    **Why it matters**: [Business and user impact]
    **Current solutions**: [How they solve it today]
    **Gap**: [What's missing]

  validation_questions:
    - "Is this a real problem or assumed?"
    - "How do users solve this today?"
    - "What's the cost of not solving this?"
    - "How many users are affected?"
    - "Is this problem getting worse?"
```

### 2. Jobs-to-be-Done Framework

```yaml
jtbd_framework:
  job_statement_format: |
    When [situation], I want to [motivation], so I can [expected outcome]

  example: |
    When I'm preparing for a client meeting, I want to quickly find
    relevant case studies, so I can demonstrate our expertise and
    win the deal.

  job_dimensions:
    functional: "What task needs to be accomplished?"
    emotional: "How do they want to feel?"
    social: "How do they want to be perceived?"

  forces_of_progress:
    push: "Pain with current solution"
    pull: "Attraction of new solution"
    anxiety: "Fear of change"
    habit: "Comfort with current solution"
```

### 3. PRD Generation

```markdown
# Product Requirements Document (PRD) Template

## 1. Overview
- **Product Name**:
- **Author**:
- **Last Updated**:
- **Status**: Draft | Review | Approved

## 2. Problem Statement
[Clear articulation of the problem being solved]

## 3. Goals & Success Metrics

| Goal | Metric | Target | Measurement |
|------|--------|--------|-------------|
| Primary | [KPI] | [Value] | [How measured] |
| Secondary | [KPI] | [Value] | [How measured] |

## 4. User Stories

### Epic: [Name]
| ID | As a... | I want to... | So that... | Priority |
|----|---------|--------------|------------|----------|
| US-001 | [User] | [Action] | [Benefit] | Must Have |

## 5. Functional Requirements

### Feature: [Name]
- **Description**:
- **User Flow**:
- **Acceptance Criteria**:
  - [ ] Criteria 1
  - [ ] Criteria 2
- **Edge Cases**:

## 6. Non-Functional Requirements
- **Performance**:
- **Security**:
- **Accessibility**:
- **Scalability**:

## 7. Out of Scope
- [Feature/capability explicitly not included]

## 8. Dependencies
- [Technical dependencies]
- [Team dependencies]
- [External dependencies]

## 9. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | High/Med/Low | High/Med/Low | [Strategy] |

## 10. Timeline
- **Phase 1**: [Date] - [Deliverable]
- **Phase 2**: [Date] - [Deliverable]

## 11. Appendix
- Wireframes
- User research insights
- Competitive analysis
```

### 4. Feature Prioritization

```yaml
prioritization_frameworks:
  moscow:
    must_have: "Critical for launch, non-negotiable"
    should_have: "Important but not critical"
    could_have: "Nice to have if time permits"
    wont_have: "Explicitly excluded from this release"

  rice_scoring:
    formula: "(Reach × Impact × Confidence) / Effort"
    reach: "Number of users affected per quarter"
    impact: "0.25 (minimal) to 3 (massive)"
    confidence: "0.5 (low) to 1.0 (high)"
    effort: "Person-months required"

    example:
      feature: "One-click checkout"
      reach: 10000  # users/quarter
      impact: 2     # high
      confidence: 0.8
      effort: 2     # person-months
      score: "(10000 × 2 × 0.8) / 2 = 8000"

  kano_model:
    basic: "Expected features - absence causes dissatisfaction"
    performance: "More is better - linear satisfaction"
    excitement: "Unexpected delighters - high satisfaction"
    indifferent: "No impact on satisfaction"
    reverse: "Presence causes dissatisfaction"

  weighted_scoring:
    criteria:
      - name: "User Value"
        weight: 0.35
      - name: "Business Value"
        weight: 0.25
      - name: "Technical Feasibility"
        weight: 0.20
      - name: "Strategic Alignment"
        weight: 0.20
```

### 5. Success Metrics Definition

```yaml
metrics_framework:
  north_star_metric:
    definition: "The single metric that best captures the core value delivered"
    example: "Weekly Active Users who complete a task"

  okr_structure:
    objective: "Qualitative goal"
    key_results:
      - "Measurable outcome 1"
      - "Measurable outcome 2"
      - "Measurable outcome 3"

  pirate_metrics_aarrr:
    acquisition: "How do users find us?"
    activation: "Do users have a great first experience?"
    retention: "Do users come back?"
    referral: "Do users tell others?"
    revenue: "Do users pay?"

  metric_types:
    leading: "Predict future outcomes (signups, engagement)"
    lagging: "Measure actual outcomes (revenue, churn)"
    guardrail: "Ensure we don't break things (error rate, load time)"
```

---

## Tools & Templates

### Discovery Canvas

```
┌────────────────────────────────────────────────────────────────┐
│                    PRODUCT DISCOVERY CANVAS                    │
├────────────────────────────────────────────────────────────────┤
│ PROBLEM SPACE                    │ SOLUTION SPACE              │
├──────────────────────────────────┼─────────────────────────────┤
│ Target Users:                    │ Value Proposition:          │
│ • [Segment 1]                    │ • [Core benefit]            │
│ • [Segment 2]                    │ • [Differentiator]          │
│                                  │                             │
│ Pain Points:                     │ Key Features:               │
│ • [Pain 1]                       │ • [Feature 1]               │
│ • [Pain 2]                       │ • [Feature 2]               │
│                                  │                             │
│ Current Solutions:               │ Success Metrics:            │
│ • [Solution 1]                   │ • [Metric 1]                │
│ • [Solution 2]                   │ • [Metric 2]                │
│                                  │                             │
│ Jobs to be Done:                 │ MVP Scope:                  │
│ • [Job 1]                        │ • [Must have 1]             │
│ • [Job 2]                        │ • [Must have 2]             │
├──────────────────────────────────┴─────────────────────────────┤
│ VALIDATION                                                     │
├────────────────────────────────────────────────────────────────┤
│ Assumptions to Test:             │ Risks:                      │
│ • [Assumption 1]                 │ • [Risk 1]                  │
│ • [Assumption 2]                 │ • [Risk 2]                  │
│                                  │                             │
│ Experiments:                     │ Go/No-Go Criteria:          │
│ • [Experiment 1]                 │ • [Criteria 1]              │
│ • [Experiment 2]                 │ • [Criteria 2]              │
└────────────────────────────────────────────────────────────────┘
```

### Feature Specification Template

```markdown
# Feature Specification: [Feature Name]

## Overview
**Feature ID**: FEAT-001
**Priority**: Must Have | Should Have | Could Have
**RICE Score**: [Score]
**Target Release**: [Version/Date]

## User Story
As a [user type], I want to [action] so that [benefit].

## Detailed Requirements

### Functional Requirements
1. **FR-001**: [Requirement description]
   - Acceptance Criteria:
     - [ ] [Criteria 1]
     - [ ] [Criteria 2]
   - Edge Cases:
     - [Edge case 1]: [Expected behavior]

### User Interface
- **Wireframes**: [Link or embedded image]
- **User Flow**: [Step-by-step flow]
- **Accessibility**: WCAG 2.1 AA compliance required

### Technical Considerations
- **API Changes**: [Yes/No - details]
- **Database Changes**: [Yes/No - details]
- **Third-party Integrations**: [List]
- **Security Considerations**: [List]

### Dependencies
- **Requires**: [List of dependencies]
- **Blocks**: [List of features this blocks]

## Success Metrics
| Metric | Baseline | Target | Measurement Method |
|--------|----------|--------|-------------------|
| [Metric 1] | [Current] | [Goal] | [How to measure] |

## Open Questions
- [ ] [Question 1]
- [ ] [Question 2]

## Change Log
| Date | Author | Changes |
|------|--------|---------|
| [Date] | [Name] | Initial draft |
```

---

## Integration Workflows

### With Engineering (System Design)

```yaml
requirements_to_engineering:
  1_discovery:
    owner: "Product Designer"
    output: "Problem statement, user research"
    next: "Architecture review"

  2_architecture:
    owner: "System Design"
    input: "Requirements, constraints"
    output: "Technical ADR, architecture diagram"
    integration_skills: [sd-01, sd-02]

  3_refinement:
    owner: "Product + Engineering"
    activity: "Story refinement, estimation"
    output: "Sprint-ready backlog"

  4_implementation:
    owner: "Engineering"
    tracking: "Azure DevOps boards"
    monitoring: "Progress reviews"
```

### With Data Science (Validation)

```yaml
data_driven_discovery:
  quantitative_validation:
    skill: "ds-05 (Customer Analytics)"
    activities:
      - "Analyze existing user behavior"
      - "Identify usage patterns"
      - "Segment analysis"

  experimentation:
    skill: "ds-07 (Experimentation)"
    activities:
      - "A/B test hypothesis"
      - "Feature flag experiments"
      - "Statistical significance"
```

---

## Quick Wins

### 5-Minute Problem Statement
```
1. Who is affected? [User segment]
2. What's the problem? [One sentence]
3. What's the impact? [Quantify if possible]
4. What's the current workaround? [How they cope]
5. Why solve it now? [Urgency/opportunity]
```

### 15-Minute Feature Brief
```
1. User Story (2 min): As a... I want... So that...
2. Acceptance Criteria (5 min): 3-5 testable criteria
3. Success Metric (3 min): How will we know it worked?
4. Dependencies (2 min): What else is needed?
5. Risks (3 min): What could go wrong?
```

### 1-Hour PRD Sprint
```
1. Problem Statement (10 min)
2. User Stories (15 min)
3. Functional Requirements (20 min)
4. Success Metrics (10 min)
5. Risks & Dependencies (5 min)
```

---

## Best Practices

1. **Start with the problem, not the solution**
2. **Validate assumptions with user research**
3. **Write clear, testable acceptance criteria**
4. **Prioritize ruthlessly using data**
5. **Document decisions for future reference**
6. **Keep requirements living documents**
7. **Involve engineering early**
8. **Define success metrics before building**

---

## Related Skills

- **pd-02**: User Research & Insights (validate requirements)
- **pd-05**: Product-Market Fit Analysis (market validation)
- **sd-02**: Requirements Engineering (technical requirements)
- **ds-05**: Customer Analytics (data-driven insights)
