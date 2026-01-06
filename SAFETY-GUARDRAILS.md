# 🛡️ Claude Code Safety Guardrails

**Comprehensive damage control system to prevent accidental file deletions, database drops, and destructive operations.**

---

## 🎯 Overview

This repository now includes production-ready safety guardrails that protect against common AI coding disasters:

- ✅ **File Deletion Protection** - Prevents accidental `rm -rf` and similar destructive commands
- ✅ **Database Safety** - Blocks unqualified DELETEs, DROP commands, and TRUNCATE operations
- ✅ **Credential Protection** - Prevents reading/modifying SSH keys, AWS credentials, and secrets
- ✅ **System File Protection** - Read-only enforcement for system configurations
- ✅ **Automatic Backups** - Creates backups before destructive operations
- ✅ **Audit Logging** - Comprehensive safety event logging
- ✅ **User Confirmation** - Prompts for risky operations

## 🚀 Quick Start

### 1. Verify Installation

```bash
# Check that hooks are installed
ls -la .claude/hooks/

# Verify dependencies
python3 -c "import yaml; print('PyYAML installed')"
```

### 2. Test Safety System

```bash
# This should ask for confirmation
echo '{"tool": {"name": "Bash", "params": {"command": "rm -rf *.db"}}}' | \
  python3 .claude/hooks/bash-safety-hook.py

# This should block immediately
echo '{"tool": {"name": "Bash", "params": {"command": "DELETE FROM users;"}}}' | \
  python3 .claude/hooks/bash-safety-hook.py

# This should allow
echo '{"tool": {"name": "Bash", "params": {"command": "ls -la"}}}' | \
  python3 .claude/hooks/bash-safety-hook.py
```

### 3. Review Configuration

```bash
cat .claude/hooks/patterns.yaml
```

## 📂 System Components

```
.claude/
├── hooks/
│   ├── bash-safety-hook.py       # Bash command protection
│   ├── edit-safety-hook.py       # Edit operation protection
│   ├── write-safety-hook.py      # Write operation protection
│   ├── patterns.yaml             # Safety configuration
│   ├── requirements.txt          # Python dependencies
│   ├── README.md                 # Comprehensive guide
│   ├── INSTALL.md                # Installation instructions
│   └── safety.log                # Audit log (auto-created)
├── skills/
│   └── safety-guardrails.md      # Safety management skill
├── settings.local.json           # Hook registrations
└── backups/                      # Auto-backups (auto-created)
```

## 🔒 Protection Levels

### Zero Access (Complete Prohibition)

**No operations allowed** - Protects highly sensitive files:

- `~/.ssh/*` - SSH keys
- `~/.aws/*` - AWS credentials
- `~/.gnupg/*` - GPG keys
- `*.key`, `*.pem` - Private keys
- `**/credentials.json` - Service accounts

**Result**: 🚫 Immediate block, operation denied

### Read-Only (Modification Protection)

**Read allowed, modifications blocked**:

- `/etc/*` - System configuration
- `~/.bashrc`, `~/.zshrc` - Shell configs
- `package-lock.json` - Dependency locks
- System binaries (`/usr/*`, `/bin/*`)

**Result**: 🚫 Block on write/edit/delete attempts

### No-Delete (Deletion Protection)

**Read and write allowed, deletion blocked**:

- `.claude/hooks/*` - Safety system files
- `*.sql`, `*.db`, `*.sqlite*` - Database files
- `.git/*` - Git repository
- `docker-compose.yml` - Infrastructure configs

**Result**: 🚫 Block only delete operations

## ⚠️ Dangerous Command Patterns

### Auto-Blocked (No Confirmation)

These commands are **immediately blocked**:

```bash
rm -rf /                    # Delete from root
DELETE FROM table;          # Unqualified SQL DELETE
rm -rf .*                   # Delete hidden files from root
```

**Result**: 🚫 BLOCKED with error message

### Confirmation Required

These commands **prompt for user confirmation**:

```bash
rm -rf *                    # Recursive delete with wildcards
DROP DATABASE prod          # Drop database
TRUNCATE TABLE users        # Truncate table
git push --force            # Force push
git reset --hard            # Hard reset
docker system prune -a      # Remove all Docker data
chmod 777 file             # Insecure permissions
sudo rm file               # Delete with privileges
```

**Result**: ⚠️ User confirmation dialog

## 📊 Safety Logs

All operations are logged to `.claude/hooks/safety.log`:

```bash
# View recent safety events
tail -20 .claude/hooks/safety.log

# Count blocked operations
grep "BLOCKED" .claude/hooks/safety.log | wc -l

# View user confirmations
grep "ASK_USER" .claude/hooks/safety.log

# View all allowed operations
grep "ALLOWED" .claude/hooks/safety.log
```

Log format (JSON):
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

## ⚙️ Configuration

### Customize Protected Paths

Edit `.claude/hooks/patterns.yaml`:

```yaml
# Add to noDeletePaths
noDeletePaths:
  - "my-database/*.db"
  - "critical-configs/*"

# Add to readOnlyPaths
readOnlyPaths:
  - "production-config.yml"

# Add to zeroAccessPaths
zeroAccessPaths:
  - "secrets/*.env"
```

### Add Custom Dangerous Patterns

```yaml
dangerousBashPatterns:
  - pattern: 'kubectl\s+delete'
    description: "Kubernetes delete"
    action: "ask"
    message: "⚠️ About to delete K8s resources. Continue?"
```

### Enable Automatic Backups

```yaml
safetySettings:
  backupBeforeDestructive: true
  backupDirectory: ".claude/backups/"
  enableLogging: true
```

## 🧪 Testing

Comprehensive tests demonstrate the safety system:

```bash
# Test 1: Dangerous deletion (should ask)
echo '{"tool": {"name": "Bash", "params": {"command": "rm -rf /tmp/test"}}}' | \
  python3 .claude/hooks/bash-safety-hook.py
# Expected: JSON with "action": "ask"

# Test 2: Safe command (should allow)
echo '{"tool": {"name": "Bash", "params": {"command": "ls -la"}}}' | \
  python3 .claude/hooks/bash-safety-hook.py
# Expected: Exit code 0

# Test 3: Protected file (should block)
echo '{"tool": {"name": "Edit", "params": {"file_path": "~/.ssh/id_rsa"}}}' | \
  python3 .claude/hooks/edit-safety-hook.py
# Expected: 🚫 BLOCKED message

# Test 4: SQL drop (should ask)
echo '{"tool": {"name": "Bash", "params": {"command": "DROP DATABASE prod;"}}}' | \
  python3 .claude/hooks/bash-safety-hook.py
# Expected: JSON with "action": "ask"

# Test 5: Unqualified delete (should block)
echo '{"tool": {"name": "Bash", "params": {"command": "DELETE FROM users;"}}}' | \
  python3 .claude/hooks/bash-safety-hook.py
# Expected: 🚫 BLOCKED message
```

## 📚 Documentation

- **Comprehensive Guide**: `.claude/hooks/README.md`
- **Installation Guide**: `.claude/hooks/INSTALL.md`
- **Safety Skill**: `.claude/skills/safety-guardrails.md`
- **Configuration Reference**: `.claude/hooks/patterns.yaml`

## 💡 Usage Examples

### Working with Claude Code

When Claude Code tries dangerous operations, hooks automatically intervene:

```
You: Delete all test files

Claude: I'll delete the test files
[Checking bash command safety...]
⚠️  This command will DELETE files recursively. Are you sure?

You: [Approve/Deny]
```

### Protected File Attempts

```
You: Edit my SSH config

Claude: I'll edit ~/.ssh/config
[Checking file edit safety...]
🚫 BLOCKED: Cannot access '~/.ssh/config' (credentials/secrets protection)

Claude: I cannot edit SSH configuration files as they're protected.
Would you like me to suggest changes you can apply manually?
```

### Database Operations

```
You: Clean up the users table

Claude: I'll clean up the users table
[Checking bash command safety...]
🚫 BLOCKED: DELETE without WHERE clause will delete all rows. Add WHERE clause.

Claude: For safety, I cannot execute DELETE without a WHERE clause.
Please specify which users to delete.
```

## 🎯 Best Practices

1. ✅ **Keep logging enabled** - Review logs weekly for risky patterns
2. ✅ **Enable automatic backups** - Set `backupBeforeDestructive: true`
3. ✅ **Start conservative** - Begin strict, relax patterns as needed
4. ✅ **Test pattern changes** - Verify with safe commands first
5. ✅ **Version control config** - Track patterns.yaml changes
6. ✅ **Review confirmation prompts** - Don't auto-approve dangerous ops
7. ❌ **Never disable credential protection** - Keep zeroAccessPaths strict
8. ❌ **Don't bypass without understanding** - Risks are real

## 🔍 Troubleshooting

### Hooks Not Running

1. Check settings.local.json has hooks registered
2. Verify executable: `ls -la .claude/hooks/*.py`
3. Test PyYAML: `python3 -c "import yaml"`

### Pattern Not Matching

1. Test regex: `python3 -c "import re; print(re.search(r'pattern', 'test'))"`
2. Check path expansion
3. Review patterns.yaml syntax

### Too Many False Positives

1. Change `action: "ask"` to `action: "skip"`
2. Make patterns more specific
3. Add exceptions for safe operations

## 🚨 Emergency Override

**NOT RECOMMENDED** - Only if you fully understand risks:

```bash
# Temporarily disable (dangerous!)
mv .claude/hooks/bash-safety-hook.py .claude/hooks/bash-safety-hook.py.disabled

# Re-enable
mv .claude/hooks/bash-safety-hook.py.disabled .claude/hooks/bash-safety-hook.py
```

## 🤝 Contributing

To improve safety patterns:

1. Test new patterns thoroughly
2. Document risks addressed
3. Add test cases
4. Update documentation
5. Commit with clear description

## 📄 License

Part of Claude Code safety system.
Use at your own risk. Provided as-is without warranty.

## 🙏 Acknowledgments

Based on:
- [Claude Code Damage Control](https://github.com/disler/claude-code-damage-control)
- AI Safety best practices

---

**⚡ Remember**: These guardrails protect against accidents, but always review Claude's proposed actions carefully. Stay safe! 🛡️
