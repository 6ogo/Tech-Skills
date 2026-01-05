# Safety Guardrails Installation Guide

## Quick Installation

The safety guardrails have been pre-configured for this repository. Follow these steps to activate:

### 1. Install Python Dependencies

```bash
pip install pyyaml
```

Or using the requirements file:

```bash
pip install -r .claude/hooks/requirements.txt
```

### 2. Verify Hook Permissions

```bash
chmod +x .claude/hooks/*.py
```

### 3. Test the Installation

Run the test commands below to verify everything works:

```bash
# Test 1: Should BLOCK (deleting from root)
echo '{"tool": {"name": "Bash", "params": {"command": "rm -rf /tmp/test"}}}' | python3 .claude/hooks/bash-safety-hook.py
echo "Exit code: $?"  # Should be 2 (blocked) or 0 with ask message

# Test 2: Should ALLOW (safe command)
echo '{"tool": {"name": "Bash", "params": {"command": "ls -la"}}}' | python3 .claude/hooks/bash-safety-hook.py
echo "Exit code: $?"  # Should be 0

# Test 3: Should BLOCK (SSH key file)
echo '{"tool": {"name": "Edit", "params": {"file_path": "~/.ssh/id_rsa"}}}' | python3 .claude/hooks/edit-safety-hook.py
echo "Exit code: $?"  # Should be 2 (blocked)
```

### 4. Review Configuration

Check your settings:

```bash
cat .claude/settings.local.json
cat .claude/hooks/patterns.yaml
```

## What's Installed

### Safety Hooks

1. **bash-safety-hook.py** - Intercepts Bash commands
   - Blocks: `rm -rf /`, unqualified SQL DELETEs, etc.
   - Asks: `rm -rf *`, DROP TABLE, git force push, etc.

2. **edit-safety-hook.py** - Intercepts Edit operations
   - Blocks: Editing credential files, system files
   - Creates: Automatic backups before edits

3. **write-safety-hook.py** - Intercepts Write operations
   - Blocks: Writing to credential paths, system files
   - Asks: Overwriting important config files
   - Checks: File size limits

### Configuration File

**patterns.yaml** - Central configuration:
- Protection levels (zeroAccess, readOnly, noDelete)
- Dangerous command patterns
- File size limits
- Backup settings

### Management Tools

- **Safety Skill**: `.claude/skills/safety-guardrails.md`
- **Documentation**: `.claude/hooks/README.md`
- **Logs**: `.claude/hooks/safety.log` (auto-created)
- **Backups**: `.claude/backups/` (auto-created)

## Customization

### Add Protected Paths

Edit `.claude/hooks/patterns.yaml`:

```yaml
noDeletePaths:
  - "my-data/*.db"
  - "important-configs/*"
```

### Add Dangerous Command Pattern

```yaml
dangerousBashPatterns:
  - pattern: 'kubectl\s+delete'
    description: "Kubernetes delete"
    action: "ask"
    message: "⚠️ About to delete Kubernetes resources. Are you sure?"
```

### Enable Automatic Backups

```yaml
safetySettings:
  backupBeforeDestructive: true
  backupDirectory: ".claude/backups/"
```

## Usage

### With Claude Code

The hooks run automatically when Claude Code tries to:
- Execute bash commands
- Edit files
- Write files

You'll see status messages like:
- "Checking bash command safety..."
- "Checking file edit safety..."
- "Checking file write safety..."

### Blocked Operations

When an operation is blocked, you'll see:

```
🚫 BLOCKED: Cannot delete '/path/to/file' (critical file protection)
```

Claude Code will receive this error and won't execute the operation.

### Confirmation Prompts

For risky operations that need confirmation:

```
⚠️ This command will DELETE files recursively. Are you sure?
```

You can approve or deny the operation.

### View Safety Logs

```bash
# Recent events
tail -20 .claude/hooks/safety.log

# All blocked operations
grep BLOCKED .claude/hooks/safety.log

# All user confirmations
grep ASK_USER .claude/hooks/safety.log
```

## Troubleshooting

### Hooks Not Running

1. Check settings.local.json has hooks registered
2. Verify hook scripts are executable: `ls -la .claude/hooks/*.py`
3. Ensure PyYAML is installed: `python3 -c "import yaml"`

### Pattern Not Matching

1. Test regex in Python: `python3 -c "import re; print(re.search(r'pattern', 'test'))"`
2. Check path expansion: `python3 -c "import os; print(os.path.expanduser('~/.ssh'))"`
3. Review patterns.yaml for typos

### Too Many False Positives

1. Change `action: "ask"` to `action: "skip"` for safe patterns
2. Make regex patterns more specific
3. Add exceptions for safe operations

## Advanced Configuration

### Global vs Project Hooks

- **Global**: `~/.claude/settings.json` (applies to all projects)
- **Project**: `.claude/settings.local.json` (this project only)

Both execute in parallel - either can block an operation.

### Hook Timeout

Default timeout is 10 seconds. Customize per hook:

```json
{
  "type": "command",
  "command": "python3 .claude/hooks/bash-safety-hook.py",
  "timeout": 5
}
```

### Disable Hooks Temporarily

**NOT RECOMMENDED**, but if needed:

```bash
# Rename to disable
mv .claude/hooks/bash-safety-hook.py .claude/hooks/bash-safety-hook.py.disabled

# Re-enable
mv .claude/hooks/bash-safety-hook.py.disabled .claude/hooks/bash-safety-hook.py
```

## Safety Best Practices

1. ✅ Keep logging enabled for audit trails
2. ✅ Enable automatic backups
3. ✅ Review logs weekly
4. ✅ Test pattern changes before relying on them
5. ✅ Version control patterns.yaml
6. ✅ Start conservative, relax as needed
7. ❌ Never disable credential path protections
8. ❌ Don't bypass safety without understanding risks

## Getting Help

Use the safety management skill:

```
@safety-guardrails how do I protect my database files?
```

Or review documentation:
- `.claude/hooks/README.md` - Comprehensive guide
- `.claude/skills/safety-guardrails.md` - Skill guide
- `.claude/hooks/patterns.yaml` - Configuration reference

## Next Steps

1. Review your patterns.yaml configuration
2. Customize protected paths for your project
3. Test with safe operations to see hooks in action
4. Review safety logs periodically
5. Share configuration with your team

**Remember**: These guardrails protect you from accidents, but always review Claude's proposed actions carefully!
