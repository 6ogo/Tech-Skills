# Tech Hub Claude Skills

This directory contains Claude Code skills that provide intelligent access to the complete Tech Hub skills library (**100+ production-ready skills across 12 roles**).

##  Primary Skill: ORCHESTRATOR

**Start here for any project!**

The `orchestrator` skill is your intelligent project manager that:

- Analyzes project requirements
- Selects optimal skill combinations across multiple roles
- Applies best practices automatically (cost, security, quality)
- Generates comprehensive execution plans
- Coordinates cross-role integrations

### How to Use the Orchestrator

In Claude Code, simply describe your project:

```
@orchestrator I need to build a customer churn prediction model
```

The orchestrator will:

1. Analyze domain, complexity, and compliance needs
2. Select optimal skills (PII detection, data pipelines, ML training, deployment, monitoring)
3. Apply automatic cost optimizations (70-90% savings)
4. Generate a phased implementation plan
5. Reference specific skill documentation for implementation

##  All Available Skills

### Core Engineering Roles

| Skill File          | Role             | When to Use                                   |
| ------------------- | ---------------- | --------------------------------------------- |
| `ai-engineer.md`    | AI Engineering   | LLMs, RAG, Agents, Embeddings, LLM APIs       |
| `data-engineer.md`  | Data Engineering | Pipelines, Lakehouse, Data Quality, Streaming |
| `ml-engineer.md`    | ML Engineering   | MLOps, Training, Serving, Monitoring          |
| `data-scientist.md` | Data Science     | EDA, Statistical Modeling, Experimentation    |

### Architecture & Security Roles

| Skill File              | Role          | When to Use                                     |
| ----------------------- | ------------- | ----------------------------------------------- |
| `security-architect.md` | Security      | PII Detection, IAM, Compliance, Threat Modeling |
| `system-design.md`      | System Design | Architecture Patterns, Scalability, HA/DR, APIs |

### Platform & Operations Roles

| Skill File             | Role                 | When to Use                                           |
| ---------------------- | -------------------- | ----------------------------------------------------- |
| `platform-engineer.md` | Platform Engineering | Internal Developer Platform, SLO/SLI, Self-Service    |
| `data-governance.md`   | Data Governance      | Data Catalog, Quality, Lineage, Access Control        |
| `devops.md`            | DevOps               | CI/CD, IaC, Containers, Monitoring                    |
| `docker.md`            | Docker/Containers    | Dockerfile Best Practices, Security, Optimization     |
| `mlops.md`             | MLOps                | Experiment Tracking, Model Registry, Deployment       |
| `finops.md`            | FinOps               | Cost Optimization, Budget Management (70-90% savings) |

### Cloud Platform

| Skill File | Role        | When to Use                                          |
| ---------- | ----------- | ---------------------------------------------------- |
| `azure.md` | Azure Cloud | All Azure services from Infrastructure to Event Hubs |

### Specialized Skills

| Skill File              | Purpose              | When to Use                                             |
| ----------------------- | -------------------- | ------------------------------------------------------- |
| `orchestrator.md`       | Project Coordination | **Start here** - Analyzes and plans multi-role projects |
| `process-automation.md` | Process Optimization | Analyze and automate business processes                 |

### Process Management Skills

| Skill File                 | Purpose             | When to Use                                 |
| -------------------------- | ------------------- | ------------------------------------------- |
| `process-kanban.md`        | Task Management     | Create epics, stories, sub-tasks for Kanban |
| `process-documentation.md` | Azure Wiki & Docs   | Document solutions, create runbooks         |
| `process-changelog.md`     | Changelog           | Maintain CHANGELOG.md, release notes        |
| `process-versioning.md`    | Semantic Versioning | Version bumping (x.x.x), release strategy   |

##  Quick Start Examples

### Example 1: Simple Data Task

```
@data-engineer Create a Python script to process CSV files with data quality checks
```

### Example 2: AI Application

```
@orchestrator Build a RAG chatbot for our internal knowledge base
```

The orchestrator will recommend:

- ai-02 (RAG Pipeline) with PII detection
- ai-01 (Prompt Engineering) with 90% cost savings via caching
- sa-01 (PII Detection) for document scanning
- docker-01 (Containerization) for deployment
- fo-01, fo-07 (Cost tracking and AI optimization)
- do-01, do-08 (CI/CD and monitoring)

### Example 3: ML Project

```
@orchestrator Implement a demand forecasting model
```

Recommended skills:

- sa-01 (PII detection if customer data)
- dg-01 (Data catalog registration)
- de-01, de-02 (Lakehouse and ETL)
- ml-01, ml-02, ml-03 (MLOps pipeline, features, training)
- docker-01, docker-02 (Container build and security)
- mo-01, mo-03, mo-06 (Tracking, registry, monitoring)
- fo-05, fo-07 (Spot instances for 80% training cost savings)

### Example 4: Platform Engineering

```
@orchestrator Build a self-service developer platform
```

Recommended skills:

- pe-01 (Internal Developer Platform)
- pe-02 (Self-Service Infrastructure)
- pe-03 (SLO/SLI Management)
- do-02, do-04 (Kubernetes, GitOps)
- docker-01 (Container standards)

### Example 5: Data Governance

```
@orchestrator Implement enterprise data governance for compliance
```

Recommended skills:

- dg-01 (Data Catalog)
- dg-02 (Data Lineage)
- dg-03 (Data Quality Framework)
- dg-06 (Compliance & Privacy)
- sa-01 (PII Detection)

### Example 6: Docker/Container Project

```
@docker Containerize our Python API with security best practices
```

Will apply:

- docker-01 (Multi-stage builds, optimization)
- docker-02 (Security hardening, non-root)
- docker-03 (Image size reduction)
- Integration with CI/CD pipelines

##  When to Use Each Skill

### Use @orchestrator when:

- Starting a new project
- Need multi-role coordination
- Want comprehensive cost/security/quality analysis
- Unclear which skills are needed
- **This should be your default starting point**

### Use specific role skills when:

- You already know which domain (AI, ML, Data, etc.)
- Need detailed guidance for that specific role
- Want to dive deep into role-specific tools
- Have a clear single-role task

### Use @platform-engineer when:

- Building internal developer platforms
- Improving developer velocity
- Managing SLOs and error budgets
- Self-service infrastructure

### Use @data-governance when:

- Implementing data catalogs
- Data quality frameworks
- GDPR/compliance requirements
- Access control policies

### Use @docker when:

- Containerizing applications
- Optimizing Docker images
- Container security
- Multi-stage builds

### Use @finops when:

- Need cost reduction (critical for AI/ML projects)
- Budget management
- Cost visibility and tracking
- **Include for ANY cloud-based project**

### Use @security-architect when:

- Handling PII or sensitive data (MANDATORY)
- Security/compliance requirements
- IAM or access control needed
- **Include if any personal/sensitive data**

##  Detailed Documentation

All skills reference comprehensive documentation in the repository:

- **ORCHESTRATOR.md**: Complete skills map, 100+ skills overview
- **SKILLS_OVERVIEW.md**: Detailed inventory of all skills
- **{role}/best-practices.md**: Role-specific best practices
- **.claude/roles/{role}/skills/{skill-id}/README.md**: Individual skill documentation
- **{role}/walkthroughs/**: Step-by-step hands-on guides

Each skill documentation includes:

- Tools and scripts
- Best practices (cost, security, quality)
- Code examples
- Deployment pipelines
- Azure-specific guidance
- Quick wins

##  Integration Flow

```
User Request
    ↓
@orchestrator (analyzes and plans)
    ↓
Selects Skills Across Roles
     @ai-engineer (if AI/LLM needed)
     @data-engineer (if data pipelines needed)
     @ml-engineer (if ML models needed)
     @data-scientist (if analytics needed)
     @system-design (if architecture needed)
     @platform-engineer (if platform needed)
     @data-governance (if governance needed)
     @security-architect (if PII/sensitive data)
     @docker (if containers needed)
     @finops (for cost optimization - ALWAYS)
     @devops (for deployment - ALWAYS for production)
     @mlops (for AI/ML lifecycle)
    ↓
Implementation (references detailed READMEs)
    ↓
Deploy with Best Practices
    - 70-90% cost savings
    - Security by default
    - Production-ready
```

##  Automatic Cost Optimizations

All skills automatically recommend:

1. **AI/ML (70-90% savings)**

   - Prompt caching: 90% LLM cost reduction
   - Spot instances: 80% training cost savings
   - Auto-scaling: 40% serving cost savings
   - Embedding optimization: 60% savings

2. **Data (40-70% savings)**

   - Storage lifecycle: 50% storage savings
   - Right-sized compute: 30% savings
   - Incremental processing: 30% savings

3. **Infrastructure (30-50% savings)**

   - Reserved instances: 40% savings
   - Auto-shutdown: 40% savings
   - Right-sizing: 30% savings

4. **Containers (30-50% savings)**
   - Multi-stage builds: 50% smaller images
   - Minimal base images: 40% reduction
   - Layer optimization: 30% faster builds

##  Automatic Security

All skills enforce:

- **PII detection** (sa-01) before processing
- **Least privilege** access control
- **Encryption** at rest and in transit
- **Audit logging** for compliance
- **Security scanning** in CI/CD
- **Container security** (non-root, vulnerability scanning)

##  Success Metrics

Using these skills, you can achieve:

- **70-90% cost savings** vs naive implementations
- **PII-protected** and compliant systems
- **Production-ready** with monitoring
- **Automated deployment** with CI/CD
- **Continuous improvement** with MLOps
- **Self-service** with Platform Engineering
- **Governed data** with Data Governance

##  Learning Path

1. **Start**: Use `@orchestrator` for your first project
2. **Learn**: Review the recommended skills documentation
3. **Specialize**: Use role-specific skills as you gain expertise
4. **Optimize**: Always include `@finops` for cost optimization
5. **Secure**: Always include `@security-architect` for PII/sensitive data
6. **Containerize**: Use `@docker` for production deployments

##  Getting Help

1. **Unclear which skill**: Start with `@orchestrator`
2. **Cost concerns**: Use `@finops` for optimization strategies
3. **Security questions**: Use `@security-architect`
4. **Container questions**: Use `@docker`
5. **Platform questions**: Use `@platform-engineer`
6. **Data governance**: Use `@data-governance`
7. **Detailed implementation**: Read skill READMEs in the repo

---

**Start with `@orchestrator` for any project - it's your intelligent guide to the complete Tech Hub!**
