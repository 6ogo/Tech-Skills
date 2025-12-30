# MCP Command

Route to the MCP Manager Agent for server management and context optimization.

## Usage

```
/mcp [your request]
```

## Examples

```
/mcp activate github server
/mcp status - show active servers
/mcp deactivate all
/mcp optimize context for this task
```

## What Happens

1. **MCP Manager** receives your request
2. **Analyzes** which servers are needed
3. **Activates** only required servers
4. **Monitors** usage and token consumption
5. **Deactivates** when task completes

## Core Principle

```
⚡ ACTIVATE ONLY WHAT YOU NEED
📉 FETCH MINIMAL DATA
🛑 DEACTIVATE IMMEDIATELY WHEN DONE
💰 SAVE TOKENS AND COSTS
```

## Available MCP Servers

| Server           | Purpose            | Cost    |
| ---------------- | ------------------ | ------- |
| **github**       | Repos, issues, PRs | Low     |
| **filesystem**   | Read/write files   | Minimal |
| **postgres**     | Database queries   | Medium  |
| **fetch**        | Web content        | Medium  |
| **brave-search** | Web search         | Low     |
| **slack**        | Team messaging     | Low     |
| **puppeteer**    | Browser automation | High    |

## Optimization Strategies

| Data Type | Strategy                      | Token Savings |
| --------- | ----------------------------- | ------------- |
| Files     | Outline first, then sections  | 60-80%        |
| Database  | SELECT specific columns only  | 70-90%        |
| APIs      | Paginate, filter, cache       | 50-70%        |
| Code      | Symbol search, not full files | 80%           |

## Auto-Behaviors

- MCPs auto-deactivate after task completion
- Minimal data fetched by default
- Caching enabled for repeated queries
- Token usage tracked and reported
