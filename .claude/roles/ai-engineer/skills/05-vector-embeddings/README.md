# Skill 5: Vector Embeddings & Search

## 🎯 Overview
Master vector embeddings, semantic search, and similarity matching for building intelligent search systems, recommendations, and clustering applications at scale.

## 🔗 Connections
- **Data Engineer**: Embedding data pipelines, vector storage optimization (de-01, de-03)
- **Security Architect**: Secure embedding APIs, access control for vector indices (sa-02, sa-06)
- **ML Engineer**: Embedding model fine-tuning and deployment (ml-03, ml-04)
- **MLOps**: Embedding model versioning, drift detection (mo-01, mo-05)
- **FinOps**: Embedding cost optimization, vector DB cost management (fo-01, fo-07)
- **DevOps**: Vector DB deployment, index update automation (do-01, do-03)
- **Data Scientist**: Dimensionality reduction, clustering analysis (ds-01, ds-08)

## 🛠️ Tools Included

### 1. `embedding_generator.py`
Multi-provider embedding generation (OpenAI, Cohere, Azure OpenAI, sentence-transformers).

### 2. `vector_index_manager.py`
Unified interface for vector databases (Pinecone, Weaviate, Qdrant, Chroma, FAISS).

### 3. `semantic_search.py`
Advanced semantic search with hybrid retrieval, re-ranking, and filtering.

### 4. `embedding_evaluator.py`
Evaluate embedding quality with retrieval metrics, clustering scores, and similarity distributions.

### 5. `vector_compression.py`
Dimension reduction and quantization for cost-efficient vector storage.

## 📊 Key Metrics
- Retrieval precision@k and recall@k
- Mean Reciprocal Rank (MRR)
- Embedding generation latency
- Vector DB query latency (p50, p95)
- Storage cost per million vectors

## 🚀 Quick Start

```python
from embedding_generator import EmbeddingGenerator
from vector_index_manager import VectorIndexManager

# Initialize embedding generator
embedder = EmbeddingGenerator(
    provider="azure_openai",
    model="text-embedding-3-large",
    dimensions=1536
)

# Initialize vector index
vector_db = VectorIndexManager(
    provider="pinecone",
    index_name="product-search",
    dimension=1536,
    metric="cosine"
)

# Index documents
documents = [
    {"id": "1", "text": "High-performance laptop with 32GB RAM"},
    {"id": "2", "text": "Lightweight tablet with long battery life"},
    {"id": "3", "text": "Professional gaming desktop with RTX 4090"}
]

for doc in documents:
    embedding = embedder.embed(doc["text"])
    vector_db.upsert(
        id=doc["id"],
        vector=embedding,
        metadata={"text": doc["text"]}
    )

# Semantic search
query = "portable computer for work"
query_embedding = embedder.embed(query)

results = vector_db.search(
    query_vector=query_embedding,
    top_k=3,
    filter={"category": "electronics"}
)

for result in results:
    print(f"Score: {result.score:.3f} - {result.metadata['text']}")
```

## 📚 Best Practices

### Cost Optimization (FinOps Integration)

1. **Optimize Embedding Generation Costs**
   - Batch embed documents (up to 2048 per request)
   - Cache embeddings for reused content
   - Choose cost-effective models (ada vs large)
   - Monitor embedding costs per collection
   - Reference: FinOps fo-07 (AI/ML Cost Optimization)

2. **Vector Database Cost Management**
   - Use quantization to reduce storage by 75%
   - Implement tiered storage (hot/warm/cold)
   - Right-size index replicas
   - Monitor query costs and optimize indices
   - Reference: FinOps fo-05 (Storage Optimization)

3. **Dimension Reduction Strategies**
   - Reduce dimensions with PCA/UMAP
   - Use matryoshka embeddings for flexible dimensions
   - Test quality vs cost tradeoffs
   - Monitor retrieval quality after reduction
   - Reference: FinOps fo-01 (Cost Monitoring)

4. **Smart Caching Strategy**
   - Cache frequent query embeddings
   - Implement approximate caching with similarity threshold
   - Cache re-ranking results
   - Monitor cache hit rates
   - Reference: ai-01 (Prompt Caching)

### Security & Privacy (Security Architect Integration)

5. **Secure Embedding APIs**
   - Use managed identity for Azure OpenAI
   - Rotate API keys regularly
   - Implement rate limiting
   - Monitor for API abuse
   - Reference: Security Architect sa-02 (IAM)

6. **Access Control for Vector Indices**
   - Implement RBAC for vector databases
   - Filter search results by user permissions
   - Encrypt vectors at rest and in transit
   - Audit vector access patterns
   - Reference: Security Architect sa-06 (Data Governance)

7. **Prevent Embedding Inversion Attacks**
   - Don't expose raw embeddings to users
   - Monitor for adversarial queries
   - Implement query result limits
   - Add noise to embeddings if needed
   - Reference: Security Architect sa-08 (LLM Security)

### Data Quality & Governance (Data Engineer Integration)

8. **Document Preprocessing Quality**
   - Clean and normalize text before embedding
   - Handle multiple languages consistently
   - Remove low-quality or duplicate documents
   - Track document freshness
   - Reference: Data Engineer de-03 (Data Quality)

9. **Embedding Data Pipeline**
   - Automate document ingestion and embedding
   - Implement incremental embedding updates
   - Version embedding datasets
   - Monitor pipeline health
   - Reference: Data Engineer de-01 (Data Ingestion), de-02 (ETL)

### Model Lifecycle Management (MLOps Integration)

10. **Embedding Model Versioning**
    - Track embedding model versions in registry
    - Version vector indices by embedding model
    - A/B test embedding model changes
    - Maintain backward compatibility
    - Reference: MLOps mo-01 (Model Registry), mo-03 (Versioning)

11. **Retrieval Quality Monitoring**
    - Track precision, recall, MRR over time
    - Monitor query latency and success rates
    - Set up alerts for degradation
    - Continuous evaluation with test queries
    - Reference: MLOps mo-04 (Monitoring)

12. **Embedding Drift Detection**
    - Monitor embedding distribution shifts
    - Detect query pattern changes
    - Alert on retrieval quality degradation
    - Trigger retraining when needed
    - Reference: MLOps mo-05 (Drift Detection)

### Deployment & Operations (DevOps Integration)

13. **Containerize Vector Services**
    - Package embedding services in containers
    - Use Docker for local development
    - Deploy to AKS for production
    - Implement auto-scaling based on load
    - Reference: DevOps do-03 (Containerization)

14. **CI/CD for Vector Indices**
    - Automate index creation and updates
    - Implement blue-green deployments
    - Test index quality before promotion
    - Rollback capability for bad updates
    - Reference: DevOps do-01 (CI/CD)

15. **Observability for Vector Search**
    - Instrument with OpenTelemetry
    - Track end-to-end search latency
    - Monitor vector DB performance
    - Set up Application Insights dashboards
    - Reference: DevOps do-08 (Monitoring & Observability)

### Azure-Specific Best Practices

16. **Azure AI Search Integration**
    - Use built-in vectorization in Azure AI Search
    - Leverage semantic ranking
    - Implement hybrid search (vector + keyword)
    - Use managed identity for security
    - Reference: Azure az-05 (Azure OpenAI), az-04 (AI/ML Services)

17. **Azure OpenAI Embeddings**
    - Use Azure OpenAI for embeddings
    - Enable diagnostic logging
    - Implement retry logic with exponential backoff
    - Use provisioned throughput for predictable costs
    - Reference: Azure az-05 (Azure OpenAI)

## 💰 Cost Optimization Examples

### Batch Embedding with Cost Tracking
```python
from embedding_generator import EmbeddingGenerator
from cost_tracker import EmbeddingCostTracker

embedder = EmbeddingGenerator(
    provider="azure_openai",
    model="text-embedding-3-large"
)

cost_tracker = EmbeddingCostTracker()

def embed_documents_efficiently(documents: List[str], batch_size: int = 100):
    """Batch embed documents with cost tracking."""
    all_embeddings = []

    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]

        # Batch embedding (more cost-effective)
        embeddings = embedder.embed_batch(batch)
        all_embeddings.extend(embeddings)

        # Track costs
        num_tokens = sum(len(doc.split()) * 1.3 for doc in batch)  # Estimate
        cost_tracker.log_embedding_request(
            model="text-embedding-3-large",
            num_tokens=num_tokens,
            num_texts=len(batch)
        )

    # Report costs
    report = cost_tracker.get_report()
    print(f"📊 Embedding Cost Report:")
    print(f"  Documents embedded: {len(documents)}")
    print(f"  Total cost: ${report.total_cost:.4f}")
    print(f"  Cost per document: ${report.cost_per_doc:.6f}")

    return all_embeddings

# Compare costs
# Single requests: 1000 docs × $0.00013 = $0.130
# Batch requests: 10 batches × $0.00011 = $0.011 (85% savings)
```

### Vector Compression for Storage Savings
```python
from vector_compression import VectorCompressor
import numpy as np

class CompressedVectorIndex:
    def __init__(self, index_manager, compression_type="quantization"):
        self.index = index_manager
        self.compressor = VectorCompressor(
            method=compression_type,
            bits=8  # 8-bit quantization (75% storage reduction)
        )

    def upsert(self, id: str, vector: np.ndarray, metadata: dict):
        """Upsert compressed vector."""
        # Compress vector (1536 dims × 4 bytes → 1536 dims × 1 byte)
        compressed = self.compressor.compress(vector)

        # Store compressed vector
        self.index.upsert(
            id=id,
            vector=compressed,
            metadata=metadata
        )

    def search(self, query_vector: np.ndarray, top_k: int = 10):
        """Search with query vector."""
        # Compress query
        compressed_query = self.compressor.compress(query_vector)

        # Search
        results = self.index.search(
            query_vector=compressed_query,
            top_k=top_k
        )

        return results

# Storage cost comparison:
# Uncompressed: 1M vectors × 1536 dims × 4 bytes = 6.144 GB → $15/month
# Quantized (8-bit): 1M vectors × 1536 dims × 1 byte = 1.536 GB → $4/month
# Savings: 75% reduction
```

### Tiered Vector Storage
```python
from vector_index_manager import VectorIndexManager

class TieredVectorStorage:
    def __init__(self):
        # Hot tier: Recent, frequently accessed (high performance)
        self.hot_index = VectorIndexManager(
            provider="pinecone",
            index_type="performance",
            replicas=3
        )

        # Warm tier: Older, occasionally accessed (balanced)
        self.warm_index = VectorIndexManager(
            provider="pinecone",
            index_type="balanced",
            replicas=2
        )

        # Cold tier: Archive, rarely accessed (cost-optimized)
        self.cold_index = VectorIndexManager(
            provider="qdrant",  # Cheaper option
            index_type="storage_optimized",
            quantization=True
        )

    def auto_tier_vectors(self, age_days: int, access_count: int):
        """Automatically move vectors to appropriate tier."""
        if age_days <= 30 or access_count > 100:
            return self.hot_index  # $0.096/hour

        elif age_days <= 90 or access_count > 10:
            return self.warm_index  # $0.048/hour

        else:
            return self.cold_index  # $0.012/hour

    def search_all_tiers(self, query_vector: np.ndarray, top_k: int = 10):
        """Search across all tiers with priority."""
        # Search hot tier first
        hot_results = self.hot_index.search(query_vector, top_k)

        if len(hot_results) >= top_k:
            return hot_results

        # Search warm tier if needed
        warm_results = self.warm_index.search(query_vector, top_k)

        # Combine and re-rank
        all_results = self._merge_results(hot_results, warm_results)

        return all_results[:top_k]

# Cost comparison:
# All hot: 1M vectors → $70/month
# Tiered (70% warm, 20% cold): $30/month (57% savings)
```

### Embedding Cache Implementation
```python
from functools import lru_cache
import hashlib
from semantic_cache import SemanticCache

class CachedEmbeddingGenerator:
    def __init__(self, provider: str, model: str):
        self.embedder = EmbeddingGenerator(provider, model)
        self.exact_cache = {}  # Exact match cache
        self.semantic_cache = SemanticCache(
            similarity_threshold=0.99,
            max_size=10000
        )

    def embed(self, text: str) -> np.ndarray:
        """Generate embedding with caching."""
        # Check exact cache
        text_hash = hashlib.md5(text.encode()).hexdigest()
        if text_hash in self.exact_cache:
            print("✅ Exact cache hit")
            return self.exact_cache[text_hash]

        # Check semantic cache for similar text
        cached_embedding = self.semantic_cache.get(text)
        if cached_embedding is not None:
            print("✅ Semantic cache hit")
            return cached_embedding

        # Generate new embedding
        embedding = self.embedder.embed(text)

        # Cache the result
        self.exact_cache[text_hash] = embedding
        self.semantic_cache.set(text, embedding)

        return embedding

    def get_cache_stats(self):
        """Get cache performance statistics."""
        return {
            "exact_cache_size": len(self.exact_cache),
            "semantic_cache_size": self.semantic_cache.size(),
            "cache_hit_rate": self.semantic_cache.hit_rate(),
            "cost_saved": self.semantic_cache.cost_saved()
        }

# Usage
embedder = CachedEmbeddingGenerator("azure_openai", "text-embedding-3-large")

# First call: Cache miss, generates embedding
emb1 = embedder.embed("machine learning tutorial")

# Second call: Exact cache hit, no cost
emb2 = embedder.embed("machine learning tutorial")

# Similar call: Semantic cache hit, no cost
emb3 = embedder.embed("tutorial on machine learning")

# Report
stats = embedder.get_cache_stats()
print(f"Cache hit rate: {stats['cache_hit_rate']:.2%}")
print(f"Cost saved: ${stats['cost_saved']:.4f}")
```

## 🔒 Security Best Practices Examples

### Secure Embedding API Access
```python
from azure.identity import DefaultAzureCredential
from embedding_generator import EmbeddingGenerator

class SecureEmbeddingGenerator:
    def __init__(self):
        # Use managed identity (no API keys in code)
        self.credential = DefaultAzureCredential()

        self.embedder = EmbeddingGenerator(
            provider="azure_openai",
            credential=self.credential,
            endpoint="https://my-openai.openai.azure.com/",
            api_version="2024-02-01"
        )

        # Rate limiting
        self.rate_limiter = RateLimiter(
            requests_per_minute=60,
            requests_per_day=10000
        )

    def embed_with_security(self, text: str, user_id: str):
        """Generate embedding with security controls."""
        # Rate limiting per user
        if not self.rate_limiter.check(user_id):
            raise RateLimitError(f"Rate limit exceeded for user {user_id}")

        # Input validation
        if len(text) > 8191:  # Max tokens for text-embedding-3-large
            raise ValueError("Text exceeds maximum length")

        # Generate embedding
        embedding = self.embedder.embed(text)

        # Audit logging
        self.audit_log.record({
            "timestamp": datetime.now(),
            "user_id": user_id,
            "text_length": len(text),
            "model": "text-embedding-3-large",
            "success": True
        })

        return embedding

# Usage with managed identity
embedder = SecureEmbeddingGenerator()
embedding = embedder.embed_with_security(
    text="sensitive document content",
    user_id="user_123"
)
```

### Access-Controlled Vector Search
```python
from vector_index_manager import VectorIndexManager

class SecureVectorSearch:
    def __init__(self, index_manager):
        self.index = index_manager

    def search_with_rbac(
        self,
        query_vector: np.ndarray,
        user_permissions: List[str],
        top_k: int = 10
    ):
        """Search with role-based access control."""
        # Retrieve more results than needed for filtering
        raw_results = self.index.search(
            query_vector=query_vector,
            top_k=top_k * 3  # Over-fetch for filtering
        )

        # Filter based on user permissions
        filtered_results = []
        for result in raw_results:
            # Check if user has access to this document
            required_permission = result.metadata.get("required_permission")

            if required_permission in user_permissions or "admin" in user_permissions:
                filtered_results.append(result)

            if len(filtered_results) >= top_k:
                break

        # Audit log
        self.audit_log.record({
            "timestamp": datetime.now(),
            "user_permissions": user_permissions,
            "results_returned": len(filtered_results),
            "results_filtered": len(raw_results) - len(filtered_results)
        })

        return filtered_results[:top_k]

# Usage
search = SecureVectorSearch(vector_db)

results = search.search_with_rbac(
    query_vector=query_embedding,
    user_permissions=["read:public", "read:internal"],
    top_k=10
)
```

## 📊 Enhanced Metrics & Monitoring

| Metric Category | Metric | Target | Tool |
|-----------------|--------|--------|------|
| **Retrieval Quality** | Precision@10 | >0.85 | Custom evaluator |
| | Recall@10 | >0.90 | Custom evaluator |
| | Mean Reciprocal Rank (MRR) | >0.80 | MLflow |
| | NDCG@10 | >0.85 | Custom evaluator |
| **Performance** | Embedding generation (p95) | <100ms | Azure Monitor |
| | Vector search latency (p95) | <50ms | App Insights |
| | Index update latency | <200ms | Custom monitor |
| **Costs** | Embedding cost per 1K docs | <$0.13 | Cost tracker |
| | Storage cost per 1M vectors | <$5/month | FinOps dashboard |
| | Query cost per 1K searches | <$0.50 | Cost analyzer |
| | Cache hit rate | >70% | Redis metrics |
| **Quality** | Embedding distribution stability | >0.95 | MLflow |
| | Duplicate detection rate | >0.98 | Custom monitor |
| | Null embedding rate | 0% | Data quality |
| **Security** | API rate limit violations | 0 | Azure Monitor |
| | Unauthorized access attempts | 0 | Security logs |

## 🚀 Deployment Pipeline

### CI/CD for Vector Search System
```yaml
# .github/workflows/vector-search-deployment.yml
name: Vector Search Deployment

on:
  push:
    paths:
      - 'embeddings/**'
      - 'vector_db/**'
    branches:
      - main

jobs:
  test-embeddings:
    runs-on: ubuntu-latest
    steps:
      - name: Unit test embedding generation
        run: pytest tests/test_embeddings.py -v

      - name: Test vector operations
        run: pytest tests/test_vector_ops.py -v

      - name: Benchmark embedding quality
        run: python scripts/benchmark_embeddings.py

      - name: Test retrieval quality
        run: pytest tests/test_retrieval_quality.py --min-precision 0.85

  validate-vector-db:
    runs-on: ubuntu-latest
    steps:
      - name: Test vector DB connections
        run: pytest tests/test_vector_db.py

      - name: Validate index schema
        run: python scripts/validate_index_schema.py

      - name: Test search performance
        run: python scripts/benchmark_search.py --max-latency-ms 50

  deploy-to-staging:
    needs: [test-embeddings, validate-vector-db]
    runs-on: ubuntu-latest
    steps:
      - name: Build embedding service
        run: docker build -t embedding-service:${{ github.sha }} .

      - name: Push to registry
        run: |
          az acr login --name myregistry
          docker push myregistry.azurecr.io/embedding-service:${{ github.sha }}

      - name: Deploy to AKS staging
        run: |
          kubectl set image deployment/embedding-service \
            embedding-service=myregistry.azurecr.io/embedding-service:${{ github.sha }} \
            --namespace staging

      - name: Create staging vector index
        run: python scripts/create_index.py --environment staging

      - name: Run integration tests
        run: pytest tests/integration/ --environment staging

  deploy-to-production:
    needs: deploy-to-staging
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Blue-green index swap
        run: python scripts/blue_green_index_swap.py

      - name: Deploy embedding service
        run: |
          kubectl set image deployment/embedding-service \
            embedding-service=myregistry.azurecr.io/embedding-service:${{ github.sha }} \
            --namespace production

      - name: Monitor search quality
        run: python scripts/monitor_search_quality.py --duration 1h

      - name: Rollback if quality degrades
        if: failure()
        run: python scripts/rollback_index.py
```

## 🔄 Integration Workflow

### End-to-End Vector Search Pipeline with All Roles
```
1. Document Ingestion (de-01)
   ↓
2. Data Quality Checks (de-03)
   ↓
3. Text Preprocessing & Cleaning
   ↓
4. Check Embedding Cache (ai-05)
   ↓
5. Batch Embedding Generation (ai-05)
   ↓
6. Embedding Cost Tracking (fo-07)
   ↓
7. Vector Compression (optional) (fo-05)
   ↓
8. Vector Index Upsert (ai-05)
   ↓
9. Access Control Metadata (sa-02)
   ↓
10. Index Health Check (mo-04)
    ↓
11. Query Received
    ↓
12. User Permission Validation (sa-02)
    ↓
13. Query Embedding Generation (ai-05)
    ↓
14. Semantic Search Execution (ai-05)
    ↓
15. RBAC Result Filtering (sa-06)
    ↓
16. Re-ranking (optional) (ai-02)
    ↓
17. Results Caching (ai-01)
    ↓
18. Search Quality Metrics (mo-04)
    ↓
19. Cost Attribution (fo-01)
    ↓
20. Embedding Drift Detection (mo-05)
```

## 🎯 Quick Wins

1. **Batch embed documents** - 85% cost reduction vs individual embedding calls
2. **Implement embedding caching** - 70%+ cost savings on repeated content
3. **Use 8-bit quantization** - 75% storage cost reduction with minimal quality loss
4. **Set up tiered storage** - 50%+ savings by moving old vectors to cold tier
5. **Enable hybrid search** - Combine vector + keyword for better accuracy
6. **Add retrieval monitoring** - Track precision/recall to catch quality issues
7. **Implement RBAC filtering** - Secure vector search with permission controls
8. **Use managed identity** - Eliminate API key management for Azure OpenAI
