# Process Documentation Template

> **Instructions:** Copy this template and fill in the sections below to document your process.
> The AI-powered automation analyzer will parse this document and suggest automation solutions.
> Write naturally - the parser understands markdown, lists, and conversational descriptions.

---

## Process Information

**Process Name:** [Your Process Name]

**Owner/Author:** [Who owns this process]

**Last Updated:** [Date]

**Frequency:** [How often does this run? e.g., Daily, Weekly, Monthly, Ad-hoc]

---

## Overview

[Describe the process in 2-3 sentences. What is the purpose? What does it accomplish?]

Example:
> This process generates monthly sales reports for the executive team. We gather data from multiple sources, analyze trends, and produce a summary document with visualizations.

---

## Stakeholders

Who is involved in or affected by this process?

- [Stakeholder 1] - [Their role, e.g., "Approver", "Consumer", "Input Provider"]
- [Stakeholder 2] - [Their role]
- [Stakeholder 3] - [Their role]

---

## Current Steps

Describe each step of the process. Include as much detail as possible.

### Step 1: [Step Name]
**Duration:** [How long does this take? e.g., "30 minutes", "2 hours"]
**Who:** [Who performs this step?]
**Tools:** [What tools/systems are used?]

[Detailed description of what happens in this step]

*Pain points:* [Any issues with this step?]

---

### Step 2: [Step Name]
**Duration:** [Time]
**Who:** [Person/Role]
**Tools:** [Systems used]

[Description]

*Pain points:* [Issues]

---

### Step 3: [Step Name]
**Duration:** [Time]
**Who:** [Person/Role]
**Tools:** [Systems used]

[Description]

*Pain points:* [Issues]

---

[Add more steps as needed...]

---

## Data Sources

What systems or data sources are involved?

| Source | Type | Access Method | Data Description |
|--------|------|---------------|------------------|
| [e.g., Salesforce] | CRM | API/Export | Customer and opportunity data |
| [e.g., SAP] | ERP | Manual export | Financial transactions |
| [e.g., Excel files] | Spreadsheet | File share | Manual tracking sheets |

---

## Current Tools

What tools and technologies are currently used?

- **Data Processing:** [e.g., Excel, Python, SQL]
- **Communication:** [e.g., Email, Slack, Teams]
- **Storage:** [e.g., SharePoint, OneDrive, Network drive]
- **Visualization:** [e.g., Power BI, Tableau, Excel charts]
- **Other:** [Any other tools]

---

## Pain Points & Challenges

What are the main problems with the current process?

### Time-Related
- [ ] Process takes too long overall
- [ ] Waiting for approvals causes delays
- [ ] Manual data entry is slow
- [ ] [Other time issues]

### Quality-Related
- [ ] Manual steps are error-prone
- [ ] Inconsistent results between runs
- [ ] Data quality issues
- [ ] [Other quality issues]

### Visibility-Related
- [ ] No visibility into process status
- [ ] Hard to track progress
- [ ] Difficult to audit
- [ ] [Other visibility issues]

### Other Challenges
- [Describe any other challenges]

---

## Goals & Success Criteria

What would success look like?

### Must Have
- [ ] [Critical requirement, e.g., "Reduce processing time by 50%"]
- [ ] [Critical requirement, e.g., "Eliminate manual data entry errors"]

### Should Have
- [ ] [Important but not critical, e.g., "Real-time status dashboard"]
- [ ] [Important feature]

### Nice to Have
- [ ] [Desired but optional, e.g., "Mobile notifications"]
- [ ] [Optional feature]

### Success Metrics
| Metric | Current | Target |
|--------|---------|--------|
| Processing Time | [e.g., 4 hours] | [e.g., 30 minutes] |
| Error Rate | [e.g., 5%] | [e.g., <1%] |
| [Other metric] | [Current] | [Target] |

---

## Constraints & Considerations

What limitations or requirements must be considered?

### Technical Constraints
- [e.g., "Must integrate with existing SAP system"]
- [e.g., "Limited to Azure cloud services"]
- [e.g., "Team only knows Python, no Java expertise"]

### Business Constraints
- [e.g., "Budget limited to $X"]
- [e.g., "Must maintain audit trail for compliance"]
- [e.g., "Cannot change approval hierarchy"]

### Compliance Requirements
- [ ] GDPR / Data Privacy
- [ ] SOX Compliance
- [ ] Industry-specific regulations
- [ ] [Other compliance needs]

---

## Existing Documentation

Links to any existing documentation:

- [Process diagram/flowchart]
- [Standard operating procedures]
- [Training materials]
- [Related policies]

---

## Additional Notes

[Any other information that might be helpful for automation analysis]

---

# How to Use This Template

## With VS Code GitHub Copilot

1. Fill out this template with your process details
2. Save the file (e.g., `my_process.md`)
3. Open a Python file and run:

```python
from process_parser import ProcessParser
from ai_prompt_generator import AIPromptGenerator, PromptStyle

# Read your process documentation
with open('my_process.md', 'r') as f:
    process_doc = f.read()

# Parse the process
parser = ProcessParser()
parsed = parser.parse(process_doc)

# Generate AI prompt
generator = AIPromptGenerator()
prompt = generator.generate_discovery_prompt(parsed, PromptStyle.COPILOT)

# Print the prompt (copy this to Copilot Chat)
print(prompt.prompt)
```

4. Copy the generated prompt to GitHub Copilot Chat
5. Get automation suggestions!

## Quick Method

Or simply paste this entire filled-out template directly into an AI assistant and ask:

> "Analyze this process and suggest automation solutions. Consider which parts can be fully automated, which need human oversight, and what technologies would work best."

---

## Example: Filled Template

Below is an example of a completed template:

---

# Process Documentation: Monthly Expense Report

## Process Information
**Process Name:** Monthly Expense Report Generation
**Owner:** Finance Team
**Last Updated:** 2024-12-01
**Frequency:** Monthly (first week of each month)

## Overview
Generate monthly expense reports consolidating data from credit cards, invoices, and reimbursements. Reports go to department heads for review and to finance for budget tracking.

## Stakeholders
- Finance Analyst - Runs the process
- Department Heads - Review and approve
- CFO - Receives final summary
- Employees - Submit expense claims

## Current Steps

### Step 1: Export Credit Card Data
**Duration:** 20 minutes
**Who:** Finance Analyst
**Tools:** Bank portal, Excel

Log into bank portal, export transactions for the month, save as CSV.

*Pain points:* Manual login, sometimes exports fail, have to retry

### Step 2: Collect Employee Reimbursements
**Duration:** 1 hour
**Who:** Finance Analyst
**Tools:** Email, Shared folder

Check shared folder for submitted expense forms, verify receipts attached.

*Pain points:* Forms are inconsistent, missing receipts common, lots of back-and-forth emails

### Step 3: Consolidate in Excel
**Duration:** 2 hours
**Who:** Finance Analyst
**Tools:** Excel

Combine all sources into master spreadsheet, categorize expenses, calculate totals.

*Pain points:* Very tedious, copy-paste errors happen, categories inconsistent

### Step 4: Generate Department Summaries
**Duration:** 1 hour
**Who:** Finance Analyst
**Tools:** Excel, PowerPoint

Create summary for each department with charts and highlights.

*Pain points:* Repetitive, formatting takes too long

### Step 5: Send for Approval
**Duration:** 2-3 days waiting
**Who:** Department Heads
**Tools:** Email

Email summaries to department heads, wait for approval replies.

*Pain points:* Long delays, hard to track who has approved, reminder emails needed

### Step 6: Compile Final Report
**Duration:** 1 hour
**Who:** Finance Analyst
**Tools:** PowerPoint, Word

Combine approved summaries into final report for CFO.

*Pain points:* Manual compilation, version control issues

## Pain Points & Challenges
- Process takes 5+ hours of active work plus 2-3 days waiting
- Manual data entry leads to ~5% error rate
- No visibility into approval status
- Inconsistent expense categorization
- Version control nightmares with multiple files

## Goals & Success Criteria
- Reduce active work time from 5 hours to <1 hour
- Eliminate manual data entry errors
- Real-time approval tracking
- Consistent automated categorization
- Single source of truth for all data

## Constraints
- Must integrate with existing bank portal (no API available)
- Team comfortable with Excel and basic Python
- Budget: Minimal (use existing tools where possible)
- Compliance: Expense data must be retained for 7 years

---

*This example shows the level of detail that helps the automation analyzer provide the best recommendations.*
