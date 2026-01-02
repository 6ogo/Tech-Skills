# Skill 2: RAG Pipeline Builder

##  Overview
Build production-grade Retrieval-Augmented Generation (RAG) systems with advanced chunking, vector search, and evaluation.

##  Connections
- **Data Engineer**: Ingests documents from Gold layer, manages vector embeddings (de-01, de-03)
- **Security Architect**: PII masking before indexing, access control for knowledge base (sa-01, sa-02)
- **ML Engineer**: Embedding model serving and optimization (ml-03, ml-04)
- **MLOps**: Embedding model versioning, RAG metrics monitoring (mo-01, mo-04)
- **FinOps**: Embedding cost optimization, vector DB cost tracking (fo-01, fo-07)
- **DevOps**: Containerization, CI/CD for knowledge base updates (do-01, do-03, do-08)
- **Data Scientist**: RAG evaluation metrics and experimentation (ds-01, ds-08)

##  Tools Included

### 1. `document_chunker.py`
Advanced document chunking with semantic, recursive, and fixed-size strategies.

### 2. `vector_db_connector.py`
Unified interface for multiple vector databases (Pinecone, Weaviate, Chroma, Qdrant).

### 3. `hybrid_search.py`
Hybrid search combining semantic (vector) and keyword (BM25) retrieval.

### 4. `rag_evaluator.py`
RAG evaluation metrics: faithfulness, answer relevance, context recall/precision.

### 5. `rag_pipeline.sql`
SQL queries for knowledge base auditing and usage analytics.

##  Key Metrics
- Retrieval precision@k and recall@k
- Answer faithfulness score
- Context relevance score
- Query latency (p50, p95, p99)

##  Quick Start

```python
from rag_pipeline import RAGPipeline

# Initialize pipeline
rag = RAGPipeline(
    vector_db="chroma",
    embedding_model="text-embedding-3-large",
    chunk_strategy="semantic"
)

# Index documents
rag.index_documents("./knowledge_base")

# Query
response = rag.query(
    "How do we handle customer churn?",
    top_k=5
)

print(response.answer)
print(f"Sources: {response.sources}")
```

##  Best Practices

### Cost Optimization (FinOps Integration)

1. **Optimize Embedding Costs**
   - Cache embeddings for frequently accessed documents
   - Use batch embedding APIs to reduce costs
   - Choose appropriate embedding models (balance cost vs quality)
   - Track embedding costs per document collection
   - Reference: FinOps fo-07 (AI/ML Cost Optimization)

2. **Vector Database Cost Management**
   - Right-size vector DB instances based on query patterns
   - Use compression for vector storage
   - Implement tiered storage (hot/warm/cold)
   - Monitor vector DB costs and query efficiency
   - Reference: FinOps fo-01 (Cost Monitoring), fo-05 (Storage Optimization)

3. **Optimize Retrieval Costs**
   - Cache frequent queries with semantic similarity
   - Implement query result caching
   - Use hybrid search (vector + keyword) strategically
   - Tune top_k parameter to balance cost and quality
   - Reference: FinOps fo-03 (Budget Management)

4. **LLM Generation Cost Optimization**
   - Cache system prompts and retrieved context
   - Use prompt caching for RAG responses (90% savings)
   - Right-size context window (don't include unnecessary documents)
   - Monitor end-to-end RAG costs per query
   - Reference: ai-01 (Prompt Caching), FinOps fo-07

### Security & Privacy (Security Architect Integration)

5. **PII Detection Before Indexing**
   - Scan documents for PII before embedding
   - Mask or redact sensitive information
   - Maintain PII inventory for compliance
   - Implement consent-based indexing
   - Reference: Security Architect sa-01 (PII Detection)

6. **Access Control for Knowledge Base**
   - Implement role-based access control (RBAC)
   - Filter retrieval results based on user permissions
   - Audit document access and queries
   - Encrypt vectors at rest and in transit
   - Reference: Security Architect sa-02 (IAM), sa-06 (Data Governance)

7. **Prevent Data Leakage**
   - Validate retrieved context before LLM generation
   - Implement content safety filters
   - Monitor for prompt injection attacks
   - Log all queries for security auditing
   - Reference: Security Architect sa-08 (LLM Security)

### Data Quality & Governance (Data Engineer Integration)

8. **Document Quality Checks**
   - Validate document schemas before ingestion
   - Implement data quality rules from Gold layer
   - Monitor document freshness and staleness
   - Track document lineage and provenance
   - Reference: Data Engineer de-03 (Data Quality)

9. **Chunking Strategy Optimization**
   - Choose chunking strategy based on document type
   - Test semantic vs fixed-size vs recursive chunking
   - Monitor chunk size distribution
   - Optimize chunk overlap for context preservation
   - Reference: Data Engineer de-02 (ETL Orchestration)

### Model Lifecycle Management (MLOps Integration)

10. **Embedding Model Versioning**
    - Version embedding models in registry
    - Track embedding model changes and impacts
    - Implement A/B testing for embedding models
    - Re-embed documents when models change
    - Reference: MLOps mo-01 (Model Registry), mo-03 (Versioning)

11. **RAG Metrics Monitoring**
    - Track retrieval precision, recall, MRR
    - Monitor answer faithfulness and relevance
    - Set up alerts for quality degradation
    - Implement continuous RAG evaluation
    - Reference: MLOps mo-04 (Monitoring), ML Engineer ml-05

12. **Drift Detection**
    - Monitor embedding distribution drift
    - Detect query pattern changes
    - Alert on retrieval quality degradation
    - Track answer quality over time
    - Reference: MLOps mo-05 (Drift Detection)

### Deployment & Operations (DevOps Integration)

13. **Containerize RAG Pipeline**
    - Package RAG components in containers
    - Use Docker for local development
    - Deploy to AKS for production
    - Implement health checks and readiness probes
    - Reference: DevOps do-03 (Containerization)

14. **CI/CD for Knowledge Base Updates**
    - Automate document ingestion pipelines
    - Implement quality gates for new documents
    - Use blue-green deployments for index updates
    - Rollback capability for bad document batches
    - Reference: DevOps do-01 (CI/CD), do-05 (GitOps)

15. **Observability & Monitoring**
    - Instrument RAG pipeline with OpenTelemetry
    - Track end-to-end latency (retrieval + generation)
    - Monitor vector DB query performance
    - Set up Application Insights dashboards
    - Reference: DevOps do-08 (Monitoring & Observability)

### Azure-Specific Best Practices

16. **Leverage Azure AI Search**
    - Use Azure AI Search for hybrid search
    - Enable semantic ranking for better retrieval
    - Use integrated chunking and vectorization
    - Implement Azure RBAC for search indexes
    - Reference: Azure az-05 (Azure OpenAI), az-04 (AI/ML Services)

17. **Azure OpenAI Integration**
    - Use managed identity for authentication
    - Enable diagnostic logging
    - Implement retry logic with circuit breakers
    - Use provisioned throughput for predictable costs
    - Reference: Azure az-05, ai-01 (Prompt Engineering)

##  Cost Optimization Examples

### Embedding Cost Tracking
```python
from vector_db_connector import VectorDBConnector
from embedding_cost_tracker import EmbeddingCostTracker

cost_tracker = EmbeddingCostTracker()

# Track embedding costs
def embed_with_tracking(texts: List[str], model: str = "text-embedding-3-large"):
    embeddings = get_embeddings(texts, model)

    # Log costs
    cost_tracker.log_embedding_request(
        model=model,
        num_tokens=sum(len(text.split()) for text in texts),
        num_texts=len(texts)
    )

    return embeddings

# Generate monthly cost report
report = cost_tracker.monthly_report()
print(f"Embedding costs: ${report.embedding_cost:.2f}")
print(f"Vector DB costs: ${report.vector_db_cost:.2f}")
print(f"LLM generation costs: ${report.llm_cost:.2f}")
print(f"Total RAG costs: ${report.total_cost:.2f}")

# Set budget alerts
cost_tracker.set_budget_alert(
    monthly_budget=500.00,
    alert_threshold=0.8
)
```

### RAG Response Caching (90% Cost Savings)
```python
from anthropic import Anthropic
from semantic_cache import SemanticCache

client = Anthropic()
cache = SemanticCache(similarity_threshold=0.95)

def rag_query_with_caching(query: str, context_docs: List[str]):
    # Check semantic cache first
    cached_response = cache.get(query)
    if cached_response:
        return cached_response

    # Build context with caching
    context = "\n\n".join(context_docs)

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": "You are a helpful assistant that answers questions based on the provided context.",
                "cache_control": {"type": "ephemeral"}  # Cache system prompt
            },
            {
                "type": "text",
                "text": f"Context:\n{context}",
                "cache_control": {"type": "ephemeral"}  # Cache retrieved docs
            }
        ],
        messages=[{"role": "user", "content": query}]
    )

    # Cache the response
    cache.set(query, response.content[0].text)

    return response.content[0].text
```

### Vector DB Cost Optimization
```python
from vector_db_connector import VectorDBConnector

# Use tiered storage for cost optimization
db = VectorDBConnector(
    provider="pinecone",
    tier_config={
        "hot": {  # Recent documents, high-performance
            "age_days": 30,
            "index_type": "performance"
        },
        "warm": {  # Older documents, balanced
            "age_days": 90,
            "index_type": "balanced"
        },
        "cold": {  # Archive, cost-optimized
            "age_days": 365,
            "index_type": "storage_optimized"
        }
    }
)

# Auto-tier documents based on access patterns
db.auto_tier_documents(
    access_threshold=10,  # Move to cold if <10 accesses in 30 days
    review_period_days=30
)

# Monitor costs
costs = db.get_cost_breakdown()
print(f"Hot tier: ${costs.hot_cost:.2f}")
print(f"Warm tier: ${costs.warm_cost:.2f}")
print(f"Cold tier: ${costs.cold_cost:.2f}")
```

##  Security Best Practices Examples

### PII Detection Before Indexing
```python
from pii_detector import PIIDetector  # from sa-01
from data_anonymizer import DataAnonymizer

detector = PIIDetector()
anonymizer = DataAnonymizer()

def safe_index_document(document: str, metadata: dict):
    # Detect PII
    pii_findings = detector.analyze_text(document)

    if pii_findings:
        print(f" PII detected: {pii_findings}")

        # Option 1: Anonymize
        anonymized_doc = anonymizer.mask_text(document, pii_findings)

        # Option 2: Skip indexing
        if pii_findings.severity == "high":
            print(" Skipping document due to sensitive PII")
            return None

        document = anonymized_doc

    # Index the document
    rag.index_document(document, metadata)

    # Log for compliance
    audit_log.record({
        "action": "document_indexed",
        "pii_detected": bool(pii_findings),
        "pii_types": [f.type for f in pii_findings],
        "timestamp": datetime.now()
    })
```

##  Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Retrieval Quality** | Precision@5 | >0.8 | Custom evaluator |
| | Recall@10 | >0.9 | Custom evaluator |
| | MRR (Mean Reciprocal Rank) | >0.85 | MLflow |
| **Answer Quality** | Faithfulness | >0.9 | RAG evaluator |
| | Answer relevance | >0.85 | RAG evaluator |
| | Context relevance | >0.8 | RAG evaluator |
| **Performance** | End-to-end latency (p95) | <3s | Azure Monitor |
| | Retrieval latency (p95) | <500ms | App Insights |
| | Generation latency (p95) | <2s | App Insights |
| **Costs** | Cost per query | <$0.02 | FinOps dashboard |
| | Embedding cost per doc | <$0.001 | Cost tracker |
| | Cache hit rate | >70% | App Insights |
| **Security** | PII detection rate | 100% | Security logs |
| | Access control violations | 0 | Azure Monitor |

##  Deployment Pipeline

### CI/CD for RAG Knowledge Base
```yaml
# .github/workflows/rag-deployment.yml
name: RAG Knowledge Base Update

on:
  push:
    paths:
      - 'knowledge_base/**'
    branches:
      - main

jobs:
  validate-and-index:
    runs-on: ubuntu-latest
    steps:
      - name: Validate documents
        run: python scripts/validate_documents.py

      - name: Run PII detection
        run: python scripts/detect_pii.py --fail-on-high-severity

      - name: Check data quality
        run: python scripts/check_data_quality.py

      - name: Embed and index documents
        run: |
          python scripts/embed_documents.py --batch-size 100
          python scripts/index_to_vector_db.py --environment staging

      - name: Run RAG evaluation tests
        run: pytest tests/test_rag_quality.py --min-score 0.8

      - name: Deploy to production
        if: success()
        run: python scripts/deploy_index.py --environment production

      - name: Monitor RAG metrics
        run: python scripts/monitor_rag.py --duration 1h
```

##  Integration Workflow

### End-to-End RAG Pipeline with All Roles
```
1. Data Ingestion (de-01)
   ↓
2. Data Quality Checks (de-03)
   ↓
3. PII Detection & Masking (sa-01)
   ↓
4. Document Chunking (ai-02)
   ↓
5. Embedding Generation (ml-03)
   ↓
6. Vector Indexing (ai-02)
   ↓
7. Embed Cost Tracking (fo-07)
   ↓
8. Deploy via CI/CD (do-01)
   ↓
9. Monitor Quality (mo-04)
   ↓
10. RAG Query with Caching (ai-01, ai-02)
    ↓
11. Monitor Costs (fo-01)
    ↓
12. Detect Drift (mo-05)
```

##  Quick Wins

1. **Enable prompt caching** - 90% cost reduction on RAG responses
2. **Implement PII detection** - Prevent compliance violations before indexing
3. **Set up embedding caching** - Reduce re-embedding costs
4. **Add vector DB cost monitoring** - Track and optimize storage costs
5. **Implement query result caching** - Reduce costs for frequent queries
6. **Set up RAG evaluation** - Catch quality degradation early
7. **Containerize for deployment** - Easier scaling and updates
8. **Enable Application Insights** - Full observability of RAG pipeline
