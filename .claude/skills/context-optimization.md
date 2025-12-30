# Context Optimization Skills

Expert techniques for minimizing token usage while maximizing effectiveness.

## 🎯 Core Principle

```
FETCH ONLY WHAT YOU NEED
ACTIVATE ONLY WHEN NEEDED
DEACTIVATE IMMEDIATELY WHEN DONE
```

## 🎯 Trigger Keywords

- "save tokens", "reduce context", "optimize"
- "too much data", "context limit", "token budget"
- "lazy loading", "minimal fetch", "selective"
- "efficiency", "cost reduction"

---

## ctx-01: Lazy Loading Patterns

### File Reading

```yaml
# ❌ WRONG: Load entire file
read_file("/src/app.py")  # 2000 tokens

# ✅ RIGHT: Load outline first
view_file_outline("/src/app.py")  # 50 tokens
# Then only load relevant section
read_file("/src/app.py", lines=45-60)  # 100 tokens

# SAVINGS: 90%
```

### Code Navigation

```yaml
# ❌ WRONG: Read all files matching pattern
find_and_read("*.py")  # 50,000 tokens

# ✅ RIGHT: Search for specific symbol
grep_search("def process_user")  # 200 tokens
view_code_item("/src/users.py", "process_user")  # 100 tokens

# SAVINGS: 99%
```

### Directory Exploration

```yaml
# ❌ WRONG: Recursive list all files
list_all_recursive("/project")  # 5,000 tokens

# ✅ RIGHT: Start shallow, go deeper only if needed
list_dir("/project")  # 100 tokens
# Identify relevant subdirectory
list_dir("/project/src")  # 50 tokens

# SAVINGS: 95%
```

---

## ctx-02: Database Query Optimization

### Column Selection

```sql
-- ❌ WRONG: Select all columns
SELECT * FROM users LIMIT 100;  -- 5,000 tokens

-- ✅ RIGHT: Select only needed columns
SELECT id, name, email FROM users LIMIT 100;  -- 500 tokens

-- SAVINGS: 90%
```

### Exploration Queries

```sql
-- ✅ Always start with structure
DESCRIBE users;  -- Schema first
SELECT COUNT(*) FROM users;  -- Size check
SELECT * FROM users LIMIT 5;  -- Sample

-- Only fetch more if needed
```

### Aggregation Over Raw Data

```sql
-- ❌ WRONG: Fetch all rows to count in code
SELECT * FROM orders;  -- 100,000 tokens

-- ✅ RIGHT: Let database aggregate
SELECT status, COUNT(*) FROM orders GROUP BY status;  -- 50 tokens

-- SAVINGS: 99.9%
```

---

## ctx-03: API Response Optimization

### Pagination

```yaml
# ❌ WRONG: Fetch all at once
GET /api/users  # 10,000 items = 50,000 tokens

# ✅ RIGHT: Paginate
GET /api/users?page=1&per_page=10  # 500 tokens
# Only fetch more pages if needed
```

### Field Selection

```yaml
# ❌ WRONG: Full response
GET /api/users/123
# Returns: all 50 fields = 2,000 tokens

# ✅ RIGHT: Sparse fields
GET /api/users/123?fields=id,name,email
# Returns: 3 fields = 100 tokens

# SAVINGS: 95%
```

### GraphQL Advantage

```graphql
# Only request what you need
query {
  user(id: 123) {
    name
    email
    # Skip: address, history, preferences, etc.
  }
}
```

---

## ctx-04: MCP Server Efficiency

### Activation Strategy

```yaml
# ❌ WRONG: Activate everything upfront
activate: [github, filesystem, postgres, slack, fetch]

# ✅ RIGHT: Activate on-demand
1. Identify task requirements
2. Activate ONLY needed server
3. Complete task
4. Deactivate immediately
```

### Minimal Fetch from GitHub

```yaml
# ❌ WRONG: Fetch full repo
github.get_repo_contents(owner, repo, "")  # Entire repo

# ✅ RIGHT: Targeted fetch
github.search_code("function_name repo:owner/repo")  # Specific
github.get_file_contents(owner, repo, "src/specific_file.py")  # One file
```

### Deactivation Discipline

```yaml
task_execution:
  - start: note active MCPs
  - execute: use minimal queries
  - complete: verify task done
  - cleanup: deactivate ALL used MCPs
  - verify: active MCPs == 0 (if task complete)
```

---

## ctx-05: Caching Strategies

### What to Cache

```yaml
cache_candidates:
  high_value:
    - File outlines (tree structure)
    - Database schemas
    - API response structures
    - Frequently accessed configs

  medium_value:
    - Search results (if queries repeat)
    - Code symbol locations
    - Directory listings

  low_value:
    - Dynamic data (avoid caching)
    - Time-sensitive info
    - User-specific data
```

### Cache Invalidation

```yaml
invalidate_when:
  - File modified (timestamp changed)
  - Explicit cache clear requested
  - Session ended
  - TTL expired (configurable)
```

---

## ctx-06: Progressive Disclosure Pattern

### For Large Documents

```yaml
step_1:
  action: "Get document outline/headers"
  tokens: 50

step_2:
  action: "Identify relevant section from outline"
  tokens: 0 (reasoning)

step_3:
  action: "Fetch only that section"
  tokens: 200
# Alternative: Fetch entire document
# tokens: 5000
# SAVINGS: 95%
```

### For Large Codebases

```yaml
step_1:
  action: "List top-level directories"
  tokens: 50

step_2:
  action: "Based on task, identify relevant dirs"
  tokens: 0

step_3:
  action: "List files in relevant dir only"
  tokens: 30

step_4:
  action: "Get outline of relevant file"
  tokens: 50

step_5:
  action: "Read specific function/class"
  tokens: 100
# Total: 230 tokens
# Full codebase read: 500,000 tokens
# SAVINGS: 99.95%
```

---

## Integration with Agents

Every agent should follow these patterns:

```yaml
agent_context_rules:
  before_fetch:
    - "Do I really need this data?"
    - "Can I get a summary instead?"
    - "Can I filter/limit the request?"

  during_fetch:
    - Use outline/structure first
    - Select specific fields/columns
    - Limit rows/items
    - Paginate large results

  after_fetch:
    - Deactivate MCPs immediately
    - Note what was cached
    - Track tokens used
```

---

## Metrics & Monitoring

Track these to optimize further:

```yaml
metrics:
  tokens_per_task:
    good: "< 5,000"
    acceptable: "5,000 - 20,000"
    review: "> 20,000"

  mcp_activation_time:
    ideal: "< 1 minute"
    review: "> 5 minutes"

  cache_hit_rate:
    target: "> 40%"

  optimization_opportunities:
    - SELECT * queries
    - Full file reads
    - Unpaginated API calls
    - Idle MCP servers
```
