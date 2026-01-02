# Skill 1: MLOps Pipeline Automation

##  Overview
Build end-to-end MLOps pipelines with automated training, versioning, and deployment.

##  Connections
- **Data Engineer**: Consumes data from feature pipelines (de-01, de-02, de-03)
- **AI Engineer**: Serves models for agent systems (ai-03, ai-07)
- **Data Scientist**: Promotes experiments to production (ds-01, ds-02, ds-08)
- **Security Architect**: Ensures model provenance and audit trails (sa-02, sa-06, sa-08)
- **MLOps**: Full lifecycle management (mo-01 through mo-08)
- **FinOps**: ML training and serving cost optimization (fo-01, fo-06, fo-07)
- **DevOps**: CI/CD for ML pipelines, container orchestration (do-01, do-03, do-08)
- **System Design**: Scalability and performance patterns (sd-03, sd-05, sd-07)

##  Tools Included

### 1. `ml_pipeline_orchestrator.py`
End-to-end ML pipeline with Kedro/ZenML patterns.

### 2. `model_registry_manager.py`
MLflow model registry with lifecycle management.

### 3. `experiment_tracker.py`
Comprehensive experiment tracking with metrics, params, artifacts.

### 4. `ci_cd_ml_pipeline.py`
CI/CD automation for ML workflows.

### 5. `mlops_config.yaml`
Configuration templates for MLOps infrastructure.

##  Pipeline Stages

```
Data Validation → Feature Engineering → Model Training →
Evaluation → Registration → Deployment → Monitoring
```

##  Quick Start

```python
from ml_pipeline_orchestrator import MLPipeline

# Define pipeline
pipeline = MLPipeline(
    name="customer_churn_predictor",
    experiment_name="churn_model_v2"
)

# Run training
pipeline.train(
    data_path="gold.customer_features",
    model_type="xgboost",
    hyperparams={"max_depth": 6, "n_estimators": 100}
)

# Promote to production
pipeline.promote_to_production(
    stage="Production",
    archive_existing=True
)
```

##  Best Practices

### ML Training Cost Optimization (FinOps Integration)

1. **Compute Cost Optimization**
   - Use spot/preemptible instances for training (60-90% savings)
   - Right-size compute based on model requirements
   - Auto-scale training clusters
   - Schedule training during off-peak hours
   - Reference: FinOps fo-06 (Compute Optimization), fo-07 (AI/ML Cost)

2. **Track Training Costs**
   - Log compute costs per experiment
   - Track GPU utilization and cost efficiency
   - Monitor training time vs accuracy trade-offs
   - Set budget alerts for long-running experiments
   - Reference: FinOps fo-01 (Cost Monitoring), fo-03 (Budget Management)

3. **Optimize Hyperparameter Tuning**
   - Use early stopping to prevent wasteful runs
   - Implement intelligent search (Bayesian vs grid search)
   - Parallelize trials efficiently
   - Track cost per trial
   - Reference: ML Engineer best practices, FinOps fo-07

4. **Model Serving Cost Optimization**
   - Use auto-scaling for inference endpoints
   - Implement model caching for frequent predictions
   - Batch predictions when possible
   - Use smaller/distilled models for cost-sensitive applications
   - Monitor inference costs per request
   - Reference: FinOps fo-06, fo-07

5. **Storage Cost Optimization**
   - Compress model artifacts and datasets
   - Implement lifecycle policies for experiments
   - Archive old model versions to cold storage
   - Monitor artifact storage costs
   - Reference: FinOps fo-05 (Storage Optimization)

### DevOps Integration for ML

6. **CI/CD for ML Pipelines**
   - Automate model training on code changes
   - Run model validation tests before deployment
   - Implement canary deployments for models
   - Automate rollback on quality degradation
   - Reference: DevOps do-01 (CI/CD), do-06 (Deployment Strategies)

7. **Containerization**
   - Package models in containers for portability
   - Use multi-stage builds to minimize image size
   - Implement health checks for model endpoints
   - Deploy to AKS for production serving
   - Reference: DevOps do-03 (Containerization)

8. **Infrastructure as Code for ML**
   - Deploy ML infrastructure with Terraform
   - Version control all infrastructure
   - Automate environment provisioning
   - Implement disaster recovery
   - Reference: DevOps do-04 (IaC)

9. **Monitoring & Observability**
   - Instrument pipelines with OpenTelemetry
   - Track model performance metrics in production
   - Set up alerts for model drift and degradation
   - Monitor inference latency and throughput
   - Reference: DevOps do-08 (Monitoring), MLOps mo-04

### Model Lifecycle Management (MLOps Integration)

10. **Experiment Tracking**
    - Track all experiments with MLflow/Azure ML
    - Log hyperparameters, metrics, and artifacts
    - Compare experiment results systematically
    - Version datasets alongside experiments
    - Reference: MLOps mo-01 (Experiment Tracking)

11. **Model Versioning & Registry**
    - Register all production models
    - Track model lineage (data + code + config)
    - Implement model approval workflows
    - Version control model configurations
    - Reference: MLOps mo-03 (Model Versioning)

12. **Feature Engineering & Feature Store**
    - Centralize features in a feature store
    - Track feature versions and lineage
    - Monitor feature drift
    - Reuse features across models
    - Reference: ML Engineer ml-02, MLOps mo-02

13. **Model Monitoring**
    - Monitor model performance in production
    - Detect data drift and concept drift
    - Track prediction distribution shifts
    - Set up automated retraining triggers
    - Reference: MLOps mo-04 (Monitoring), mo-05 (Drift Detection)

### Security & Compliance

14. **Model Security**
    - Scan model dependencies for vulnerabilities
    - Implement model access controls
    - Encrypt model artifacts at rest
    - Audit model predictions for compliance
    - Reference: Security Architect sa-02 (IAM), sa-08 (LLM Security)

15. **Data Privacy in Training**
    - Remove PII before training
    - Implement differential privacy where needed
    - Track data usage for compliance
    - Document data sources and lineage
    - Reference: Security Architect sa-01 (PII Detection), sa-06 (Governance)

16. **Model Provenance**
    - Track complete model lineage
    - Document training data sources
    - Version all training code and configs
    - Maintain audit logs for model decisions
    - Reference: MLOps mo-06 (Lineage), Security Architect sa-06

### Azure-Specific Best Practices

17. **Azure Machine Learning**
    - Use managed compute clusters
    - Enable auto-scaling for training and inference
    - Implement managed endpoints for serving
    - Use Azure ML Pipelines for orchestration
    - Reference: Azure az-04 (AI/ML Services)

18. **Cost Management in Azure ML**
    - Use low-priority compute for training
    - Enable compute instance auto-shutdown
    - Monitor compute utilization
    - Set spending limits per workspace
    - Reference: Azure az-04, FinOps fo-06

### Production Best Practices

19. **A/B Testing for Models**
    - Deploy multiple model versions
    - Route traffic based on experiment design
    - Track statistical significance
    - Automated winner selection
    - Reference: Data Scientist ds-08 (Experimentation)

20. **Model Performance Optimization**
    - Optimize model inference latency
    - Implement model quantization
    - Use ONNX for cross-platform deployment
    - Batch predictions for throughput
    - Reference: ML Engineer best practices

##  Cost Optimization Examples

### Training Cost Tracking
```python
from ml_pipeline_orchestrator import MLPipeline
from finops_tracker import MLCostTracker

cost_tracker = MLCostTracker()

# Track training costs
@cost_tracker.track_training_cost
def train_model(config: dict):
    pipeline = MLPipeline(
        name="customer_churn_predictor",
        compute_target="spot-gpu-cluster",  # Use spot instances
        auto_scale=True,
        max_nodes=4
    )

    # Track costs per experiment
    with cost_tracker.experiment_context("churn_v2"):
        pipeline.train(
            data_path="gold.customer_features",
            model_type="xgboost",
            hyperparams=config
        )

# Generate cost report
report = cost_tracker.generate_training_report(period="monthly")
print(f"Total training costs: ${report.total_cost:.2f}")
print(f"Cost per experiment: ${report.avg_cost_per_experiment:.2f}")
print(f"Savings from spot instances: ${report.spot_savings:.2f}")
print(f"Most expensive experiments: {report.top_experiments}")

# Set budget alerts
cost_tracker.set_budget_alert(
    experiment_name="churn_v2",
    budget_per_run=50.00,
    monthly_budget=500.00
)
```

### Spot Instance Training (60-90% Savings)
```python
from azure.ai.ml import command, Input
from azure.ai.ml.entities import AmlCompute

# Create spot compute cluster
compute_config = AmlCompute(
    name="spot-training-cluster",
    size="Standard_NC6s_v3",  # GPU instance
    min_instances=0,
    max_instances=4,
    tier="LowPriority",  # Spot instances!
    idle_time_before_scale_down=300
)

# Submit training job with checkpointing
job = command(
    code="./src",
    command="python train.py --checkpoint-freq 100",  # Save checkpoints
    environment="azureml:training-env:1",
    compute="spot-training-cluster",
    inputs={
        "data": Input(path="azureml://datasets/customer_features/labels/latest")
    }
)

# Job will automatically resume from checkpoint if preempted
ml_client.jobs.create_or_update(job)
```

### Model Serving Cost Optimization
```python
from model_registry_manager import ModelRegistry
from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment

registry = ModelRegistry()

# Deploy with auto-scaling
endpoint = ManagedOnlineEndpoint(
    name="churn-prediction",
    auth_mode="key"
)

deployment = ManagedOnlineDeployment(
    name="churn-v2",
    endpoint_name="churn-prediction",
    model=registry.get_model("churn_predictor:v2"),
    instance_type="Standard_DS2_v2",
    instance_count=1,
    # Auto-scale based on load
    scale_settings={
        "scale_type": "target_utilization",
        "min_instances": 1,
        "max_instances": 5,
        "target_utilization_percentage": 70
    },
    # Request timeout for cost control
    request_timeout_ms=5000
)

# Monitor serving costs
from finops_tracker import InferenceCostTracker
inference_tracker = InferenceCostTracker()

@inference_tracker.track_inference_cost
def predict(data):
    return endpoint.invoke(data)

# Cost report
report = inference_tracker.generate_inference_report()
print(f"Cost per 1000 predictions: ${report.cost_per_1k:.4f}")
print(f"Monthly serving costs: ${report.monthly_cost:.2f}")
```

### Hyperparameter Tuning Cost Optimization
```python
from azure.ai.ml.sweep import Choice, Uniform, BayesianSamplingAlgorithm
from ml_cost_optimizer import EarlyStoppingPolicy

# Use Bayesian optimization (more efficient than grid search)
sweep_job = command_job.sweep(
    sampling_algorithm=BayesianSamplingAlgorithm(),  # Smart search
    primary_metric="accuracy",
    goal="maximize",
    max_total_trials=20,  # Limit trials
    max_concurrent_trials=4,
    early_termination_policy=EarlyStoppingPolicy(
        evaluation_interval=1,
        delay_evaluation=5,
        slack_factor=0.1  # Stop if 10% worse than best
    )
)

# Track tuning costs
cost_tracker.track_sweep_cost(sweep_job)
```

##  CI/CD for ML Pipelines

### Automated ML Pipeline
```yaml
# .github/workflows/ml-pipeline.yml
name: ML Pipeline CI/CD

on:
  push:
    paths:
      - 'models/**'
      - 'pipelines/**'
    branches:
      - main
  schedule:
    - cron: '0 2 * * 0'  # Weekly retraining

jobs:
  train-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Run unit tests
        run: pytest tests/unit/

      - name: Validate data quality
        run: python scripts/validate_training_data.py

      - name: Train model (spot instances)
        run: |
          python pipelines/train.py \
            --compute-type spot \
            --max-cost 100.00 \
            --early-stopping true

      - name: Evaluate model
        run: |
          python pipelines/evaluate.py \
            --min-accuracy 0.85 \
            --min-auc 0.90

      - name: Register model
        if: success()
        run: python scripts/register_model.py

      - name: Deploy to staging
        run: |
          python scripts/deploy_model.py \
            --environment staging \
            --traffic-percent 100

      - name: Run integration tests
        run: pytest tests/integration/

      - name: Deploy to production (canary)
        if: success()
        run: |
          python scripts/deploy_model.py \
            --environment production \
            --strategy canary \
            --traffic-percent 10

      - name: Monitor model performance
        run: python scripts/monitor_model.py --duration 24h

      - name: Promote canary to full
        if: success()
        run: python scripts/promote_deployment.py --traffic-percent 100

      - name: Generate cost report
        run: python scripts/ml_cost_report.py
```

### Infrastructure as Code for ML
```hcl
# ml-infrastructure.tf
module "ml_workspace" {
  source = "./modules/azure-ml"

  resource_group = "rg-ml-prod"
  location       = "eastus"

  workspace = {
    name                = "ml-workspace-prod"
    sku                 = "Basic"
    public_network_access = false
  }

  compute_clusters = [
    {
      name          = "cpu-cluster"
      vm_size       = "Standard_D4s_v3"
      min_nodes     = 0
      max_nodes     = 4
      idle_time     = 300
      tier          = "Dedicated"
    },
    {
      name          = "gpu-spot-cluster"
      vm_size       = "Standard_NC6s_v3"
      min_nodes     = 0
      max_nodes     = 4
      idle_time     = 120
      tier          = "LowPriority"  # 60-90% cost savings
    }
  ]

  endpoints = [
    {
      name          = "churn-prediction"
      traffic_rules = {
        "blue"  = 90  # Current production
        "green" = 10  # Canary deployment
      }
      auto_scale = {
        min_instances = 2
        max_instances = 10
        target_cpu    = 70
      }
    }
  ]

  cost_management = {
    monthly_budget        = 5000.00
    alert_threshold       = 0.8
    auto_shutdown_enabled = true
    auto_shutdown_time    = "19:00"
  }

  tags = {
    Environment = "Production"
    CostCenter  = "ML-Platform"
    Owner       = "MLOps-Team"
  }
}
```

##  Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Training Costs** | Cost per experiment | <$50 | FinOps tracker |
| | Monthly training budget | <$5000 | Azure Cost Management |
| | Spot instance savings | >70% | Cost tracker |
| | GPU utilization | >80% | Azure Monitor |
| **Serving Costs** | Cost per 1000 predictions | <$0.10 | Inference tracker |
| | Monthly serving costs | <$2000 | FinOps dashboard |
| | Auto-scaling efficiency | >70% | Azure Monitor |
| **Model Performance** | Production accuracy | >0.85 | MLflow |
| | Prediction latency (p95) | <100ms | App Insights |
| | Model drift score | <0.1 | Drift monitor |
| **Pipeline Reliability** | Training success rate | >95% | Azure ML |
| | Deployment success rate | >99% | DevOps metrics |
| | Rollback frequency | <2/month | Deployment logs |
| **Data Quality** | Feature freshness | <1 hour | Data quality checks |
| | Training data completeness | >99% | Validation tests |

##  Integration Workflow

### End-to-End MLOps Pipeline
```
1. Feature Engineering (de-01, ml-02)
   ↓
2. Data Validation (de-03)
   ↓
3. PII Removal (sa-01)
   ↓
4. Experiment Tracking (mo-01)
   ↓
5. Model Training with Cost Tracking (ml-01, fo-07)
   ↓
6. Model Evaluation (ml-01, ds-08)
   ↓
7. Model Registry (mo-03)
   ↓
8. Security Scan (sa-08)
   ↓
9. CI/CD Deployment (do-01)
   ↓
10. Canary Deployment (do-06)
    ↓
11. Production Monitoring (mo-04, do-08)
    ↓
12. Drift Detection (mo-05)
    ↓
13. Cost Optimization (fo-01, fo-06, fo-07)
    ↓
14. Automated Retraining (ml-01)
```

##  Quick Wins

1. **Use spot instances for training** - 60-90% compute cost savings
2. **Enable auto-scaling for inference** - 30-50% serving cost reduction
3. **Implement early stopping** - Reduce wasteful hyperparameter trials
4. **Set up experiment tracking** - Compare models systematically
5. **Automate model deployment** - Faster time to production
6. **Enable model monitoring** - Detect drift before degradation
7. **Implement cost tracking** - Know where ML budget is going
8. **Use canary deployments** - Safer model releases
9. **Containerize models** - Portable and scalable serving
10. **Set budget alerts** - Prevent cost overruns
