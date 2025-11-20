# Task XML Template

Complete XML template for creating structured task assignments.

## Full Template Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<task_assignment>
    <header>
        <task_id>[Task ID - e.g., AUTH-001, FEAT-042]</task_id>
        <project_name>[Descriptive Project Title]</project_name>
        <target_agent_role>[@path/to/AGENT_PROMPT.xml or .md]</target_agent_role>
        <priority>[High/Medium/Low]</priority>
        <dependencies>
            <dependency>[List of prerequisite tasks or agents]</dependency>
        </dependencies>
        <collaboration_required>[Yes/No - other agents needed]</collaboration_required>
        <estimated_duration>[Duration in hours, e.g., "4-6 hours"]</estimated_duration>
        <task_file>{DAY-MONTH-YEAR}-[{COUNTER}]-{task-name}.xml</task_file>
    </header>

    <objective>
        <description>[Clear, single-sentence goal statement describing what needs to be achieved]</description>
    </objective>

    <context>
        <description>[Brief background explaining why this task exists, the current state, and how it fits into the larger project]</description>
    </context>

    <repository_safety_requirements>
        <requirement priority="critical">NO COMMITS: Do not commit any changes to the repository</requirement>
        <requirement priority="critical">NO PUSHES: Do not push any changes to the repository</requirement>
        <requirement priority="critical">LOCAL WORK ONLY: All changes must remain local</requirement>
    </repository_safety_requirements>

    <requirements>
        <functional_requirements>
            <requirement>[Specific feature or functionality needed - user-facing capabilities]</requirement>
            <requirement>[User story or use case describing expected behavior]</requirement>
            <requirement>[Additional functional requirements as needed]</requirement>
        </functional_requirements>

        <technical_requirements>
            <requirement>[Technology stack constraints or preferences]</requirement>
            <requirement>[Performance criteria and benchmarks]</requirement>
            <requirement>[Integration points with existing systems]</requirement>
            <requirement>[Security requirements]</requirement>
            <requirement>[Scalability considerations]</requirement>
        </technical_requirements>

        <quality_standards>
            <requirement>[Code quality expectations - e.g., test coverage, linting rules]</requirement>
            <requirement>[Testing requirements - unit, integration, e2e]</requirement>
            <requirement>[Documentation needs - inline comments, API docs, guides]</requirement>
            <requirement>[Code review requirements]</requirement>
        </quality_standards>
    </requirements>

    <deliverables>
        <deliverable status="pending">[Specific concrete output 1]</deliverable>
        <deliverable status="pending">[Specific concrete output 2]</deliverable>
        <deliverable status="pending">[Specific concrete output 3]</deliverable>
        <deliverable status="pending">[Additional deliverables as needed]</deliverable>
    </deliverables>

    <acceptance_criteria>
        <criterion status="unchecked">[Measurable success condition 1]</criterion>
        <criterion status="unchecked">[Measurable success condition 2]</criterion>
        <criterion status="unchecked">[Measurable success condition 3]</criterion>
        <criterion status="unchecked">[Additional criteria as needed]</criterion>
    </acceptance_criteria>

    <error_correction_phase>
        <title>Application Testing & Error Resolution</title>
        <steps>
            <step number="1">
                <name>Start Application</name>
                <command>npm run start:dev</command>
                <alternative>[appropriate start command for this project]</alternative>
            </step>

            <step number="2">
                <name>Error Detection & Resolution Loop</name>
                <conditions>
                    <if_success>Continue to step 3</if_success>
                    <if_error>Fix all errors and repeat this step</if_error>
                    <note>Continue this loop until application runs without errors</note>
                </conditions>
            </step>

            <step number="3">
                <name>Port Cleanup</name>
                <commands>
                    <command>npx kill-port 3000</command>
                    <alternative>lsof -ti:3000 | xargs kill -9</alternative>
                    <note>Adjust port number as needed for this application</note>
                </commands>
            </step>

            <step number="4">
                <name>Verification Checklist</name>
                <checks>
                    <check status="pending">Application starts without errors</check>
                    <check status="pending">All functionality works as expected</check>
                    <check status="pending">No console errors in development mode</check>
                    <check status="pending">Port cleanup completed after testing</check>
                    <check status="pending">[Additional project-specific checks]</check>
                </checks>
            </step>
        </steps>
    </error_correction_phase>

    <handoff_instructions>
        <instruction>[Instructions for passing work to next agent or integration points]</instruction>
        <instruction>[Specific files or documentation to share with other agents]</instruction>
        <instruction>[Coordination requirements with other team members or agents]</instruction>
    </handoff_instructions>
</task_assignment>
```

## Field Descriptions

### Header Fields

**task_id**: Unique identifier using a prefix-number format
- Development: DEV-001, DEV-002
- Testing: TEST-001, QA-001
- Skills: SKILL-001
- Infrastructure: INFRA-001, DEVOPS-001

**project_name**: Human-readable title that describes the task scope

**target_agent_role**: Path to agent prompt file using @ notation
- Must be actual path to existing agent prompt
- Examples: `@agents/TECHNICAL_LEAD_PROMPT.xml`, `@agents/QA_ENGINEER_PROMPT.md`

**priority**: Urgency level
- High: Blocking other work, critical bugs, time-sensitive
- Medium: Important but not blocking
- Low: Nice-to-have, optimization, refactoring

**dependencies**: What must be completed first
- Reference other tasks by ID
- Note external dependencies
- Describe required state or setup

**collaboration_required**: Will other agents be needed?
- Yes: Specify which agents in handoff_instructions
- No: Single agent can complete independently

**estimated_duration**: Realistic time estimate
- Format: "X-Y hours" for range
- Format: "X hours" for specific estimate
- Consider agent capabilities and task complexity

**task_file**: Auto-generated filename
- Must follow naming convention exactly
- Include correct counter for date
- Example: `20-11-2025-[001]-task-name.xml`

### Content Fields

**objective/description**: One clear sentence
- Start with action verb (Implement, Create, Refactor, Test, Deploy)
- State what needs to be achieved
- Avoid implementation details here

**context/description**: Background information
- Why this task exists
- Current state of the system
- How it fits into larger goals
- Any relevant history or constraints

**requirements**: Three categories

*Functional Requirements*: What the system must do
- User-facing features
- Business logic
- Use cases and scenarios
- Expected behaviors

*Technical Requirements*: How it must be built
- Technology choices
- Frameworks and libraries
- APIs and integrations
- Performance targets
- Security requirements

*Quality Standards*: Quality expectations
- Test coverage percentage
- Documentation requirements
- Code style and linting
- Review process

**deliverables**: Concrete outputs
- Be specific (not "authentication" but "Registration endpoint with email validation")
- Include all file types (code, tests, docs, configs)
- Use status="pending" for new tasks

**acceptance_criteria**: How to verify success
- Must be measurable or testable
- Cover functionality, quality, and non-functional requirements
- Use status="unchecked" for new tasks

**error_correction_phase**: Testing workflow
- Adjust commands for specific project
- Include project-specific verification steps
- Define clear success/failure conditions

**handoff_instructions**: Integration points
- Name specific agents for coordination
- List artifacts to share
- Describe integration touchpoints

## Status Attributes

### Deliverable Status

- `pending`: Not started
- `in_progress`: Currently being worked on
- `completed`: Finished and verified
- `blocked`: Waiting on dependency

### Acceptance Criterion Status

- `unchecked`: Not yet verified
- `checked`: Verified and passing
- `failed`: Tested but not meeting criteria

### Error Correction Check Status

- `pending`: Not yet executed
- `passed`: Executed successfully
- `failed`: Needs attention

## Customization Guidelines

### For Different Task Types

**Development Tasks**: Focus on technical requirements, include architecture decisions

**Testing Tasks**: Emphasize quality standards, define coverage targets

**Documentation Tasks**: List all documentation artifacts, specify formats

**Infrastructure Tasks**: Include deployment steps, monitoring requirements

**Skills Tasks**: Reference Skills spec, include validation requirements

### For Different Agents

**Technical Lead**: Include architecture patterns, design decisions

**QA Engineer**: Specify test types, coverage requirements

**DevOps Master**: Detail infrastructure, deployment pipelines

**Skills Master**: Reference best practices, validation scripts

## Validation Checklist

Before using this template:

- [ ] All XML tags properly opened and closed
- [ ] Required fields filled with specific information
- [ ] Agent role path is correct
- [ ] Counter number is unique for date
- [ ] Repository safety requirements included
- [ ] Error correction phase complete
- [ ] Deliverables are specific and measurable
- [ ] Acceptance criteria can be verified
- [ ] No placeholder text remains
- [ ] Forward slashes used in all paths
