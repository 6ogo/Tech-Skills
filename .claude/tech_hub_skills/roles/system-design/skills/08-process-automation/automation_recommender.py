"""
Automation Recommender - Recommends optimal automation strategies.

Part of the Tech Hub Skills Library (sd-08: Process Automation).
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum

from process_analyzer import ProcessAnalysis, ProcessComplexity, AutomationType


class AutomationApproach(Enum):
    """High-level automation approaches."""
    BUILD = "build"           # Custom development
    BUY = "buy"               # Purchase existing solution
    CONFIGURE = "configure"   # Configure existing tools
    HYBRID = "hybrid"         # Mix of approaches


class RiskLevel(Enum):
    """Risk levels for automation initiatives."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class ToolRecommendation:
    """A recommended tool for automation."""
    name: str
    category: str
    fit_score: float  # 0-100
    pros: List[str]
    cons: List[str]
    azure_service: Optional[str] = None
    estimated_cost: str = "varies"
    learning_curve: str = "medium"


@dataclass
class AutomationStrategy:
    """Complete automation strategy recommendation."""
    primary_approach: AutomationApproach
    automation_types: List[AutomationType]
    recommended_tools: List[ToolRecommendation]
    implementation_phases: List[Dict]
    risk_assessment: Dict
    estimated_effort_weeks: float
    confidence_score: float  # 0-100

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "primary_approach": self.primary_approach.value,
            "automation_types": [t.value for t in self.automation_types],
            "recommended_tools": [
                {
                    "name": t.name,
                    "category": t.category,
                    "fit_score": t.fit_score,
                    "azure_service": t.azure_service
                }
                for t in self.recommended_tools
            ],
            "phases": self.implementation_phases,
            "risk_assessment": self.risk_assessment,
            "effort_weeks": self.estimated_effort_weeks,
            "confidence": self.confidence_score
        }


class AutomationRecommender:
    """
    Recommends optimal automation strategies based on process analysis.

    Evaluates multiple automation approaches and provides detailed
    recommendations including tools, patterns, and implementation guidance.
    """

    # Tool catalog by automation type
    TOOL_CATALOG = {
        AutomationType.RPA: [
            ToolRecommendation(
                name="Power Automate",
                category="RPA/Workflow",
                fit_score=85,
                pros=["Azure native", "Low-code", "Office 365 integration"],
                cons=["Limited for complex logic", "Licensing costs"],
                azure_service="Power Platform",
                estimated_cost="$15/user/month",
                learning_curve="low"
            ),
            ToolRecommendation(
                name="UiPath",
                category="RPA",
                fit_score=90,
                pros=["Enterprise-grade", "AI capabilities", "Large community"],
                cons=["Higher cost", "Steeper learning curve"],
                estimated_cost="$420/robot/month",
                learning_curve="medium"
            ),
        ],
        AutomationType.WORKFLOW: [
            ToolRecommendation(
                name="Azure Logic Apps",
                category="Workflow",
                fit_score=88,
                pros=["Azure native", "400+ connectors", "Serverless"],
                cons=["Consumption pricing can spike", "Limited debugging"],
                azure_service="Logic Apps",
                estimated_cost="Pay-per-execution",
                learning_curve="low"
            ),
            ToolRecommendation(
                name="Apache Airflow",
                category="Workflow Orchestration",
                fit_score=85,
                pros=["Open source", "Python-native", "Highly flexible"],
                cons=["Requires infrastructure", "Steeper learning curve"],
                azure_service="Azure Container Apps",
                estimated_cost="Infrastructure only",
                learning_curve="medium"
            ),
        ],
        AutomationType.DATA_PIPELINE: [
            ToolRecommendation(
                name="Azure Data Factory",
                category="Data Integration",
                fit_score=92,
                pros=["Azure native", "90+ connectors", "Mapping data flows"],
                cons=["Complex pricing", "Limited transformations"],
                azure_service="Data Factory",
                estimated_cost="Pay-per-activity",
                learning_curve="medium"
            ),
            ToolRecommendation(
                name="Azure Synapse Pipelines",
                category="Data Integration",
                fit_score=88,
                pros=["Unified analytics", "Spark integration", "Serverless SQL"],
                cons=["Overkill for simple ETL", "Higher cost"],
                azure_service="Synapse Analytics",
                estimated_cost="Varies by usage",
                learning_curve="medium"
            ),
            ToolRecommendation(
                name="dbt",
                category="Data Transformation",
                fit_score=85,
                pros=["SQL-first", "Version control", "Testing built-in"],
                cons=["Transformation only", "Requires warehouse"],
                azure_service="Azure Synapse/Databricks",
                estimated_cost="Free (open source)",
                learning_curve="low"
            ),
        ],
        AutomationType.ML_BASED: [
            ToolRecommendation(
                name="Azure Machine Learning",
                category="ML Platform",
                fit_score=90,
                pros=["Full MLOps", "AutoML", "Managed endpoints"],
                cons=["Complexity", "Cost at scale"],
                azure_service="Azure ML",
                estimated_cost="Compute-based",
                learning_curve="high"
            ),
            ToolRecommendation(
                name="MLflow",
                category="ML Lifecycle",
                fit_score=85,
                pros=["Open source", "Experiment tracking", "Model registry"],
                cons=["Requires hosting", "Basic UI"],
                azure_service="Azure ML (integrated)",
                estimated_cost="Free (open source)",
                learning_curve="medium"
            ),
        ],
        AutomationType.AI_POWERED: [
            ToolRecommendation(
                name="Azure OpenAI Service",
                category="LLM Platform",
                fit_score=95,
                pros=["GPT-4 access", "Enterprise security", "Azure integration"],
                cons=["Token costs", "Rate limits"],
                azure_service="Azure OpenAI",
                estimated_cost="$0.01-0.12/1K tokens",
                learning_curve="medium"
            ),
            ToolRecommendation(
                name="LangChain",
                category="LLM Framework",
                fit_score=82,
                pros=["Flexible", "Many integrations", "Active community"],
                cons=["Rapid changes", "Abstraction overhead"],
                estimated_cost="Free (open source)",
                learning_curve="medium"
            ),
            ToolRecommendation(
                name="Semantic Kernel",
                category="LLM Orchestration",
                fit_score=85,
                pros=["Microsoft backed", "C#/Python", "Azure native"],
                cons=["Newer ecosystem", "Less examples"],
                azure_service="Azure OpenAI",
                estimated_cost="Free (open source)",
                learning_curve="medium"
            ),
        ],
        AutomationType.INFRASTRUCTURE: [
            ToolRecommendation(
                name="Terraform",
                category="IaC",
                fit_score=92,
                pros=["Multi-cloud", "Large community", "State management"],
                cons=["HCL learning curve", "State file management"],
                azure_service="Any",
                estimated_cost="Free (open source)",
                learning_curve="medium"
            ),
            ToolRecommendation(
                name="Bicep",
                category="IaC",
                fit_score=88,
                pros=["Azure native", "ARM simplified", "VS Code support"],
                cons=["Azure only", "Smaller community"],
                azure_service="Azure Resource Manager",
                estimated_cost="Free",
                learning_curve="low"
            ),
        ],
        AutomationType.SECURITY: [
            ToolRecommendation(
                name="Microsoft Defender for Cloud",
                category="Security Posture",
                fit_score=90,
                pros=["Azure native", "CSPM/CWPP", "Compliance"],
                cons=["Cost at scale", "Alert fatigue"],
                azure_service="Defender for Cloud",
                estimated_cost="$15/server/month",
                learning_curve="medium"
            ),
            ToolRecommendation(
                name="Azure Policy",
                category="Governance",
                fit_score=88,
                pros=["Free", "Preventive controls", "Built-in policies"],
                cons=["Limited remediation", "Policy as code learning"],
                azure_service="Azure Policy",
                estimated_cost="Free",
                learning_curve="medium"
            ),
        ],
    }

    def __init__(self):
        """Initialize the recommender."""
        pass

    def recommend(
        self,
        analysis: ProcessAnalysis,
        budget_constraint: Optional[float] = None,
        timeline_weeks: Optional[int] = None,
        prefer_azure_native: bool = True
    ) -> AutomationStrategy:
        """
        Generate automation strategy recommendations.

        Args:
            analysis: Process analysis from ProcessAnalyzer
            budget_constraint: Maximum budget (optional)
            timeline_weeks: Target timeline in weeks (optional)
            prefer_azure_native: Prefer Azure-native solutions

        Returns:
            Complete AutomationStrategy recommendation
        """
        # Determine primary approach
        primary_approach = self._determine_approach(analysis, budget_constraint)

        # Get tool recommendations
        tools = self._recommend_tools(
            analysis.automation_types,
            prefer_azure_native
        )

        # Generate implementation phases
        phases = self._generate_phases(analysis, tools)

        # Assess risks
        risks = self._assess_risks(analysis)

        # Estimate effort
        effort = self._estimate_effort(analysis, primary_approach)

        # Calculate confidence
        confidence = self._calculate_confidence(analysis, tools)

        return AutomationStrategy(
            primary_approach=primary_approach,
            automation_types=analysis.automation_types,
            recommended_tools=tools,
            implementation_phases=phases,
            risk_assessment=risks,
            estimated_effort_weeks=effort,
            confidence_score=confidence
        )

    def _determine_approach(
        self,
        analysis: ProcessAnalysis,
        budget: Optional[float]
    ) -> AutomationApproach:
        """Determine build vs buy vs configure."""
        complexity = analysis.complexity

        if complexity == ProcessComplexity.SIMPLE:
            return AutomationApproach.CONFIGURE
        elif complexity == ProcessComplexity.MODERATE:
            if budget and budget < 50000:
                return AutomationApproach.CONFIGURE
            return AutomationApproach.HYBRID
        elif complexity == ProcessComplexity.COMPLEX:
            return AutomationApproach.HYBRID
        else:  # ENTERPRISE
            return AutomationApproach.BUILD

    def _recommend_tools(
        self,
        automation_types: List[AutomationType],
        prefer_azure: bool
    ) -> List[ToolRecommendation]:
        """Get tool recommendations for automation types."""
        tools = []
        seen_tools = set()

        for auto_type in automation_types:
            if auto_type in self.TOOL_CATALOG:
                for tool in self.TOOL_CATALOG[auto_type]:
                    if tool.name not in seen_tools:
                        # Boost Azure-native tools if preferred
                        if prefer_azure and tool.azure_service:
                            tool.fit_score = min(100, tool.fit_score + 5)
                        tools.append(tool)
                        seen_tools.add(tool.name)

        # Sort by fit score
        tools.sort(key=lambda t: t.fit_score, reverse=True)

        return tools[:8]  # Top 8 recommendations

    def _generate_phases(
        self,
        analysis: ProcessAnalysis,
        tools: List[ToolRecommendation]
    ) -> List[Dict]:
        """Generate implementation phases."""
        phases = []

        # Phase 1: Foundation
        phases.append({
            "phase": 1,
            "name": "Foundation & Setup",
            "duration_weeks": 1,
            "activities": [
                "Set up development environment",
                "Configure Azure resources",
                "Establish CI/CD pipeline",
                "Document current process baseline"
            ],
            "deliverables": [
                "Infrastructure provisioned",
                "Development environment ready",
                "Baseline metrics captured"
            ],
            "skills_needed": ["do-01", "do-03", "az-01"]
        })

        # Phase 2: Core Automation (varies by type)
        core_activities = []
        core_skills = []

        if AutomationType.DATA_PIPELINE in analysis.automation_types:
            core_activities.extend([
                "Build data extraction connectors",
                "Implement transformation logic",
                "Set up data quality checks"
            ])
            core_skills.extend(["de-02", "de-03"])

        if AutomationType.ML_BASED in analysis.automation_types:
            core_activities.extend([
                "Develop ML model",
                "Set up training pipeline",
                "Configure model serving"
            ])
            core_skills.extend(["ml-01", "ml-03", "ml-04"])

        if AutomationType.AI_POWERED in analysis.automation_types:
            core_activities.extend([
                "Design prompt templates",
                "Integrate LLM API",
                "Implement guardrails"
            ])
            core_skills.extend(["ai-01", "ai-04", "ai-07"])

        if AutomationType.WORKFLOW in analysis.automation_types:
            core_activities.extend([
                "Design workflow orchestration",
                "Implement business logic",
                "Configure triggers and schedules"
            ])
            core_skills.extend(["de-02", "do-01"])

        phases.append({
            "phase": 2,
            "name": "Core Automation Development",
            "duration_weeks": 2,
            "activities": core_activities or ["Implement automation logic"],
            "deliverables": [
                "Core automation components built",
                "Unit tests passing",
                "Integration points defined"
            ],
            "skills_needed": list(set(core_skills)) or ["de-02"]
        })

        # Phase 3: Integration & Testing
        phases.append({
            "phase": 3,
            "name": "Integration & Testing",
            "duration_weeks": 1,
            "activities": [
                "End-to-end integration testing",
                "Performance testing",
                "Security review",
                "User acceptance testing"
            ],
            "deliverables": [
                "All tests passing",
                "Security approval",
                "UAT sign-off"
            ],
            "skills_needed": ["do-06", "sa-05", "sd-03"]
        })

        # Phase 4: Deployment & Monitoring
        phases.append({
            "phase": 4,
            "name": "Deployment & Monitoring",
            "duration_weeks": 1,
            "activities": [
                "Deploy to production",
                "Configure monitoring and alerts",
                "Create runbooks",
                "Train users"
            ],
            "deliverables": [
                "Production deployment complete",
                "Monitoring dashboard live",
                "Documentation complete"
            ],
            "skills_needed": ["do-07", "do-08", "sd-07"]
        })

        return phases

    def _assess_risks(self, analysis: ProcessAnalysis) -> Dict:
        """Assess automation risks."""
        risks = {
            "overall_level": RiskLevel.LOW.value,
            "factors": [],
            "mitigations": []
        }

        # Complexity risk
        if analysis.complexity in [ProcessComplexity.COMPLEX, ProcessComplexity.ENTERPRISE]:
            risks["factors"].append({
                "risk": "High process complexity",
                "level": "high",
                "impact": "Implementation delays, cost overruns"
            })
            risks["mitigations"].append(
                "Break into smaller phases with clear milestones"
            )
            risks["overall_level"] = RiskLevel.MEDIUM.value

        # Data integration risk
        if len(analysis.data_sources_involved) > 3:
            risks["factors"].append({
                "risk": "Multiple data source integration",
                "level": "medium",
                "impact": "Integration complexity, data quality issues"
            })
            risks["mitigations"].append(
                "Implement robust data validation and monitoring"
            )

        # Stakeholder risk
        if len(analysis.stakeholders) > 4:
            risks["factors"].append({
                "risk": "Many stakeholders",
                "level": "medium",
                "impact": "Conflicting requirements, approval delays"
            })
            risks["mitigations"].append(
                "Establish clear RACI and regular stakeholder updates"
            )

        # Compliance risk
        if analysis.compliance_requirements:
            risks["factors"].append({
                "risk": "Compliance requirements",
                "level": "high",
                "impact": "Regulatory penalties, project blocks"
            })
            risks["mitigations"].append(
                "Engage Security Architect early, document compliance controls"
            )
            risks["overall_level"] = RiskLevel.HIGH.value

        # Change management risk
        if analysis.total_time_minutes > 120:
            risks["factors"].append({
                "risk": "Significant process change",
                "level": "medium",
                "impact": "User resistance, adoption challenges"
            })
            risks["mitigations"].append(
                "Develop change management plan with training"
            )

        return risks

    def _estimate_effort(
        self,
        analysis: ProcessAnalysis,
        approach: AutomationApproach
    ) -> float:
        """Estimate implementation effort in weeks."""
        base_effort = {
            ProcessComplexity.SIMPLE: 1,
            ProcessComplexity.MODERATE: 3,
            ProcessComplexity.COMPLEX: 6,
            ProcessComplexity.ENTERPRISE: 12
        }

        approach_multiplier = {
            AutomationApproach.CONFIGURE: 0.5,
            AutomationApproach.BUY: 0.75,
            AutomationApproach.HYBRID: 1.0,
            AutomationApproach.BUILD: 1.5
        }

        effort = base_effort.get(analysis.complexity, 4)
        effort *= approach_multiplier.get(approach, 1.0)

        # Add time for integrations
        effort += len(analysis.data_sources_involved) * 0.5

        # Add time for compliance
        if analysis.compliance_requirements:
            effort += 2

        return round(effort, 1)

    def _calculate_confidence(
        self,
        analysis: ProcessAnalysis,
        tools: List[ToolRecommendation]
    ) -> float:
        """Calculate confidence score for recommendations."""
        confidence = 70.0  # Base confidence

        # Higher automation score = higher confidence
        confidence += (analysis.automation_score - 50) * 0.3

        # More tool options = higher confidence
        if len(tools) >= 5:
            confidence += 10

        # Simpler processes = higher confidence
        complexity_adjustment = {
            ProcessComplexity.SIMPLE: 15,
            ProcessComplexity.MODERATE: 5,
            ProcessComplexity.COMPLEX: -5,
            ProcessComplexity.ENTERPRISE: -15
        }
        confidence += complexity_adjustment.get(analysis.complexity, 0)

        return max(0, min(100, round(confidence, 1)))

    def compare_approaches(
        self,
        analysis: ProcessAnalysis
    ) -> List[Dict]:
        """Compare different automation approaches."""
        approaches = []

        for approach in AutomationApproach:
            effort = self._estimate_effort(analysis, approach)

            cost_multiplier = {
                AutomationApproach.CONFIGURE: 0.3,
                AutomationApproach.BUY: 0.6,
                AutomationApproach.HYBRID: 1.0,
                AutomationApproach.BUILD: 1.5
            }

            flexibility_score = {
                AutomationApproach.CONFIGURE: 40,
                AutomationApproach.BUY: 50,
                AutomationApproach.HYBRID: 75,
                AutomationApproach.BUILD: 95
            }

            approaches.append({
                "approach": approach.value,
                "effort_weeks": effort,
                "relative_cost": cost_multiplier.get(approach, 1.0),
                "flexibility_score": flexibility_score.get(approach, 50),
                "best_for": self._get_approach_best_for(approach)
            })

        return approaches

    def _get_approach_best_for(self, approach: AutomationApproach) -> str:
        """Get description of when approach is best."""
        descriptions = {
            AutomationApproach.CONFIGURE: "Simple processes, tight timelines, limited budget",
            AutomationApproach.BUY: "Standard processes, quick deployment needed",
            AutomationApproach.HYBRID: "Most scenarios, balance of speed and flexibility",
            AutomationApproach.BUILD: "Unique requirements, competitive advantage, full control"
        }
        return descriptions.get(approach, "General use")


# Example usage
if __name__ == "__main__":
    from process_analyzer import ProcessAnalyzer

    # First analyze the process
    analyzer = ProcessAnalyzer()
    analysis = analyzer.analyze_process(
        name="Customer Onboarding",
        description="Onboard new enterprise customers",
        steps=[
            {"name": "Receive application", "time_minutes": 5, "manual": False},
            {"name": "Verify documents", "time_minutes": 45, "manual": True, "requires_expertise": True},
            {"name": "Credit check", "time_minutes": 30, "manual": True, "data_sources": ["Credit Bureau"]},
            {"name": "Risk assessment", "time_minutes": 60, "manual": True, "requires_decision": True},
            {"name": "Generate contract", "time_minutes": 20, "manual": True},
            {"name": "Send for signature", "time_minutes": 10, "manual": True},
            {"name": "Setup account", "time_minutes": 30, "manual": True, "tools_used": ["CRM", "ERP"]}
        ],
        frequency="daily",
        stakeholders=["Sales", "Risk", "Legal", "Operations"],
        compliance_requirements=["KYC", "AML"]
    )

    # Get recommendations
    recommender = AutomationRecommender()
    strategy = recommender.recommend(analysis, prefer_azure_native=True)

    print("=" * 60)
    print("AUTOMATION STRATEGY RECOMMENDATION")
    print("=" * 60)
    print(f"\nPrimary Approach: {strategy.primary_approach.value.upper()}")
    print(f"Estimated Effort: {strategy.estimated_effort_weeks} weeks")
    print(f"Confidence Score: {strategy.confidence_score}%")

    print(f"\nRecommended Tools:")
    for tool in strategy.recommended_tools[:5]:
        print(f"  - {tool.name} ({tool.category}): {tool.fit_score}% fit")
        if tool.azure_service:
            print(f"    Azure: {tool.azure_service}")

    print(f"\nImplementation Phases:")
    for phase in strategy.implementation_phases:
        print(f"  Phase {phase['phase']}: {phase['name']} ({phase['duration_weeks']}w)")

    print(f"\nRisk Assessment: {strategy.risk_assessment['overall_level'].upper()}")
    for risk in strategy.risk_assessment['factors']:
        print(f"  - {risk['risk']} ({risk['level']})")
