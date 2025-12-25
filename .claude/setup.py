#!/usr/bin/env python3
"""
setup.py for tech-hub-skills

Legacy setup.py for backward compatibility with older pip versions.
Modern configuration is in pyproject.toml.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="tech-hub-skills",
    version="1.2.0",
    description="110+ production-ready AI agent skills for Claude Code and GitHub Copilot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="6ogo",
    url="https://github.com/6ogo/Tech-Skills",
    license="MIT",
    packages=find_packages(include=["tech_hub_skills", "tech_hub_skills.*"]),
    package_data={
        "tech_hub_skills": ["skills/*.md", "roles/**/*.md"],
    },
    include_package_data=True,
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "tech-hub-skills=tech_hub_skills.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=[
        "claude",
        "claude-code",
        "github-copilot",
        "copilot",
        "ai-agents",
        "skills",
        "llm",
        "ai-engineer",
        "data-engineer",
        "security",
        "enterprise",
        "vscode",
    ],
)
