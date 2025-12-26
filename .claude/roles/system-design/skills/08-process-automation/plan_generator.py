"""
Plan Generator - Generates comprehensive automation implementation plans.

Part of the Tech Hub Skills Library (sd-08: Process Automation).
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import json

from process_analyzer import ProcessAnalysis, ProcessComplexity
from automation_recommender import AutomationStrategy, AutomationApproach
from role_matcher import TeamComposition, RoleAssignment


@dataclass
class Milestone:
    """A project milestone."""
    name: str
    phase: int
    deliverables: List[str]
    success_criteria: List[str]
    dependencies: List[str] = field(default_factory=list)


@dataclass
class RiskMitigation:
    """Risk mitigation strategy."""
    risk: str
    probability: str  # low, medium, high
    impact: str       # low, medium, high
    mitigation: str
    owner: str
    contingency: str


@dataclass
class AutomationPlan:
    """Complete automation implementation plan."""
    # Header
    name: str
    version: str
    created_date: str

    # Summary
    executive_summary: Dict

    # Analysis
    process_analysis: Dict
    automation_strategy: Dict
    team_composition: Dict

    # Implementation
    phases: List[Dict]
    milestones: List[Milestone]

    # Risk & Governance
    risks: List[RiskMitigation]
    success_metrics: List[Dict]
    governance: Dict

    # Documentation
    adr_template: str
    prd_outline: str
    technical_spec_outline: str

    def to_markdown(self) -> str:
        """Convert plan to markdown document."""
        md = []

        # Title
        md.append(f"# Automation Plan: {self.name}")
        md.append(f"\n**Version**: {self.version}")
        md.append(f"**Created**: {self.created_date}")
        md.append("")

        # Executive Summary
        md.append("## Executive Summary")
        md.append("")
        summary = self.executive_summary
        md.append(f"- **Automation Potential**: {summary.get('automation_score', 'N/A')}/100")
        md.append(f"- **Complexity**: {summary.get('complexity', 'N/A')}")
        md.append(f"- **Estimated Effort**: {summary.get('effort_weeks', 'N/A')} weeks")
        md.append(f"- **Primary Approach**: {summary.get('approach', 'N/A')}")
        md.append(f"- **Confidence**: {summary.get('confidence', 'N/A')}%")
        md.append("")

        # Current State
        md.append("## Current State Analysis")
        md.append("")
        analysis = self.process_analysis
        md.append(f"**Process**: {analysis.get('name', 'N/A')}")
        md.append(f"\n{analysis.get('description', '')}")
        md.append("")
        md.append(f"- **Frequency**: {analysis.get('frequency', 'N/A')}")
        md.append(f"- **Total Time**: {analysis.get('total_time_minutes', 0)} minutes")
        md.append(f"- **Stakeholders**: {', '.join(analysis.get('stakeholders', []))}")
        md.append("")

        # Bottlenecks
        if analysis.get('bottlenecks'):
            md.append("### Identified Bottlenecks")
            for bn in analysis.get('bottlenecks', []):
                md.append(f"- {bn}")
            md.append("")

        # Team Composition
        md.append("## Recommended Team")
        md.append("")
        md.append("| Role | Effort | Key Skills | Primary |")
        md.append("|------|--------|------------|---------|")
        for assignment in self.team_composition.get('assignments', []):
            skills = ', '.join(assignment.get('skills', [])[:3])
            primary = "Yes" if assignment.get('is_primary') else ""
            md.append(f"| {assignment.get('role_name', '')} | {assignment.get('effort_pct', 0)}% | {skills} | {primary} |")
        md.append("")

        # Skill Gaps
        if self.team_composition.get('skill_gaps'):
            md.append("### Skill Gaps")
            for gap in self.team_composition.get('skill_gaps', []):
                md.append(f"- **{gap.get('area', '')}**: {gap.get('recommendation', '')}")
            md.append("")

        # Recommended Tools
        md.append("## Recommended Tools & Technologies")
        md.append("")
        strategy = self.automation_strategy
        md.append("| Tool | Category | Fit Score | Azure Service |")
        md.append("|------|----------|-----------|---------------|")
        for tool in strategy.get('recommended_tools', [])[:6]:
            azure = tool.get('azure_service', '-')
            md.append(f"| {tool.get('name', '')} | {tool.get('category', '')} | {tool.get('fit_score', 0)}% | {azure} |")
        md.append("")

        # Implementation Phases
        md.append("## Implementation Phases")
        md.append("")
        for phase in self.phases:
            md.append(f"### Phase {phase.get('phase', '')}: {phase.get('name', '')}")
            md.append(f"**Duration**: {phase.get('duration_weeks', '')} weeks")
            md.append("")
            md.append("**Activities**:")
            for activity in phase.get('activities', []):
                md.append(f"- {activity}")
            md.append("")
            md.append("**Deliverables**:")
            for deliverable in phase.get('deliverables', []):
                md.append(f"- {deliverable}")
            md.append("")
            md.append(f"**Skills Needed**: {', '.join(phase.get('skills_needed', []))}")
            md.append("")

        # Milestones
        md.append("## Key Milestones")
        md.append("")
        md.append("| Milestone | Phase | Deliverables | Success Criteria |")
        md.append("|-----------|-------|--------------|------------------|")
        for milestone in self.milestones:
            deliverables = "; ".join(milestone.deliverables[:2])
            criteria = "; ".join(milestone.success_criteria[:2])
            md.append(f"| {milestone.name} | {milestone.phase} | {deliverables} | {criteria} |")
        md.append("")

        # Risk Assessment
        md.append("## Risk Assessment")
        md.append("")
        md.append("| Risk | Probability | Impact | Mitigation | Owner |")
        md.append("|------|-------------|--------|------------|-------|")
        for risk in self.risks:
            md.append(f"| {risk.risk} | {risk.probability} | {risk.impact} | {risk.mitigation} | {risk.owner} |")
        md.append("")

        # Success Metrics
        md.append("## Success Metrics")
        md.append("")
        md.append("| Metric | Current | Target | Measurement |")
        md.append("|--------|---------|--------|-------------|")
        for metric in self.success_metrics:
            md.append(f"| {metric.get('name', '')} | {metric.get('current', '-')} | {metric.get('target', '')} | {metric.get('measurement', '')} |")
        md.append("")

        # Governance
        md.append("## Governance")
        md.append("")
        gov = self.governance
        md.append(f"- **Review Cadence**: {gov.get('review_cadence', 'Weekly')}")
        md.append(f"- **Escalation Path**: {gov.get('escalation_path', 'Project Lead → Manager → Director')}")
        md.append(f"- **Change Control**: {gov.get('change_control', 'ADR for significant changes')}")
        md.append("")

        # ADR Template
        md.append("## Appendix A: Architecture Decision Record Template")
        md.append("")
        md.append("```markdown")
        md.append(self.adr_template)
        md.append("```")
        md.append("")

        # PRD Outline
        md.append("## Appendix B: PRD Outline")
        md.append("")
        md.append(self.prd_outline)
        md.append("")

        return "\n".join(md)

    def to_dict(self) -> Dict:
        """Convert plan to dictionary."""
        return {
            "name": self.name,
            "version": self.version,
            "created_date": self.created_date,
            "executive_summary": self.executive_summary,
            "process_analysis": self.process_analysis,
            "automation_strategy": self.automation_strategy,
            "team_composition": self.team_composition,
            "phases": self.phases,
            "milestones": [
                {
                    "name": m.name,
                    "phase": m.phase,
                    "deliverables": m.deliverables,
                    "success_criteria": m.success_criteria
                }
                for m in self.milestones
            ],
            "risks": [
                {
                    "risk": r.risk,
                    "probability": r.probability,
                    "impact": r.impact,
                    "mitigation": r.mitigation,
                    "owner": r.owner
                }
                for r in self.risks
            ],
            "success_metrics": self.success_metrics,
            "governance": self.governance
        }

    def to_json(self) -> str:
        """Convert plan to JSON."""
        return json.dumps(self.to_dict(), indent=2)


class PlanGenerator:
    """
    Generates comprehensive automation implementation plans.

    Combines process analysis, automation strategy, and team composition
    into actionable implementation plans with documentation templates.
    """

    def __init__(self):
        """Initialize plan generator."""
        self.version = "1.0"

    def generate_plan(
        self,
        analysis: ProcessAnalysis,
        recommendations: AutomationStrategy,
        team_composition: TeamComposition,
        project_name: Optional[str] = None
    ) -> AutomationPlan:
        """
        Generate complete automation implementation plan.

        Args:
            analysis: Process analysis
            recommendations: Automation strategy
            team_composition: Team composition

        Returns:
            Complete AutomationPlan
        """
        name = project_name or f"{analysis.name} Automation"

        # Build executive summary
        executive_summary = {
            "automation_score": round(analysis.automation_score, 1),
            "complexity": analysis.complexity.value,
            "effort_weeks": recommendations.estimated_effort_weeks,
            "approach": recommendations.primary_approach.value,
            "confidence": recommendations.confidence_score,
            "roi_potential": "High" if analysis.automation_score > 70 else "Medium"
        }

        # Convert analysis to dict
        process_analysis = analysis.to_dict()

        # Convert strategy to dict
        automation_strategy = recommendations.to_dict()

        # Convert team to dict
        team_dict = team_composition.to_dict()

        # Generate milestones
        milestones = self._generate_milestones(recommendations.implementation_phases)

        # Generate risks
        risks = self._generate_risks(analysis, recommendations, team_composition)

        # Generate success metrics
        success_metrics = self._generate_metrics(analysis)

        # Generate governance
        governance = self._generate_governance(analysis)

        # Generate documentation templates
        adr_template = self._generate_adr_template(name)
        prd_outline = self._generate_prd_outline(analysis)
        tech_spec = self._generate_tech_spec_outline(analysis, recommendations)

        return AutomationPlan(
            name=name,
            version=self.version,
            created_date=datetime.now().strftime("%Y-%m-%d"),
            executive_summary=executive_summary,
            process_analysis=process_analysis,
            automation_strategy=automation_strategy,
            team_composition=team_dict,
            phases=recommendations.implementation_phases,
            milestones=milestones,
            risks=risks,
            success_metrics=success_metrics,
            governance=governance,
            adr_template=adr_template,
            prd_outline=prd_outline,
            technical_spec_outline=tech_spec
        )

    def _generate_milestones(self, phases: List[Dict]) -> List[Milestone]:
        """Generate milestones from phases."""
        milestones = []

        for phase in phases:
            phase_num = phase.get('phase', 0)
            phase_name = phase.get('name', f'Phase {phase_num}')

            milestones.append(Milestone(
                name=f"M{phase_num}: {phase_name} Complete",
                phase=phase_num,
                deliverables=phase.get('deliverables', []),
                success_criteria=[
                    f"All {phase_name.lower()} activities completed",
                    "Stakeholder sign-off obtained",
                    "Documentation updated"
                ],
                dependencies=[f"M{phase_num - 1}"] if phase_num > 1 else []
            ))

        # Add final milestone
        milestones.append(Milestone(
            name="Project Complete",
            phase=len(phases) + 1,
            deliverables=[
                "Production deployment",
                "User training complete",
                "Runbooks delivered"
            ],
            success_criteria=[
                "All success metrics achieved",
                "No critical issues open",
                "Handover to operations complete"
            ],
            dependencies=[f"M{len(phases)}"]
        ))

        return milestones

    def _generate_risks(
        self,
        analysis: ProcessAnalysis,
        strategy: AutomationStrategy,
        team: TeamComposition
    ) -> List[RiskMitigation]:
        """Generate risk register."""
        risks = []

        # Technical risks
        if analysis.complexity in [ProcessComplexity.COMPLEX, ProcessComplexity.ENTERPRISE]:
            risks.append(RiskMitigation(
                risk="Technical complexity exceeds estimates",
                probability="medium",
                impact="high",
                mitigation="Break into smaller increments, add technical spikes",
                owner="Tech Lead",
                contingency="Descope non-essential features"
            ))

        # Integration risks
        if len(analysis.data_sources_involved) > 2:
            risks.append(RiskMitigation(
                risk="Data integration issues",
                probability="medium",
                impact="medium",
                mitigation="Early integration testing, mock services",
                owner="Data Engineer",
                contingency="Manual data entry fallback"
            ))

        # Resource risks
        if team.recommended_team_size > 4:
            risks.append(RiskMitigation(
                risk="Resource availability constraints",
                probability="medium",
                impact="high",
                mitigation="Identify backup resources, cross-training",
                owner="Project Manager",
                contingency="Extend timeline, prioritize features"
            ))

        # Skill gap risks
        if team.skill_gaps:
            risks.append(RiskMitigation(
                risk="Team skill gaps",
                probability="low",
                impact="medium",
                mitigation="Training plan, expert consultation",
                owner="Tech Lead",
                contingency="External contractor support"
            ))

        # Adoption risks
        risks.append(RiskMitigation(
            risk="User adoption resistance",
            probability="medium",
            impact="medium",
            mitigation="Early stakeholder engagement, training program",
            owner="Product Owner",
            contingency="Phased rollout, additional change management"
        ))

        # Security/Compliance risks
        if analysis.compliance_requirements:
            risks.append(RiskMitigation(
                risk="Compliance requirements not met",
                probability="low",
                impact="critical",
                mitigation="Security review gates, compliance checklist",
                owner="Security Architect",
                contingency="Halt deployment until resolved"
            ))

        return risks

    def _generate_metrics(self, analysis: ProcessAnalysis) -> List[Dict]:
        """Generate success metrics."""
        metrics = [
            {
                "name": "Process Time Reduction",
                "current": f"{analysis.total_time_minutes} min",
                "target": f"<{int(analysis.total_time_minutes * 0.2)} min",
                "measurement": "Time from start to completion"
            },
            {
                "name": "Manual Effort",
                "current": "100%",
                "target": "<20%",
                "measurement": "Human intervention required"
            },
            {
                "name": "Error Rate",
                "current": "Unknown",
                "target": "<5%",
                "measurement": "Errors per 100 executions"
            },
            {
                "name": "Automation Reliability",
                "current": "N/A",
                "target": ">99%",
                "measurement": "Successful runs / Total runs"
            }
        ]

        # Add stakeholder-specific metrics
        if "Finance" in analysis.stakeholders or "CFO" in str(analysis.stakeholders):
            metrics.append({
                "name": "Cost Savings",
                "current": "Baseline",
                "target": ">$50K/year",
                "measurement": "Reduced labor + efficiency gains"
            })

        if "Customer" in str(analysis.stakeholders).lower():
            metrics.append({
                "name": "Customer Impact",
                "current": "Baseline",
                "target": "NPS +5",
                "measurement": "Customer satisfaction surveys"
            })

        return metrics

    def _generate_governance(self, analysis: ProcessAnalysis) -> Dict:
        """Generate governance structure."""
        # More governance for complex processes
        if analysis.complexity == ProcessComplexity.ENTERPRISE:
            return {
                "review_cadence": "Weekly steering committee",
                "escalation_path": "Tech Lead → Project Manager → Director → VP",
                "change_control": "Change Advisory Board for scope changes",
                "documentation": "ADRs, PRDs, Technical Specs required",
                "approvals": ["Security", "Compliance", "Architecture", "Business"]
            }
        elif analysis.complexity == ProcessComplexity.COMPLEX:
            return {
                "review_cadence": "Weekly team standup + bi-weekly stakeholder sync",
                "escalation_path": "Tech Lead → Manager → Director",
                "change_control": "ADR for architectural changes, team consensus for others",
                "documentation": "ADRs for major decisions, technical design doc",
                "approvals": ["Security", "Architecture"]
            }
        else:
            return {
                "review_cadence": "Weekly team standup",
                "escalation_path": "Tech Lead → Manager",
                "change_control": "Team consensus, ADR for major decisions",
                "documentation": "README, inline documentation",
                "approvals": ["Tech Lead"]
            }

    def _generate_adr_template(self, project_name: str) -> str:
        """Generate ADR template."""
        return f"""# ADR-001: [Decision Title]

## Status
Proposed | Accepted | Deprecated | Superseded

## Context
What is the issue we're trying to solve?
What constraints do we have?

## Decision
What decision did we make and why?

## Consequences
### Positive
- Benefit 1
- Benefit 2

### Negative
- Tradeoff 1
- Tradeoff 2

### Risks
- Risk 1 and mitigation

## Related
- Related ADRs
- Related documentation

## Project
{project_name}

## Date
{datetime.now().strftime("%Y-%m-%d")}
"""

    def _generate_prd_outline(self, analysis: ProcessAnalysis) -> str:
        """Generate PRD outline."""
        stakeholders = ", ".join(analysis.stakeholders[:3])
        return f"""### Product Requirements Document Outline

1. **Overview**
   - Problem statement: Manual {analysis.name.lower()} process
   - Solution summary: Automation using recommended approach

2. **Stakeholders**
   - Primary: {stakeholders}
   - Secondary: IT Operations, Support

3. **User Stories**
   - As a stakeholder, I want automated {analysis.name.lower()}
   - As an operator, I want monitoring and alerting
   - As a manager, I want visibility into process metrics

4. **Functional Requirements**
   - FR1: Automate data collection
   - FR2: Automate processing logic
   - FR3: Automate output generation
   - FR4: Provide manual override capability

5. **Non-Functional Requirements**
   - Performance: Complete in <{int(analysis.total_time_minutes * 0.2)} minutes
   - Reliability: 99% success rate
   - Security: Comply with data policies

6. **Success Criteria**
   - Time reduction >80%
   - Error rate <5%
   - User satisfaction >4/5
"""

    def _generate_tech_spec_outline(
        self,
        analysis: ProcessAnalysis,
        strategy: AutomationStrategy
    ) -> str:
        """Generate technical spec outline."""
        tools = [t['name'] for t in strategy.to_dict().get('recommended_tools', [])[:3]]
        return f"""### Technical Specification Outline

1. **Architecture Overview**
   - High-level system diagram
   - Component interactions
   - Data flow

2. **Technology Stack**
   - Primary tools: {', '.join(tools)}
   - Azure services: As per recommendations
   - Languages: Python, SQL

3. **Data Architecture**
   - Input sources: {', '.join(analysis.data_sources_involved[:3]) or 'TBD'}
   - Data transformations
   - Output formats

4. **Integration Points**
   - External systems
   - APIs and protocols
   - Authentication

5. **Security Design**
   - Access control
   - Data protection
   - Audit logging

6. **Monitoring & Operations**
   - Health checks
   - Alerting rules
   - Runbook procedures
"""


# Example usage
if __name__ == "__main__":
    from process_analyzer import ProcessAnalyzer
    from automation_recommender import AutomationRecommender
    from role_matcher import RoleMatcher

    # Analyze process
    analyzer = ProcessAnalyzer()
    analysis = analyzer.analyze_process(
        name="Monthly Sales Report",
        description="Generate and distribute monthly sales performance reports",
        steps=[
            {"name": "Extract CRM data", "time_minutes": 30, "manual": True, "data_sources": ["Salesforce"]},
            {"name": "Extract ERP data", "time_minutes": 45, "manual": True, "data_sources": ["SAP"]},
            {"name": "Merge and clean", "time_minutes": 60, "manual": True, "error_prone": True},
            {"name": "Calculate KPIs", "time_minutes": 30, "manual": True, "requires_expertise": True},
            {"name": "Generate charts", "time_minutes": 45, "manual": True},
            {"name": "Write summary", "time_minutes": 60, "manual": True, "requires_decision": True},
            {"name": "Review and send", "time_minutes": 30, "manual": True}
        ],
        frequency="monthly",
        stakeholders=["Sales Director", "CFO", "Regional Managers"]
    )

    # Get recommendations
    recommender = AutomationRecommender()
    strategy = recommender.recommend(analysis)

    # Match roles
    matcher = RoleMatcher()
    team = matcher.match_roles(analysis, strategy)

    # Generate plan
    generator = PlanGenerator()
    plan = generator.generate_plan(
        analysis=analysis,
        recommendations=strategy,
        team_composition=team
    )

    # Output as markdown
    print(plan.to_markdown())
