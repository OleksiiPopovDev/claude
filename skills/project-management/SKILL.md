---
name: project-management
description: Navigate and understand this project's structure, including agents directory with XML/MD prompt files, templates for task creation, XML-based task management with naming conventions, and development workflows. Use when exploring the codebase structure, understanding project organization, or explaining how agents, tasks, and templates work together.
---

# Project Management System

Understand and work with this project's management structure including agents, tasks, templates, and workflows.

## Project Structure

### Core Directories

**agents/**
- Contains agent prompt files in both XML and MD formats
- Agent prompts define specialized AI roles (Technical Lead, QA Engineer, Task Manager, etc.)
- File naming: `{AGENT_NAME}_PROMPT.xml` or `{AGENT_NAME}_PROMPT.md`
- Referenced in tasks using `@` notation: `@/path/to/AGENT_PROMPT.xml`

**templates/**
- Task templates for different workflows
- `develop_task_template.xml` - Development task structure
- `skill_build_task_template.xml` - Skill creation task structure
- `agent_build_task_template.xml` - Agent creation task structure
- All templates use XML format with structured sections

**commands/**
- Slash command definitions for common operations
- `git/` - Git workflow commands (cm, cp, pr)
- `skill/` - Skill management commands
- Format: Markdown files with command instructions

**docs/**
- Project documentation
- Prompt engineering guides
- Best practices and guidelines
- XML tag usage documentation

**skills/**
- Agent Skills collection (this is part of it)
- Both third-party and project-specific Skills
- Each skill in its own directory with SKILL.md

## Task Management System

### Task File Naming Convention

Format: `{DAY-MONTH-YEAR}-[{COUNTER}]-{TASK-NAME}.xml`

Examples:
- `20-11-2025-[001]-user-authentication.xml`
- `20-11-2025-[002]-api-refactoring.xml`
- `21-11-2025-[001]-new-feature.xml`

Counter Rules:
- Starts at 001 each day
- Increments for each new task on same day
- Resets to 001 for new calendar day
- Always use leading zeros (001, 002, etc.)

### Task XML Structure

Every task file includes these sections:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<task_assignment>
    <header>
        <task_id>Unique identifier</task_id>
        <target_agent_role>@path/to/agent/prompt</target_agent_role>
        <priority>High/Medium/Low</priority>
        <dependencies>Prerequisite tasks</dependencies>
        <task_file>Filename following naming convention</task_file>
    </header>

    <objective>
        <description>Clear goal statement</description>
    </objective>

    <repository_safety_requirements>
        <requirement priority="critical">NO COMMITS</requirement>
        <requirement priority="critical">NO PUSHES</requirement>
        <requirement priority="critical">LOCAL WORK ONLY</requirement>
    </repository_safety_requirements>

    <requirements>
        <functional_requirements>Features needed</functional_requirements>
        <technical_requirements>Technology constraints</technical_requirements>
        <quality_standards>Code quality expectations</quality_standards>
    </requirements>

    <deliverables>
        <deliverable status="pending">Specific output</deliverable>
    </deliverables>

    <acceptance_criteria>
        <criterion status="unchecked">Measurable success condition</criterion>
    </acceptance_criteria>

    <error_correction_phase>
        <steps>Testing and error resolution workflow</steps>
    </error_correction_phase>
</task_assignment>
```

## Repository Safety Rules

**Critical Requirements:**
- NO commits during task execution
- NO pushes to repository
- ALL work remains LOCAL only
- These rules appear in every task file

## Agent System

### Available Agent Roles

Located in `agents/` directory:
- Technical Lead - NestJS/Porto architecture implementation
- QA Engineer - Testing and quality assurance
- Task Manager - Creates structured task assignments
- Git Master - Git commit management
- Logger Inspector - Logging analysis
- Skills Master - Agent Skills development
- DevOps Master - CI/CD and infrastructure

### Agent Reference Format

In task files, reference agents using:
```xml
<target_agent_role>@/path/to/AGENT_PROMPT.xml</target_agent_role>
```

## Workflows

### Creating New Tasks

1. Check existing tasks in target directory for today's date
2. Determine next counter number (find highest + 1)
3. Format filename: `{DATE}-[{COUNTER}]-{name}.xml`
4. Use appropriate template from `templates/`
5. Fill in all required sections
6. Include repository safety requirements
7. Add error correction phase
8. Save with proper XML structure

### Working with Agent Prompts

1. Locate prompt file in `agents/` directory
2. Agent prompts define role, capabilities, and constraints
3. XML format for system-level prompts
4. MD format for detailed instructions
5. Reference in tasks using `@` notation

### Skill Development

1. Use `skill-creator` skill for guidance
2. Create in `skills/` directory
3. Follow YAML frontmatter requirements
4. Validate before packaging
5. Document in skills README

## Error Correction Pattern

All tasks include an error correction phase:

```xml
<error_correction_phase>
    <steps>
        <step number="1">Start Application</step>
        <step number="2">Error Detection & Resolution Loop
            - If success: continue
            - If error: fix and repeat
        </step>
        <step number="3">Port Cleanup</step>
        <step number="4">Verification Checklist</step>
    </steps>
</error_correction_phase>
```

## Key Principles

**Task Management:**
- XML-based structured tasks
- Date-based naming with counters
- Mandatory safety requirements
- Clear acceptance criteria
- Built-in error correction

**Agent Collaboration:**
- Specialized roles with clear boundaries
- Structured handoff instructions
- Reference-based agent assignment
- XML/MD prompt definitions

**Development Workflow:**
- Local-only development
- Iterative error correction
- Template-based task creation
- Validation before completion

## File Path Conventions

- Use forward slashes (/) for all paths (Unix-style)
- Agent references: `@/absolute/path/to/AGENT_PROMPT.xml`
- Relative paths from project root for local files
- Templates stored in `templates/` directory
- Tasks stored in designated task directories

## Common Patterns

**Task Creation Flow:**
1. Analyze request
2. Check existing tasks → determine counter
3. Select appropriate template
4. Structure requirements for target agent
5. Add mandatory sections (safety, error correction)
6. Save with proper naming convention

**Agent Assignment:**
- Human specifies target agent role
- Task Manager creates structured task
- Task includes agent reference path
- Agent executes according to role definition

**Validation Requirements:**
- All XML must be valid
- Task filename matches naming convention
- Counter number is unique for date
- Repository safety rules included
- Error correction phase defined
