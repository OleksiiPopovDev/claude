# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Claude Code agent system configuration repository containing specialized AI agent prompts, skills, documentation, and task templates. The system enables creating, managing, and deploying role-specific AI agents that follow Anthropic's best practices for prompt engineering.

## Architecture

### Directory Structure

```
~/.claude/
├── agents/          # Specialized agent prompt files (XML format)
├── skills/          # Global and project-specific skills
├── docs/            # Prompt engineering documentation and best practices
├── templates/       # Task creation templates
├── commands/        # Custom slash commands
└── tasks/           # Generated task assignments (ignored in git)
```

### Agent System

The repository implements a **multi-agent ecosystem** where specialized agents collaborate:

- **Agent Builder** (`AGENT_BUILDER_PROMPT.xml`) - Creates and edits agent prompts
- **Skills Master** (`SKILLS_MASTER_AGENT.xml`) - Creates project-specific skills
- **Task Manager** (`TASK_MANAGER_PROMPT.xml`) - Generates structured task assignments
- **DevOps Master** (`DEVOPS_MASTER_PROMPT.xml`) - Infrastructure automation
- **Technical Lead** (`TECHNICAL_LEAD_PROMPT.xml`) - Code architecture guidance

### Agent File Format

All agents follow this structure:

```yaml
---
name: Agent Name
description: What the agent does AND when to use it
color: visual-identifier
model: claude-opus-4-1-20250805
---
```

Followed by XML body containing:
- `<metadata>` - Agent identification and version
- `<role>` - Clear identity and expertise definition
- `<workflow>` - Phased execution steps
- `<standards_and_requirements>` - Quality criteria
- `<examples>` - Correct and incorrect patterns (using CDATA)
- `<validation_checklist>` - Quality assurance
- `<anti_patterns>` - What to avoid

## Key Principles

### Prompt Engineering Standards

This repository follows Anthropic's official best practices (see `docs/`):

1. **XML Structuring** - All prompts use XML tags for clarity, parseability, and flexibility
2. **Role-Based Prompting** - Each agent has explicit identity and domain expertise
3. **Progressive Disclosure** - Information layered from general to specific
4. **Complete Output** - Never use placeholders or partial updates (see `docs/why_are_you_gay.md`)
5. **Multi-Shot Examples** - Both correct ✓ and incorrect ❌ patterns shown

### File Naming Conventions

**Agents:**
- Format: `[AGENT_NAME]_PROMPT.xml`
- Location: `~/.claude/agents/`
- Example: `SKILLS_MASTER_AGENT.xml`

**Tasks:**
- Format: `{DAY-MONTH-YEAR}-[{COUNTER}]-{task-name}.xml`
- Location: `~/.claude/tasks/` (or project-specific)
- Counter: 001, 002, 003... (resets daily)
- Example: `20-11-2025-[001]-build-agent-system.xml`

**Skills:**
- Format: `{skill-name}/SKILL.md`
- Location: `~/.claude/skills/` or `{project}/.claude/skills/`
- YAML frontmatter required with name, description
- Must pass validation: `python3 ~/.claude/skills/skill-creator/scripts/validate_skill.py`

## Working with Agents

### Creating New Agents

Use the Agent Builder agent:

```bash
# Reference the agent builder
@~/.claude/agents/AGENT_BUILDER_PROMPT.xml
```

Required reading before creating agents:
- `docs/prompting_best_practices.md` - Anthropic's official guidelines
- `docs/use_xml_tags.md` - XML structuring patterns
- `docs/giving_claude_a_role_with_a_system_prompt.md` - Role prompting
- `docs/why_are_you_gay.md` - Output quality rules

Study existing agents for patterns:
- `agents/DEVOPS_MASTER_PROMPT.xml` - Pure XML structure
- `agents/SKILLS_MASTER_AGENT.xml` - YAML + XML hybrid
- `agents/TASK_MANAGER_PROMPT.xml` - Task generation patterns

### Creating Skills

Use the Skills Master agent and skill-creator skill:

```bash
# Validate a skill
python3 ~/.claude/skills/skill-creator/scripts/validate_skill.py path/to/SKILL.md

# Initialize new skill from template
python3 ~/.claude/skills/skill-creator/scripts/init_skill.py skill-name --path output-dir

# Package skill for distribution
python3 ~/.claude/skills/skill-creator/scripts/package_skill.py path/to/skill-folder
```

**Skill Requirements:**
- YAML frontmatter with name (max 64 chars, lowercase/hyphens/numbers)
- Description including WHAT and WHEN to use (max 1024 chars)
- SKILL.md body under 500 lines
- Total size under 8MB
- Minimum 3 evaluations per skill
- Progressive disclosure (metadata → instructions → resources)

### Creating Tasks

Use templates in `templates/`:

- `agent_build_task_template.xml` - For agent creation tasks
- `skill_build_task_template.xml` - For skill creation tasks
- `develop_task_template.xml` - For development tasks

All tasks include:
- Task ID and priority
- Target agent role (XML file reference)
- Objective and context
- Requirements (functional, technical, quality)
- Deliverables with status tracking
- Acceptance criteria
- Error correction phase
- Repository safety requirements (NO COMMITS/PUSHES unless explicitly requested)

## Path Conventions

Use **portable paths** with tilde notation:

```xml
<!-- CORRECT -->
<doc>@~/.claude/docs/prompting_best_practices.md</doc>
<agent>@~/.claude/agents/SKILLS_MASTER_AGENT.xml</agent>

<!-- INCORRECT -->
<doc>@/Users/oleksii/.claude/docs/prompting_best_practices.md</doc>
```

Always use **Unix-style forward slashes**:
```
~/.claude/skills/skill-name/SKILL.md  ✓
~/.claude\skills\skill-name\SKILL.md  ❌
```

## Quality Standards

### Validation Checklist for Agents

- [ ] YAML frontmatter with all required fields
- [ ] Well-formed XML structure (all tags closed)
- [ ] Clear role definition with identity statement
- [ ] Phased workflow with numbered steps
- [ ] Concrete examples (correct and incorrect)
- [ ] Measurable success criteria
- [ ] Anti-patterns documented
- [ ] Consistent tag naming
- [ ] CDATA sections for code examples

### Validation Checklist for Skills

- [ ] Passes validation script with zero errors
- [ ] Description includes WHAT and WHEN
- [ ] SKILL.md under 500 lines
- [ ] Minimum 3 evaluations created
- [ ] Progressive disclosure implemented
- [ ] File paths use forward slashes
- [ ] No time-sensitive information
- [ ] No reserved words in name

## Integration Points

### MCP Servers Referenced

- **vibe-kanban** - Task/project management integration
- **context7** - Library documentation retrieval
- **octocode** - GitHub code navigation
- **playwright** - Browser automation

### Global Skills Available

The `~/.claude/skills/` directory contains 40+ global skills including:
- `skill-creator` - Primary skill for creating/validating skills
- Document processing (PDF, XLSX, DOCX, PPTX)
- Cloud platforms (Cloudflare, GCloud)
- Frameworks (Next.js, Shopify, NestJS)
- AI services (Gemini document/audio/video/vision)
- Development tools (Docker, FFmpeg, PostgreSQL)

## Anti-Patterns to Avoid

❌ **Don't** use Windows-style paths (`\`)
❌ **Don't** create tasks without checking counter
❌ **Don't** skip validation scripts
❌ **Don't** use vague agent descriptions
❌ **Don't** commit without explicit user request
❌ **Don't** create partial/placeholder output
❌ **Don't** duplicate global skills in projects
❌ **Don't** exceed 500 lines in SKILL.md body

## Critical Safety Rules

From Task Manager agent:

1. **NEVER** commit changes unless explicitly requested
2. **NEVER** push changes unless explicitly requested
3. **ALL** development work remains LOCAL by default
4. Check existing task files before creating new ones (to get correct counter)

## References

Always reference these core documents when working with this system:

- `docs/prompting_best_practices.md` - Anthropic's best practices
- `docs/use_xml_tags.md` - XML structuring guide
- `docs/giving_claude_a_role_with_a_system_prompt.md` - Role prompting
- `docs/prompt_engineering_overview.md` - General principles
- `docs/why_are_you_gay.md` - Output quality rules (mandatory reading)
- `docs/using_agent_skills_with_the_api.md` - Skills API integration
