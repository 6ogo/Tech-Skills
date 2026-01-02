# Skill 3: Data Quality & Validation

##  Overview
Implement comprehensive data quality frameworks with automated validation, monitoring, anomaly detection, and data profiling to ensure data reliability and trustworthiness.

##  Connections
- **Data Engineer**: Quality gates for lakehouse layers (de-01, de-02)
- **ML Engineer**: Feature quality validation (ml-02, ml-03)
- **MLOps**: Drift detection and data monitoring (mo-05, mo-06)
- **AI Engineer**: RAG data quality assurance (ai-02)
- **Data Scientist**: Clean data for analysis (ds-01, ds-02)
- **Security Architect**: PII detection and data governance (sa-01, sa-06)
- **FinOps**: Prevent costly data quality issues (fo-01)
- **DevOps**: Automated quality testing in CI/CD (do-01, do-02)

##  Tools Included

### 1. `data_validator.py`
Comprehensive data validation rules engine with 50+ built-in validators.

### 2. `data_profiler.py`
Statistical profiling and summary statistics generation.

### 3. `anomaly_detector.py`
ML-based anomaly detection for data quality monitoring.

### 4. `quality_dashboard.py`
Real-time data quality dashboards and reporting.

### 5. `data_quality_rules.yaml`
Declarative quality rules configuration.

##  Data Quality Dimensions

```
Completeness → Are all required fields present?
Accuracy     → Is the data correct?
Consistency  → Is data uniform across systems?
Validity     → Does data conform to rules?
Timeliness   → Is data fresh and up-to-date?
Uniqueness   → Are there duplicates?
```

##  Quick Start

```python
from data_validator import DataValidator
from data_profiler import DataProfiler

# Initialize validator
validator = DataValidator()

# Define quality rules
rules = {
    "completeness": [
        validator.not_null("customer_id"),
        validator.not_null("email"),
        validator.not_null("created_at")
    ],
    "validity": [
        validator.email_format("email"),
        validator.value_in_range("age", min_val=0, max_val=120),
        validator.matches_regex("phone", r"^\+?\d{10,15}$")
    ],
    "uniqueness": [
        validator.unique("customer_id")
    ],
    "consistency": [
        validator.referential_integrity(
            column="country_code",
            reference_table="countries",
            reference_column="code"
        )
    ]
}

# Validate data
df = spark.read.table("silver.customers")
validation_result = validator.validate(df, rules)

# Check results
if validation_result.passed:
    print(" All quality checks passed!")
else:
    print(f" {validation_result.failed_count} checks failed")
    for failure in validation_result.failures:
        print(f"  - {failure.rule}: {failure.message}")
        print(f"    Failed records: {failure.failed_count}")

# Profile data
profiler = DataProfiler()
profile = profiler.profile(df)

print(f"Total records: {profile.row_count:,}")
print(f"Total columns: {profile.column_count}")
print(f"Missing values: {profile.missing_percentage:.2f}%")
print(f"Duplicate records: {profile.duplicate_count}")
```

##  Best Practices

### Data Quality Framework (Data Engineer Integration)

1. **Implement Quality Gates**
   - Validate at each lakehouse layer (Bronze → Silver → Gold)
   - Block bad data from propagating downstream
   - Quarantine failed records for review
   - Alert on quality threshold violations
   - Reference: Data Engineer de-01 (Lakehouse)

2. **Automated Quality Checks**
   - Run validation on every pipeline execution
   - Schedule periodic data profiling
   - Monitor quality metrics over time
   - Integrate with CI/CD pipelines
   - Reference: DevOps do-01 (CI/CD), do-02 (Testing)

3. **Data Profiling Strategy**
   - Profile new data sources before ingestion
   - Generate statistical summaries
   - Detect schema drift automatically
   - Track data distributions over time
   - Reference: Data Engineer best practices

4. **Quality Metrics & KPIs**
   - Define quality SLAs for each dataset
   - Track quality trends over time
   - Dashboard for stakeholder visibility
   - Alert on quality degradation
   - Reference: DevOps do-08 (Monitoring)

### ML/AI Data Quality (ML Engineer & MLOps Integration)

5. **Feature Quality Validation**
   - Validate feature distributions
   - Check for feature drift
   - Detect data leakage
   - Monitor feature correlations
   - Reference: ML Engineer ml-02 (Feature Engineering), MLOps mo-05 (Drift)

6. **Training Data Quality**
   - Validate labels and targets
   - Check class balance
   - Detect outliers and anomalies
   - Ensure temporal consistency
   - Reference: ML Engineer ml-01 (Training)

7. **Data Drift Detection**
   - Monitor statistical properties over time
   - Detect distribution shifts
   - Alert on significant drift
   - Trigger retraining when needed
   - Reference: MLOps mo-05 (Drift Detection)

### Security & Governance (Security Architect Integration)

8. **PII Detection in Quality Checks**
   - Scan for unexpected PII in data
   - Validate PII masking/encryption
   - Alert on PII in non-compliant columns
   - Audit PII handling
   - Reference: Security Architect sa-01 (PII Detection)

9. **Data Governance Integration**
   - Enforce data lineage tracking
   - Validate data classification tags
   - Compliance checks (GDPR, CCPA)
   - Retention policy validation
   - Reference: Security Architect sa-06 (Data Governance)

10. **Access Control Validation**
    - Verify row-level security rules
    - Audit data access patterns
    - Detect unauthorized access attempts
    - Validate encryption status
    - Reference: Security Architect sa-02 (IAM)

### Cost Optimization (FinOps Integration)

11. **Prevent Costly Quality Issues**
    - Catch bad data before expensive processing
    - Reduce compute waste on invalid data
    - Minimize storage of duplicates
    - Avoid downstream rework costs
    - Reference: FinOps fo-01 (Cost Monitoring)

12. **Optimize Quality Check Costs**
    - Use sampling for large datasets
    - Cache validation results
    - Incremental quality checks
    - Right-size compute for validation jobs
    - Reference: FinOps fo-06 (Compute Optimization)

### Azure-Specific Best Practices

13. **Azure Purview Integration**
    - Auto-discover data assets
    - Classify data automatically
    - Track data lineage
    - Quality annotations in catalog
    - Reference: Azure best practices

14. **Azure Monitor Integration**
    - Log quality metrics to Application Insights
    - Create custom dashboards
    - Set up alert rules
    - Track quality trends over time
    - Reference: DevOps do-08 (Monitoring)

15. **Azure Data Factory Data Flows**
    - Use data preview for validation
    - Implement conditional splits for quality
    - Error row handling
    - Quality metrics in pipeline monitoring
    - Reference: Azure az-01 (Data Factory)

### Anomaly Detection

16. **Statistical Anomaly Detection**
    - Z-score for univariate outliers
    - Isolation Forest for multivariate anomalies
    - Time-series anomaly detection
    - Seasonal pattern analysis
    - Reference: Data Scientist ds-01 (EDA)

17. **ML-Based Quality Monitoring**
    - Train models on historical quality patterns
    - Predict quality issues before they occur
    - Adaptive thresholds based on trends
    - Automated root cause analysis
    - Reference: ML Engineer ml-01, MLOps mo-04

##  Cost Optimization Examples

### Sampling Strategy for Large Datasets
```python
from data_validator import DataValidator
from sampling_strategies import SmartSampler

validator = DataValidator()
sampler = SmartSampler()

# Load large dataset
df = spark.read.table("bronze.events")  # 10TB table

# Smart sampling (stratified by key dimensions)
sample = sampler.stratified_sample(
    df,
    sample_size=1_000_000,  # 1M records instead of billions
    stratify_by=["event_type", "date"],
    confidence_level=0.95
)

print(f"Original size: {df.count():,} records")
print(f"Sample size: {sample.count():,} records")
print(f"Cost reduction: {sampler.cost_savings_percentage:.1f}%")

# Run validation on sample
validation_result = validator.validate(sample, quality_rules)

# Extrapolate results to full dataset
estimated_failures = validation_result.extrapolate_to_population(
    population_size=df.count()
)

print(f"Estimated failures in full dataset: {estimated_failures:,}")

# If sample passes, validate full dataset incrementally
if validation_result.passed:
    # Only validate new/changed records
    incremental_result = validator.validate_incremental(
        df,
        watermark_column="ingestion_date",
        last_validated_date=last_run_date
    )
```

### Optimize Validation Compute Costs
```python
from data_validator import DataValidator
from finops_tracker import ValidationCostTracker

validator = DataValidator()
cost_tracker = ValidationCostTracker()

# Cache expensive validation results
@cost_tracker.track_validation_costs
def validate_with_caching(table_name: str, rules: dict):
    # Check if data hasn't changed
    current_hash = calculate_table_hash(table_name)
    cached_result = validation_cache.get(current_hash)

    if cached_result:
        print(f" Using cached validation result")
        print(f"Cost saved: ${cached_result.cost_saved:.2f}")
        return cached_result

    # Run validation
    df = spark.read.table(table_name)
    result = validator.validate(df, rules)

    # Cache for future use
    validation_cache.set(current_hash, result, ttl=3600)  # 1 hour

    return result

# Incremental validation (only new data)
def validate_incremental_only(table_name: str, rules: dict):
    # Only validate records since last check
    df = spark.read.table(table_name)
    new_records = df.filter(
        f"ingestion_date > '{last_validation_date}'"
    )

    print(f"Validating {new_records.count():,} new records")
    print(f"Skipping {df.count() - new_records.count():,} already validated")

    result = validator.validate(new_records, rules)
    return result

# Cost report
report = cost_tracker.generate_report(period="monthly")
print(f"Total validation costs: ${report.total_cost:.2f}")
print(f"Savings from caching: ${report.caching_savings:.2f}")
print(f"Savings from sampling: ${report.sampling_savings:.2f}")
```

##  Security Integration Examples

### PII Detection in Quality Checks
```python
from data_validator import DataValidator
from pii_detector import PIIDetector  # from sa-01

validator = DataValidator()
pii_detector = PIIDetector()

# Comprehensive quality + security validation
def validate_with_pii_check(df, table_name: str):
    # Standard quality checks
    quality_result = validator.validate(df, quality_rules)

    # PII detection
    pii_result = pii_detector.scan_dataframe(df)

    if pii_result.pii_found:
        print(f" PII detected in {table_name}:")
        for finding in pii_result.findings:
            print(f"  - Column '{finding.column}': {finding.pii_type}")
            print(f"    Confidence: {finding.confidence:.2%}")
            print(f"    Sample count: {finding.count}")

        # Check if PII is in expected columns
        unexpected_pii = [
            f for f in pii_result.findings
            if f.column not in ALLOWED_PII_COLUMNS
        ]

        if unexpected_pii:
            raise DataQualityError(
                f"PII found in unexpected columns: {unexpected_pii}"
            )

    # Combined result
    return {
        "quality_passed": quality_result.passed,
        "pii_compliant": len(unexpected_pii) == 0,
        "quality_failures": quality_result.failures,
        "pii_findings": pii_result.findings
    }
```

### Data Lineage in Quality Reports
```python
from data_validator import DataValidator
from data_lineage import LineageTracker

validator = DataValidator()
lineage_tracker = LineageTracker()

def validate_with_lineage(table_name: str, rules: dict):
    df = spark.read.table(table_name)

    # Run validation
    result = validator.validate(df, rules)

    # Track quality in lineage
    lineage_tracker.log_quality_check(
        dataset=table_name,
        timestamp=datetime.now(),
        passed=result.passed,
        quality_score=result.quality_score,
        failed_rules=[f.rule for f in result.failures]
    )

    # If quality check fails, trace back to source
    if not result.passed:
        lineage = lineage_tracker.get_lineage(table_name)
        print(f"Quality issue in {table_name}")
        print(f"Source: {lineage.source}")
        print(f"Transformations: {lineage.transformations}")

        # Check quality of upstream sources
        for source in lineage.sources:
            source_quality = validator.get_quality_history(source)
            print(f"  {source}: {source_quality.latest_score:.2f}")

    return result
```

##  Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Completeness** | Null rate | <1% | Data validator |
| | Required field coverage | 100% | Data validator |
| **Accuracy** | Schema validation pass rate | >99% | Data validator |
| | Data type conformance | 100% | Data profiler |
| **Consistency** | Cross-table referential integrity | 100% | Data validator |
| | Format standardization | >98% | Data validator |
| **Validity** | Business rule compliance | >98% | Data validator |
| | Range constraint violations | <1% | Data validator |
| **Timeliness** | Data freshness (SLA) | <1 hour | Azure Monitor |
| | Staleness detection | 0 tables | Data profiler |
| **Uniqueness** | Duplicate rate | <0.1% | Data validator |
| | Primary key violations | 0 | Data validator |
| **Overall** | Composite quality score | >95% | Quality dashboard |
| | Quality SLA compliance | >99% | Quality dashboard |

##  Data Quality Pipeline

### Automated Quality Framework
```python
from data_validator import DataValidator
from quality_dashboard import QualityDashboard
from alert_manager import AlertManager

class DataQualityFramework:
    def __init__(self):
        self.validator = DataValidator()
        self.dashboard = QualityDashboard()
        self.alerter = AlertManager()

    def validate_table(self, table_name: str, layer: str):
        """
        Validate table with layer-specific rules
        """
        # Load rules for layer
        rules = self.load_rules(table_name, layer)

        # Read data
        df = spark.read.table(table_name)

        # Profile data
        profile = DataProfiler().profile(df)

        # Validate
        result = self.validator.validate(df, rules)

        # Calculate quality score
        quality_score = self.calculate_quality_score(result, profile)

        # Update dashboard
        self.dashboard.update(
            table_name=table_name,
            quality_score=quality_score,
            profile=profile,
            validation_result=result
        )

        # Check SLA
        sla_threshold = self.get_sla_threshold(table_name)
        if quality_score < sla_threshold:
            self.alerter.send_alert(
                severity="high",
                title=f"Quality SLA Breach: {table_name}",
                message=f"Quality score {quality_score:.2f} below threshold {sla_threshold:.2f}",
                failures=result.failures
            )

        # Quarantine if critical failures
        if result.has_critical_failures:
            self.quarantine_bad_data(table_name, result)

        return result

    def load_rules(self, table_name: str, layer: str):
        """
        Load validation rules from configuration
        """
        # Bronze layer: Basic schema validation
        if layer == "bronze":
            return {
                "schema_validation": True,
                "null_checks": ["id", "timestamp"],
                "type_checks": True
            }

        # Silver layer: Comprehensive validation
        elif layer == "silver":
            return {
                "schema_validation": True,
                "completeness_checks": True,
                "validity_checks": True,
                "consistency_checks": True,
                "uniqueness_checks": True
            }

        # Gold layer: Business rule validation
        elif layer == "gold":
            return {
                "business_rules": self.load_business_rules(table_name),
                "aggregation_checks": True,
                "referential_integrity": True
            }

# Usage
framework = DataQualityFramework()

# Validate Bronze layer
framework.validate_table("bronze.events", layer="bronze")

# Validate Silver layer
framework.validate_table("silver.events_clean", layer="silver")

# Validate Gold layer
framework.validate_table("gold.daily_metrics", layer="gold")
```

##  Integration Workflow

### End-to-End Quality Process
```
1. Data Ingestion (de-02)
   ↓
2. Bronze Layer Quality Check (de-03)
   - Schema validation
   - Basic completeness
   ↓
3. Silver Layer Quality Check (de-03)
   - Comprehensive validation
   - PII detection (sa-01)
   - Data profiling
   ↓
4. Quarantine Bad Data
   - Dead letter queue
   - Manual review process
   ↓
5. Gold Layer Quality Check (de-03)
   - Business rule validation
   - Aggregation checks
   ↓
6. Feature Quality Check (ml-02)
   - Feature distribution
   - Drift detection (mo-05)
   ↓
7. Quality Monitoring (do-08)
   - Dashboard updates
   - Trend analysis
   - Alerting
   ↓
8. Continuous Improvement
   - Root cause analysis
   - Rule optimization
   - SLA tuning
```

##  Quick Wins

1. **Implement schema validation** - Catch breaking changes immediately
2. **Add null checks on critical fields** - Prevent downstream failures
3. **Set up duplicate detection** - Reduce storage costs
4. **Enable data profiling** - Understand data distribution
5. **Create quality dashboard** - Visibility for stakeholders
6. **Implement PII scanning** - Prevent compliance violations
7. **Add anomaly detection** - Catch unusual patterns early
8. **Set up quality alerts** - Reduce MTTR for data issues
9. **Use sampling for validation** - 70-90% cost reduction
10. **Track quality trends** - Proactive quality improvement
