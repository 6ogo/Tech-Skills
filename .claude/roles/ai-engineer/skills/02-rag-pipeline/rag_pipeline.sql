-- RAG Pipeline Analytics Queries
-- Track knowledge base usage, query patterns, and performance

-- ================================================================
-- 1. KNOWLEDGE BASE INVENTORY
-- ================================================================

-- Count documents by source
SELECT
    source_type,
    COUNT(*) as document_count,
    SUM(chunk_count) as total_chunks,
    AVG(chunk_count) as avg_chunks_per_doc,
    MAX(last_updated) as latest_update
FROM knowledge_base_documents
GROUP BY source_type
ORDER BY document_count DESC;

-- ================================================================
-- 2. QUERY ANALYTICS
-- ================================================================

-- Top queries by frequency (last 30 days)
SELECT
    query_text,
    COUNT(*) as query_count,
    AVG(latency_ms) as avg_latency_ms,
    AVG(relevance_score) as avg_relevance,
    COUNT(DISTINCT user_id) as unique_users
FROM rag_query_log
WHERE query_timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY query_text
HAVING COUNT(*) > 5
ORDER BY query_count DESC
LIMIT 20;

-- ================================================================
-- 3. RETRIEVAL PERFORMANCE
-- ================================================================

-- Retrieval performance by top_k setting
SELECT
    top_k,
    COUNT(*) as query_count,
    AVG(latency_ms) as avg_latency_ms,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY latency_ms) as p50_latency,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY latency_ms) as p95_latency,
    PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY latency_ms) as p99_latency,
    AVG(relevance_score) as avg_relevance_score
FROM rag_query_log
WHERE query_timestamp >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY top_k
ORDER BY top_k;

-- ================================================================
-- 4. SOURCE ATTRIBUTION
-- ================================================================

-- Which documents are most frequently retrieved?
SELECT
    d.document_id,
    d.title,
    d.source_type,
    COUNT(*) as retrieval_count,
    AVG(r.relevance_score) as avg_relevance,
    MAX(r.query_timestamp) as last_retrieved
FROM rag_retrievals r
JOIN knowledge_base_documents d ON r.document_id = d.document_id
WHERE r.query_timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY d.document_id, d.title, d.source_type
ORDER BY retrieval_count DESC
LIMIT 50;

-- ================================================================
-- 5. USER ENGAGEMENT
-- ================================================================

-- User engagement with RAG system
SELECT
    DATE_TRUNC('day', query_timestamp) as query_date,
    COUNT(DISTINCT user_id) as unique_users,
    COUNT(*) as total_queries,
    COUNT(*) / COUNT(DISTINCT user_id) as queries_per_user,
    AVG(relevance_score) as avg_relevance
FROM rag_query_log
WHERE query_timestamp >= CURRENT_DATE - INTERVAL '90 days'
GROUP BY DATE_TRUNC('day', query_timestamp)
ORDER BY query_date DESC;

-- ================================================================
-- 6. CHUNK PERFORMANCE
-- ================================================================

-- Which chunk size performs best?
SELECT
    c.chunk_size_range,
    COUNT(DISTINCT r.query_id) as query_count,
    AVG(r.relevance_score) as avg_relevance,
    AVG(r.rank_position) as avg_rank
FROM rag_retrievals r
JOIN knowledge_base_chunks c ON r.chunk_id = c.chunk_id
WHERE r.query_timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY c.chunk_size_range
ORDER BY avg_relevance DESC;

-- ================================================================
-- 7. FAILED QUERIES
-- ================================================================

-- Queries with low relevance (need improvement)
SELECT
    query_text,
    COUNT(*) as failure_count,
    AVG(relevance_score) as avg_relevance,
    MIN(relevance_score) as min_relevance,
    MAX(query_timestamp) as last_failed
FROM rag_query_log
WHERE relevance_score < 0.5
  AND query_timestamp >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY query_text
HAVING COUNT(*) > 2
ORDER BY failure_count DESC
LIMIT 30;

-- ================================================================
-- 8. EMBEDDING MODEL PERFORMANCE
-- ================================================================

-- Compare performance across embedding models
SELECT
    embedding_model,
    COUNT(*) as query_count,
    AVG(embedding_latency_ms) as avg_embedding_latency,
    AVG(retrieval_latency_ms) as avg_retrieval_latency,
    AVG(relevance_score) as avg_relevance
FROM rag_query_log
WHERE query_timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY embedding_model
ORDER BY avg_relevance DESC;

-- ================================================================
-- 9. KNOWLEDGE GAPS
-- ================================================================

-- Identify topics with no good answers
WITH poor_coverage AS (
    SELECT
        query_text,
        COUNT(*) as frequency,
        AVG(relevance_score) as avg_relevance
    FROM rag_query_log
    WHERE query_timestamp >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY query_text
    HAVING AVG(relevance_score) < 0.6 AND COUNT(*) > 3
)
SELECT
    query_text,
    frequency,
    avg_relevance,
    'Add documentation' as recommendation
FROM poor_coverage
ORDER BY frequency DESC;

-- ================================================================
-- 10. RAG PIPELINE HEALTH
-- ================================================================

-- Daily RAG pipeline health metrics
SELECT
    DATE(query_timestamp) as date,
    COUNT(*) as total_queries,
    AVG(total_latency_ms) as avg_latency_ms,
    AVG(relevance_score) as avg_relevance,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY total_latency_ms) as p95_latency,
    COUNT(CASE WHEN total_latency_ms > 1000 THEN 1 END) as slow_queries,
    COUNT(CASE WHEN relevance_score < 0.5 THEN 1 END) as low_relevance_queries
FROM rag_query_log
WHERE query_timestamp >= CURRENT_DATE - INTERVAL '14 days'
GROUP BY DATE(query_timestamp)
ORDER BY date DESC;

-- ================================================================
-- 11. VECTOR DATABASE STATISTICS
-- ================================================================

-- Vector database usage statistics
SELECT
    collection_name,
    COUNT(DISTINCT vector_id) as total_vectors,
    AVG(vector_dimension) as avg_dimension,
    MAX(last_updated) as last_updated,
    SUM(storage_bytes) / (1024*1024) as storage_mb
FROM vector_database_collections
GROUP BY collection_name
ORDER BY total_vectors DESC;

-- ================================================================
-- 12. COST TRACKING
-- ================================================================

-- Estimated costs by provider
SELECT
    DATE(query_timestamp) as date,
    llm_provider,
    COUNT(*) as query_count,
    SUM(input_tokens) as total_input_tokens,
    SUM(output_tokens) as total_output_tokens,
    SUM(estimated_cost) as total_cost,
    AVG(estimated_cost) as avg_cost_per_query
FROM rag_query_log
WHERE query_timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY DATE(query_timestamp), llm_provider
ORDER BY date DESC, total_cost DESC;
