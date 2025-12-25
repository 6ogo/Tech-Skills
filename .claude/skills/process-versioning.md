# Process Skill: Semantic Versioning

You are a release management specialist with expertise in semantic versioning and version control strategies.

## Available Skills

1. **ver-01: Semantic Versioning**

   - MAJOR.MINOR.PATCH format
   - Version bump rules
   - Pre-release versions
   - Build metadata

2. **ver-02: Release Strategy**
   - Release branches
   - Tag management
   - Version scripts
   - CI/CD integration

## Semantic Versioning (SemVer)

### Format: MAJOR.MINOR.PATCH

```
X.Y.Z[-prerelease][+build]

Examples:
1.0.0       - Initial release
1.0.1       - Patch release (bug fix)
1.1.0       - Minor release (new feature)
2.0.0       - Major release (breaking change)
2.0.0-alpha - Pre-release
2.0.0-rc.1  - Release candidate
2.0.0+build.123 - With build metadata
```

### When to Increment

| Change Type                       | Version | Example       |
| --------------------------------- | ------- | ------------- |
| Breaking API change               | MAJOR   | 1.x.x → 2.0.0 |
| New feature (backward compatible) | MINOR   | 1.0.x → 1.1.0 |
| Bug fix (backward compatible)     | PATCH   | 1.0.0 → 1.0.1 |
| Pre-release                       | -suffix | 2.0.0-alpha.1 |

### Rules

1. **MAJOR** (X.0.0): Increment when making incompatible API changes
2. **MINOR** (x.Y.0): Increment when adding functionality in backward-compatible manner
3. **PATCH** (x.y.Z): Increment when making backward-compatible bug fixes

### Pre-release Labels

```
alpha   - Early testing, unstable
beta    - Feature complete, may have bugs
rc      - Release candidate, near final
```

## Version Scripts

### Python Version Bump

```python
"""
Semantic version management.
"""
import re
from pathlib import Path
from enum import Enum

class VersionBump(Enum):
    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"

def parse_version(version: str) -> tuple:
    """Parse version string to tuple."""
    match = re.match(r'^(\d+)\.(\d+)\.(\d+)', version)
    if not match:
        raise ValueError(f"Invalid version: {version}")
    return tuple(map(int, match.groups()))

def bump_version(current: str, bump_type: VersionBump) -> str:
    """Bump version according to SemVer."""
    major, minor, patch = parse_version(current)

    if bump_type == VersionBump.MAJOR:
        return f"{major + 1}.0.0"
    elif bump_type == VersionBump.MINOR:
        return f"{major}.{minor + 1}.0"
    else:
        return f"{major}.{minor}.{patch + 1}"

def update_version_file(filepath: str, new_version: str):
    """Update version in file."""
    content = Path(filepath).read_text()

    # Update __version__ = "x.y.z"
    content = re.sub(
        r'__version__\s*=\s*["\'][^"\']+["\']',
        f'__version__ = "{new_version}"',
        content
    )

    Path(filepath).write_text(content)
    return new_version

# Usage
current = "1.2.3"
new_version = bump_version(current, VersionBump.MINOR)  # -> "1.3.0"
```

### package.json Version

```bash
# NPM version commands
npm version patch  # 1.0.0 -> 1.0.1
npm version minor  # 1.0.0 -> 1.1.0
npm version major  # 1.0.0 -> 2.0.0

# With git tag
npm version minor -m "Release v%s"
```

## Git Tagging Strategy

```bash
# Create annotated tag
git tag -a v2.0.0 -m "Release version 2.0.0"

# Push tags
git push origin v2.0.0
git push origin --tags

# List tags
git tag -l "v2.*"

# Delete tag
git tag -d v2.0.0-beta
git push origin :refs/tags/v2.0.0-beta
```

## CI/CD Integration

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - "v*"

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Get version from tag
        id: version
        run: echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT

      - name: Build and publish
        run: |
          echo "Building version ${{ steps.version.outputs.VERSION }}"
```

## Version in Files

### Python

```python
# __init__.py or _version.py
__version__ = "2.0.0"
```

### package.json

```json
{
  "name": "my-app",
  "version": "2.0.0"
}
```

### pyproject.toml

```toml
[project]
version = "2.0.0"
```

## Best Practices

1. **Start at 1.0.0** - First stable release
2. **0.x.x = Development** - Breaking changes expected
3. **Never Reuse Versions** - Each version is unique
4. **Tag Releases** - Git tags for each release
5. **Document Changes** - Update changelog with version
6. **Pre-release Testing** - Use alpha/beta/rc labels
7. **Automate Versioning** - Use CI/CD

## Integration with Other Skills

- **process-changelog (pm-log)**: Version references in changelog
- **process-kanban (pm-01)**: Link releases to completed work
- **DevOps (do-07)**: Release management automation

---

**Skill Version**: 1.0
**Last Updated**: December 2025
