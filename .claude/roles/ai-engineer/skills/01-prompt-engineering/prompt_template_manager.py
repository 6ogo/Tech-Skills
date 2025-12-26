"""
Prompt Template Manager with Version Control
Manages prompt templates with variable injection, inheritance, and versioning.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
from jinja2 import Environment, FileSystemLoader, Template
import yaml


class PromptTemplate:
    """Version-controlled prompt template with variable injection."""

    def __init__(
        self,
        name: str,
        template: str,
        version: str = "1.0.0",
        metadata: Optional[Dict[str, Any]] = None,
        parent: Optional[str] = None
    ):
        self.name = name
        self.template = template
        self.version = version
        self.metadata = metadata or {}
        self.parent = parent
        self.created_at = datetime.now().isoformat()
        self._jinja_template = Template(template)

    def render(self, **kwargs) -> str:
        """Render the template with provided variables."""
        return self._jinja_template.render(**kwargs)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "name": self.name,
            "template": self.template,
            "version": self.version,
            "metadata": self.metadata,
            "parent": self.parent,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PromptTemplate":
        """Create from dictionary."""
        return cls(
            name=data["name"],
            template=data["template"],
            version=data.get("version", "1.0.0"),
            metadata=data.get("metadata", {}),
            parent=data.get("parent")
        )

    def save(self, directory: str = "./prompts") -> None:
        """Save template to disk."""
        Path(directory).mkdir(parents=True, exist_ok=True)
        filepath = Path(directory) / f"{self.name}_v{self.version}.json"

        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)

        print(f"✅ Saved: {filepath}")

    @classmethod
    def load(cls, name: str, version: Optional[str] = None, directory: str = "./prompts") -> "PromptTemplate":
        """Load template from disk."""
        if version:
            filepath = Path(directory) / f"{name}_v{version}.json"
        else:
            # Load latest version
            pattern = f"{name}_v*.json"
            files = sorted(Path(directory).glob(pattern), reverse=True)
            if not files:
                raise FileNotFoundError(f"No template found for {name}")
            filepath = files[0]

        with open(filepath, 'r') as f:
            data = json.load(f)

        return cls.from_dict(data)


class PromptLibrary:
    """Centralized library for managing multiple prompt templates."""

    def __init__(self, library_path: str = "./prompt_library"):
        self.library_path = Path(library_path)
        self.library_path.mkdir(parents=True, exist_ok=True)
        self.templates: Dict[str, PromptTemplate] = {}
        self._load_all()

    def _load_all(self) -> None:
        """Load all templates from library."""
        for filepath in self.library_path.glob("*.json"):
            with open(filepath, 'r') as f:
                data = json.load(f)
                template = PromptTemplate.from_dict(data)
                self.templates[template.name] = template

    def add(self, template: PromptTemplate) -> None:
        """Add a template to the library."""
        self.templates[template.name] = template
        template.save(str(self.library_path))

    def get(self, name: str, version: Optional[str] = None) -> PromptTemplate:
        """Get a template by name."""
        if version:
            return PromptTemplate.load(name, version, str(self.library_path))
        return self.templates.get(name) or PromptTemplate.load(name, directory=str(self.library_path))

    def list(self) -> List[Dict[str, Any]]:
        """List all templates."""
        return [
            {
                "name": t.name,
                "version": t.version,
                "created_at": t.created_at,
                "parent": t.parent
            }
            for t in self.templates.values()
        ]

    def create_from_yaml(self, yaml_path: str) -> PromptTemplate:
        """Create template from YAML configuration."""
        with open(yaml_path, 'r') as f:
            config = yaml.safe_load(f)

        template = PromptTemplate(
            name=config["name"],
            template=config["template"],
            version=config.get("version", "1.0.0"),
            metadata=config.get("metadata", {}),
            parent=config.get("parent")
        )

        self.add(template)
        return template


# Example templates
EXAMPLE_TEMPLATES = {
    "marketing_email": """You are a marketing copywriter for {company}.

Write a compelling email for {product} targeting {audience}.

Requirements:
- Tone: {tone}
- Length: {length} words
- Include a clear call-to-action
- Use the brand voice: {brand_voice}

Product Details:
{product_details}

Email:""",

    "seo_optimizer": """Analyze and optimize the following content for SEO.

Target Keywords: {keywords}
Target Audience: {audience}

Original Content:
{content}

Provide:
1. Keyword density analysis
2. Readability score
3. Recommended improvements
4. Optimized version

Analysis:""",

    "lead_scorer": """You are a lead scoring expert for B2B SaaS.

Evaluate this lead based on the following criteria:

Lead Information:
- Company: {company}
- Industry: {industry}
- Company Size: {company_size}
- Job Title: {job_title}
- Engagement Level: {engagement_level}

Scoring Criteria (0-100):
1. Fit Score (company size, industry match)
2. Interest Score (engagement, intent signals)
3. Urgency Score (buying timeline indicators)

Provide:
- Overall Score (0-100)
- Category: Hot/Warm/Cold
- Recommended Action
- Reasoning

Analysis:"""
}


def create_default_library() -> PromptLibrary:
    """Create a library with example templates."""
    library = PromptLibrary()

    for name, template_text in EXAMPLE_TEMPLATES.items():
        template = PromptTemplate(
            name=name,
            template=template_text,
            version="1.0.0",
            metadata={
                "author": "Tech Innovation Hub",
                "category": "marketing",
                "tags": ["production", "tested"]
            }
        )
        library.add(template)

    return library


# Example usage
if __name__ == "__main__":
    # Create library with examples
    library = create_default_library()

    # List all templates
    print("📚 Available Templates:")
    for t in library.list():
        print(f"  - {t['name']} (v{t['version']})")

    print("\n" + "="*60 + "\n")

    # Use marketing email template
    template = library.get("marketing_email")

    email = template.render(
        company="Tech Innovation Hub",
        product="AI Engineering Masterclass",
        audience="Data Scientists and ML Engineers",
        tone="professional yet approachable",
        length="150",
        brand_voice="innovative, data-driven, practical",
        product_details="A comprehensive course covering LLMs, RAG, and Multi-Agent Systems"
    )

    print("📧 Generated Email:")
    print(email)

    print("\n" + "="*60 + "\n")

    # Create a custom template
    custom_template = PromptTemplate(
        name="campaign_analyzer",
        template="""Analyze this marketing campaign performance:

Campaign: {campaign_name}
Duration: {duration}
Metrics:
- Impressions: {impressions}
- Clicks: {clicks}
- Conversions: {conversions}
- Revenue: ${revenue}

Provide insights and recommendations.""",
        version="1.0.0",
        metadata={"author": "Marketing Team", "category": "analytics"}
    )

    library.add(custom_template)
    print(f"✅ Added custom template: {custom_template.name}")
