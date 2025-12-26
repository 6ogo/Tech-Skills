# dg-06: Compliance & Privacy

## Overview

GDPR compliance automation, data retention policies, right to be forgotten, consent management, and privacy impact assessments.

## Key Capabilities

- **GDPR Automation**: Automated compliance checks
- **Data Retention**: Automated data lifecycle
- **Right to be Forgotten**: Delete personal data on request
- **Consent Management**: Track user consent
- **Privacy Impact Assessments**: Risk assessment

## Implementation

```python
# Right to be forgotten
def delete_user_data(user_id):
    """Delete all personal data for a user"""
    tables = [
        'customers', 'orders', 'payments',
        'preferences', 'analytics_events'
    ]

    for table in tables:
        spark.sql(f"""
            DELETE FROM {table}
            WHERE user_id = '{user_id}'
        """)

    # Log deletion for audit
    log_gdpr_deletion(user_id, tables)

# Data retention policy
def apply_retention_policy():
    """Delete data past retention period"""
    spark.sql("""
        DELETE FROM customer_events
        WHERE event_date < DATE_SUB(CURRENT_DATE(), 730)  -- 2 years
    """)
```

## Integration

**Connects with:** sa-01 (PII Detection), dg-01 (Catalog), dg-04 (Access Control)
