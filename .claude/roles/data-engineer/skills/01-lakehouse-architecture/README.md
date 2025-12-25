# Skill 1: Lakehouse Architecture (Bronze-Silver-Gold)

## 🎯 Overview
Implement medallion architecture (Bronze-Silver-Gold) for scalable, governed data lakehouse.

## 🔗 Connections
- **All Roles**: Provides clean, structured data foundation for analytics and ML
- **ML Engineer**: Feeds feature store with Gold layer (ml-02, ml-03)
- **MLOps**: Data versioning and lineage tracking (mo-02, mo-06)
- **AI Engineer**: Provides context for RAG systems (ai-02, ai-03)
- **Data Scientist**: Provides clean data for analysis and modeling (ds-01, ds-02)
- **Security Architect**: Implements data governance and encryption (sa-01, sa-02, sa-06)
- **FinOps**: Storage and compute cost optimization (fo-01, fo-05, fo-06)
- **DevOps**: IaC for data infrastructure, CI/CD for pipelines (do-01, do-04, do-08)
- **System Design**: Scalability and disaster recovery patterns (sd-03, sd-04, sd-06)

## 🛠️ Tools Included

### 1. `bronze_ingestion.py`
Raw data ingestion with schema validation and error handling.

### 2. `silver_transformation.py`
Data cleaning, standardization, and deduplication.

### 3. `gold_aggregation.py`
Business logic, aggregations, and feature engineering.

### 4. `delta_optimizer.py`
Delta Lake optimization (vacuum, Z-ordering, compaction).

### 5. `medallion_queries.sql`
SQL patterns for each layer of the medallion architecture.

## 📊 Architecture

```
Bronze (Raw) → Silver (Cleaned) → Gold (Business-Ready)
    ↓              ↓                    ↓
 Append-only   Deduped/Valid      Aggregated/Featured
 Full history  Schema enforced    Business logic
```

## 🚀 Quick Start

```python
from bronze_ingestion import BronzeLoader
from silver_transformation import SilverTransformer
from gold_aggregation import GoldAggregator

# Bronze: Ingest raw data
bronze = BronzeLoader(source="salesforce_crm")
bronze.ingest(path="raw_data.json")

# Silver: Clean and standardize
silver = SilverTransformer()
silver.transform(bronze_table="bronze.crm_leads")

# Gold: Create business views
gold = GoldAggregator()
gold.aggregate(silver_table="silver.crm_leads_clean")
```

## 📚 Best Practices

### Cost Optimization (FinOps Integration)

1. **Storage Cost Optimization**
   - Implement lifecycle policies (hot → cool → archive)
   - Use compression (Snappy, Zstandard) for Delta tables
   - Partition data by date for efficient pruning
   - Monitor storage growth and set capacity alerts
   - Reference: FinOps fo-05 (Storage Cost Optimization)

2. **Compute Cost Optimization**
   - Use serverless SQL pools for ad-hoc queries
   - Auto-scale Spark clusters based on workload
   - Use spot instances for batch processing
   - Schedule non-critical jobs during off-peak hours
   - Right-size compute based on actual usage patterns
   - Reference: FinOps fo-06 (Compute Optimization), fo-01 (Cost Monitoring)

3. **Delta Lake Optimization for Cost**
   - Run OPTIMIZE command to compact small files
   - Use Z-Ordering for frequently queried columns
   - VACUUM old versions with appropriate retention
   - Monitor table sizes and file counts
   - Reference: FinOps fo-05, Data Engineer best practices

4. **Query Cost Optimization**
   - Cache frequently accessed tables
   - Use materialized views for complex aggregations
   - Implement data skipping with statistics
   - Monitor query costs and optimize expensive queries
   - Reference: FinOps fo-03 (Budget Management)

### Infrastructure as Code (DevOps Integration)

5. **Deploy with IaC**
   - Use Terraform or Bicep for all infrastructure
   - Version control infrastructure code in Git
   - Implement CI/CD for infrastructure changes
   - Use multiple environments (dev, staging, prod)
   - Reference: DevOps do-04 (IaC), do-05 (GitOps)

6. **Automate Data Pipeline Deployment**
   - Package pipelines as code
   - Use CI/CD for pipeline deployment
   - Implement automated testing for pipelines
   - Blue-green deployments for critical pipelines
   - Reference: DevOps do-01 (CI/CD), do-02 (Testing)

7. **Monitoring & Observability**
   - Enable diagnostic logging for all services
   - Set up Azure Monitor dashboards
   - Alert on pipeline failures and anomalies
   - Track data quality metrics over time
   - Reference: DevOps do-08 (Monitoring & Observability)

### Security & Governance (Security Architect Integration)

8. **Data Governance Framework**
   - Implement data catalog (Azure Purview)
   - Tag all datasets with business metadata
   - Track data lineage from Bronze to Gold
   - Enforce data quality policies
   - Reference: Security Architect sa-06 (Data Governance)

9. **PII Protection**
   - Detect PII in Bronze layer
   - Mask/encrypt PII in Silver layer
   - Implement row-level security on Gold tables
   - Audit PII access and usage
   - Reference: Security Architect sa-01 (PII Detection)

10. **Access Control**
    - Implement RBAC for all data layers
    - Use managed identities for service authentication
    - Enforce least privilege access
    - Audit all data access
    - Reference: Security Architect sa-02 (IAM)

11. **Encryption**
    - Enable encryption at rest (all storage)
    - Use TLS for data in transit
    - Manage keys with Azure Key Vault
    - Rotate encryption keys regularly
    - Reference: Security Architect sa-04 (Encryption)

### Data Quality (Data Engineer Integration)

12. **Automated Data Quality Checks**
    - Validate schemas at Bronze ingestion
    - Check data completeness in Silver
    - Monitor data freshness
    - Alert on quality threshold violations
    - Reference: Data Engineer de-03 (Data Quality)

13. **Data Lineage Tracking**
    - Track data transformations end-to-end
    - Document data sources and dependencies
    - Enable impact analysis for changes
    - Integrate with MLOps for model lineage
    - Reference: MLOps mo-02 (Data Versioning), mo-06 (Lineage)

### Enterprise Patterns

14. **Multi-Tenancy**
    - Isolate data by tenant/business unit
    - Implement tenant-level security
    - Monitor costs per tenant
    - Scale compute independently per tenant
    - Reference: System Design sd-07 (Multi-Tenant Architecture)

15. **Disaster Recovery**
    - Implement geo-redundant storage
    - Automate backups with retention policies
    - Test recovery procedures regularly
    - Document RPO/RTO targets
    - Reference: System Design sd-06 (HA/DR)

16. **Compliance**
    - Implement GDPR right-to-erasure
    - Maintain audit logs for compliance
    - Data retention policies by regulation
    - Regular compliance audits
    - Reference: Security Architect sa-06 (Compliance)

### Azure-Specific Best Practices

17. **Azure Synapse Analytics**
    - Use dedicated SQL pools for production workloads
    - Implement workload isolation and classification
    - Enable result set caching for frequent queries
    - Monitor and optimize distribution keys
    - Reference: Azure az-02 (Synapse Analytics)

18. **Azure Data Factory**
    - Use managed VNet for secure integration
    - Implement parameterized pipelines
    - Enable git integration for version control
    - Monitor pipeline costs and optimize activities
    - Reference: Azure az-01 (Data Factory)

19. **Delta Lake on Azure**
    - Enable delta cache for hot data
    - Use optimized writes for streaming
    - Implement time travel for debugging
    - Monitor delta table metrics
    - Reference: Data Engineer best practices

### ML/AI Integration

20. **Feature Store Integration**
    - Design Gold layer for feature consumption
    - Implement point-in-time correctness
    - Version features alongside models
    - Monitor feature drift
    - Reference: ML Engineer ml-02 (Feature Engineering)

21. **RAG Knowledge Base**
    - Export Gold tables for RAG indexing
    - Ensure data freshness for AI context
    - Track document versions
    - Monitor data quality for RAG
    - Reference: AI Engineer ai-02 (RAG Pipeline)

## 💰 Cost Optimization Examples

### Storage Lifecycle Management
```python
from delta_optimizer import DeltaOptimizer
from azure.storage.blob import BlobServiceClient

# Implement storage tiering
optimizer = DeltaOptimizer()

# Optimize Delta tables
optimizer.optimize_table(
    table_name="bronze.events",
    z_order_by=["event_date", "event_type"],
    vacuum_retention_hours=168  # 7 days
)

# Set lifecycle policies
blob_client = BlobServiceClient(connection_string=conn_str)
lifecycle_policy = {
    "rules": [
        {
            "enabled": True,
            "name": "move-to-cool",
            "type": "Lifecycle",
            "definition": {
                "actions": {
                    "baseBlob": {
                        "tierToCool": {"daysAfterModificationGreaterThan": 30},
                        "tierToArchive": {"daysAfterModificationGreaterThan": 90}
                    }
                }
            }
        }
    ]
}

# Monitor storage costs
from finops_tracker import StorageCostTracker
cost_tracker = StorageCostTracker()
monthly_costs = cost_tracker.get_storage_costs(
    resource_group="data-lakehouse",
    period="monthly"
)

print(f"Bronze layer: ${monthly_costs.bronze:.2f}")
print(f"Silver layer: ${monthly_costs.silver:.2f}")
print(f"Gold layer: ${monthly_costs.gold:.2f}")
print(f"Total savings from tiering: ${monthly_costs.savings:.2f}")
```

### Compute Cost Optimization
```python
from azure.synapse.spark import SparkPoolManager

# Auto-scaling configuration
spark_pool = SparkPoolManager()
spark_pool.configure_autoscale(
    pool_name="default-spark-pool",
    min_nodes=2,
    max_nodes=10,
    auto_pause_minutes=15  # Pause when idle
)

# Use spot instances for batch jobs
spark_pool.submit_batch_job(
    script="bronze_ingestion.py",
    executor_size="Medium",
    executors=5,
    use_spot_instances=True,  # 60-90% cost savings
    max_price_per_hour=0.50
)

# Monitor compute costs
from finops_tracker import ComputeCostTracker
compute_tracker = ComputeCostTracker()

# Get cost breakdown
costs = compute_tracker.get_compute_costs(
    resource_type="synapse_spark",
    period="daily"
)

# Set budget alerts
compute_tracker.set_budget_alert(
    pool_name="default-spark-pool",
    daily_budget=100.00,
    alert_threshold=0.8
)
```

### Query Cost Tracking
```python
from synapse_cost_tracker import QueryCostAnalyzer

analyzer = QueryCostAnalyzer()

# Track query costs
@analyzer.track_cost
def run_gold_aggregation(query: str):
    return spark.sql(query)

# Generate cost report
report = analyzer.generate_cost_report(period="weekly")
print(f"Total query costs: ${report.total_cost:.2f}")
print(f"Most expensive queries: {report.top_queries}")
print(f"Cost by user: {report.cost_by_user}")

# Optimize expensive queries
recommendations = analyzer.optimize_queries(
    cost_threshold=10.00  # Queries costing more than $10
)
```

## 🏗️ Infrastructure as Code Examples

### Terraform for Lakehouse
```hcl
# main.tf - Lakehouse infrastructure
module "lakehouse" {
  source = "./modules/lakehouse"

  resource_group = "rg-lakehouse-prod"
  location       = "eastus"

  storage_account = {
    name                     = "lakehouseprod"
    tier                     = "Standard"
    replication_type         = "GRS"  # Geo-redundant
    enable_versioning        = true
    lifecycle_rules          = {
      move_to_cool    = 30  # days
      move_to_archive = 90  # days
    }
  }

  synapse_workspace = {
    name                = "synapse-lakehouse-prod"
    sql_admin_username  = "sqladmin"
    managed_vnet_enabled = true

    spark_pools = [{
      name               = "default"
      node_size          = "Medium"
      min_nodes          = 2
      max_nodes          = 10
      auto_pause_minutes = 15
      use_spot_instances = true  # Cost savings
    }]

    sql_pools = [{
      name               = "gold_analytics"
      sku                = "DW100c"
      auto_pause_enabled = true
      auto_pause_delay   = 60  # minutes
    }]
  }

  delta_tables = {
    bronze = ["events", "transactions", "users"]
    silver = ["events_clean", "transactions_validated", "users_enriched"]
    gold   = ["daily_metrics", "user_features", "transaction_summary"]
  }

  tags = {
    Environment = "Production"
    CostCenter  = "Data-Platform"
    Owner       = "DataEngineering"
  }
}

# monitoring.tf
resource "azurerm_monitor_diagnostic_setting" "lakehouse" {
  name                       = "lakehouse-diagnostics"
  target_resource_id         = module.lakehouse.storage_account_id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.main.id

  log {
    category = "StorageRead"
    enabled  = true
  }

  log {
    category = "StorageWrite"
    enabled  = true
  }

  metric {
    category = "Transaction"
    enabled  = true
  }
}

# alerts.tf
resource "azurerm_monitor_metric_alert" "storage_cost" {
  name                = "lakehouse-storage-cost-alert"
  resource_group_name = var.resource_group
  scopes              = [module.lakehouse.storage_account_id]
  description         = "Alert when storage costs exceed threshold"

  criteria {
    metric_namespace = "Microsoft.Storage/storageAccounts"
    metric_name      = "UsedCapacity"
    aggregation      = "Average"
    operator         = "GreaterThan"
    threshold        = 5000000000000  # 5TB
  }

  action {
    action_group_id = azurerm_monitor_action_group.ops_team.id
  }
}
```

### CI/CD Pipeline for Data Pipelines
```yaml
# .github/workflows/deploy-pipeline.yml
name: Deploy Data Pipeline

on:
  push:
    paths:
      - 'pipelines/**'
    branches:
      - main

jobs:
  test-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run unit tests
        run: pytest tests/unit/

      - name: Run data quality tests
        run: pytest tests/data_quality/

      - name: Deploy infrastructure (Terraform)
        run: |
          cd terraform
          terraform init
          terraform plan -out=tfplan
          terraform apply tfplan

      - name: Deploy pipelines to Synapse
        run: |
          python scripts/deploy_pipelines.py \
            --workspace synapse-lakehouse-prod \
            --environment production

      - name: Run integration tests
        run: pytest tests/integration/

      - name: Monitor pipeline health
        run: python scripts/monitor_pipelines.py --duration 30m

      - name: Generate cost report
        run: python scripts/generate_cost_report.py
```

## 📊 Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Cost** | Monthly storage cost | <$5000 | FinOps dashboard |
| | Compute cost per pipeline run | <$50 | Cost Management |
| | Cost per TB processed | <$10 | Custom tracker |
| **Performance** | Bronze ingestion latency | <5min | Azure Monitor |
| | Silver transformation time | <15min | Synapse metrics |
| | Gold aggregation time | <30min | Spark UI |
| **Quality** | Schema validation pass rate | >99% | Data quality checks |
| | Data completeness | >98% | DQ framework |
| | Data freshness (SLA) | <1 hour | Custom alerts |
| **Reliability** | Pipeline success rate | >99.5% | Azure Monitor |
| | Data availability | >99.9% | Health checks |
| **Security** | PII detection coverage | 100% | Security scans |
| | Access control violations | 0 | Audit logs |

## 🔄 Integration Workflow

### End-to-End Data Flow
```
1. Source Systems (APIs, Databases, Files)
   ↓
2. Bronze Ingestion (de-01) → Cost Tracking (fo-05)
   ↓
3. Schema Validation (de-03)
   ↓
4. PII Detection (sa-01)
   ↓
5. Silver Transformation (de-01) → Quality Checks (de-03)
   ↓
6. Gold Aggregation (de-01) → Feature Engineering (ml-02)
   ↓
7. Serve to downstream (AI, ML, Analytics)
   ├── Feature Store (ml-02)
   ├── RAG Knowledge Base (ai-02)
   ├── Analytics Dashboards (ds-01)
   └── Model Training (ml-01)
   ↓
8. Monitor (do-08, mo-04) → Optimize Costs (fo-01)
```

## 🎯 Quick Wins

1. **Enable storage lifecycle policies** - 40-60% storage cost reduction
2. **Implement auto-scaling for Spark** - 30-50% compute cost savings
3. **Use spot instances for batch jobs** - 60-90% compute cost savings
4. **Set up Delta table optimization** - Faster queries, lower costs
5. **Deploy with IaC** - Consistent environments, faster deployments
6. **Enable diagnostic logging** - Full observability
7. **Implement PII detection** - Compliance and data protection
8. **Set up cost alerts** - Prevent budget overruns
9. **Use materialized views** - 10x faster query performance
10. **Implement data quality checks** - Prevent downstream issues
