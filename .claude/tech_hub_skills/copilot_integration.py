#!/usr/bin/env python3
"""GitHub Copilot integration for Tech Hub Skills."""

from pathlib import Path
from typing import List, Dict


def generate_copilot_instructions(skills_dir: Path, roles_dir: Path, selected_roles: List[str] = None) -> str:
    """
    Generate GitHub Copilot instructions file content.

    Args:
        skills_dir: Path to skills directory
        roles_dir: Path to roles directory
        selected_roles: Optional list of specific roles to include (default: all)

    Returns:
        Generated markdown content for .github/copilot-instructions.md
    """

    content = """# GitHub Copilot Instructions - Tech Hub Skills

## Overview
This workspace uses Tech Hub Skills - 110+ production-ready AI agent skills for software engineering.

## Available Expert Roles

"""

    # Role metadata
    all_roles = {
        "orchestrator": {"name": "Orchestrator", "skills": "Routes all", "focus": "Project coordination"},
        "ai-engineer": {"name": "AI Engineer", "skills": "8", "focus": "LLMs, RAG, Agents"},
        "data-engineer": {"name": "Data Engineer", "skills": "9", "focus": "Pipelines, Lakehouse"},
        "ml-engineer": {"name": "ML Engineer", "skills": "9", "focus": "Training, Serving, MLOps"},
        "data-scientist": {"name": "Data Scientist", "skills": "8", "focus": "Analytics, Modeling"},
        "security-architect": {"name": "Security Architect", "skills": "7", "focus": "PII, IAM, Compliance"},
        "system-design": {"name": "System Design", "skills": "8", "focus": "Architecture, Scalability"},
        "platform-engineer": {"name": "Platform Engineer", "skills": "6", "focus": "IDP, SLOs"},
        "data-governance": {"name": "Data Governance", "skills": "6", "focus": "Catalog, Lineage, Quality"},
        "devops": {"name": "DevOps", "skills": "9", "focus": "CI/CD, Containers, IaC"},
        "mlops": {"name": "MLOps", "skills": "9", "focus": "Experiments, Registry"},
        "finops": {"name": "FinOps", "skills": "8", "focus": "Cost Optimization"},
        "azure": {"name": "Azure", "skills": "12", "focus": "Azure Services"},
        "code-review": {"name": "Code Review", "skills": "5", "focus": "PR Automation, Quality Gates"},
        "product-designer": {"name": "Product Designer", "skills": "6", "focus": "Requirements, UX"},
    }

    # Filter roles if specified
    if selected_roles:
        roles_to_include = {k: v for k, v in all_roles.items() if k in selected_roles}
    else:
        roles_to_include = all_roles

    # Add role summaries
    for role_key, role_info in roles_to_include.items():
        content += f"### {role_info['name']}\n"
        content += f"- **Focus**: {role_info['focus']}\n"
        content += f"- **Skills**: {role_info['skills']} specialized capabilities\n\n"

    content += """
## How to Use These Skills

When working on tasks, Copilot will reference these expert roles automatically. You can also:

1. **Mention roles in comments**: `// Using AI Engineer approach for RAG pipeline`
2. **Request specific expertise**: `# Apply Security Architect best practices`
3. **Combine roles**: `/* DevOps + FinOps: optimize CI/CD costs */`

## Coding Standards

"""

    # Add role-specific instructions
    if "security-architect" in roles_to_include or not selected_roles:
        content += """
### Security (Security Architect)
- Always validate and sanitize user inputs
- Implement proper authentication and authorization
- Never hardcode secrets or credentials
- Use parameterized queries to prevent SQL injection
- Apply principle of least privilege
- Scan for PII before logging

"""

    if "ai-engineer" in roles_to_include or not selected_roles:
        content += """
### AI/ML Development (AI Engineer)
- Implement guardrails for LLM outputs
- Use prompt templates for consistency
- Monitor token usage and costs
- Implement proper error handling for API calls
- Cache embeddings when possible
- Version control prompts and models

"""

    if "data-engineer" in roles_to_include or not selected_roles:
        content += """
### Data Engineering (Data Engineer)
- Follow medallion architecture (bronze/silver/gold)
- Implement idempotent pipelines
- Add data quality checks at each stage
- Use partitioning for large datasets
- Implement proper error handling and retries
- Document data lineage

"""

    if "devops" in roles_to_include or not selected_roles:
        content += """
### DevOps Practices
- Write infrastructure as code (IaC)
- Implement CI/CD pipelines
- Use containerization (Docker)
- Apply GitOps principles
- Implement monitoring and alerting
- Automate testing at all levels

"""

    content += """
## Project Structure

Follow these conventions:
- `/src` - Source code
- `/tests` - Test files
- `/docs` - Documentation
- `/infrastructure` - IaC templates
- `/pipelines` - CI/CD configurations
- `/.github` - GitHub workflows and configurations

## Quality Gates

All code should:
-  Pass unit tests (>80% coverage)
-  Pass linting and formatting
-  Include error handling
-  Have inline documentation
-  Follow security best practices
-  Be optimized for performance

## Tech Hub Skills Integration

These instructions are generated from Tech Hub Skills package.
To update: `tech-hub-skills install --copilot`

---
*Generated by Tech Hub Skills v2.0.0*
"""

    return content


def install_copilot_instructions(
    project_dir: Path,
    skills_dir: Path,
    roles_dir: Path,
    selected_roles: List[str] = None,
    force: bool = False
) -> bool:
    """
    Install GitHub Copilot instructions file to project.

    Args:
        project_dir: Root directory of the project
        skills_dir: Path to skills directory
        roles_dir: Path to roles directory
        selected_roles: Optional list of specific roles to include
        force: Whether to overwrite existing file

    Returns:
        True if successful, False otherwise
    """

    github_dir = project_dir / ".github"
    copilot_file = github_dir / "copilot-instructions.md"

    # Check if file exists
    if copilot_file.exists() and not force:
        print(f"    Copilot instructions already exist at: {copilot_file}")
        print(f"      Use --force to overwrite")
        return False

    # Create .github directory if it doesn't exist
    github_dir.mkdir(parents=True, exist_ok=True)

    # Generate and write instructions
    content = generate_copilot_instructions(skills_dir, roles_dir, selected_roles)
    copilot_file.write_text(content, encoding="utf-8")

    print(f"   GitHub Copilot instructions created: {copilot_file}")
    return True


def get_available_roles() -> List[str]:
    """Get list of available role identifiers."""
    return [
        "orchestrator",
        "ai-engineer",
        "data-engineer",
        "ml-engineer",
        "data-scientist",
        "security-architect",
        "system-design",
        "platform-engineer",
        "data-governance",
        "devops",
        "mlops",
        "finops",
        "azure",
        "code-review",
        "product-designer",
    ]
