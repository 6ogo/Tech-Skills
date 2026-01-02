# Skill 5: Performance Optimization

##  Overview
Master advanced performance tuning techniques for data pipelines, query optimization, partitioning strategies, caching, and cost-efficient compute to achieve 10x faster processing at lower costs.

##  Connections
- **Data Engineer**: Optimize lakehouse and pipelines (de-01, de-02, de-03, de-04)
- **ML Engineer**: Faster feature engineering and training (ml-01, ml-02, ml-03)
- **MLOps**: Optimize model serving latency (mo-04)
- **AI Engineer**: Speed up RAG retrieval (ai-02)
- **Data Scientist**: Faster data exploration (ds-01, ds-02)
- **FinOps**: Reduce compute costs through efficiency (fo-01, fo-06)
- **DevOps**: Infrastructure optimization (do-04, do-08)
- **System Design**: Scalability and caching patterns (sd-03, sd-04)

##  Tools Included

### 1. `query_optimizer.py`
Automated query optimization and execution plan analysis.

### 2. `partition_optimizer.py`
Smart partitioning strategies and optimization recommendations.

### 3. `cache_manager.py`
Multi-level caching with cache warming and invalidation.

### 4. `performance_profiler.py`
End-to-end pipeline profiling and bottleneck detection.

### 5. `index_advisor.py`
Index recommendation engine for query acceleration.

##  Performance Optimization Framework

```
Identify → Measure → Optimize → Validate → Monitor
   ↓         ↓          ↓          ↓         ↓
Bottleneck Profile   Partition  Benchmark  Track
Detection  Queries   Cache      Results    Trends
           Storage   Indexes    A/B Test   Alert
```

##  Quick Start

```python
from query_optimizer import QueryOptimizer
from partition_optimizer import PartitionOptimizer
from cache_manager import CacheManager

# Analyze slow query
optimizer = QueryOptimizer()

query = """
    SELECT customer_id, SUM(amount) as total
    FROM transactions
    WHERE event_date >= '2024-01-01'
    GROUP BY customer_id
"""

# Get optimization recommendations
analysis = optimizer.analyze(query, table="transactions")

print(f"Current execution time: {analysis.baseline_time}s")
print(f"\nRecommendations:")
for rec in analysis.recommendations:
    print(f"  - {rec.type}: {rec.description}")
    print(f"    Expected improvement: {rec.speedup}x")
    print(f"    Cost: {rec.cost_impact}")

# Apply optimizations
optimized_query = optimizer.apply_recommendations(query, analysis.recommendations)

# Optimize partitioning
part_optimizer = PartitionOptimizer()
part_analysis = part_optimizer.analyze_table("transactions")

if part_analysis.needs_repartitioning:
    print(f"\nCurrent partitioning: {part_analysis.current_strategy}")
    print(f"Recommended: {part_analysis.recommended_strategy}")
    print(f"Expected speedup: {part_analysis.speedup}x")

    # Repartition table
    part_optimizer.repartition_table(
        table="transactions",
        partition_by=["event_date"],
        bucket_by=["customer_id"],
        num_buckets=32
    )

# Enable caching
cache = CacheManager()
cache.enable_table_cache(
    table="transactions",
    cache_level="hot",  # hot/warm/cold
    ttl_hours=24
)

# Warm cache with common queries
cache.warm_cache([
    "SELECT * FROM transactions WHERE event_date = CURRENT_DATE",
    "SELECT customer_id, COUNT(*) FROM transactions GROUP BY customer_id"
])
```

##  Best Practices

### Query Optimization

1. **Predicate Pushdown**
   - Filter early to reduce data scanned
   - Push filters to data source when possible
   - Use partition pruning effectively
   - Leverage data skipping with statistics
   - Reference: Data Engineer best practices

2. **Join Optimization**
   - Use broadcast joins for small tables (<10GB)
   - Implement bucketing for large-large joins
   - Sort-merge join for sorted data
   - Avoid cross joins
   - Reference: System Design sd-03 (Scalability)

3. **Aggregation Optimization**
   - Partial aggregation before shuffle
   - Use approximate aggregations when exact not needed
   - Pre-aggregate in Gold layer
   - Cache frequently aggregated results
   - Reference: Data Engineer de-01 (Lakehouse)

4. **Query Plan Analysis**
   - Examine execution plans regularly
   - Identify shuffle-heavy operations
   - Optimize stage boundaries
   - Monitor skew in data distribution
   - Reference: Data Engineer best practices

### Partitioning Strategies

5. **Time-Based Partitioning**
   - Partition by date/datetime for time-series data
   - Use hierarchical partitioning (year/month/day)
   - Balance partition size (target 1GB per partition)
   - Monitor partition count (<10,000 partitions)
   - Reference: Data Engineer de-01 (Lakehouse)

6. **Hash Partitioning**
   - Use for evenly distributed data
   - Choose partition key with high cardinality
   - Avoid skewed partition keys
   - Consider composite partition keys
   - Reference: Data Engineer best practices

7. **Bucketing**
   - Bucket by join keys
   - Optimize bucket count (32-128 typical)
   - Combine with partitioning for best results
   - Sort within buckets for range queries
   - Reference: Data Engineer best practices

### Caching Strategies (System Design Integration)

8. **Multi-Level Caching**
   - L1: Result cache (query results)
   - L2: Disk cache (Delta cache)
   - L3: Table cache (in-memory tables)
   - Cache hot data, tier cold data
   - Reference: System Design sd-04 (Caching Strategies)

9. **Cache Invalidation**
   - Time-based TTL for changing data
   - Event-based invalidation for updates
   - Partial invalidation for partitioned data
   - Monitor cache hit rates
   - Reference: System Design sd-04 (Caching Strategies)

10. **Cache Warming**
    - Pre-load cache on deployment
    - Schedule cache refresh for predictable queries
    - Predictive caching based on patterns
    - Monitor cache utilization
    - Reference: System Design sd-04 (Caching Strategies)

### Indexing (when applicable)

11. **Covering Indexes**
    - Include all columns in SELECT
    - Reduce table lookups
    - Balance index size vs benefit
    - Monitor index usage
    - Reference: Database best practices

12. **Composite Indexes**
    - Order columns by selectivity
    - Include filter and sort columns
    - Avoid index duplication
    - Regular index maintenance
    - Reference: Database best practices

### Storage Optimization

13. **Compression**
    - Use Snappy for balance (speed/ratio)
    - Zstd for better compression
    - Gzip for archival data
    - Monitor compression ratios
    - Reference: Data Engineer de-01 (Lakehouse)

14. **File Sizing**
    - Target 1GB files for Parquet/Delta
    - Avoid small files (<128MB)
    - Use OPTIMIZE for Delta tables
    - Z-ORDER for common filters
    - Reference: Data Engineer de-01 (Lakehouse)

15. **Columnar Storage**
    - Use Parquet/Delta for analytical workloads
    - Project only needed columns
    - Leverage column statistics
    - Enable column pruning
    - Reference: Data Engineer best practices

### Compute Optimization (FinOps Integration)

16. **Right-Size Clusters**
    - Profile workload characteristics
    - Match node types to workload
    - Use memory-optimized for caching
    - Compute-optimized for CPU-bound
    - Reference: FinOps fo-06 (Compute Optimization)

17. **Auto-Scaling**
    - Enable cluster auto-scaling
    - Set appropriate min/max nodes
    - Monitor scale-up/down patterns
    - Balance cost vs performance
    - Reference: FinOps fo-06 (Compute Optimization)

18. **Spot Instances**
    - Use for batch workloads
    - Implement checkpointing
    - Graceful handling of interruptions
    - 60-90% cost savings
    - Reference: FinOps fo-06 (Compute Optimization)

### Azure-Specific Optimizations

19. **Delta Cache (Databricks)**
    - Enable for frequently accessed data
    - Cache hot partitions
    - Monitor cache hit metrics
    - Right-size cache storage
    - Reference: Azure az-02 (Databricks)

20. **Synapse SQL Optimization**
    - Use result set caching
    - Implement materialized views
    - Optimize distribution keys
    - Monitor DWU utilization
    - Reference: Azure az-02 (Synapse Analytics)

21. **Photon Engine (Databricks)**
    - Enable for SQL and DataFrame workloads
    - 2-5x faster for compatible workloads
    - Monitor Photon utilization
    - Cost-benefit analysis
    - Reference: Azure az-02 (Databricks)

##  Cost-Performance Trade-offs

### Optimize Query Performance and Cost
```python
from query_optimizer import QueryOptimizer
from cost_analyzer import CostPerformanceAnalyzer

optimizer = QueryOptimizer()
cost_analyzer = CostPerformanceAnalyzer()

# Baseline query
baseline_query = """
    SELECT user_id, COUNT(*) as event_count
    FROM events
    WHERE event_date >= '2024-01-01'
    GROUP BY user_id
"""

# Analyze cost and performance
baseline = cost_analyzer.analyze(baseline_query)
print(f"Baseline:")
print(f"  Execution time: {baseline.execution_time}s")
print(f"  Cost: ${baseline.cost:.4f}")
print(f"  Data scanned: {baseline.data_scanned_gb:.2f} GB")

# Optimization 1: Partition pruning
optimized_v1 = """
    SELECT user_id, COUNT(*) as event_count
    FROM events
    WHERE event_date BETWEEN '2024-01-01' AND '2024-01-31'  -- Explicit range
    GROUP BY user_id
"""

result_v1 = cost_analyzer.analyze(optimized_v1)
print(f"\nV1 (Partition pruning):")
print(f"  Execution time: {result_v1.execution_time}s ({baseline.execution_time/result_v1.execution_time:.1f}x faster)")
print(f"  Cost: ${result_v1.cost:.4f} ({(1-result_v1.cost/baseline.cost)*100:.1f}% cheaper)")
print(f"  Data scanned: {result_v1.data_scanned_gb:.2f} GB")

# Optimization 2: Pre-aggregated table
# Create a Gold layer aggregation
spark.sql("""
    CREATE OR REPLACE TABLE gold.daily_user_events
    AS
    SELECT event_date, user_id, COUNT(*) as event_count
    FROM events
    GROUP BY event_date, user_id
""")

optimized_v2 = """
    SELECT user_id, SUM(event_count) as event_count
    FROM gold.daily_user_events
    WHERE event_date >= '2024-01-01'
    GROUP BY user_id
"""

result_v2 = cost_analyzer.analyze(optimized_v2)
print(f"\nV2 (Pre-aggregated):")
print(f"  Execution time: {result_v2.execution_time}s ({baseline.execution_time/result_v2.execution_time:.1f}x faster)")
print(f"  Cost: ${result_v2.cost:.4f} ({(1-result_v2.cost/baseline.cost)*100:.1f}% cheaper)")

# Optimization 3: Caching
from cache_manager import CacheManager
cache = CacheManager()
cache.cache_table("gold.daily_user_events")

result_v3 = cost_analyzer.analyze(optimized_v2)  # Same query, cached
print(f"\nV3 (Cached):")
print(f"  Execution time: {result_v3.execution_time}s ({baseline.execution_time/result_v3.execution_time:.1f}x faster)")
print(f"  Cost: ${result_v3.cost:.4f} ({(1-result_v3.cost/baseline.cost)*100:.1f}% cheaper)")
print(f"  Cache hit: {result_v3.cache_hit}")
```

### Delta Table Optimization
```python
from delta_optimizer import DeltaOptimizer

optimizer = DeltaOptimizer()

# Optimize table (compact small files)
table_name = "silver.transactions"
metrics = optimizer.optimize_table(
    table=table_name,
    z_order_by=["customer_id", "event_date"]  # Common filter columns
)

print(f"Optimization results for {table_name}:")
print(f"  Files before: {metrics.files_before:,}")
print(f"  Files after: {metrics.files_after:,}")
print(f"  Size before: {metrics.size_before_gb:.2f} GB")
print(f"  Size after: {metrics.size_after_gb:.2f} GB")
print(f"  Compression improvement: {metrics.compression_ratio:.2f}x")

# Query performance comparison
from performance_profiler import PerformanceProfiler
profiler = PerformanceProfiler()

query = """
    SELECT customer_id, SUM(amount)
    FROM silver.transactions
    WHERE event_date >= '2024-01-01'
    AND customer_id IN (SELECT customer_id FROM high_value_customers)
    GROUP BY customer_id
"""

before_metrics = profiler.profile_query(query, version="before")
after_metrics = profiler.profile_query(query, version="after")

print(f"\nQuery performance:")
print(f"  Before optimization: {before_metrics.execution_time:.2f}s")
print(f"  After optimization: {after_metrics.execution_time:.2f}s")
print(f"  Speedup: {before_metrics.execution_time/after_metrics.execution_time:.1f}x")
print(f"  Data skipped: {after_metrics.data_skipped_percentage:.1f}%")

# Cost impact
print(f"\nCost impact:")
print(f"  Query cost before: ${before_metrics.cost:.4f}")
print(f"  Query cost after: ${after_metrics.cost:.4f}")
print(f"  Monthly savings (1000 queries): ${(before_metrics.cost - after_metrics.cost) * 1000:.2f}")
```

### Adaptive Query Execution
```python
from pyspark.sql import SparkSession

# Enable Adaptive Query Execution (AQE)
spark = SparkSession.builder \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .config("spark.sql.adaptive.skewJoin.enabled", "true") \
    .config("spark.sql.adaptive.localShuffleReader.enabled", "true") \
    .getOrCreate()

# Query with AQE benefits
query = """
    SELECT t1.customer_id, t1.total_amount, t2.segment
    FROM (
        SELECT customer_id, SUM(amount) as total_amount
        FROM transactions
        GROUP BY customer_id
    ) t1
    JOIN customer_segments t2
    ON t1.customer_id = t2.customer_id
"""

# AQE will automatically:
# 1. Dynamically coalesce shuffle partitions
# 2. Convert sort-merge join to broadcast join if one side is small
# 3. Optimize skewed joins by splitting large partitions

df = spark.sql(query)

# Monitor AQE impact
metrics = df.explain("cost")
print(f"AQE optimizations applied:")
print(f"  - Coalesced partitions: {metrics.coalesced_partitions}")
print(f"  - Broadcast joins: {metrics.broadcast_joins}")
print(f"  - Skew handled: {metrics.skew_optimizations}")
```

##  Performance Benchmarks

### Common Optimization Impact

| Optimization Technique | Typical Speedup | Cost Reduction | Effort |
|------------------------|-----------------|----------------|--------|
| Partition pruning | 5-10x | 80-90% | Low |
| Z-ordering | 2-5x | 50-80% | Low |
| File compaction | 2-3x | 30-50% | Low |
| Broadcast joins (small tables) | 10-100x | 90-99% | Low |
| Caching hot data | 10-50x | 90-95% | Medium |
| Pre-aggregation (Gold layer) | 10-100x | 90-99% | Medium |
| Materialized views | 10-100x | 90-99% | Medium |
| Bucketing | 2-5x | 50-80% | Medium |
| Adaptive Query Execution | 1.5-3x | 30-60% | Low (config) |
| Photon engine | 2-5x | -20-0% | Low (enable) |
| Delta cache | 3-10x | 70-90% | Low (enable) |
| Column pruning | 2-10x | 50-90% | Low |
| Compression (Zstd) | 1-2x | 40-60% | Low |

##  Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Query Performance** | Query latency (p95) | <10s | Query history |
| | Data scanned per query | <10GB | Query metrics |
| | Shuffle data size | <1GB | Spark UI |
| **Storage** | File count per partition | <1000 | Delta logs |
| | Average file size | >128MB | Delta logs |
| | Compression ratio | >3x | Storage metrics |
| **Cache** | Cache hit rate | >80% | Cache metrics |
| | Cache eviction rate | <10% | Cache metrics |
| | Cache memory utilization | 70-90% | Cluster metrics |
| **Cost** | Cost per query | <$0.10 | FinOps tracker |
| | Cost per TB scanned | <$5 | Cost analysis |
| | Compute utilization | 70-85% | Cluster metrics |
| **Cluster** | CPU utilization | 60-80% | Azure Monitor |
| | Memory utilization | 70-85% | Azure Monitor |
| | Spill to disk | <5% | Spark metrics |

##  Performance Optimization Workflow

### End-to-End Optimization Process
```
1. Identify Performance Issues (do-08)
   ↓
2. Profile Queries and Pipelines (de-05)
   ↓
3. Analyze Execution Plans
   ↓
4. Apply Optimizations
    Partitioning (de-01)
    Caching (sd-04)
    Indexing
    Query rewriting
   ↓
5. Benchmark Results
   ↓
6. A/B Testing
   ↓
7. Monitor Performance (do-08)
   ↓
8. Track Cost Impact (fo-01)
   ↓
9. Continuous Optimization
```

##  Quick Wins

1. **Enable Delta cache** - 3-10x faster for hot data
2. **Optimize Delta tables (OPTIMIZE + Z-ORDER)** - 2-5x faster queries
3. **Enable Adaptive Query Execution** - 1.5-3x speedup automatically
4. **Partition pruning** - 5-10x faster, 80-90% cost reduction
5. **Use broadcast joins for small tables** - 10-100x faster
6. **Cache frequently accessed tables** - 10-50x faster
7. **Pre-aggregate in Gold layer** - 10-100x faster analytics
8. **Enable Photon engine** - 2-5x faster (Databricks)
9. **Column pruning** - Select only needed columns, 2-10x faster
10. **Compress with Zstd** - 40-60% storage savings

##  Performance Tuning Checklist

### Before Optimization
- [ ] Identify slow queries (>30s execution time)
- [ ] Profile data access patterns
- [ ] Analyze execution plans
- [ ] Measure baseline performance
- [ ] Document current costs

### Storage Optimization
- [ ] Run OPTIMIZE on Delta tables weekly
- [ ] Z-ORDER by common filter columns
- [ ] VACUUM to remove old files (>7 days)
- [ ] Check file sizes (target 1GB)
- [ ] Monitor partition count (<10,000)
- [ ] Enable compression (Snappy/Zstd)

### Query Optimization
- [ ] Enable Adaptive Query Execution
- [ ] Use partition pruning
- [ ] Implement broadcast joins where applicable
- [ ] Pre-aggregate in Gold layer
- [ ] Cache hot tables
- [ ] Project only needed columns
- [ ] Push down filters early

### Cluster Optimization
- [ ] Right-size cluster nodes
- [ ] Enable auto-scaling
- [ ] Use spot instances for batch
- [ ] Monitor CPU/memory utilization
- [ ] Enable Delta cache
- [ ] Enable Photon (if Databricks)

### Monitoring
- [ ] Track query performance trends
- [ ] Monitor cache hit rates
- [ ] Alert on performance degradation
- [ ] Track cost per query
- [ ] Review execution plans regularly
