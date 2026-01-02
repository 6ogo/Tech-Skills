# Complete Skill Reference

Quick reference mapping agents to their skills for proper execution.

## AI/ML Domain

### AI Engineer Agent

| Skill     | Name                | When to Use                                     |
| --------- | ------------------- | ----------------------------------------------- |
| ai-01     | Prompt Engineering  | Optimizing prompts, caching, cost reduction     |
| ai-02     | RAG Pipeline        | Building retrieval-augmented generation systems |
| ai-03     | Agent Orchestration | Multi-agent systems, tool calling               |
| ai-04     | Guardrails & Safety | Content moderation, injection prevention        |
| ai-05     | Vector Embeddings   | Embedding pipelines, similarity search          |
| ai-06     | LLM Evaluation      | Benchmarking, quality scoring                   |
| ai-07     | Production LLM API  | Multi-provider clients, async processing        |
| ai-08     | Marketing AI        | Email generation, SEO, lead scoring             |
| **ai-09** | **Fine-Tuning**     | LoRA, QLoRA, PEFT, custom models                |
| **ai-10** | **Multimodal AI**   | Vision, audio, video, document understanding    |
| **ai-11** | **AI Agents 2.0**   | MCP integration, planning, advanced memory      |
| **ai-12** | **Local LLMs**      | Ollama, vLLM, on-prem deployment                |
| **ai-13** | **Synthetic Data**  | Training data generation                        |

### ML Engineer Agent

| Skill | Name                  | When to Use                         |
| ----- | --------------------- | ----------------------------------- |
| ml-01 | MLOps Pipeline        | End-to-end ML pipelines             |
| ml-02 | Feature Engineering   | Feature creation and transformation |
| ml-03 | Training Pipeline     | Model training workflows            |
| ml-04 | Model Serving         | Deployment and inference            |
| ml-05 | Model Monitoring      | Drift detection, performance        |
| ml-06 | Distributed Training  | Large-scale training                |
| ml-07 | Model Registry        | Version management                  |
| ml-08 | Model Compression     | Optimization for inference          |
| ml-09 | Continuous Retraining | Automated retraining                |

### Data Scientist Agent

| Skill | Name                      | When to Use                   |
| ----- | ------------------------- | ----------------------------- |
| ds-01 | Exploratory Data Analysis | Data understanding            |
| ds-02 | Statistical Modeling      | Hypothesis testing, inference |
| ds-03 | Feature Engineering       | Feature creation for ML       |
| ds-04 | Predictive Modeling       | Classification, regression    |
| ds-05 | Customer Analytics        | Churn, LTV, segmentation      |
| ds-06 | Campaign Analysis         | Marketing analytics           |
| ds-07 | A/B Testing               | Experimentation design        |
| ds-08 | Data Visualization        | Dashboards, reports           |

### MLOps Engineer Agent

| Skill | Name                   | When to Use              |
| ----- | ---------------------- | ------------------------ |
| mo-01 | Pipeline Orchestration | Workflow management      |
| mo-02 | Experiment Tracking    | MLflow, W&B integration  |
| mo-03 | Model Registry         | Model versioning         |
| mo-04 | Feature Store          | Feature management       |
| mo-05 | Model Deployment       | Production serving       |
| mo-06 | ML Observability       | Monitoring, logging      |
| mo-07 | Data Versioning        | DVC, data tracking       |
| mo-08 | A/B Testing Infra      | Experimentation platform |
| mo-09 | Automated Retraining   | Trigger-based retraining |

---

## Platform Domain

### DevOps Engineer Agent

| Skill | Name                    | When to Use              |
| ----- | ----------------------- | ------------------------ |
| do-01 | CI/CD Pipeline          | Automated build/deploy   |
| do-02 | Container Orchestration | Kubernetes, Docker Swarm |
| do-03 | Infrastructure as Code  | Terraform, Pulumi, CDK   |
| do-04 | GitOps                  | ArgoCD, Flux             |
| do-05 | Environment Management  | Dev/staging/prod         |
| do-06 | Pipeline Testing        | Pipeline validation      |
| do-07 | Release Management      | Versioning, rollbacks    |
| do-08 | Monitoring & Alerting   | Prometheus, Grafana      |
| do-09 | DevSecOps               | Security scanning        |

### SRE Agent

| Skill | Name                 | When to Use               |
| ----- | -------------------- | ------------------------- |
| sr-01 | Incident Response    | Runbooks, escalation      |
| sr-02 | Chaos Engineering    | Fault injection           |
| sr-03 | SLO Definition       | SLIs, targets             |
| sr-04 | Error Budgets        | Burn rate alerts          |
| sr-05 | On-Call Management   | Rotation setup            |
| sr-06 | Reliability Patterns | Circuit breakers, retries |
| sr-07 | Disaster Recovery    | RTO/RPO planning          |

### Docker Specialist Agent

| Skill     | Name                      | When to Use         |
| --------- | ------------------------- | ------------------- |
| docker-01 | Dockerfile Best Practices | Container creation  |
| docker-02 | Container Security        | Scanning, hardening |
| docker-03 | Image Optimization        | Size reduction      |
| docker-04 | Docker Compose            | Multi-container     |
| docker-05 | Container Registry        | Image management    |

### Cloud Specialists (AWS/Azure/GCP)

Each has 12 skills covering: Compute, Serverless, Storage, Database, Analytics, Networking, IAM, Monitoring, Kubernetes, Messaging, IaC, Cost Management.

---

## Security Domain

### Security Architect Agent

| Skill     | Name                      | When to Use                       |
| --------- | ------------------------- | --------------------------------- |
| sa-01     | PII Detection             | Personal data identification      |
| sa-02     | Threat Modeling           | STRIDE analysis                   |
| sa-03     | Infrastructure Security   | IaC security policies             |
| sa-04     | IAM Design                | RBAC, least privilege             |
| sa-05     | Application Security      | OWASP, secure coding              |
| sa-06     | Secrets Management        | Vault, Key Vault                  |
| sa-07     | Security Monitoring       | SIEM, alerting                    |
| **sa-08** | **API Security**          | OAuth2, OIDC, JWT, API gateways   |
| **sa-09** | **Supply Chain Security** | SBOM, Sigstore, SLSA              |
| **sa-10** | **Zero Trust**            | Never trust, always verify        |
| **sa-11** | **CSPM**                  | Cloud security posture management |

### Compliance Officer Agent

| Skill | Name                 | When to Use          |
| ----- | -------------------- | -------------------- |
| co-01 | SOC 2 Audit          | Type 1/2 preparation |
| co-02 | GDPR Compliance      | EU data protection   |
| co-03 | HIPAA Compliance     | Healthcare data      |
| co-04 | PCI-DSS Compliance   | Payment card data    |
| co-05 | ISO 27001            | ISMS certification   |
| co-06 | Audit Trails         | Logging requirements |
| co-07 | Policy Documentation | Policy creation      |

### Security Hardener Agent

| Skill | Name                     | When to Use       |
| ----- | ------------------------ | ----------------- |
| sh-01 | Vulnerability Scanning   | CVE detection     |
| sh-02 | Secure Configuration     | CIS benchmarks    |
| sh-03 | Attack Surface Reduction | Minimize exposure |
| sh-04 | Security Testing         | Pen testing prep  |
| sh-05 | Incident Preparation     | Response planning |

---

## Data Domain

### Data Engineer Agent

| Skill | Name                     | When to Use            |
| ----- | ------------------------ | ---------------------- |
| de-01 | Lakehouse Architecture   | Medallion architecture |
| de-02 | ETL/ELT Pipeline         | Data movement          |
| de-03 | Data Quality             | Validation, testing    |
| de-04 | Streaming Pipelines      | Real-time processing   |
| de-05 | Performance Optimization | Query tuning           |
| de-06 | Cloud Data Infra         | Cloud storage setup    |
| de-07 | Database Integration     | Multi-DB support       |
| de-08 | Marketing Data Pipelines | Marketing ETL          |
| de-09 | Pipeline Monitoring      | Observability          |

### Data Governance Agent

| Skill | Name                   | When to Use         |
| ----- | ---------------------- | ------------------- |
| dg-01 | Data Catalog           | Asset discovery     |
| dg-02 | Data Lineage           | Flow tracking       |
| dg-03 | Data Quality Framework | Standards           |
| dg-04 | Access Control         | Row/column security |
| dg-05 | Master Data Management | Golden records      |
| dg-06 | Compliance & Privacy   | GDPR implementation |

### Database Admin Agent

| Skill | Name                   | When to Use        |
| ----- | ---------------------- | ------------------ |
| db-01 | Query Optimization     | Performance tuning |
| db-02 | Index Strategies       | Index design       |
| db-03 | Backup & Recovery      | DR planning        |
| db-04 | Replication Setup      | High availability  |
| db-05 | Performance Tuning     | Overall DB perf    |
| db-06 | Schema Migrations      | Version control    |
| db-07 | Transaction Management | ACID compliance    |

---

## Product Domain

### Product Designer Agent

| Skill | Name                     | When to Use            |
| ----- | ------------------------ | ---------------------- |
| pd-01 | Requirements Discovery   | PRD creation           |
| pd-02 | User Research            | Interviews, personas   |
| pd-03 | Brainstorming & Ideation | Design sprints         |
| pd-04 | UX Design                | Wireframes, prototypes |
| pd-05 | Product-Market Fit       | Validation             |
| pd-06 | Stakeholder Management   | Alignment              |

### Frontend Developer Agent

| Skill | Name                     | When to Use              |
| ----- | ------------------------ | ------------------------ |
| fe-01 | React/Vue/Angular        | Framework implementation |
| fe-02 | State Management         | Redux, Zustand           |
| fe-03 | TypeScript               | Type-safe code           |
| fe-04 | Component Architecture   | Design systems           |
| fe-05 | Performance Optimization | Core Web Vitals          |
| fe-06 | Accessibility            | WCAG compliance          |
| fe-07 | Frontend Testing         | Jest, RTL                |

### Backend Developer Agent

| Skill | Name               | When to Use        |
| ----- | ------------------ | ------------------ |
| be-01 | REST API Design    | OpenAPI, endpoints |
| be-02 | GraphQL            | Schema, resolvers  |
| be-03 | Microservices      | Service design     |
| be-04 | Database Design    | Schema design      |
| be-05 | API Versioning     | Backward compat    |
| be-06 | Rate Limiting      | Throttling         |
| be-07 | Caching Strategies | Redis, CDN         |

### QA Engineer Agent

| Skill | Name                  | When to Use         |
| ----- | --------------------- | ------------------- |
| qa-01 | Test Strategy         | Planning            |
| qa-02 | Automation Frameworks | Playwright, Cypress |
| qa-03 | Integration Testing   | API tests           |
| qa-04 | Performance Testing   | Load testing        |
| qa-05 | Load Testing          | Stress testing      |
| qa-06 | Test Data Management  | Data generation     |
| qa-07 | Bug Tracking          | Reporting           |

### Technical Writer Agent

| Skill | Name              | When to Use      |
| ----- | ----------------- | ---------------- |
| tw-01 | API Documentation | OpenAPI, Swagger |
| tw-02 | User Guides       | End-user docs    |
| tw-03 | ADRs              | Decision records |
| tw-04 | Runbooks          | Operational docs |
| tw-05 | Knowledge Base    | Wiki articles    |
| tw-06 | Docs-as-Code      | Automated docs   |

### FinOps Engineer Agent

| Skill | Name                    | When to Use             |
| ----- | ----------------------- | ----------------------- |
| fo-01 | Cost Visibility         | Dashboards              |
| fo-02 | Resource Tagging        | Cost allocation         |
| fo-03 | Budget Management       | Alerts, limits          |
| fo-04 | Reserved Instances      | Commitment savings      |
| fo-05 | Spot Optimization       | Interruptible workloads |
| fo-06 | Storage Tiering         | Cost-effective storage  |
| fo-07 | AI/ML Cost Optimization | Model cost reduction    |
| fo-08 | Chargeback              | Team billing            |

---

## Infrastructure Domain

### MCP Manager Agent (NEW)

| Skill  | Name                 | When to Use                   |
| ------ | -------------------- | ----------------------------- |
| mcp-01 | MCP Server Registry  | Available servers and configs |
| mcp-02 | Dynamic Activation   | Activate servers on-demand    |
| mcp-03 | Context Optimization | Minimize token usage          |
| mcp-04 | Lifecycle Management | Activate/deactivate protocol  |
| mcp-05 | Server Catalog       | Available MCP servers         |

### Context Optimization (System-Wide)

| Skill  | Name                   | When to Use                  |
| ------ | ---------------------- | ---------------------------- |
| ctx-01 | Lazy Loading           | File/code reading efficiency |
| ctx-02 | Database Optimization  | Minimal SQL queries          |
| ctx-03 | API Optimization       | Paginate, filter, cache      |
| ctx-04 | MCP Efficiency         | Server activation patterns   |
| ctx-05 | Caching Strategies     | Reduce repeated fetches      |
| ctx-06 | Progressive Disclosure | Load incrementally           |

---

## Data Engineering Advanced

| Skill | Name           | When to Use                     |
| ----- | -------------- | ------------------------------- |
| de-10 | Reverse ETL    | Warehouse → operational systems |
| de-11 | Data Contracts | Schema enforcement, SLAs        |
| de-12 | Semantic Layer | Consistent metrics definitions  |
| de-13 | Data Mesh      | Domain ownership, federation    |
