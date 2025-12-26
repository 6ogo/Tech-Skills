# dg-02: Data Lineage

## Overview

Track end-to-end data lineage for impact analysis, root cause analysis, and regulatory compliance.

## Key Capabilities

- **End-to-End Lineage**: From source to consumption
- **Impact Analysis**: Understand downstream impacts
- **Root Cause Analysis**: Trace issues to source
- **Column-Level Lineage**: Field-level tracking
- **Transformation Documentation**: Track data transformations

## Tools & Technologies

- **Azure Purview**: Native lineage tracking
- **OpenLineage**: Open standard for lineage
- **Marquez**: Metadata service for lineage
- **Spline**: Spark lineage tracking

## Implementation

### 1. Lineage Extraction

```python
# Extract lineage from Spark jobs
from spline import SplineAgent

def track_spark_lineage(spark_session):
    """Enable lineage tracking for Spark"""
    spark_session.sparkContext.setLogLevel("INFO")

    # Initialize Spline agent
    SplineAgent.builder() \
        .appName("data-pipeline") \
        .mode("REQUIRED") \
        .url("http://spline-server:9090") \
        .build()
```

### 2. Column-Level Lineage

```sql
-- Azure Purview automatically tracks column lineage
-- Example transformation with lineage
CREATE VIEW customer_360 AS
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name as full_name,  -- Lineage: derived
    o.total_orders,
    p.total_payments
FROM customers c
LEFT JOIN order_summary o ON c.customer_id = o.customer_id
LEFT JOIN payment_summary p ON c.customer_id = p.customer_id;
```

### 3. Impact Analysis

```python
# Find downstream dependencies
def get_downstream_impact(asset_id):
    """Find all downstream assets affected by changes"""
    lineage = client.lineage.get_lineage(
        guid=asset_id,
        direction="OUTPUT",
        depth=10
    )

    downstream_assets = []
    for entity in lineage['guidEntityMap'].values():
        downstream_assets.append({
            'name': entity['attributes']['name'],
            'type': entity['typeName'],
            'owner': entity.get('attributes', {}).get('owner')
        })

    return downstream_assets
```

### 4. OpenLineage Integration

```python
# Emit lineage events using OpenLineage
from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState, Run, Job

def emit_lineage_event(job_name, inputs, outputs):
    """Emit lineage event to OpenLineage"""
    client = OpenLineageClient(url="http://lineage-api:5000")

    event = RunEvent(
        eventType=RunState.COMPLETE,
        eventTime="2025-01-01T00:00:00Z",
        run=Run(runId=str(uuid.uuid4())),
        job=Job(namespace="production", name=job_name),
        inputs=inputs,
        outputs=outputs
    )

    client.emit(event)
```

## Best Practices

1. **Automate Collection** - Manual lineage doesn't scale
2. **Column-Level Tracking** - For sensitive data, track field-level
3. **Version Control** - Track lineage changes over time
4. **Clear Visualization** - Make lineage easy to understand
5. **Regular Validation** - Verify lineage accuracy

## Cost Optimization

- Use incremental lineage updates
- Archive old lineage data after retention period
- Cache frequently accessed lineage queries
- Use materialized views for complex lineage

## Integration

**Connects with:**
- de-02 (ETL): Track pipeline lineage
- dg-01 (Catalog): Link assets to lineage
- ml-02 (Feature Engineering): Track feature lineage
- ai-02 (RAG): Track document lineage

## Quick Win

Start with 1 critical data pipeline, manually document lineage, validate accuracy, then automate extraction.
