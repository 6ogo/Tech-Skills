# Skill 1: Architecture Pattern Selection & Design

##  Overview
Tools for selecting, documenting, and implementing architectural patterns with trade-off analysis.

##  Connections
- **All Roles**: Provides architectural guidance for implementations
- **Security Architect**: Security pattern integration (sa-02, sa-06, sa-08)
- **Data Engineer**: Data architecture patterns (de-01, de-02)
- **DevOps**: Infrastructure and deployment patterns (do-01, do-03, do-04)
- **ML Engineer**: ML system architecture (ml-01, ml-03)
- **AI Engineer**: AI application architecture (ai-02, ai-03)
- **FinOps**: Cost-optimized architecture design (fo-05, fo-06)

##  Tools Included

### 1. `pattern_selector.py`
Decision framework for choosing architectural patterns.

### 2. `adr_generator.py`
Architecture Decision Record (ADR) automation.

### 3. `diagram_generator.py`
Mermaid diagram generation for C4 model and system architecture.

### 4. `tradeoff_analyzer.py`
CAP theorem and architectural trade-off analysis.

### 5. `architecture_templates.md`
Templates for common patterns (microservices, event-driven, layered, etc.).

##  Supported Patterns
- Microservices
- Event-Driven Architecture (EDA)
- Layered Architecture
- CQRS & Event Sourcing
- Serverless
- Data Mesh

##  Quick Start

```python
from pattern_selector import ArchitectureSelector
from adr_generator import ADRGenerator

# Analyze requirements
selector = ArchitectureSelector()
recommendation = selector.recommend_pattern(
    scalability="high",
    consistency="eventual",
    team_size="large",
    deployment_frequency="daily"
)

# Generate ADR
adr = ADRGenerator()
adr.create_decision_record(
    title="Adopt Microservices Architecture",
    context="Need to scale teams and deployments independently",
    decision="Implement microservices with event-driven communication",
    consequences=["Increased operational complexity", "Better scalability"]
)
```

##  Best Practices

### Cost-Optimized Architecture (FinOps Integration)

1. **Design for Cost Efficiency**
   - Choose serverless vs containers based on usage patterns
   - Implement auto-scaling with appropriate thresholds
   - Use spot instances for fault-tolerant workloads
   - Design for right-sizing from the start
   - Reference: FinOps fo-05, fo-06

2. **Cost-Aware Pattern Selection**
   - Evaluate TCO for each architecture pattern
   - Consider operational costs, not just infrastructure
   - Design for observability to enable optimization
   - Track architectural decisions vs cost impact
   - Reference: FinOps fo-01, System Design sd-05

### Security by Design (Security Architect Integration)

3. **Zero Trust Architecture**
   - Assume breach mentality
   - Implement least privilege access
   - Encrypt all data in transit and at rest
   - Continuous authentication and authorization
   - Reference: Security Architect sa-02 (IAM), sa-04 (Encryption)

4. **Defense in Depth**
   - Multiple layers of security controls
   - Network segmentation and isolation
   - API gateway with rate limiting
   - WAF and DDoS protection
   - Reference: Security Architect sa-03 (Network Security)

### DevOps-Enabled Architecture

5. **Infrastructure as Code**
   - Design for automated provisioning
   - Use immutable infrastructure patterns
   - Implement blue-green deployments
   - Enable infrastructure versioning
   - Reference: DevOps do-04 (IaC), do-05 (GitOps)

6. **Observable by Design**
   - Built-in logging, metrics, and tracing
   - Distributed tracing for microservices
   - Health checks and readiness probes
   - Structured logging standards
   - Reference: DevOps do-08 (Monitoring & Observability)

### Data Architecture Patterns

7. **Scalable Data Architecture**
   - Implement data mesh for large organizations
   - Use CQRS for read-heavy workloads
   - Design for eventual consistency
   - Partition strategies for scale
   - Reference: Data Engineer de-01, de-02

8. **Data Governance Integration**
   - Data catalog and lineage tracking
   - Policy enforcement at architecture level
   - Data quality gates
   - Compliance by design
   - Reference: Security Architect sa-06 (Data Governance)

### ML/AI Architecture Patterns

9. **ML System Architecture**
   - Separate training and serving infrastructure
   - Model registry and versioning
   - Feature store architecture
   - A/B testing infrastructure
   - Reference: ML Engineer ml-01, ml-02

10. **AI Application Architecture**
    - LLM gateway pattern for cost control
    - RAG architecture for knowledge systems
    - Agent orchestration patterns
    - Prompt template management
    - Reference: AI Engineer ai-01, ai-02, ai-03

##  Architecture Decision Records (ADRs)

### Cost-Optimized Microservices
```markdown
# ADR-001: Adopt Serverless-First for Microservices

## Status
Accepted

## Context
Need to build scalable microservices with minimal operational overhead and cost-efficient scaling.

## Decision
Use Azure Functions (serverless) for event-driven services with variable load.
Use Azure Container Apps for always-on services requiring more control.

## Consequences
**Positive:**
- Auto-scaling with pay-per-execution model (70% cost savings on variable workloads)
- Reduced operational complexity
- Built-in monitoring and logging

**Negative:**
- Cold start latency for infrequent functions
- Vendor lock-in to Azure ecosystem
- Limited customization vs Kubernetes

## Cost Impact
- Estimated 60-70% reduction in compute costs for variable workloads
- Operational cost savings: ~40% reduction in DevOps overhead

## References
- FinOps fo-06 (Compute Optimization)
- DevOps do-03 (Containerization)
```

### Security Architecture
```markdown
# ADR-002: Implement Zero Trust Network Architecture

## Status
Accepted

## Context
Legacy network perimeter security insufficient for cloud-native applications.

## Decision
Implement zero trust architecture with:
- Mutual TLS for all service-to-service communication
- Identity-based access control (not network-based)
- Continuous verification and least privilege access
- Azure Managed Identity for all service authentication

## Consequences
**Positive:**
- Stronger security posture
- Better compliance with SOC 2, ISO 27001
- Reduced attack surface

**Negative:**
- Increased complexity in initial setup
- More stringent certificate management
- Potential latency from additional auth checks

## Implementation
- Use Azure API Management as central gateway
- Implement Azure AD for identity management
- Enable Azure Key Vault for secrets management

## References
- Security Architect sa-02 (IAM)
- Security Architect sa-04 (Encryption)
- DevOps do-07 (Secrets Management)
```

##  Architecture Pattern Library

### Pattern: Event-Driven Microservices
```python
"""
Enterprise-grade event-driven architecture with Azure Event Grid
"""
from azure.eventgrid import EventGridPublisherClient
from azure.identity import DefaultAzureCredential

class EventDrivenArchitecture:
    def __init__(self, topic_endpoint: str):
        self.client = EventGridPublisherClient(
            topic_endpoint,
            DefaultAzureCredential()
        )

    def publish_event(self, event_type: str, data: dict):
        event = {
            "eventType": event_type,
            "subject": f"/{event_type}",
            "dataVersion": "1.0",
            "data": data
        }
        self.client.send(event)

# Usage with cost tracking
from finops_tracker import EventCostTracker

cost_tracker = EventCostTracker()

@cost_tracker.track_event_cost
def process_order(order_id: str):
    architecture = EventDrivenArchitecture(topic_endpoint)
    architecture.publish_event(
        "order.created",
        {"order_id": order_id, "status": "pending"}
    )
```

### Pattern: CQRS with Event Sourcing
```python
"""
Command Query Responsibility Segregation for scalable reads
"""
class CQRSArchitecture:
    def __init__(self):
        self.write_db = CosmosDBClient()  # Strong consistency
        self.read_db = AzureSearchClient()  # Optimized for queries
        self.event_store = EventGridClient()

    def execute_command(self, command: Command):
        # Write to command store
        result = self.write_db.execute(command)

        # Publish event for read model update
        self.event_store.publish({
            "type": "command.executed",
            "aggregate_id": command.aggregate_id,
            "data": result
        })

        return result

    def execute_query(self, query: Query):
        # Read from optimized read model
        return self.read_db.search(query)
```

##  Architecture Metrics

| Metric | Target | Tool |
|--------|--------|------|
| **System Availability** | >99.9% | Azure Monitor |
| **Mean Time to Recovery (MTTR)** | <30 min | Incident tracking |
| **Deployment Frequency** | Daily | CI/CD metrics |
| **Lead Time for Changes** | <1 day | DevOps metrics |
| **Change Failure Rate** | <5% | Deployment tracking |
| **Architecture Cost Efficiency** | >60% savings vs baseline | FinOps dashboard |
| **Security Posture Score** | >90/100 | Security assessment |

##  Integration Patterns

### Cross-Role Architecture Workflow
```
1. Requirements Gathering (sd-02)
   ↓
2. Architecture Pattern Selection (sd-01)
   ↓
3. Security Architecture Review (sa-02, sa-06)
   ↓
4. Cost Impact Analysis (fo-05, fo-06)
   ↓
5. Infrastructure Design (do-04)
   ↓
6. Data Architecture (de-01, de-02)
   ↓
7. ML System Architecture (ml-01)
   ↓
8. API Design (sd-04)
   ↓
9. ADR Documentation (sd-01)
   ↓
10. Implementation & Deployment (do-01, do-03)
    ↓
11. Monitoring & Optimization (do-08, fo-01)
```

##  Quick Wins

1. **Document architecture decisions** - Enable informed evolution
2. **Implement ADRs** - Track rationale and consequences
3. **Design for observability** - Enable optimization
4. **Security by design** - Prevent costly retrofits
5. **Cost-aware architecture** - Optimize from day one
6. **Infrastructure as Code** - Enable automation and consistency
