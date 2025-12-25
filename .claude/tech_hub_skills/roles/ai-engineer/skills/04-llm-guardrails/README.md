# Skill 4: LLM Guardrails & Safety

## 🎯 Overview
Implement comprehensive safety mechanisms for LLM applications including content filtering, bias detection, hallucination prevention, and compliance controls for production deployments.

## 🔗 Connections
- **Data Engineer**: Training data filtering, safety metrics storage (de-01, de-03)
- **Security Architect**: PII detection, prompt injection prevention (sa-01, sa-08)
- **ML Engineer**: Safety model fine-tuning and deployment (ml-03, ml-04)
- **MLOps**: Safety metrics monitoring, guardrail versioning (mo-01, mo-04)
- **FinOps**: Guardrail execution cost optimization (fo-01, fo-07)
- **DevOps**: Guardrail service deployment, failover mechanisms (do-01, do-03)
- **Data Scientist**: Bias analysis, safety model evaluation (ds-01, ds-08)

## 🛠️ Tools Included

### 1. `content_filter.py`
Multi-layer content filtering for harmful, toxic, and inappropriate outputs with custom policies.

### 2. `hallucination_detector.py`
Fact-checking and source verification system to detect and prevent hallucinations.

### 3. `bias_detector.py`
Identify and mitigate demographic, gender, and cultural biases in model outputs.

### 4. `prompt_injection_guard.py`
Defense against prompt injection, jailbreaking, and adversarial attacks.

### 5. `compliance_checker.py`
Industry-specific compliance validation (HIPAA, GDPR, financial regulations).

## 📊 Key Metrics
- Content filter accuracy (precision/recall)
- Hallucination detection rate
- Bias score across demographics
- Prompt injection block rate
- Compliance violation prevention rate

## 🚀 Quick Start

```python
from llm_guardrails import GuardrailPipeline
from anthropic import Anthropic

# Initialize guardrails
guardrails = GuardrailPipeline(
    filters=["toxicity", "pii", "bias", "hallucination"],
    compliance_standards=["gdpr", "hipaa"],
    strictness_level="high"
)

client = Anthropic()

# Wrap LLM calls with guardrails
def safe_llm_call(prompt: str, user_context: dict = None):
    # Pre-processing guardrails
    validated_prompt = guardrails.validate_input(
        prompt=prompt,
        user_context=user_context
    )

    if not validated_prompt.safe:
        return {
            "blocked": True,
            "reason": validated_prompt.violation_reason,
            "severity": validated_prompt.severity
        }

    # Make LLM call
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": validated_prompt.sanitized_prompt}]
    )

    # Post-processing guardrails
    validated_output = guardrails.validate_output(
        output=response.content[0].text,
        prompt=prompt,
        context=user_context
    )

    if not validated_output.safe:
        return {
            "blocked": True,
            "reason": validated_output.violation_reason,
            "alternative": validated_output.safe_alternative
        }

    return {
        "blocked": False,
        "response": validated_output.sanitized_output,
        "safety_score": validated_output.safety_score
    }

# Use with safety guarantees
result = safe_llm_call("Explain the treatment protocol for diabetes")
print(result["response"])
```

## 📚 Best Practices

### Cost Optimization (FinOps Integration)

1. **Optimize Guardrail Execution Order**
   - Run cheap filters first (regex, keyword matching)
   - Use ML-based filters only when needed
   - Implement early termination for obvious violations
   - Cache guardrail results for similar inputs
   - Reference: FinOps fo-07 (AI/ML Cost Optimization)

2. **Batch Guardrail Processing**
   - Process multiple inputs in batches
   - Amortize model loading costs
   - Use batch APIs for classification models
   - Implement async processing for non-blocking checks
   - Reference: FinOps fo-03 (Budget Management)

3. **Tiered Guardrail Strategies**
   - Light filtering for low-risk applications
   - Comprehensive checks for high-risk domains
   - Dynamic filtering based on user trust scores
   - Cost-aware filter selection
   - Reference: FinOps fo-01 (Cost Monitoring)

4. **Cache Guardrail Results**
   - Cache validation results with semantic similarity
   - Reuse PII detection results
   - Cache compliance check outcomes
   - Monitor cache hit rates for optimization
   - Reference: ai-01 (Prompt Caching)

### Security & Privacy (Security Architect Integration)

5. **PII Detection & Redaction**
   - Scan all inputs and outputs for PII
   - Redact or mask sensitive information
   - Maintain audit trail of PII handling
   - Comply with data protection regulations
   - Reference: Security Architect sa-01 (PII Detection)

6. **Prompt Injection Prevention**
   - Detect and block prompt injection attempts
   - Implement input sanitization
   - Use structured prompts with clear boundaries
   - Monitor for jailbreaking patterns
   - Reference: Security Architect sa-08 (LLM Security)

7. **Access Control & Audit Logging**
   - Log all guardrail violations
   - Implement RBAC for guardrail configuration
   - Track user-level safety metrics
   - Alert on suspicious patterns
   - Reference: Security Architect sa-02 (IAM), sa-06 (Data Governance)

### Data Quality & Governance (Data Engineer Integration)

8. **Training Data Filtering**
   - Apply guardrails to training datasets
   - Remove toxic and biased examples
   - Validate data quality before fine-tuning
   - Track data lineage for safety-critical data
   - Reference: Data Engineer de-03 (Data Quality)

9. **Safety Metrics Storage**
   - Persist guardrail execution results
   - Store violation patterns for analysis
   - Track safety metrics over time
   - Enable historical safety audits
   - Reference: Data Engineer de-01 (Data Ingestion)

### Model Lifecycle Management (MLOps Integration)

10. **Guardrail Model Versioning**
    - Version all safety models in registry
    - Track guardrail model performance
    - A/B test new guardrail versions
    - Rollback capability for safety regressions
    - Reference: MLOps mo-01 (Model Registry), mo-03 (Versioning)

11. **Safety Metrics Monitoring**
    - Track false positive/negative rates
    - Monitor guardrail execution latency
    - Alert on guardrail failures or bypasses
    - Dashboard for real-time safety metrics
    - Reference: MLOps mo-04 (Monitoring)

12. **Guardrail Drift Detection**
    - Monitor changes in violation patterns
    - Detect emerging attack vectors
    - Track effectiveness degradation
    - Retrain safety models as needed
    - Reference: MLOps mo-05 (Drift Detection)

### Deployment & Operations (DevOps Integration)

13. **Deploy Guardrails as Microservices**
    - Separate service for each guardrail type
    - Independent scaling based on load
    - Circuit breakers for guardrail failures
    - Health checks and monitoring
    - Reference: DevOps do-03 (Containerization)

14. **CI/CD for Guardrail Updates**
    - Automated testing for guardrail changes
    - Canary deployments for new filters
    - Rollback on increased false positives
    - Continuous safety benchmarking
    - Reference: DevOps do-01 (CI/CD)

15. **High Availability for Safety Systems**
    - Multi-region guardrail deployment
    - Fallback to conservative filtering on failures
    - Load balancing across guardrail instances
    - Zero-downtime updates
    - Reference: DevOps do-04 (High Availability)

### Azure-Specific Best Practices

16. **Azure AI Content Safety**
    - Integrate Azure Content Safety API
    - Use managed safety models
    - Enable custom categories for domain-specific filtering
    - Monitor via Azure Monitor
    - Reference: Azure az-04 (AI/ML Services)

17. **Azure OpenAI Safety Features**
    - Enable content filtering in Azure OpenAI
    - Use content filtering configurations
    - Implement custom blocklists
    - Monitor safety events in Application Insights
    - Reference: Azure az-05 (Azure OpenAI)

## 💰 Cost Optimization Examples

### Tiered Guardrail Strategy
```python
from llm_guardrails import GuardrailPipeline, FilterLevel

class CostOptimizedGuardrails:
    def __init__(self):
        # Define tiered filtering strategies
        self.light_filters = GuardrailPipeline(
            filters=["regex_profanity", "keyword_blocklist"],
            level=FilterLevel.LIGHT
        )

        self.standard_filters = GuardrailPipeline(
            filters=["toxicity_classifier", "pii_detection"],
            level=FilterLevel.STANDARD
        )

        self.comprehensive_filters = GuardrailPipeline(
            filters=[
                "toxicity_classifier",
                "pii_detection",
                "bias_detector",
                "hallucination_checker",
                "compliance_validator"
            ],
            level=FilterLevel.COMPREHENSIVE
        )

    def select_filters(self, user_trust_score: float, content_risk: str):
        """Select appropriate filter level based on context."""
        if user_trust_score > 0.9 and content_risk == "low":
            return self.light_filters  # $0.0001 per request

        elif user_trust_score > 0.7 and content_risk in ["low", "medium"]:
            return self.standard_filters  # $0.001 per request

        else:
            return self.comprehensive_filters  # $0.005 per request

    def validate(self, prompt: str, user_context: dict):
        filters = self.select_filters(
            user_trust_score=user_context.get("trust_score", 0.5),
            content_risk=user_context.get("risk_level", "high")
        )

        return filters.validate_input(prompt)

# Usage
guardrails = CostOptimizedGuardrails()

# Low-risk user, low-risk content → cheap filtering
result = guardrails.validate(
    prompt="What's the weather today?",
    user_context={"trust_score": 0.95, "risk_level": "low"}
)

# High-risk content → comprehensive filtering
result = guardrails.validate(
    prompt="Provide medical advice for my condition",
    user_context={"trust_score": 0.5, "risk_level": "high"}
)
```

### Cached Guardrail Results
```python
from functools import lru_cache
import hashlib
from semantic_cache import SemanticCache

class CachedGuardrailPipeline:
    def __init__(self):
        self.guardrails = GuardrailPipeline()
        self.semantic_cache = SemanticCache(
            similarity_threshold=0.95,
            ttl_seconds=3600
        )

    def validate_input(self, prompt: str, user_context: dict = None):
        # Check semantic cache for similar prompts
        cached_result = self.semantic_cache.get(prompt)
        if cached_result:
            print("✅ Cache hit - guardrail cost saved!")
            return cached_result

        # Run guardrails
        result = self.guardrails.validate_input(prompt, user_context)

        # Cache the result
        if result.safe:  # Only cache safe results
            self.semantic_cache.set(prompt, result)

        return result

# Track cost savings
guardrails = CachedGuardrailPipeline()

# Generate cost report
savings_report = guardrails.semantic_cache.get_savings_report()
print(f"Cache hit rate: {savings_report.hit_rate:.2%}")
print(f"Requests saved: {savings_report.hits}")
print(f"Cost savings: ${savings_report.cost_saved:.4f}")
```

### Batch Processing for Guardrails
```python
from llm_guardrails import BatchGuardrailPipeline

class BatchGuardrails:
    def __init__(self):
        self.pipeline = BatchGuardrailPipeline(
            batch_size=32,  # Process 32 items at once
            max_wait_ms=100  # Wait up to 100ms to fill batch
        )

    async def validate_async(self, prompts: List[str]):
        """Validate multiple prompts efficiently."""
        # Batch processing reduces per-item cost by 70%
        results = await self.pipeline.validate_batch(prompts)

        return [
            {
                "prompt": prompt,
                "safe": result.safe,
                "violations": result.violations
            }
            for prompt, result in zip(prompts, results)
        ]

# Usage for high-throughput applications
guardrails = BatchGuardrails()

# Validate 100 prompts in batches of 32
prompts = [f"User query {i}" for i in range(100)]
results = await guardrails.validate_async(prompts)

# Cost comparison:
# Individual processing: 100 requests × $0.001 = $0.10
# Batch processing: 4 batches × $0.008 = $0.032 (68% savings)
```

## 🔒 Security Best Practices Examples

### Comprehensive PII Detection
```python
from pii_detector import PIIDetector  # from sa-01
from data_anonymizer import DataAnonymizer

class PIIGuardrail:
    def __init__(self):
        self.detector = PIIDetector()
        self.anonymizer = DataAnonymizer()

    def validate_and_sanitize(self, text: str, mode: str = "redact"):
        """Detect and handle PII in text."""
        # Detect PII
        findings = self.detector.analyze_text(text)

        if not findings:
            return {
                "safe": True,
                "sanitized_text": text,
                "pii_found": False
            }

        # Handle based on mode
        if mode == "redact":
            sanitized = self.anonymizer.redact_pii(text, findings)
        elif mode == "mask":
            sanitized = self.anonymizer.mask_pii(text, findings)
        elif mode == "block":
            return {
                "safe": False,
                "reason": "PII detected - request blocked",
                "pii_types": [f.entity_type for f in findings]
            }

        # Log for compliance
        self._log_pii_handling({
            "pii_types": [f.entity_type for f in findings],
            "action": mode,
            "timestamp": datetime.now()
        })

        return {
            "safe": True,
            "sanitized_text": sanitized,
            "pii_found": True,
            "pii_types": [f.entity_type for f in findings]
        }

# Integration with LLM pipeline
pii_guard = PIIGuardrail()

def safe_llm_call_with_pii_protection(prompt: str):
    # Check input
    input_result = pii_guard.validate_and_sanitize(prompt, mode="redact")

    if not input_result["safe"]:
        return {"blocked": True, "reason": input_result["reason"]}

    # Make LLM call with sanitized prompt
    response = llm_call(input_result["sanitized_text"])

    # Check output
    output_result = pii_guard.validate_and_sanitize(response, mode="mask")

    return {
        "response": output_result["sanitized_text"],
        "pii_found": input_result["pii_found"] or output_result["pii_found"]
    }
```

### Prompt Injection Defense
```python
from prompt_injection_detector import PromptInjectionDetector  # from sa-08

class PromptInjectionGuardrail:
    def __init__(self):
        self.detector = PromptInjectionDetector()
        self.attack_patterns = [
            r"ignore previous instructions",
            r"disregard all prior",
            r"new instructions:",
            r"system:",
            r"<\|im_start\|>",
            # Add more patterns
        ]

    def validate(self, prompt: str):
        """Detect prompt injection attempts."""
        # Rule-based detection (fast)
        for pattern in self.attack_patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                return {
                    "safe": False,
                    "threat": "prompt_injection",
                    "confidence": 0.95,
                    "pattern_matched": pattern
                }

        # ML-based detection (comprehensive)
        ml_result = self.detector.analyze(prompt)

        if ml_result.injection_score > 0.7:
            return {
                "safe": False,
                "threat": "prompt_injection",
                "confidence": ml_result.injection_score,
                "attack_type": ml_result.attack_type
            }

        return {"safe": True, "confidence": 1 - ml_result.injection_score}

    def sanitize(self, prompt: str):
        """Sanitize potentially malicious prompts."""
        # Remove special tokens
        sanitized = re.sub(r'<\|.*?\|>', '', prompt)

        # Escape problematic characters
        sanitized = sanitized.replace('\\n\\n', ' ')

        # Enforce length limits
        if len(sanitized) > 2000:
            sanitized = sanitized[:2000]

        return sanitized

# Usage
injection_guard = PromptInjectionGuardrail()

def protected_llm_call(user_prompt: str):
    # Validate input
    validation = injection_guard.validate(user_prompt)

    if not validation["safe"]:
        # Log attack attempt
        security_logger.warning(
            f"Prompt injection blocked: {validation['attack_type']} "
            f"(confidence: {validation['confidence']:.2%})"
        )
        return {"blocked": True, "reason": "Security violation detected"}

    # Sanitize and proceed
    safe_prompt = injection_guard.sanitize(user_prompt)
    return llm_call(safe_prompt)
```

### Hallucination Detection
```python
from hallucination_detector import HallucinationDetector

class HallucinationGuardrail:
    def __init__(self):
        self.detector = HallucinationDetector()

    def validate_output(self, output: str, context: dict, sources: List[str]):
        """Check if LLM output is grounded in provided sources."""
        # Extract claims from output
        claims = self.detector.extract_claims(output)

        unverified_claims = []
        for claim in claims:
            # Check if claim is supported by sources
            verification = self.detector.verify_claim(
                claim=claim,
                sources=sources,
                context=context
            )

            if not verification.supported:
                unverified_claims.append({
                    "claim": claim,
                    "confidence": verification.confidence,
                    "reason": verification.reason
                })

        # Calculate hallucination score
        hallucination_score = len(unverified_claims) / len(claims) if claims else 0

        if hallucination_score > 0.3:  # More than 30% unverified
            return {
                "safe": False,
                "reason": "High hallucination risk",
                "score": hallucination_score,
                "unverified_claims": unverified_claims
            }

        return {
            "safe": True,
            "score": hallucination_score,
            "verified_claims": len(claims) - len(unverified_claims)
        }

# Integration with RAG pipeline
hallucination_guard = HallucinationGuardrail()

def rag_with_hallucination_check(query: str):
    # Retrieve context
    sources = rag_pipeline.retrieve(query, top_k=5)

    # Generate response
    response = llm_generate(query, sources)

    # Validate response
    validation = hallucination_guard.validate_output(
        output=response,
        context={"query": query},
        sources=sources
    )

    if not validation["safe"]:
        # Return conservative response or request more sources
        return {
            "response": "I don't have enough reliable information to answer this.",
            "reason": validation["reason"]
        }

    return {"response": response, "safety_score": 1 - validation["score"]}
```

## 📊 Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Content Safety** | Toxic content block rate | 100% | Azure Content Safety |
| | False positive rate | <2% | Custom evaluator |
| | Filter accuracy | >0.98 | MLflow |
| | Response time (p95) | <200ms | Azure Monitor |
| **PII Protection** | PII detection recall | >0.99 | Custom evaluator |
| | PII detection precision | >0.95 | Custom evaluator |
| | Redaction accuracy | >0.98 | Audit logs |
| **Prompt Injection** | Injection detection rate | >0.95 | Security monitor |
| | False positive rate | <5% | Security logs |
| | Attack pattern coverage | >90% | Security audit |
| **Hallucination** | Hallucination detection rate | >0.85 | Custom evaluator |
| | Fact-check accuracy | >0.90 | MLflow |
| | Source grounding score | >0.85 | Custom metric |
| **Costs** | Cost per guardrail check | <$0.002 | FinOps dashboard |
| | Cache hit rate | >60% | App Insights |
| **Compliance** | GDPR compliance rate | 100% | Compliance tracker |
| | HIPAA violation prevention | 100% | Audit logs |

## 🚀 Deployment Pipeline

### CI/CD for Guardrail System
```yaml
# .github/workflows/guardrails-deployment.yml
name: Guardrails Deployment

on:
  push:
    paths:
      - 'guardrails/**'
    branches:
      - main

jobs:
  test-guardrails:
    runs-on: ubuntu-latest
    steps:
      - name: Unit test all guardrails
        run: pytest tests/test_guardrails.py -v

      - name: Test PII detection accuracy
        run: pytest tests/test_pii_detection.py --min-recall 0.99

      - name: Test prompt injection detection
        run: pytest tests/test_injection_detection.py --min-accuracy 0.95

      - name: Benchmark guardrail performance
        run: python scripts/benchmark_guardrails.py

      - name: Test false positive rates
        run: pytest tests/test_false_positives.py --max-fp-rate 0.02

  security-validation:
    runs-on: ubuntu-latest
    steps:
      - name: Validate security policies
        run: python scripts/validate_security_policies.py

      - name: Test adversarial examples
        run: pytest tests/test_adversarial.py

      - name: Compliance check
        run: python scripts/check_compliance.py --standards gdpr,hipaa

  deploy-guardrails:
    needs: [test-guardrails, security-validation]
    runs-on: ubuntu-latest
    steps:
      - name: Build guardrail service
        run: docker build -t guardrails-service:${{ github.sha }} .

      - name: Push to Azure Container Registry
        run: |
          az acr login --name myregistry
          docker push myregistry.azurecr.io/guardrails-service:${{ github.sha }}

      - name: Deploy to AKS
        run: |
          kubectl set image deployment/guardrails-service \
            guardrails=myregistry.azurecr.io/guardrails-service:${{ github.sha }}

      - name: Run smoke tests
        run: python scripts/smoke_test_guardrails.py

      - name: Monitor guardrail metrics
        run: python scripts/monitor_guardrails.py --duration 1h --alert-on-regression
```

## 🔄 Integration Workflow

### End-to-End Guardrail Pipeline with All Roles
```
1. User Input Received
   ↓
2. Input Length & Format Validation
   ↓
3. Prompt Injection Detection (sa-08)
   ↓
4. PII Detection in Input (sa-01)
   ↓
5. Input Sanitization
   ↓
6. Cost-Optimized Filter Selection (fo-07)
   ↓
7. LLM Processing with Caching (ai-01)
   ↓
8. Output Content Safety Check (sa-08)
   ↓
9. Hallucination Detection (ai-04)
   ↓
10. Bias Detection (ds-01)
    ↓
11. PII Detection in Output (sa-01)
    ↓
12. Compliance Validation (sa-06)
    ↓
13. Output Sanitization
    ↓
14. Safety Metrics Logging (mo-04)
    ↓
15. Cost Attribution (fo-01)
    ↓
16. Guardrail Performance Monitoring (mo-04)
    ↓
17. Safe Response Delivery
```

## 🎯 Quick Wins

1. **Enable Azure Content Safety** - Instant toxic content filtering with managed service
2. **Implement PII detection** - Prevent data leakage and compliance violations
3. **Add prompt injection defense** - Block jailbreaking and adversarial attacks
4. **Cache guardrail results** - 60%+ cost reduction on repeated checks
5. **Use tiered filtering** - Balance cost and safety based on risk level
6. **Set up safety monitoring** - Real-time alerts on guardrail failures
7. **Implement hallucination detection** - Improve output factuality for RAG systems
8. **Enable compliance validation** - Automated GDPR/HIPAA checks before deployment
