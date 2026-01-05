#!/usr/bin/env python3
"""
Bash Tool Safety Hook for Claude Code
Intercepts Bash tool calls to prevent destructive operations
Exit codes: 0 = allow, 2 = block, other = warning
"""

import sys
import json
import re
import os
from pathlib import Path
from datetime import datetime
import yaml

def load_patterns():
    """Load safety patterns from patterns.yaml"""
    hook_dir = Path(__file__).parent
    patterns_file = hook_dir / "patterns.yaml"

    if not patterns_file.exists():
        return {
            "dangerousBashPatterns": [],
            "zeroAccessPaths": [],
            "readOnlyPaths": [],
            "noDeletePaths": [],
            "safetySettings": {"enableLogging": True}
        }

    with open(patterns_file, 'r') as f:
        return yaml.safe_load(f)

def log_safety_event(event_type, command, action, message=""):
    """Log safety events for audit trail"""
    hook_dir = Path(__file__).parent
    log_file = hook_dir / "safety.log"

    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "type": event_type,
        "command": command,
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

    # Convert glob pattern to regex
    regex_pattern = pattern_expanded.replace('*', '.*').replace('?', '.')
    regex_pattern = f"^{regex_pattern}$"

    return bool(re.match(regex_pattern, test_expanded))

def extract_paths_from_command(command):
    """Extract file paths from bash command"""
    paths = []

    # Common patterns for file paths in commands
    # Match arguments that look like paths
    path_patterns = [
        r'(?:^|\s)(/?(?:[\w\-\.~]+/)*[\w\-\.~]+)',  # Unix paths
        r'(?:^|\s)(\.{1,2}/(?:[\w\-\.]+/)*[\w\-\.]*)',  # Relative paths
    ]

    for pattern in path_patterns:
        matches = re.finditer(pattern, command)
        for match in matches:
            path = match.group(1)
            # Filter out command names and flags
            if not path.startswith('-') and path not in ['rm', 'mv', 'cp', 'cat', 'chmod', 'chown']:
                paths.append(path)

    return paths

def check_path_protection(command, patterns):
    """Check if command affects protected paths"""
    paths = extract_paths_from_command(command)

    for path in paths:
        # Check zero access paths
        for zero_pattern in patterns.get("zeroAccessPaths", []):
            if matches_path_pattern(path, zero_pattern):
                return {
                    "block": True,
                    "message": f"🚫 BLOCKED: Access to protected path '{path}' is forbidden (credentials/secrets)"
                }

        # Check read-only paths for write operations
        if any(cmd in command for cmd in ['rm', 'mv', 'chmod', 'chown', '>', '>>']):
            for readonly_pattern in patterns.get("readOnlyPaths", []):
                if matches_path_pattern(path, readonly_pattern):
                    return {
                        "block": True,
                        "message": f"🚫 BLOCKED: Path '{path}' is read-only (system file protection)"
                    }

        # Check no-delete paths for delete operations
        if any(cmd in command for cmd in ['rm ', 'rmdir']):
            for nodelete_pattern in patterns.get("noDeletePaths", []):
                if matches_path_pattern(path, nodelete_pattern):
                    return {
                        "block": True,
                        "message": f"🚫 BLOCKED: Cannot delete '{path}' (critical file protection)"
                    }

    return None

def check_dangerous_patterns(command, patterns):
    """Check if command matches dangerous patterns"""
    for pattern_config in patterns.get("dangerousBashPatterns", []):
        pattern = pattern_config.get("pattern", "")
        action = pattern_config.get("action", "ask")
        message = pattern_config.get("message", "")
        description = pattern_config.get("description", "")

        if action == "skip":
            continue

        if re.search(pattern, command, re.IGNORECASE):
            if action == "block":
                return {
                    "block": True,
                    "message": message or f"🚫 BLOCKED: {description}"
                }
            elif action == "ask":
                return {
                    "ask": True,
                    "message": message or f"⚠️  Warning: {description}",
                    "pattern": description
                }

    return None

def main():
    # Read hook input from stdin
    try:
        hook_input = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        print("Error: Invalid JSON input", file=sys.stderr)
        sys.exit(1)

    # Extract command from tool parameters
    tool_name = hook_input.get("tool", {}).get("name", "")
    if tool_name != "Bash":
        # Not a bash command, allow
        sys.exit(0)

    params = hook_input.get("tool", {}).get("params", {})
    command = params.get("command", "")

    if not command:
        # No command to check
        sys.exit(0)

    # Load safety patterns
    patterns = load_patterns()

    # Check path protection
    path_result = check_path_protection(command, patterns)
    if path_result:
        if path_result.get("block"):
            log_safety_event("BLOCKED_PATH", command, "block", path_result["message"])
            print(path_result["message"], file=sys.stderr)
            sys.exit(2)  # Block

    # Check dangerous command patterns
    pattern_result = check_dangerous_patterns(command, patterns)
    if pattern_result:
        if pattern_result.get("block"):
            log_safety_event("BLOCKED_PATTERN", command, "block", pattern_result["message"])
            print(pattern_result["message"], file=sys.stderr)
            sys.exit(2)  # Block

        if pattern_result.get("ask"):
            # Return JSON for user confirmation dialog
            log_safety_event("ASK_USER", command, "ask", pattern_result["message"])
            response = {
                "action": "ask",
                "message": pattern_result["message"],
                "command": command,
                "pattern": pattern_result.get("pattern", "")
            }
            print(json.dumps(response))
            sys.exit(0)

    # Log allowed command
    if patterns.get("safetySettings", {}).get("enableLogging", True):
        log_safety_event("ALLOWED", command, "allow", "")

    # Allow command
    sys.exit(0)

if __name__ == "__main__":
    main()
