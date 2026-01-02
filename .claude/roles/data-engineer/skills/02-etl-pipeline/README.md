# Skill 2: ETL/ELT Pipeline Orchestration

##  Overview
Build and orchestrate production-grade ETL/ELT pipelines with scheduling, monitoring, error handling, and dependency management for scalable data workflows.

##  Connections
- **Data Engineer**: Feeds lakehouse architecture layers (de-01, de-03)
- **ML Engineer**: Provides training data pipelines (ml-01, ml-02)
- **MLOps**: Data versioning and feature pipelines (mo-02, mo-06)
- **AI Engineer**: Prepares data for RAG systems (ai-02)
- **Data Scientist**: Delivers clean data for analysis (ds-01, ds-02)
- **Security Architect**: Secure data movement, encryption in transit (sa-04, sa-05)
- **FinOps**: Pipeline cost optimization and monitoring (fo-01, fo-06)
- **DevOps**: CI/CD for pipeline deployment, IaC (do-01, do-04, do-08)

##  Tools Included

### 1. `orchestrator.py`
Pipeline orchestration with DAG-based workflow management using Airflow/Prefect.

### 2. `connector_factory.py`
Universal connectors for databases, APIs, files, and cloud storage.

### 3. `transformation_engine.py`
Scalable data transformations with schema validation and error handling.

### 4. `incremental_loader.py`
Change Data Capture (CDC) and incremental loading strategies.

### 5. `pipeline_monitor.py`
Real-time pipeline monitoring, alerting, and SLA tracking.

##  Architecture

```
Source Systems → Extract → Transform → Load → Target Systems
       ↓           ↓          ↓          ↓          ↓
   Connectors  Staging   Validation  Loading   Lakehouse
   API/DB/File  Area     Quality     Strategy   Layers
                         Checks      (Full/Inc)
```

##  Quick Start

```python
from orchestrator import Pipeline, Task
from connector_factory import ConnectorFactory

# Define pipeline
pipeline = Pipeline(
    name="customer_etl",
    schedule="0 2 * * *",  # Daily at 2 AM
    max_retries=3
)

# Extract task
@pipeline.task(name="extract_customers")
def extract():
    connector = ConnectorFactory.create(
        source_type="postgres",
        connection_string=os.getenv("DB_CONNECTION")
    )
    return connector.extract(
        query="SELECT * FROM customers WHERE updated_at > :last_run",
        params={"last_run": pipeline.last_run_time}
    )

# Transform task
@pipeline.task(name="transform_customers", depends_on=["extract_customers"])
def transform(data):
    from transformation_engine import TransformationEngine

    engine = TransformationEngine()
    return engine.apply([
        engine.clean_nulls(),
        engine.standardize_phone_numbers(),
        engine.deduplicate(key="customer_id"),
        engine.validate_schema(schema="customer_schema.json")
    ], data)

# Load task
@pipeline.task(name="load_customers", depends_on=["transform_customers"])
def load(data):
    connector = ConnectorFactory.create(
        target_type="delta_lake",
        path="abfss://silver@lakehouse.dfs.core.windows.net/customers"
    )
    connector.load(data, mode="append", partition_by="ingestion_date")

# Execute
pipeline.run()
```

##  Best Practices

### Cost Optimization (FinOps Integration)

1. **Optimize Compute for Pipeline Execution**
   - Use serverless compute for sporadic pipelines
   - Right-size dedicated compute pools for regular jobs
   - Implement auto-scaling based on queue depth
   - Schedule resource-intensive jobs during off-peak hours
   - Reference: FinOps fo-06 (Compute Optimization)

2. **Incremental Loading to Reduce Costs**
   - Implement CDC to process only changed records
   - Use watermarks for incremental extraction
   - Partition data by date for efficient processing
   - Track last successful run timestamps
   - Reference: Data Engineer best practices

3. **Pipeline Cost Monitoring**
   - Track costs per pipeline execution
   - Monitor data transfer costs between regions
   - Alert on cost anomalies
   - Generate cost attribution reports by team/project
   - Reference: FinOps fo-01 (Cost Monitoring), fo-03 (Budget Management)

4. **Data Transfer Cost Optimization**
   - Minimize cross-region data movement
   - Compress data before transfer
   - Use Azure Private Link to avoid egress charges
   - Batch small files to reduce transaction costs
   - Reference: FinOps fo-05 (Storage Optimization)

### Infrastructure as Code (DevOps Integration)

5. **Deploy Pipelines as Code**
   - Version control all pipeline definitions
   - Use IaC for pipeline infrastructure (Terraform/Bicep)
   - Implement GitOps for pipeline deployment
   - Maintain separate environments (dev/staging/prod)
   - Reference: DevOps do-04 (IaC), do-05 (GitOps)

6. **CI/CD for Data Pipelines**
   - Automated testing for pipeline logic
   - Schema validation tests
   - Data quality tests in CI
   - Blue-green deployments for critical pipelines
   - Reference: DevOps do-01 (CI/CD), do-02 (Testing)

7. **Containerize Pipeline Components**
   - Package transformations in Docker containers
   - Use Kubernetes for orchestration at scale
   - Implement health checks and readiness probes
   - Version container images alongside code
   - Reference: DevOps do-03 (Containerization)

### Security & Compliance (Security Architect Integration)

8. **Secure Credential Management**
   - Store credentials in Azure Key Vault
   - Use managed identities where possible
   - Rotate credentials regularly
   - Never hardcode secrets in pipeline code
   - Reference: Security Architect sa-03 (Secrets Management)

9. **Encrypt Data in Transit**
   - Use TLS for all data transfers
   - Implement VPN/Private Link for sensitive data
   - Validate SSL certificates
   - Monitor for unencrypted connections
   - Reference: Security Architect sa-04 (Encryption)

10. **Audit Trail for Data Movement**
    - Log all pipeline executions with metadata
    - Track data lineage from source to target
    - Implement compliance auditing
    - Retain audit logs per regulatory requirements
    - Reference: Security Architect sa-06 (Data Governance)

### Data Quality (Data Engineer Integration)

11. **Schema Validation**
    - Validate schemas before transformation
    - Detect schema drift automatically
    - Alert on breaking schema changes
    - Maintain schema registry
    - Reference: Data Engineer de-03 (Data Quality)

12. **Data Quality Gates**
    - Implement quality checks at each stage
    - Quarantine bad data for review
    - Alert on quality threshold violations
    - Track data quality metrics over time
    - Reference: Data Engineer de-03 (Data Quality)

13. **Error Handling & Recovery**
    - Implement circuit breakers for failing sources
    - Dead letter queues for failed records
    - Automatic retry with exponential backoff
    - Manual review process for persistent failures
    - Reference: System Design sd-05 (Resilience Patterns)

### Monitoring & Observability (DevOps Integration)

14. **Pipeline Monitoring**
    - Track execution time, success rate, data volume
    - Set up SLA alerts for critical pipelines
    - Monitor resource utilization (CPU, memory, I/O)
    - Implement distributed tracing for complex workflows
    - Reference: DevOps do-08 (Monitoring & Observability)

15. **Alerting Strategy**
    - Alert on pipeline failures with context
    - Warning alerts for performance degradation
    - SLA breach notifications
    - Cost spike alerts
    - Reference: DevOps do-08, FinOps fo-03

### Azure-Specific Best Practices

16. **Azure Data Factory**
    - Use managed VNet for secure connectivity
    - Implement parameterized pipelines
    - Enable git integration for version control
    - Use mapping data flows for complex transformations
    - Reference: Azure az-01 (Data Factory)

17. **Azure Synapse Pipelines**
    - Leverage Spark pools for big data processing
    - Use serverless SQL for ad-hoc transformations
    - Implement workload management
    - Monitor pipeline costs via Synapse Studio
    - Reference: Azure az-02 (Synapse Analytics)

18. **Integration Runtime Optimization**
    - Use Azure IR for Azure-to-Azure transfers
    - Self-hosted IR for on-premises connectivity
    - Right-size IR compute units
    - Enable VNet integration for security
    - Reference: Azure az-01

##  Cost Optimization Examples

### Incremental Loading with CDC
```python
from incremental_loader import IncrementalLoader
from datetime import datetime, timedelta

# Initialize incremental loader
loader = IncrementalLoader(
    source="sales_db",
    target="bronze.sales",
    watermark_column="updated_at"
)

# Load only changed records
result = loader.load_incremental(
    query="""
        SELECT * FROM sales
        WHERE updated_at > :watermark
        AND updated_at <= :current_time
    """,
    merge_key="sale_id"
)

print(f"Records processed: {result.records_processed}")
print(f"Records skipped: {result.records_skipped}")
print(f"Cost saved vs full load: ${result.cost_savings:.2f}")

# Track incremental loading efficiency
from finops_tracker import PipelineCostTracker

cost_tracker = PipelineCostTracker()
cost_tracker.log_execution(
    pipeline_name="sales_incremental",
    execution_time=result.execution_time,
    data_processed_gb=result.data_size_gb,
    compute_cost=result.compute_cost,
    storage_cost=result.storage_cost
)
```

### Pipeline Cost Monitoring
```python
from pipeline_monitor import PipelineMonitor
from finops_tracker import PipelineCostTracker

monitor = PipelineMonitor()
cost_tracker = PipelineCostTracker()

# Track pipeline execution costs
@cost_tracker.track_costs
def run_pipeline(pipeline_name: str):
    pipeline = Pipeline.get(pipeline_name)
    result = pipeline.run()

    # Log detailed cost breakdown
    cost_tracker.log_execution(
        pipeline_name=pipeline_name,
        execution_time=result.duration,
        data_processed_gb=result.data_volume,
        compute_cost=result.compute_cost,
        data_transfer_cost=result.transfer_cost,
        storage_cost=result.storage_cost
    )

    return result

# Generate cost report
report = cost_tracker.generate_report(
    period="monthly",
    group_by=["pipeline_name", "environment"]
)

print(f"Total pipeline costs: ${report.total_cost:.2f}")
print(f"Top 5 expensive pipelines:")
for pipeline in report.top_pipelines:
    print(f"  {pipeline.name}: ${pipeline.cost:.2f}")

# Set budget alerts
cost_tracker.set_budget_alert(
    pipeline_name="customer_etl",
    monthly_budget=500.00,
    alert_threshold=0.8
)
```

### Optimize Data Transfer Costs
```python
from connector_factory import ConnectorFactory
from compression_utils import compress_data

# Extract with compression
source_connector = ConnectorFactory.create(
    source_type="postgres",
    connection_string=db_connection
)

data = source_connector.extract(query="SELECT * FROM large_table")

# Compress before transfer
compressed_data = compress_data(
    data,
    algorithm="zstd",  # Better compression than gzip
    compression_level=3  # Balance speed vs size
)

print(f"Original size: {data.size_mb:.2f} MB")
print(f"Compressed size: {compressed_data.size_mb:.2f} MB")
print(f"Compression ratio: {compressed_data.ratio:.2f}x")
print(f"Transfer cost saved: ${compressed_data.cost_savings:.2f}")

# Load to target
target_connector = ConnectorFactory.create(
    target_type="delta_lake",
    path="abfss://bronze@lakehouse.dfs.core.windows.net/data"
)

target_connector.load(
    compressed_data,
    decompress=True,
    partition_by="ingestion_date"
)
```

##  Security Best Practices Examples

### Secure Credential Management
```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from connector_factory import ConnectorFactory

# Use managed identity to access Key Vault
credential = DefaultAzureCredential()
key_vault_client = SecretClient(
    vault_url="https://my-keyvault.vault.azure.net/",
    credential=credential
)

# Retrieve connection string securely
db_connection = key_vault_client.get_secret("postgres-connection-string").value

# Create connector with secure credentials
connector = ConnectorFactory.create(
    source_type="postgres",
    connection_string=db_connection,
    ssl_mode="require",  # Enforce SSL
    ssl_cert_path="/certs/postgres.crt"
)

# Audit credential access
from audit_logger import AuditLogger
audit_logger = AuditLogger()
audit_logger.log_credential_access(
    secret_name="postgres-connection-string",
    accessed_by=os.getenv("USER"),
    pipeline="customer_etl",
    timestamp=datetime.now()
)
```

### Data Lineage Tracking
```python
from data_lineage import LineageTracker

tracker = LineageTracker()

# Track data movement
@tracker.track_lineage
def customer_etl_pipeline():
    # Extract
    source_data = extract_from_postgres(
        table="customers",
        database="prod_crm"
    )

    tracker.log_source(
        dataset="prod_crm.customers",
        record_count=len(source_data),
        extraction_time=datetime.now()
    )

    # Transform
    transformed_data = apply_transformations(source_data)

    tracker.log_transformation(
        operation="clean_and_standardize",
        input_records=len(source_data),
        output_records=len(transformed_data),
        rules_applied=["deduplicate", "validate_email", "standardize_phone"]
    )

    # Load
    load_to_lakehouse(
        data=transformed_data,
        target="silver.customers"
    )

    tracker.log_target(
        dataset="silver.customers",
        record_count=len(transformed_data),
        load_time=datetime.now()
    )

# Query lineage
lineage = tracker.get_lineage(dataset="silver.customers")
print(f"Source: {lineage.source}")
print(f"Transformations: {lineage.transformations}")
print(f"Load timestamp: {lineage.loaded_at}")
```

##  Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Performance** | Pipeline execution time (p95) | <30min | Azure Monitor |
| | Data throughput | >10GB/hour | Pipeline metrics |
| | Task success rate | >99% | Airflow/Prefect |
| **Cost** | Cost per pipeline run | <$5 | FinOps tracker |
| | Data transfer cost | <$0.10/GB | Cost Management |
| | Compute cost per GB processed | <$0.50 | Custom tracker |
| **Quality** | Schema validation pass rate | 100% | DQ framework |
| | Data completeness | >98% | DQ checks |
| | Duplicate rate | <1% | DQ checks |
| **Reliability** | Pipeline availability | >99.5% | Azure Monitor |
| | Mean Time To Recovery (MTTR) | <15min | Incident tracker |
| | Failed task retry success rate | >80% | Pipeline logs |
| **Security** | Encrypted connections | 100% | Security scans |
| | Credential rotation compliance | 100% | Compliance dashboard |

##  Deployment Pipeline

### CI/CD for ETL Pipelines
```yaml
# .github/workflows/deploy-etl-pipeline.yml
name: Deploy ETL Pipeline

on:
  push:
    paths:
      - 'pipelines/**'
      - 'transformations/**'
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
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run unit tests
        run: pytest tests/unit/ --cov=pipelines

      - name: Validate pipeline definitions
        run: python scripts/validate_pipelines.py

      - name: Test schema validation
        run: pytest tests/schema_validation/

      - name: Run data quality tests
        run: pytest tests/data_quality/

      - name: Security scan
        run: |
          pip install bandit safety
          bandit -r pipelines/
          safety check

      - name: Deploy to staging
        run: |
          python scripts/deploy_pipeline.py \
            --environment staging \
            --pipeline customer_etl

      - name: Run integration tests
        run: pytest tests/integration/ --env staging

      - name: Deploy to production
        if: success()
        run: |
          python scripts/deploy_pipeline.py \
            --environment production \
            --pipeline customer_etl

      - name: Monitor pipeline health
        run: python scripts/monitor_pipeline.py --duration 1h

      - name: Generate deployment report
        run: python scripts/generate_deployment_report.py
```

##  Integration Workflow

### End-to-End Pipeline Workflow
```
1. Schedule Trigger (Airflow/Prefect/ADF)
   ↓
2. Extract from Sources (API/DB/Files)
   ↓
3. Validate Schema (de-03)
   ↓
4. Security Scan & PII Detection (sa-01)
   ↓
5. Transform Data (de-02)
   ↓
6. Data Quality Checks (de-03)
   ↓
7. Load to Lakehouse (de-01)
    Bronze Layer (raw)
    Silver Layer (cleaned)
    Gold Layer (business-ready)
   ↓
8. Trigger Downstream Pipelines
    Feature Store Update (ml-02)
    RAG Knowledge Base (ai-02)
    Analytics Refresh (ds-01)
    Model Retraining (ml-01)
   ↓
9. Monitor & Alert (do-08)
   ↓
10. Cost Tracking & Optimization (fo-01)
```

##  Quick Wins

1. **Implement incremental loading** - 60-80% cost reduction vs full loads
2. **Add schema validation** - Catch data issues early
3. **Set up pipeline monitoring** - Reduce MTTR by 50%
4. **Use managed identities** - Eliminate credential management overhead
5. **Enable auto-scaling** - 30-50% compute cost savings
6. **Implement retry logic** - Improve reliability to 99%+
7. **Add data quality checks** - Prevent downstream issues
8. **Set up cost alerts** - Avoid budget overruns
9. **Containerize transformations** - Portable, reproducible pipelines
10. **Enable diagnostic logging** - Full observability and debugging
