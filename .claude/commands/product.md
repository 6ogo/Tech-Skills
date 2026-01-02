# Product Lead Command

Route to the Product Lead Agent for product development, design, and quality tasks.

## Usage

```
/product [your request]
```

## Examples

```
/product design new feature
/product build React dashboard
/product create REST API
/product add test coverage
```

## What Happens

1. **Orchestrator** receives your request
2. **Product Lead** takes ownership and analyzes
3. **Specialists** are assigned based on need:
   - Product Designer (requirements, UX, research)
   - Frontend Developer (React, Vue, TypeScript)
   - Backend Developer (APIs, microservices)
   - QA Engineer (testing, automation)
   - Technical Writer (documentation)

## Available Skills

| Agent            | Skills                                                                                       |
| ---------------- | -------------------------------------------------------------------------------------------- |
| Product Designer | pd-01 to pd-06 (requirements, research, ideation, UX, PMF, stakeholders)                     |
| Frontend Dev     | fe-01 to fe-07 (React/Vue, state, TypeScript, components, performance, a11y, testing)        |
| Backend Dev      | be-01 to be-07 (REST, GraphQL, microservices, DB design, versioning, rate limiting, caching) |
| QA Engineer      | qa-01 to qa-07 (strategy, automation, integration, performance, load, data, bugs)            |
| Technical Writer | tw-01 to tw-06 (API docs, user guides, ADRs, runbooks, KB, docs-as-code)                     |

## Mandatory Collaborations

- **Security Lead** → For user-facing features
- **Platform Lead** → For deployment
- **Data Lead** → For data-driven features
