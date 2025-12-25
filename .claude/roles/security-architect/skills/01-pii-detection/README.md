# Skill 1: PII Detection & Data Privacy

## 🎯 Overview
Automated PII detection, masking, and GDPR compliance tools.

## 🔗 Connections
- **Data Engineer**: PII masking in data pipelines (de-01, de-02, de-03)
- **AI Engineer**: PII filtering before RAG indexing (ai-02, ai-03)
- **ML Engineer**: Remove PII before model training (ml-01, ml-02)
- **Data Scientist**: PII detection in analysis datasets (ds-01)
- **DevOps**: Automated PII scanning in CI/CD (do-01, do-02)
- **FinOps**: Track compliance audit costs (fo-01)
- **All Roles**: GDPR compliance and data protection

## 🛠️ Tools Included

### 1. `pii_detector.py`
PII detection using Microsoft Presidio and custom patterns.

### 2. `data_anonymizer.py`
Data anonymization with multiple strategies (masking, hashing, generalization).

### 3. `gdpr_compliance_checker.py`
GDPR compliance validation and audit trails.

### 4. `consent_manager.py`
User consent tracking and right-to-erasure automation.

### 5. `pii_audit_queries.sql`
SQL queries for PII inventory and audit logs.

## 📊 PII Types Detected
- Email addresses
- Phone numbers
- Credit cards
- SSN / National IDs
- IP addresses
- Addresses
- Names
- Dates of birth

## 🚀 Quick Start

```python
from pii_detector import PIIDetector
from data_anonymizer import DataAnonymizer

# Detect PII
detector = PIIDetector()
pii_findings = detector.analyze_text(
    "Contact John Smith at john.smith@email.com or 555-123-4567"
)

# Anonymize data
anonymizer = DataAnonymizer()
anonymized = anonymizer.mask_dataframe(
    df=customer_df,
    pii_columns=["email", "phone", "ssn"]
)
```

## 📚 Best Practices

### Integration with Data Pipelines (Data Engineer)

1. **Bronze Layer PII Scanning**
   - Scan all raw data at ingestion
   - Tag datasets containing PII
   - Block high-risk PII from pipeline
   - Maintain PII inventory
   - Reference: Data Engineer de-01 (Lakehouse Architecture)

2. **Silver Layer PII Masking**
   - Apply masking transformations
   - Implement k-anonymity for aggregations
   - Track masked vs raw data lineage
   - Validate masking effectiveness
   - Reference: Data Engineer de-01, de-03

3. **Gold Layer Compliance**
   - Ensure no PII in analytics layers
   - Implement row-level security
   - Audit PII access logs
   - Enable right-to-erasure automation
   - Reference: Data Engineer de-01

### AI/ML Integration

4. **Pre-Training PII Removal**
   - Scan training data before ML experiments
   - Remove PII from feature engineering
   - Anonymize datasets for model development
   - Track data provenance for compliance
   - Reference: ML Engineer ml-01, ml-02

5. **RAG Knowledge Base Protection**
   - Scan documents before embedding
   - Prevent PII indexing in vector databases
   - Filter PII from LLM context
   - Audit knowledge base for compliance
   - Reference: AI Engineer ai-02 (RAG Pipeline)

6. **LLM Input/Output Filtering**
   - Detect PII in user prompts
   - Redact PII from LLM responses
   - Log PII exposure incidents
   - Implement real-time PII alerts
   - Reference: AI Engineer ai-01, ai-07

### Automation & CI/CD (DevOps Integration)

7. **Automated PII Scanning**
   - Integrate PII detection in CI/CD pipelines
   - Block commits containing PII
   - Scan code, configs, and test data
   - Automate compliance reports
   - Reference: DevOps do-01 (CI/CD), do-02 (Testing)

8. **Continuous Compliance Monitoring**
   - Schedule regular PII scans
   - Alert on new PII discoveries
   - Track remediation progress
   - Generate audit trails
   - Reference: DevOps do-08 (Monitoring)

### Cost Management (FinOps Integration)

9. **Optimize PII Scanning Costs**
   - Use sampling for large datasets
   - Cache PII detection results
   - Right-size scanning compute
   - Monitor compliance operation costs
   - Reference: FinOps fo-01, fo-06

### Enterprise Governance

10. **Data Governance Framework**
    - Classify data by sensitivity level
    - Implement data handling policies
    - Track PII across all systems
    - Enable compliance reporting
    - Reference: Security Architect sa-06 (Data Governance)

11. **GDPR Right-to-Erasure**
    - Automate data deletion requests
    - Track PII deletion across systems
    - Verify erasure completeness
    - Maintain deletion audit logs
    - Reference: Security Architect sa-06

## 💰 Cost Optimization Examples

### Efficient PII Scanning
```python
from pii_detector import PIIDetector
from finops_tracker import ComplianceCostTracker

detector = PIIDetector()
cost_tracker = ComplianceCostTracker()

@cost_tracker.track_scan_cost
def smart_pii_scan(df: pd.DataFrame, sample_size: int = 10000):
    # Sample for initial detection (cost savings)
    if len(df) > sample_size:
        sample_df = df.sample(n=sample_size, random_state=42)
        pii_columns = detector.find_pii_columns(sample_df)

        # Full scan only on suspected PII columns
        results = {}
        for col in pii_columns:
            results[col] = detector.analyze_column(df[col])
    else:
        results = detector.analyze_dataframe(df)

    return results

# Cost report
report = cost_tracker.monthly_report()
print(f"PII scanning costs: ${report.total_cost:.2f}")
print(f"Datasets scanned: {report.datasets_scanned}")
```

## 🚀 Automated PII Protection Pipeline

### CI/CD Integration
```yaml
# .github/workflows/pii-protection.yml
name: PII Protection

on:
  push:
    paths:
      - 'data/**'
      - 'pipelines/**'
  pull_request:

jobs:
  pii-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Scan code for PII patterns
        run: |
          python scripts/scan_code_for_pii.py \
            --fail-on-detection \
            --exclude-patterns .gitignore

      - name: Scan test data
        run: |
          python scripts/scan_test_data.py \
            --redact-if-found \
            --report-path reports/pii_scan.json

      - name: Validate data pipelines
        run: |
          python scripts/validate_pii_masking.py \
            --pipeline-config pipelines/config.yaml

      - name: Generate compliance report
        run: python scripts/generate_compliance_report.py

      - name: Upload scan results
        uses: actions/upload-artifact@v3
        with:
          name: pii-scan-results
          path: reports/
```

### Data Pipeline Integration
```python
from bronze_ingestion import BronzeLoader
from pii_detector import PIIDetector
from data_anonymizer import DataAnonymizer

detector = PIIDetector()
anonymizer = DataAnonymizer()

def secure_data_pipeline(source_data: str, output_table: str):
    # Bronze: Ingest with PII detection
    bronze = BronzeLoader()
    df = bronze.ingest(source_data)

    # Detect PII
    pii_findings = detector.analyze_dataframe(df)

    if pii_findings:
        # Log for compliance
        log_pii_detection(
            dataset=output_table,
            pii_types=[f.type for f in pii_findings],
            timestamp=datetime.now()
        )

        # Silver: Mask PII
        df_masked = anonymizer.mask_dataframe(
            df,
            pii_columns=[f.column for f in pii_findings],
            strategy="hash"  # Deterministic for joins
        )

        # Store both raw (encrypted) and masked
        bronze.save(df, f"{output_table}_raw_encrypted")
        bronze.save(df_masked, f"{output_table}_masked")

        # Alert security team
        if any(f.severity == "high" for f in pii_findings):
            send_security_alert(pii_findings)
    else:
        bronze.save(df, output_table)

    return pii_findings
```

## 📊 Enhanced Metrics

| Metric | Target | Tool |
|--------|--------|------|
| **PII Detection Coverage** | 100% of datasets | Automated scanning |
| **False Positive Rate** | <5% | Model tuning |
| **Detection Latency** | <1min per GB | Performance monitoring |
| **Masking Accuracy** | >99.9% | Validation tests |
| **Compliance Audit Pass Rate** | 100% | Audit logs |
| **Mean Time to Remediate** | <24 hours | Incident tracking |

## 🔄 Integration Workflow

### End-to-End PII Protection
```
1. Data Ingestion (de-01)
   ↓
2. PII Detection (sa-01) → Log Finding
   ↓
3. Risk Assessment (High/Medium/Low)
   ↓
4. Masking/Encryption (sa-01)
   ↓
5. Quality Validation (de-03)
   ↓
6. Compliance Audit Log (sa-06)
   ↓
7. Downstream Processing (ML, Analytics)
   ├── Model Training (ml-01) - PII-free
   ├── RAG Indexing (ai-02) - PII-free
   └── EDA Reports (ds-01) - Masked
   ↓
8. Continuous Monitoring (do-08)
   ↓
9. Cost Tracking (fo-01)
```

## 🎯 Quick Wins

1. **Integrate PII scanning in CI/CD** - Prevent PII commits
2. **Automate Bronze layer scanning** - Detect PII at ingestion
3. **Implement PII masking in Silver** - Protect downstream systems
4. **Enable LLM input filtering** - Prevent PII in prompts
5. **Set up compliance dashboards** - Real-time PII tracking
6. **Automate right-to-erasure** - GDPR compliance automation
