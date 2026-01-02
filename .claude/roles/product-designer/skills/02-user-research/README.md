# pd-02: User Research & Insights

> **Understand Your Users**: Systematic methods for gathering, analyzing, and synthesizing user insights to inform product decisions.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Skill ID** | pd-02 |
| **Role** | Product Designer |
| **Complexity** | Medium |
| **Dependencies** | None |
| **Outputs** | Research Reports, Personas, Journey Maps |

---

## Core Capabilities

### 1. User Interview Design

```yaml
interview_framework:
  preparation:
    research_questions:
      - "What are we trying to learn?"
      - "What decisions will this inform?"
      - "What's our hypothesis to validate/invalidate?"

    participant_criteria:
      - Target segment characteristics
      - Usage patterns (new, power user, churned)
      - Diversity considerations

    interview_structure:
      opening: "5 min - Build rapport, explain purpose"
      warm_up: "5 min - Easy background questions"
      core: "30 min - Deep dive on research questions"
      exploration: "10 min - Follow unexpected threads"
      closing: "5 min - Summary, next steps, thank you"

  question_types:
    behavioral: "Tell me about the last time you..."
    contextual: "Walk me through how you typically..."
    emotional: "How did that make you feel?"
    comparative: "How does this compare to...?"
    projective: "If you could wave a magic wand..."

  interview_guide_template: |
    # User Interview Guide: [Topic]

    ## Objectives
    1. [Research objective 1]
    2. [Research objective 2]

    ## Warm-Up (5 min)
    - Tell me about your role and how long you've been in it.
    - What does a typical day look like for you?

    ## Core Questions (30 min)

    ### Theme 1: [Topic]
    - [Open-ended question]
      - Follow-up: [Probe deeper]
      - Follow-up: [Explore emotions]

    ### Theme 2: [Topic]
    - [Open-ended question]
      - Follow-up: [Probe deeper]

    ## Closing (5 min)
    - Is there anything else you'd like to share?
    - Would you be open to follow-up questions?

  synthesis_framework:
    step_1: "Transcribe or summarize each interview"
    step_2: "Extract key quotes and observations"
    step_3: "Identify patterns across interviews"
    step_4: "Create affinity diagram"
    step_5: "Synthesize into insights and recommendations"
```

### 2. Survey Design & Analysis

```yaml
survey_design:
  question_types:
    scale:
      likert: "1-5 agree/disagree"
      nps: "0-10 likelihood to recommend"
      semantic_differential: "Easy ---- Difficult"

    multiple_choice:
      single_select: "Choose one option"
      multi_select: "Choose all that apply"
      ranking: "Order by preference"

    open_ended:
      short_text: "Brief response"
      long_text: "Detailed feedback"

  best_practices:
    - "Start with easy, engaging questions"
    - "Group related questions together"
    - "Use simple, unambiguous language"
    - "Avoid leading questions"
    - "Include 'Other' options with text input"
    - "Keep surveys under 5 minutes"
    - "Test with 3-5 people before launching"

  sample_size_calculator:
    formula: "n = (Z² × p × (1-p)) / e²"
    where:
      Z: "1.96 for 95% confidence"
      p: "0.5 for maximum variability"
      e: "margin of error (e.g., 0.05 for ±5%)"
    example:
      confidence: "95%"
      margin_of_error: "5%"
      sample_size: "385 responses"

  nps_analysis:
    calculation: "% Promoters (9-10) - % Detractors (0-6)"
    benchmarks:
      excellent: ">70"
      good: "50-70"
      acceptable: "30-50"
      needs_improvement: "<30"
```

### 3. Persona Development

```markdown
# Persona Template

## [Persona Name]

![Photo placeholder]

**Demographics**
- Age: [Range]
- Role: [Job title]
- Industry: [Sector]
- Location: [Region]
- Tech savviness: [Low/Medium/High]

**Quote**
> "[Representative quote that captures their mindset]"

---

### Goals
1. [Primary goal]
2. [Secondary goal]
3. [Tertiary goal]

### Frustrations
1. [Pain point 1]
2. [Pain point 2]
3. [Pain point 3]

### Behaviors
- [Typical behavior pattern]
- [Tool/product usage]
- [Information seeking habits]

### Needs
| Need | Priority | Current Solution |
|------|----------|------------------|
| [Need 1] | High | [How they solve it today] |
| [Need 2] | Medium | [How they solve it today] |

### Scenario
[A day-in-the-life story that illustrates their context and challenges]

---

### Products/Tools Used
- [Tool 1] - [What for]
- [Tool 2] - [What for]

### Influencers
- [Who influences their decisions]
- [Information sources they trust]

### Key Insights for Design
1. [Design implication 1]
2. [Design implication 2]
3. [Design implication 3]
```

### 4. Customer Journey Mapping

```yaml
journey_map_structure:
  stages:
    awareness: "How do they discover the need/solution?"
    consideration: "How do they evaluate options?"
    decision: "How do they choose?"
    onboarding: "How do they get started?"
    usage: "How do they use the product?"
    retention: "What keeps them coming back?"
    advocacy: "How do they share with others?"

  elements_per_stage:
    actions: "What are they doing?"
    thoughts: "What are they thinking?"
    emotions: "How are they feeling?"
    touchpoints: "Where do they interact?"
    pain_points: "What frustrates them?"
    opportunities: "How can we improve?"

  journey_map_template: |
    
                         CUSTOMER JOURNEY MAP                            
     Persona: [Name]    |    Scenario: [Context]                        
    
     STAGE      Awareness  Consider   Decision   Onboard    Usage  
    
     ACTIONS                                                       
    
     THOUGHTS                                                      
    
     EMOTIONS     → 🤔    🤔 →      →      →         
    
     TOUCHPTS                                                      
    
     PAIN PTS                                                      
    
     OPPTYS                                                        
    
```

### 5. Competitive Analysis

```yaml
competitive_analysis:
  framework:
    direct_competitors: "Same product, same market"
    indirect_competitors: "Different product, same problem"
    aspirational: "Best-in-class experiences to learn from"

  analysis_dimensions:
    product:
      - Features and capabilities
      - User experience
      - Pricing model
      - Target audience
      - Strengths and weaknesses

    market:
      - Market share
      - Brand perception
      - Customer reviews
      - Growth trajectory

    strategy:
      - Positioning
      - Go-to-market approach
      - Partnerships
      - Recent announcements

  competitive_matrix_template: |
    | Feature/Capability | Our Product | Competitor A | Competitor B | Competitor C |
    |--------------------|-------------|--------------|--------------|--------------|
    | [Feature 1]        |  Strong   |  Strong    |  Weak      |  Missing   |
    | [Feature 2]        |  Weak     |  Strong    |  Strong    |  Weak      |
    | [Feature 3]        |  Missing  |  Weak      |  Strong    |  Strong    |
    | Price              | $$          | $$$          | $            | $$           |
    | Target Segment     | SMB         | Enterprise   | Startup      | Mid-market   |

  swot_template:
    strengths: "What do we do better than competitors?"
    weaknesses: "Where do competitors outperform us?"
    opportunities: "What gaps can we exploit?"
    threats: "What competitor moves threaten us?"
```

---

## Research Methods Matrix

| Method | When to Use | Sample Size | Time Required | Output |
|--------|-------------|-------------|---------------|--------|
| **User Interviews** | Deep understanding | 5-15 | 2-4 weeks | Insights, quotes |
| **Surveys** | Quantitative validation | 100-1000+ | 1-2 weeks | Statistics, trends |
| **Usability Testing** | Evaluate designs | 5-8 | 1-2 weeks | Issues, improvements |
| **Card Sorting** | Information architecture | 15-30 | 1 week | Categories, labels |
| **A/B Testing** | Compare options | 1000+ | 2-4 weeks | Statistical winner |
| **Analytics Review** | Behavior patterns | N/A | 1-3 days | Usage data |
| **Diary Studies** | Long-term behavior | 10-20 | 2-4 weeks | Longitudinal insights |
| **Focus Groups** | Group dynamics | 6-10 per group | 1-2 weeks | Themes, consensus |

---

## Research Report Template

```markdown
# Research Report: [Study Title]

**Date**: [Date]
**Researcher**: [Name]
**Stakeholders**: [Who requested/will use this]

---

## Executive Summary
[2-3 paragraph summary of key findings and recommendations]

## Research Objectives
1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

## Methodology
- **Method**: [Interviews/Survey/Usability testing/etc.]
- **Participants**: [Number and criteria]
- **Duration**: [Timeframe]
- **Tools Used**: [Software, recording, analysis]

## Key Findings

### Finding 1: [Title]
**Insight**: [What we learned]
**Evidence**: [Data, quotes, observations]
**Implication**: [What this means for the product]

### Finding 2: [Title]
**Insight**: [What we learned]
**Evidence**: [Data, quotes, observations]
**Implication**: [What this means for the product]

## Recommendations

| Priority | Recommendation | Rationale | Effort |
|----------|----------------|-----------|--------|
| High | [Recommendation 1] | [Why] | [Est.] |
| Medium | [Recommendation 2] | [Why] | [Est.] |

## Next Steps
1. [Action item 1] - Owner: [Name] - Due: [Date]
2. [Action item 2] - Owner: [Name] - Due: [Date]

## Appendix
- Raw data
- Interview transcripts
- Survey results
- Participant demographics
```

---

## Quick Wins

### 5-Minute Insight Capture
After any user interaction:
1. What surprised you?
2. What confirmed your assumptions?
3. What new questions emerged?
4. What would you do differently next time?

### 30-Minute Competitive Scan
1. Google the problem you're solving (5 min)
2. Check G2/Capterra reviews for top 3 competitors (10 min)
3. Sign up for competitor free trials (10 min)
4. Note 3 strengths and 3 weaknesses each (5 min)

### 1-Hour User Interview
1. Prep interview guide from template (15 min)
2. Conduct interview (30 min)
3. Debrief and capture key quotes (15 min)

---

## Integration with Other Skills

- **pd-01**: Feed research into requirements
- **pd-03**: Use insights to fuel brainstorming
- **pd-04**: Inform UX design decisions
- **ds-05**: Combine with customer analytics
- **ds-07**: Design experiments to validate findings
