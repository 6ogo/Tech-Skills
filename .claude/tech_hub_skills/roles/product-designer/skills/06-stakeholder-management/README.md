# pd-06: Stakeholder Management

> **Align and Deliver**: Techniques for gathering requirements, managing expectations, and driving alignment across teams.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Skill ID** | pd-06 |
| **Role** | Product Designer |
| **Complexity** | Medium |
| **Dependencies** | None |
| **Outputs** | Stakeholder Maps, Communication Plans, Decision Docs |

---

## Core Capabilities

### 1. Stakeholder Mapping

```yaml
stakeholder_mapping:
  identification:
    questions:
      - "Who will use this product?"
      - "Who approves/funds this project?"
      - "Who will build this?"
      - "Who is affected by this?"
      - "Who has relevant expertise?"

  power_interest_grid: |
    
                        STAKEHOLDER MAP                          
    
     HIGH                                                        
     POWER                   
                KEEP            MANAGE                       
                SATISFIED       CLOSELY                      
                                 Exec Sponsor               
                 Legal         Product Lead               
                                                              
                             
                MONITOR         KEEP                         
                (Minimal        INFORMED                     
                 effort)                                     
                 External      Users                     
     LOW                         Dev Team                  
     POWER                   
                  LOW                    HIGH                    
                          INTEREST                               
    

  stakeholder_template: |
    ## Stakeholder: [Name/Role]

    **Power Level**: High / Medium / Low
    **Interest Level**: High / Medium / Low
    **Influence**: Positive / Neutral / Negative

    **What they care about**:
    - [Priority 1]
    - [Priority 2]

    **What they need from us**:
    - [Need 1]
    - [Need 2]

    **Communication preference**:
    - Frequency: [Weekly/Bi-weekly/Monthly]
    - Format: [Meeting/Email/Slack]

    **Potential concerns**:
    - [Concern 1]
    - [Concern 2]
```

### 2. Requirements Gathering Workshops

```yaml
workshop_formats:
  discovery_workshop:
    duration: "2-3 hours"
    participants: "5-10 stakeholders"
    agenda:
      1_intro: "10 min - Purpose, ground rules"
      2_context: "20 min - Current state, pain points"
      3_vision: "30 min - Future state, success criteria"
      4_requirements: "45 min - Must have vs nice to have"
      5_constraints: "20 min - Timeline, budget, tech limits"
      6_risks: "20 min - Potential blockers"
      7_next_steps: "15 min - Actions, owners, timeline"

    facilitation_tips:
      - "Use sticky notes for equal participation"
      - "Timeboxed activities keep momentum"
      - "Park tangents in 'Parking Lot'"
      - "Summarize after each section"
      - "Capture disagreements explicitly"

  prioritization_workshop:
    duration: "1-2 hours"
    purpose: "Align on what to build first"
    techniques:
      dot_voting:
        description: "Each person gets X votes"
        pros: "Quick, democratic"
        cons: "Doesn't account for power dynamics"

      buy_a_feature:
        description: "Stakeholders 'spend' budget on features"
        pros: "Forces trade-offs"
        cons: "Requires prep work"

      moscow:
        description: "Categorize as Must/Should/Could/Won't"
        pros: "Clear categories"
        cons: "Everything becomes 'Must Have'"

      stack_ranking:
        description: "Force rank all items"
        pros: "No ties possible"
        cons: "Time-consuming for large lists"
```

### 3. Communication Planning

```yaml
communication_plan:
  template: |
    ## Communication Plan: [Project Name]

    ### Regular Updates

    | Stakeholder | Format | Frequency | Owner | Content |
    |-------------|--------|-----------|-------|---------|
    | Exec Sponsor | 1:1 | Weekly | PM | Status, risks |
    | Dev Team | Stand-up | Daily | Scrum Master | Progress |
    | All Stakeholders | Email | Bi-weekly | PM | Newsletter |

    ### Key Milestones

    | Milestone | Date | Audience | Format |
    |-----------|------|----------|--------|
    | Kickoff | [Date] | All | Meeting |
    | Design Review | [Date] | Core team | Workshop |
    | Beta Launch | [Date] | All | Announcement |

    ### Escalation Path

    1. PM escalates to Product Lead
    2. Product Lead escalates to VP Product
    3. VP Product escalates to C-Suite

  status_update_template: |
    ## Project Status Update: [Date]

    ### TL;DR
    [One sentence summary]

    ### Progress This Period
     [Completed item 1]
     [Completed item 2]

    ### In Progress
     [In progress item 1] - [Owner]
     [In progress item 2] - [Owner]

    ### Blockers / Risks
     [Blocker 1] - [Mitigation]
     [Risk 1] - [Mitigation]

    ### Upcoming
     [Next milestone] - [Date]

    ### Decisions Needed
     [Decision 1] - by [Date]
```

### 4. Decision Documentation (ADRs)

```yaml
architecture_decision_record:
  purpose: "Document decisions for future reference"

  adr_template: |
    # ADR-XXX: [Decision Title]

    **Date**: [YYYY-MM-DD]
    **Status**: Proposed | Accepted | Deprecated | Superseded
    **Deciders**: [Names]

    ## Context
    [What is the issue that we're seeing that is motivating this decision?]

    ## Decision
    [What is the change that we're proposing or have agreed to implement?]

    ## Consequences

    ### Positive
    - [Benefit 1]
    - [Benefit 2]

    ### Negative
    - [Drawback 1]
    - [Drawback 2]

    ### Neutral
    - [Trade-off 1]

    ## Alternatives Considered

    ### Option A: [Name]
    - **Pros**: [List]
    - **Cons**: [List]
    - **Why not chosen**: [Reason]

    ### Option B: [Name]
    - **Pros**: [List]
    - **Cons**: [List]
    - **Why not chosen**: [Reason]

  decision_matrix: |
    | Criteria | Weight | Option A | Option B | Option C |
    |----------|--------|----------|----------|----------|
    | [Criteria 1] | 30% | 4 | 3 | 5 |
    | [Criteria 2] | 25% | 3 | 5 | 3 |
    | [Criteria 3] | 25% | 5 | 4 | 3 |
    | [Criteria 4] | 20% | 3 | 4 | 4 |
    | **Weighted Total** | | **X.X** | **X.X** | **X.X** |
```

### 5. Change Management

```yaml
change_management:
  adkar_model:
    A_awareness: "Understanding why change is needed"
    D_desire: "Motivation to support the change"
    K_knowledge: "Information on how to change"
    A_ability: "Skills to implement the change"
    R_reinforcement: "Sustained change over time"

  change_impact_assessment: |
    ## Change Impact Assessment

    ### Change Overview
    **What's changing**: [Description]
    **Who's affected**: [Groups/roles]
    **When**: [Timeline]

    ### Impact Analysis

    | Group | Impact Level | What Changes | Support Needed |
    |-------|--------------|--------------|----------------|
    | [Group 1] | High | [Details] | [Training, etc.] |
    | [Group 2] | Medium | [Details] | [Communication] |
    | [Group 3] | Low | [Details] | [Documentation] |

    ### Resistance Mitigation
    - Anticipated resistance: [List]
    - Mitigation strategies: [List]

    ### Success Metrics
    - [Metric 1]: [Target]
    - [Metric 2]: [Target]

  training_plan:
    formats:
      - "Live training sessions"
      - "Recorded videos"
      - "Documentation/guides"
      - "Office hours/Q&A"
      - "Peer mentoring"
```

### 6. Executive Presentations

```yaml
executive_presentations:
  structure:
    situation: "What's the context? (1-2 slides)"
    complication: "What's the problem/opportunity? (1 slide)"
    question: "What decision do you need? (1 slide)"
    answer: "What's your recommendation? (1 slide)"
    evidence: "Why should they believe you? (2-3 slides)"
    ask: "What do you need from them? (1 slide)"

  tips:
    - "Lead with the ask, not the backstory"
    - "One message per slide"
    - "Data over opinions"
    - "Prepare for objections"
    - "Have backup slides for details"
    - "Respect time limits strictly"

  slide_template: |
    
     [TITLE: Action-oriented headline]                          
    
                                                                 
       • Key point 1 with supporting data                       
                                                                 
       • Key point 2 with supporting data                       
                                                                 
       • Key point 3 with supporting data                       
                                                                 
                                                                 
       [VISUAL: Chart, diagram, or image]                       
                                                                 
    
     Source: [Data source]                    Slide X of Y      
    

  one_pager_template: |
    # [Project Name] - Executive Summary

    ## The Ask
    [What you need from them in 1-2 sentences]

    ## The Opportunity
    [Problem and opportunity in 2-3 sentences]

    ## Proposed Solution
    [Your recommendation in 2-3 sentences]

    ## Key Benefits
    • [Benefit 1 with quantification]
    • [Benefit 2 with quantification]
    • [Benefit 3 with quantification]

    ## Investment Required
    • Timeline: [X months]
    • Resources: [X FTEs]
    • Budget: $[X]

    ## Risks & Mitigations
    | Risk | Mitigation |
    |------|------------|
    | [Risk 1] | [Mitigation] |

    ## Next Steps
    1. [Action 1] - [Owner] - [Date]
    2. [Action 2] - [Owner] - [Date]
```

---

## Meeting Facilitation Templates

### Requirements Meeting (60 min)

```
00:00 - 05:00  Introductions and goals
05:00 - 15:00  Context setting (current state)
15:00 - 35:00  Requirements gathering (sticky notes)
35:00 - 50:00  Prioritization (dot voting)
50:00 - 60:00  Next steps and actions
```

### Sprint Review (30 min)

```
00:00 - 02:00  Sprint goal reminder
02:00 - 20:00  Demo completed work
20:00 - 25:00  Stakeholder feedback
25:00 - 30:00  Upcoming sprint preview
```

### Steering Committee (45 min)

```
00:00 - 05:00  Status summary
05:00 - 20:00  Key decisions needed
20:00 - 35:00  Discussion
35:00 - 45:00  Actions and commitments
```

---

## Quick Wins

### 5-Minute Stakeholder Check
Before any meeting:
1. Who's the decision maker?
2. What do they care about most?
3. What's their biggest concern?
4. What outcome do I need?

### 15-Minute Status Update
1. What was accomplished (3 min)
2. What's in progress (3 min)
3. What's blocked (3 min)
4. What's next (3 min)
5. What decisions needed (3 min)

### 30-Minute Decision Doc
1. State the decision needed (5 min)
2. List 2-3 options (10 min)
3. Pros/cons for each (10 min)
4. Your recommendation (5 min)

---

## Related Skills

- **pd-01**: Gather requirements from stakeholders
- **sd-02**: Technical requirements engineering
- **pe-05**: Incident management communication
- **do-07**: Release management coordination
