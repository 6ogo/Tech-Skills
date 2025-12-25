# Skill 2: Feature Engineering & Feature Store

## 🎯 Overview
Build scalable feature engineering pipelines with centralized feature stores for consistency across training and serving.

## 🔗 Connections
- **Data Engineer**: Consumes data pipelines for feature creation (de-01, de-02, de-03)
- **Data Scientist**: Provides features for experimentation (ds-01, ds-02, ds-05)
- **MLOps**: Feature versioning and lineage tracking (mo-02, mo-06)
- **ML Engineer**: Feeds features to training pipelines (ml-01, ml-03)
- **FinOps**: Optimizes feature computation and storage costs (fo-05, fo-07)
- **DevOps**: Automates feature pipeline deployment (do-01, do-04)
- **Security Architect**: Ensures feature-level access controls (sa-02, sa-06)
- **System Design**: Scalable feature serving architecture (sd-03, sd-05)

## 🛠️ Tools Included

### 1. `feature_store_manager.py`
Centralized feature store with versioning and lineage.

### 2. `feature_transformer.py`
Reusable feature transformations with sklearn/pandas patterns.

### 3. `feature_validator.py`
Data quality checks and feature drift detection.

### 4. `online_feature_server.py`
Low-latency feature serving for real-time inference.

### 5. `feature_store_config.yaml`
Configuration templates for feature store infrastructure.

## 🏗️ Feature Store Architecture

```
Raw Data → Feature Engineering → Feature Store → Training/Serving
                ↓                       ↓              ↓
         Transformations          Versioning     Low-latency
         Validation              Lineage        Online/Offline
         Testing                 Reusability    Consistency
```

## 🚀 Quick Start

```python
from feature_store_manager import FeatureStore
from feature_transformer import FeatureEngineering

# Initialize feature store
store = FeatureStore(
    name="customer_features",
    backend="azure_ml"  # or "feast", "tecton"
)

# Define feature transformations
engineer = FeatureEngineering()

# Create feature group
features = engineer.create_features(
    source_table="bronze.customer_events",
    transformations=[
        engineer.aggregate("purchases", window="30d", agg=["sum", "count", "mean"]),
        engineer.categorical_encode("customer_segment"),
        engineer.time_features("last_activity_date"),
        engineer.ratio("purchase_amount", "page_views")
    ]
)

# Register in feature store
store.register_features(
    feature_group="customer_behavior",
    features=features,
    version="v1",
    description="Customer behavior features for churn prediction"
)

# Get features for training
training_data = store.get_historical_features(
    feature_refs=["customer_behavior:v1"],
    entity_df=training_entities,
    point_in_time="event_timestamp"
)

# Get features for online serving
online_features = store.get_online_features(
    feature_refs=["customer_behavior:v1"],
    entity_keys={"customer_id": "12345"}
)
```

## 📚 Best Practices

### Feature Engineering Cost Optimization (FinOps Integration)

1. **Optimize Feature Computation Costs**
   - Compute features incrementally, not full refresh
   - Cache frequently used feature transformations
   - Use materialized views for expensive aggregations
   - Schedule batch feature updates during off-peak hours
   - Reference: FinOps fo-07 (AI/ML Cost), fo-05 (Storage)

2. **Storage Cost Optimization**
   - Implement feature lifecycle policies
   - Archive old feature versions to cold storage
   - Compress feature data (Parquet with snappy)
   - Monitor feature store storage costs
   - Delete unused feature groups
   - Reference: FinOps fo-05 (Storage Optimization)

3. **Compute Resource Optimization**
   - Right-size Spark clusters for feature computation
   - Use auto-scaling for variable workloads
   - Optimize Spark jobs (partitioning, broadcast joins)
   - Track cost per feature group
   - Reference: FinOps fo-06 (Compute Optimization)

4. **Online Serving Cost Optimization**
   - Implement feature caching (Redis)
   - Use connection pooling
   - Batch feature requests when possible
   - Monitor serving QPS and costs
   - Auto-scale online store based on traffic
   - Reference: FinOps fo-06, fo-07

5. **Feature Reusability for Cost Savings**
   - Centralize features to avoid duplication
   - Track feature usage across models
   - Deprecate unused features
   - Share features across teams
   - Reference: MLOps mo-02 (Feature Store)

### MLOps Integration for Features

6. **Feature Versioning & Lineage**
   - Version all feature definitions
   - Track feature lineage (source data → transformations → features)
   - Document feature meanings and calculations
   - Maintain backward compatibility
   - Reference: MLOps mo-02 (Feature Store), mo-06 (Lineage)

7. **Feature Monitoring & Drift Detection**
   - Monitor feature distributions in production
   - Detect feature drift vs training data
   - Track feature nullability and cardinality
   - Alert on feature quality issues
   - Reference: MLOps mo-04 (Monitoring), mo-05 (Drift Detection)

8. **Training-Serving Consistency**
   - Use same feature code for training and serving
   - Prevent training-serving skew
   - Implement point-in-time correctness
   - Test feature consistency rigorously
   - Reference: MLOps mo-02, ML Engineer best practices

### DevOps Integration for Features

9. **CI/CD for Feature Pipelines**
   - Automate feature pipeline deployment
   - Run feature validation tests before deployment
   - Version control all feature code
   - Implement feature rollback mechanisms
   - Reference: DevOps do-01 (CI/CD), do-06 (Deployment)

10. **Infrastructure as Code**
    - Deploy feature store with Terraform
    - Automate feature pipeline infrastructure
    - Version all infrastructure configs
    - Implement disaster recovery
    - Reference: DevOps do-04 (IaC)

11. **Monitoring & Observability**
    - Instrument feature pipelines with metrics
    - Track feature computation latency
    - Monitor feature serving performance
    - Set up alerts for pipeline failures
    - Reference: DevOps do-08 (Monitoring)

### Data Quality & Validation

12. **Feature Validation**
    - Validate feature schema before registration
    - Check feature distributions and ranges
    - Detect outliers and anomalies
    - Ensure data completeness
    - Reference: Data Engineer de-03 (Data Quality)

13. **Feature Testing**
    - Unit test feature transformations
    - Integration test feature pipelines
    - Test training-serving consistency
    - Validate point-in-time correctness
    - Reference: DevOps do-01 (CI/CD)

### Security & Compliance

14. **Feature-Level Access Control**
    - Implement RBAC for feature groups
    - Restrict access to sensitive features (PII)
    - Audit feature access logs
    - Encrypt features at rest and in transit
    - Reference: Security Architect sa-02 (IAM), sa-06 (Governance)

15. **PII Handling in Features**
    - Detect and mask PII in features
    - Use feature hashing for sensitive data
    - Implement differential privacy where needed
    - Document data sensitivity levels
    - Reference: Security Architect sa-01 (PII Detection)

### Azure-Specific Best Practices

16. **Azure ML Feature Store**
    - Use managed feature store for simplicity
    - Integrate with Azure ML datasets
    - Enable offline and online stores
    - Use Azure Cache for Redis for online serving
    - Reference: Azure az-04 (AI/ML Services)

17. **Azure Synapse for Feature Engineering**
    - Use Synapse Spark for large-scale transformations
    - Implement serverless SQL for feature queries
    - Optimize Synapse costs with auto-pause
    - Reference: Azure az-01 (Data Services)

### Data Engineer Integration

18. **Feature Pipeline Orchestration**
    - Integrate with data pipelines (Databricks, ADF)
    - Schedule feature updates appropriately
    - Handle upstream data dependencies
    - Implement incremental feature updates
    - Reference: Data Engineer de-01 (Pipeline Orchestration)

19. **Data Quality for Features**
    - Validate source data before feature computation
    - Monitor data freshness for features
    - Handle missing data appropriately
    - Track data lineage from source to features
    - Reference: Data Engineer de-03 (Data Quality)

20. **Feature Discovery & Documentation**
    - Maintain feature catalog with descriptions
    - Document feature creation logic
    - Track feature owners and SLAs
    - Enable feature search and discovery
    - Reference: MLOps mo-02, Data Engineer best practices

## 💰 Cost Optimization Examples

### Incremental Feature Computation
```python
from feature_store_manager import FeatureStore
from finops_tracker import FeatureCostTracker

store = FeatureStore(name="customer_features")
cost_tracker = FeatureCostTracker()

@cost_tracker.track_feature_cost
def compute_features_incremental(last_processed_timestamp):
    """Compute only new features since last run (saves 80-95% compute costs)"""

    # Read only new data
    new_data = spark.read.parquet("bronze.events") \
        .filter(f"event_timestamp > '{last_processed_timestamp}'")

    # Incremental aggregations
    new_features = new_data.groupBy("customer_id").agg(
        count("*").alias("event_count_30d"),
        sum("purchase_amount").alias("total_purchase_30d"),
        avg("session_duration").alias("avg_session_duration")
    )

    # Merge with existing features
    existing_features = store.get_latest_features("customer_behavior")
    updated_features = existing_features.merge(
        new_features,
        on="customer_id",
        how="outer"
    )

    # Write to feature store
    store.write_features(
        feature_group="customer_behavior",
        features=updated_features,
        mode="overwrite"
    )

    return updated_features

# Run incremental update
last_run = store.get_last_update_time("customer_behavior")
compute_features_incremental(last_run)

# Cost report
report = cost_tracker.generate_report()
print(f"Feature computation cost: ${report.compute_cost:.2f}")
print(f"Storage cost: ${report.storage_cost:.2f}")
print(f"Savings from incremental: ${report.full_refresh_cost - report.compute_cost:.2f}")
```

### Feature Store with Cost-Optimized Storage
```python
from azure.ai.ml.entities import FeatureStore, FeatureSet
from datetime import timedelta

# Create feature store with lifecycle management
feature_store = FeatureStore(
    name="ml-feature-store",
    description="Centralized feature store with cost optimization",
    offline_store={
        "type": "azure_data_lake_gen2",
        "storage_account": "mlfeaturestore",
        "container": "features",
        "format": "parquet",
        "compression": "snappy",  # 3-5x compression
        "partition_by": ["year", "month", "day"]  # Partition pruning
    },
    online_store={
        "type": "azure_cache_redis",
        "tier": "Basic",  # Upgrade to Premium for production
        "capacity": 1,
        "ttl": 3600,  # 1 hour cache
        "enable_clustering": False  # Enable for high throughput
    }
)

# Define feature set with lifecycle policy
feature_set = FeatureSet(
    name="customer_behavior",
    version="v1",
    description="Customer behavior features",
    entities=["customer_id"],
    features=[
        {"name": "purchase_count_7d", "type": "integer"},
        {"name": "total_spend_30d", "type": "float"},
        {"name": "avg_session_duration", "type": "float"},
        {"name": "last_purchase_days_ago", "type": "integer"}
    ],
    # Lifecycle management for cost savings
    lifecycle_policy={
        "hot_tier_retention_days": 30,     # Recent data in premium storage
        "cool_tier_retention_days": 90,    # 50% cheaper
        "archive_tier_retention_days": 365, # 90% cheaper
        "delete_after_days": 730           # Compliance requirement
    }
)

# Track feature usage and costs
feature_set.enable_usage_tracking(True)
feature_set.enable_cost_tracking(True)

# Register feature set
ml_client.feature_sets.create_or_update(feature_set)
```

### Low-Latency Online Feature Serving
```python
from online_feature_server import OnlineFeatureServer
from azure.core.credentials import AzureKeyCredential
import redis
from functools import lru_cache

class OptimizedFeatureServer:
    def __init__(self):
        # Redis cache for features (sub-millisecond latency)
        self.cache = redis.Redis(
            host="ml-features.redis.cache.windows.net",
            port=6380,
            password=os.getenv("REDIS_PASSWORD"),
            ssl=True,
            decode_responses=True,
            # Connection pooling for efficiency
            connection_pool=redis.ConnectionPool(max_connections=50)
        )

        self.feature_store = FeatureStore(name="customer_features")
        self.cost_tracker = FeatureCostTracker()

    @lru_cache(maxsize=1000)  # In-memory cache for hot features
    def get_features(self, customer_id: str, feature_list: list) -> dict:
        """Get features with multi-level caching"""

        cache_key = f"features:{customer_id}:{':'.join(feature_list)}"

        # Level 1: In-memory cache (LRU)
        # Handled by @lru_cache decorator

        # Level 2: Redis cache
        cached = self.cache.get(cache_key)
        if cached:
            self.cost_tracker.record_cache_hit("redis")
            return json.loads(cached)

        # Level 3: Feature store (fallback)
        features = self.feature_store.get_online_features(
            feature_refs=feature_list,
            entity_keys={"customer_id": customer_id}
        )

        # Update cache with 1-hour TTL
        self.cache.setex(
            cache_key,
            timedelta(hours=1),
            json.dumps(features)
        )

        self.cost_tracker.record_cache_miss()
        return features

    def batch_get_features(self, customer_ids: list, feature_list: list) -> dict:
        """Batch feature retrieval for cost efficiency"""

        # Use Redis pipeline for bulk operations (10x faster)
        pipeline = self.cache.pipeline()
        cache_keys = [
            f"features:{cid}:{':'.join(feature_list)}"
            for cid in customer_ids
        ]

        for key in cache_keys:
            pipeline.get(key)

        cached_results = pipeline.execute()

        # Fetch missing features in bulk
        missing_ids = [
            customer_ids[i]
            for i, result in enumerate(cached_results)
            if result is None
        ]

        if missing_ids:
            # Bulk fetch from feature store
            missing_features = self.feature_store.get_online_features_batch(
                feature_refs=feature_list,
                entity_keys=[{"customer_id": cid} for cid in missing_ids]
            )

            # Bulk cache update
            pipeline = self.cache.pipeline()
            for cid, features in zip(missing_ids, missing_features):
                cache_key = f"features:{cid}:{':'.join(feature_list)}"
                pipeline.setex(cache_key, timedelta(hours=1), json.dumps(features))
            pipeline.execute()

        return {
            "cache_hit_rate": 1 - len(missing_ids) / len(customer_ids),
            "features": cached_results
        }

# Usage
server = OptimizedFeatureServer()

# Single feature request (< 5ms with cache)
features = server.get_features(
    customer_id="12345",
    feature_list=["customer_behavior:v1"]
)

# Batch request (100x more efficient)
batch_features = server.batch_get_features(
    customer_ids=["12345", "67890", "11111"],
    feature_list=["customer_behavior:v1"]
)
```

### Cost-Optimized Feature Computation with Spark
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

def optimize_spark_feature_computation():
    """Optimized Spark configuration for feature engineering"""

    spark = SparkSession.builder \
        .appName("FeatureEngineering") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .config("spark.dynamicAllocation.enabled", "true") \
        .config("spark.dynamicAllocation.minExecutors", "1") \
        .config("spark.dynamicAllocation.maxExecutors", "10") \
        .config("spark.sql.shuffle.partitions", "auto") \
        .config("spark.executor.instances", "auto") \
        .getOrCreate()

    # Read data with partition pruning
    events = spark.read.parquet("bronze.customer_events") \
        .filter(col("event_date") >= date_sub(current_date(), 30))  # Last 30 days only

    # Broadcast small dimension tables
    customer_dim = spark.read.parquet("gold.customer_dim")
    broadcast_customers = broadcast(customer_dim)  # Avoid shuffle

    # Efficient window functions with partition and ordering
    window_7d = Window.partitionBy("customer_id").orderBy("event_timestamp").rowsBetween(-6, 0)
    window_30d = Window.partitionBy("customer_id").orderBy("event_timestamp").rowsBetween(-29, 0)

    # Compute features efficiently
    features = events.join(broadcast_customers, "customer_id", "left") \
        .groupBy("customer_id") \
        .agg(
            # Aggregations
            count("*").alias("event_count_30d"),
            sum(when(col("event_type") == "purchase", 1).otherwise(0)).alias("purchase_count_30d"),
            sum("purchase_amount").alias("total_spend_30d"),
            avg("session_duration").alias("avg_session_duration"),
            max("event_timestamp").alias("last_activity_timestamp"),

            # Percentiles (approximate for speed)
            expr("percentile_approx(purchase_amount, 0.5)").alias("median_purchase_amount"),

            # Collect list for sequential features
            collect_list(struct("event_timestamp", "event_type")).alias("event_sequence")
        )

    # Write with optimization
    features.write \
        .mode("overwrite") \
        .format("parquet") \
        .option("compression", "snappy") \
        .partitionBy("customer_segment") \
        .save("gold.customer_behavior_features")

    spark.stop()

# Run with cost tracking
cost_tracker.track_spark_job(optimize_spark_feature_computation)
```

## 🚀 CI/CD for Feature Pipelines

### Automated Feature Pipeline
```yaml
# .github/workflows/feature-pipeline.yml
name: Feature Engineering Pipeline

on:
  push:
    paths:
      - 'features/**'
      - 'transformations/**'
    branches:
      - main
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours

jobs:
  feature-engineering:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Unit test feature transformations
        run: pytest tests/features/

      - name: Validate feature schema
        run: python scripts/validate_feature_schema.py

      - name: Run feature quality checks
        run: python scripts/feature_quality_checks.py

      - name: Compute features (incremental)
        run: |
          python pipelines/compute_features.py \
            --mode incremental \
            --optimize-cost true \
            --max-cost 50.00

      - name: Validate feature distributions
        run: python scripts/validate_feature_distributions.py

      - name: Test training-serving consistency
        run: pytest tests/integration/test_feature_consistency.py

      - name: Register features in feature store
        if: success()
        run: python scripts/register_features.py --version auto

      - name: Update online feature store
        run: python scripts/sync_online_features.py

      - name: Run feature drift detection
        run: python scripts/detect_feature_drift.py

      - name: Generate feature cost report
        run: python scripts/feature_cost_report.py
```

## 📊 Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Computation Costs** | Cost per feature group | <$10 | FinOps tracker |
| | Monthly feature compute | <$1000 | Azure Cost Management |
| | Incremental savings | >80% | Cost tracker |
| | Spark cluster utilization | >75% | Azure Monitor |
| **Storage Costs** | Feature storage cost | <$500/month | Azure Storage metrics |
| | Compression ratio | >3x | Parquet metrics |
| | Archived features | >60% | Lifecycle policy |
| **Serving Performance** | Online feature latency (p95) | <10ms | App Insights |
| | Cache hit rate | >90% | Redis metrics |
| | Feature freshness | <6 hours | Freshness monitor |
| **Data Quality** | Feature completeness | >99% | Quality checks |
| | Feature drift score | <0.15 | Drift detector |
| | Schema validation success | 100% | Validation tests |
| **Pipeline Reliability** | Feature pipeline success | >99% | Airflow/ADF |
| | Training-serving skew | <1% | Consistency tests |

## 🔄 Integration Workflow

### End-to-End Feature Pipeline
```
1. Data Ingestion (de-01)
   ↓
2. Data Quality Validation (de-03)
   ↓
3. PII Detection & Masking (sa-01)
   ↓
4. Feature Transformation (ml-02)
   ↓
5. Feature Validation (ml-02)
   ↓
6. Cost Optimization (fo-05, fo-07)
   ↓
7. Feature Store Registration (mo-02)
   ↓
8. Lineage Tracking (mo-06)
   ↓
9. Online Store Sync (ml-02)
   ↓
10. Feature Drift Monitoring (mo-05)
    ↓
11. Training Data Generation (ml-01, ml-03)
    ↓
12. Real-time Feature Serving (ml-04)
```

## 🎯 Quick Wins

1. **Implement incremental feature computation** - 80-95% compute cost reduction
2. **Enable feature caching with Redis** - 10x faster online serving
3. **Use Parquet with compression** - 3-5x storage cost reduction
4. **Centralize features in feature store** - Eliminate duplicate computations
5. **Set up feature versioning** - Enable reproducibility and rollback
6. **Implement lifecycle policies** - 60-90% storage cost savings
7. **Optimize Spark configurations** - 30-50% faster feature computation
8. **Enable feature drift monitoring** - Detect data quality issues early
9. **Use broadcast joins for lookups** - 5-10x faster Spark joins
10. **Implement batch feature serving** - 100x more efficient than single requests
