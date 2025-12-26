"""
Process Parser - Parses natural language process descriptions for AI-driven automation.

Part of the Tech Hub Skills Library (sd-08: Process Automation).

This module enables dynamic process analysis by parsing unstructured or
semi-structured process descriptions written in natural language or markdown.
Designed to work seamlessly with AI assistants like VS Code GitHub Copilot.
"""

import re
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple, Any
from enum import Enum
import json


class DocumentFormat(Enum):
    """Supported document formats for process descriptions."""
    MARKDOWN = "markdown"
    PLAIN_TEXT = "plain_text"
    STRUCTURED = "structured"
    YAML_FRONTMATTER = "yaml_frontmatter"


@dataclass
class ParsedStep:
    """A step extracted from natural language description."""
    name: str
    description: str
    estimated_time: Optional[str] = None
    is_manual: bool = True
    tools_mentioned: List[str] = field(default_factory=list)
    data_sources: List[str] = field(default_factory=list)
    pain_points: List[str] = field(default_factory=list)
    automation_hints: List[str] = field(default_factory=list)
    sequence_number: int = 0


@dataclass
class ParsedProcess:
    """Complete parsed process from natural language."""
    name: str
    description: str
    steps: List[ParsedStep]
    stakeholders: List[str]
    frequency: str
    pain_points: List[str]
    current_tools: List[str]
    data_sources: List[str]
    goals: List[str]
    constraints: List[str]
    raw_text: str
    confidence_score: float  # How confident we are in the parsing

    def to_analyzer_input(self) -> Dict:
        """Convert to format expected by ProcessAnalyzer."""
        return {
            "name": self.name,
            "description": self.description,
            "steps": [
                {
                    "name": step.name,
                    "description": step.description,
                    "time_minutes": self._parse_time(step.estimated_time),
                    "manual": step.is_manual,
                    "tools_used": step.tools_mentioned,
                    "data_sources": step.data_sources,
                    "error_prone": len(step.pain_points) > 0,
                    "requires_expertise": any(
                        kw in step.description.lower()
                        for kw in ["expertise", "experienced", "specialist", "complex", "judgment"]
                    ),
                    "requires_decision": any(
                        kw in step.description.lower()
                        for kw in ["decide", "decision", "choose", "evaluate", "assess", "determine"]
                    )
                }
                for step in self.steps
            ],
            "frequency": self.frequency,
            "stakeholders": self.stakeholders
        }

    def _parse_time(self, time_str: Optional[str]) -> float:
        """Parse time string to minutes."""
        if not time_str:
            return 30  # Default

        time_str = time_str.lower()

        # Extract numbers
        numbers = re.findall(r'(\d+(?:\.\d+)?)', time_str)
        if not numbers:
            return 30

        value = float(numbers[0])

        # Determine unit
        if 'hour' in time_str or 'hr' in time_str:
            return value * 60
        elif 'day' in time_str:
            return value * 480  # 8 hour workday
        elif 'min' in time_str:
            return value
        elif 'sec' in time_str:
            return value / 60
        else:
            return value  # Assume minutes

    def to_json(self) -> str:
        """Convert to JSON for AI consumption."""
        return json.dumps({
            "process": {
                "name": self.name,
                "description": self.description,
                "frequency": self.frequency,
                "stakeholders": self.stakeholders,
                "goals": self.goals,
                "constraints": self.constraints,
                "pain_points": self.pain_points,
                "current_tools": self.current_tools,
                "data_sources": self.data_sources
            },
            "steps": [
                {
                    "sequence": s.sequence_number,
                    "name": s.name,
                    "description": s.description,
                    "estimated_time": s.estimated_time,
                    "is_manual": s.is_manual,
                    "tools": s.tools_mentioned,
                    "data_sources": s.data_sources,
                    "pain_points": s.pain_points,
                    "automation_hints": s.automation_hints
                }
                for s in self.steps
            ],
            "parsing_confidence": self.confidence_score
        }, indent=2)


class ProcessParser:
    """
    Parses natural language process descriptions into structured data.

    Designed for dynamic, AI-driven automation discovery. Users can write
    process documentation in natural language, and this parser extracts
    the structured information needed for automation analysis.

    Works seamlessly with VS Code GitHub Copilot and other AI assistants.
    """

    # Keywords for identifying different aspects
    FREQUENCY_KEYWORDS = {
        "hourly": ["hourly", "every hour", "each hour"],
        "daily": ["daily", "every day", "each day", "once a day"],
        "weekly": ["weekly", "every week", "each week", "once a week"],
        "bi-weekly": ["bi-weekly", "every two weeks", "fortnightly"],
        "monthly": ["monthly", "every month", "each month", "once a month"],
        "quarterly": ["quarterly", "every quarter", "each quarter"],
        "annually": ["annually", "yearly", "every year", "once a year"],
        "ad-hoc": ["ad-hoc", "as needed", "on demand", "when required"]
    }

    TOOL_PATTERNS = [
        r'\b(Excel|Word|PowerPoint|Outlook|Teams|SharePoint)\b',
        r'\b(Salesforce|SAP|Oracle|Workday|ServiceNow)\b',
        r'\b(Jira|Confluence|Slack|Asana|Trello|Monday)\b',
        r'\b(Power BI|Tableau|Looker|Qlik)\b',
        r'\b(Python|SQL|R|JavaScript|VBA)\b',
        r'\b(Azure|AWS|GCP|Databricks|Snowflake)\b',
        r'\b(API|REST|GraphQL|webhook)\b',
        r'\b(email|Email|e-mail)\b',
        r'\b(PDF|CSV|JSON|XML)\b',
    ]

    DATA_SOURCE_PATTERNS = [
        r'\b(database|DB|data warehouse|data lake)\b',
        r'\b(CRM|ERP|HRIS|HCM)\b',
        r'\b(spreadsheet|worksheet|workbook)\b',
        r'\b(report|dashboard|analytics)\b',
        r'\b(file|folder|directory|share)\b',
        r'\b(API|web service|endpoint)\b',
        r'\b(email|inbox|mailbox)\b',
    ]

    PAIN_POINT_INDICATORS = [
        r'(takes too long|time-consuming|tedious)',
        r'(error-prone|mistakes|errors|inaccurate)',
        r'(manual|manually|by hand)',
        r'(repetitive|boring|mundane)',
        r'(bottleneck|delays?|waiting)',
        r'(frustrating|painful|difficult)',
        r'(copy.?paste|copying|duplicate)',
        r'(inconsistent|varies|depends on)',
    ]

    AUTOMATION_HINT_PATTERNS = [
        r'(could be automated|should automate|needs automation)',
        r'(same steps|repeated|routine)',
        r'(template|standardized|consistent)',
        r'(rule-based|if-then|conditions?)',
        r'(schedule|scheduled|recurring)',
        r'(notify|notification|alert)',
        r'(extract|transform|load|ETL)',
        r'(validate|validation|check)',
    ]

    def __init__(self):
        """Initialize the parser."""
        self._compile_patterns()

    def _compile_patterns(self):
        """Compile regex patterns for efficiency."""
        self.tool_regex = [re.compile(p, re.IGNORECASE) for p in self.TOOL_PATTERNS]
        self.data_source_regex = [re.compile(p, re.IGNORECASE) for p in self.DATA_SOURCE_PATTERNS]
        self.pain_point_regex = [re.compile(p, re.IGNORECASE) for p in self.PAIN_POINT_INDICATORS]
        self.automation_hint_regex = [re.compile(p, re.IGNORECASE) for p in self.AUTOMATION_HINT_PATTERNS]

    def parse(self, text: str, format_hint: Optional[DocumentFormat] = None) -> ParsedProcess:
        """
        Parse a natural language process description.

        Args:
            text: The process description text
            format_hint: Optional hint about the document format

        Returns:
            ParsedProcess with extracted information
        """
        # Detect format if not provided
        doc_format = format_hint or self._detect_format(text)

        # Extract components based on format
        if doc_format == DocumentFormat.MARKDOWN:
            return self._parse_markdown(text)
        elif doc_format == DocumentFormat.YAML_FRONTMATTER:
            return self._parse_yaml_frontmatter(text)
        else:
            return self._parse_plain_text(text)

    def _detect_format(self, text: str) -> DocumentFormat:
        """Detect the format of the input text."""
        if text.strip().startswith('---'):
            return DocumentFormat.YAML_FRONTMATTER
        elif re.search(r'^#+\s', text, re.MULTILINE):
            return DocumentFormat.MARKDOWN
        elif re.search(r'^\d+\.\s|^-\s|^\*\s', text, re.MULTILINE):
            return DocumentFormat.MARKDOWN
        else:
            return DocumentFormat.PLAIN_TEXT

    def _parse_markdown(self, text: str) -> ParsedProcess:
        """Parse markdown-formatted process description."""
        lines = text.split('\n')

        # Extract title from first heading
        name = "Untitled Process"
        for line in lines:
            if line.startswith('#'):
                name = re.sub(r'^#+\s*', '', line).strip()
                break

        # Extract sections
        sections = self._extract_sections(text)

        # Parse steps from numbered lists or step sections
        steps = self._extract_steps_markdown(text, sections)

        # Extract other components
        description = sections.get('overview', sections.get('description', ''))
        stakeholders = self._extract_list_items(sections.get('stakeholders', ''))
        frequency = self._detect_frequency(text)
        pain_points = self._extract_pain_points(text)
        current_tools = self._extract_tools(text)
        data_sources = self._extract_data_sources(text)
        goals = self._extract_list_items(sections.get('goals', sections.get('objectives', '')))
        constraints = self._extract_list_items(sections.get('constraints', sections.get('limitations', '')))

        # Calculate confidence
        confidence = self._calculate_confidence(steps, stakeholders, description)

        return ParsedProcess(
            name=name,
            description=description if isinstance(description, str) else ' '.join(description),
            steps=steps,
            stakeholders=stakeholders,
            frequency=frequency,
            pain_points=pain_points,
            current_tools=current_tools,
            data_sources=data_sources,
            goals=goals,
            constraints=constraints,
            raw_text=text,
            confidence_score=confidence
        )

    def _parse_yaml_frontmatter(self, text: str) -> ParsedProcess:
        """Parse markdown with YAML frontmatter."""
        # Split frontmatter from content
        parts = text.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            content = parts[2]
        else:
            frontmatter = ""
            content = text

        # Parse frontmatter for metadata
        metadata = self._parse_simple_yaml(frontmatter)

        # Parse content as markdown
        parsed = self._parse_markdown(content)

        # Override with frontmatter values
        if metadata.get('name'):
            parsed.name = metadata['name']
        if metadata.get('frequency'):
            parsed.frequency = metadata['frequency']
        if metadata.get('stakeholders'):
            parsed.stakeholders = metadata['stakeholders'] if isinstance(metadata['stakeholders'], list) else [metadata['stakeholders']]

        return parsed

    def _parse_plain_text(self, text: str) -> ParsedProcess:
        """Parse plain text process description."""
        paragraphs = text.split('\n\n')

        # First paragraph is usually the description
        description = paragraphs[0] if paragraphs else ""
        name = description[:50].strip() + "..." if len(description) > 50 else description

        # Look for step patterns
        steps = self._extract_steps_plain(text)

        # Extract other components
        frequency = self._detect_frequency(text)
        pain_points = self._extract_pain_points(text)
        current_tools = self._extract_tools(text)
        data_sources = self._extract_data_sources(text)

        confidence = self._calculate_confidence(steps, [], description)

        return ParsedProcess(
            name=name,
            description=description,
            steps=steps,
            stakeholders=[],
            frequency=frequency,
            pain_points=pain_points,
            current_tools=current_tools,
            data_sources=data_sources,
            goals=[],
            constraints=[],
            raw_text=text,
            confidence_score=confidence
        )

    def _extract_sections(self, text: str) -> Dict[str, str]:
        """Extract sections from markdown text."""
        sections = {}
        current_section = "intro"
        current_content = []

        for line in text.split('\n'):
            if re.match(r'^#+\s', line):
                if current_content:
                    sections[current_section.lower()] = '\n'.join(current_content)
                current_section = re.sub(r'^#+\s*', '', line).strip()
                current_content = []
            else:
                current_content.append(line)

        if current_content:
            sections[current_section.lower()] = '\n'.join(current_content)

        return sections

    def _extract_steps_markdown(self, text: str, sections: Dict) -> List[ParsedStep]:
        """Extract steps from markdown."""
        steps = []

        # Look for steps section
        steps_text = sections.get('steps', sections.get('process steps', sections.get('workflow', '')))

        if not steps_text:
            # Look for numbered list anywhere
            steps_text = text

        # Find numbered list items
        step_pattern = r'(?:^|\n)\s*(\d+)[.\)]\s*\*?\*?([^:\n]+?)(?:\*?\*?)?\s*(?::|\n|$)(.*?)(?=(?:\n\s*\d+[.\)]|\Z))'
        matches = re.findall(step_pattern, steps_text, re.DOTALL | re.MULTILINE)

        if matches:
            for i, (num, name, desc) in enumerate(matches):
                step = self._create_step(name.strip(), desc.strip(), i + 1)
                steps.append(step)
        else:
            # Try bullet points
            bullet_pattern = r'(?:^|\n)\s*[-*]\s+(.+?)(?=\n\s*[-*]|\n\n|\Z)'
            matches = re.findall(bullet_pattern, steps_text, re.DOTALL)
            for i, content in enumerate(matches):
                step = self._create_step(content.strip()[:100], content.strip(), i + 1)
                steps.append(step)

        return steps

    def _extract_steps_plain(self, text: str) -> List[ParsedStep]:
        """Extract steps from plain text."""
        steps = []

        # Look for patterns like "First, ...", "Then, ...", "Finally, ..."
        sequence_words = [
            (r'\bfirst\b', 1), (r'\bsecond\b', 2), (r'\bthird\b', 3),
            (r'\bthen\b', 0), (r'\bnext\b', 0), (r'\bafter that\b', 0),
            (r'\bfinally\b', 99), (r'\blast(?:ly)?\b', 99)
        ]

        sentences = re.split(r'[.!?]+', text)
        step_num = 0

        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 10:
                continue

            for pattern, _ in sequence_words:
                if re.search(pattern, sentence, re.IGNORECASE):
                    step_num += 1
                    step = self._create_step(sentence[:100], sentence, step_num)
                    steps.append(step)
                    break

        return steps

    def _create_step(self, name: str, description: str, sequence: int) -> ParsedStep:
        """Create a ParsedStep with extracted metadata."""
        # Extract time estimate
        time_match = re.search(r'(\d+)\s*(minutes?|mins?|hours?|hrs?|days?)', description, re.IGNORECASE)
        time_str = time_match.group(0) if time_match else None

        # Check if manual
        is_manual = not any(kw in description.lower() for kw in ['automated', 'automatic', 'auto-'])

        # Extract tools
        tools = []
        for regex in self.tool_regex:
            tools.extend(regex.findall(description))

        # Extract data sources
        data_sources = []
        for regex in self.data_source_regex:
            data_sources.extend(regex.findall(description))

        # Extract pain points
        pain_points = []
        for regex in self.pain_point_regex:
            if regex.search(description):
                pain_points.append(regex.pattern)

        # Extract automation hints
        automation_hints = []
        for regex in self.automation_hint_regex:
            if regex.search(description):
                automation_hints.append(regex.pattern)

        return ParsedStep(
            name=name,
            description=description,
            estimated_time=time_str,
            is_manual=is_manual,
            tools_mentioned=list(set(tools)),
            data_sources=list(set(data_sources)),
            pain_points=pain_points,
            automation_hints=automation_hints,
            sequence_number=sequence
        )

    def _extract_list_items(self, text: str) -> List[str]:
        """Extract list items from text."""
        items = []
        # Bullet points
        items.extend(re.findall(r'[-*]\s+(.+?)(?:\n|$)', text))
        # Numbered
        items.extend(re.findall(r'\d+[.\)]\s+(.+?)(?:\n|$)', text))
        # Comma-separated in a sentence
        if not items and ',' in text:
            items = [i.strip() for i in text.split(',')]
        return [i.strip() for i in items if i.strip()]

    def _detect_frequency(self, text: str) -> str:
        """Detect process frequency from text."""
        text_lower = text.lower()
        for freq, keywords in self.FREQUENCY_KEYWORDS.items():
            for kw in keywords:
                if kw in text_lower:
                    return freq
        return "ad-hoc"

    def _extract_pain_points(self, text: str) -> List[str]:
        """Extract pain points from text."""
        pain_points = []
        for regex in self.pain_point_regex:
            matches = regex.findall(text)
            pain_points.extend(matches)
        return list(set(pain_points))

    def _extract_tools(self, text: str) -> List[str]:
        """Extract mentioned tools from text."""
        tools = []
        for regex in self.tool_regex:
            tools.extend(regex.findall(text))
        return list(set(tools))

    def _extract_data_sources(self, text: str) -> List[str]:
        """Extract data sources from text."""
        sources = []
        for regex in self.data_source_regex:
            sources.extend(regex.findall(text))
        return list(set(sources))

    def _parse_simple_yaml(self, yaml_text: str) -> Dict[str, Any]:
        """Simple YAML parser for frontmatter."""
        result = {}
        current_key = None
        current_list = []

        for line in yaml_text.split('\n'):
            line = line.strip()
            if not line:
                continue

            if ':' in line and not line.startswith('-'):
                if current_key and current_list:
                    result[current_key] = current_list
                    current_list = []

                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()

                if value:
                    result[key] = value
                else:
                    current_key = key
            elif line.startswith('-'):
                current_list.append(line[1:].strip())

        if current_key and current_list:
            result[current_key] = current_list

        return result

    def _calculate_confidence(self, steps: List[ParsedStep], stakeholders: List[str], description: str) -> float:
        """Calculate parsing confidence score."""
        confidence = 50.0  # Base

        # More steps = more confidence (up to 20 points)
        confidence += min(len(steps) * 5, 20)

        # Stakeholders identified = +10
        if stakeholders:
            confidence += 10

        # Good description = +10
        if len(description) > 100:
            confidence += 10

        # Steps have details = +10
        detailed_steps = sum(1 for s in steps if len(s.description) > 50)
        confidence += min(detailed_steps * 2, 10)

        return min(confidence, 100)


# Example usage and AI integration helpers
def parse_for_copilot(process_description: str) -> str:
    """
    Parse a process description and return JSON for AI consumption.

    Use this in VS Code with GitHub Copilot:
    1. Write your process description in a markdown file
    2. Call this function with the description
    3. Pass the output to the AI prompt generator

    Example:
        from process_parser import parse_for_copilot

        description = '''
        # Monthly Sales Report Process

        ## Overview
        Every month we generate sales reports for leadership.

        ## Steps
        1. Export data from Salesforce (30 mins)
        2. Clean data in Excel (1 hour) - very error-prone!
        3. Create pivot tables (45 mins)
        4. Generate charts (30 mins)
        5. Write summary (1 hour)
        6. Email to stakeholders (15 mins)

        ## Stakeholders
        - Sales Director
        - CFO
        - Regional Managers
        '''

        parsed_json = parse_for_copilot(description)
        print(parsed_json)
    """
    parser = ProcessParser()
    parsed = parser.parse(process_description)
    return parsed.to_json()


if __name__ == "__main__":
    # Demo with sample process
    sample = """
# Weekly Customer Feedback Analysis

## Overview
Every week, we analyze customer feedback from multiple sources to identify
trends and issues. This process takes about 4 hours and is mostly manual.

## Current Pain Points
- Data comes from 5 different sources (email, surveys, social, support tickets, reviews)
- Manually copying data into Excel is tedious and error-prone
- Categorization is inconsistent between team members
- Report formatting takes too long

## Steps
1. **Export survey responses** from SurveyMonkey (20 mins)
2. **Download support tickets** from Zendesk (15 mins)
3. **Scrape social mentions** - manual copy/paste from Hootsuite (30 mins)
4. **Consolidate in Excel** - merge all sources, very tedious (45 mins)
5. **Categorize feedback** - requires judgment, inconsistent (1 hour)
6. **Identify trends** - pivot tables and analysis (45 mins)
7. **Generate charts** in Power BI (30 mins)
8. **Write summary report** - needs expertise (1 hour)
9. **Send to stakeholders** via email (10 mins)

## Stakeholders
- Product Manager
- Customer Success Lead
- VP of Product
- Support Team Lead

## Goals
- Reduce time spent from 4 hours to under 1 hour
- Improve categorization consistency
- Enable real-time or daily analysis instead of weekly

## Constraints
- Budget is limited
- Team has basic Python skills
- Must maintain data privacy (GDPR)
"""

    parser = ProcessParser()
    result = parser.parse(sample)

    print("=" * 60)
    print("PARSED PROCESS")
    print("=" * 60)
    print(f"Name: {result.name}")
    print(f"Frequency: {result.frequency}")
    print(f"Confidence: {result.confidence_score}%")
    print(f"\nStakeholders: {', '.join(result.stakeholders)}")
    print(f"Tools Found: {', '.join(result.current_tools)}")
    print(f"Pain Points: {result.pain_points}")
    print(f"\nSteps ({len(result.steps)}):")
    for step in result.steps:
        print(f"  {step.sequence_number}. {step.name}")
        if step.estimated_time:
            print(f"     Time: {step.estimated_time}")
        if step.pain_points:
            print(f"     Issues: {step.pain_points}")

    print("\n" + "=" * 60)
    print("JSON OUTPUT FOR AI")
    print("=" * 60)
    print(result.to_json())
