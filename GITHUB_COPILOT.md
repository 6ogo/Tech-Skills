# GitHub Copilot Integration

Tech Hub Skills works with **GitHub Copilot** in VSCode, providing Copilot with 200+ production-ready AI agent skills.

## Quick Start

```bash
# Install with Copilot support
npx tech-hub-skills install --copilot

# Or with Python
pip install tech-hub-skills
tech-hub-skills install --copilot
```

This creates `.github/copilot-instructions.md` that Copilot automatically reads.

## 🧠 Agent Architecture (v2.2.1)

Copilot uses the same hierarchical agent system as Claude Code:

1.  **Orchestrator Agent** - The entry point that brainstorms and plans.
2.  **5 Lead Agents** - Domain experts (AI, Platform, Security, Data, Product).
3.  **25 Specialist Agents** - Deep experts (e.g., AI Engineer, SRE, MLOps) loaded by Leads.

## Usage Examples

### Request Expertise in Comments

```python
# Using AI Engineer approach for RAG pipeline
def build_rag_system():
    # Copilot suggests: adaptive chunking, hybrid search, etc.
    pass

# Apply Security Architect best practices
def handle_user_upload(file_data):
    # Copilot adds: PII scan, malware check, sanitization
    pass
```

### Hierarchical Workflow (Combined with Claude Code)

Both tools work together seamlessly:

| Feature      | GitHub Copilot            | Claude Code                     |
| ------------ | ------------------------- | ------------------------------- |
| **Usage**    | Inline suggestions        | `/mention` roles or `/commands` |
| **Logic**    | Automatic (Context-based) | Interactive (Task-based)        |
| **Best For** | Real-time coding          | Architecture, complex refactors |

### Combined Workflow

```bash
# 1. Install for both
npx tech-hub-skills install --copilot

# 2. Use Claude Code for the high-level plan
/orchestrator "Design a multi-cloud lakehouse architecture"

# 3. Use Copilot to implement the details (automatic expert guidance)
```

## Troubleshooting

**Copilot not using instructions?**

- Verify `.github/copilot-instructions.md` exists
- Reload VSCode: `Cmd/Ctrl + Shift + P` → "Reload Window"
- Check Copilot is enabled in VSCode status bar

**Want to update?**

```bash
npx tech-hub-skills install --copilot --force
```

**Remove Copilot integration only:**

```bash
rm .github/copilot-instructions.md
```

## Learn More

- **Main Docs**: [README.md](README.md)
- **GitHub Copilot**: https://docs.github.com/copilot
