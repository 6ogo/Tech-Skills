# Skill 3: Model Training & Hyperparameter Tuning

##  Overview
Implement scalable model training pipelines with automated hyperparameter optimization and experiment tracking.

##  Connections
- **Data Scientist**: Productionizes experimental models (ds-01, ds-02, ds-08)
- **ML Engineer**: Feeds from feature store, deploys to serving (ml-02, ml-04, ml-07)
- **MLOps**: Experiment tracking and model versioning (mo-01, mo-03)
- **FinOps**: Optimizes training costs and compute usage (fo-06, fo-07)
- **DevOps**: Automates training pipelines with CI/CD (do-01, do-03, do-08)
- **Security Architect**: Ensures secure training environments (sa-02, sa-08)
- **System Design**: Distributed training architecture (sd-03, sd-05)
- **Data Engineer**: Consumes validated training data (de-03)

##  Tools Included

### 1. `model_trainer.py`
Unified training interface for sklearn, XGBoost, LightGBM, PyTorch.

### 2. `hyperparameter_optimizer.py`
Automated hyperparameter tuning with Optuna/Ray Tune.

### 3. `experiment_tracker.py`
MLflow integration for comprehensive experiment tracking.

### 4. `model_evaluator.py`
Model evaluation with business metrics and validation.

### 5. `training_config.yaml`
Configuration templates for training pipelines.

##  Training Pipeline Architecture

```
Feature Store → Data Preparation → Model Training → Evaluation → Registry
                      ↓                   ↓              ↓           ↓
                 Validation      Experiment Track  Metrics    Versioning
                 Splitting       HPO               Comparison  Lineage
                 Augmentation    Checkpointing     Validation  Promotion
```

##  Quick Start

```python
from model_trainer import ModelTrainer
from hyperparameter_optimizer import HPOptimizer
from experiment_tracker import ExperimentTracker

# Initialize tracker
tracker = ExperimentTracker(experiment_name="churn_prediction_v2")

# Configure training
trainer = ModelTrainer(
    model_type="xgboost",
    objective="binary:logistic",
    eval_metric="auc"
)

# Load features from feature store
features = feature_store.get_historical_features(
    feature_refs=["customer_behavior:v1"],
    entity_df=training_entities
)

# Train with experiment tracking
with tracker.start_run():
    # Log parameters
    tracker.log_params({
        "model_type": "xgboost",
        "max_depth": 6,
        "n_estimators": 100
    })

    # Train model
    model = trainer.train(
        X_train=features.drop(columns=["target"]),
        y_train=features["target"],
        validation_split=0.2
    )

    # Evaluate
    metrics = trainer.evaluate(X_test, y_test)
    tracker.log_metrics(metrics)

    # Save model
    tracker.log_model(model, "churn_predictor")

# Hyperparameter optimization
optimizer = HPOptimizer(
    estimator=trainer,
    param_space={
        "max_depth": [3, 5, 7, 9],
        "n_estimators": [50, 100, 200],
        "learning_rate": [0.01, 0.05, 0.1],
        "subsample": [0.7, 0.8, 0.9, 1.0]
    },
    optimization_metric="auc",
    n_trials=50
)

best_params = optimizer.optimize(X_train, y_train, X_val, y_val)
```

##  Best Practices

### Training Cost Optimization (FinOps Integration)

1. **Use Spot/Preemptible Instances**
   - 60-90% cost savings for interruptible training
   - Implement checkpointing for fault tolerance
   - Automatic job resumption after preemption
   - Best for batch training jobs
   - Reference: FinOps fo-06 (Compute Optimization), fo-07 (AI/ML Cost)

2. **Right-Size Training Compute**
   - Profile training jobs to determine optimal instance size
   - Use CPU for tree-based models (XGBoost, LightGBM)
   - Reserve GPUs for deep learning only
   - Monitor GPU/CPU utilization
   - Auto-scale compute clusters
   - Reference: FinOps fo-06

3. **Optimize Hyperparameter Tuning**
   - Use Bayesian optimization over grid search (10x fewer trials)
   - Implement early stopping to terminate poor trials
   - Parallelize trials efficiently
   - Track cost per hyperparameter trial
   - Set budget limits per optimization run
   - Reference: FinOps fo-07, ML best practices

4. **Training Time Optimization**
   - Use early stopping to prevent overtraining
   - Implement learning rate schedules
   - Use mixed precision training (2x faster on GPUs)
   - Profile and optimize data loading
   - Cache preprocessed data
   - Reference: ML Engineer best practices

5. **Track Training Costs Per Experiment**
   - Log compute costs with experiments
   - Track training duration and resource usage
   - Monitor cost vs accuracy trade-offs
   - Set budget alerts for runaway experiments
   - Reference: FinOps fo-01 (Cost Monitoring), fo-03 (Budget Management)

### MLOps Integration for Training

6. **Comprehensive Experiment Tracking**
   - Track all hyperparameters and configurations
   - Log all metrics (training, validation, test)
   - Version datasets used for training
   - Save model artifacts and checkpoints
   - Track training duration and resource usage
   - Reference: MLOps mo-01 (Experiment Tracking)

7. **Model Versioning & Lineage**
   - Version all trained models
   - Track complete lineage (data + code + config)
   - Link models to training runs
   - Document model architecture and purpose
   - Reference: MLOps mo-03 (Model Versioning), mo-06 (Lineage)

8. **Reproducible Training**
   - Set random seeds for reproducibility
   - Version control training code
   - Pin dependency versions
   - Document training environment
   - Store training configurations
   - Reference: MLOps mo-01, DevOps do-01

9. **Model Validation & Testing**
   - Validate on held-out test set
   - Test model performance on edge cases
   - Verify model fairness and bias
   - Test inference latency
   - Reference: MLOps mo-07 (Testing), Data Scientist ds-08

### DevOps Integration for Training

10. **Automated Training Pipelines**
    - Trigger training on data updates
    - Automate model evaluation and comparison
    - Implement automatic model promotion
    - Schedule periodic retraining
    - Reference: DevOps do-01 (CI/CD), ML Engineer ml-01

11. **Containerized Training**
    - Package training code in Docker containers
    - Use multi-stage builds for efficiency
    - Version control container definitions
    - Test containers locally before deployment
    - Reference: DevOps do-03 (Containerization)

12. **Infrastructure as Code for Training**
    - Define training infrastructure in Terraform
    - Automate compute cluster provisioning
    - Version control all infrastructure
    - Implement environment parity (dev/staging/prod)
    - Reference: DevOps do-04 (IaC)

13. **Monitoring & Observability**
    - Monitor training job status and health
    - Track training metrics in real-time
    - Set up alerts for training failures
    - Log training errors and exceptions
    - Reference: DevOps do-08 (Monitoring)

### Data Quality for Training

14. **Training Data Validation**
    - Validate data schema before training
    - Check for data drift vs previous training
    - Verify label distribution
    - Detect data quality issues early
    - Reference: Data Engineer de-03 (Data Quality)

15. **Data Versioning**
    - Version training datasets
    - Track data lineage for reproducibility
    - Document data collection and labeling
    - Reference: MLOps mo-06 (Lineage)

### Security & Compliance

16. **Secure Training Environments**
    - Train in isolated network environments
    - Use managed identities for authentication
    - Encrypt data at rest and in transit
    - Audit training job access
    - Reference: Security Architect sa-02 (IAM), sa-03 (Network)

17. **Model Security**
    - Scan training dependencies for vulnerabilities
    - Implement model access controls
    - Audit model artifacts
    - Document model security posture
    - Reference: Security Architect sa-08 (LLM Security)

### Azure-Specific Best Practices

18. **Azure Machine Learning**
    - Use managed compute clusters
    - Enable auto-scaling for training jobs
    - Leverage Azure ML pipelines
    - Use Azure ML environments for reproducibility
    - Reference: Azure az-04 (AI/ML Services)

19. **Cost Management in Azure ML**
    - Use low-priority compute for training (70-80% savings)
    - Enable compute auto-shutdown
    - Monitor compute utilization
    - Set workspace spending limits
    - Reference: Azure az-04, FinOps fo-06

20. **Model Training Best Practices**
    - Use early stopping callbacks
    - Implement cross-validation for robust estimates
    - Track learning curves for overfitting detection
    - Save best model checkpoints
    - Reference: ML Engineer best practices

##  Cost Optimization Examples

### Spot Instance Training with Checkpointing
```python
from azure.ai.ml import command, Input
from azure.ai.ml.entities import AmlCompute
from model_trainer import CheckpointedTrainer

# Create spot compute cluster (60-90% savings)
spot_cluster = AmlCompute(
    name="spot-training-cluster",
    size="Standard_NC6s_v3",  # GPU instance
    min_instances=0,
    max_instances=4,
    tier="LowPriority",  # Spot pricing!
    idle_time_before_scale_down=300
)

ml_client.compute.begin_create_or_update(spot_cluster).result()

# Checkpointed trainer (automatically resumes after preemption)
trainer = CheckpointedTrainer(
    model_type="pytorch",
    checkpoint_dir="./checkpoints",
    checkpoint_frequency=100,  # Save every 100 steps
    resume_from_checkpoint=True
)

# Training script with checkpointing
training_script = """
import torch
from model_trainer import CheckpointedTrainer

trainer = CheckpointedTrainer(
    model_type="pytorch",
    checkpoint_dir="./outputs/checkpoints"
)

# Load checkpoint if exists (after preemption)
start_epoch = trainer.load_checkpoint_if_exists()

# Training loop with automatic checkpointing
for epoch in range(start_epoch, num_epochs):
    train_loss = trainer.train_epoch(model, train_loader)
    val_loss = trainer.validate(model, val_loader)

    # Automatic checkpoint saving
    trainer.save_checkpoint(
        epoch=epoch,
        model=model,
        optimizer=optimizer,
        loss=val_loss
    )
"""

# Submit to spot cluster
job = command(
    code="./src",
    command="python train.py",
    environment="azureml:pytorch-training:1",
    compute="spot-training-cluster",
    inputs={
        "training_data": Input(path="azureml://datasets/training_data/labels/latest")
    }
)

# Job automatically resumes from checkpoint if preempted
run = ml_client.jobs.create_or_update(job)

# Track savings
from finops_tracker import TrainingCostTracker
cost_tracker = TrainingCostTracker()
savings_report = cost_tracker.calculate_spot_savings(run.name)
print(f"Cost with spot: ${savings_report.spot_cost:.2f}")
print(f"Cost with dedicated: ${savings_report.dedicated_cost:.2f}")
print(f"Total savings: ${savings_report.savings:.2f} ({savings_report.savings_percent}%)")
```

### Bayesian Hyperparameter Optimization (10x Fewer Trials)
```python
from hyperparameter_optimizer import BayesianOptimizer
from finops_tracker import HPOCostTracker
import optuna

cost_tracker = HPOCostTracker()

def objective(trial):
    """Objective function with cost tracking"""

    # Suggest hyperparameters
    params = {
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'n_estimators': trial.suggest_int('n_estimators', 50, 300),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 1.0),
        'min_child_weight': trial.suggest_int('min_child_weight', 1, 7),
        'gamma': trial.suggest_float('gamma', 0, 0.5)
    }

    # Track trial cost
    with cost_tracker.track_trial(trial.number):
        # Train model
        trainer = ModelTrainer(model_type="xgboost", **params)
        trainer.train(X_train, y_train)

        # Evaluate
        score = trainer.evaluate(X_val, y_val)['auc']

    # Report cost
    cost_tracker.report_trial_cost(trial.number, score)

    return score

# Bayesian optimization with early stopping
study = optuna.create_study(
    direction='maximize',
    sampler=optuna.samplers.TPESampler(seed=42),  # Bayesian optimization
    pruner=optuna.pruners.MedianPruner(  # Early stopping for poor trials
        n_startup_trials=5,
        n_warmup_steps=10,
        interval_steps=1
    )
)

# Run optimization with budget limit
study.optimize(
    objective,
    n_trials=50,  # vs 1000+ for grid search
    timeout=3600,  # 1 hour max
    callbacks=[cost_tracker.budget_callback(max_budget=100.00)]
)

# Results with cost analysis
print(f"Best AUC: {study.best_value:.4f}")
print(f"Best params: {study.best_params}")

cost_report = cost_tracker.generate_hpo_report()
print(f"\nHPO Cost Analysis:")
print(f"Total trials: {cost_report.total_trials}")
print(f"Completed trials: {cost_report.completed_trials}")
print(f"Pruned trials: {cost_report.pruned_trials} (cost savings!)")
print(f"Total cost: ${cost_report.total_cost:.2f}")
print(f"Average cost per trial: ${cost_report.avg_cost_per_trial:.2f}")
print(f"Estimated grid search cost: ${cost_report.grid_search_cost_estimate:.2f}")
print(f"Savings vs grid search: ${cost_report.savings:.2f} ({cost_report.savings_percent}%)")

# Visualize optimization
from optuna.visualization import plot_optimization_history, plot_param_importances
plot_optimization_history(study).show()
plot_param_importances(study).show()
```

### Mixed Precision Training (2x Speed on GPUs)
```python
import torch
from torch.cuda.amp import autocast, GradScaler
from model_trainer import PyTorchTrainer

class MixedPrecisionTrainer(PyTorchTrainer):
    """Mixed precision training for 2x speed and 50% memory reduction"""

    def __init__(self, model, optimizer, **kwargs):
        super().__init__(model, optimizer, **kwargs)
        self.scaler = GradScaler()  # For numerical stability
        self.cost_tracker = TrainingCostTracker()

    def train_epoch(self, train_loader):
        self.model.train()
        total_loss = 0

        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.cuda(), target.cuda()

            # Mixed precision training
            with autocast():  # Automatic mixed precision
                output = self.model(data)
                loss = self.criterion(output, target)

            # Scaled backpropagation
            self.optimizer.zero_grad()
            self.scaler.scale(loss).backward()
            self.scaler.step(self.optimizer)
            self.scaler.update()

            total_loss += loss.item()

        return total_loss / len(train_loader)

# Usage
model = MyModel().cuda()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

trainer = MixedPrecisionTrainer(model, optimizer)

# Track training time and cost
with cost_tracker.track_training("mixed_precision_training"):
    for epoch in range(num_epochs):
        train_loss = trainer.train_epoch(train_loader)
        val_loss = trainer.validate(val_loader)

# Compare with FP32 training
report = cost_tracker.compare_precision_modes()
print(f"Mixed precision training time: {report.mixed_time:.2f}s")
print(f"FP32 training time: {report.fp32_time:.2f}s")
print(f"Speedup: {report.speedup:.2f}x")
print(f"Cost savings: ${report.cost_savings:.2f}")
```

### Cost-Tracked Experiment Management
```python
from experiment_tracker import ExperimentTracker
from finops_tracker import ExperimentCostTracker
from datetime import datetime

class CostAwareExperimentTracker:
    """Experiment tracker with integrated cost monitoring"""

    def __init__(self, experiment_name: str):
        self.tracker = ExperimentTracker(experiment_name=experiment_name)
        self.cost_tracker = ExperimentCostTracker()

    def start_run(self, run_name: str, compute_type: str = "cpu"):
        """Start a new run with cost tracking"""

        # Start MLflow run
        self.run = self.tracker.start_run(run_name=run_name)

        # Start cost tracking
        self.cost_tracker.start_tracking(
            run_id=self.run.info.run_id,
            compute_type=compute_type
        )

        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Calculate and log costs
        cost_metrics = self.cost_tracker.stop_tracking()

        # Log cost metrics to MLflow
        self.tracker.log_metrics({
            "compute_cost_usd": cost_metrics.compute_cost,
            "storage_cost_usd": cost_metrics.storage_cost,
            "total_cost_usd": cost_metrics.total_cost,
            "training_duration_seconds": cost_metrics.duration,
            "cost_per_hour": cost_metrics.cost_per_hour
        })

        # Add cost tags
        self.tracker.set_tags({
            "compute_type": cost_metrics.compute_type,
            "instance_type": cost_metrics.instance_type,
            "cost_optimized": str(cost_metrics.compute_type == "spot")
        })

        # End run
        self.tracker.end_run()

# Usage
tracker = CostAwareExperimentTracker("customer_churn")

# Experiment 1: Standard training
with tracker.start_run("baseline_xgboost", compute_type="cpu"):
    model = train_xgboost(X_train, y_train)
    metrics = evaluate(model, X_test, y_test)
    tracker.tracker.log_metrics(metrics)
    tracker.tracker.log_model(model, "xgboost_baseline")

# Experiment 2: GPU training with spot instances
with tracker.start_run("deep_learning_spot", compute_type="spot_gpu"):
    model = train_neural_network(X_train, y_train)
    metrics = evaluate(model, X_test, y_test)
    tracker.tracker.log_metrics(metrics)
    tracker.tracker.log_model(model, "nn_spot")

# Compare experiments by cost and performance
experiments_df = tracker.cost_tracker.compare_experiments()
print(experiments_df[['run_name', 'accuracy', 'total_cost_usd', 'cost_per_point_accuracy']])

# Find most cost-efficient model
best_value = experiments_df['cost_per_point_accuracy'].idxmin()
print(f"\nMost cost-efficient model: {experiments_df.loc[best_value, 'run_name']}")
print(f"Accuracy: {experiments_df.loc[best_value, 'accuracy']:.4f}")
print(f"Cost: ${experiments_df.loc[best_value, 'total_cost_usd']:.2f}")
```

##  CI/CD for Model Training

### Automated Training Pipeline
```yaml
# .github/workflows/model-training.yml
name: Model Training Pipeline

on:
  push:
    paths:
      - 'models/**'
      - 'training/**'
    branches:
      - main
  schedule:
    - cron: '0 3 * * 0'  # Weekly retraining

jobs:
  train-and-evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run unit tests
        run: pytest tests/unit/ --cov=src

      - name: Validate training data
        run: python scripts/validate_training_data.py

      - name: Train model on spot instances
        run: |
          python training/train_model.py \
            --experiment-name "churn_weekly_${{ github.run_number }}" \
            --compute-type spot \
            --max-cost 50.00 \
            --enable-early-stopping

      - name: Run hyperparameter optimization
        if: github.ref == 'refs/heads/main'
        run: |
          python training/optimize_hyperparameters.py \
            --n-trials 30 \
            --optimization-method bayesian \
            --max-cost 100.00

      - name: Evaluate model
        run: |
          python training/evaluate_model.py \
            --min-accuracy 0.85 \
            --min-auc 0.90 \
            --test-fairness

      - name: Generate model card
        run: python scripts/generate_model_card.py

      - name: Register model
        if: success()
        run: python scripts/register_model.py --stage Staging

      - name: Run integration tests
        run: pytest tests/integration/

      - name: Generate training report
        run: python scripts/generate_training_report.py

      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: training-artifacts
          path: |
            outputs/
            reports/
```

##  Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Training Costs** | Cost per training run | <$25 | FinOps tracker |
| | Monthly training budget | <$2000 | Azure Cost Management |
| | Spot instance savings | >70% | Cost tracker |
| | GPU utilization | >80% | Azure Monitor |
| **HPO Costs** | Cost per HPO run | <$100 | HPO cost tracker |
| | Trials pruned (savings) | >40% | Optuna |
| | Bayesian vs grid savings | >80% | Cost comparison |
| **Training Performance** | Training time | <2 hours | Experiment tracker |
| | Model accuracy | >0.85 | MLflow |
| | AUC score | >0.90 | Evaluation metrics |
| **Resource Utilization** | CPU utilization | >70% | Azure Monitor |
| | Memory utilization | >60% | Azure Monitor |
| | Data loading time | <10% total | Profiler |
| **Pipeline Reliability** | Training success rate | >95% | Pipeline metrics |
| | Experiment reproducibility | 100% | Seed + versioning |
| **Model Quality** | Validation score | >baseline | Experiment tracker |
| | Test set performance | >0.85 | Model evaluator |

##  Integration Workflow

### End-to-End Training Pipeline
```
1. Feature Store Access (ml-02)
   ↓
2. Data Validation (de-03)
   ↓
3. Training Data Preparation (ml-03)
   ↓
4. Experiment Initialization (mo-01)
   ↓
5. Hyperparameter Optimization (ml-03)
   ↓
6. Model Training with Cost Tracking (ml-03, fo-07)
   ↓
7. Model Evaluation (ml-03, ds-08)
   ↓
8. Model Versioning (mo-03)
   ↓
9. Model Security Scan (sa-08)
   ↓
10. Model Registration (ml-07)
    ↓
11. Lineage Tracking (mo-06)
    ↓
12. Model Deployment (ml-04)
```

##  Quick Wins

1. **Switch to spot instances** - 60-90% training cost reduction
2. **Use Bayesian optimization** - 80-90% fewer hyperparameter trials
3. **Enable mixed precision training** - 2x speed on GPUs
4. **Implement early stopping** - 20-40% faster training
5. **Cache preprocessed data** - 30-50% faster data loading
6. **Set up experiment tracking** - Better model comparison
7. **Implement checkpointing** - Resilience to preemption
8. **Use learning rate schedules** - Better convergence
9. **Track training costs** - Visibility into spending
10. **Automate model evaluation** - Consistent quality gates
