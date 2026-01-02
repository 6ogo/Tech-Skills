# Skill 4: Real-Time Streaming Pipelines

##  Overview
Build and operate production-grade real-time streaming data pipelines with event processing, stateful transformations, exactly-once semantics, and low-latency analytics.

##  Connections
- **Data Engineer**: Feeds real-time data to lakehouse (de-01, de-02, de-03)
- **ML Engineer**: Real-time feature computation (ml-02, ml-04)
- **MLOps**: Online model serving and monitoring (mo-04, mo-05)
- **AI Engineer**: Real-time RAG updates (ai-02)
- **Data Scientist**: Streaming analytics and dashboards (ds-01)
- **Security Architect**: Event encryption and access control (sa-04, sa-05)
- **FinOps**: Streaming compute cost optimization (fo-01, fo-06)
- **DevOps**: Streaming infrastructure and monitoring (do-03, do-08)
- **System Design**: Event-driven architecture patterns (sd-02, sd-05)

##  Tools Included

### 1. `stream_processor.py`
Unified streaming processor supporting Kafka, Event Hubs, and Kinesis.

### 2. `stateful_transformer.py`
Windowing, aggregations, and stateful operations for streaming data.

### 3. `exactly_once_handler.py`
Idempotency and exactly-once processing guarantees.

### 4. `stream_monitor.py`
Real-time monitoring of lag, throughput, and data quality.

### 5. `stream_schemas.py`
Schema registry integration and evolution management.

##  Architecture

```
Event Sources → Stream Ingestion → Processing → Output Sinks
     ↓              ↓                  ↓            ↓
  IoT/Apps    Kafka/EventHub    Transformations  Lakehouse
  Webhooks    Checkpointing     Aggregations     Real-time DB
  CDC         Partitioning      Windowing        Analytics
```

##  Quick Start

```python
from stream_processor import StreamProcessor
from transformations import window, aggregate

# Initialize stream processor
processor = StreamProcessor(
    source="azure_event_hub",
    connection_string=os.getenv("EVENT_HUB_CONNECTION"),
    consumer_group="streaming-pipeline",
    checkpoint_location="abfss://checkpoints@storage.dfs.core.windows.net"
)

# Define streaming query
stream = processor.read_stream(
    topic="user-events",
    schema=user_event_schema
)

# Transformations with windowing
processed = (
    stream
    .withWatermark("timestamp", "10 minutes")  # Handle late data
    .groupBy(
        window("timestamp", "5 minutes", "1 minute"),  # Sliding window
        "user_id"
    )
    .agg(
        count("*").alias("event_count"),
        countDistinct("session_id").alias("session_count"),
        avg("duration").alias("avg_duration")
    )
)

# Write to multiple sinks
query = (
    processed.writeStream
    .foreachBatch(lambda batch, batch_id: (
        # Write to Delta Lake for historical analysis
        batch.write.format("delta")
            .mode("append")
            .save("abfss://gold@storage.dfs.core.windows.net/user_metrics"),

        # Write to Redis for real-time serving
        write_to_redis(batch),

        # Update feature store for ML
        update_feature_store(batch)
    ))
    .option("checkpointLocation", "abfss://checkpoints@storage.dfs.core.windows.net/user_metrics")
    .trigger(processingTime="1 minute")
    .start()
)

# Monitor stream health
from stream_monitor import StreamMonitor
monitor = StreamMonitor(query)
monitor.track_metrics(["lag", "throughput", "latency"])
```

##  Best Practices

### Streaming Architecture (System Design Integration)

1. **Event-Driven Design**
   - Use pub/sub pattern for decoupling
   - Implement event sourcing for auditability
   - Design idempotent consumers
   - Use dead letter queues for failed events
   - Reference: System Design sd-02 (Event-Driven Architecture)

2. **Partitioning Strategy**
   - Partition by key for ordered processing
   - Balance partition sizes for even load
   - Monitor partition skew
   - Plan for repartitioning as scale grows
   - Reference: System Design sd-03 (Scalability)

3. **Backpressure Handling**
   - Implement rate limiting
   - Use buffering for traffic spikes
   - Auto-scale consumers based on lag
   - Circuit breakers for downstream failures
   - Reference: System Design sd-05 (Resilience Patterns)

### Exactly-Once Semantics

4. **Idempotent Processing**
   - Use deterministic keys for deduplication
   - Implement idempotent writes
   - Track processed message IDs
   - Handle retries gracefully
   - Reference: Data Engineer best practices

5. **Checkpointing Strategy**
   - Frequent checkpoints for fault tolerance
   - Store checkpoints in reliable storage
   - Test checkpoint recovery regularly
   - Monitor checkpoint lag
   - Reference: Data Engineer best practices

6. **Transaction Management**
   - Use transactional writes where possible
   - Implement two-phase commit for distributed transactions
   - Handle partial failures gracefully
   - Maintain strong consistency guarantees
   - Reference: System Design best practices

### Performance Optimization

7. **Throughput Optimization**
   - Batch processing where latency allows
   - Optimize serialization (Avro > JSON)
   - Use compression for network transfer
   - Parallel processing with proper partitioning
   - Reference: Data Engineer de-05 (Performance)

8. **Latency Optimization**
   - Minimize transformation complexity
   - Optimize window sizes for use case
   - Use in-memory state stores
   - Reduce network hops
   - Reference: Data Engineer de-05 (Performance)

9. **State Management**
   - Use RocksDB for large state
   - Implement state compaction
   - Monitor state store size
   - Backup state periodically
   - Reference: Data Engineer best practices

### Cost Optimization (FinOps Integration)

10. **Right-Size Streaming Clusters**
    - Monitor CPU and memory utilization
    - Auto-scale based on lag and throughput
    - Use spot instances for dev/test
    - Consolidate low-volume streams
    - Reference: FinOps fo-06 (Compute Optimization)

11. **Optimize Data Transfer Costs**
    - Compress events before transmission
    - Use regional endpoints to avoid egress
    - Batch small messages
    - Filter early to reduce downstream processing
    - Reference: FinOps fo-05 (Storage Optimization)

12. **Retention and Tiering**
    - Set appropriate retention policies
    - Tier old data to cheaper storage
    - Archive to blob storage for compliance
    - Monitor storage growth
    - Reference: FinOps fo-05 (Storage Optimization)

### Security (Security Architect Integration)

13. **Event Encryption**
    - Encrypt data in transit (TLS)
    - Encrypt data at rest in event store
    - Use managed keys from Key Vault
    - Rotate encryption keys regularly
    - Reference: Security Architect sa-04 (Encryption)

14. **Access Control**
    - Use RBAC for topic access
    - Implement consumer group isolation
    - Audit access to streaming data
    - Managed identities for authentication
    - Reference: Security Architect sa-02 (IAM)

15. **PII in Streaming Data**
    - Detect and mask PII in real-time
    - Implement data retention policies
    - Log PII access for compliance
    - Right-to-erasure for GDPR
    - Reference: Security Architect sa-01 (PII Detection)

### Monitoring & Observability (DevOps Integration)

16. **Streaming Metrics**
    - Monitor consumer lag continuously
    - Track throughput (events/sec)
    - Measure end-to-end latency
    - Alert on processing failures
    - Reference: DevOps do-08 (Monitoring & Observability)

17. **Distributed Tracing**
    - Trace events end-to-end
    - Correlate events across systems
    - Identify bottlenecks
    - Debug processing issues
    - Reference: DevOps do-08 (Monitoring & Observability)

### Azure-Specific Best Practices

18. **Azure Event Hubs**
    - Use capture for automatic archival
    - Enable auto-inflate for throughput
    - Partition key design for even distribution
    - Monitor namespace metrics
    - Reference: Azure az-03 (Event-Driven Services)

19. **Azure Stream Analytics**
    - Use for simple transformations (no code)
    - Optimize streaming units (SU)
    - Enable diagnostic logs
    - Test queries with sample data
    - Reference: Azure best practices

20. **Databricks Structured Streaming**
    - Use Delta Lake for ACID guarantees
    - Optimize shuffle partitions
    - Monitor streaming query metrics
    - Use optimized writes
    - Reference: Azure az-02 (Synapse/Databricks)

##  Cost Optimization Examples

### Auto-Scaling Based on Lag
```python
from stream_processor import StreamProcessor
from auto_scaler import StreamAutoScaler

processor = StreamProcessor(source="event_hub")
scaler = StreamAutoScaler(
    min_consumers=2,
    max_consumers=10,
    target_lag_seconds=30
)

# Monitor and auto-scale
@scaler.auto_scale
def process_stream():
    stream = processor.read_stream("user-events")

    # Check current lag
    lag = processor.get_consumer_lag()

    if lag > 60:  # More than 1 minute lag
        scaler.scale_up()
        print(f"Scaling up: lag={lag}s")
    elif lag < 10:  # Very low lag
        scaler.scale_down()
        print(f"Scaling down: lag={lag}s")

    return stream

# Cost tracking
from finops_tracker import StreamingCostTracker

cost_tracker = StreamingCostTracker()
cost_tracker.track_stream(
    stream_name="user-events",
    consumers=scaler.current_consumers,
    throughput_mb=processor.get_throughput(),
    storage_gb=processor.get_storage_usage()
)

# Generate cost report
report = cost_tracker.generate_report(period="daily")
print(f"Compute cost: ${report.compute_cost:.2f}")
print(f"Storage cost: ${report.storage_cost:.2f}")
print(f"Data transfer cost: ${report.transfer_cost:.2f}")
print(f"Total: ${report.total_cost:.2f}")
```

### Optimize Event Serialization
```python
from stream_processor import StreamProcessor
import avro
import json

# Bad: JSON (verbose, slow)
def serialize_json(event: dict) -> bytes:
    return json.dumps(event).encode('utf-8')

# Good: Avro (compact, fast, schema evolution)
def serialize_avro(event: dict, schema: avro.Schema) -> bytes:
    return avro.serialize(event, schema)

# Compare sizes and costs
json_size = len(serialize_json(sample_event))
avro_size = len(serialize_avro(sample_event, event_schema))

print(f"JSON size: {json_size} bytes")
print(f"Avro size: {avro_size} bytes")
print(f"Size reduction: {(1 - avro_size/json_size)*100:.1f}%")

# Cost impact (assuming 1B events/month)
events_per_month = 1_000_000_000
json_transfer_gb = (json_size * events_per_month) / (1024**3)
avro_transfer_gb = (avro_size * events_per_month) / (1024**3)

transfer_cost_per_gb = 0.05  # Example
json_cost = json_transfer_gb * transfer_cost_per_gb
avro_cost = avro_transfer_gb * transfer_cost_per_gb

print(f"\nMonthly data transfer:")
print(f"JSON: {json_transfer_gb:.2f} GB → ${json_cost:.2f}")
print(f"Avro: {avro_transfer_gb:.2f} GB → ${avro_cost:.2f}")
print(f"Monthly savings: ${json_cost - avro_cost:.2f}")
```

### Retention Policy Optimization
```python
from azure.eventhub import EventHubProducerClient
from datetime import timedelta

# Configure retention based on use case
retention_policies = {
    "hot_events": {
        "retention_days": 7,  # Recent data in Event Hub
        "tier": "premium"
    },
    "warm_events": {
        "retention_days": 30,  # Move to blob storage
        "tier": "cool"
    },
    "cold_events": {
        "retention_days": 365,  # Archive for compliance
        "tier": "archive"
    }
}

# Implement tiering
def tier_streaming_data():
    # Hot: Keep in Event Hub (7 days)
    event_hub.set_retention(days=7)

    # Warm: Capture to cool blob storage (8-30 days)
    event_hub.enable_capture(
        destination="cool_storage",
        interval_seconds=300,  # 5 minutes
        size_limit_bytes=314572800  # 300 MB
    )

    # Cold: Archive old data (30+ days)
    # Move cool storage to archive tier
    from azure.storage.blob import BlobServiceClient

    blob_client = BlobServiceClient(connection_string=conn_str)
    container = blob_client.get_container_client("warm-events")

    for blob in container.list_blobs():
        age_days = (datetime.now() - blob.last_modified).days
        if age_days > 30:
            blob_client.get_blob_client(
                container="warm-events",
                blob=blob.name
            ).set_standard_blob_tier("Archive")

# Cost comparison
hot_cost = 7 * 100 * 0.015  # 7 days, 100GB/day, $0.015/GB
warm_cost = 23 * 100 * 0.01  # 23 days, cool tier
cold_cost = 335 * 100 * 0.002  # 335 days, archive tier

print(f"Hot (Event Hub): ${hot_cost:.2f}")
print(f"Warm (Cool Storage): ${warm_cost:.2f}")
print(f"Cold (Archive): ${cold_cost:.2f}")
print(f"Total: ${hot_cost + warm_cost + cold_cost:.2f}")
print(f"vs. all hot: ${365 * 100 * 0.015:.2f}")
```

##  Security Examples

### Encrypt Streaming Data
```python
from azure.eventhub import EventHubProducerClient
from azure.identity import DefaultAzureCredential
from cryptography.fernet import Fernet

# Use managed identity
credential = DefaultAzureCredential()

# Initialize Event Hub with encryption
producer = EventHubProducerClient(
    fully_qualified_namespace="mynamespace.servicebus.windows.net",
    eventhub_name="secure-events",
    credential=credential
)

# Encrypt sensitive fields
def encrypt_sensitive_data(event: dict, encryption_key: bytes) -> dict:
    cipher = Fernet(encryption_key)

    # Encrypt PII fields
    if "email" in event:
        event["email"] = cipher.encrypt(event["email"].encode()).decode()
    if "phone" in event:
        event["phone"] = cipher.encrypt(event["phone"].encode()).decode()

    return event

# Send encrypted events
from azure.keyvault.secrets import SecretClient

# Get encryption key from Key Vault
kv_client = SecretClient(
    vault_url="https://my-keyvault.vault.azure.net/",
    credential=credential
)
encryption_key = kv_client.get_secret("stream-encryption-key").value

# Produce events
event_batch = producer.create_batch()
for event in events:
    encrypted_event = encrypt_sensitive_data(event, encryption_key)
    event_batch.add(EventData(json.dumps(encrypted_event)))

producer.send_batch(event_batch)

# Audit
from audit_logger import AuditLogger
audit = AuditLogger()
audit.log_stream_access(
    stream="secure-events",
    action="write",
    user=os.getenv("USER"),
    encrypted=True,
    timestamp=datetime.now()
)
```

##  Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Throughput** | Events per second | >10,000 | Azure Monitor |
| | Data throughput (MB/s) | >100 | Stream metrics |
| | Batch processing time | <5s | Custom metrics |
| **Latency** | End-to-end latency (p95) | <1s | Application Insights |
| | Processing latency (p95) | <500ms | Stream processor |
| | Consumer lag | <30s | Event Hub metrics |
| **Reliability** | Processing success rate | >99.9% | Azure Monitor |
| | Exactly-once delivery | 100% | Custom validator |
| | Checkpoint success rate | >99.5% | Stream metrics |
| **Cost** | Cost per million events | <$0.50 | FinOps tracker |
| | Storage cost per GB/day | <$0.02 | Cost Management |
| | Compute utilization | 60-80% | Azure Monitor |
| **Quality** | Schema validation pass rate | >99.9% | Data validator |
| | Late event rate | <1% | Watermark metrics |
| **Security** | Encrypted events | 100% | Security scans |
| | Access violations | 0 | Audit logs |

##  Deployment Example

### Streaming Infrastructure as Code
```hcl
# terraform/streaming.tf

resource "azurerm_eventhub_namespace" "streaming" {
  name                = "streaming-${var.environment}"
  location            = var.location
  resource_group_name = azurerm_resource_group.main.name
  sku                 = "Standard"
  capacity            = 2
  auto_inflate_enabled = true
  maximum_throughput_units = 10

  tags = {
    Environment = var.environment
    CostCenter  = "DataEngineering"
  }
}

resource "azurerm_eventhub" "user_events" {
  name                = "user-events"
  namespace_name      = azurerm_eventhub_namespace.streaming.name
  resource_group_name = azurerm_resource_group.main.name
  partition_count     = 32
  message_retention   = 7

  capture_description {
    enabled             = true
    encoding            = "Avro"
    interval_in_seconds = 300
    size_limit_in_bytes = 314572800

    destination {
      name = "EventHubArchive.AzureBlockBlob"
      archive_name_format = "{Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}"
      blob_container_name = "streaming-archive"
      storage_account_id  = azurerm_storage_account.lakehouse.id
    }
  }
}

# Databricks job for stream processing
resource "databricks_job" "stream_processor" {
  name = "user-events-processor"

  new_cluster {
    num_workers   = 4
    spark_version = "13.3.x-scala2.12"
    node_type_id  = "Standard_DS3_v2"

    autoscale {
      min_workers = 2
      max_workers = 10
    }

    spark_conf = {
      "spark.databricks.delta.optimizeWrite.enabled" = "true"
      "spark.databricks.delta.autoCompact.enabled"   = "true"
    }
  }

  spark_python_task {
    python_file = "dbfs:/streaming/process_user_events.py"
  }

  schedule {
    quartz_cron_expression = "0 0/5 * * * ?"  # Every 5 minutes
    timezone_id            = "UTC"
  }
}
```

##  Integration Workflow

### End-to-End Streaming Pipeline
```
1. Event Production (IoT/Apps/CDC)
   ↓
2. Event Hub Ingestion (de-04)
   ↓
3. Schema Validation (de-03)
   ↓
4. PII Detection & Masking (sa-01)
   ↓
5. Stream Processing (de-04)
   - Windowing
   - Aggregations
   - Enrichment
   ↓
6. Multi-Sink Output
    Delta Lake (de-01) → Historical analysis
    Redis → Real-time serving (ml-04)
    Feature Store → ML features (ml-02)
    Analytics → Dashboards (ds-01)
   ↓
7. Monitoring (do-08)
   - Lag tracking
   - Throughput monitoring
   - Quality metrics
   ↓
8. Cost Optimization (fo-01)
   - Auto-scaling
   - Retention policies
   - Compression
```

##  Quick Wins

1. **Enable Event Hub capture** - Automatic archival to blob storage
2. **Implement auto-scaling** - 30-50% cost reduction
3. **Use Avro serialization** - 40-60% bandwidth savings
4. **Set up lag monitoring** - Prevent data delays
5. **Implement checkpointing** - Fault tolerance and recovery
6. **Add schema validation** - Catch bad events early
7. **Enable encryption** - Data security compliance
8. **Optimize partitioning** - Better parallelism and throughput
9. **Set retention policies** - 60-80% storage cost reduction
10. **Use watermarking** - Handle late-arriving data correctly
