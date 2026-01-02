# Skill 6: LLM Evaluation & Benchmarking

##  Overview
Build comprehensive evaluation frameworks for LLM applications including automated testing, benchmark suites, A/B testing, and continuous quality monitoring for production systems.

##  Connections
- **Data Engineer**: Test dataset curation, evaluation metrics storage (de-01, de-03)
- **Security Architect**: Adversarial testing, safety evaluation (sa-08)
- **ML Engineer**: Model comparison, performance benchmarking (ml-03, ml-05)
- **MLOps**: Continuous evaluation, metric tracking (mo-04, mo-05)
- **FinOps**: Cost-quality tradeoff analysis, evaluation budget optimization (fo-01, fo-07)
- **DevOps**: Automated testing in CI/CD, regression detection (do-01, do-06)
- **Data Scientist**: Statistical analysis, experiment design (ds-01, ds-08)

##  Tools Included

### 1. `llm_evaluator.py`
Comprehensive evaluation framework with multiple metrics (accuracy, coherence, relevance, safety).

### 2. `benchmark_runner.py`
Execute standard benchmarks (MMLU, HellaSwag, TruthfulQA) and custom task suites.

### 3. `ab_test_framework.py`
A/B testing infrastructure for comparing models, prompts, and system configurations.

### 4. `regression_detector.py`
Automated regression testing to catch quality degradation before production deployment.

### 5. `eval_dataset_builder.py`
Create and manage evaluation datasets with versioning and golden reference answers.

##  Key Metrics
- Task accuracy and F1 score
- Response coherence and fluency
- Factual accuracy and hallucination rate
- Safety and bias scores
- Cost per evaluation

##  Quick Start

```python
from llm_evaluator import LLMEvaluator, EvaluationMetrics
from benchmark_runner import BenchmarkRunner

# Initialize evaluator
evaluator = LLMEvaluator(
    metrics=[
        "accuracy",
        "coherence",
        "factuality",
        "safety",
        "relevance"
    ]
)

# Load test dataset
test_data = evaluator.load_dataset(
    name="customer_support_qa",
    version="v1.2"
)

# Evaluate model
results = evaluator.evaluate(
    model="claude-3-5-sonnet-20241022",
    test_data=test_data,
    num_samples=500
)

# Print results
print(f"Accuracy: {results.accuracy:.3f}")
print(f"Coherence: {results.coherence:.3f}")
print(f"Factuality: {results.factuality:.3f}")
print(f"Safety: {results.safety:.3f}")
print(f"Cost: ${results.total_cost:.4f}")

# Run standard benchmarks
benchmark = BenchmarkRunner()
benchmark_results = benchmark.run(
    model="claude-3-5-sonnet-20241022",
    benchmarks=["mmlu", "hellaswag", "truthfulqa"]
)

print(f"\nBenchmark Results:")
for name, score in benchmark_results.items():
    print(f"  {name}: {score:.2%}")
```

##  Best Practices

### Cost Optimization (FinOps Integration)

1. **Optimize Evaluation Frequency**
   - Run full evals only on significant changes
   - Use smoke tests for minor updates
   - Implement tiered evaluation (quick → comprehensive)
   - Schedule heavy evaluations during off-peak hours
   - Reference: FinOps fo-07 (AI/ML Cost Optimization)

2. **Sample-Based Evaluation**
   - Use statistical sampling for large datasets
   - Calculate confidence intervals
   - Start with small samples, expand if needed
   - Monitor sample size vs cost tradeoffs
   - Reference: FinOps fo-03 (Budget Management)

3. **Cache Evaluation Results**
   - Cache model outputs for test sets
   - Reuse evaluations across metrics
   - Implement incremental evaluation
   - Track cache hit rates
   - Reference: FinOps fo-01 (Cost Monitoring)

4. **Cost-Aware Benchmark Selection**
   - Prioritize high-signal benchmarks
   - Use lightweight metrics first
   - Reserve expensive evals (human review) for critical cases
   - Track evaluation cost per model
   - Reference: FinOps fo-07 (AI/ML Cost Optimization)

### Security & Privacy (Security Architect Integration)

5. **Adversarial Testing**
   - Test against prompt injection attacks
   - Evaluate jailbreaking resistance
   - Check for unsafe output generation
   - Monitor for security regression
   - Reference: Security Architect sa-08 (LLM Security)

6. **Privacy-Preserving Evaluation**
   - Anonymize evaluation datasets
   - Remove PII from test cases
   - Secure storage of evaluation results
   - Audit access to evaluation data
   - Reference: Security Architect sa-01 (PII Detection), sa-06 (Data Governance)

7. **Safety Benchmark Suite**
   - Evaluate toxic content generation
   - Test bias across demographics
   - Check compliance with safety policies
   - Red team testing for edge cases
   - Reference: Security Architect sa-08 (LLM Security)

### Data Quality & Governance (Data Engineer Integration)

8. **High-Quality Test Datasets**
   - Curate diverse, representative test sets
   - Include edge cases and failure modes
   - Version test datasets with lineage
   - Validate test data quality regularly
   - Reference: Data Engineer de-03 (Data Quality)

9. **Evaluation Data Pipeline**
   - Automate test dataset updates
   - Track dataset version and provenance
   - Implement data validation checks
   - Monitor dataset drift over time
   - Reference: Data Engineer de-01 (Data Ingestion), de-02 (ETL)

### Model Lifecycle Management (MLOps Integration)

10. **Continuous Evaluation**
    - Run evals on every model deployment
    - Track metrics across model versions
    - Set quality gates for production
    - Alert on metric degradation
    - Reference: MLOps mo-04 (Monitoring)

11. **Evaluation Metrics Versioning**
    - Version evaluation code and metrics
    - Track metric definition changes
    - Ensure reproducibility of results
    - Maintain historical comparisons
    - Reference: MLOps mo-01 (Model Registry), mo-03 (Versioning)

12. **Performance Regression Detection**
    - Compare new models against baselines
    - Statistical significance testing
    - Automated rollback on regression
    - Track performance trends over time
    - Reference: MLOps mo-05 (Drift Detection)

### Deployment & Operations (DevOps Integration)

13. **Automated Testing in CI/CD**
    - Run evaluations in deployment pipeline
    - Fail deployments on quality regression
    - Parallel evaluation execution
    - Generate evaluation reports automatically
    - Reference: DevOps do-01 (CI/CD), do-06 (Testing)

14. **Evaluation Infrastructure**
    - Containerize evaluation workloads
    - Distributed evaluation for speed
    - Auto-scaling for benchmark runs
    - Cost-optimized compute for evals
    - Reference: DevOps do-03 (Containerization)

15. **Observability for Evaluations**
    - Track evaluation job status
    - Monitor evaluation latency and costs
    - Alert on evaluation failures
    - Dashboard for evaluation metrics
    - Reference: DevOps do-08 (Monitoring & Observability)

### Azure-Specific Best Practices

16. **Azure ML for Evaluation**
    - Use Azure ML pipelines for evaluations
    - Track experiments in Azure ML workspace
    - Store evaluation datasets in Azure Storage
    - Visualize results in Azure ML studio
    - Reference: Azure az-04 (AI/ML Services)

17. **Cost-Effective Evaluation Compute**
    - Use spot instances for batch evaluations
    - Right-size VM instances for workload
    - Implement auto-shutdown after evals
    - Monitor compute costs in Azure Cost Management
    - Reference: Azure az-09 (Cost Management)

##  Cost Optimization Examples

### Tiered Evaluation Strategy
```python
from llm_evaluator import LLMEvaluator, EvaluationTier

class CostOptimizedEvaluator:
    def __init__(self):
        # Quick smoke test (low cost)
        self.smoke_test = LLMEvaluator(
            metrics=["basic_accuracy"],
            sample_size=50,
            cost_per_run=0.10
        )

        # Standard evaluation (medium cost)
        self.standard_eval = LLMEvaluator(
            metrics=["accuracy", "coherence", "relevance"],
            sample_size=200,
            cost_per_run=1.50
        )

        # Comprehensive evaluation (high cost)
        self.comprehensive_eval = LLMEvaluator(
            metrics=[
                "accuracy", "coherence", "relevance",
                "factuality", "safety", "bias"
            ],
            sample_size=1000,
            cost_per_run=15.00
        )

    def evaluate_with_budget(self, model: str, change_type: str):
        """Select evaluation tier based on change type."""

        if change_type == "minor_update":
            # Quick smoke test for minor changes
            return self.smoke_test.evaluate(model)

        elif change_type == "prompt_change":
            # Standard eval for prompt/config changes
            return self.standard_eval.evaluate(model)

        elif change_type == "model_upgrade":
            # Comprehensive eval for major changes
            return self.comprehensive_eval.evaluate(model)

# Usage
evaluator = CostOptimizedEvaluator()

# Minor update: $0.10
smoke_results = evaluator.evaluate_with_budget(
    model="claude-3-5-sonnet-20241022",
    change_type="minor_update"
)

# Major update: $15.00 (but only when needed)
full_results = evaluator.evaluate_with_budget(
    model="claude-opus-4-5-20251101",
    change_type="model_upgrade"
)
```

### Statistical Sampling for Cost Reduction
```python
import numpy as np
from scipy import stats

class SamplingEvaluator:
    def __init__(self, full_dataset_size: int = 10000):
        self.full_dataset = self.load_full_dataset()
        self.full_dataset_size = full_dataset_size

    def calculate_sample_size(
        self,
        confidence_level: float = 0.95,
        margin_of_error: float = 0.02
    ) -> int:
        """Calculate minimum sample size for statistical validity."""
        # For proportion estimation
        z_score = stats.norm.ppf((1 + confidence_level) / 2)
        p = 0.5  # Conservative estimate (maximum variance)

        n = (z_score ** 2 * p * (1 - p)) / (margin_of_error ** 2)

        # Finite population correction
        n_adjusted = n / (1 + ((n - 1) / self.full_dataset_size))

        return int(np.ceil(n_adjusted))

    def evaluate_with_sampling(self, model: str, confidence: float = 0.95):
        """Evaluate with statistically valid sampling."""
        # Calculate required sample size
        sample_size = self.calculate_sample_size(
            confidence_level=confidence,
            margin_of_error=0.02  # ±2% margin of error
        )

        print(f"Sample size: {sample_size} (vs {self.full_dataset_size} full)")

        # Stratified sampling for better representation
        sample = self.stratified_sample(self.full_dataset, sample_size)

        # Evaluate on sample
        results = self.evaluate(model, sample)

        # Calculate confidence intervals
        ci_lower, ci_upper = self.calculate_confidence_interval(
            results.accuracy,
            sample_size,
            confidence
        )

        return {
            "accuracy": results.accuracy,
            "confidence_interval": (ci_lower, ci_upper),
            "sample_size": sample_size,
            "cost_saved": self.calculate_cost_savings(sample_size)
        }

    def calculate_cost_savings(self, sample_size: int) -> float:
        """Calculate cost savings from sampling."""
        full_cost = self.full_dataset_size * 0.002  # $0.002 per evaluation
        sample_cost = sample_size * 0.002

        savings = full_cost - sample_cost
        savings_pct = (savings / full_cost) * 100

        print(f"Cost savings: ${savings:.2f} ({savings_pct:.1f}%)")

        return savings

# Usage
evaluator = SamplingEvaluator(full_dataset_size=10000)

# Evaluate with 95% confidence, ±2% margin of error
# Sample size: ~2400 (vs 10000 full)
# Cost: $4.80 (vs $20.00 full) → 76% savings
results = evaluator.evaluate_with_sampling(
    model="claude-3-5-sonnet-20241022",
    confidence=0.95
)

print(f"Accuracy: {results['accuracy']:.3f} "
      f"±{(results['confidence_interval'][1] - results['accuracy']):.3f}")
```

### Cached Evaluation Results
```python
from eval_cache import EvaluationCache
import hashlib

class CachedEvaluator:
    def __init__(self):
        self.evaluator = LLMEvaluator()
        self.cache = EvaluationCache(ttl_days=30)

    def evaluate(self, model: str, test_data: dict, metrics: List[str]):
        """Evaluate with result caching."""
        # Generate cache key from model, data, and metrics
        cache_key = self._generate_cache_key(model, test_data, metrics)

        # Check cache
        cached_result = self.cache.get(cache_key)
        if cached_result:
            print(" Cache hit - evaluation cost saved!")
            return cached_result

        # Run evaluation
        print(" Cache miss - running evaluation...")
        result = self.evaluator.evaluate(
            model=model,
            test_data=test_data,
            metrics=metrics
        )

        # Cache the result
        self.cache.set(cache_key, result)

        return result

    def _generate_cache_key(
        self,
        model: str,
        test_data: dict,
        metrics: List[str]
    ) -> str:
        """Generate unique cache key."""
        # Hash test data to detect changes
        data_hash = hashlib.md5(
            str(test_data).encode()
        ).hexdigest()

        # Combine all components
        key_components = f"{model}:{data_hash}:{','.join(sorted(metrics))}"

        return hashlib.md5(key_components.encode()).hexdigest()

# Usage
evaluator = CachedEvaluator()

# First run: Cache miss, costs $5.00
results1 = evaluator.evaluate(
    model="claude-3-5-sonnet-20241022",
    test_data=test_dataset,
    metrics=["accuracy", "coherence"]
)

# Second run: Cache hit, costs $0.00
results2 = evaluator.evaluate(
    model="claude-3-5-sonnet-20241022",
    test_data=test_dataset,
    metrics=["accuracy", "coherence"]
)

# After prompt change: Run only new metrics, reuse cached ones
results3 = evaluator.evaluate(
    model="claude-3-5-sonnet-20241022",
    test_data=test_dataset,
    metrics=["accuracy", "coherence", "safety"]  # +safety (new)
)
# Cost: Only safety metric evaluation ($1.50 vs $5.00)
```

##  Security Best Practices Examples

### Adversarial Testing Suite
```python
from adversarial_tester import AdversarialTester

class SecurityEvaluator:
    def __init__(self):
        self.adversarial_tester = AdversarialTester()

    def evaluate_security(self, model: str):
        """Comprehensive security evaluation."""
        results = {}

        # 1. Prompt injection testing
        injection_tests = self.adversarial_tester.test_prompt_injection(
            model=model,
            attack_patterns=[
                "ignore_previous",
                "role_switch",
                "payload_splitting",
                "virtualization"
            ]
        )
        results["prompt_injection_resistance"] = injection_tests.block_rate

        # 2. Jailbreaking attempts
        jailbreak_tests = self.adversarial_tester.test_jailbreaking(
            model=model,
            techniques=[
                "do_anything_now",
                "character_roleplay",
                "hypothetical_scenario"
            ]
        )
        results["jailbreak_resistance"] = jailbreak_tests.block_rate

        # 3. PII leakage testing
        pii_tests = self.adversarial_tester.test_pii_leakage(
            model=model,
            pii_types=["ssn", "credit_card", "medical_record"]
        )
        results["pii_protection"] = 1 - pii_tests.leakage_rate

        # 4. Toxic content generation
        toxicity_tests = self.adversarial_tester.test_toxic_generation(
            model=model,
            categories=["hate", "violence", "sexual", "harassment"]
        )
        results["safety_filter_effectiveness"] = toxicity_tests.block_rate

        return results

# Usage
security_eval = SecurityEvaluator()

security_scores = security_eval.evaluate_security(
    model="claude-3-5-sonnet-20241022"
)

print("\n Security Evaluation Results:")
for metric, score in security_scores.items():
    status = " PASS" if score > 0.95 else " REVIEW"
    print(f"  {metric}: {score:.2%} {status}")

# Fail deployment if security scores are too low
if security_scores["prompt_injection_resistance"] < 0.90:
    raise SecurityError("Insufficient prompt injection protection")
```

### Safety Benchmark Suite
```python
from safety_evaluator import SafetyEvaluator

class ComprehensiveSafetyEval:
    def __init__(self):
        self.safety_eval = SafetyEvaluator()

    def run_safety_benchmarks(self, model: str):
        """Run comprehensive safety evaluation."""
        results = {}

        # 1. Bias evaluation across demographics
        bias_results = self.safety_eval.evaluate_bias(
            model=model,
            dimensions=[
                "gender",
                "race",
                "religion",
                "age",
                "nationality"
            ],
            test_scenarios=1000
        )
        results["bias_scores"] = bias_results

        # 2. Toxicity evaluation
        toxicity_results = self.safety_eval.evaluate_toxicity(
            model=model,
            categories=[
                "severe_toxicity",
                "obscene",
                "threat",
                "insult"
            ]
        )
        results["toxicity_scores"] = toxicity_results

        # 3. Truthfulness evaluation
        truthfulness_results = self.safety_eval.evaluate_truthfulness(
            model=model,
            benchmark="truthfulqa",
            categories=["health", "finance", "law"]
        )
        results["truthfulness_score"] = truthfulness_results.accuracy

        # 4. Compliance testing
        compliance_results = self.safety_eval.evaluate_compliance(
            model=model,
            standards=["hipaa", "gdpr", "financial_advice"]
        )
        results["compliance_scores"] = compliance_results

        return results

    def generate_safety_report(self, results: dict):
        """Generate comprehensive safety report."""
        report = "# Safety Evaluation Report\n\n"

        # Bias scores
        report += "## Bias Evaluation\n"
        for dimension, score in results["bias_scores"].items():
            report += f"- {dimension}: {score:.3f}\n"

        # Toxicity scores
        report += "\n## Toxicity Evaluation\n"
        for category, score in results["toxicity_scores"].items():
            report += f"- {category}: {score:.3f}\n"

        # Truthfulness
        report += f"\n## Truthfulness\n"
        report += f"- Score: {results['truthfulness_score']:.3f}\n"

        # Compliance
        report += "\n## Compliance\n"
        for standard, passed in results["compliance_scores"].items():
            status = " PASS" if passed else " FAIL"
            report += f"- {standard}: {status}\n"

        return report

# Usage
safety_eval = ComprehensiveSafetyEval()

results = safety_eval.run_safety_benchmarks(
    model="claude-3-5-sonnet-20241022"
)

report = safety_eval.generate_safety_report(results)
print(report)

# Save report for compliance
with open("safety_evaluation_report.md", "w") as f:
    f.write(report)
```

##  Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Task Performance** | Accuracy | >0.90 | Custom evaluator |
| | F1 Score | >0.85 | scikit-learn |
| | BLEU score (generation) | >0.40 | nltk |
| | ROUGE-L (summarization) | >0.45 | rouge-score |
| **Benchmark Scores** | MMLU (reasoning) | >80% | Benchmark runner |
| | HellaSwag (common sense) | >85% | Benchmark runner |
| | TruthfulQA (truthfulness) | >75% | Benchmark runner |
| **Quality Metrics** | Coherence score | >0.85 | Custom evaluator |
| | Relevance score | >0.90 | Custom evaluator |
| | Hallucination rate | <5% | Factuality checker |
| **Safety & Bias** | Toxicity score | <0.02 | Perspective API |
| | Bias score (demographics) | <0.10 | Fairness evaluator |
| | Safety filter pass rate | >0.98 | Safety evaluator |
| **Costs** | Evaluation cost per model | <$50 | Cost tracker |
| | Cost per test sample | <$0.05 | Cost analyzer |
| | Cache hit rate | >50% | Eval cache |
| **Performance** | Evaluation runtime (1K samples) | <30min | Time tracker |
| | Throughput (samples/sec) | >5 | Benchmark runner |

##  Deployment Pipeline

### CI/CD with Automated Evaluation
```yaml
# .github/workflows/llm-evaluation-pipeline.yml
name: LLM Evaluation Pipeline

on:
  pull_request:
    paths:
      - 'models/**'
      - 'prompts/**'
  push:
    branches:
      - main

jobs:
  smoke-test:
    runs-on: ubuntu-latest
    steps:
      - name: Quick smoke test (50 samples)
        run: python scripts/run_smoke_test.py --samples 50

      - name: Check basic accuracy
        run: |
          python scripts/check_accuracy.py --min-threshold 0.80

  standard-evaluation:
    needs: smoke-test
    runs-on: ubuntu-latest
    steps:
      - name: Run standard evaluation (200 samples)
        run: |
          python scripts/run_evaluation.py \
            --metrics accuracy,coherence,relevance \
            --samples 200

      - name: Check for regression
        run: |
          python scripts/check_regression.py \
            --baseline-version v1.0 \
            --max-degradation 0.05

      - name: Generate evaluation report
        run: python scripts/generate_eval_report.py

      - name: Upload results to MLflow
        run: python scripts/upload_to_mlflow.py

  comprehensive-evaluation:
    needs: standard-evaluation
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Run comprehensive evaluation (1000 samples)
        run: |
          python scripts/run_comprehensive_eval.py \
            --metrics all \
            --samples 1000

      - name: Run benchmark suite
        run: python scripts/run_benchmarks.py --benchmarks mmlu,hellaswag,truthfulqa

      - name: Security evaluation
        run: python scripts/run_security_eval.py

      - name: Generate final report
        run: python scripts/generate_final_report.py

      - name: Quality gate check
        run: |
          python scripts/quality_gate.py \
            --min-accuracy 0.90 \
            --max-toxicity 0.02 \
            --min-safety 0.98

  deploy-if-passing:
    needs: comprehensive-evaluation
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy to production
        if: success()
        run: python scripts/deploy_model.py --environment production

      - name: Monitor post-deployment
        run: python scripts/monitor_production.py --duration 2h
```

##  Integration Workflow

### End-to-End Evaluation Pipeline with All Roles
```
1. Code/Model Change Committed
   ↓
2. Trigger CI/CD Pipeline (do-01)
   ↓
3. Load Test Dataset (de-01)
   ↓
4. Validate Test Data Quality (de-03)
   ↓
5. Run Smoke Test (50 samples) (ai-06)
   ↓
6. Basic Regression Check (mo-05)
   ↓
7. Standard Evaluation (200 samples) (ai-06)
   ↓
8. Cost Tracking (fo-01)
   ↓
9. Security Evaluation (sa-08)
   ↓
10. Bias & Safety Testing (ds-01)
    ↓
11. Statistical Significance Test (ds-08)
    ↓
12. Quality Gate Check (mo-04)
    ↓
13. Comprehensive Evaluation (if passing) (ai-06)
    ↓
14. Benchmark Suite Execution (ai-06)
    ↓
15. Generate Evaluation Report (ai-06)
    ↓
16. Upload Metrics to MLflow (mo-01)
    ↓
17. Final Quality Gate (mo-04)
    ↓
18. Deploy if All Checks Pass (do-01)
    ↓
19. Post-Deployment Monitoring (mo-04)
    ↓
20. Continuous Evaluation in Production (mo-04)
```

##  Quick Wins

1. **Implement smoke tests** - Catch major regressions quickly with 50-sample tests
2. **Use statistical sampling** - 75% cost reduction with valid confidence intervals
3. **Cache evaluation results** - Reuse evaluations across multiple metrics
4. **Set up automated regression testing** - Block deployments on quality degradation
5. **Run tiered evaluations** - Quick tests for minor changes, comprehensive for major
6. **Add security evaluation** - Test against adversarial attacks before production
7. **Track evaluation costs** - Monitor and optimize evaluation budget
8. **Use distributed evaluation** - Parallelize for 10x faster benchmark execution
