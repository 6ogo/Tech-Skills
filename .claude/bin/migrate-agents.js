#!/usr/bin/env node

/**
 * Agent Migration Script
 * Flattens agents from leads/ and specialists/ to root agents/ directory
 * Adds proper YAML frontmatter for Claude Code discovery
 */

const fs = require("fs");
const path = require("path");

const AGENTS_DIR = path.join(__dirname, "..", "agents");
const LEADS_DIR = path.join(AGENTS_DIR, "leads");
const SPECIALISTS_DIR = path.join(AGENTS_DIR, "specialists");

// Agent configuration for YAML frontmatter
const agentConfigs = {
  // Lead Agents - use "sonnet" for coordination
  "ai-ml-lead.md": {
    name: "AI/ML Lead",
    model: "sonnet",
    description:
      "Coordinates AI/ML initiatives - manages AI Engineers, ML Engineers, Data Scientists, and MLOps specialists",
  },
  "data-lead.md": {
    name: "Data Lead",
    model: "sonnet",
    description:
      "Coordinates data initiatives - manages Data Engineers, Data Governance, and Database Admins",
  },
  "platform-lead.md": {
    name: "Platform Lead",
    model: "sonnet",
    description:
      "Coordinates infrastructure and DevOps - manages DevOps, SRE, Platform Engineers, and Cloud specialists",
  },
  "product-lead.md": {
    name: "Product Lead",
    model: "sonnet",
    description:
      "Coordinates product development - manages Designers, Frontend/Backend Devs, QA, and Technical Writers",
  },
  "security-lead.md": {
    name: "Security Lead",
    model: "sonnet",
    description:
      "Coordinates security and compliance - manages Security Architects, Compliance Officers, and Security Hardeners",
  },

  // Specialist Agents - use "haiku" for efficiency (fast, cheap, focused tasks)
  "ai-engineer-agent.md": {
    name: "AI Engineer",
    model: "haiku",
    description:
      "Expert in LLMs, RAG systems, AI agents, and production AI applications",
  },
  "aws-specialist-agent.md": {
    name: "AWS Specialist",
    model: "haiku",
    description:
      "Expert in Amazon Web Services - EC2, S3, Lambda, ECS, RDS, and AWS-native architectures",
  },
  "azure-specialist-agent.md": {
    name: "Azure Specialist",
    model: "haiku",
    description:
      "Expert in Microsoft Azure - VMs, AKS, Functions, Cosmos DB, and Azure-native solutions",
  },
  "backend-developer-agent.md": {
    name: "Backend Developer",
    model: "haiku",
    description:
      "Expert in APIs, microservices, databases, and server-side development",
  },
  "compliance-officer-agent.md": {
    name: "Compliance Officer",
    model: "haiku",
    description:
      "Expert in GDPR, HIPAA, SOC 2, ISO 27001, and regulatory compliance frameworks",
  },
  "data-engineer-agent.md": {
    name: "Data Engineer",
    model: "haiku",
    description:
      "Expert in data pipelines, ETL/ELT, data lakes, and distributed data processing",
  },
  "data-governance-agent.md": {
    name: "Data Governance",
    model: "haiku",
    description:
      "Expert in data catalogs, lineage, quality rules, and governance frameworks",
  },
  "data-scientist-agent.md": {
    name: "Data Scientist",
    model: "haiku",
    description:
      "Expert in EDA, feature engineering, predictive modeling, and statistical analysis",
  },
  "database-admin-agent.md": {
    name: "Database Admin",
    model: "haiku",
    description:
      "Expert in SQL/NoSQL databases, performance tuning, replication, and database security",
  },
  "devops-engineer-agent.md": {
    name: "DevOps Engineer",
    model: "haiku",
    description:
      "Expert in CI/CD, GitOps, IaC, containers, and deployment automation",
  },
  "docker-specialist-agent.md": {
    name: "Docker Specialist",
    model: "haiku",
    description:
      "Expert in containerization, Docker Compose, multi-stage builds, and container security",
  },
  "finops-engineer-agent.md": {
    name: "FinOps Engineer",
    model: "haiku",
    description:
      "Expert in cloud cost optimization, resource right-sizing, and financial governance",
  },
  "frontend-developer-agent.md": {
    name: "Frontend Developer",
    model: "haiku",
    description:
      "Expert in React, Vue, accessibility, responsive design, and frontend architecture",
  },
  "gcp-specialist-agent.md": {
    name: "GCP Specialist",
    model: "haiku",
    description:
      "Expert in Google Cloud Platform - GKE, BigQuery, Cloud Run, and GCP-native solutions",
  },
  "mcp-manager-agent.md": {
    name: "MCP Manager",
    model: "sonnet", // Sonnet for complex tool management
    description:
      "Expert in Model Context Protocol server management, tool integration, and context optimization",
  },
  "ml-engineer-agent.md": {
    name: "ML Engineer",
    model: "haiku",
    description:
      "Expert in model training, serving, optimization, and ML systems architecture",
  },
  "mlops-engineer-agent.md": {
    name: "MLOps Engineer",
    model: "haiku",
    description:
      "Expert in ML pipelines, experiment tracking, model registry, and ML infrastructure",
  },
  "network-engineer-agent.md": {
    name: "Network Engineer",
    model: "haiku",
    description:
      "Expert in VPC, DNS, load balancing, CDN, and network security",
  },
  "platform-engineer-agent.md": {
    name: "Platform Engineer",
    model: "haiku",
    description:
      "Expert in internal developer platforms, SLOs, golden paths, and platform APIs",
  },
  "product-designer-agent.md": {
    name: "Product Designer",
    model: "haiku",
    description:
      "Expert in user research, wireframes, prototyping, and UX design",
  },
  "qa-engineer-agent.md": {
    name: "QA Engineer",
    model: "haiku",
    description:
      "Expert in test automation, E2E testing, load testing, and quality assurance",
  },
  "security-architect-agent.md": {
    name: "Security Architect",
    model: "haiku",
    description:
      "Expert in threat modeling, PII detection, IAM design, and application security",
  },
  "security-hardener-agent.md": {
    name: "Security Hardener",
    model: "haiku",
    description:
      "Expert in security hardening, vulnerability remediation, and security configurations",
  },
  "sre-agent.md": {
    name: "SRE",
    model: "haiku",
    description:
      "Expert in reliability engineering, incident response, SLIs/SLOs, and observability",
  },
  "technical-writer-agent.md": {
    name: "Technical Writer",
    model: "haiku",
    description:
      "Expert in API docs, user guides, architecture documentation, and technical content",
  },
};

function addFrontmatter(content, config) {
  // Check if frontmatter already exists
  if (content.trim().startsWith("---")) {
    console.log(`  ⚠️  Already has frontmatter, skipping`);
    return content;
  }

  const frontmatter = `---
name: "${config.name}"
model: "${config.model}"
description: "${config.description}"
---

`;

  // Remove the old Agent Identity code block if present
  const identityBlockRegex = /## Agent Identity\s*\n\s*```yaml[\s\S]*?```\s*\n/;
  let newContent = content.replace(identityBlockRegex, "");

  return frontmatter + newContent;
}

function migrateAgents() {
  console.log(
    "\n🔄 Migrating agents to flat structure with YAML frontmatter...\n"
  );

  let migrated = 0;
  let skipped = 0;

  // Process leads
  if (fs.existsSync(LEADS_DIR)) {
    const leadFiles = fs
      .readdirSync(LEADS_DIR)
      .filter((f) => f.endsWith(".md"));
    console.log(`📁 Processing ${leadFiles.length} lead agents...`);

    for (const file of leadFiles) {
      const srcPath = path.join(LEADS_DIR, file);
      const destPath = path.join(AGENTS_DIR, file);
      const config = agentConfigs[file];

      if (!config) {
        console.log(`  ⚠️  No config for ${file}, skipping`);
        skipped++;
        continue;
      }

      console.log(`  → ${file}`);
      let content = fs.readFileSync(srcPath, "utf8");
      content = addFrontmatter(content, config);
      fs.writeFileSync(destPath, content);
      migrated++;
    }
  }

  // Process specialists
  if (fs.existsSync(SPECIALISTS_DIR)) {
    const specialistFiles = fs
      .readdirSync(SPECIALISTS_DIR)
      .filter((f) => f.endsWith(".md"));
    console.log(
      `\n📁 Processing ${specialistFiles.length} specialist agents...`
    );

    for (const file of specialistFiles) {
      const srcPath = path.join(SPECIALISTS_DIR, file);
      const destPath = path.join(AGENTS_DIR, file);
      const config = agentConfigs[file];

      if (!config) {
        console.log(`  ⚠️  No config for ${file}, skipping`);
        skipped++;
        continue;
      }

      console.log(`  → ${file}`);
      let content = fs.readFileSync(srcPath, "utf8");
      content = addFrontmatter(content, config);
      fs.writeFileSync(destPath, content);
      migrated++;
    }
  }

  console.log(`\n✅ Migration complete!`);
  console.log(`   Migrated: ${migrated} agents`);
  console.log(`   Skipped: ${skipped} agents`);
  console.log(`\n📍 Agents are now in: ${AGENTS_DIR}`);
  console.log(
    `\n💡 You can safely delete the leads/ and specialists/ subdirectories after verification.`
  );
}

migrateAgents();
