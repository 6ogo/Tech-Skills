"""
AI Prompt Generator - Generates prompts for AI-driven automation discovery.

Part of the Tech Hub Skills Library (sd-08: Process Automation).

This module generates optimized prompts for AI assistants (GitHub Copilot,
Claude, ChatGPT, etc.) to analyze processes and suggest automation solutions.
Designed for seamless VS Code integration.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from enum import Enum
import json

try:
    from process_parser import ParsedProcess, ProcessParser
    from process_analyzer import ProcessAnalysis
except ImportError:
    # Allow standalone usage
    ParsedProcess = Any
    ProcessAnalysis = Any


class PromptStyle(Enum):
    """Different prompt styles for different AI assistants."""
    CONCISE = "concise"           # Short, focused prompts
    DETAILED = "detailed"         # Comprehensive analysis
    STRUCTURED = "structured"     # JSON/YAML output format
    CONVERSATIONAL = "conversational"  # Chat-style exploration
    COPILOT = "copilot"          # Optimized for GitHub Copilot
    STEP_BY_STEP = "step_by_step"  # Guided analysis


class AnalysisDepth(Enum):
    """How deep the AI should analyze."""
    QUICK = "quick"              # High-level suggestions
    STANDARD = "standard"        # Balanced analysis
    DEEP = "deep"               # Comprehensive exploration
    IMPLEMENTATION = "implementation"  # Ready-to-implement details


@dataclass
class GeneratedPrompt:
    """A generated prompt with metadata."""
    prompt: str
    style: PromptStyle
    depth: AnalysisDepth
    expected_output: str
    follow_up_prompts: List[str]
    context_variables: Dict[str, str]

    def to_clipboard_format(self) -> str:
        """Format for easy copy-paste."""
        return f"""
{self.prompt}

---
Expected Output: {self.expected_output}
Follow-up Questions:
{chr(10).join(f'- {q}' for q in self.follow_up_prompts)}
"""


class AIPromptGenerator:
    """
    Generates optimized prompts for AI assistants to analyze automation.

    Use this to create prompts that help AI assistants like GitHub Copilot
    understand your process and suggest automation solutions.

    Example workflow in VS Code:
    1. Write your process in PROCESS_TEMPLATE.md
    2. Run: prompt = generator.generate_discovery_prompt(parsed_process)
    3. Paste prompt into Copilot Chat
    4. Get automation suggestions
    5. Use follow-up prompts to drill deeper
    """

    # Tech Hub skill context for AI
    TECH_HUB_CONTEXT = """
You have access to the following automation capabilities from the Tech Hub Skills Library:

**Data Engineering (de-*):**
- de-01: Lakehouse Architecture (Bronze-Silver-Gold medallion pattern)
- de-02: ETL/ELT Pipeline Orchestration (Airflow, Data Factory)
- de-03: Data Quality & Validation (Great Expectations)
- de-04: Real-Time Streaming (Kafka, Event Hubs)

**AI Engineering (ai-*):**
- ai-01: Prompt Engineering & Optimization
- ai-02: RAG Pipeline Builder (retrieval augmented generation)
- ai-03: LLM Agent Orchestration (multi-agent systems)
- ai-07: Production LLM API Integration

**ML Engineering (ml-*):**
- ml-01: MLOps Pipeline Automation
- ml-03: Model Training & Tuning
- ml-04: Model Serving & APIs

**DevOps (do-*):**
- do-01: CI/CD Pipeline Design
- do-03: Infrastructure as Code (Terraform, Bicep)
- do-08: Monitoring & Alerting

**Azure Services:**
- Azure Data Factory, Synapse, Databricks
- Azure OpenAI, Azure ML
- Azure Functions, Logic Apps, Power Automate
- Azure Event Hubs, Service Bus
"""

    def __init__(self, include_tech_hub_context: bool = True):
        """Initialize the prompt generator."""
        self.include_context = include_tech_hub_context

    def generate_discovery_prompt(
        self,
        process: ParsedProcess,
        style: PromptStyle = PromptStyle.DETAILED,
        depth: AnalysisDepth = AnalysisDepth.STANDARD
    ) -> GeneratedPrompt:
        """
        Generate a prompt for initial automation discovery.

        This is the main entry point - use this to get AI suggestions
        for how to automate a process.
        """
        if style == PromptStyle.COPILOT:
            return self._generate_copilot_prompt(process, depth)
        elif style == PromptStyle.STRUCTURED:
            return self._generate_structured_prompt(process, depth)
        elif style == PromptStyle.STEP_BY_STEP:
            return self._generate_stepwise_prompt(process, depth)
        else:
            return self._generate_detailed_prompt(process, depth)

    def _generate_copilot_prompt(
        self,
        process: ParsedProcess,
        depth: AnalysisDepth
    ) -> GeneratedPrompt:
        """Generate prompt optimized for GitHub Copilot."""
        prompt = f"""# Automation Analysis Request

## Process to Analyze
**Name:** {process.name}
**Frequency:** {process.frequency}
**Current Pain Points:** {', '.join(process.pain_points) if process.pain_points else 'Not specified'}

## Current Steps
{self._format_steps_for_prompt(process.steps)}

## Current Tools
{', '.join(process.current_tools) if process.current_tools else 'Manual/unspecified'}

## Goals
{chr(10).join(f'- {g}' for g in process.goals) if process.goals else '- Reduce manual effort\n- Improve accuracy\n- Save time'}

## Analysis Request
Please analyze this process and provide:

1. **Automation Score** (0-100): How automatable is this process?

2. **Recommended Automation Approach:**
   - Which steps can be fully automated?
   - Which steps need human-in-the-loop?
   - What's the optimal automation pattern? (RPA, Workflow, ML, AI-powered)

3. **Technology Recommendations:**
   - Primary tools/services to use
   - Azure services that fit
   - Open source alternatives

4. **Implementation Roadmap:**
   - Quick wins (< 1 week)
   - Medium-term improvements (1-4 weeks)
   - Long-term optimization

5. **Code Snippets:** Provide starter code for the most impactful automation.
"""

        if self.include_context:
            prompt = self.TECH_HUB_CONTEXT + "\n---\n\n" + prompt

        follow_ups = [
            "Show me the Python code to automate step [X]",
            "How would I implement this using Azure Data Factory?",
            "What's the error handling strategy for this automation?",
            "How do I add monitoring and alerting?",
            "What tests should I write for this automation?"
        ]

        return GeneratedPrompt(
            prompt=prompt,
            style=PromptStyle.COPILOT,
            depth=depth,
            expected_output="Structured automation analysis with code snippets",
            follow_up_prompts=follow_ups,
            context_variables={
                "process_name": process.name,
                "step_count": str(len(process.steps)),
                "frequency": process.frequency
            }
        )

    def _generate_structured_prompt(
        self,
        process: ParsedProcess,
        depth: AnalysisDepth
    ) -> GeneratedPrompt:
        """Generate prompt for structured JSON/YAML output."""
        prompt = f"""Analyze the following process for automation opportunities.

**INPUT PROCESS:**
```json
{process.to_json()}
```

**REQUIRED OUTPUT FORMAT:**
```yaml
automation_analysis:
  overall_score: <0-100>
  complexity: <simple|moderate|complex|enterprise>
  primary_approach: <rpa|workflow|data_pipeline|ml_based|ai_powered|hybrid>

  step_analysis:
    - step_number: <n>
      automation_feasibility: <high|medium|low>
      recommended_approach: <description>
      tools: [<list of tools>]
      effort: <hours/days>

  recommended_architecture:
    pattern: <description>
    components:
      - name: <component>
        purpose: <why>
        technology: <what>

  implementation_phases:
    - phase: 1
      name: <phase name>
      duration: <time>
      deliverables: [<list>]

  risks:
    - risk: <description>
      mitigation: <strategy>

  roi_estimate:
    time_savings_percent: <0-100>
    payback_months: <n>
```

Provide your analysis in exactly this YAML format.
"""

        if self.include_context:
            prompt = self.TECH_HUB_CONTEXT + "\n---\n\n" + prompt

        return GeneratedPrompt(
            prompt=prompt,
            style=PromptStyle.STRUCTURED,
            depth=depth,
            expected_output="YAML-formatted automation analysis",
            follow_up_prompts=[
                "Convert this to Terraform/Bicep infrastructure code",
                "Generate the CI/CD pipeline YAML for this",
                "Create the monitoring dashboard configuration"
            ],
            context_variables={"output_format": "yaml"}
        )

    def _generate_stepwise_prompt(
        self,
        process: ParsedProcess,
        depth: AnalysisDepth
    ) -> GeneratedPrompt:
        """Generate step-by-step analysis prompt."""
        prompt = f"""Let's analyze this process step by step for automation.

## The Process: {process.name}

### Step-by-Step Analysis Framework

For each step below, I'll ask you to evaluate:
- A: Automation feasibility (1-10)
- B: Technical approach
- C: Tools/services needed
- D: Implementation complexity
- E: Dependencies on other steps

---

### Current Process Steps:

{self._format_steps_for_prompt(process.steps)}

---

### Let's Start

**STEP 1 ANALYSIS:**
Please analyze the first step: "{process.steps[0].name if process.steps else 'N/A'}"

Provide:
1. Automation feasibility score (1-10) and why
2. Best technical approach for this specific step
3. Recommended tools (prefer Azure-native when applicable)
4. Estimated effort to automate
5. What information flows into and out of this step

After analyzing Step 1, I'll ask about subsequent steps.
"""

        return GeneratedPrompt(
            prompt=prompt,
            style=PromptStyle.STEP_BY_STEP,
            depth=depth,
            expected_output="Iterative step-by-step analysis",
            follow_up_prompts=[
                f"Now analyze step {i+2}: {step.name}"
                for i, step in enumerate(process.steps[1:5])
            ],
            context_variables={"analysis_mode": "iterative"}
        )

    def _generate_detailed_prompt(
        self,
        process: ParsedProcess,
        depth: AnalysisDepth
    ) -> GeneratedPrompt:
        """Generate comprehensive detailed analysis prompt."""
        depth_instructions = {
            AnalysisDepth.QUICK: "Provide a high-level overview focusing on the top 3 automation opportunities.",
            AnalysisDepth.STANDARD: "Provide a balanced analysis covering all major aspects.",
            AnalysisDepth.DEEP: "Provide comprehensive analysis including edge cases, error handling, and optimization.",
            AnalysisDepth.IMPLEMENTATION: "Provide implementation-ready details including code, configurations, and deployment steps."
        }

        prompt = f"""# Process Automation Analysis

## Context
I need help automating a business process. Please analyze it thoroughly and suggest the best automation strategy.

## Process Details

**Name:** {process.name}
**Description:** {process.description}
**Frequency:** {process.frequency}
**Stakeholders:** {', '.join(process.stakeholders) if process.stakeholders else 'Not specified'}

### Current Workflow

{self._format_steps_for_prompt(process.steps)}

### Pain Points
{chr(10).join(f'- {p}' for p in process.pain_points) if process.pain_points else '- Manual effort\n- Time-consuming'}

### Current Tools in Use
{', '.join(process.current_tools) if process.current_tools else 'Mostly manual'}

### Data Sources Involved
{', '.join(process.data_sources) if process.data_sources else 'Various'}

### Goals for Automation
{chr(10).join(f'- {g}' for g in process.goals) if process.goals else '- Reduce time\n- Improve accuracy\n- Enable scaling'}

### Constraints
{chr(10).join(f'- {c}' for c in process.constraints) if process.constraints else '- Standard enterprise constraints'}

---

## Analysis Request

{depth_instructions[depth]}

Please provide:

### 1. Executive Summary
- Overall automation potential (score 0-100)
- Recommended approach in one sentence
- Expected benefits

### 2. Detailed Step Analysis
For each step, evaluate:
- Can it be automated? (fully/partially/no)
- What technology fits best?
- What are the risks?

### 3. Recommended Architecture
- High-level design
- Key components
- Data flow

### 4. Technology Stack
- Primary tools and why
- Azure services to leverage
- Integration points

### 5. Implementation Roadmap
- Phase 1: Quick wins
- Phase 2: Core automation
- Phase 3: Optimization

### 6. Risk Assessment
- Technical risks
- Business risks
- Mitigation strategies

### 7. Success Metrics
- How to measure success
- KPIs to track

{f"### 8. Starter Code" if depth == AnalysisDepth.IMPLEMENTATION else ""}
{f"Provide working code snippets for the key automation components." if depth == AnalysisDepth.IMPLEMENTATION else ""}
"""

        if self.include_context:
            prompt = self.TECH_HUB_CONTEXT + "\n---\n\n" + prompt

        return GeneratedPrompt(
            prompt=prompt,
            style=PromptStyle.DETAILED,
            depth=depth,
            expected_output="Comprehensive automation analysis document",
            follow_up_prompts=[
                "Elaborate on the architecture with a diagram",
                "Provide the implementation code for [component]",
                "How do I handle [specific edge case]?",
                "What's the testing strategy?",
                "How do I deploy this to production?"
            ],
            context_variables={
                "analysis_depth": depth.value,
                "process_name": process.name
            }
        )

    def _format_steps_for_prompt(self, steps: List) -> str:
        """Format steps for inclusion in prompt."""
        if not steps:
            return "*No steps defined*"

        lines = []
        for step in steps:
            line = f"{step.sequence_number}. **{step.name}**"
            if step.estimated_time:
                line += f" ({step.estimated_time})"
            if step.description and step.description != step.name:
                line += f"\n   {step.description[:200]}"
            if step.pain_points:
                line += f"\n    Issues: {', '.join(str(p) for p in step.pain_points[:3])}"
            if step.tools_mentioned:
                line += f"\n    Tools: {', '.join(step.tools_mentioned)}"
            lines.append(line)

        return "\n\n".join(lines)

    def generate_implementation_prompt(
        self,
        process: ParsedProcess,
        target_step: int,
        technology: str = "python"
    ) -> GeneratedPrompt:
        """Generate a prompt for implementing specific step automation."""
        if target_step > len(process.steps) or target_step < 1:
            target_step = 1

        step = process.steps[target_step - 1]

        prompt = f"""# Implementation Request

## Context
I'm automating the "{process.name}" process and need to implement step {target_step}.

## Step to Implement
**Name:** {step.name}
**Description:** {step.description}
**Current Duration:** {step.estimated_time or 'Unknown'}
**Tools Used:** {', '.join(step.tools_mentioned) if step.tools_mentioned else 'Manual'}
**Data Sources:** {', '.join(step.data_sources) if step.data_sources else 'Various'}

## Requirements
- Technology: {technology}
- Must integrate with: {', '.join(process.current_tools) if process.current_tools else 'existing systems'}
- Error handling required
- Logging for observability

## Implementation Request

Please provide:

1. **Complete working code** for this step
2. **Configuration/setup** needed
3. **Dependencies** (requirements.txt or similar)
4. **Unit tests**
5. **Integration points** with previous/next steps
6. **Error handling** strategy
7. **Logging** approach

Make the code production-ready with proper:
- Type hints
- Docstrings
- Error handling
- Logging
- Configuration management
"""

        return GeneratedPrompt(
            prompt=prompt,
            style=PromptStyle.COPILOT,
            depth=AnalysisDepth.IMPLEMENTATION,
            expected_output=f"Working {technology} code for step {target_step}",
            follow_up_prompts=[
                "Add retry logic with exponential backoff",
                "How do I test this in isolation?",
                "Create a Docker container for this",
                "Add Prometheus metrics",
                "Implement the next step"
            ],
            context_variables={
                "step_number": str(target_step),
                "technology": technology
            }
        )

    def generate_comparison_prompt(
        self,
        process: ParsedProcess,
        approaches: List[str] = None
    ) -> GeneratedPrompt:
        """Generate prompt to compare different automation approaches."""
        approaches = approaches or [
            "Azure Logic Apps + Power Automate",
            "Python + Airflow + Azure Functions",
            "Azure Data Factory + Synapse",
            "Custom microservices"
        ]

        prompt = f"""# Automation Approach Comparison

## Process Overview
**Name:** {process.name}
**Steps:** {len(process.steps)}
**Frequency:** {process.frequency}

## Approaches to Compare
{chr(10).join(f'{i+1}. {a}' for i, a in enumerate(approaches))}

## Comparison Request

For the process described above, compare these {len(approaches)} approaches:

Create a comparison table with:
| Criteria | {' | '.join(approaches)} |
|----------|{'|'.join(['---' for _ in approaches])}|
| Initial Cost | | |
| Ongoing Cost | | |
| Time to Implement | | |
| Scalability | | |
| Maintainability | | |
| Flexibility | | |
| Learning Curve | | |
| Azure Integration | | |
| Error Handling | | |
| Monitoring | | |

Then provide:

1. **Recommendation** - Which approach fits best and why
2. **Trade-offs** - What you gain/lose with each
3. **Migration Path** - How to evolve if needs change
4. **Risk Comparison** - Risks unique to each approach
"""

        return GeneratedPrompt(
            prompt=prompt,
            style=PromptStyle.DETAILED,
            depth=AnalysisDepth.STANDARD,
            expected_output="Comparison table with recommendation",
            follow_up_prompts=[
                f"Show me how to implement with {approaches[0]}",
                "What if budget is the primary constraint?",
                "What if time-to-market is critical?",
                "How would the architecture look for the recommended approach?"
            ],
            context_variables={"approaches_count": str(len(approaches))}
        )


# Convenience functions for quick usage
def quick_analyze(process_text: str) -> str:
    """
    Quick analysis of a process from text.

    Usage in VS Code:
        1. Write your process description
        2. Call: prompt = quick_analyze(your_description)
        3. Paste into Copilot Chat

    Returns the prompt ready for copy-paste.
    """
    from process_parser import ProcessParser

    parser = ProcessParser()
    parsed = parser.parse(process_text)

    generator = AIPromptGenerator()
    result = generator.generate_discovery_prompt(parsed, PromptStyle.COPILOT)

    return result.prompt


def get_implementation_prompt(process_text: str, step: int, tech: str = "python") -> str:
    """Get implementation prompt for a specific step."""
    from process_parser import ProcessParser

    parser = ProcessParser()
    parsed = parser.parse(process_text)

    generator = AIPromptGenerator()
    result = generator.generate_implementation_prompt(parsed, step, tech)

    return result.prompt


# VS Code / Copilot integration example
VSCODE_USAGE = """
# How to Use with VS Code GitHub Copilot

## Quick Start

1. Create a new file: `my_process.md`
2. Describe your process using the template (see PROCESS_TEMPLATE.md)
3. Open a new Python file and run:

```python
from ai_prompt_generator import quick_analyze

# Read your process description
with open('my_process.md', 'r') as f:
    process_text = f.read()

# Generate the prompt
prompt = quick_analyze(process_text)

# Copy to clipboard (or print and copy)
print(prompt)
```

4. Open GitHub Copilot Chat (Ctrl+Shift+I)
5. Paste the prompt
6. Get automation suggestions!

## Advanced Usage

```python
from process_parser import ProcessParser
from ai_prompt_generator import AIPromptGenerator, PromptStyle, AnalysisDepth

# Parse your process
parser = ProcessParser()
parsed = parser.parse(process_text)

# Generate different types of prompts
generator = AIPromptGenerator()

# For quick overview
quick_prompt = generator.generate_discovery_prompt(
    parsed,
    style=PromptStyle.CONCISE,
    depth=AnalysisDepth.QUICK
)

# For detailed implementation
impl_prompt = generator.generate_implementation_prompt(
    parsed,
    target_step=1,
    technology="python"
)

# For comparing approaches
compare_prompt = generator.generate_comparison_prompt(
    parsed,
    approaches=["Azure Functions", "Airflow", "Logic Apps"]
)
```
"""


if __name__ == "__main__":
    # Demo
    sample_process = """
# Invoice Processing Workflow

## Overview
Monthly invoice processing for vendor payments. Currently takes 2 days.

## Steps
1. **Receive invoices** via email (ongoing)
2. **Extract invoice data** - manually type into Excel (2 hours)
3. **Validate against PO** - check purchase orders (1 hour)
4. **Get approvals** - email chains, very slow (4 hours wait)
5. **Enter into ERP** - manual SAP entry (1 hour)
6. **Schedule payment** - batch processing (30 mins)
7. **Archive documents** - save to SharePoint (20 mins)

## Pain Points
- Manual data entry is error-prone
- Approval delays are frustrating
- No visibility into status

## Stakeholders
- Accounts Payable Team
- Finance Manager
- Department Heads (approvers)

## Goals
- Reduce processing time by 80%
- Eliminate manual data entry errors
- Real-time status visibility
"""

    from process_parser import ProcessParser

    parser = ProcessParser()
    parsed = parser.parse(sample_process)

    generator = AIPromptGenerator()

    print("=" * 70)
    print("GENERATED COPILOT PROMPT")
    print("=" * 70)

    result = generator.generate_discovery_prompt(parsed, PromptStyle.COPILOT)
    print(result.prompt[:2000] + "...")

    print("\n" + "=" * 70)
    print("FOLLOW-UP PROMPTS")
    print("=" * 70)
    for p in result.follow_up_prompts:
        print(f"  → {p}")
