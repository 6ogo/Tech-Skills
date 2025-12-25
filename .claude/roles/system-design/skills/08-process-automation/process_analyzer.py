"""
Process Analyzer - Analyzes work processes for automation opportunities.

Part of the Tech Hub Skills Library (sd-08: Process Automation).
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
import json


class ProcessComplexity(Enum):
    """Process complexity classification."""
    SIMPLE = "simple"           # Linear, few decisions, single system
    MODERATE = "moderate"       # Some branching, multiple sources
    COMPLEX = "complex"         # Many decisions, unstructured data, ML needed
    ENTERPRISE = "enterprise"   # Cross-departmental, compliance, legacy


class AutomationType(Enum):
    """Types of automation approaches."""
    RPA = "rpa"                         # Robotic Process Automation
    WORKFLOW = "workflow"               # Workflow/orchestration
    DATA_PIPELINE = "data_pipeline"     # ETL/ELT automation
    ML_BASED = "ml_based"               # Machine learning automation
    AI_POWERED = "ai_powered"           # LLM/GenAI automation
    INFRASTRUCTURE = "infrastructure"   # IaC/DevOps automation
    SECURITY = "security"               # Security/compliance automation
    HYBRID = "hybrid"                   # Multiple approaches combined


@dataclass
class ProcessStep:
    """Represents a single step in a process."""
    name: str
    description: str = ""
    time_minutes: float = 0.0
    is_manual: bool = True
    requires_decision: bool = False
    requires_expertise: bool = False
    error_prone: bool = False
    data_sources: List[str] = field(default_factory=list)
    tools_used: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)

    @property
    def automation_difficulty(self) -> float:
        """Calculate automation difficulty score (0-1, higher = harder)."""
        difficulty = 0.0
        if self.requires_decision:
            difficulty += 0.3
        if self.requires_expertise:
            difficulty += 0.3
        if len(self.data_sources) > 2:
            difficulty += 0.2
        if len(self.dependencies) > 2:
            difficulty += 0.2
        return min(difficulty, 1.0)


@dataclass
class ProcessAnalysis:
    """Complete analysis of a work process."""
    name: str
    description: str
    steps: List[ProcessStep]
    frequency: str  # daily, weekly, monthly, quarterly, ad-hoc
    stakeholders: List[str]

    # Calculated fields
    total_time_minutes: float = 0.0
    automation_score: float = 0.0
    complexity: ProcessComplexity = ProcessComplexity.SIMPLE
    bottlenecks: List[str] = field(default_factory=list)
    automation_types: List[AutomationType] = field(default_factory=list)

    # Metadata
    data_sources_involved: List[str] = field(default_factory=list)
    systems_involved: List[str] = field(default_factory=list)
    compliance_requirements: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert analysis to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "frequency": self.frequency,
            "stakeholders": self.stakeholders,
            "total_time_minutes": self.total_time_minutes,
            "automation_score": self.automation_score,
            "complexity": self.complexity.value,
            "bottlenecks": self.bottlenecks,
            "automation_types": [t.value for t in self.automation_types],
            "steps": [
                {
                    "name": s.name,
                    "time_minutes": s.time_minutes,
                    "is_manual": s.is_manual,
                    "automation_difficulty": s.automation_difficulty
                }
                for s in self.steps
            ]
        }

    def to_json(self) -> str:
        """Convert analysis to JSON string."""
        return json.dumps(self.to_dict(), indent=2)


class ProcessAnalyzer:
    """
    Analyzes work processes to identify automation opportunities.

    This is the core analysis engine that examines process characteristics,
    calculates automation potential, and identifies bottlenecks.
    """

    # Frequency multipliers for ROI calculation
    FREQUENCY_MULTIPLIERS = {
        "hourly": 2080,      # Per year
        "daily": 260,
        "weekly": 52,
        "bi-weekly": 26,
        "monthly": 12,
        "quarterly": 4,
        "annually": 1,
        "ad-hoc": 10         # Estimated
    }

    def __init__(self):
        """Initialize the process analyzer."""
        self.analysis_history: List[ProcessAnalysis] = []

    def analyze_process(
        self,
        name: str,
        description: str,
        steps: List[Dict],
        frequency: str = "weekly",
        stakeholders: Optional[List[str]] = None,
        compliance_requirements: Optional[List[str]] = None
    ) -> ProcessAnalysis:
        """
        Analyze a work process for automation opportunities.

        Args:
            name: Process name
            description: Process description
            steps: List of process steps with properties
            frequency: How often the process runs
            stakeholders: List of stakeholders
            compliance_requirements: Any compliance needs

        Returns:
            ProcessAnalysis object with complete analysis
        """
        # Convert step dictionaries to ProcessStep objects
        process_steps = [
            ProcessStep(
                name=s.get("name", f"Step {i+1}"),
                description=s.get("description", ""),
                time_minutes=s.get("time_minutes", 0),
                is_manual=s.get("manual", s.get("is_manual", True)),
                requires_decision=s.get("requires_decision", False),
                requires_expertise=s.get("requires_expertise", False),
                error_prone=s.get("error_prone", False),
                data_sources=s.get("data_sources", []),
                tools_used=s.get("tools_used", []),
                dependencies=s.get("dependencies", [])
            )
            for i, s in enumerate(steps)
        ]

        # Create initial analysis
        analysis = ProcessAnalysis(
            name=name,
            description=description,
            steps=process_steps,
            frequency=frequency,
            stakeholders=stakeholders or [],
            compliance_requirements=compliance_requirements or []
        )

        # Calculate total time
        analysis.total_time_minutes = sum(s.time_minutes for s in process_steps)

        # Collect all data sources and systems
        analysis.data_sources_involved = list(set(
            source
            for step in process_steps
            for source in step.data_sources
        ))
        analysis.systems_involved = list(set(
            tool
            for step in process_steps
            for tool in step.tools_used
        ))

        # Calculate automation score
        analysis.automation_score = self._calculate_automation_score(process_steps)

        # Determine complexity
        analysis.complexity = self._determine_complexity(analysis)

        # Identify bottlenecks
        analysis.bottlenecks = self._identify_bottlenecks(process_steps)

        # Recommend automation types
        analysis.automation_types = self._recommend_automation_types(analysis)

        # Store in history
        self.analysis_history.append(analysis)

        return analysis

    def _calculate_automation_score(self, steps: List[ProcessStep]) -> float:
        """
        Calculate automation potential score (0-100).

        Higher score = easier to automate with higher potential value.
        """
        if not steps:
            return 0.0

        # Base score from manual steps (more manual = more opportunity)
        manual_ratio = sum(1 for s in steps if s.is_manual) / len(steps)
        base_score = manual_ratio * 40  # Up to 40 points

        # Time-based score (more time = more value in automating)
        total_time = sum(s.time_minutes for s in steps)
        time_score = min(total_time / 60, 1.0) * 20  # Up to 20 points for 1+ hour

        # Difficulty penalty
        avg_difficulty = sum(s.automation_difficulty for s in steps) / len(steps)
        difficulty_penalty = avg_difficulty * 30  # Up to 30 points penalty

        # Repetitiveness bonus (more steps = likely more repetitive)
        repetition_score = min(len(steps) / 10, 1.0) * 20  # Up to 20 points

        # Error-prone bonus (high value in automating error-prone steps)
        error_prone_ratio = sum(1 for s in steps if s.error_prone) / len(steps)
        error_score = error_prone_ratio * 20  # Up to 20 points

        final_score = base_score + time_score - difficulty_penalty + repetition_score + error_score
        return max(0, min(100, final_score))

    def _determine_complexity(self, analysis: ProcessAnalysis) -> ProcessComplexity:
        """Determine process complexity level."""
        steps = analysis.steps

        # Count complexity factors
        decision_count = sum(1 for s in steps if s.requires_decision)
        expertise_count = sum(1 for s in steps if s.requires_expertise)
        data_source_count = len(analysis.data_sources_involved)
        system_count = len(analysis.systems_involved)
        has_compliance = len(analysis.compliance_requirements) > 0

        # Calculate complexity score
        complexity_score = (
            decision_count * 2 +
            expertise_count * 3 +
            data_source_count +
            system_count +
            (5 if has_compliance else 0)
        )

        # Map to complexity level
        if complexity_score <= 5:
            return ProcessComplexity.SIMPLE
        elif complexity_score <= 12:
            return ProcessComplexity.MODERATE
        elif complexity_score <= 20:
            return ProcessComplexity.COMPLEX
        else:
            return ProcessComplexity.ENTERPRISE

    def _identify_bottlenecks(self, steps: List[ProcessStep]) -> List[str]:
        """Identify bottleneck steps in the process."""
        if not steps:
            return []

        bottlenecks = []
        avg_time = sum(s.time_minutes for s in steps) / len(steps)

        for step in steps:
            reasons = []

            # Time-based bottleneck
            if step.time_minutes > avg_time * 1.5:
                reasons.append("high time consumption")

            # Dependency bottleneck
            if len(step.dependencies) >= 3:
                reasons.append("multiple dependencies")

            # Expertise bottleneck
            if step.requires_expertise and step.is_manual:
                reasons.append("requires specialized expertise")

            # Error-prone bottleneck
            if step.error_prone:
                reasons.append("error-prone")

            if reasons:
                bottlenecks.append(f"{step.name}: {', '.join(reasons)}")

        return bottlenecks

    def _recommend_automation_types(
        self,
        analysis: ProcessAnalysis
    ) -> List[AutomationType]:
        """Recommend suitable automation types based on analysis."""
        types = []
        steps = analysis.steps

        # Check for data-centric patterns
        if analysis.data_sources_involved:
            types.append(AutomationType.DATA_PIPELINE)

        # Check for repetitive, rule-based patterns
        simple_manual = sum(
            1 for s in steps
            if s.is_manual and not s.requires_decision and not s.requires_expertise
        )
        if simple_manual > len(steps) * 0.5:
            types.append(AutomationType.RPA)

        # Check for workflow patterns
        if len(steps) >= 5 and len(analysis.stakeholders) > 1:
            types.append(AutomationType.WORKFLOW)

        # Check for ML patterns
        decision_heavy = sum(1 for s in steps if s.requires_decision)
        if decision_heavy > len(steps) * 0.3:
            types.append(AutomationType.ML_BASED)

        # Check for AI patterns (content, reasoning, NLP)
        content_keywords = ["write", "generate", "summarize", "analyze", "review"]
        has_content_steps = any(
            any(kw in s.name.lower() or kw in s.description.lower() for kw in content_keywords)
            for s in steps
        )
        if has_content_steps:
            types.append(AutomationType.AI_POWERED)

        # Check for infrastructure patterns
        infra_keywords = ["deploy", "provision", "scale", "monitor", "backup"]
        has_infra_steps = any(
            any(kw in s.name.lower() or kw in s.description.lower() for kw in infra_keywords)
            for s in steps
        )
        if has_infra_steps:
            types.append(AutomationType.INFRASTRUCTURE)

        # Check for security patterns
        if analysis.compliance_requirements:
            types.append(AutomationType.SECURITY)

        # If multiple types, mark as hybrid
        if len(types) >= 3:
            types.append(AutomationType.HYBRID)

        return list(set(types))  # Remove duplicates

    def calculate_roi(
        self,
        analysis: ProcessAnalysis,
        hourly_cost: float = 75.0,
        automation_cost: float = 10000.0,
        automation_reduction_pct: float = 0.80
    ) -> Dict:
        """
        Calculate ROI for automating a process.

        Args:
            analysis: Process analysis
            hourly_cost: Cost per hour of manual work
            automation_cost: One-time automation implementation cost
            automation_reduction_pct: Expected time reduction (0-1)

        Returns:
            ROI calculation dictionary
        """
        frequency_multiplier = self.FREQUENCY_MULTIPLIERS.get(
            analysis.frequency, 12
        )

        # Current annual cost
        hours_per_execution = analysis.total_time_minutes / 60
        annual_manual_cost = hours_per_execution * hourly_cost * frequency_multiplier

        # Post-automation annual cost
        automated_hours = hours_per_execution * (1 - automation_reduction_pct)
        annual_automated_cost = automated_hours * hourly_cost * frequency_multiplier

        # Savings and ROI
        annual_savings = annual_manual_cost - annual_automated_cost
        roi_year_1 = ((annual_savings - automation_cost) / automation_cost) * 100
        payback_months = (automation_cost / (annual_savings / 12)) if annual_savings > 0 else float('inf')

        return {
            "current_annual_cost": round(annual_manual_cost, 2),
            "automated_annual_cost": round(annual_automated_cost, 2),
            "annual_savings": round(annual_savings, 2),
            "implementation_cost": automation_cost,
            "roi_year_1_percent": round(roi_year_1, 1),
            "payback_months": round(payback_months, 1),
            "break_even_executions": round(automation_cost / (hours_per_execution * hourly_cost * automation_reduction_pct), 0)
        }

    def compare_processes(
        self,
        analyses: List[ProcessAnalysis]
    ) -> List[Dict]:
        """
        Compare multiple processes for automation prioritization.

        Returns processes ranked by automation potential and ROI.
        """
        rankings = []

        for analysis in analyses:
            roi = self.calculate_roi(analysis)

            # Priority score combines automation score and ROI
            priority_score = (
                analysis.automation_score * 0.4 +
                min(roi["roi_year_1_percent"] / 10, 60) +  # Cap ROI contribution
                (100 - roi["payback_months"] * 2) * 0.2   # Faster payback = higher priority
            )

            rankings.append({
                "name": analysis.name,
                "automation_score": analysis.automation_score,
                "complexity": analysis.complexity.value,
                "roi_year_1_percent": roi["roi_year_1_percent"],
                "payback_months": roi["payback_months"],
                "priority_score": round(max(0, priority_score), 1)
            })

        # Sort by priority score
        rankings.sort(key=lambda x: x["priority_score"], reverse=True)

        return rankings


# Example usage
if __name__ == "__main__":
    analyzer = ProcessAnalyzer()

    # Example: Monthly report generation process
    analysis = analyzer.analyze_process(
        name="Monthly Sales Report Generation",
        description="Generate and distribute monthly sales performance reports",
        steps=[
            {
                "name": "Extract data from CRM",
                "time_minutes": 30,
                "manual": True,
                "data_sources": ["Salesforce"],
                "tools_used": ["Excel"]
            },
            {
                "name": "Extract data from ERP",
                "time_minutes": 45,
                "manual": True,
                "data_sources": ["SAP"],
                "tools_used": ["Excel"]
            },
            {
                "name": "Merge and clean data",
                "time_minutes": 60,
                "manual": True,
                "error_prone": True
            },
            {
                "name": "Calculate KPIs",
                "time_minutes": 30,
                "manual": True,
                "requires_expertise": True
            },
            {
                "name": "Generate visualizations",
                "time_minutes": 45,
                "manual": True,
                "tools_used": ["Power BI"]
            },
            {
                "name": "Write executive summary",
                "time_minutes": 60,
                "manual": True,
                "requires_decision": True,
                "requires_expertise": True
            },
            {
                "name": "Review and distribute",
                "time_minutes": 30,
                "manual": True
            }
        ],
        frequency="monthly",
        stakeholders=["Sales Director", "CFO", "Regional Managers"]
    )

    print("=" * 60)
    print("PROCESS ANALYSIS REPORT")
    print("=" * 60)
    print(f"\nProcess: {analysis.name}")
    print(f"Total Time: {analysis.total_time_minutes} minutes")
    print(f"Automation Score: {analysis.automation_score:.1f}/100")
    print(f"Complexity: {analysis.complexity.value.upper()}")
    print(f"\nRecommended Automation Types:")
    for at in analysis.automation_types:
        print(f"  - {at.value}")
    print(f"\nBottlenecks Identified:")
    for bn in analysis.bottlenecks:
        print(f"  - {bn}")

    # Calculate ROI
    roi = analyzer.calculate_roi(analysis)
    print(f"\nROI Analysis:")
    print(f"  Current Annual Cost: ${roi['current_annual_cost']:,.2f}")
    print(f"  Automated Annual Cost: ${roi['automated_annual_cost']:,.2f}")
    print(f"  Annual Savings: ${roi['annual_savings']:,.2f}")
    print(f"  Year 1 ROI: {roi['roi_year_1_percent']}%")
    print(f"  Payback Period: {roi['payback_months']} months")
