#!/usr/bin/env python3
"""Tech Hub Skills CLI - Install AI agent skills for Claude Code and GitHub Copilot."""

import argparse
import shutil
import sys
from pathlib import Path
from .copilot_integration import install_copilot_instructions, get_available_roles

__version__ = "1.0.0"

BANNER = """

╔═══════════════════════════════════════════════════════════╗
║         TECH HUB SKILLS - AI Agent Skills for Claude      ║
║                  110+ Production-Ready Skills             ║
╚═══════════════════════════════════════════════════════════╝
"""


def get_package_dir() -> Path:
    """Get the directory containing the skills."""
    return Path(__file__).parent


def install(global_install: bool = False, force: bool = False, copilot: bool = False) -> None:
    """Install skills to project or global directory."""
    print(BANNER)

    package_dir = get_package_dir()
    skills_src = package_dir / "skills"
    roles_src = package_dir / "roles"

    if global_install:
        target_dir = Path.home() / ".claude"
    else:
        target_dir = Path.cwd() / ".claude"

    print(f"\n📦 Installing Tech Hub Skills to: {target_dir}")

    # Create target directory
    target_dir.mkdir(parents=True, exist_ok=True)

    # Copy skills
    skills_dest = target_dir / "skills"
    if skills_src.exists():
        if skills_dest.exists() and not force:
            print(f"  ⚠️  Skills already exist. Use --force to overwrite.")
        else:
            if skills_dest.exists():
                shutil.rmtree(skills_dest)
            shutil.copytree(skills_src, skills_dest)
            print("  ✓ Skills copied")

    # Copy roles
    roles_dest = target_dir / "roles"
    if roles_src.exists():
        if roles_dest.exists() and not force:
            print(f"  ⚠️  Roles already exist. Use --force to overwrite.")
        else:
            if roles_dest.exists():
                shutil.rmtree(roles_dest)
            shutil.copytree(roles_src, roles_dest)
            print("  ✓ Roles copied")

    # Install GitHub Copilot instructions if requested
    if copilot:
        print("\n🤖 Installing GitHub Copilot integration...")
        project_dir = Path.cwd()
        install_copilot_instructions(
            project_dir=project_dir,
            skills_dir=skills_src,
            roles_dir=roles_src,
            force=force
        )

    # Count installed
    skill_count = len(list(skills_dest.glob("*.md"))) if skills_dest.exists() else 0

    print(f"\n✅ Installation complete!")
    print(f"   Location: {target_dir}")
    print(f"   Skills: {skill_count} role files")
    print(f"   Roles: 16+ specialized agents")

    if copilot:
        print(f"   Copilot: .github/copilot-instructions.md")

    print("\n📝 Next Steps:")
    if copilot:
        print("   GitHub Copilot:")
        print("   1. Open VSCode with GitHub Copilot enabled")
        print("   2. Copilot will automatically use the instructions")
        print("   3. Try: // Using AI Engineer approach for RAG pipeline")
        print("")
    print("   Claude Code:")
    print("   1. Open Claude Code in your project")
    print("   2. Use @orchestrator to start")
    print("   3. Or invoke: @ai-engineer, @security-architect, etc.")

    print("\n💡 Example:")
    if copilot:
        print('   Copilot: // Apply Security Architect best practices')
    print('   Claude: @orchestrator "Build a customer churn prediction model"')


def init(enterprise: bool = False) -> None:
    """Initialize project with guided setup."""
    print(BANNER)

    if enterprise:
        print("\n🏢 ENTERPRISE MODE")
        print("   Mandatory: Security Architect + Data Governance")
        print("\n   Use in Claude Code:")
        print('   @project-starter --enterprise "Your project description"')
    else:
        print("\n📦 Standard Mode")
        print("\n   Use in Claude Code:")
        print('   @project-starter "Your project description"')


def list_skills() -> None:
    """List all available roles and skills."""
    print(BANNER)

    roles = [
        ("Orchestrator", "Routes all", "Project coordination"),
        ("AI Engineer", "8", "LLMs, RAG, Agents"),
        ("Data Engineer", "9", "Pipelines, Lakehouse"),
        ("ML Engineer", "9", "Training, Serving, MLOps"),
        ("Data Scientist", "8", "Analytics, Modeling"),
        ("Security Architect", "7", "PII, IAM, Compliance"),
        ("System Design", "8", "Architecture, Scalability"),
        ("Platform Engineer", "6", "IDP, SLOs"),
        ("Data Governance", "6", "Catalog, Lineage, Quality"),
        ("DevOps", "9", "CI/CD, Containers, IaC"),
        ("MLOps", "9", "Experiments, Registry"),
        ("FinOps", "8", "Cost Optimization"),
        ("Azure", "12", "Azure Services"),
        ("Code Review", "5", "PR Automation, Quality Gates"),
        ("Product Designer", "6", "Requirements, UX"),
    ]

    print("\nAvailable Roles:\n")
    print("  Role                 Skills   Focus")
    print("  " + "─" * 50)

    for name, skills, focus in roles:
        print(f"  {name:<20} {skills:<8} {focus}")

    print("\n  Total: 110+ skills across 16+ roles")


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Tech Hub Skills - AI Agent Skills for Claude Code & GitHub Copilot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  tech-hub-skills install                  Install to current project (Claude Code)
  tech-hub-skills install --copilot        Install with GitHub Copilot integration
  tech-hub-skills install --global         Install globally
  tech-hub-skills init --enterprise        Enterprise mode setup
  tech-hub-skills list                     List all roles
        """
    )

    parser.add_argument(
        "--version", "-v",
        action="version",
        version=f"tech-hub-skills {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Install command
    install_parser = subparsers.add_parser("install", help="Install skills")
    install_parser.add_argument(
        "--global", "-g",
        dest="global_install",
        action="store_true",
        help="Install globally to ~/.claude"
    )
    install_parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Force overwrite existing installation"
    )
    install_parser.add_argument(
        "--copilot", "-c",
        action="store_true",
        help="Also install GitHub Copilot instructions (.github/copilot-instructions.md)"
    )

    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize project")
    init_parser.add_argument(
        "--enterprise", "-E",
        action="store_true",
        help="Enterprise mode with security + governance"
    )

    # List command
    subparsers.add_parser("list", help="List available roles")

    args = parser.parse_args()

    if args.command == "install":
        install(
            global_install=args.global_install,
            force=args.force,
            copilot=args.copilot
        )
    elif args.command == "init":
        init(enterprise=args.enterprise)
    elif args.command == "list":
        list_skills()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
