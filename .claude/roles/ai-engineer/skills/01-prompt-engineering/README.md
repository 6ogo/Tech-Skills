# Skill 1: Prompt Engineering & Optimization

## 🎯 Overview
Master the art and science of crafting, versioning, and optimizing prompts for production LLM applications.

## 🔗 Connections
- **ML Engineer**: Model evaluation and performance metrics (ml-01)
- **MLOps**: Prompt versioning and experiment tracking (mo-01, mo-03)
- **Data Scientist**: A/B testing and statistical analysis of prompt variations (ds-08)
- **System Design**: Cost optimization and latency management (sd-05)
- **FinOps**: LLM cost optimization, prompt caching strategies (fo-01, fo-03, fo-07)
- **DevOps**: CI/CD for prompt templates, version control (do-01, do-05)
- **Security Architect**: Prompt injection prevention, content safety (sa-08)

## 🛠️ Tools Included

### 1. `prompt_template_manager.py`
Version-controlled prompt template system with variable injection and inheritance.

### 2. `token_cost_estimator.py`
Calculate costs across providers (OpenAI, Claude, Gemini) with real-time pricing.

### 3. `prompt_ab_tester.py`
A/B testing framework for comparing prompt variations with statistical significance.

### 4. `prompt_quality_scorer.py`
Automated quality scoring for relevance, coherence, and factuality.

## 📊 Key Metrics
- Token efficiency (output quality per token)
- Cost per query
- Response latency
- Quality scores (0-100)

## 🚀 Quick Start

```python
from prompt_template_manager import PromptTemplate
from token_cost_estimator import estimate_cost

# Load a template
template = PromptTemplate.load("marketing_email_generator")

# Inject variables
prompt = template.render(product="AI Course", audience="Data Scientists")

# Estimate cost
cost = estimate_cost(prompt, model="gpt-4", provider="openai")
print(f"Estimated cost: ${cost:.4f}")
```

## 📚 Best Practices

### Cost Optimization (FinOps Integration)
1. **Enable Prompt Caching** - Save up to 90% on costs by caching system prompts and context
   - Cache static system prompts with `cache_control: ephemeral`
   - Cache large knowledge bases and conversation history
   - Monitor cache hit rates and adjust caching strategy
   - Reference: FinOps fo-07 (AI/ML Cost Optimization)

2. **Track and Optimize Token Usage**
   - Monitor input/output token ratios
   - Set token budgets per application/user
   - Use smaller models (Haiku) for simple tasks, Sonnet/Opus for complex reasoning
   - Implement token usage alerts and cost dashboards
   - Reference: FinOps fo-01 (Cost Monitoring), fo-03 (Budget Management)

3. **Optimize Prompt Length**
   - Remove redundant instructions
   - Use structured prompts with clear sections
   - Implement dynamic context pruning for long conversations
   - Reference: AI Engineer best practices on prompt optimization

### Version Control & Deployment (DevOps Integration)
4. **Version Prompts with Semantic Versioning**
   - Store prompts in Git with version tags (v1.0.0, v1.1.0)
   - Use CI/CD pipelines to deploy prompt changes
   - Implement blue-green deployments for critical prompts
   - Reference: DevOps do-01 (CI/CD), do-05 (GitOps)

5. **Automate Prompt Testing**
   - Run automated tests on prompt changes before deployment
   - Use golden datasets for regression testing
   - Implement quality gates in CI/CD pipelines
   - Reference: DevOps do-02 (Testing Automation)

### Experimentation & Quality (MLOps Integration)
6. **Use A/B Testing for Production Changes**
   - Deploy prompt variations to subset of users
   - Track statistical significance before full rollout
   - Use experiment tracking (MLflow, Azure ML)
   - Reference: MLOps mo-01 (Experiment Tracking), Data Scientist ds-08

7. **Monitor Quality Metrics Over Time**
   - Track quality score degradation (model drift)
   - Set up alerts for quality drops below thresholds
   - Implement continuous evaluation pipelines
   - Reference: MLOps mo-04 (Monitoring), ML Engineer ml-05

### Security & Compliance
8. **Prevent Prompt Injection Attacks**
   - Validate and sanitize user inputs
   - Use structured prompts with clear delimiters
   - Implement content safety filters
   - Reference: Security Architect sa-08 (LLM Security)

9. **Audit Prompt Usage**
   - Log all prompt executions for compliance
   - Track PII in prompts and responses
   - Implement GDPR-compliant data retention
   - Reference: Security Architect sa-01 (PII Detection)

### Azure-Specific Best Practices
10. **Leverage Azure OpenAI Features**
    - Use managed identities for authentication
    - Enable diagnostic logging to Azure Monitor
    - Implement retry logic with exponential backoff
    - Use provisioned throughput for high-volume applications
    - Reference: Azure az-05 (Azure OpenAI Service)

## 💰 Cost Optimization Examples

### Prompt Caching Implementation (90% Cost Savings)
```python
from anthropic import Anthropic

client = Anthropic()

# Without caching: $0.015 per request
# With caching: $0.0015 per request (10x cheaper!)

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=2048,
    system=[
        {
            "type": "text",
            "text": "You are a customer support AI assistant with access to our knowledge base...",
            "cache_control": {"type": "ephemeral"}  # Cache this! Saves 90%
        },
        {
            "type": "text",
            "text": LARGE_KNOWLEDGE_BASE,  # 50K tokens
            "cache_control": {"type": "ephemeral"}  # Cache this too!
        }
    ],
    messages=[{"role": "user", "content": user_message}]
)

# Monitor cache performance
print(f"Cache hit rate: {response.usage.cache_read_input_tokens / response.usage.input_tokens * 100:.1f}%")
print(f"Cost savings: ${calculate_savings(response.usage):.4f}")
```

### Cost Tracking Dashboard
```python
from token_cost_estimator import LLMCostTracker

tracker = LLMCostTracker()

# Track all requests
tracker.log_request(
    model="claude-3-5-sonnet",
    input_tokens=1000,
    output_tokens=500,
    cached_tokens=800,
    user_id="team_alpha",
    project="customer_support"
)

# Generate cost reports
monthly_report = tracker.generate_report(period="monthly")
print(f"Total cost: ${monthly_report.total_cost}")
print(f"Cost by team: {monthly_report.cost_by_user}")
print(f"Savings from caching: ${monthly_report.cache_savings}")

# Set budget alerts
tracker.set_budget_alert(
    project="customer_support",
    monthly_budget=1000.00,
    alert_threshold=0.8  # Alert at 80%
)
```

## 🚀 CI/CD for Prompt Templates

### Git-Based Prompt Versioning
```yaml
# .github/workflows/prompt-deployment.yml
name: Deploy Prompts

on:
  push:
    paths:
      - 'prompts/**'
    branches:
      - main

jobs:
  test-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Run prompt tests
        run: pytest tests/test_prompts.py

      - name: A/B test new prompts
        run: python scripts/ab_test_prompts.py --canary 10%

      - name: Deploy to production
        if: success()
        run: python scripts/deploy_prompts.py --env production

      - name: Monitor quality metrics
        run: python scripts/monitor_quality.py --duration 1h
```

## 📊 Enhanced Metrics

| Metric | Description | Target | Monitoring Tool |
|--------|-------------|--------|-----------------|
| **Token Efficiency** | Output quality per token | >0.8 | Custom dashboard |
| **Cost per Query** | Average cost including caching | <$0.01 | Azure Monitor + FinOps dashboard |
| **Cache Hit Rate** | % of tokens served from cache | >70% | Application Insights |
| **Response Latency** | P95 latency | <2s | Azure Monitor |
| **Quality Score** | Automated quality rating | >85/100 | MLOps monitoring |
| **A/B Test Win Rate** | % of new prompts that beat baseline | >60% | MLflow experiments |

## 🔄 Integration with Other Skills

### End-to-End Workflow
```
1. Develop Prompt (ai-01)
   ↓
2. Version in Git (do-05)
   ↓
3. A/B Test (ds-08, mo-01)
   ↓
4. Monitor Costs (fo-01, fo-07)
   ↓
5. Deploy via CI/CD (do-01)
   ↓
6. Monitor Quality (ml-05, mo-04)
   ↓
7. Optimize Caching (fo-07)
```

## 🎯 Quick Wins
1. **Enable caching today** - Immediate 70-90% cost reduction for conversational apps
2. **Set up cost tracking** - Know where your LLM budget is going
3. **Version prompts in Git** - Enable rollbacks and A/B testing
4. **Automate testing** - Catch regressions before production
5. **Monitor quality** - Detect model drift early
