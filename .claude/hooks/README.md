# Claude Code Safety Guardrails

Comprehensive damage control system for Claude Code to prevent accidental file deletions, database drops, and other destructive operations.

## 🛡️ Overview

This safety system implements **defense-in-depth protection** through Pre-Tool-Use hooks that intercept Claude Code tool calls before execution. It provides:

- ✅ Protection against accidental file/directory deletion
- ✅ Database operation safeguards (prevents unqualified DELETEs, DROPs)
- ✅ Credential and secret file protection
- ✅ Read-only system file enforcement
- ✅ Automatic backup creation before destructive operations
- ✅ Comprehensive audit logging
- ✅ User confirmation prompts for risky operations

## 📁 System Components

```
.claude/hooks/
├── README.md                 # This file
├── patterns.yaml            # Safety configuration
├── bash-safety-hook.py      # Bash tool protection
├── edit-safety-hook.py      # Edit tool protection
├── write-safety-hook.py     # Write tool protection
└── safety.log              # Audit log (auto-created)

.claude/backups/             # Automatic backups (auto-created)
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install pyyaml
```

### 2. Verify Installation

```bash
# Check hooks are executable
ls -la .claude/hooks/*.py

# Test a pattern (should block)
echo '{"tool": {"name": "Bash", "params": {"command": "rm -rf /"}}}' | python3 .claude/hooks/bash-safety-hook.py
```

### 3. Configure Settings

The hooks are registered in `.claude/settings.local.json`. They will automatically intercept tool calls.

## 🔒 Protection Levels

### Zero Access Paths (Complete Prohibition)

No operations allowed - protects sensitive files:

- `~/.ssh/*` - SSH keys
- `~/.aws/*` - AWS credentials
- `~/.gnupg/*` - GPG keys
- `*.key`, `*.pem` - Private keys
- `**/credentials.json` - Service account files

**Result**: 🚫 BLOCKED immediately, no user prompt

### Read-Only Paths

Allow reading but block modifications:

- `/etc/*` - System configuration files
- `~/.bashrc`, `~/.zshrc` - Shell configs
- `package-lock.json` - Dependency lock files
- `/usr/*`, `/bin/*` - System binaries

**Result**: 🚫 BLOCKED immediately for write/edit/delete

### No-Delete Paths

Allow read and write but block deletion:

- `.claude/hooks/*` - Safety system itself
- `*.sql`, `*.db`, `*.sqlite*` - Database files
- `.git/*` - Git repository
- `docker-compose.yml`, `Dockerfile` - Infrastructure files

**Result**: 🚫 BLOCKED for delete operations only

## ⚠️ Dangerous Command Patterns

### Automatically Blocked (No Confirmation)

- `rm -rf /` - Delete from root
- `DELETE FROM table;` - Unqualified SQL DELETE
- Other catastrophic operations

**Result**: 🚫 BLOCKED with error message

### Requires User Confirmation

- `rm -rf *` - Recursive delete with wildcards
- `DROP DATABASE/TABLE` - Database drops
- `git push --force` - Force push
- `docker system prune -a` - Remove all Docker data
- `chmod 777` - Insecure permissions
- And many more...

**Result**: ⚠️ User prompted for confirmation

## 📊 Safety Logs

All operations are logged to `.claude/hooks/safety.log` in JSON format:

```json
{
  "timestamp": "2026-01-05T10:30:00",
  "type": "BLOCKED_PATH",
  "tool": "Bash",
  "command": "rm -rf ~/.ssh",
  "action": "block",
  "message": "BLOCKED: Access to protected path"
}
```

### Log Event Types

- `ALLOWED` - Operation permitted
- `BLOCKED_PATH` - Blocked due to path protection
- `BLOCKED_PATTERN` - Blocked due to dangerous pattern
- `BLOCKED_CONTENT` - Blocked due to dangerous content
- `ASK_USER` - User confirmation requested
- `BACKUP_CREATED` - Backup created before operation
- `OVERWRITE` - File overwritten (after checks passed)
- `CREATE` - New file created

### View Recent Logs

```bash
# Last 20 events
tail -20 .claude/hooks/safety.log

# Count blocked operations
grep "BLOCKED" .claude/hooks/safety.log | wc -l

# View all user confirmations
grep "ASK_USER" .claude/hooks/safety.log
```

## ⚙️ Configuration

### patterns.yaml Structure

```yaml
# Protection Levels
zeroAccessPaths:
  - "path/pattern"

readOnlyPaths:
  - "path/pattern"

noDeletePaths:
  - "path/pattern"

# Command Patterns
dangerousBashPatterns:
  - pattern: 'regex-pattern'
    description: "Human readable description"
    action: "ask"  # or "block" or "skip"
    message: "Warning message to user"

# Settings
safetySettings:
  enableLogging: true
  logFile: ".claude/hooks/safety.log"
  backupBeforeDestructive: true
  backupDirectory: ".claude/backups/"
```

### Adding Custom Protections

#### Protect a Specific Directory

```yaml
noDeletePaths:
  - "my-important-data/**/*"
```

#### Block a Custom Command

```yaml
dangerousBashPatterns:
  - pattern: 'npm\s+publish'
    description: "NPM publish"
    action: "ask"
    message: "⚠️ About to publish to NPM. Are you sure?"
```

#### Add Read-Only Config File

```yaml
readOnlyPaths:
  - "config/production.yml"
```

## 🔧 Hook Exit Codes

Hooks communicate through standardized exit codes:

- **0** = Allow operation (or JSON for user prompt)
- **2** = Block operation (error sent to Claude)
- **Other** = Warning (operation proceeds)

## 🧪 Testing

### Test Bash Hook

```bash
# Should block
echo '{"tool": {"name": "Bash", "params": {"command": "rm -rf *.db"}}}' | \
  python3 .claude/hooks/bash-safety-hook.py

# Should ask
echo '{"tool": {"name": "Bash", "params": {"command": "git push --force"}}}' | \
  python3 .claude/hooks/bash-safety-hook.py

# Should allow
echo '{"tool": {"name": "Bash", "params": {"command": "ls -la"}}}' | \
  python3 .claude/hooks/bash-safety-hook.py
```

### Test Edit Hook

```bash
# Should block (SSH key)
echo '{"tool": {"name": "Edit", "params": {"file_path": "~/.ssh/id_rsa"}}}' | \
  python3 .claude/hooks/edit-safety-hook.py

# Should allow (regular file)
echo '{"tool": {"name": "Edit", "params": {"file_path": "test.txt"}}}' | \
  python3 .claude/hooks/edit-safety-hook.py
```

### Test Write Hook

```bash
# Should block (system file)
echo '{"tool": {"name": "Write", "params": {"file_path": "/etc/hosts"}}}' | \
  python3 .claude/hooks/write-safety-hook.py

# Should ask (overwriting package.json)
echo '{"tool": {"name": "Write", "params": {"file_path": "package.json"}}}' | \
  python3 .claude/hooks/write-safety-hook.py
```

## 🔍 Troubleshooting

### Hooks Not Triggering

1. **Check registration**: Verify hooks in `.claude/settings.local.json`
2. **Check permissions**: Run `chmod +x .claude/hooks/*.py`
3. **Check dependencies**: Run `pip install pyyaml`
4. **Check logs**: Look for errors in safety.log

### Too Many False Positives

1. Review `patterns.yaml` for overly broad patterns
2. Change `action: "ask"` to `action: "skip"` for safe patterns
3. Add exceptions to patterns for specific safe cases
4. Use more specific regex patterns

### Pattern Not Matching

1. Test regex with Python: `re.search(pattern, command)`
2. Check path expansion: `~` vs absolute paths
3. Verify glob patterns use `*` not regex syntax
4. Check case sensitivity (patterns use `re.IGNORECASE`)

## 🎯 Best Practices

1. **Start Conservative**: Begin with strict protections, relax as needed
2. **Log Everything**: Keep `enableLogging: true` for audit trails
3. **Enable Backups**: Set `backupBeforeDestructive: true`
4. **Review Logs Weekly**: Check for patterns of risky operations
5. **Test Changes**: Test pattern changes before relying on them
6. **Document Custom Rules**: Add comments in patterns.yaml
7. **Version Control**: Commit patterns.yaml to track changes

## 🚨 Emergency Override

If you need to temporarily disable safety (NOT RECOMMENDED):

```bash
# Rename hooks to disable
mv .claude/hooks/bash-safety-hook.py .claude/hooks/bash-safety-hook.py.disabled

# Re-enable
mv .claude/hooks/bash-safety-hook.py.disabled .claude/hooks/bash-safety-hook.py
```

**WARNING**: Only disable safety hooks if you fully understand the risks!

## 📚 Additional Resources

- [Claude Code Damage Control (GitHub)](https://github.com/disler/claude-code-damage-control)
- [Claude Code Hooks Documentation](https://docs.anthropic.com/claude/docs)
- Safety Skill: `.claude/skills/safety-guardrails.md`

## 🤝 Contributing

To improve safety patterns:

1. Test new patterns thoroughly
2. Document the risk being addressed
3. Add test cases
4. Update this README
5. Commit with clear description

## 📝 License

Part of Claude Code safety system. Use at your own risk.
Provided as-is without warranty.

## ⚡ Quick Reference

| Operation | Zero Access | Read-Only | No-Delete |
|-----------|-------------|-----------|-----------|
| Read      | 🚫 Block    | ✅ Allow   | ✅ Allow   |
| Write     | 🚫 Block    | 🚫 Block   | ✅ Allow   |
| Edit      | 🚫 Block    | 🚫 Block   | ✅ Allow   |
| Delete    | 🚫 Block    | 🚫 Block   | 🚫 Block   |

---

**Remember**: Safety hooks protect you from accidents, but they're not foolproof. Always review Claude's proposed actions carefully!
