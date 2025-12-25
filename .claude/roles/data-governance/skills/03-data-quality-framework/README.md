# dg-03: Data Quality Framework

## Overview

Implement automated data quality validation, scoring, monitoring, and issue remediation workflows.

## Key Capabilities

- **Quality Rules Definition**: Completeness, accuracy, consistency
- **Automated Validation**: Real-time quality checks
- **Quality Scoring**: Quantifiable quality metrics
- **Quality Monitoring**: Continuous quality tracking
- **Issue Remediation**: Workflows for quality issues

## Tools & Technologies

- **Great Expectations**: Python data validation
- **Soda**: Data quality as code
- **dbt tests**: Quality tests in dbt
- **Azure Data Quality**: Native Azure solution

## Implementation

### 1. Quality Rules with Great Expectations

```python
# Define quality expectations
import great_expectations as gx

def create_quality_suite(context, table_name):
    """Create data quality test suite"""
    suite = context.add_expectation_suite(
        expectation_suite_name=f"{table_name}_quality_suite"
    )

    validator = context.get_validator(
        batch_request=batch_request,
        expectation_suite_name=suite.expectation_suite_name
    )

    # Completeness checks
    validator.expect_column_values_to_not_be_null(column="customer_id")
    validator.expect_column_values_to_not_be_null(column="order_date")

    # Accuracy checks
    validator.expect_column_values_to_be_between(
        column="age",
        min_value=0,
        max_value=120
    )

    # Consistency checks
    validator.expect_column_values_to_match_regex(
        column="email",
        regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )

    validator.save_expectation_suite()
    return validator
```

### 2. Quality Scoring

```python
# Calculate quality score
def calculate_quality_score(validation_results):
    """Calculate overall quality score"""
    total_checks = validation_results.statistics['evaluated_expectations']
    successful_checks = validation_results.statistics['successful_expectations']

    score = (successful_checks / total_checks) * 100

    # Categorize quality
    if score >= 95:
        quality_level = "Excellent"
    elif score >= 85:
        quality_level = "Good"
    elif score >= 70:
        quality_level = "Acceptable"
    else:
        quality_level = "Poor"

    return {
        'score': score,
        'level': quality_level,
        'total_checks': total_checks,
        'passed_checks': successful_checks
    }
```

### 3. Automated Monitoring

```python
# Set up quality monitoring
def setup_quality_monitoring(checkpoint_name):
    """Configure automated quality monitoring"""
    checkpoint_config = {
        "name": checkpoint_name,
        "config_version": 1.0,
        "template_name": "default",
        "run_name_template": "%Y%m%d-%H%M%S",
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "production_data",
                    "data_connector_name": "default_inferred_data_connector_name",
                    "data_asset_name": "customers"
                },
                "expectation_suite_name": "customers_quality_suite"
            }
        ],
        "action_list": [
            {
                "name": "store_validation_result",
                "action": {"class_name": "StoreValidationResultAction"}
            },
            {
                "name": "send_slack_notification",
                "action": {
                    "class_name": "SlackNotificationAction",
                    "slack_webhook": "${SLACK_WEBHOOK}",
                    "notify_on": "failure"
                }
            }
        ]
    }

    context.add_checkpoint(**checkpoint_config)
```

### 4. Issue Remediation Workflow

```python
# Create remediation workflow
def create_remediation_workflow(quality_issues):
    """Create tickets for quality issues"""
    from azure.devops import AzureDevOpsClient

    client = AzureDevOpsClient()

    for issue in quality_issues:
        work_item = {
            'title': f"Data Quality Issue: {issue['column']}",
            'description': issue['description'],
            'priority': issue['severity'],
            'assigned_to': issue['data_owner'],
            'tags': ['data-quality', issue['table']]
        }

        client.create_work_item(
            project='DataGovernance',
            work_item_type='Bug',
            fields=work_item
        )
```

## Best Practices

1. **Start Simple** - Begin with critical fields, expand coverage
2. **Automate Everything** - Manual checks don't scale
3. **Clear Ownership** - Assign quality issues to data owners
4. **Threshold Alerts** - Alert on quality score drops
5. **Historical Tracking** - Monitor quality trends over time

## Cost Optimization

- Run quality checks incrementally (only new/changed data)
- Use sampling for large datasets
- Cache validation results
- Right-size validation compute

## Integration

**Connects with:**
- de-01 (Lakehouse): Validate lakehouse data
- de-03 (Data Quality): Engineering quality checks
- dg-01 (Catalog): Link quality scores to assets
- dg-02 (Lineage): Trace quality issues to source

## Quick Win

Implement completeness checks on 5 critical fields in your most important table. Show before/after quality scores.
