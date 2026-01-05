#!/usr/bin/env python3
"""
Edit Tool Safety Hook for Claude Code
Intercepts Edit tool calls to prevent modification of protected files
Exit codes: 0 = allow, 2 = block, other = warning
"""

import sys
import json
import re
import os
from pathlib import Path
from datetime import datetime
import yaml
import shutil

def load_patterns():
    """Load safety patterns from patterns.yaml"""
    hook_dir = Path(__file__).parent
    patterns_file = hook_dir / "patterns.yaml"

    if not patterns_file.exists():
        return {
            "zeroAccessPaths": [],
            "readOnlyPaths": [],
            "dangerousEditPatterns": [],
            "safetySettings": {"enableLogging": True}
        }

    with open(patterns_file, 'r') as f:
        return yaml.safe_load(f)

def log_safety_event(event_type, file_path, action, message=""):
    """Log safety events for audit trail"""
    hook_dir = Path(__file__).parent
    log_file = hook_dir / "safety.log"

    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "type": event_type,
        "tool": "Edit",
        "file": file_path,
        "action": action,
        "message": message
    }

    with open(log_file, 'a') as f:
        f.write(json.dumps(log_entry) + "\n")

def expand_path(path_pattern):
    """Expand ~ and environment variables in path"""
    expanded = os.path.expanduser(path_pattern)
    expanded = os.path.expandvars(expanded)
    return expanded

def matches_path_pattern(test_path, pattern):
    """Check if a path matches a pattern (supports wildcards)"""
    pattern_expanded = expand_path(pattern)
    test_expanded = expand_path(test_path)

    # Normalize paths
    try:
        test_expanded = str(Path(test_expanded).resolve())
        if '*' in pattern_expanded:
            # Convert glob pattern to regex
            regex_pattern = pattern_expanded.replace('*', '.*').replace('?', '.')
            regex_pattern = f"^{regex_pattern}$"
            return bool(re.match(regex_pattern, test_expanded))
        else:
            pattern_expanded = str(Path(pattern_expanded).resolve())
            return test_expanded == pattern_expanded or test_expanded.startswith(pattern_expanded)
    except Exception:
        # Fallback to simple string matching
        return test_expanded.startswith(pattern_expanded)

def check_path_protection(file_path, patterns):
    """Check if file is protected from editing"""
    # Check zero access paths
    for zero_pattern in patterns.get("zeroAccessPaths", []):
        if matches_path_pattern(file_path, zero_pattern):
            return {
                "block": True,
                "message": f"🚫 BLOCKED: Cannot access '{file_path}' (credentials/secrets protection)"
            }

    # Check read-only paths
    for readonly_pattern in patterns.get("readOnlyPaths", []):
        if matches_path_pattern(file_path, readonly_pattern):
            return {
                "block": True,
                "message": f"🚫 BLOCKED: Cannot modify '{file_path}' (read-only system file)"
            }

    return None

def check_dangerous_content(new_string, patterns):
    """Check if new content contains dangerous patterns"""
    for pattern_config in patterns.get("dangerousEditPatterns", []):
        pattern = pattern_config.get("pattern", "")
        action = pattern_config.get("action", "ask")
        message = pattern_config.get("message", "")

        if re.search(pattern, new_string, re.IGNORECASE):
            if action == "block":
                return {
                    "block": True,
                    "message": message
                }
            elif action == "ask":
                return {
                    "ask": True,
                    "message": message
                }

    return None

def create_backup(file_path, patterns):
    """Create backup of file before modification"""
    settings = patterns.get("safetySettings", {})
    if not settings.get("backupBeforeDestructive", False):
        return

    backup_dir = Path(expand_path(settings.get("backupDirectory", ".claude/backups/")))
    backup_dir.mkdir(parents=True, exist_ok=True)

    # Create backup with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = Path(file_path).name
    backup_path = backup_dir / f"{file_name}.{timestamp}.backup"

    try:
        if Path(file_path).exists():
            shutil.copy2(file_path, backup_path)
            log_safety_event("BACKUP_CREATED", file_path, "backup", f"Backed up to {backup_path}")
    except Exception as e:
        log_safety_event("BACKUP_FAILED", file_path, "error", str(e))

def main():
    # Read hook input from stdin
    try:
        hook_input = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        print("Error: Invalid JSON input", file=sys.stderr)
        sys.exit(1)

    # Extract file info from tool parameters
    tool_name = hook_input.get("tool", {}).get("name", "")
    if tool_name != "Edit":
        # Not an edit command, allow
        sys.exit(0)

    params = hook_input.get("tool", {}).get("params", {})
    file_path = params.get("file_path", "")
    new_string = params.get("new_string", "")

    if not file_path:
        # No file path to check
        sys.exit(0)

    # Load safety patterns
    patterns = load_patterns()

    # Check path protection
    path_result = check_path_protection(file_path, patterns)
    if path_result and path_result.get("block"):
        log_safety_event("BLOCKED_PATH", file_path, "block", path_result["message"])
        print(path_result["message"], file=sys.stderr)
        sys.exit(2)  # Block

    # Check dangerous content patterns
    content_result = check_dangerous_content(new_string, patterns)
    if content_result:
        if content_result.get("block"):
            log_safety_event("BLOCKED_CONTENT", file_path, "block", content_result["message"])
            print(content_result["message"], file=sys.stderr)
            sys.exit(2)  # Block

        if content_result.get("ask"):
            log_safety_event("ASK_USER", file_path, "ask", content_result["message"])
            response = {
                "action": "ask",
                "message": content_result["message"],
                "file": file_path
            }
            print(json.dumps(response))
            sys.exit(0)

    # Create backup before allowing edit
    create_backup(file_path, patterns)

    # Log allowed edit
    if patterns.get("safetySettings", {}).get("enableLogging", True):
        log_safety_event("ALLOWED", file_path, "allow", "")

    # Allow edit
    sys.exit(0)

if __name__ == "__main__":
    main()
