# Data Engineering - Advanced Skills

Extended skills for modern data stack including dbt, data contracts, reverse ETL, and data mesh.

## 🎯 Trigger Keywords

- "dbt", "data transformation", "analytics engineering"
- "data contracts", "schema enforcement", "SLAs"
- "reverse ETL", "operational analytics", "activation"
- "data mesh", "domain ownership", "federated"
- "semantic layer", "metrics", "headless BI"

---

## de-10: Reverse ETL

### When to Use

- Syncing warehouse data to operational systems
- Activating data in CRM/marketing tools
- Operational analytics
- Real-time customer data platforms

### Skills

```yaml
reverse_etl:
  concept:
    description: "Sync data warehouse → operational systems"
    flow: "Warehouse → Transform → Destinations"

  platforms:
    - Census
    - Hightouch
    - Polytomic
    - RudderStack
    - Custom (Airflow + APIs)

  destinations:
    crm:
      - Salesforce
      - HubSpot
      - Pipedrive

    marketing:
      - Braze
      - Iterable
      - Klaviyo
      - Facebook Ads
      - Google Ads

    product:
      - Intercom
      - Amplitude
      - Mixpanel

    support:
      - Zendesk
      - Freshdesk

  patterns:
    - Full sync (initial load)
    - Incremental sync (changes only)
    - Real-time CDC
    - Scheduled batch

  use_cases:
    - Customer 360 to CRM
    - Lead scoring to sales
    - Churn prediction to CS
    - Personalization to marketing
```

### Best Practices

```yaml
reverse_etl:
  - Define clear ownership (who triggers?)
  - Implement idempotency (safe reruns)
  - Handle API rate limits
  - Monitor sync failures
  - Version destination schemas

integration:
  → de-02 (ETL): Source data quality
  → sa-01 (Security): PII handling
  → dg-02 (Governance): Lineage tracking
```

---

## de-11: Data Contracts

### When to Use

- Enforcing schema agreements
- Producer-consumer SLAs
- Breaking change prevention
- Data quality guarantees

### Skills

```yaml
data_contracts:
  definition:
    description: "Formal agreements between data producers/consumers"
    elements:
      - Schema definition
      - Quality expectations
      - SLAs (freshness, availability)
      - Ownership information
      - Semantic meaning

  specification_formats:
    - DataContract Spec (Open Standard)
    - Protocol Buffers
    - Avro schemas
    - JSON Schema
    - dbt contracts

  enforcement:
    schema:
      - Schema registry (Confluent, AWS Glue)
      - dbt contracts
      - Great Expectations

    runtime:
      - Schema validation on write
      - Contract testing in CI/CD
      - Breaking change detection

    monitoring:
      - SLA tracking
      - Quality metrics
      - Freshness checks

  governance:
    - Contract versioning
    - Deprecation policies
    - Consumer notification
    - Approval workflows
```

### Contract Template

```yaml
# data-contract.yaml
dataContractSpecification: 1.0.0
info:
  title: Customer Orders
  version: 1.0.0
  owner: data-platform-team

servers:
  production:
    type: snowflake
    database: analytics
    schema: gold

models:
  orders:
    description: "Order facts table"
    columns:
      order_id:
        type: string
        required: true
        unique: true
      customer_id:
        type: string
        required: true

quality:
  freshness:
    max_delay_hours: 1
  completeness:
    min_percent: 99.5

sla:
  availability: 99.9%
  response_time_p99: 5s
```

### Integration

```
→ dg-03 (Governance): Quality framework
→ de-03 (Data): Data quality
→ do-01 (DevOps): CI/CD testing
→ dg-01 (Governance): Data catalog
```

---

## de-12: Semantic Layer / Metrics Layer

### When to Use

- Consistent metric definitions
- Self-service analytics
- API-driven metrics
- Headless BI

### Skills

```yaml
semantic_layer:
  concept:
    description: "Single source of truth for business metrics"
    benefits:
      - Consistent definitions
      - Reusable across tools
      - API-driven access
      - Version controlled

  platforms:
    open_source:
      - dbt Semantic Layer / MetricFlow
      - Cube.js
      - Minerva (Airbnb)

    commercial:
      - Looker (LookML)
      - AtScale
      - Kyligence

  components:
    entities:
      description: "Business objects (customer, order, product)"

    measures:
      description: "Aggregations (sum, avg, count)"

    dimensions:
      description: "Attributes for slicing (date, region)"

    metrics:
      description: "Business logic combining above"

  integration_patterns:
    - BI tools (Tableau, Power BI, Looker)
    - Notebooks (Jupyter, Databricks)
    - Applications (via API)
    - AI/LLM (natural language to SQL)
```

### Metric Definition

```yaml
# dbt semantic layer example
semantic_models:
  - name: orders
    model: ref('fct_orders')
    entities:
      - name: order_id
        type: primary
      - name: customer_id
        type: foreign
    measures:
      - name: order_total
        agg: sum
        expr: amount
    dimensions:
      - name: order_date
        type: time

metrics:
  - name: revenue
    type: simple
    type_params:
      measure: order_total

  - name: revenue_per_customer
    type: derived
    type_params:
      expr: revenue / count_distinct(customer_id)
```

### Integration

```
→ ds-08 (Data Sci): Visualization
→ dg-01 (Governance): Catalog
→ ai-02 (AI): LLM-to-SQL
→ be-01 (Backend): API access
```

---

## de-13: Data Mesh

### When to Use

- Large organizations with multiple domains
- Decentralized data ownership
- Scalability challenges with central team
- Domain-driven design

### Skills

```yaml
data_mesh:
  principles:
    1_domain_ownership:
      description: "Domains own their data as products"
      implementation:
        - Domain teams build/maintain data products
        - Clear ownership and accountability
        - Domain-specific data models

    2_data_as_product:
      description: "Treat data as a product with consumers"
      characteristics:
        - Discoverable (in catalog)
        - Addressable (clear endpoints)
        - Trustworthy (quality, freshness)
        - Self-describing (schema, docs)
        - Interoperable (standards)
        - Secure (access controls)

    3_self_serve_platform:
      description: "Platform enables domains to create data products"
      capabilities:
        - Infrastructure provisioning
        - Compute/storage allocation
        - CI/CD pipelines
        - Monitoring/observability
        - Access control

    4_federated_governance:
      description: "Global standards, local autonomy"
      aspects:
        - Global interoperability standards
        - Global security/compliance
        - Local schema design
        - Local quality ownership

  implementation:
    data_products:
      - Input ports (data ingestion)
      - Transformation (dbt, Spark)
      - Output ports (APIs, tables, streams)
      - Observability (metrics, logs)

    platform:
      - Kubernetes-based compute
      - Object storage (S3, GCS, ADLS)
      - Catalog (DataHub, Atlan)
      - Access management (IAM)

    governance:
      - Schema registry
      - Data contracts
      - Quality SLAs
      - Access policies
```

### Migration Path

```yaml
mesh_adoption:
  phase_1:
    - Identify domain boundaries
    - Pilot 1-2 domains
    - Build platform foundation

  phase_2:
    - Expand to more domains
    - Implement federated governance
    - Build self-serve capabilities

  phase_3:
    - Full decentralization
    - Mature platform
    - Cross-domain data products
```

### Integration

```
→ dg-01 to dg-06 (Governance): All skills
→ pe-01 (Platform): Self-service infra
→ de-11 (Data): Contracts between domains
→ sa-04 (Security): Access control
```

---

## Skill Dependencies

| Skill               | Requires     | Enables               |
| ------------------- | ------------ | --------------------- |
| de-10 (Reverse ETL) | de-02, dg-02 | Operational analytics |
| de-11 (Contracts)   | dg-03, do-01 | Quality guarantees    |
| de-12 (Semantic)    | dg-01, de-01 | Consistent metrics    |
| de-13 (Mesh)        | dg-\*, pe-01 | Scalable data org     |

## Quick Reference

```yaml
reverse_etl: "I need to sync warehouse to operational tools"
data_contracts: "I need to enforce schema agreements"
semantic_layer: "I need consistent metric definitions"
data_mesh: "I need decentralized data ownership"
```
