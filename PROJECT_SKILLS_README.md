# Project-Specific Agent Skills

This document describes the custom Agent Skills created specifically for this project's development workflow.

## Overview

These Skills provide specialized knowledge about this project's unique patterns, structures, and workflows that extend Claude's capabilities for working with this codebase.

## Available Project Skills

### 1. project-management

**File**: `skills/project-management/SKILL.md`

**Purpose**: Navigate and understand the project's organizational structure

**When to use:**
- Exploring the codebase layout
- Understanding how agents, tasks, and templates work together
- Learning about the project's directory structure
- Need guidance on where files are located

**Key capabilities:**
- Explains agents/ directory with XML/MD prompt files
- Documents templates/ for task creation
- Describes commands/ slash command system
- Details task management system structure

**Trigger terms**: project structure, codebase organization, directory layout, agents directory, templates directory

---

### 2. task-creation

**File**: `skills/task-creation/SKILL.md`

**Purpose**: Generate structured XML task assignments following project conventions

**When to use:**
- Creating new task files for agents
- Need to manage task counter numbers
- Setting up structured development assignments
- Defining deliverables and acceptance criteria

**Key capabilities:**
- Date-based naming with counter management (DD-MM-YYYY-[001]-name.xml)
- XML task structure generation
- Repository safety requirements enforcement
- Error correction phase templates
- Agent role assignment

**Trigger terms**: create task, task file, XML task, task assignment, counter number, task structure

**Reference files:**
- `references/task-template.md` - Complete XML task template

---

### 3. agent-management

**File**: `skills/agent-management/SKILL.md`

**Purpose**: Create and maintain specialized AI agent prompts in XML and Markdown formats

**When to use:**
- Creating new agent prompts
- Updating existing agent roles
- Understanding agent collaboration patterns
- Setting up specialized agent roles

**Key capabilities:**
- XML vs Markdown format selection guidance
- Agent role definition patterns
- Collaboration and handoff workflows
- Safety requirements for agents
- Agent ecosystem design principles

**Trigger terms**: agent prompt, agent role, create agent, XML agent, agent collaboration, agent system

---

## Integration with Existing Skills

These project-specific Skills work alongside the general-purpose Skills already in the `skills/` directory:

**Development Support:**
- `skill-creator` - For creating new Skills
- `debugging/*` - Systematic debugging approaches
- `problem-solving/*` - Advanced problem-solving techniques

**Technical Domains:**
- `nextjs` - Next.js framework
- `docker` - Containerization
- `cloudflare*` - Cloudflare services
- `mongodb`, `postgresql-psql` - Databases

**Document Processing:**
- `document-skills/*` - PDF, Excel, Word, PowerPoint
- `canvas-design` - Visual design creation

## Skill Discovery

Claude automatically discovers and activates these Skills when:

1. **Keywords match description** - The Skill description contains relevant trigger terms
2. **Context indicates need** - The conversation context suggests the Skill would be helpful
3. **Explicit reference** - User mentions the Skill by name or category

## Progressive Disclosure Architecture

All Skills follow a three-level loading pattern:

1. **Metadata (Always loaded)**: Name and description (~100 tokens)
2. **SKILL.md body (Loaded when triggered)**: Main instructions (<500 lines)
3. **Reference files (Loaded as needed)**: Detailed documentation (unlimited)

This keeps context windows efficient while providing deep knowledge when required.

## Validation Standards

All project Skills meet these requirements:

**YAML Frontmatter:**
- `name`: Max 64 chars, lowercase/numbers/hyphens only
- `description`: Max 1024 chars, includes what AND when to use
- No XML tags, no reserved words ("anthropic", "claude")

**Content Quality:**
- SKILL.md body under 500 lines
- Forward slashes (/) for all file paths
- Progressive disclosure implemented
- Concise, assuming Claude's intelligence
- No time-sensitive information

**Structure:**
- Complete sections with clear headers
- Concrete examples (not abstract)
- Workflows with actionable steps
- File references one level deep from SKILL.md

## Development Workflow Integration

### Task Creation Flow

```
User Request
    ↓
project-management Skill → Understanding project structure
    ↓
task-creation Skill → Generate XML task file
    ↓
agent-management Skill → Reference correct agent
    ↓
Task File Created
```

### Agent Development Flow

```
Need New Agent Role
    ↓
agent-management Skill → Design agent prompt
    ↓
skill-creator Skill → Create Skill for agent (if needed)
    ↓
project-management Skill → Understand integration points
    ↓
New Agent Ready
```

## Common Usage Patterns

### Creating a New Development Task

```
1. Use project-management to understand task storage location
2. Use task-creation to generate XML with correct counter
3. Use agent-management to reference appropriate agent
4. Save task file with proper naming convention
```

### Understanding Project Organization

```
1. Trigger project-management Skill
2. Learn about agents/, templates/, commands/ directories
3. Understand how pieces fit together
4. Apply knowledge to current task
```

### Setting Up New Agent

```
1. Use agent-management for prompt structure
2. Choose XML or Markdown format
3. Define role, capabilities, constraints
4. Add to agents/ directory
5. Update task templates to reference new agent
```

## Skill Authoring Notes

These Skills were created following Anthropic's best practices:

**Conciseness Principle**: Only include information Claude doesn't already have. Challenge each piece: "Does Claude really need this explanation?"

**Evaluation-Driven**: Designed based on actual usage patterns observed in the project.

**Appropriate Freedom**: Medium freedom level - preferred patterns exist, but some variation acceptable based on context.

**Progressive Disclosure**: Essential information in SKILL.md, detailed references in separate files.

## Future Skill Ideas

Potential Skills to add as patterns emerge:

- **testing-workflows** - Project-specific testing patterns
- **deployment-procedures** - CI/CD and deployment workflows
- **code-review-standards** - Project code quality expectations
- **documentation-generation** - Project documentation conventions

## Maintenance

### When to Update Skills

- New project patterns identified
- Workflow improvements discovered
- Integration points change
- Naming conventions evolve
- Best practices updated

### Update Process

1. Identify what needs to change
2. Update SKILL.md or reference files
3. Re-validate with validation script
4. Test with representative prompts
5. Document changes in commit message

### Validation Commands

```bash
# Validate individual Skill
python3 skills/skill-creator/scripts/validate_skill.py skills/project-management/SKILL.md

# Quick validation during development
python3 skills/skill-creator/scripts/quick_validate.py skills/project-management/

# Package for distribution
python3 skills/skill-creator/scripts/package_skill.py skills/project-management/
```

## Support and Questions

For questions about these Skills:

1. **Skill usage**: Activate the relevant Skill and ask Claude directly
2. **Skill creation**: Use the `skill-creator` Skill for guidance
3. **Project patterns**: Consult `project-management` Skill
4. **Task management**: Reference `task-creation` Skill
5. **Agent system**: Check `agent-management` Skill

## Version History

**Version 1.0** (November 20, 2025)
- Initial creation of project-specific Skills
- project-management: Project structure navigation
- task-creation: XML task generation with counter management
- agent-management: Agent prompt creation and maintenance

---

*These Skills were created following the comprehensive best practices documented in the skill-creator Skill and Anthropic's Agent Skills guidelines.*
