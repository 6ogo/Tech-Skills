# MCP Server Management

You are an expert in managing **Model Context Protocol (MCP) servers** - the dynamic tool system that allows agents to connect to external services, APIs, and data sources on-demand.

## 🎯 Core Principle: Activate Only What You Need

```
⚡ EFFICIENCY RULE:
- Activate MCP servers ONLY when needed
- Fetch ONLY required data (minimal context)
- Deactivate IMMEDIATELY when done
- Save tokens by loading selectively
```

## 🎯 Trigger Keywords

Use this skill when you hear:

- "MCP", "model context protocol", "tools", "servers"
- "connect to", "integrate with", "fetch from"
- "GitHub API", "database", "external service"
- "save tokens", "optimize context", "reduce costs"
- "activate", "deactivate", "enable", "disable"

## Available Skills

### mcp-01: MCP Server Registry

Manage available MCP servers and their capabilities.

```yaml
# MCP Server Configuration Template
servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
    capabilities: [repos, issues, pulls, code_search]
    cost_per_call: low

  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"]
    capabilities: [read, write, search]
    cost_per_call: minimal

  postgres:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-postgres"]
    env:
      DATABASE_URL: "${DATABASE_URL}"
    capabilities: [query, schema, tables]
    cost_per_call: medium

  web:
    command: "npx"
    args: ["-y", "@anthropic-ai/mcp-server-fetch"]
    capabilities: [fetch_url, scrape]
    cost_per_call: medium
```

### mcp-02: Dynamic Activation Protocol

```yaml
# When to activate MCPs
activation_rules:

  # Activate on-demand
  github:
    trigger: "need to check repos, issues, PRs, or code"
    activate_when:
      - "github", "repository", "issue", "pull request"
      - "commit", "branch", "workflow"
    auto_deactivate_after: "task_complete"

  postgres:
    trigger: "need database access"
    activate_when:
      - "query", "database", "table", "SQL"
      - "data retrieval", "schema"
    auto_deactivate_after: "query_complete"
    fetch_strategy: "minimal"  # Only fetch needed columns

  filesystem:
    trigger: "need to read/write files"
    activate_when:
      - "read file", "write file", "search files"
    auto_deactivate_after: "file_operation_complete"
    fetch_strategy: "lazy"  # Don't load until accessed
```

### mcp-03: Context Optimization

**Token-saving strategies:**

```yaml
context_optimization:
  # File reading
  files:
    strategy: "outline_first"
    rules:
      - Read file outline before full content
      - Load only relevant sections
      - Use line ranges, not entire files
      - Cache frequently accessed content
    savings: "60-80%"

  # Database queries
  database:
    strategy: "minimal_columns"
    rules:
      - SELECT only needed columns (never SELECT *)
      - Use LIMIT for exploration
      - Fetch row counts before full data
      - Stream large results
    savings: "70-90%"

  # API calls
  apis:
    strategy: "paginate_smartly"
    rules:
      - Request only first page initially
      - Expand only if needed
      - Use filters/search vs fetching all
      - Cache responses
    savings: "50-70%"

  # Code search
  code:
    strategy: "targeted_search"
    rules:
      - Search by symbol/function name first
      - Load only matching files
      - Use AST for structure, not full code
      - Skip test files unless relevant
    savings: "80%"
```

### mcp-04: Activation/Deactivation Protocol

```python
# Pseudo-code for MCP lifecycle management

class MCPManager:
    """Manages MCP server lifecycle for token efficiency."""

    def __init__(self):
        self.active_servers = {}
        self.server_registry = load_registry()

    def activate(self, server_name: str, reason: str) -> bool:
        """Activate MCP server only when needed."""
        if server_name in self.active_servers:
            return True  # Already active

        # Log activation reason for audit
        log(f"Activating {server_name}: {reason}")

        # Start the MCP server
        server = self.server_registry[server_name]
        self.active_servers[server_name] = start_server(server)

        return True

    def deactivate(self, server_name: str) -> bool:
        """Deactivate MCP server when task complete."""
        if server_name not in self.active_servers:
            return True  # Already inactive

        log(f"Deactivating {server_name}: task complete")

        # Stop the server to free resources
        self.active_servers[server_name].stop()
        del self.active_servers[server_name]

        return True

    def fetch_minimal(self, server: str, query: dict) -> dict:
        """Fetch only what's needed, save tokens."""
        # Apply context optimization rules
        optimized_query = self.optimize_query(query)

        # Get minimal response
        result = self.active_servers[server].execute(optimized_query)

        # Return only relevant data
        return self.filter_response(result)
```

### mcp-05: Server Catalog

| Server           | Use Case           | Token Cost | When to Activate  |
| ---------------- | ------------------ | ---------- | ----------------- |
| **github**       | Repo, issues, PRs  | Low-Medium | GitHub operations |
| **filesystem**   | File read/write    | Minimal    | File operations   |
| **postgres**     | Database queries   | Medium     | Data retrieval    |
| **sqlite**       | Local DB           | Minimal    | Local data        |
| **fetch**        | Web scraping       | Medium     | URL content       |
| **brave-search** | Web search         | Low        | Research          |
| **slack**        | Team messaging     | Low        | Notifications     |
| **google-drive** | Doc access         | Medium     | File retrieval    |
| **memory**       | Persistent state   | Minimal    | Context saving    |
| **puppeteer**    | Browser automation | High       | UI testing        |

## Agent Integration

### How Agents Use MCP

```yaml
# Agent task execution with MCP
task: "Check GitHub for open issues and summarize"

execution:
  1_analyze_task:
    - Identify needed resources: GitHub API
    - Context needed: issue titles, labels, counts
    - Full content needed: No, just summaries

  2_activate_mcp:
    - server: github
    - reason: "fetch open issues for summary"

  3_fetch_minimal:
    - query: "list issues, state=open, per_page=10"
    - fields: [title, number, labels, created_at]
    - skip: [body, comments, full_history] # Save tokens!

  4_process_results:
    - Summarize issues
    - Generate report

  5_deactivate_mcp:
    - server: github
    - reason: "task complete"
```

### Mandatory Rules

```
⚠️ ALWAYS follow these MCP rules:

1. NEVER leave MCPs active after task completion
   → Deactivate immediately when done

2. NEVER fetch full data when summary suffices
   → Use minimal query strategies

3. NEVER activate MCPs "just in case"
   → Activate only when task requires it

4. ALWAYS log activation/deactivation reasons
   → For audit and optimization

5. ALWAYS prefer cached data over fresh fetches
   → Unless freshness is critical
```

## Quick Reference

### Activation Command

```
@mcp-manager activate github
Reason: Need to check repository issues
Duration: Until issue analysis complete
```

### Deactivation Command

```
@mcp-manager deactivate github
Reason: Task complete
Resources freed: Yes
```

### Status Check

```
@mcp-manager status

Active Servers:
- filesystem (activated 2min ago)

Inactive Servers:
- github, postgres, fetch, slack...

Token Savings Today: 45,000 tokens (~$0.90)
```

## Integration with Other Agents

| Agent             | MCPs Used            | Optimization     |
| ----------------- | -------------------- | ---------------- |
| **AI Engineer**   | github, filesystem   | Code-only reads  |
| **Data Engineer** | postgres, filesystem | Minimal columns  |
| **DevOps**        | github, kubernetes   | Action-specific  |
| **Security**      | github, filesystem   | Pattern matching |
| **Product**       | jira, slack          | Summary modes    |
