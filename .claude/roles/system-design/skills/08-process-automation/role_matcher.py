"""
Role Matcher - Maps processes to the most suitable roles and skills.

Part of the Tech Hub Skills Library (sd-08: Process Automation).
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set, Tuple
from enum import Enum

from process_analyzer import ProcessAnalysis, AutomationType


@dataclass
class Skill:
    """Represents a Tech Hub skill."""
    id: str
    name: str
    role: str
    complexity: str
    description: str
    keywords: List[str] = field(default_factory=list)


@dataclass
class RoleAssignment:
    """Assignment of a role to a process automation task."""
    role: str
    role_name: str
    affinity_score: float  # 0-100
    skills_required: List[str]
    responsibilities: List[str]
    effort_percentage: float
    is_primary: bool = False


@dataclass
class TeamComposition:
    """Complete team composition for automation implementation."""
    assignments: List[RoleAssignment]
    skill_gaps: List[Dict]
    cross_functional_dependencies: List[Dict]
    recommended_team_size: int

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "assignments": [
                {
                    "role": a.role,
                    "role_name": a.role_name,
                    "affinity_score": a.affinity_score,
                    "skills": a.skills_required,
                    "effort_pct": a.effort_percentage,
                    "is_primary": a.is_primary
                }
                for a in self.assignments
            ],
            "skill_gaps": self.skill_gaps,
            "dependencies": self.cross_functional_dependencies,
            "team_size": self.recommended_team_size
        }

    def get_primary_role(self) -> Optional[RoleAssignment]:
        """Get the primary role assignment."""
        for assignment in self.assignments:
            if assignment.is_primary:
                return assignment
        return self.assignments[0] if self.assignments else None


class RoleMatcher:
    """
    Maps processes to suitable roles and skills for implementation.

    Uses the Tech Hub skills library to identify the best team composition
    for implementing automation initiatives.
    """

    # Complete Tech Hub role definitions
    ROLES = {
        "ai-engineer": {
            "name": "AI Engineer",
            "focus": ["LLMs", "RAG", "Agents", "Prompt Engineering", "NLP"],
            "automation_types": [AutomationType.AI_POWERED],
            "skills": [
                Skill("ai-01", "Prompt Engineering & Optimization", "ai-engineer", "basic",
                      "Design and optimize prompts", ["prompt", "llm", "gpt", "template"]),
                Skill("ai-02", "RAG Pipeline Builder", "ai-engineer", "medium",
                      "Build retrieval augmented generation", ["rag", "vector", "embedding", "search"]),
                Skill("ai-03", "LLM Agent Orchestration", "ai-engineer", "advanced",
                      "Multi-agent systems", ["agent", "tool", "function", "reasoning"]),
                Skill("ai-04", "LLM Guardrails & Safety", "ai-engineer", "medium",
                      "Safety and content moderation", ["safety", "guardrail", "moderation"]),
                Skill("ai-05", "Vector Embeddings & Search", "ai-engineer", "medium",
                      "Semantic search systems", ["embedding", "vector", "similarity"]),
                Skill("ai-06", "LLM Evaluation & Benchmarking", "ai-engineer", "advanced",
                      "Evaluate LLM performance", ["evaluation", "benchmark", "metrics"]),
                Skill("ai-07", "Production LLM API Integration", "ai-engineer", "medium",
                      "LLM API integration", ["api", "openai", "azure", "integration"]),
                Skill("ai-08", "Marketing AI Automation", "ai-engineer", "expert",
                      "Marketing automation with AI", ["marketing", "content", "email", "seo"]),
            ]
        },
        "data-engineer": {
            "name": "Data Engineer",
            "focus": ["Pipelines", "ETL", "Lakehouse", "Streaming", "Data Quality"],
            "automation_types": [AutomationType.DATA_PIPELINE, AutomationType.WORKFLOW],
            "skills": [
                Skill("de-01", "Lakehouse Architecture", "data-engineer", "medium",
                      "Bronze-Silver-Gold architecture", ["lakehouse", "medallion", "delta"]),
                Skill("de-02", "ETL/ELT Pipeline Orchestration", "data-engineer", "medium",
                      "Data pipeline orchestration", ["etl", "elt", "pipeline", "airflow"]),
                Skill("de-03", "Data Quality & Validation", "data-engineer", "medium",
                      "Data quality checks", ["quality", "validation", "testing"]),
                Skill("de-04", "Real-Time Streaming Pipelines", "data-engineer", "advanced",
                      "Streaming data processing", ["streaming", "kafka", "real-time"]),
                Skill("de-05", "Performance Optimization", "data-engineer", "advanced",
                      "Query and pipeline optimization", ["performance", "optimization", "tuning"]),
                Skill("de-06", "Cloud Data Infrastructure", "data-engineer", "medium",
                      "Azure data infrastructure", ["azure", "cloud", "infrastructure"]),
                Skill("de-07", "Database Management & Migration", "data-engineer", "medium",
                      "Database operations", ["database", "sql", "migration"]),
                Skill("de-08", "Marketing Data Ingestion", "data-engineer", "medium",
                      "Marketing data sources", ["marketing", "salesforce", "crm"]),
                Skill("de-09", "Monitoring & Observability", "data-engineer", "medium",
                      "Pipeline monitoring", ["monitoring", "observability", "alerts"]),
            ]
        },
        "ml-engineer": {
            "name": "ML Engineer",
            "focus": ["MLOps", "Model Training", "Model Serving", "Feature Stores"],
            "automation_types": [AutomationType.ML_BASED],
            "skills": [
                Skill("ml-01", "MLOps Pipeline Automation", "ml-engineer", "medium",
                      "ML pipeline automation", ["mlops", "pipeline", "automation"]),
                Skill("ml-02", "Feature Engineering & Store", "ml-engineer", "medium",
                      "Feature store management", ["feature", "feast", "store"]),
                Skill("ml-03", "Model Training & Tuning", "ml-engineer", "medium",
                      "Model training", ["training", "hyperparameter", "tuning"]),
                Skill("ml-04", "Model Serving & APIs", "ml-engineer", "medium",
                      "Model deployment", ["serving", "inference", "api", "endpoint"]),
                Skill("ml-05", "Model Monitoring & Drift", "ml-engineer", "advanced",
                      "Model monitoring", ["monitoring", "drift", "performance"]),
                Skill("ml-06", "Distributed Training", "ml-engineer", "expert",
                      "Distributed ML", ["distributed", "gpu", "scaling"]),
                Skill("ml-07", "Model Versioning & Registry", "ml-engineer", "medium",
                      "Model registry", ["versioning", "registry", "mlflow"]),
                Skill("ml-08", "Model Compression", "ml-engineer", "advanced",
                      "Model optimization", ["compression", "quantization", "pruning"]),
                Skill("ml-09", "Continuous Retraining", "ml-engineer", "expert",
                      "Automated retraining", ["retraining", "continuous", "automation"]),
            ]
        },
        "data-scientist": {
            "name": "Data Scientist",
            "focus": ["Analytics", "Statistics", "Modeling", "Experimentation"],
            "automation_types": [AutomationType.ML_BASED],
            "skills": [
                Skill("ds-01", "Automated EDA", "data-scientist", "basic",
                      "Exploratory data analysis", ["eda", "analysis", "profiling"]),
                Skill("ds-02", "Statistical Modeling", "data-scientist", "medium",
                      "Statistical analysis", ["statistics", "hypothesis", "testing"]),
                Skill("ds-03", "Feature Engineering", "data-scientist", "medium",
                      "Feature creation", ["feature", "engineering", "transformation"]),
                Skill("ds-04", "Predictive Modeling", "data-scientist", "medium",
                      "Prediction models", ["prediction", "forecasting", "classification"]),
                Skill("ds-05", "Customer Analytics", "data-scientist", "advanced",
                      "Customer analysis", ["customer", "segmentation", "churn"]),
                Skill("ds-06", "Campaign Analysis", "data-scientist", "medium",
                      "Marketing analysis", ["campaign", "attribution", "roi"]),
                Skill("ds-07", "Experimentation & Causal", "data-scientist", "expert",
                      "A/B testing and causal", ["experiment", "ab-test", "causal"]),
                Skill("ds-08", "Data Visualization", "data-scientist", "medium",
                      "Visualization", ["visualization", "dashboard", "reporting"]),
            ]
        },
        "security-architect": {
            "name": "Security Architect",
            "focus": ["Security", "Compliance", "IAM", "Threat Modeling"],
            "automation_types": [AutomationType.SECURITY],
            "skills": [
                Skill("sa-01", "PII Detection & Privacy", "security-architect", "medium",
                      "PII and privacy", ["pii", "privacy", "gdpr", "anonymization"]),
                Skill("sa-02", "Threat Modeling", "security-architect", "medium",
                      "Threat analysis", ["threat", "risk", "stride"]),
                Skill("sa-03", "Infrastructure Security", "security-architect", "medium",
                      "IaC security", ["infrastructure", "iac", "hardening"]),
                Skill("sa-04", "Identity & Access Management", "security-architect", "medium",
                      "IAM", ["iam", "identity", "access", "rbac"]),
                Skill("sa-05", "Application Security", "security-architect", "medium",
                      "AppSec", ["sast", "dast", "appsec", "vulnerability"]),
                Skill("sa-06", "Secrets & Key Management", "security-architect", "basic",
                      "Secrets management", ["secrets", "keys", "vault"]),
                Skill("sa-07", "Security Monitoring", "security-architect", "advanced",
                      "Security monitoring", ["siem", "sentinel", "incident"]),
            ]
        },
        "system-design": {
            "name": "System Designer",
            "focus": ["Architecture", "Patterns", "Scalability", "Design"],
            "automation_types": [],
            "skills": [
                Skill("sd-01", "Architecture Pattern Selection", "system-design", "medium",
                      "Architecture patterns", ["architecture", "pattern", "microservices"]),
                Skill("sd-02", "Requirements Engineering", "system-design", "basic",
                      "Requirements", ["requirements", "user-story", "specification"]),
                Skill("sd-03", "Scalability & Performance", "system-design", "advanced",
                      "Scalability design", ["scalability", "performance", "capacity"]),
                Skill("sd-04", "High Availability & DR", "system-design", "advanced",
                      "HA/DR", ["availability", "disaster-recovery", "failover"]),
                Skill("sd-05", "Cost Optimization Design", "system-design", "medium",
                      "Cost optimization", ["cost", "optimization", "finops"]),
                Skill("sd-06", "API Design & Integration", "system-design", "medium",
                      "API design", ["api", "rest", "graphql", "integration"]),
                Skill("sd-07", "Observability Architecture", "system-design", "medium",
                      "Observability", ["observability", "monitoring", "tracing"]),
                Skill("sd-08", "Process Automation Analysis", "system-design", "medium",
                      "Process automation", ["automation", "process", "workflow", "optimization"]),
            ]
        },
        "devops": {
            "name": "DevOps Engineer",
            "focus": ["CI/CD", "Infrastructure", "Kubernetes", "Automation"],
            "automation_types": [AutomationType.INFRASTRUCTURE, AutomationType.RPA],
            "skills": [
                Skill("do-01", "CI/CD Pipeline Design", "devops", "medium",
                      "CI/CD pipelines", ["cicd", "pipeline", "github-actions"]),
                Skill("do-02", "Container Orchestration", "devops", "medium",
                      "Kubernetes", ["kubernetes", "k8s", "container", "helm"]),
                Skill("do-03", "Infrastructure as Code", "devops", "medium",
                      "IaC", ["terraform", "bicep", "iac", "infrastructure"]),
                Skill("do-04", "GitOps & Version Control", "devops", "basic",
                      "GitOps", ["git", "gitops", "flux", "argocd"]),
                Skill("do-05", "Environment Management", "devops", "medium",
                      "Environments", ["environment", "staging", "production"]),
                Skill("do-06", "Automated Testing", "devops", "medium",
                      "Testing automation", ["testing", "pytest", "integration"]),
                Skill("do-07", "Release Management", "devops", "medium",
                      "Release management", ["release", "deployment", "rollback"]),
                Skill("do-08", "Monitoring & Alerting", "devops", "medium",
                      "Monitoring", ["monitoring", "prometheus", "grafana", "alerting"]),
                Skill("do-09", "DevSecOps", "devops", "advanced",
                      "Security in DevOps", ["devsecops", "security", "scanning"]),
            ]
        },
        "finops": {
            "name": "FinOps Practitioner",
            "focus": ["Cost Management", "Optimization", "Budgets"],
            "automation_types": [],
            "skills": [
                Skill("fo-01", "Cost Visibility & Reporting", "finops", "basic",
                      "Cost visibility", ["cost", "reporting", "dashboard"]),
                Skill("fo-02", "Resource Tagging Strategy", "finops", "basic",
                      "Tagging", ["tagging", "governance", "policy"]),
                Skill("fo-03", "Budget Management & Alerts", "finops", "basic",
                      "Budgets", ["budget", "alert", "threshold"]),
                Skill("fo-04", "Reserved Instance Planning", "finops", "medium",
                      "RIs", ["reserved", "commitment", "savings"]),
                Skill("fo-05", "Spot Instance Optimization", "finops", "medium",
                      "Spot", ["spot", "preemptible", "interruptible"]),
                Skill("fo-06", "Storage Tiering", "finops", "medium",
                      "Storage optimization", ["storage", "tiering", "lifecycle"]),
                Skill("fo-07", "Compute Right-sizing", "finops", "medium",
                      "Right-sizing", ["rightsizing", "optimization", "advisor"]),
                Skill("fo-08", "Chargeback & Showback", "finops", "advanced",
                      "Cost allocation", ["chargeback", "showback", "allocation"]),
            ]
        },
    }

    def __init__(self):
        """Initialize role matcher."""
        self._build_keyword_index()

    def _build_keyword_index(self):
        """Build keyword to skill index for fast matching."""
        self.keyword_index: Dict[str, List[Tuple[str, Skill]]] = {}

        for role_id, role_data in self.ROLES.items():
            for skill in role_data.get("skills", []):
                for keyword in skill.keywords:
                    if keyword not in self.keyword_index:
                        self.keyword_index[keyword] = []
                    self.keyword_index[keyword].append((role_id, skill))

    def match_roles(
        self,
        analysis: ProcessAnalysis,
        strategy: Optional[object] = None
    ) -> TeamComposition:
        """
        Match process to optimal team composition.

        Args:
            analysis: Process analysis
            strategy: Optional automation strategy

        Returns:
            TeamComposition with role assignments
        """
        # Calculate affinity scores for each role
        role_scores = self._calculate_role_affinities(analysis)

        # Create role assignments
        assignments = []
        total_effort = 0

        # Sort roles by affinity
        sorted_roles = sorted(
            role_scores.items(),
            key=lambda x: x[1]["score"],
            reverse=True
        )

        # Assign primary role (highest affinity)
        primary_assigned = False

        for role_id, score_data in sorted_roles:
            if score_data["score"] < 20:
                continue

            # Determine effort based on affinity
            if not primary_assigned:
                effort = 40  # Primary role gets 40%
                is_primary = True
                primary_assigned = True
            else:
                effort = max(10, min(30, score_data["score"] / 3))
                is_primary = False

            total_effort += effort

            assignments.append(RoleAssignment(
                role=role_id,
                role_name=self.ROLES[role_id]["name"],
                affinity_score=score_data["score"],
                skills_required=score_data["skills"],
                responsibilities=score_data["responsibilities"],
                effort_percentage=effort,
                is_primary=is_primary
            ))

        # Normalize effort to 100%
        if total_effort > 0:
            for assignment in assignments:
                assignment.effort_percentage = round(
                    (assignment.effort_percentage / total_effort) * 100, 1
                )

        # Identify skill gaps
        skill_gaps = self._identify_skill_gaps(analysis, assignments)

        # Map cross-functional dependencies
        dependencies = self._map_dependencies(assignments)

        # Calculate team size
        team_size = self._calculate_team_size(analysis, assignments)

        return TeamComposition(
            assignments=assignments,
            skill_gaps=skill_gaps,
            cross_functional_dependencies=dependencies,
            recommended_team_size=team_size
        )

    def _calculate_role_affinities(
        self,
        analysis: ProcessAnalysis
    ) -> Dict[str, Dict]:
        """Calculate affinity scores for each role."""
        scores = {}

        for role_id, role_data in self.ROLES.items():
            score = 0
            matched_skills = []
            responsibilities = []

            # Check automation type match
            role_auto_types = role_data.get("automation_types", [])
            for auto_type in analysis.automation_types:
                if auto_type in role_auto_types:
                    score += 25
                    responsibilities.append(f"Implement {auto_type.value} automation")

            # Check keyword matches in process
            process_text = f"{analysis.name} {analysis.description}".lower()
            for step in analysis.steps:
                process_text += f" {step.name} {step.description}".lower()

            for skill in role_data.get("skills", []):
                for keyword in skill.keywords:
                    if keyword in process_text:
                        score += 10
                        if skill.id not in matched_skills:
                            matched_skills.append(skill.id)
                        break

            # Check data source relevance
            if role_id == "data-engineer" and analysis.data_sources_involved:
                score += 20
                responsibilities.append("Build data integration pipelines")

            # Check compliance relevance
            if role_id == "security-architect" and analysis.compliance_requirements:
                score += 30
                responsibilities.append("Ensure compliance requirements are met")

            # System design always involved for complex processes
            if role_id == "system-design":
                if analysis.complexity.value in ["complex", "enterprise"]:
                    score += 25
                    responsibilities.append("Design overall architecture")
                else:
                    score += 10
                    responsibilities.append("Review architecture decisions")

            # DevOps always needed for deployment
            if role_id == "devops":
                score += 15
                responsibilities.append("Set up CI/CD and deployment")

            # FinOps for cost tracking
            if role_id == "finops":
                score += 10
                responsibilities.append("Track and optimize costs")

            scores[role_id] = {
                "score": min(100, score),
                "skills": matched_skills[:5],  # Top 5 skills
                "responsibilities": responsibilities
            }

        return scores

    def _identify_skill_gaps(
        self,
        analysis: ProcessAnalysis,
        assignments: List[RoleAssignment]
    ) -> List[Dict]:
        """Identify potential skill gaps."""
        gaps = []

        # Get all matched skills
        matched_skills = set()
        for assignment in assignments:
            matched_skills.update(assignment.skills_required)

        # Check for common gaps based on automation types
        if AutomationType.AI_POWERED in analysis.automation_types:
            ai_skills = {"ai-01", "ai-04", "ai-07"}
            missing = ai_skills - matched_skills
            if missing:
                gaps.append({
                    "area": "AI/LLM",
                    "missing_skills": list(missing),
                    "recommendation": "Ensure AI Engineer covers prompt engineering and safety"
                })

        if AutomationType.ML_BASED in analysis.automation_types:
            ml_skills = {"ml-01", "ml-04", "ml-05"}
            missing = ml_skills - matched_skills
            if missing:
                gaps.append({
                    "area": "MLOps",
                    "missing_skills": list(missing),
                    "recommendation": "Include ML Engineer for model lifecycle management"
                })

        if analysis.compliance_requirements:
            sec_skills = {"sa-01", "sa-02"}
            missing = sec_skills - matched_skills
            if missing:
                gaps.append({
                    "area": "Security/Compliance",
                    "missing_skills": list(missing),
                    "recommendation": "Engage Security Architect for compliance validation"
                })

        return gaps

    def _map_dependencies(
        self,
        assignments: List[RoleAssignment]
    ) -> List[Dict]:
        """Map cross-functional dependencies."""
        dependencies = []

        role_ids = [a.role for a in assignments]

        # Common dependency patterns
        if "data-engineer" in role_ids and "ml-engineer" in role_ids:
            dependencies.append({
                "from": "data-engineer",
                "to": "ml-engineer",
                "type": "data",
                "description": "Feature pipelines and training data"
            })

        if "data-engineer" in role_ids and "ai-engineer" in role_ids:
            dependencies.append({
                "from": "data-engineer",
                "to": "ai-engineer",
                "type": "data",
                "description": "Document processing and embeddings"
            })

        if "ml-engineer" in role_ids and "devops" in role_ids:
            dependencies.append({
                "from": "ml-engineer",
                "to": "devops",
                "type": "deployment",
                "description": "Model serving infrastructure"
            })

        if "security-architect" in role_ids:
            dependencies.append({
                "from": "security-architect",
                "to": "all",
                "type": "review",
                "description": "Security review gates"
            })

        if "system-design" in role_ids:
            dependencies.append({
                "from": "system-design",
                "to": "all",
                "type": "architecture",
                "description": "Architecture guidance and ADRs"
            })

        return dependencies

    def _calculate_team_size(
        self,
        analysis: ProcessAnalysis,
        assignments: List[RoleAssignment]
    ) -> int:
        """Calculate recommended team size."""
        base_size = len([a for a in assignments if a.affinity_score >= 30])

        # Adjust for complexity
        complexity_adjustment = {
            "simple": 0,
            "moderate": 1,
            "complex": 2,
            "enterprise": 3
        }
        base_size += complexity_adjustment.get(analysis.complexity.value, 0)

        return max(2, min(8, base_size))

    def get_skill_details(self, skill_id: str) -> Optional[Skill]:
        """Get details for a specific skill."""
        for role_data in self.ROLES.values():
            for skill in role_data.get("skills", []):
                if skill.id == skill_id:
                    return skill
        return None

    def get_role_skills(self, role_id: str) -> List[Skill]:
        """Get all skills for a role."""
        if role_id in self.ROLES:
            return self.ROLES[role_id].get("skills", [])
        return []


# Example usage
if __name__ == "__main__":
    from process_analyzer import ProcessAnalyzer

    analyzer = ProcessAnalyzer()
    analysis = analyzer.analyze_process(
        name="Automated Customer Insights Report",
        description="Generate weekly insights from customer data using ML",
        steps=[
            {"name": "Extract CRM data", "time_minutes": 20, "data_sources": ["Salesforce"]},
            {"name": "Extract usage data", "time_minutes": 15, "data_sources": ["Product DB"]},
            {"name": "Run segmentation model", "time_minutes": 30, "requires_expertise": True},
            {"name": "Generate insights with LLM", "time_minutes": 20, "requires_expertise": True},
            {"name": "Create visualizations", "time_minutes": 25},
            {"name": "Distribute report", "time_minutes": 10}
        ],
        frequency="weekly",
        stakeholders=["Product", "Marketing", "Sales"],
        compliance_requirements=["GDPR"]
    )

    matcher = RoleMatcher()
    team = matcher.match_roles(analysis)

    print("=" * 60)
    print("TEAM COMPOSITION RECOMMENDATION")
    print("=" * 60)
    print(f"\nRecommended Team Size: {team.recommended_team_size}")

    print("\nRole Assignments:")
    for assignment in team.assignments:
        primary = " (PRIMARY)" if assignment.is_primary else ""
        print(f"\n  {assignment.role_name}{primary}")
        print(f"    Affinity Score: {assignment.affinity_score}%")
        print(f"    Effort: {assignment.effort_percentage}%")
        print(f"    Skills: {', '.join(assignment.skills_required)}")
        print(f"    Responsibilities:")
        for resp in assignment.responsibilities:
            print(f"      - {resp}")

    if team.skill_gaps:
        print("\nSkill Gaps Identified:")
        for gap in team.skill_gaps:
            print(f"  - {gap['area']}: {gap['recommendation']}")

    print("\nCross-Functional Dependencies:")
    for dep in team.cross_functional_dependencies:
        print(f"  - {dep['from']} → {dep['to']}: {dep['description']}")
