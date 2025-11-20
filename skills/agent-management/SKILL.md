---
name: agent-management
description: Create, update, and maintain specialized AI agent prompts stored in XML and Markdown formats. This skill covers agent role definitions, capabilities, constraints, and best practices for agent prompt authoring. Use when creating new agent prompts, updating existing agents, understanding agent roles, or when users mention agent creation, agent prompts, or role-based AI systems.
---

# Agent Management System

Create and maintain specialized AI agent prompts that define roles, capabilities, and constraints for different development tasks.

## Agent Prompt Formats

### XML Format (System-Level)

Used for structural, system-level agent definitions with complex nested configurations.

**Location**: `agents/{AGENT_NAME}_PROMPT.xml`

**Use cases:**
- Task management systems
- Multi-agent coordination
- Structured workflow definitions
- Configuration-heavy agents

**Structure:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<agent_name_system>
    <role_definition>
        Clear description of agent's primary function
    </role_definition>

    <critical_safety_rules>
        Mandatory operational constraints
    </critical_safety_rules>

    <capabilities>
        What the agent can do
    </capabilities>

    <workflows>
        Step-by-step processes
    </workflows>

    <examples>
        Concrete usage examples
    </examples>
</agent_name_system>
```

### Markdown Format (Instructional)

Used for narrative, instructional agent prompts with detailed guidelines.

**Location**: `agents/{AGENT_NAME}_PROMPT.md`

**Use cases:**
- Development roles (Technical Lead, QA Engineer)
- Specialized technical tasks
- Documentation-heavy agents
- Principle-based guidance

**Structure:**
```markdown
---
name: Agent Name
description: Brief role summary
color: visual identifier
model: preferred Claude model
---

# Agent Role Title

## Role Definition

Clear statement of agent's purpose and responsibilities.

## Capabilities

Bullet list of what the agent can do.

## Constraints

What the agent must not do or must always consider.

## Workflows

### Workflow Name

Step-by-step process descriptions.

## Best Practices

Guidelines for effective execution.

## Examples

Concrete usage scenarios.
```

## Available Agent Roles

### Technical Lead
- **File**: `TECHNICAL_LEAD_PROMPT.xml` or `.md`
- **Purpose**: NestJS/Porto architecture implementation
- **Specialization**: Server-side development, API design
- **Use when**: Building backend features, implementing business logic

### QA Engineer
- **File**: `QA_ENGINEER_PROMPT.md`
- **Purpose**: Testing and quality assurance
- **Specialization**: Test coverage, quality metrics
- **Use when**: Writing tests, ensuring code quality

### Task Manager
- **File**: `TASK_MANAGER_PROMPT.xml`
- **Purpose**: Creates structured task assignments
- **Specialization**: XML task generation, counter management
- **Use when**: Creating new task files for agents

### Skills Master
- **File**: `SKILLS_MASTER_AGENT.xml`
- **Purpose**: Agent Skills development
- **Specialization**: YAML validation, Skill authoring
- **Use when**: Creating or updating Agent Skills

### Git Master
- **File**: `GIT_MASTER_PROMPT.md`
- **Purpose**: Git workflow management
- **Specialization**: Commit messages, PR creation
- **Use when**: Managing git operations, creating PRs

### Logger Inspector
- **File**: `LOGGER_INSPECTOR_PROMPT.md`
- **Purpose**: Logging analysis and optimization
- **Specialization**: Log structure, debugging
- **Use when**: Analyzing logs, improving logging

### DevOps Master
- **File**: `DEVOPS_MASTER_PROMPT.md`
- **Purpose**: CI/CD and infrastructure
- **Specialization**: Deployment, monitoring, automation
- **Use when**: Setting up pipelines, infrastructure work

## Creating New Agent Prompts

### Step 1: Define Agent Role

Ask these questions:
- What specific problem does this agent solve?
- What tasks will this agent repeatedly perform?
- What domain expertise does this agent need?
- How does this agent collaborate with others?

### Step 2: Choose Format

**Choose XML when:**
- Agent needs structured configuration
- Complex nested workflows
- Multiple interconnected sections
- System-level coordination

**Choose Markdown when:**
- Agent needs narrative guidance
- Principle-based instructions
- Heavy documentation requirements
- Conversational workflow descriptions

### Step 3: Define Core Sections

**Role Definition**
- One clear sentence describing primary purpose
- Scope of responsibilities
- Position in agent ecosystem

**Capabilities**
- Specific technical skills
- Tools and technologies
- Integration points
- Domain knowledge areas

**Constraints**
- Safety requirements (especially repository safety)
- Technical limitations
- Quality standards
- Collaboration boundaries

**Workflows**
- Step-by-step processes
- Decision trees
- Error handling procedures
- Validation checkpoints

### Step 4: Add Safety Requirements

**Mandatory for all agents:**
```xml
<critical_safety_rules>
    <rule priority="critical">NO COMMITS to repository</rule>
    <rule priority="critical">NO PUSHES to repository</rule>
    <rule priority="critical">LOCAL WORK ONLY</rule>
</critical_safety_rules>
```

Or in Markdown:
```markdown
## Critical Safety Rules

- **NO COMMITS**: Never commit changes to the repository
- **NO PUSHES**: Never push changes to the repository
- **LOCAL ONLY**: All development work must remain local
```

### Step 5: Include Examples

**Concrete scenarios showing:**
- Input: What the agent receives
- Process: How the agent thinks through the task
- Output: What the agent produces
- Edge cases: How the agent handles special situations

### Step 6: Validate and Test

**Validation checklist:**
- [ ] Role is clearly defined
- [ ] Capabilities are specific
- [ ] Safety rules included
- [ ] Workflows are actionable
- [ ] Examples are concrete
- [ ] File naming follows convention
- [ ] Format (XML/MD) is appropriate

## Agent Prompt Best Practices

### Clarity

**Clear role definition:**
```
✅ "Technical Lead specialized in implementing NestJS applications following Porto architecture patterns with emphasis on Actions and Tasks layers."

❌ "Helps with backend development and stuff."
```

**Specific capabilities:**
```
✅ "Create service classes following Porto structure, implement repository patterns, design API controllers with proper validation."

❌ "Can write backend code."
```

### Actionability

**Concrete steps:**
```xml
<step number="1">
    <name>Analyze Requirements</name>
    <actions>
        <action>Review task objectives and acceptance criteria</action>
        <action>Identify required Actions and Tasks</action>
        <action>Check for existing similar implementations</action>
    </actions>
</step>
```

**Avoid vague guidance:**
```
❌ "Think about the problem and solve it well."
```

### Safety

**Always include repository safety:**
- Every agent must have explicit no-commit/no-push rules
- State safety requirements in multiple places if needed
- Make constraints impossible to miss

**Error prevention:**
- Include validation steps
- Define what to check before completion
- Specify error recovery procedures

### Collaboration

**Define handoff points:**
```xml
<collaboration>
    <handoff_to agent="@agents/QA_ENGINEER_PROMPT.md">
        After implementation complete, provide:
        - List of new functions/endpoints
        - Test coverage expectations
        - Known edge cases
    </handoff_to>
</collaboration>
```

**Clear boundaries:**
- What this agent does
- What this agent doesn't do
- When to involve other agents

## Updating Existing Agents

### When to Update

- New capabilities added to agent role
- Workflow improvements identified
- Safety requirements changed
- Integration points evolved
- Best practices updated

### Update Process

1. **Read current prompt** - Understand existing structure
2. **Identify changes** - What needs to be added/modified/removed
3. **Maintain consistency** - Keep existing structure and format
4. **Update examples** - Ensure examples reflect changes
5. **Validate** - Test updated prompt with representative tasks
6. **Document changes** - Note what was changed and why

### Versioning Strategy

**For significant changes:**
- Keep a copy of previous version
- Document migration path
- Update all tasks referencing this agent

**For minor updates:**
- Direct file updates
- No versioning needed
- Ensure backward compatibility

## Agent Referencing

### In Task Files

```xml
<target_agent_role>@agents/TECHNICAL_LEAD_PROMPT.xml</target_agent_role>
```

### Path Format Rules

- Always use `@` prefix for agent references
- Use forward slashes (/) for paths
- Include file extension (.xml or .md)
- Path can be absolute or relative to project root

### Validation

**Check agent reference:**
```bash
# Verify agent file exists
ls agents/TECHNICAL_LEAD_PROMPT.xml

# Verify it's readable
cat agents/TECHNICAL_LEAD_PROMPT.xml | head
```

## Agent Ecosystem Design

### Specialization

**Each agent should:**
- Have one clear primary role
- Excel in specific domain
- Have well-defined boundaries
- Know when to hand off to others

**Avoid:**
- Overly broad "do everything" agents
- Overlapping responsibilities
- Unclear role boundaries

### Collaboration

**Design for teamwork:**
- Define explicit handoff points
- Specify what artifacts to share
- Document coordination requirements
- Enable parallel work where possible

**Example collaboration flow:**
```
Technical Lead → Implements feature
    ↓ (hands off: code, test requirements)
QA Engineer → Creates test suite
    ↓ (hands off: test report, issues)
Technical Lead → Fixes issues
    ↓ (hands off: updated code)
DevOps Master → Deploys to environment
```

### Model Selection

**Guidelines:**
- Haiku: Simple, repetitive tasks
- Sonnet: Standard development work (default)
- Opus: Complex reasoning, architecture decisions

**Specify in Markdown frontmatter:**
```yaml
---
model: claude-sonnet-4-5-20250929
---
```

## File Organization

### Directory Structure

```
agents/
├── TECHNICAL_LEAD_PROMPT.xml
├── TECHNICAL_LEAD_PROMPT.md
├── QA_ENGINEER_PROMPT.md
├── TASK_MANAGER_PROMPT.xml
├── SKILLS_MASTER_AGENT.xml
├── GIT_MASTER_PROMPT.md
├── LOGGER_INSPECTOR_PROMPT.md
└── DEVOPS_MASTER_PROMPT.md
```

### Naming Conventions

**Format:** `{AGENT_NAME}_PROMPT.{xml|md}`

**Examples:**
- `BACKEND_DEVELOPER_PROMPT.xml`
- `FRONTEND_SPECIALIST_PROMPT.md`
- `DATABASE_ARCHITECT_PROMPT.md`

**Rules:**
- ALL_CAPS for agent name
- Underscore separators
- Descriptive names
- Consistent suffixes (_PROMPT, _AGENT)

## Common Agent Patterns

### Development Agent

**Focus:** Implementing features, writing code

**Key sections:**
- Technical stack and frameworks
- Architecture patterns to follow
- Code quality standards
- Testing expectations
- Documentation requirements

### Quality Assurance Agent

**Focus:** Testing, validation, quality metrics

**Key sections:**
- Test types and coverage targets
- Quality metrics to track
- Validation procedures
- Issue reporting format
- Regression testing approach

### Infrastructure Agent

**Focus:** Deployment, monitoring, operations

**Key sections:**
- Deployment procedures
- Monitoring setup
- Alerting configuration
- Backup strategies
- Disaster recovery

### Coordination Agent

**Focus:** Task management, workflow orchestration

**Key sections:**
- Task creation procedures
- Counter management
- Agent assignment logic
- Handoff coordination
- Status tracking

## Quality Checklist

Before finalizing any agent prompt:

- [ ] Role is clearly defined in one sentence
- [ ] Capabilities list is specific and actionable
- [ ] Safety rules explicitly stated
- [ ] Workflows have concrete steps
- [ ] Examples demonstrate real usage
- [ ] Collaboration points defined
- [ ] File naming follows convention
- [ ] Format (XML/MD) is appropriate
- [ ] No Windows-style paths
- [ ] Tested with representative task

## Advanced Features

### Conditional Workflows

```xml
<workflow name="implementation">
    <step>Implement feature</step>
    <conditional>
        <if condition="feature involves data persistence">
            <then>Coordinate with Database Architect</then>
        </if>
        <if condition="feature has user interface">
            <then>Coordinate with Frontend Developer</then>
        </if>
    </conditional>
</workflow>
```

### Context-Aware Guidance

```markdown
## Context-Aware Decisions

### When implementing API endpoints:
- RESTful: Follow REST conventions
- GraphQL: Use schema-first approach
- WebSocket: Consider connection lifecycle

### When writing tests:
- Unit tests: Focus on business logic
- Integration: Test API contracts
- E2E: Cover critical user journeys
```

### Dynamic Templates

```xml
<template name="feature_implementation">
    <placeholders>
        <placeholder name="feature_name"/>
        <placeholder name="affected_layers"/>
        <placeholder name="integration_points"/>
    </placeholders>
    <structure>
        <!-- Template structure using placeholders -->
    </structure>
</template>
```

## Troubleshooting

### Agent Not Activating

**Check:**
- File exists at referenced path
- File extension is correct
- Path uses forward slashes
- @ prefix included in reference

### Agent Behavior Inconsistent

**Review:**
- Role definition clarity
- Workflow step ambiguity
- Example relevance
- Safety rule emphasis

### Agent Scope Too Broad

**Solutions:**
- Split into multiple specialized agents
- Define clearer boundaries
- Specify explicit handoff points
- Remove overlapping responsibilities

### Agent Collaboration Issues

**Verify:**
- Handoff instructions are clear
- Required artifacts are specified
- Timing of handoffs is defined
- Communication format is consistent

## Quick Reference

**Agent file format:**
```
agents/{AGENT_NAME}_PROMPT.{xml|md}
```

**Required sections:**
- Role definition
- Capabilities
- Safety rules
- Workflows
- Examples

**Referencing agents:**
```xml
<target_agent_role>@agents/{NAME}_PROMPT.{xml|md}</target_agent_role>
```

**Format selection:**
- XML: Structured, system-level
- Markdown: Narrative, instructional
