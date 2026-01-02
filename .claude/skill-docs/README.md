# Tech Hub Skill Library

This directory contains the detailed skill documentation for all **Specialist Agents**. These files are loaded **on-demand** by Lead Agents or the Orchestrator to maintain context efficiency.

## 🎯 Architecture: On-Demand Loading

To save up to 95% in token costs, only high-level registries are loaded at startup. Detailed guidance from this directory is read ONLY when a specific role is activated.

### Loading Protocol

1.  **Lead/Orchestrator** identifies the need for a specialist (e.g., SRE).
2.  **Lead/Orchestrator** uses the `Read` tool to load `.claude/skill-docs/sre.md`.
3.  The agent now has full expert guidance for SRE tasks.
4.  Guidance is summarized and unloaded after the milestone is complete.

## 📚 Specialist Role Files

### Core Engineering

- `ai-engineer.md`: LLMs, RAG, Agents, Guardrails, Embeddings
- `data-engineer.md`: Pipelines, Lakehouse, Quality, Streaming
- `ml-engineer.md`: MLOps, Training, Serving, Monitoring
- `data-scientist.md`: EDA, Statistical Modeling, Experimentation
- `frontend-developer.md`: React, TypeScript, Component Architecture
- `backend-developer.md`: REST, GraphQL, Microservices, Caching

### Architecture & Security

- `security-architect.md`: PII Detection, IAM, Compliance, Threat Modeling
- `system-design.md`: Patterns, Scalability, HA/DR, APIs
- `network-engineer.md`: Topology, VPN/VPC, Load Balancers

### Platform & Operations

- `platform-engineer.md`: IDP, SLO/SLI, Self-Service
- `devops.md`: CI/CD, IaC, GitOps, Monitoring
- `sre.md`: Incident Response, Chaos Engineering, SLOs
- `database-admin.md`: Optimization, Replication, Migrations
- `data-governance.md`: Catalog, Lineage, Quality, Access Control
- `finops.md`: Cost optimization (MANDATORY for cloud)
- `docker.md`: Container Best Practices, Security

### Cloud Platforms

- `azure.md`: Dedicated Azure service guidance
- `aws.md`: Dedicated AWS service guidance
- `gcp.md`: Dedicated GCP service guidance

### Enterprise & Governance

- `code-review.md`: Quality gates, PR automation
- `compliance-officer.md`: SOC 2, GDPR, HIPAA, PCI-DSS
- `compliance-automation.md`: Policy-as-code and automated checks

### Product & Quality

- `product-designer.md`: Requirements, UX, Research
- `qa-engineer.md`: Test strategy, Automation, Performance
- `technical-writer.md`: API Docs, ADRs, Runbooks

## 🚀 Usage by Agents

Agents should reference these files using the `Read` tool as follows:
`Read: .claude/skill-docs/{role}.md`

Example for a Security Audit:

1.  **Orchestrator** identifies "Security audit" keyword.
2.  **Orchestrator** loads `security-architect.md`.
3.  **Orchestrator** applies `sa-01` (PII) and `sa-02` (Threat Modeling) guidance.

---

_Part of Tech Hub Skills v2.2.1_
