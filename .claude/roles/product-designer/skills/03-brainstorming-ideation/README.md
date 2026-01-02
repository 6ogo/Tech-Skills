# pd-03: Brainstorming & Ideation

> **Generate Breakthrough Ideas**: Structured techniques for creative problem-solving and innovative solution discovery.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Skill ID** | pd-03 |
| **Role** | Product Designer |
| **Complexity** | Basic to Medium |
| **Dependencies** | pd-01 (Problem definition) |
| **Outputs** | Idea backlog, Concept sketches, Evaluation matrices |

---

## Core Ideation Frameworks

### 1. SCAMPER Method

```yaml
scamper:
  description: "Systematic prompts to transform existing ideas"

  S_substitute:
    question: "What can be substituted?"
    prompts:
      - "What materials, components, or people could be swapped?"
      - "What process could replace the current one?"
      - "What if we used different technology?"
    example: "Substitute in-person meetings with async video messages"

  C_combine:
    question: "What can be combined?"
    prompts:
      - "What ideas, features, or purposes could be merged?"
      - "What if we combined this with another product?"
      - "How could we bundle services together?"
    example: "Combine note-taking with AI summarization"

  A_adapt:
    question: "What can be adapted?"
    prompts:
      - "What else is like this? What could we copy?"
      - "What ideas from other industries could apply?"
      - "How did others solve similar problems?"
    example: "Adapt Spotify's discovery algorithm for learning content"

  M_modify:
    question: "What can be modified?"
    prompts:
      - "What can be made bigger, smaller, faster, slower?"
      - "What features could be emphasized or minimized?"
      - "How could the form, shape, or structure change?"
    example: "Modify the onboarding to be 80% shorter"

  P_put_to_other_use:
    question: "What else could this be used for?"
    prompts:
      - "What other markets could use this?"
      - "What if different users tried this?"
      - "Could this solve a different problem?"
    example: "Use project management tool for personal goal tracking"

  E_eliminate:
    question: "What can be eliminated?"
    prompts:
      - "What features could be removed?"
      - "What if we simplified dramatically?"
      - "What's the minimum viable version?"
    example: "Eliminate account creation - use magic links only"

  R_reverse:
    question: "What can be reversed or rearranged?"
    prompts:
      - "What if we did the opposite?"
      - "What if we reversed the order?"
      - "What if users became creators?"
    example: "Reverse the pricing - pay what you want"
```

### 2. Six Thinking Hats

```yaml
six_thinking_hats:
  description: "Parallel thinking for comprehensive exploration"

  white_hat:
    focus: "Facts and Information"
    questions:
      - "What data do we have?"
      - "What data do we need?"
      - "What are the known facts?"
    duration: "5-10 minutes"

  red_hat:
    focus: "Emotions and Intuition"
    questions:
      - "How do you feel about this idea?"
      - "What's your gut reaction?"
      - "What would users feel?"
    duration: "3-5 minutes"

  black_hat:
    focus: "Critical Judgment"
    questions:
      - "What could go wrong?"
      - "What are the risks?"
      - "Why might this fail?"
    duration: "5-10 minutes"

  yellow_hat:
    focus: "Optimism and Benefits"
    questions:
      - "What are the benefits?"
      - "Why might this work?"
      - "What's the best case scenario?"
    duration: "5-10 minutes"

  green_hat:
    focus: "Creativity and Alternatives"
    questions:
      - "What else could we try?"
      - "What's a crazy alternative?"
      - "How could we overcome the black hat concerns?"
    duration: "10-15 minutes"

  blue_hat:
    focus: "Process and Summary"
    questions:
      - "What have we decided?"
      - "What are the next steps?"
      - "What thinking is still needed?"
    duration: "5 minutes"

  facilitation_order:
    opening: "Blue - Set the agenda"
    exploration: "White → Red → Black → Yellow → Green"
    closing: "Blue - Summarize and decide"
```

### 3. Design Sprint (5-Day Framework)

```yaml
design_sprint:
  day_1_understand:
    morning:
      - "Expert interviews (30 min each)"
      - "Lightning demos from competitors"
      - "How Might We notes"
    afternoon:
      - "Long-term goal definition"
      - "Sprint questions"
      - "Map the user journey"
    output: "Shared understanding, target area identified"

  day_2_diverge:
    morning:
      - "Lightning demos (inspiration)"
      - "4-step sketch process"
    afternoon:
      - "Crazy 8s (8 ideas in 8 minutes)"
      - "Solution sketch (detailed concept)"
    output: "Individual solution sketches"

  day_3_decide:
    morning:
      - "Art museum (review all sketches)"
      - "Heat map voting"
      - "Speed critique (3 min each)"
    afternoon:
      - "Straw poll"
      - "Super vote (decider picks)"
      - "Storyboard the winner"
    output: "Winning concept with storyboard"

  day_4_prototype:
    all_day:
      - "Divide and conquer prototyping"
      - "Facade prototype (looks real, isn't)"
      - "Prepare for testing"
    tools: "Figma, Keynote, or paper"
    output: "Testable prototype"

  day_5_test:
    all_day:
      - "5 user interviews (1 hour each)"
      - "Team observes and takes notes"
      - "Debrief after each session"
      - "Final pattern identification"
    output: "Validated learnings, next steps"
```

### 4. Crazy 8s Exercise

```yaml
crazy_8s:
  description: "Rapid sketching to generate volume of ideas"

  setup:
    materials: "Paper, pen, timer"
    duration: "8 minutes total"
    format: "Fold paper into 8 sections"

  process:
    step_1: "Set timer for 8 minutes"
    step_2: "Sketch one idea per section (1 min each)"
    step_3: "No talking, just draw"
    step_4: "Quantity over quality"
    step_5: "Words and arrows are fine"

  variations:
    crazy_4s: "4 minutes, 4 ideas (for beginners)"
    crazy_16s: "16 minutes, 16 ideas (deep exploration)"
    themed_8s: "All 8 variations of one concept"

  facilitation_tips:
    - "Start with a clear problem statement"
    - "Show examples of rough sketches"
    - "Encourage wild ideas"
    - "No judgment during sketching"
    - "Share and discuss after"
```

### 5. How Might We (HMW)

```yaml
how_might_we:
  description: "Reframe problems as opportunity questions"

  formula: "How might we [verb] [user] [outcome]?"

  examples:
    problem: "Users forget to complete their profile"
    hmw_variations:
      - "HMW make profile completion feel rewarding?"
      - "HMW reduce the information needed in profiles?"
      - "HMW remind users at the right moment?"
      - "HMW make profiles optional but valuable?"
      - "HMW let users build profiles gradually?"

  quality_criteria:
    too_narrow: "How might we add a progress bar?"
    too_broad: "How might we improve onboarding?"
    just_right: "How might we show users the value of completing profiles?"

  workshop_format:
    step_1: "Present problem/insight (5 min)"
    step_2: "Individual HMW writing on sticky notes (5 min)"
    step_3: "Post all HMWs on wall"
    step_4: "Silent reading and grouping (5 min)"
    step_5: "Dot voting for top HMWs (3 min)"
    step_6: "Select 3-5 HMWs to ideate on"
```

---

## Idea Evaluation Frameworks

### Feasibility-Desirability-Viability

```yaml
fdv_framework:
  desirability:
    question: "Do users want this?"
    criteria:
      - "Solves a real problem"
      - "Users would pay/use this"
      - "Better than alternatives"
    weight: 0.4

  feasibility:
    question: "Can we build this?"
    criteria:
      - "Technical capability exists"
      - "Resources available"
      - "Timeline is realistic"
    weight: 0.3

  viability:
    question: "Should we build this?"
    criteria:
      - "Aligns with business goals"
      - "Sustainable business model"
      - "Competitive advantage"
    weight: 0.3

  scoring:
    scale: "1-5 for each dimension"
    calculation: "(D × 0.4) + (F × 0.3) + (V × 0.3)"
```

### Idea Evaluation Matrix

```markdown
| Idea | Desirability | Feasibility | Viability | Score | Priority |
|------|--------------|-------------|-----------|-------|----------|
| [Idea 1] | 5 | 3 | 4 | 4.1 | High |
| [Idea 2] | 4 | 5 | 3 | 3.9 | Medium |
| [Idea 3] | 3 | 4 | 5 | 3.8 | Medium |
| [Idea 4] | 5 | 2 | 4 | 3.8 | Low (tech risk) |
```

### Impact-Effort Matrix

```
                     HIGH IMPACT
                         
    
                                            
       BIG BETS            QUICK WINS       
       (Plan carefully)    (Do first!)      
                                            
HIGH LOW
EFFORT                                       EFFORT
                                            
       MONEY PIT           FILL-INS         
       (Avoid)             (Do if time)     
                                            
    
                         
                     LOW IMPACT
```

---

## Workshop Facilitation Templates

### 1-Hour Ideation Session

```yaml
session_structure:
  00_05:
    activity: "Context setting"
    description: "Share problem statement, constraints, goals"

  05_15:
    activity: "Inspiration round"
    description: "Share 3-5 examples of how others solved similar problems"

  15_25:
    activity: "Crazy 8s"
    description: "Individual sketching, 8 ideas in 8 minutes"

  25_40:
    activity: "Share and cluster"
    description: "Present ideas, group similar ones"

  40_50:
    activity: "Dot voting"
    description: "3 dots per person on favorite ideas"

  50_60:
    activity: "Discussion and next steps"
    description: "Discuss top ideas, assign owners"
```

### 2-Hour Deep Dive

```yaml
session_structure:
  00_15:
    activity: "Problem deep dive"
    description: "Present research insights, user quotes, data"

  15_30:
    activity: "HMW generation"
    description: "Write How Might We questions"

  30_45:
    activity: "SCAMPER exploration"
    description: "Apply SCAMPER to top HMW"

  45_65:
    activity: "Concept sketching"
    description: "Develop 2-3 detailed concepts"

  65_90:
    activity: "Six Thinking Hats review"
    description: "Evaluate concepts from all perspectives"

  90_110:
    activity: "Prioritization"
    description: "Score using Impact-Effort matrix"

  110_120:
    activity: "Action planning"
    description: "Define next steps for top concept"
```

---

## Quick Wins

### 5-Minute Brainstorm Burst
1. Write problem at top of page
2. Set 5-minute timer
3. Write every idea that comes to mind
4. No filtering or judgment
5. Aim for 15+ ideas

### 15-Minute Concept Exploration
1. Pick one idea from brainstorm (2 min)
2. Sketch the user flow (5 min)
3. List 3 risks and 3 benefits (4 min)
4. Define one experiment to validate (4 min)

### "Yes, And..." Exercise
1. Partner shares an idea
2. You say "Yes, and..." and build on it
3. Partner says "Yes, and..." and builds more
4. Continue for 3-5 rounds
5. No "but" or "no" allowed

---

## Best Practices

1. **Diverge before converging** - Generate many ideas before evaluating
2. **Defer judgment** - Critique kills creativity in early stages
3. **Go for quantity** - More ideas = better chance of breakthrough
4. **Build on others' ideas** - "Yes, and..." mindset
5. **Encourage wild ideas** - They often lead to practical innovations
6. **Be visual** - Sketches communicate better than words
7. **One conversation at a time** - Focus enables depth
8. **Stay on topic** - Tangents waste group energy

---

## Related Skills

- **pd-01**: Define the problem before ideating
- **pd-02**: Use research insights as inspiration
- **pd-04**: Turn concepts into UX designs
- **ai-01**: Use AI to expand idea generation
