# Skill 1: Automated Exploratory Data Analysis (EDA)

##  Overview
Automated EDA with statistical profiling, visualization, and insight generation.

##  Connections
- **Data Engineer**: Provides feedback on data quality issues (de-01, de-03)
- **ML Engineer**: Identifies promising features for modeling (ml-01, ml-02)
- **MLOps**: Experiment tracking for EDA findings (mo-01)
- **AI Engineer**: Generates insights for LLM context (ai-02, ai-03)
- **Security Architect**: PII detection in datasets (sa-01)
- **FinOps**: Cost-effective analytics compute (fo-06)
- **DevOps**: Automated reporting pipelines (do-01)

##  Tools Included

### 1. `eda_generator.py`
Automated EDA report generation with ydata-profiling.

### 2. `statistical_analyzer.py`
Statistical tests, distributions, and correlations.

### 3. `visualization_suite.py`
Interactive visualizations with Plotly.

### 4. `insight_extractor.py`
Automated insight extraction and anomaly detection.

### 5. `eda_queries.sql`
SQL templates for common analytical queries.

##  Key Outputs
- Automated profiling reports (HTML)
- Statistical summaries
- Correlation matrices
- Distribution plots
- Anomaly detection alerts

##  Quick Start

```python
from eda_generator import EDAGenerator

# Initialize
eda = EDAGenerator()

# Load data
df = pd.read_csv("customer_data.csv")

# Generate comprehensive report
report = eda.generate_report(
    df=df,
    title="Customer Data Analysis",
    output_file="eda_report.html"
)

# Extract key insights
insights = eda.extract_insights(df)
print(insights)
```

##  Best Practices

### Data Quality & Security (Cross-Role Integration)

1. **PII Detection Before Analysis**
   - Scan datasets for PII before profiling
   - Mask sensitive data in reports and visualizations
   - Track data lineage for compliance
   - Reference: Security Architect sa-01 (PII Detection)

2. **Data Quality Validation**
   - Validate schema before EDA
   - Check completeness, accuracy, consistency
   - Alert Data Engineering team on quality issues
   - Reference: Data Engineer de-03 (Data Quality)

3. **Automated Quality Feedback Loop**
   - Generate data quality scorecards
   - Feed insights back to data pipelines
   - Track quality improvements over time
   - Reference: Data Engineer de-01, de-03

### Cost Optimization (FinOps Integration)

4. **Optimize Compute for Analysis**
   - Use appropriate instance sizes for EDA workloads
   - Auto-shutdown notebooks when idle
   - Sample large datasets intelligently
   - Monitor analysis costs per project
   - Reference: FinOps fo-06 (Compute Optimization)

5. **Efficient Data Sampling**
   - Use stratified sampling for large datasets
   - Profile samples before full dataset analysis
   - Cache intermediate results
   - Minimize data movement and storage
   - Reference: FinOps fo-05, Data Engineer de-01

### MLOps Integration

6. **Track EDA Experiments**
   - Log EDA findings in MLflow/Azure ML
   - Version datasets used for analysis
   - Document feature engineering insights
   - Link EDA to downstream model experiments
   - Reference: MLOps mo-01 (Experiment Tracking)

7. **Feature Discovery Documentation**
   - Document promising features for ML
   - Track feature importance from EDA
   - Share insights with ML Engineering team
   - Maintain feature catalog
   - Reference: ML Engineer ml-02 (Feature Engineering)

### Automation & Deployment (DevOps Integration)

8. **Automated EDA Pipelines**
   - Schedule regular EDA reports for key datasets
   - Automate anomaly detection and alerting
   - Deploy EDA as part of data pipeline monitoring
   - Version control EDA scripts
   - Reference: DevOps do-01 (CI/CD), do-08 (Monitoring)

9. **Reproducible Analysis**
   - Use containerized environments
   - Pin package versions
   - Document analysis dependencies
   - Enable one-click report regeneration
   - Reference: DevOps do-03 (Containerization)

### AI Integration

10. **LLM-Powered Insights**
    - Use LLMs to generate narrative insights
    - Automate insight extraction from distributions
    - Create natural language data summaries
    - Reference: AI Engineer ai-01, ai-07

##  Cost Optimization Examples

### Compute Cost Tracking
```python
from eda_generator import EDAGenerator
from finops_tracker import AnalyticsCostTracker

cost_tracker = AnalyticsCostTracker()

# Track EDA compute costs
@cost_tracker.track_analysis_cost
def run_eda(dataset_path: str):
    eda = EDAGenerator()
    df = pd.read_csv(dataset_path)

    # Smart sampling for large datasets
    if len(df) > 1_000_000:
        df = df.sample(n=100_000, random_state=42)  # Cost savings

    report = eda.generate_report(df)
    return report

# Cost report
report = cost_tracker.monthly_report()
print(f"Total EDA costs: ${report.total_cost:.2f}")
print(f"Cost per analysis: ${report.avg_cost:.2f}")
```

##  Security Best Practices

### PII Masking in Reports
```python
from pii_detector import PIIDetector
from eda_generator import EDAGenerator

detector = PIIDetector()
eda = EDAGenerator()

def secure_eda(df: pd.DataFrame):
    # Detect PII columns
    pii_columns = []
    for col in df.columns:
        sample = df[col].astype(str).sample(min(100, len(df)))
        if detector.contains_pii(sample.tolist()):
            pii_columns.append(col)

    # Mask PII before EDA
    df_masked = df.copy()
    for col in pii_columns:
        df_masked[col] = "***MASKED***"

    # Generate report on masked data
    report = eda.generate_report(
        df_masked,
        title="Customer Data Analysis (PII Masked)"
    )

    return report, pii_columns
```

##  Integration Workflow

### End-to-End EDA Pipeline
```
1. Data Ingestion (de-01)
   ↓
2. PII Detection (sa-01)
   ↓
3. Data Quality Check (de-03)
   ↓
4. Automated EDA (ds-01)
   ↓
5. Track Findings (mo-01)
   ↓
6. Feature Discovery (ml-02)
   ↓
7. Generate Insights (ai-07)
   ↓
8. Share Report (Automated)
   ↓
9. Monitor Costs (fo-06)
```

##  Quick Wins

1. **Automate PII detection** - Prevent compliance violations in reports
2. **Set up cost tracking** - Monitor analysis compute spending
3. **Enable auto-shutdown** - Stop idle notebooks to save costs
4. **Sample large datasets** - Faster EDA at lower cost
5. **Track EDA experiments** - Link insights to model performance
6. **Automate report generation** - Schedule weekly data profiling
