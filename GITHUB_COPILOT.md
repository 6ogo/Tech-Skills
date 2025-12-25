# GitHub Copilot Integration

Tech Hub Skills works with **GitHub Copilot** in VSCode, providing Copilot with 110+ production-ready AI agent skills.

## Quick Start

```bash
# Install with Copilot support
npx tech-hub-skills install --copilot

# Or with Python
pip install tech-hub-skills
tech-hub-skills install --copilot
```

This creates `.github/copilot-instructions.md` that Copilot automatically reads.

## How It Works

GitHub Copilot reads workspace instructions from `.github/copilot-instructions.md`. Once installed, Copilot applies expert knowledge automatically to all code suggestions.

### Expert Roles Available

- **AI Engineer** - LLMs, RAG, Agents, Guardrails
- **Data Engineer** - Lakehouse, ETL, Streaming
- **ML Engineer** - Training, Serving, MLOps
- **Security Architect** - PII, IAM, Compliance
- **DevOps** - CI/CD, Containers, IaC
- **System Design** - Architecture, Scalability
- Plus 10 more specialized roles

## Usage Examples

### Request Expertise in Comments

```python
# Using AI Engineer approach for RAG pipeline
def build_rag_pipeline():
    # Copilot suggests: vector stores, embeddings, chunking
    pass

# Apply Security Architect best practices
def process_user_data(user_input):
    # Copilot adds: validation, sanitization, PII scanning
    pass
```

### Combine Multiple Roles

```typescript
/* DevOps + FinOps: optimize CI/CD costs */
const cicdConfig = {
  // Copilot suggests cost-optimized configuration
};
```

### Implicit Guidance

Even without comments, Copilot applies:
- Security best practices (no hardcoded secrets, input validation)
- Proper error handling
- Performance optimization
- Quality standards

## Copilot vs Claude Code

Both tools work together:

| Feature | GitHub Copilot | Claude Code |
|---------|----------------|-------------|
| **Usage** | Inline suggestions | `@mention` roles |
| **Mode** | Automatic | Interactive |
| **Best For** | Writing code | Complex tasks, architecture |

### Combined Workflow

```bash
# 1. Install for both
npx tech-hub-skills install --copilot

# 2. Use Copilot while coding (automatic)
# 3. Use Claude Code for complex tasks
@orchestrator "Design a data lakehouse architecture"
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
