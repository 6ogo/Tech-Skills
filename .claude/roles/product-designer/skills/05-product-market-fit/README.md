# pd-05: Product-Market Fit Analysis

> **Find Your Market**: Validate that your product solves a real problem for a viable market before scaling.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Skill ID** | pd-05 |
| **Role** | Product Designer |
| **Complexity** | Advanced |
| **Dependencies** | pd-01, pd-02 |
| **Outputs** | Market Analysis, Value Proposition, MVP Definition |

---

## Core Frameworks

### 1. Product-Market Fit Definition

```yaml
pmf_definition:
  marc_andreessen: |
    "Product-market fit means being in a good market with a product
    that can satisfy that market."

  indicators_of_pmf:
    strong_signals:
      - "Users would be very disappointed without your product (>40%)"
      - "Organic word-of-mouth growth"
      - "High retention rates"
      - "Users pay without heavy discounting"
      - "Usage increases over time"

    weak_signals:
      - "High churn rates"
      - "Constant feature requests"
      - "Users don't recommend"
      - "Heavy discounting needed"
      - "Flat or declining usage"

  pmf_survey:
    question: "How would you feel if you could no longer use [Product]?"
    scale:
      - "Very disappointed"
      - "Somewhat disappointed"
      - "Not disappointed"
    benchmark: ">40% 'Very disappointed' = PMF achieved"
```

### 2. Market Opportunity Assessment

```yaml
market_assessment:
  tam_sam_som:
    tam:
      name: "Total Addressable Market"
      definition: "Total revenue opportunity if 100% market share"
      calculation: "Total potential customers × Average revenue per customer"

    sam:
      name: "Serviceable Addressable Market"
      definition: "Portion of TAM you can realistically reach"
      factors:
        - "Geographic limitations"
        - "Product fit limitations"
        - "Channel access"

    som:
      name: "Serviceable Obtainable Market"
      definition: "Realistic market share in near term"
      factors:
        - "Competition"
        - "Resources"
        - "Go-to-market capability"

  market_sizing_methods:
    top_down:
      approach: "Start with industry data, narrow down"
      sources:
        - "Industry reports (Gartner, Forrester)"
        - "Government statistics"
        - "Public company filings"

    bottom_up:
      approach: "Build from individual customer data"
      calculation: |
        Number of potential customers ×
        Conversion rate ×
        Average deal size ×
        Purchase frequency

  market_attractiveness:
    factors:
      - size: "Is the market big enough?"
      - growth: "Is the market growing?"
      - profitability: "Can we make money here?"
      - competition: "How intense is competition?"
      - barriers: "Can we enter and defend?"
```

### 3. Value Proposition Canvas

```yaml
value_proposition_canvas:
  customer_profile:
    jobs:
      functional: "Tasks they're trying to complete"
      social: "How they want to be perceived"
      emotional: "How they want to feel"

    pains:
      obstacles: "What prevents them from getting the job done?"
      risks: "What could go wrong?"
      negative_outcomes: "What do they want to avoid?"

    gains:
      required: "Basic expectations"
      expected: "Standard features"
      desired: "Things they'd love but don't expect"
      unexpected: "Delighters"

  value_map:
    products_services:
      - "Core product features"
      - "Supporting services"
      - "Add-ons and extras"

    pain_relievers:
      - "How do we eliminate/reduce pains?"
      - "Which pains do we address?"

    gain_creators:
      - "How do we create gains?"
      - "Which gains do we create?"

  fit_assessment:
    questions:
      - "Does our product address the most important jobs?"
      - "Do we relieve the most severe pains?"
      - "Do we create meaningful gains?"
      - "Is our solution better than alternatives?"
```

### 4. MVP Definition

```yaml
mvp_framework:
  definition: "Minimum Viable Product - smallest thing that tests your hypothesis"

  mvp_types:
    landing_page:
      purpose: "Test demand and messaging"
      build_time: "1-3 days"
      example: "Dropbox video MVP"

    wizard_of_oz:
      purpose: "Test experience without building backend"
      build_time: "1-2 weeks"
      example: "Manual processes behind automated facade"

    concierge:
      purpose: "Deliver value manually to learn"
      build_time: "None"
      example: "Personal service before productizing"

    single_feature:
      purpose: "Test core value proposition"
      build_time: "2-4 weeks"
      example: "One killer feature only"

    piecemeal:
      purpose: "Combine existing tools"
      build_time: "Days"
      example: "Zapier + Typeform + Airtable"

  mvp_canvas: |
    
                           MVP CANVAS                            
    
     HYPOTHESIS                    SUCCESS METRICS              
     We believe [target users]     We'll know we're right if:   
     will [behavior]               • [Metric 1] > [Target]      
     because [reason]              • [Metric 2] > [Target]      
    
     MUST HAVE                     MUST NOT HAVE                
     • [Feature 1]                 • [Feature A]                
     • [Feature 2]                 • [Feature B]                
     • [Feature 3]                 • [Feature C]                
    
     BUILD TIME                    LEARN BY                     
     [X weeks]                     [Date]                       
    
```

### 5. Go-to-Market Strategy

```yaml
gtm_strategy:
  positioning:
    formula: |
      For [target customer]
      Who [statement of need]
      [Product] is a [category]
      That [key benefit]
      Unlike [competition]
      Our product [differentiator]

    example: |
      For busy professionals
      Who struggle to find time for learning
      LearnFast is a micro-learning platform
      That delivers 5-minute lessons on the go
      Unlike traditional courses
      Our product uses AI to personalize content to your schedule

  channel_strategy:
    owned:
      - "Website/app"
      - "Email list"
      - "Blog content"
      - "Social media"

    earned:
      - "Word of mouth"
      - "PR/media coverage"
      - "Reviews"
      - "SEO"

    paid:
      - "Search ads"
      - "Social ads"
      - "Sponsorships"
      - "Influencer partnerships"

  launch_phases:
    phase_1_alpha:
      audience: "Internal team, close friends"
      goal: "Find major bugs, validate core value"
      duration: "1-2 weeks"

    phase_2_beta:
      audience: "Waitlist, early adopters"
      goal: "Gather feedback, iterate"
      duration: "4-8 weeks"

    phase_3_limited:
      audience: "Broader invite-only"
      goal: "Test scale, refine messaging"
      duration: "2-4 weeks"

    phase_4_public:
      audience: "General availability"
      goal: "Growth and optimization"
      duration: "Ongoing"
```

### 6. Pricing Strategy

```yaml
pricing_analysis:
  pricing_models:
    freemium:
      description: "Free tier with paid upgrades"
      when_to_use: "High volume, low marginal cost"
      example: "Slack, Dropbox"

    subscription:
      description: "Recurring payment for access"
      when_to_use: "Ongoing value delivery"
      example: "Netflix, SaaS products"

    usage_based:
      description: "Pay per use"
      when_to_use: "Variable consumption"
      example: "AWS, Twilio"

    one_time:
      description: "Single purchase"
      when_to_use: "Standalone products"
      example: "Software licenses"

    tiered:
      description: "Multiple packages at price points"
      when_to_use: "Diverse customer segments"
      example: "Most SaaS products"

  van_westendorp:
    questions:
      - "At what price would it be too expensive?"
      - "At what price would it be so cheap you'd question quality?"
      - "At what price does it start to feel expensive but worth it?"
      - "At what price is it a bargain?"

    analysis: "Plot responses to find optimal price range"

  competitive_pricing:
    positions:
      premium: "Higher than market, justify with value"
      parity: "Match market rates"
      penetration: "Lower to gain share"
```

---

## PMF Measurement Dashboard

```markdown
## Product-Market Fit Dashboard

### Leading Indicators

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| PMF Survey Score (Very Disappointed) | X% | >40% | 🟡 |
| Weekly Active Users (WAU) | X | +X% MoM | 🟢 |
| Activation Rate | X% | >50% |  |
| NPS Score | X | >50 | 🟡 |

### Retention Metrics

| Cohort | Week 1 | Week 4 | Week 8 | Week 12 |
|--------|--------|--------|--------|---------|
| Jan '25 | 100% | X% | X% | X% |
| Feb '25 | 100% | X% | X% | - |
| Mar '25 | 100% | X% | - | - |

### Growth Metrics

| Channel | Acquisition | Conversion | CAC | LTV |
|---------|-------------|------------|-----|-----|
| Organic | X | X% | $X | $X |
| Paid | X | X% | $X | $X |
| Referral | X | X% | $X | $X |

### Qualitative Signals
- User feedback themes: [List]
- Top feature requests: [List]
- Churn reasons: [List]
```

---

## Quick Wins

### 15-Minute Market Sizing
1. Define your target customer (3 min)
2. Estimate total potential customers (5 min)
3. Estimate conversion and pricing (5 min)
4. Calculate TAM/SAM/SOM (2 min)

### 30-Minute Value Prop
1. List top 3 customer jobs (5 min)
2. List top 3 pains (5 min)
3. List top 3 gains they want (5 min)
4. Map your features to jobs/pains/gains (10 min)
5. Write positioning statement (5 min)

### 1-Hour PMF Assessment
1. Create PMF survey (10 min)
2. Send to 50+ users (5 min)
3. Analyze retention cohorts (15 min)
4. Review qualitative feedback (15 min)
5. Identify top 3 improvement areas (15 min)

---

## Related Skills

- **pd-01**: Define requirements based on market needs
- **pd-02**: Conduct market research
- **ds-05**: Analyze customer data
- **ds-07**: Design pricing experiments
- **fo-01**: Model revenue and costs
