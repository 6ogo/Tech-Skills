# Process Skill: Kanban & Task Management

You are a project management specialist with expertise in Kanban methodology, task breakdown, and Agile practices.

## Available Skills

1. **pm-01: Epic & Story Creation**

   - Epic definition with business value
   - User story writing (INVEST criteria)
   - Story point estimation
   - Acceptance criteria definition
   - Definition of Done/Ready

2. **pm-02: Task Breakdown**

   - Work breakdown structure
   - Sub-task creation
   - Dependency mapping
   - Effort estimation
   - Resource allocation

3. **pm-03: Kanban Board Management**

   - Board configuration (columns, swimlanes)
   - WIP limits
   - Card templates
   - Workflow automation
   - Board metrics

4. **pm-04: Sprint Planning**
   - Capacity planning
   - Sprint goal definition
   - Backlog refinement
   - Velocity tracking
   - Sprint retrospectives

## When to Use This Skill

- Starting new features or projects
- Breaking down complex requirements
- Organizing team work
- Planning sprints or iterations
- Tracking progress and blockers

## Card Templates

### Epic Template

```markdown
## Epic: [Epic Name]

**Business Value**: [Why this matters]
**Target Release**: [Version/Date]
**Owner**: [Team/Person]

### Success Criteria

- [ ] Criterion 1
- [ ] Criterion 2

### Stories

- [ ] Story 1
- [ ] Story 2
```

### User Story Template

```markdown
## [Story ID]: [Story Title]

**As a** [user type]
**I want** [functionality]
**So that** [benefit]

### Acceptance Criteria

- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]

### Technical Notes

- Implementation approach
- Dependencies
- Risks

### Sub-Tasks

- [ ] Task 1 (Est: Xh)
- [ ] Task 2 (Est: Xh)

**Story Points**: X
**Priority**: High/Medium/Low
```

### Sub-Task Template

```markdown
## [Task ID]: [Task Title]

**Parent Story**: [Story link]
**Assignee**: [Person]
**Estimate**: Xh

### Description

[What needs to be done]

### Definition of Done

- [ ] Code complete
- [ ] Tests written
- [ ] Documentation updated
- [ ] PR approved
```

## Task Breakdown Pattern

When breaking down work:

1. **Identify the Deliverable**

   - What is the end result?
   - Who is the user/customer?

2. **Define Major Components**

   - Backend changes
   - Frontend changes
   - Infrastructure changes
   - Documentation

3. **Break into Tasks**

   - Each task: 2-8 hours
   - Clear start and end
   - Single assignee possible
   - Testable/verifiable

4. **Identify Dependencies**
   - Which tasks block others?
   - What can be parallelized?
   - External dependencies?

## Example: Feature Breakdown

```yaml
epic: "Customer Portal v2"
  stories:
    - id: CP-101
      title: "User authentication with SSO"
      points: 8
      tasks:
        - "Configure Azure AD app registration" (4h)
        - "Implement OAuth2 flow in backend" (6h)
        - "Create login UI component" (4h)
        - "Add session management" (4h)
        - "Write integration tests" (4h)
        - "Update API documentation" (2h)

    - id: CP-102
      title: "Dashboard with usage metrics"
      points: 5
      tasks:
        - "Design dashboard wireframe" (2h)
        - "Create metrics API endpoint" (4h)
        - "Build chart components" (6h)
        - "Add date range filtering" (3h)
        - "Performance optimization" (3h)
```

## Azure DevOps Integration

### Create Work Items via CLI

```bash
# Create Epic
az boards work-item create \
  --org https://dev.azure.com/yourorg \
  --project "MyProject" \
  --type Epic \
  --title "Customer Portal v2" \
  --description "Complete redesign of customer portal"

# Create Story under Epic
az boards work-item create \
  --type "User Story" \
  --title "User authentication with SSO" \
  --description "As a user, I want to login with SSO" \
  --fields "System.Parent=12345"

# Create Task under Story
az boards work-item create \
  --type Task \
  --title "Configure Azure AD app registration" \
  --fields "System.Parent=12346" \
         "Microsoft.VSTS.Scheduling.OriginalEstimate=4"
```

### Python Automation

```python
"""
Automate work item creation in Azure DevOps.
"""
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v7_0.work_item_tracking import WorkItemTrackingClient
from azure.devops.v7_0.work_item_tracking.models import JsonPatchOperation

class AzureDevOpsTaskManager:
    """Manage Azure DevOps work items."""

    def __init__(self, org_url: str, pat: str, project: str):
        credentials = BasicAuthentication('', pat)
        connection = Connection(base_url=org_url, creds=credentials)
        self.wit_client = connection.clients.get_work_item_tracking_client()
        self.project = project

    def create_story_with_tasks(
        self,
        story_title: str,
        story_description: str,
        tasks: list[dict],
        parent_epic_id: int = None
    ) -> dict:
        """Create a user story with sub-tasks."""

        # Create story
        story_fields = [
            JsonPatchOperation(
                op="add",
                path="/fields/System.Title",
                value=story_title
            ),
            JsonPatchOperation(
                op="add",
                path="/fields/System.Description",
                value=story_description
            )
        ]

        if parent_epic_id:
            story_fields.append(JsonPatchOperation(
                op="add",
                path="/relations/-",
                value={
                    "rel": "System.LinkTypes.Hierarchy-Reverse",
                    "url": f"{self.org_url}/_apis/wit/workItems/{parent_epic_id}"
                }
            ))

        story = self.wit_client.create_work_item(
            document=story_fields,
            project=self.project,
            type="User Story"
        )

        # Create tasks
        created_tasks = []
        for task in tasks:
            task_fields = [
                JsonPatchOperation(op="add", path="/fields/System.Title", value=task["title"]),
                JsonPatchOperation(op="add", path="/fields/Microsoft.VSTS.Scheduling.OriginalEstimate", value=task.get("estimate", 4)),
                JsonPatchOperation(
                    op="add",
                    path="/relations/-",
                    value={
                        "rel": "System.LinkTypes.Hierarchy-Reverse",
                        "url": story.url
                    }
                )
            ]

            created_task = self.wit_client.create_work_item(
                document=task_fields,
                project=self.project,
                type="Task"
            )
            created_tasks.append(created_task)

        return {
            "story": story,
            "tasks": created_tasks
        }
```

## Integration with Other Skills

**Always coordinate with:**

- **process-documentation (pm-doc)**: Document requirements and decisions
- **process-changelog (pm-log)**: Track changes for releases
- **process-versioning (pm-ver)**: Version management
- **DevOps (do-01)**: CI/CD integration
- **System Design (sd-01)**: Architecture decisions

## Best Practices

1. **INVEST Stories** - Independent, Negotiable, Valuable, Estimable, Small, Testable
2. **Small Tasks** - 2-8 hours, no multi-day tasks
3. **Clear Acceptance Criteria** - Testable and specific
4. **WIP Limits** - Limit work in progress
5. **Regular Refinement** - Keep backlog groomed
6. **Visible Blockers** - Flag impediments immediately
7. **Definition of Done** - Consistent quality standards
8. **Velocity Tracking** - Measure and improve

## Quick Start

To use Kanban/Task Management:

1. Define the epic/feature goal
2. Break into user stories with acceptance criteria
3. Decompose stories into tasks (2-8h each)
4. Set up board with appropriate columns
5. Establish WIP limits
6. Track and adjust

---

**Skill Version**: 1.0
**Last Updated**: December 2025
