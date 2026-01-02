# Skill 4: Model Serving & API Development

##  Overview
Deploy production-ready ML models with high-performance REST/gRPC APIs, auto-scaling, and comprehensive monitoring.

##  Connections
- **ML Engineer**: Serves trained models from registry (ml-03, ml-07)
- **AI Engineer**: Powers agent systems and LLM applications (ai-03, ai-07)
- **MLOps**: Model deployment and endpoint management (mo-03, mo-04)
- **FinOps**: Optimizes serving costs and resource usage (fo-06, fo-07)
- **DevOps**: Container orchestration and deployment (do-03, do-06, do-08)
- **Security Architect**: Secures API endpoints and authentication (sa-02, sa-03)
- **System Design**: Scalable serving architecture (sd-03, sd-05, sd-06)
- **Data Engineer**: Serves features for inference (de-02, ml-02)

##  Tools Included

### 1. `model_server.py`
FastAPI/Flask production model serving with async support.

### 2. `batch_inference.py`
Efficient batch prediction pipeline for large-scale inference.

### 3. `model_optimizer.py`
Model optimization (ONNX, TensorRT, quantization) for low latency.

### 4. `api_gateway.py`
API gateway with rate limiting, authentication, and monitoring.

### 5. `deployment_config.yaml`
Configuration templates for model deployment infrastructure.

##  Model Serving Architecture

```
API Gateway → Load Balancer → Model Servers → Feature Store
     ↓              ↓               ↓              ↓
  Auth/Rate    Traffic Split   Predictions   Online Features
  Monitoring   A/B Testing     Caching       Low Latency
  Logging      Auto-scale      Batching      Consistency
```

##  Quick Start

```python
from model_server import ModelServer, FastAPIApp
from model_optimizer import ModelOptimizer

# Load and optimize model
optimizer = ModelOptimizer()
model = optimizer.load_model("models/churn_predictor_v2")
optimized_model = optimizer.optimize(
    model,
    target_format="onnx",
    optimization_level=2
)

# Create FastAPI server
app = FastAPIApp(
    model=optimized_model,
    feature_store=feature_store,
    enable_caching=True,
    enable_batching=True
)

# Define prediction endpoint
@app.post("/predict")
async def predict(request: PredictionRequest):
    """Real-time prediction endpoint"""

    # Get online features
    features = await app.get_online_features(
        feature_refs=["customer_behavior:v1"],
        entity_keys={"customer_id": request.customer_id}
    )

    # Predict with caching
    prediction = await app.predict(features)

    return {
        "customer_id": request.customer_id,
        "churn_probability": prediction["probability"],
        "prediction": prediction["class"],
        "model_version": "v2"
    }

# Health check
@app.get("/health")
async def health():
    return {"status": "healthy", "model_loaded": app.model_loaded}

# Run server
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        workers=4,
        reload=False
    )
```

##  Best Practices

### Serving Cost Optimization (FinOps Integration)

1. **Auto-Scaling for Variable Loads**
   - Scale instances based on request rate
   - Set appropriate min/max instances
   - Use horizontal pod autoscaling (HPA)
   - Monitor scaling efficiency
   - Scale to zero during off-hours
   - Reference: FinOps fo-06 (Compute Optimization), fo-07 (AI/ML Cost)

2. **Model Caching for Cost Reduction**
   - Cache predictions for frequent inputs
   - Use Redis for distributed caching
   - Implement cache warming strategies
   - Monitor cache hit rates (target >80%)
   - Reference: FinOps fo-06, System Design sd-05

3. **Request Batching**
   - Batch requests for throughput optimization
   - Reduce per-request overhead
   - Optimize batch size for latency/throughput
   - Use dynamic batching
   - Reference: ML Engineer best practices

4. **Model Optimization**
   - Quantize models (4-8x size reduction)
   - Convert to ONNX for faster inference
   - Use TensorRT for GPU optimization
   - Implement model pruning
   - Reference: ML Engineer ml-08 (Model Compression)

5. **Right-Size Serving Instances**
   - Profile inference workload
   - Choose appropriate instance types
   - Use CPU for most models (cheaper than GPU)
   - Reserve GPUs for large deep learning models
   - Monitor resource utilization
   - Reference: FinOps fo-06

6. **Monitoring Serving Costs**
   - Track cost per prediction
   - Monitor monthly serving costs
   - Alert on cost anomalies
   - Optimize expensive endpoints
   - Reference: FinOps fo-01 (Cost Monitoring), fo-03 (Budget Management)

### DevOps Integration for Serving

7. **Containerized Deployments**
   - Package models in Docker containers
   - Use multi-stage builds to minimize size
   - Implement health checks
   - Version container images
   - Reference: DevOps do-03 (Containerization)

8. **Blue-Green & Canary Deployments**
   - Test new models with small traffic percentage
   - Gradual traffic shifting
   - Automated rollback on errors
   - A/B testing infrastructure
   - Reference: DevOps do-06 (Deployment Strategies)

9. **CI/CD for Model Deployment**
   - Automate model deployment pipelines
   - Run inference tests before deployment
   - Validate model performance in staging
   - Automated promotion to production
   - Reference: DevOps do-01 (CI/CD)

10. **Infrastructure as Code**
    - Define serving infrastructure in Terraform
    - Version control all configurations
    - Automate environment provisioning
    - Implement disaster recovery
    - Reference: DevOps do-04 (IaC)

11. **Comprehensive Monitoring**
    - Monitor prediction latency (p50, p95, p99)
    - Track request rates and throughput
    - Monitor error rates and types
    - Set up alerts for degradation
    - Reference: DevOps do-08 (Monitoring), MLOps mo-04

### Performance Optimization

12. **Low-Latency Inference**
    - Optimize model inference code
    - Use async/await for I/O operations
    - Implement connection pooling
    - Minimize feature retrieval latency
    - Pre-load models at startup
    - Reference: System Design sd-06 (Performance)

13. **Async & Concurrent Processing**
    - Use async frameworks (FastAPI, aiohttp)
    - Implement concurrent request handling
    - Non-blocking I/O for feature fetching
    - Thread pools for CPU-bound inference
    - Reference: System Design sd-03 (Scalability)

14. **Load Balancing**
    - Distribute traffic across instances
    - Use health-based routing
    - Implement sticky sessions if needed
    - Configure timeout policies
    - Reference: System Design sd-05 (Load Balancing)

### Security & Compliance

15. **API Authentication & Authorization**
    - Implement API key authentication
    - Use OAuth 2.0 for user authentication
    - Implement RBAC for endpoints
    - Audit API access logs
    - Reference: Security Architect sa-02 (IAM)

16. **Rate Limiting & Throttling**
    - Prevent API abuse with rate limits
    - Implement per-user quotas
    - Graceful degradation under load
    - DDoS protection
    - Reference: Security Architect sa-03 (Network Security)

17. **Input Validation & Sanitization**
    - Validate all input data
    - Sanitize inputs to prevent injection
    - Implement schema validation
    - Handle malformed requests gracefully
    - Reference: Security Architect sa-08 (LLM Security)

18. **Secure Model Serving**
    - Encrypt model artifacts at rest
    - Use TLS for API endpoints
    - Implement network isolation
    - Audit prediction requests
    - Reference: Security Architect sa-02, sa-03

### MLOps Integration

19. **Model Version Management**
    - Serve multiple model versions simultaneously
    - Gradual migration between versions
    - Track which version served each request
    - Rollback capabilities
    - Reference: MLOps mo-03 (Model Versioning)

20. **Prediction Logging & Monitoring**
    - Log predictions for analysis
    - Monitor prediction distributions
    - Detect model drift in production
    - Track model performance metrics
    - Reference: MLOps mo-04 (Monitoring), mo-05 (Drift Detection)

### Azure-Specific Best Practices

21. **Azure ML Managed Endpoints**
    - Use managed online endpoints
    - Enable auto-scaling
    - Implement multi-model endpoints
    - Use Azure Monitor for observability
    - Reference: Azure az-04 (AI/ML Services)

22. **Azure API Management**
    - Centralize API management
    - Implement rate limiting and quotas
    - Enable caching at API gateway
    - Monitor API usage and costs
    - Reference: Azure az-05 (Application Services)

##  Cost Optimization Examples

### Auto-Scaling Model Deployment
```python
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    ResourceRequests,
    ResourceSettings
)
from finops_tracker import ServingCostTracker

cost_tracker = ServingCostTracker()

# Create endpoint
endpoint = ManagedOnlineEndpoint(
    name="churn-prediction-optimized",
    description="Cost-optimized churn prediction endpoint",
    auth_mode="key",
    tags={
        "cost_center": "ml-platform",
        "environment": "production"
    }
)

ml_client.online_endpoints.begin_create_or_update(endpoint).result()

# Cost-optimized deployment with auto-scaling
deployment = ManagedOnlineDeployment(
    name="churn-v2-optimized",
    endpoint_name=endpoint.name,
    model="azureml:churn_predictor:2",

    # Right-sized instance
    instance_type="Standard_DS2_v2",  # CPU instance (cheaper than GPU)
    instance_count=1,

    # Auto-scaling configuration
    scale_settings={
        "scale_type": "target_utilization",
        "min_instances": 1,  # Scale to 1 during off-hours
        "max_instances": 10,  # Scale up for peak traffic
        "polling_interval": 30,  # Check every 30 seconds
        "target_utilization_percentage": 70,  # Scale at 70% CPU
        "cooldown_period": 300  # 5 min cooldown
    },

    # Resource limits
    request_settings=ResourceSettings(
        request_timeout_ms=5000,  # 5s timeout
        max_concurrent_requests_per_instance=10,
        max_queue_wait_ms=500
    ),

    # Health monitoring
    liveness_probe=ProbeSettings(
        initial_delay=10,
        period=10,
        timeout=2,
        failure_threshold=3
    ),

    readiness_probe=ProbeSettings(
        initial_delay=10,
        period=10,
        timeout=2,
        failure_threshold=3
    ),

    # Environment variables
    environment_variables={
        "ENABLE_CACHING": "true",
        "CACHE_TTL": "3600",
        "ENABLE_BATCHING": "true",
        "MAX_BATCH_SIZE": "32"
    }
)

ml_client.online_deployments.begin_create_or_update(deployment).result()

# Set traffic to new deployment
endpoint.traffic = {"churn-v2-optimized": 100}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()

# Monitor costs
cost_tracker.track_endpoint(
    endpoint_name=endpoint.name,
    deployment_name=deployment.name
)

# Cost report
report = cost_tracker.generate_serving_report(period="daily")
print(f"Daily serving cost: ${report.daily_cost:.2f}")
print(f"Cost per 1000 predictions: ${report.cost_per_1k:.4f}")
print(f"Average instances: {report.avg_instances:.2f}")
print(f"Peak instances: {report.peak_instances}")
print(f"Auto-scaling savings: ${report.autoscale_savings:.2f}")
```

### Prediction Caching for Cost Reduction
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import hashlib
import json
from datetime import timedelta
from finops_tracker import CacheCostTracker

app = FastAPI()

# Redis cache
cache = redis.Redis(
    host="ml-cache.redis.cache.windows.net",
    port=6380,
    password=os.getenv("REDIS_PASSWORD"),
    ssl=True,
    decode_responses=True,
    connection_pool=redis.ConnectionPool(max_connections=50)
)

cost_tracker = CacheCostTracker()

class PredictionRequest(BaseModel):
    customer_id: str
    features: dict

class PredictionResponse(BaseModel):
    prediction: float
    cached: bool
    model_version: str

def generate_cache_key(request: PredictionRequest) -> str:
    """Generate deterministic cache key"""
    content = f"{request.customer_id}:{json.dumps(request.features, sort_keys=True)}"
    return f"pred:{hashlib.md5(content.encode()).hexdigest()}"

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Prediction endpoint with caching"""

    cache_key = generate_cache_key(request)

    # Check cache first
    cached_prediction = cache.get(cache_key)
    if cached_prediction:
        cost_tracker.record_cache_hit()
        return PredictionResponse(
            prediction=float(cached_prediction),
            cached=True,
            model_version="v2"
        )

    # Cache miss - compute prediction
    cost_tracker.record_cache_miss()

    # Get features and predict
    features = await feature_store.get_online_features(
        feature_refs=["customer_behavior:v1"],
        entity_keys={"customer_id": request.customer_id}
    )

    prediction = model.predict(features)[0]

    # Cache result (1 hour TTL)
    cache.setex(
        cache_key,
        timedelta(hours=1),
        str(prediction)
    )

    return PredictionResponse(
        prediction=prediction,
        cached=False,
        model_version="v2"
    )

@app.get("/cache-stats")
async def cache_stats():
    """Cache performance and cost metrics"""
    stats = cost_tracker.get_stats()

    return {
        "cache_hit_rate": stats.hit_rate,
        "total_requests": stats.total_requests,
        "cache_hits": stats.cache_hits,
        "cache_misses": stats.cache_misses,
        "cost_savings": f"${stats.cost_savings:.2f}",
        "avg_latency_cached": f"{stats.avg_latency_cached:.2f}ms",
        "avg_latency_uncached": f"{stats.avg_latency_uncached:.2f}ms"
    }

# Expected results:
# - Cache hit rate: 80-95%
# - Cost reduction: 60-80% (fewer model inferences)
# - Latency improvement: 10-50x for cached requests
```

### Batch Inference for Cost Efficiency
```python
from batch_inference import BatchInferenceEngine
from azure.ai.ml import Input, Output
from finops_tracker import BatchCostTracker

class OptimizedBatchInference:
    """Cost-optimized batch inference"""

    def __init__(self):
        self.engine = BatchInferenceEngine()
        self.cost_tracker = BatchCostTracker()

    def batch_predict(
        self,
        input_data_path: str,
        output_path: str,
        batch_size: int = 1000,
        use_spot: bool = True
    ):
        """Run batch inference with cost optimization"""

        # Use spot instances for 60-90% savings
        compute_config = {
            "instance_type": "Standard_D4s_v3",
            "instance_count": 4,
            "tier": "LowPriority" if use_spot else "Dedicated",
            "max_concurrent_tasks": 4
        }

        with self.cost_tracker.track_batch_job():
            # Configure batch job
            batch_job = self.engine.create_batch_job(
                name="churn_prediction_batch",
                model="azureml:churn_predictor:2",
                compute=compute_config,
                mini_batch_size=batch_size,
                retry_settings={
                    "max_retries": 3,
                    "timeout": 300
                },
                environment_variables={
                    "BATCH_SIZE": str(batch_size),
                    "ENABLE_OPTIMIZATION": "true"
                },
                inputs={
                    "input_data": Input(
                        type="uri_folder",
                        path=input_data_path
                    )
                },
                outputs={
                    "predictions": Output(
                        type="uri_folder",
                        path=output_path
                    )
                }
            )

            # Run batch inference
            job = ml_client.batch_deployments.invoke(
                deployment_name="batch-deployment",
                inputs=batch_job.inputs,
                outputs=batch_job.outputs
            )

            # Wait for completion
            ml_client.jobs.stream(job.name)

        # Cost analysis
        cost_report = self.cost_tracker.generate_report()
        print(f"\nBatch Inference Cost Report:")
        print(f"Total predictions: {cost_report.total_predictions:,}")
        print(f"Total cost: ${cost_report.total_cost:.2f}")
        print(f"Cost per 1000 predictions: ${cost_report.cost_per_1k:.4f}")
        print(f"Spot savings: ${cost_report.spot_savings:.2f}")
        print(f"Duration: {cost_report.duration_minutes:.2f} minutes")
        print(f"Throughput: {cost_report.throughput_per_minute:,.0f} predictions/min")

        # Compare with online serving
        online_cost = cost_report.total_predictions * 0.001  # Assume $0.001 per prediction
        print(f"\nCost comparison:")
        print(f"Batch inference: ${cost_report.total_cost:.2f}")
        print(f"Online serving equivalent: ${online_cost:.2f}")
        print(f"Savings: ${online_cost - cost_report.total_cost:.2f} ({((online_cost - cost_report.total_cost) / online_cost * 100):.1f}%)")

        return cost_report

# Usage
batch_engine = OptimizedBatchInference()

# Run batch prediction (100x cheaper than online for large batches)
cost_report = batch_engine.batch_predict(
    input_data_path="azureml://datasets/scoring_data/labels/latest",
    output_path="azureml://datastores/predictions/paths/batch_2024_01/",
    batch_size=1000,
    use_spot=True
)
```

### Model Optimization for Faster Inference
```python
from model_optimizer import ModelOptimizer, ONNXConverter
import onnxruntime as ort
import numpy as np
from finops_tracker import InferenceCostTracker

class OptimizedModelServer:
    """Optimized model serving with ONNX"""

    def __init__(self, model_path: str):
        self.optimizer = ModelOptimizer()
        self.cost_tracker = InferenceCostTracker()

        # Convert to ONNX for 2-5x speedup
        self.onnx_model = self.optimizer.convert_to_onnx(
            model_path=model_path,
            opset_version=13
        )

        # Quantize for 4x size reduction and faster inference
        self.quantized_model = self.optimizer.quantize(
            self.onnx_model,
            quantization_mode="dynamic",  # or "static" for more accuracy
            optimize_for="latency"  # or "throughput"
        )

        # Create ONNX Runtime session
        sess_options = ort.SessionOptions()
        sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        sess_options.intra_op_num_threads = 4

        self.session = ort.InferenceSession(
            self.quantized_model,
            sess_options,
            providers=['CPUExecutionProvider']  # Use CPU for cost savings
        )

    def predict(self, features: np.ndarray) -> np.ndarray:
        """Optimized prediction"""

        with self.cost_tracker.track_inference():
            # ONNX inference (2-5x faster than native)
            input_name = self.session.get_inputs()[0].name
            output_name = self.session.get_outputs()[0].name

            predictions = self.session.run(
                [output_name],
                {input_name: features.astype(np.float32)}
            )[0]

        return predictions

    def benchmark(self, test_data: np.ndarray, num_iterations: int = 1000):
        """Benchmark optimized vs original model"""

        # Original model (for comparison)
        original_model = self.optimizer.load_original_model()

        print("Benchmarking optimized model...")

        # Warm up
        for _ in range(10):
            self.predict(test_data[:1])
            original_model.predict(test_data[:1])

        # Benchmark optimized
        import time
        start = time.time()
        for _ in range(num_iterations):
            self.predict(test_data[:1])
        optimized_time = time.time() - start

        # Benchmark original
        start = time.time()
        for _ in range(num_iterations):
            original_model.predict(test_data[:1])
        original_time = time.time() - start

        # Results
        speedup = original_time / optimized_time
        cost_reduction = 1 - (1 / speedup)

        print(f"\nBenchmark Results:")
        print(f"Original model time: {original_time:.3f}s ({original_time/num_iterations*1000:.2f}ms per prediction)")
        print(f"Optimized model time: {optimized_time:.3f}s ({optimized_time/num_iterations*1000:.2f}ms per prediction)")
        print(f"Speedup: {speedup:.2f}x")
        print(f"Latency reduction: {(1 - optimized_time/original_time)*100:.1f}%")
        print(f"Cost reduction: {cost_reduction*100:.1f}%")
        print(f"Model size reduction: {self.optimizer.get_size_reduction():.1f}x")

        return {
            "speedup": speedup,
            "cost_reduction_percent": cost_reduction * 100,
            "optimized_latency_ms": optimized_time / num_iterations * 1000
        }

# Usage
server = OptimizedModelServer("models/churn_predictor_v2.pkl")

# Benchmark
test_features = np.random.rand(100, 20)
results = server.benchmark(test_features)

# Expected results:
# - 2-5x speedup with ONNX
# - 4x model size reduction with quantization
# - 50-80% cost reduction (same throughput with fewer instances)
```

##  CI/CD for Model Serving

### Automated Deployment Pipeline
```yaml
# .github/workflows/model-deployment.yml
name: Model Deployment Pipeline

on:
  workflow_run:
    workflows: ["Model Training Pipeline"]
    types:
      - completed
  workflow_dispatch:
    inputs:
      model_version:
        description: 'Model version to deploy'
        required: true

jobs:
  deploy-model:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    steps:
      - uses: actions/checkout@v3

      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Get model from registry
        run: |
          python scripts/download_model.py \
            --model-name churn_predictor \
            --version ${{ github.event.inputs.model_version || 'latest' }}

      - name: Optimize model for serving
        run: |
          python scripts/optimize_model.py \
            --input-model ./model \
            --output-model ./optimized_model \
            --format onnx \
            --quantize dynamic

      - name: Build Docker image
        run: |
          docker build -t ${{ secrets.ACR_NAME }}.azurecr.io/churn-predictor:${{ github.sha }} \
            -f Dockerfile.serving .

      - name: Run container security scan
        run: |
          docker scan ${{ secrets.ACR_NAME }}.azurecr.io/churn-predictor:${{ github.sha }}

      - name: Push to container registry
        run: |
          az acr login --name ${{ secrets.ACR_NAME }}
          docker push ${{ secrets.ACR_NAME }}.azurecr.io/churn-predictor:${{ github.sha }}

      - name: Run inference tests
        run: |
          docker run -d -p 8000:8000 \
            ${{ secrets.ACR_NAME }}.azurecr.io/churn-predictor:${{ github.sha }}
          sleep 10
          pytest tests/inference/ --endpoint http://localhost:8000

      - name: Deploy to staging (canary)
        run: |
          python scripts/deploy_model.py \
            --environment staging \
            --image ${{ secrets.ACR_NAME }}.azurecr.io/churn-predictor:${{ github.sha }} \
            --traffic-percent 10

      - name: Run load tests
        run: |
          locust -f tests/load/test_endpoint.py \
            --headless \
            --users 100 \
            --spawn-rate 10 \
            --run-time 5m \
            --host https://staging-churn-api.azurewebsites.net

      - name: Monitor canary performance
        run: |
          python scripts/monitor_canary.py \
            --duration 30m \
            --min-success-rate 99 \
            --max-latency-p95 100

      - name: Promote to production
        if: success()
        run: |
          python scripts/deploy_model.py \
            --environment production \
            --image ${{ secrets.ACR_NAME }}.azurecr.io/churn-predictor:${{ github.sha }} \
            --strategy blue-green \
            --traffic-percent 100

      - name: Generate deployment report
        run: python scripts/deployment_report.py
```

##  Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Serving Costs** | Cost per 1000 predictions | <$0.05 | FinOps tracker |
| | Monthly serving costs | <$1500 | Azure Cost Management |
| | Auto-scaling savings | >50% | Cost tracker |
| | Cache savings | >60% | Redis metrics |
| **Performance** | Prediction latency (p95) | <100ms | App Insights |
| | Throughput | >1000 req/s | Load balancer |
| | Cache hit rate | >80% | Redis |
| | Model load time | <10s | Startup metrics |
| **Reliability** | Availability (SLA) | >99.9% | Azure Monitor |
| | Error rate | <0.1% | API metrics |
| | Deployment success rate | >99% | CI/CD metrics |
| **Resource Usage** | CPU utilization | 60-80% | Azure Monitor |
| | Memory utilization | <80% | Container metrics |
| | Instance count | Auto-scaled | HPA metrics |
| **API Usage** | Requests per minute | Monitored | API Gateway |
| | Rate limit violations | <1% | Gateway logs |

##  Integration Workflow

### End-to-End Serving Pipeline
```
1. Model Registry (ml-07)
   ↓
2. Model Optimization (ml-08)
   ↓
3. Container Build (do-03)
   ↓
4. Security Scan (sa-08)
   ↓
5. Staging Deployment (do-06)
   ↓
6. Load Testing (ml-04)
   ↓
7. Canary Deployment (do-06)
   ↓
8. Performance Monitoring (mo-04, do-08)
   ↓
9. Production Promotion (ml-04)
   ↓
10. Auto-Scaling (fo-06)
    ↓
11. Cost Monitoring (fo-01, fo-07)
    ↓
12. Drift Detection (mo-05)
```

##  Quick Wins

1. **Enable auto-scaling** - 40-60% serving cost reduction
2. **Implement prediction caching** - 60-80% cost savings
3. **Convert models to ONNX** - 2-5x inference speedup
4. **Use model quantization** - 4x model size reduction
5. **Implement request batching** - 10-50x throughput increase
6. **Right-size instances** - 30-50% cost reduction
7. **Use canary deployments** - Zero-downtime releases
8. **Add health checks** - Better reliability
9. **Enable async processing** - Higher concurrency
10. **Monitor serving costs** - Identify optimization opportunities
