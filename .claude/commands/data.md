# Data Lead Command

Route to the Data Lead Agent for data engineering, governance, and database tasks.

## Usage

```
/data [your request]
```

## Examples

```
/data build ETL pipeline
/data create data catalog
/data optimize database queries
/data implement data quality
```

## What Happens

1. **Orchestrator** receives your request
2. **Data Lead** takes ownership and analyzes
3. **Specialists** are assigned:
   - Data Engineer (pipelines, lakehouse, streaming)
   - Data Governance (catalog, lineage, quality)
   - Database Admin (optimization, backup, migrations)

## Available Skills

| Agent           | Skills                                                                                             |
| --------------- | -------------------------------------------------------------------------------------------------- |
| Data Engineer   | de-01 to de-09 (lakehouse, ETL, quality, streaming, performance, cloud, DB, marketing, monitoring) |
| Data Governance | dg-01 to dg-06 (catalog, lineage, quality, access, MDM, compliance)                                |
| Database Admin  | db-01 to db-07 (optimization, indexes, backup, replication, tuning, migrations, transactions)      |

## Mandatory Collaborations

- **Security Lead** → Always for PII/sensitive data
- **Platform Lead** → For infrastructure/deployment
- **AI/ML Lead** → For ML feature pipelines
