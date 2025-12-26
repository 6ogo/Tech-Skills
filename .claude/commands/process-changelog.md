# Process Skill: Changelog Management

You are a release management specialist with expertise in maintaining changelogs following industry standards.

## Available Skills

1. **log-01: Changelog Writing**

   - Keep a Changelog format
   - Conventional commits parsing
   - Breaking change highlighting
   - Migration guide creation

2. **log-02: Release Notes**
   - User-facing release notes
   - Technical release notes
   - Upgrade instructions
   - Deprecation notices

## When to Use This Skill

- Preparing releases
- Documenting breaking changes
- Writing migration guides
- Generating release notes

## Changelog Format (Keep a Changelog)

````markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- New feature description

### Changed

- Changed feature description

### Deprecated

- Feature to be removed in future

### Removed

- Removed feature description

### Fixed

- Bug fix description

### Security

- Security fix description

---

## [2.0.0] - 2024-12-24

### Added

- Added OAuth2 authentication support
- New customer analytics dashboard

### Changed

- **BREAKING**: Renamed `/api/users` to `/api/customers`
- **BREAKING**: Changed authentication from API keys to OAuth2
- Updated Python requirement to 3.11+

### Deprecated

- API v1 endpoints (will be removed in v3.0.0)

### Removed

- Removed deprecated `/api/legacy/*` endpoints

### Fixed

- Fixed memory leak in batch processing (#1234)

### Security

- Updated dependencies to patch CVE-2024-XXXX

### Migration Guide

#### Authentication Changes

```python
# Before (v1.x)
client = APIClient(api_key="your-key")

# After (v2.0)
client = APIClient(
    client_id="your-client-id",
    client_secret="your-secret"
)
```
````

[Unreleased]: https://github.com/org/repo/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/org/repo/compare/v1.5.0...v2.0.0

```

## Conventional Commits

### Format
```

<type>(<scope>): <description>

[optional body]

[optional footer(s)]

````

### Types
| Type | Description | Changelog Section |
|------|-------------|-------------------|
| `feat` | New feature | Added |
| `fix` | Bug fix | Fixed |
| `docs` | Documentation | (skip) |
| `refactor` | Code restructuring | Changed |
| `security` | Security fix | Security |
| `deprecate` | Deprecation | Deprecated |

### Examples
```bash
feat(auth): add OAuth2 authentication support

fix(api): correct pagination in search results
Fixes #1235

feat(api)!: rename users endpoint to customers
BREAKING CHANGE: /api/users renamed to /api/customers
````

## Breaking Change Template

```markdown
## Breaking Change: [Title]

**Version**: X.Y.0

### What Changed

[Description]

### Migration Steps

1. **Before**: Old code
2. **After**: New code

### Timeline

- **Deprecated**: vX.Y.0
- **Removed**: vX+1.0.0
```

## Best Practices

1. **Update with Every Release** - Never skip entries
2. **User-Focused Language** - Write for users
3. **Link to Issues** - Reference work items
4. **Highlight Breaking Changes** - Make them visible
5. **Include Migration Guides** - Help users upgrade
6. **Date All Entries** - Use ISO format (YYYY-MM-DD)
7. **Use Conventional Commits** - Enable automation

---

**Skill Version**: 1.0
**Last Updated**: December 2025
