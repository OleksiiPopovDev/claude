---
name: task-creation
description: Generate structured XML task assignments following project conventions including date-based naming with counter management, mandatory repository safety requirements, error correction phases, and agent role assignments. Use when creating new development tasks, assignments for specialized agents, or when users mention task creation, task files, or XML task structure.
---

# Task Creation System

Create structured XML task assignments for specialized AI agents following project conventions.

## Quick Start

### Pre-Creation Checklist

Before creating any task:

1. **Determine target directory** - Where will the task file be saved?
2. **Check today's date** - Format: DD-MM-YYYY
3. **Scan existing tasks** - Find all files for today in target directory
4. **Calculate next counter** - Highest counter + 1 (or 001 if none exist)
5. **Verify agent role** - Confirm agent prompt file exists

### Basic Task Creation Steps

1. Analyze request for clarity and requirements
2. **CHECK existing tasks for counter number** (CRITICAL)
3. Generate filename: `{DATE}-[{COUNTER}]-{task-name}.xml`
4. Use appropriate template structure
5. Fill all required sections with specific details
6. Include mandatory repository safety rules
7. Add error correction phase
8. Save with validated XML structure

## File Naming Convention

### Format

```
{DAY-MONTH-YEAR}-[{COUNTER_TASK_OF_CURRENT_DAY}]-{TASK-NAME}.xml
```

### Examples

```
20-11-2025-[001]-user-authentication-backend.xml
20-11-2025-[002]-security-audit-review.xml
21-11-2025-[001]-frontend-dashboard-component.xml
```

### Counter Rules

- Counter starts at 001 each day
- Increments for each new task on same day
- Resets to 001 for new calendar day
- Always use 3-digit format with leading zeros
- Task name in kebab-case (lowercase with hyphens)

## Counter Management Workflow

### Critical Procedure

**ALWAYS follow this workflow before creating task file:**

```
Step 1: List directory contents
    → bash: ls {task_directory}

Step 2: Filter by today's date
    → Pattern: {TODAY_DATE}-[XXX]-*.xml
    → Example: "20-11-2025-[*]-*.xml"

Step 3: Extract counter numbers
    → From: "20-11-2025-[003]-api.xml"
    → Extract: "003"

Step 4: Find highest counter
    → If no files: use "001"
    → If files exist: max(counters) + 1

Step 5: Format new counter
    → Always 3 digits with leading zeros
    → Example: 1 → "001", 12 → "012"

Step 6: Generate filename
    → {DATE}-[{COUNTER}]-{task-name}.xml
```

### Example Counter Calculation

```bash
# Existing files for 20-11-2025:
20-11-2025-[001]-auth-system.xml
20-11-2025-[002]-api-refactor.xml
20-11-2025-[005]-database-migration.xml

# Next counter: 006 (highest is 005)
# New filename: 20-11-2025-[006]-new-feature.xml
```

## Task XML Structure

### Complete Template

See `references/task-template.md` for full XML template with all sections.

### Required Sections

**Header:**
- task_id: Unique identifier (e.g., "AUTH-001", "FEAT-042")
- project_name: Descriptive project title
- target_agent_role: Agent prompt path using @ notation
- priority: High/Medium/Low
- dependencies: List of prerequisites
- collaboration_required: Yes/No
- estimated_duration: Time estimate in hours
- task_file: Generated filename with correct counter

**Core Content:**
- objective: Single clear goal statement
- context: Background and project overview
- repository_safety_requirements: Mandatory NO COMMIT/PUSH rules
- requirements: Functional, technical, and quality standards
- deliverables: Specific outputs with status="pending"
- acceptance_criteria: Measurable conditions with status="unchecked"
- error_correction_phase: Testing and resolution workflow
- handoff_instructions: Integration points with other agents

## Repository Safety Requirements

**MANDATORY in every task:**

```xml
<repository_safety_requirements>
    <requirement priority="critical">NO COMMITS: Do not commit any changes</requirement>
    <requirement priority="critical">NO PUSHES: Do not push any changes</requirement>
    <requirement priority="critical">LOCAL WORK ONLY: All changes must remain local</requirement>
</repository_safety_requirements>
```

## Error Correction Phase

**MANDATORY in every task:**

```xml
<error_correction_phase>
    <title>Application Testing & Error Resolution</title>
    <steps>
        <step number="1">
            <name>Start Application</name>
            <command>npm run start:dev</command>
            <alternative>appropriate start command</alternative>
        </step>

        <step number="2">
            <name>Error Detection & Resolution Loop</name>
            <conditions>
                <if_success>Continue to step 3</if_success>
                <if_error>Fix all errors and repeat this step</if_error>
                <note>Continue loop until application runs without errors</note>
            </conditions>
        </step>

        <step number="3">
            <name>Port Cleanup</name>
            <commands>
                <command>npx kill-port 3000</command>
                <alternative>lsof -ti:3000 | xargs kill -9</alternative>
            </commands>
        </step>

        <step number="4">
            <name>Verification Checklist</name>
            <checks>
                <check status="pending">Application starts without errors</check>
                <check status="pending">All functionality works as expected</check>
                <check status="pending">No console errors in development mode</check>
                <check status="pending">Port cleanup completed</check>
            </checks>
        </step>
    </steps>
</error_correction_phase>
```

## Agent Role Assignment

### Available Agent Roles

Common agents in this project:
- `@agents/TECHNICAL_LEAD_PROMPT.xml` - NestJS/Porto architecture
- `@agents/QA_ENGINEER_PROMPT.md` - Testing and quality assurance
- `@agents/TASK_MANAGER_PROMPT.xml` - Task creation and management
- `@agents/GIT_MASTER_PROMPT.md` - Git workflow management
- `@agents/SKILLS_MASTER_AGENT.xml` - Agent Skills development
- `@agents/LOGGER_INSPECTOR_PROMPT.md` - Logging analysis
- `@agents/DEVOPS_MASTER_PROMPT.md` - CI/CD and infrastructure

### Assignment Format

```xml
<target_agent_role>@agents/TECHNICAL_LEAD_PROMPT.xml</target_agent_role>
```

## Task Creation Workflow

### 1. Request Analysis

```
Input: Human request + target agent role
↓
Parse requirements
↓
Identify deliverables
↓
Define acceptance criteria
```

### 2. Counter Management

```
Check task directory
↓
Find today's tasks
↓
Extract counters
↓
Calculate next number
↓
Format with leading zeros
```

### 3. Template Population

```
Select appropriate template
↓
Fill header with metadata
↓
Write objective and context
↓
Add safety requirements
↓
Structure requirements
↓
List deliverables
↓
Define acceptance criteria
↓
Include error correction phase
```

### 4. Validation

```
Verify XML structure
↓
Check filename format
↓
Confirm counter uniqueness
↓
Validate all required sections
↓
Review agent role reference
```

### 5. Save and Confirm

```
Write file to disk
↓
Confirm creation
↓
Report filename to user
```

## Common Task Types

### Development Task

```xml
<task_id>DEV-001</task_id>
<target_agent_role>@agents/TECHNICAL_LEAD_PROMPT.xml</target_agent_role>
```

Focus: Feature implementation, refactoring, architecture

### Testing Task

```xml
<task_id>TEST-001</task_id>
<target_agent_role>@agents/QA_ENGINEER_PROMPT.md</target_agent_role>
```

Focus: Test coverage, quality assurance, validation

### Skills Task

```xml
<task_id>SKILL-001</task_id>
<target_agent_role>@agents/SKILLS_MASTER_AGENT.xml</target_agent_role>
```

Focus: Agent Skills development, validation, documentation

### Infrastructure Task

```xml
<task_id>INFRA-001</task_id>
<target_agent_role>@agents/DEVOPS_MASTER_PROMPT.md</target_agent_role>
```

Focus: CI/CD, deployment, monitoring, infrastructure

## Validation Checklist

Before finalizing any task file:

- [ ] XML structure is valid (can be parsed)
- [ ] Filename follows naming convention exactly
- [ ] Counter number is unique for today's date
- [ ] All required sections are present
- [ ] Repository safety requirements included
- [ ] Error correction phase defined
- [ ] Deliverables have status="pending"
- [ ] Acceptance criteria have status="unchecked"
- [ ] Agent role path is correct and file exists
- [ ] Task ID is unique
- [ ] No Windows-style paths (use forward slashes)

## Error Prevention

### Common Mistakes to Avoid

❌ Duplicate counter numbers on same date
✅ Always check existing tasks first

❌ Missing repository safety requirements
✅ Include mandatory safety section

❌ No error correction phase
✅ Add complete error correction workflow

❌ Windows-style paths (backslashes)
✅ Use forward slashes for all paths

❌ Vague deliverables or acceptance criteria
✅ Be specific and measurable

❌ Missing counter in filename
✅ Format: `DATE-[COUNTER]-name.xml`

## Integration Points

### With Task Manager Agent

Task creation typically invoked by Task Manager agent based on:
- Human request for new task
- Specified target agent role
- Project context and requirements

### With Executing Agents

Created tasks consumed by:
- Target agent specified in task file
- Agents follow task structure for execution
- Status attributes updated during execution

### With Project Management

Tasks integrate with:
- Kanban board systems (vibe-kanban integration possible)
- Project tracking and progress monitoring
- Agent collaboration workflows

## Advanced Features

### Multi-Agent Collaboration

```xml
<collaboration_required>Yes</collaboration_required>
<handoff_instructions>
    <instruction>Coordinate with QA Engineer for testing</instruction>
    <instruction>Provide API docs to Frontend Developer</instruction>
</handoff_instructions>
```

### Dependencies

```xml
<dependencies>
    <dependency>AUTH-001: User authentication must be complete</dependency>
    <dependency>DB-003: Database migration must be applied</dependency>
</dependencies>
```

### Progress Tracking

```xml
<deliverable status="pending">User model and schema</deliverable>
<deliverable status="in_progress">Registration endpoint</deliverable>
<deliverable status="completed">Login endpoint</deliverable>
```

## Best Practices

1. **Always verify counter before creating file** - Duplicate counters cause confusion
2. **Be specific in deliverables** - "Implement user auth" → "User registration endpoint with email validation"
3. **Make acceptance criteria measurable** - "Works well" → "95%+ test coverage with all tests passing"
4. **Include complete error correction** - Don't skip the testing workflow
5. **Reference agents correctly** - Use `@` notation with correct path
6. **Keep task files focused** - One clear objective per task
7. **Use proper XML formatting** - Valid structure enables automated processing

## Quick Reference

**Filename format:**
```
{DD-MM-YYYY}-[{001}]-{task-name}.xml
```

**Required sections:**
- header, objective, context, repository_safety_requirements
- requirements, deliverables, acceptance_criteria
- error_correction_phase, handoff_instructions

**Mandatory elements:**
- Repository safety rules (NO COMMITS/PUSHES)
- Error correction testing loop
- Valid XML structure
- Unique counter for date
