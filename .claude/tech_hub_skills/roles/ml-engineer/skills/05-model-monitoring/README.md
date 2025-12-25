# Skill 5: Model Monitoring & Drift Detection

## 🎯 Overview
Implement comprehensive model monitoring with data drift, concept drift, and performance degradation detection for production ML systems.

## 🔗 Connections
- **MLOps**: Core monitoring and drift detection capabilities (mo-04, mo-05)
- **ML Engineer**: Monitors deployed models and triggers retraining (ml-04, ml-09)
- **Data Scientist**: Analyzes model degradation patterns (ds-08)
- **DevOps**: Integrates with observability platforms (do-08)
- **FinOps**: Monitors model performance vs cost trade-offs (fo-07)
- **Security Architect**: Detects anomalous predictions (sa-08)
- **Data Engineer**: Monitors data quality for features (de-03)
- **System Design**: Scalable monitoring architecture (sd-08)

## 🛠️ Tools Included

### 1. `drift_detector.py`
Statistical drift detection for features and predictions.

### 2. `model_monitor.py`
Comprehensive model performance monitoring with alerting.

### 3. `prediction_analyzer.py`
Prediction distribution analysis and anomaly detection.

### 4. `monitoring_dashboard.py`
Real-time monitoring dashboards with Grafana/Azure Monitor.

### 5. `alert_manager.py`
Intelligent alerting system for model degradation.

## 🏗️ Monitoring Architecture

```
Production Traffic → Logging → Analysis → Drift Detection → Alerting
                       ↓          ↓            ↓              ↓
                  Predictions  Metrics    Statistics    Notifications
                  Features     Business   Comparison    Auto-retrain
                  Metadata     Technical  Baseline      Dashboards
```

## 🚀 Quick Start

```python
from drift_detector import DriftDetector, KSTest, PSICalculator
from model_monitor import ModelMonitor
from alert_manager import AlertManager

# Initialize drift detector
drift_detector = DriftDetector(
    baseline_data=training_data,
    detection_methods=[
        KSTest(significance_level=0.05),
        PSICalculator(threshold=0.2)
    ]
)

# Initialize model monitor
monitor = ModelMonitor(
    model_name="churn_predictor_v2",
    metrics=["accuracy", "auc", "precision", "recall"],
    alert_thresholds={
        "accuracy": 0.85,
        "auc": 0.90,
        "data_drift_score": 0.2,
        "prediction_drift_score": 0.15
    }
)

# Monitor predictions in production
@monitor.track_predictions
async def predict(features):
    prediction = model.predict(features)

    # Log prediction for monitoring
    monitor.log_prediction(
        features=features,
        prediction=prediction,
        timestamp=datetime.now(),
        metadata={"customer_id": features["customer_id"]}
    )

    return prediction

# Run drift detection (scheduled job)
def check_drift():
    """Daily drift detection job"""

    # Get recent production data
    production_data = monitor.get_recent_predictions(days=7)

    # Detect feature drift
    feature_drift = drift_detector.detect_feature_drift(
        production_data=production_data,
        features=feature_list
    )

    # Detect prediction drift
    prediction_drift = drift_detector.detect_prediction_drift(
        production_predictions=production_data["predictions"],
        baseline_predictions=training_predictions
    )

    # Alert if drift detected
    if feature_drift.has_drift or prediction_drift.has_drift:
        alert_manager.send_alert(
            severity="warning",
            title="Model Drift Detected",
            message=f"Drifted features: {feature_drift.drifted_features}\n"
                    f"Prediction drift score: {prediction_drift.score:.3f}",
            actions=["Review model", "Trigger retraining"]
        )

    # Generate drift report
    drift_report = drift_detector.generate_report(
        feature_drift=feature_drift,
        prediction_drift=prediction_drift
    )

    return drift_report
```

## 📚 Best Practices

### Drift Detection & Monitoring (MLOps Integration)

1. **Multi-Level Drift Detection**
   - Monitor data drift (feature distribution changes)
   - Monitor concept drift (relationship between features and target)
   - Monitor prediction drift (output distribution changes)
   - Monitor performance drift (metric degradation)
   - Reference: MLOps mo-05 (Drift Detection)

2. **Statistical Drift Tests**
   - Use Kolmogorov-Smirnov test for continuous features
   - Use Chi-square test for categorical features
   - Calculate Population Stability Index (PSI)
   - Track Jensen-Shannon divergence
   - Set appropriate significance levels
   - Reference: MLOps mo-05, Data Scientist ds-08

3. **Baseline Comparison**
   - Maintain reference datasets (training data)
   - Update baselines periodically
   - Track distribution shifts over time
   - Document baseline versions
   - Reference: MLOps mo-05, mo-06 (Lineage)

4. **Monitoring Cadence**
   - Real-time monitoring for critical models
   - Hourly/daily drift checks for most models
   - Weekly deep-dive analysis
   - Monthly model review
   - Reference: MLOps mo-04 (Monitoring)

5. **Comprehensive Model Metrics**
   - Track business metrics (revenue impact, user engagement)
   - Monitor technical metrics (accuracy, AUC, F1)
   - Track operational metrics (latency, throughput)
   - Monitor data quality metrics
   - Reference: MLOps mo-04

### DevOps Integration for Monitoring

6. **Observability Integration**
   - Integrate with Azure Monitor / App Insights
   - Use OpenTelemetry for instrumentation
   - Centralize logs and metrics
   - Implement distributed tracing
   - Reference: DevOps do-08 (Monitoring)

7. **Alerting & Incident Response**
   - Set up intelligent alerting (avoid alert fatigue)
   - Define alert severity levels
   - Implement escalation policies
   - Automate incident response
   - Reference: DevOps do-08

8. **Monitoring Dashboards**
   - Build real-time monitoring dashboards
   - Visualize drift metrics over time
   - Track model performance trends
   - Enable team collaboration
   - Reference: DevOps do-08, MLOps mo-04

### Cost Optimization for Monitoring (FinOps Integration)

9. **Efficient Logging Strategy**
   - Sample predictions for monitoring (not 100%)
   - Implement tiered logging (critical vs routine)
   - Compress and archive old logs
   - Monitor log storage costs
   - Reference: FinOps fo-05 (Storage), fo-07 (AI/ML Cost)

10. **Optimize Monitoring Compute**
    - Run drift detection on scheduled batches
    - Use serverless for event-driven monitoring
    - Right-size monitoring infrastructure
    - Cache expensive drift calculations
    - Reference: FinOps fo-06 (Compute Optimization)

11. **Monitoring Cost Tracking**
    - Track monitoring infrastructure costs
    - Monitor log ingestion costs
    - Optimize retention policies
    - Balance cost vs visibility
    - Reference: FinOps fo-01 (Cost Monitoring)

### Automated Response & Retraining

12. **Automated Drift Response**
    - Auto-alert when drift exceeds thresholds
    - Trigger model investigation workflows
    - Initiate automated retraining pipelines
    - Implement automatic rollback if needed
    - Reference: MLOps mo-05, ML Engineer ml-09

13. **Model Retraining Triggers**
    - Performance degradation thresholds
    - Significant data drift detected
    - Concept drift indicators
    - Scheduled periodic retraining
    - Reference: ML Engineer ml-09 (Continuous Retraining)

### Data Quality Monitoring

14. **Feature Quality Checks**
    - Monitor feature completeness
    - Detect feature value range violations
    - Track feature correlation changes
    - Alert on missing features
    - Reference: Data Engineer de-03 (Data Quality)

15. **Input Validation Monitoring**
    - Track invalid input rates
    - Monitor schema violations
    - Detect data type mismatches
    - Alert on data quality issues
    - Reference: Data Engineer de-03

### Security & Anomaly Detection

16. **Prediction Anomaly Detection**
    - Detect unusual prediction patterns
    - Identify potential model attacks
    - Monitor for adversarial inputs
    - Alert on suspicious behavior
    - Reference: Security Architect sa-08 (LLM Security)

17. **Model Behavior Monitoring**
    - Track prediction confidence scores
    - Monitor prediction uncertainty
    - Detect model degradation patterns
    - Identify edge cases
    - Reference: MLOps mo-04, Security Architect sa-08

### Azure-Specific Best Practices

18. **Azure Monitor Integration**
    - Use Azure Monitor for metrics
    - Enable Application Insights
    - Set up Log Analytics workspaces
    - Configure metric alerts
    - Reference: Azure az-04 (AI/ML Services)

19. **Azure ML Model Monitoring**
    - Enable model data collection
    - Configure data drift detection
    - Use built-in monitoring dashboards
    - Integrate with Azure Monitor
    - Reference: Azure az-04

20. **Cost-Effective Monitoring**
    - Use log sampling for high-volume models
    - Implement retention policies
    - Archive to cold storage
    - Monitor monitoring costs
    - Reference: Azure az-04, FinOps fo-05

## 💰 Cost Optimization Examples

### Intelligent Prediction Logging
```python
from model_monitor import SmartLogger
from finops_tracker import MonitoringCostTracker
import random

class CostOptimizedMonitor:
    """Cost-optimized prediction logging with sampling"""

    def __init__(self, model_name: str, sampling_rate: float = 0.1):
        self.model_name = model_name
        self.sampling_rate = sampling_rate  # Log 10% of predictions
        self.logger = SmartLogger(model_name)
        self.cost_tracker = MonitoringCostTracker()

        # Always log certain predictions
        self.always_log_conditions = [
            lambda pred: pred["confidence"] < 0.5,  # Low confidence
            lambda pred: pred["value"] > 0.9,        # High risk
            lambda pred: pred.get("is_edge_case", False)  # Edge cases
        ]

    def should_log_prediction(self, prediction: dict) -> bool:
        """Intelligent sampling decision"""

        # Always log important predictions
        for condition in self.always_log_conditions:
            if condition(prediction):
                return True

        # Sample remaining predictions
        return random.random() < self.sampling_rate

    async def log_prediction(
        self,
        features: dict,
        prediction: dict,
        metadata: dict
    ):
        """Log prediction with cost optimization"""

        if not self.should_log_prediction(prediction):
            self.cost_tracker.record_skipped_log()
            return

        # Log to monitoring system
        with self.cost_tracker.track_logging_cost():
            await self.logger.log(
                timestamp=datetime.now(),
                features=features,
                prediction=prediction,
                metadata=metadata,
                # Compress large payloads
                compress=len(str(features)) > 1000
            )

        self.cost_tracker.record_logged_prediction()

    def get_cost_report(self):
        """Monitoring cost analysis"""
        report = self.cost_tracker.generate_report()

        print(f"Monitoring Cost Report:")
        print(f"Total predictions: {report.total_predictions:,}")
        print(f"Logged predictions: {report.logged_predictions:,}")
        print(f"Sampling rate: {report.actual_sampling_rate:.1%}")
        print(f"Log storage cost: ${report.storage_cost:.2f}")
        print(f"Log ingestion cost: ${report.ingestion_cost:.2f}")
        print(f"Total monitoring cost: ${report.total_cost:.2f}")
        print(f"Cost per logged prediction: ${report.cost_per_log:.4f}")
        print(f"Savings from sampling: ${report.sampling_savings:.2f}")

        return report

# Usage
monitor = CostOptimizedMonitor(
    model_name="churn_predictor_v2",
    sampling_rate=0.1  # Log 10% + important predictions
)

# In production
for prediction_request in prediction_stream:
    features = prediction_request.features
    prediction = model.predict(features)

    await monitor.log_prediction(
        features=features,
        prediction=prediction,
        metadata={"customer_id": prediction_request.customer_id}
    )

# Monitor costs
monthly_report = monitor.get_cost_report()

# Expected results:
# - 90% reduction in logging costs
# - Still captures all important events
# - Sufficient data for drift detection
```

### Efficient Drift Detection
```python
from drift_detector import BatchDriftDetector
from scipy import stats
import numpy as np
from finops_tracker import DriftCostTracker

class CostOptimizedDriftDetection:
    """Efficient drift detection with cost optimization"""

    def __init__(self, baseline_data: pd.DataFrame):
        self.baseline_data = baseline_data
        self.detector = BatchDriftDetector()
        self.cost_tracker = DriftCostTracker()

        # Pre-compute baseline statistics (one-time cost)
        self.baseline_stats = self._compute_baseline_stats()

    def _compute_baseline_stats(self):
        """Pre-compute baseline statistics for efficiency"""
        stats = {}

        for column in self.baseline_data.columns:
            if self.baseline_data[column].dtype in ['float64', 'int64']:
                stats[column] = {
                    'mean': self.baseline_data[column].mean(),
                    'std': self.baseline_data[column].std(),
                    'min': self.baseline_data[column].min(),
                    'max': self.baseline_data[column].max(),
                    'quantiles': self.baseline_data[column].quantile([0.25, 0.5, 0.75]).to_dict(),
                    'distribution': self.baseline_data[column].values
                }
            else:
                stats[column] = {
                    'value_counts': self.baseline_data[column].value_counts().to_dict(),
                    'unique_values': set(self.baseline_data[column].unique())
                }

        return stats

    def detect_drift_efficient(
        self,
        production_data: pd.DataFrame,
        features: list = None,
        method: str = "ks_test"
    ) -> dict:
        """Efficient drift detection using pre-computed statistics"""

        with self.cost_tracker.track_drift_detection():
            drift_results = {}
            features = features or production_data.columns

            for feature in features:
                if feature not in self.baseline_stats:
                    continue

                baseline_values = self.baseline_stats[feature]['distribution']
                production_values = production_data[feature].values

                # Use cached baseline statistics
                if method == "ks_test":
                    # Kolmogorov-Smirnov test (efficient)
                    statistic, p_value = stats.ks_2samp(
                        baseline_values,
                        production_values
                    )
                    has_drift = p_value < 0.05

                elif method == "psi":
                    # Population Stability Index (very efficient)
                    psi_score = self._calculate_psi_efficient(
                        baseline_values,
                        production_values
                    )
                    has_drift = psi_score > 0.2
                    statistic = psi_score
                    p_value = None

                drift_results[feature] = {
                    'has_drift': has_drift,
                    'statistic': statistic,
                    'p_value': p_value,
                    'drift_magnitude': abs(
                        production_values.mean() - baseline_values.mean()
                    ) / baseline_values.std() if baseline_values.std() > 0 else 0
                }

        # Cost report
        cost_report = self.cost_tracker.get_detection_cost()
        print(f"Drift detection cost: ${cost_report.cost:.4f}")
        print(f"Detection time: {cost_report.duration_ms:.2f}ms")

        return {
            'drift_results': drift_results,
            'drifted_features': [f for f, r in drift_results.items() if r['has_drift']],
            'drift_score': np.mean([r['drift_magnitude'] for r in drift_results.values()]),
            'cost': cost_report.cost
        }

    def _calculate_psi_efficient(
        self,
        baseline: np.ndarray,
        production: np.ndarray,
        bins: int = 10
    ) -> float:
        """Efficient PSI calculation"""

        # Create bins from baseline
        bin_edges = np.percentile(baseline, np.linspace(0, 100, bins + 1))
        bin_edges[0] = -np.inf
        bin_edges[-1] = np.inf

        # Calculate distributions
        baseline_dist = np.histogram(baseline, bins=bin_edges)[0] / len(baseline)
        production_dist = np.histogram(production, bins=bin_edges)[0] / len(production)

        # PSI calculation
        psi = np.sum(
            (production_dist - baseline_dist) * np.log(
                (production_dist + 1e-10) / (baseline_dist + 1e-10)
            )
        )

        return psi

    def incremental_drift_monitoring(
        self,
        data_stream,
        window_size: int = 1000,
        check_frequency: int = 100
    ):
        """Incremental drift detection for streaming data"""

        buffer = []
        check_count = 0

        for record in data_stream:
            buffer.append(record)

            # Check drift every N records
            if len(buffer) >= check_frequency:
                check_count += 1

                # Convert to DataFrame
                production_sample = pd.DataFrame(buffer[-window_size:])

                # Run efficient drift detection
                drift_result = self.detect_drift_efficient(
                    production_data=production_sample,
                    method="psi"  # Faster than KS test
                )

                # Alert if drift detected
                if drift_result['drifted_features']:
                    print(f"\nDrift detected at check #{check_count}:")
                    print(f"Drifted features: {drift_result['drifted_features']}")
                    print(f"Drift score: {drift_result['drift_score']:.3f}")

                # Clear old records from buffer
                buffer = buffer[-window_size:]

# Usage
drift_detector = CostOptimizedDriftDetection(
    baseline_data=training_data
)

# Batch drift detection (daily job)
production_data = get_recent_predictions(days=7)
drift_result = drift_detector.detect_drift_efficient(
    production_data=production_data,
    method="psi"  # 10x faster than KS test
)

print(f"Drift detection completed in {drift_result['cost']:.4f}s")
print(f"Drifted features: {drift_result['drifted_features']}")

# Streaming drift detection
drift_detector.incremental_drift_monitoring(
    data_stream=prediction_stream,
    window_size=1000,
    check_frequency=100
)
```

### Automated Drift Response
```python
from alert_manager import AlertManager, AlertSeverity
from model_retrainer import AutoRetrainer
from drift_detector import DriftAnalyzer

class AutomatedDriftResponse:
    """Automated drift detection and response system"""

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.drift_analyzer = DriftAnalyzer(model_name)
        self.alert_manager = AlertManager()
        self.retrainer = AutoRetrainer(model_name)

        # Configure drift response thresholds
        self.thresholds = {
            "minor_drift": 0.1,      # Warning alert
            "moderate_drift": 0.2,   # Trigger investigation
            "severe_drift": 0.3      # Auto-retrain
        }

    async def monitor_and_respond(self):
        """Continuous drift monitoring with automated response"""

        # Get recent production data
        production_data = await self.get_production_data(days=7)

        # Detect drift
        drift_result = self.drift_analyzer.analyze_drift(
            production_data=production_data,
            features=feature_list
        )

        drift_score = drift_result['drift_score']
        drifted_features = drift_result['drifted_features']

        # Automated response based on severity
        if drift_score >= self.thresholds["severe_drift"]:
            # Severe drift - auto-retrain
            await self._handle_severe_drift(drift_result)

        elif drift_score >= self.thresholds["moderate_drift"]:
            # Moderate drift - trigger investigation
            await self._handle_moderate_drift(drift_result)

        elif drift_score >= self.thresholds["minor_drift"]:
            # Minor drift - warning alert
            await self._handle_minor_drift(drift_result)

        return drift_result

    async def _handle_severe_drift(self, drift_result):
        """Handle severe drift with auto-retraining"""

        # Send critical alert
        await self.alert_manager.send_alert(
            severity=AlertSeverity.CRITICAL,
            title=f"Severe Drift Detected - Auto-Retraining Initiated",
            message=f"Model: {self.model_name}\n"
                    f"Drift score: {drift_result['drift_score']:.3f}\n"
                    f"Drifted features: {drift_result['drifted_features']}\n"
                    f"Action: Automatic retraining initiated",
            channels=["slack", "email", "pagerduty"]
        )

        # Trigger automated retraining
        retrain_job = await self.retrainer.trigger_retraining(
            reason="severe_drift_detected",
            drift_score=drift_result['drift_score'],
            drifted_features=drift_result['drifted_features'],
            priority="high"
        )

        print(f"Retraining job initiated: {retrain_job.id}")

    async def _handle_moderate_drift(self, drift_result):
        """Handle moderate drift with investigation workflow"""

        # Send warning alert
        await self.alert_manager.send_alert(
            severity=AlertSeverity.WARNING,
            title=f"Moderate Drift Detected - Investigation Required",
            message=f"Model: {self.model_name}\n"
                    f"Drift score: {drift_result['drift_score']:.3f}\n"
                    f"Drifted features: {drift_result['drifted_features']}\n"
                    f"Action: Please investigate and determine if retraining is needed",
            channels=["slack", "email"],
            actions=[
                {"label": "Trigger Retraining", "action": "retrain"},
                {"label": "Acknowledge", "action": "ack"},
                {"label": "View Dashboard", "action": "dashboard"}
            ]
        )

        # Create investigation ticket
        await self.alert_manager.create_investigation_ticket(
            title=f"Model Drift Investigation - {self.model_name}",
            description=drift_result,
            assignee="ml-ops-team"
        )

    async def _handle_minor_drift(self, drift_result):
        """Handle minor drift with monitoring"""

        # Send info alert
        await self.alert_manager.send_alert(
            severity=AlertSeverity.INFO,
            title=f"Minor Drift Detected",
            message=f"Model: {self.model_name}\n"
                    f"Drift score: {drift_result['drift_score']:.3f}\n"
                    f"Drifted features: {drift_result['drifted_features']}\n"
                    f"Action: Continuing to monitor",
            channels=["slack"]
        )

        # Log to dashboard
        await self.drift_analyzer.log_drift_event(drift_result)

# Usage (scheduled job)
drift_responder = AutomatedDriftResponse(model_name="churn_predictor_v2")

# Run daily
async def daily_drift_check():
    result = await drift_responder.monitor_and_respond()
    print(f"Drift check completed. Score: {result['drift_score']:.3f}")

# Schedule with APScheduler or similar
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()
scheduler.add_job(daily_drift_check, 'cron', hour=2)  # Run at 2 AM daily
scheduler.start()
```

## 🚀 Monitoring Dashboards

### Grafana Dashboard Configuration
```python
# monitoring_dashboard.py
from grafana_api import GrafanaDashboard
from azure.monitor import MetricsClient

def create_model_monitoring_dashboard(model_name: str):
    """Create comprehensive model monitoring dashboard"""

    dashboard = GrafanaDashboard(
        title=f"Model Monitoring - {model_name}",
        refresh="30s"
    )

    # Row 1: Model Performance Metrics
    dashboard.add_row("Model Performance")
    dashboard.add_panel(
        title="Model Accuracy (7d rolling)",
        query="avg(model_accuracy{model_name='" + model_name + "'})",
        panel_type="graph",
        threshold=0.85,
        alert_condition="below"
    )
    dashboard.add_panel(
        title="AUC Score",
        query="avg(model_auc{model_name='" + model_name + "'})",
        panel_type="gauge",
        thresholds=[0.80, 0.90, 0.95]
    )

    # Row 2: Drift Metrics
    dashboard.add_row("Drift Detection")
    dashboard.add_panel(
        title="Feature Drift Score",
        query="max(feature_drift_score{model_name='" + model_name + "'})",
        panel_type="graph",
        threshold=0.2,
        alert_condition="above"
    )
    dashboard.add_panel(
        title="Prediction Drift Score",
        query="max(prediction_drift_score{model_name='" + model_name + "'})",
        panel_type="graph",
        threshold=0.15
    )
    dashboard.add_panel(
        title="Drifted Features Count",
        query="count(drifted_features{model_name='" + model_name + "'})",
        panel_type="stat"
    )

    # Row 3: Operational Metrics
    dashboard.add_row("Operational Metrics")
    dashboard.add_panel(
        title="Prediction Latency (p95)",
        query="histogram_quantile(0.95, prediction_latency{model_name='" + model_name + "'})",
        panel_type="graph",
        threshold=100,
        unit="ms"
    )
    dashboard.add_panel(
        title="Requests per Minute",
        query="rate(prediction_requests{model_name='" + model_name + "'}[1m])",
        panel_type="graph"
    )
    dashboard.add_panel(
        title="Error Rate",
        query="rate(prediction_errors{model_name='" + model_name + "'}[5m])",
        panel_type="graph",
        threshold=0.01,
        alert_condition="above"
    )

    # Row 4: Data Quality
    dashboard.add_row("Data Quality")
    dashboard.add_panel(
        title="Feature Completeness",
        query="avg(feature_completeness{model_name='" + model_name + "'})",
        panel_type="gauge",
        thresholds=[0.95, 0.99, 1.0]
    )
    dashboard.add_panel(
        title="Invalid Inputs Rate",
        query="rate(invalid_inputs{model_name='" + model_name + "'}[5m])",
        panel_type="graph"
    )

    # Row 5: Cost Metrics
    dashboard.add_row("Cost & Resource Usage")
    dashboard.add_panel(
        title="Daily Serving Cost",
        query="sum(serving_cost_usd{model_name='" + model_name + "'})",
        panel_type="stat",
        unit="currencyUSD"
    )
    dashboard.add_panel(
        title="Cost per 1000 Predictions",
        query="serving_cost_usd{model_name='" + model_name + "'} / prediction_count * 1000",
        panel_type="graph",
        unit="currencyUSD"
    )

    # Save dashboard
    dashboard.save()
    return dashboard

# Create dashboard
dashboard = create_model_monitoring_dashboard("churn_predictor_v2")
print(f"Dashboard created: {dashboard.url}")
```

## 📊 Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Drift Detection** | Feature drift score | <0.2 | Drift detector |
| | Prediction drift score | <0.15 | Drift detector |
| | Drifted features count | <3 | KS/PSI tests |
| | Drift check frequency | Daily | Scheduler |
| **Model Performance** | Production accuracy | >0.85 | Model monitor |
| | Production AUC | >0.90 | Model monitor |
| | Performance vs baseline | >95% | Comparison |
| **Data Quality** | Feature completeness | >99% | Quality checker |
| | Invalid input rate | <1% | Validator |
| | Missing feature rate | <0.1% | Monitor |
| **Monitoring Costs** | Log storage cost | <$100/mo | FinOps tracker |
| | Monitoring compute | <$50/mo | Cost tracker |
| | Alert notification cost | <$20/mo | Alert manager |
| **Operational** | Alert response time | <30 min | SLA monitor |
| | False alert rate | <5% | Alert tuning |
| | Dashboard load time | <2s | Performance |

## 🔄 Integration Workflow

### End-to-End Monitoring Pipeline
```
1. Production Predictions (ml-04)
   ↓
2. Intelligent Logging (ml-05)
   ↓
3. Data Aggregation (ml-05)
   ↓
4. Drift Detection (mo-05)
   ↓
5. Performance Monitoring (mo-04)
   ↓
6. Anomaly Detection (ml-05)
   ↓
7. Alert Generation (ml-05)
   ↓
8. Dashboard Updates (do-08)
   ↓
9. Investigation Workflow (ml-05)
   ↓
10. Auto-Retraining Trigger (ml-09)
    ↓
11. Cost Tracking (fo-07)
```

## 🎯 Quick Wins

1. **Enable prediction logging** - Visibility into production behavior
2. **Set up drift detection** - Early warning for model degradation
3. **Create monitoring dashboards** - Real-time visibility
4. **Implement intelligent sampling** - 90% reduction in logging costs
5. **Configure performance alerts** - Proactive issue detection
6. **Use PSI for drift** - 10x faster than KS test
7. **Pre-compute baseline stats** - Faster drift detection
8. **Set up automated alerts** - Faster incident response
9. **Track monitoring costs** - Optimize monitoring spend
10. **Implement auto-retraining** - Automated drift response
