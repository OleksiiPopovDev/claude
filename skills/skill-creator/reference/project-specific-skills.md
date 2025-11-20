# Project-Specific Skills Guide

Guide for creating Skills that are specific to a particular project's patterns, workflows, and conventions.

## What are Project-Specific Skills?

Project-specific Skills extend Claude's capabilities for working with a particular codebase by encoding:
- Project structure and organization patterns
- Custom workflows and processes (e.g., task management, agent systems)
- File naming conventions and formats
- Project-specific templates and patterns
- Team conventions and best practices

Unlike general-purpose Skills (like `pdf` or `nextjs`), project-specific Skills are tailored to one project's unique needs.

## When to Create Project-Specific Skills

Create project-specific Skills when:

✅ **Project has unique patterns** - Custom task management, agent systems, specific workflows
✅ **Patterns are repeatable** - Same processes used multiple times
✅ **Context is non-obvious** - Claude wouldn't know these patterns without documentation
✅ **Benefits multiple use cases** - Useful across different tasks in the project

Don't create project-specific Skills when:
❌ One-time operations
❌ Standard patterns Claude already knows
❌ Project patterns that change frequently
❌ Better served by general documentation

## Identifying Project Patterns

### Analysis Process

1. **Review project structure**
   - Look at directory organization
   - Identify file naming patterns
   - Note configuration files and templates

2. **Document workflows**
   - How are tasks created?
   - How do different parts interact?
   - What processes are repeated?

3. **Find unique conventions**
   - Custom formats (XML task files, agent prompts)
   - Naming conventions (date-based counters)
   - Mandatory requirements (safety rules, error correction)

4. **Identify integration points**
   - How do different systems connect?
   - What handoff patterns exist?
   - Where do agents collaborate?

### Example: Task Management System

**Project pattern identified:**
- XML task files with specific structure
- Date-based naming: `DD-MM-YYYY-[COUNTER]-name.xml`
- Counter management (unique per day)
- Mandatory safety requirements
- Error correction phases

**Skill needed:** `task-creation` - Generate XML tasks following conventions

## Skill Architecture for Projects

### Common Project-Specific Skill Types

**1. Project Navigation Skills**
- **Purpose**: Help understand project structure
- **Contains**: Directory layout, file locations, organization patterns
- **Example**: `project-management` - Documents agents/, templates/, commands/

**2. Workflow Skills**
- **Purpose**: Guide through project-specific processes
- **Contains**: Step-by-step workflows, checklists, validation
- **Example**: `task-creation` - XML task generation with counter management

**3. Convention Skills**
- **Purpose**: Encode project conventions and patterns
- **Contains**: Naming conventions, format requirements, templates
- **Example**: `agent-management` - Agent prompt creation (XML/MD)

**4. Integration Skills**
- **Purpose**: Connect different project systems
- **Contains**: API patterns, handoff procedures, collaboration workflows
- **Example**: Agent collaboration patterns, task-agent references

### Skill Composition Patterns

**Pattern 1: Layered Skills**
```
project-management (structure)
    ↓ references
task-creation (uses structure knowledge)
    ↓ references
agent-management (uses both above)
```

**Pattern 2: Modular Skills**
```
Each Skill handles one aspect:
- project-management → Structure navigation
- task-creation → Task generation
- agent-management → Agent prompts

Skills reference each other when needed
```

**Pattern 3: Hierarchical Skills**
```
Core Skill (project-overview)
    ↓
Specialized Skills (tasks, agents, deployment)
    ↓
Domain-specific Skills (specific features)
```

## Creating Project-Specific Skills

### Step 1: Identify Project Patterns

**Questions to ask:**
- What makes this project's structure unique?
- What workflows are repeated frequently?
- What conventions must be followed?
- What would Claude struggle with without guidance?

**Document:**
- File structures
- Naming conventions
- Required patterns
- Mandatory sections
- Integration points

### Step 2: Define Skill Boundaries

**For each identified pattern:**
- Is this one Skill or multiple?
- What's the primary trigger?
- What's included vs. referenced?
- How does it relate to other Skills?

**Decision criteria:**
- **Separation**: Different triggers, different concerns
- **Combination**: Tightly coupled, always used together
- **Reference**: One builds on another

### Step 3: Structure Skill Content

**SKILL.md structure for project Skills:**

```markdown
# [Skill Name]

[Brief purpose - what project pattern this handles]

## Quick Start
[Minimal steps to use the pattern]

## [Project Component]
[Explanation of specific project component]

## [Workflow/Process]
[Step-by-step guidance for project process]

## [Conventions]
[Project-specific conventions and rules]

## Common Patterns
[Typical usage scenarios in the project]

## Validation/Verification
[How to verify correct usage]

## Integration Points
[How this connects with other project parts]
```

**Reference files for project Skills:**
- Templates (complete examples)
- Detailed workflows (multi-step processes)
- Validation rules (comprehensive checklists)
- Examples (concrete scenarios)

### Step 4: Emphasize Critical Requirements

**Mandatory elements** (project safety rules, required sections):
- State multiple times if critical
- Use emphasis (CRITICAL, MANDATORY, MUST)
- Show examples of correct usage
- Explain consequences of omission

**Example: Repository safety in task-creation:**
```markdown
## Repository Safety Requirements

**MANDATORY in every task:**

[Shows XML structure]

**CRITICAL**: These rules can never be omitted.
```

### Step 5: Create Project-Specific Examples

**Use actual project patterns:**
- Real file names from the project
- Actual directory structures
- Genuine workflow scenarios
- Project-specific terminology

**Don't use generic examples** - use patterns specific to this project.

### Step 6: Cross-Reference Skills

**When Skills relate:**
- Reference by name in description
- Link in "See also" sections
- Show integration workflows
- Document handoff points

**Example:**
```markdown
## Integration with Other Skills

This Skill works with:
- `project-management` - Understanding where to save files
- `agent-management` - Referencing agent prompts correctly
```

## Project Skills Best Practices

### 1. Document Actual Patterns, Not Ideals

✅ Document what the project actually does
❌ Document what it "should" do or "will" do

Use real file names, actual directory structures, existing conventions.

### 2. Make Critical Rules Impossible to Miss

For project-critical requirements:
- State in multiple places
- Use emphasis and formatting
- Show correct examples
- Explain why it matters

### 3. Include Concrete Project Examples

✅ `20-11-2025-[001]-user-auth.xml` (actual format)
❌ `YYYY-MM-DD-[NNN]-task-name.xml` (abstract format)

Use both, but emphasize concrete examples.

### 4. Keep Skills Focused

Each Skill should handle one clear aspect:
- Structure navigation
- File creation
- Convention enforcement

Don't create "project-everything" Skills.

### 5. Plan for Updates

Project patterns evolve:
- Version Skill with project
- Note when patterns changed
- Update examples to match reality
- Keep Skills in sync with codebase

### 6. Test with Real Scenarios

Create evaluations using:
- Actual project tasks
- Real file names and structures
- Genuine workflow scenarios
- Project-specific edge cases

## Common Project Patterns

### Pattern: File Naming Conventions

**When project has specific naming rules:**

```markdown
## File Naming Convention

Format: `{DATE}-[{COUNTER}]-{name}.ext`

Examples:
- `20-11-2025-[001]-auth-system.xml`
- `20-11-2025-[002]-api-refactor.xml`

Counter Rules:
- Starts at 001 each day
- [Specific counter management workflow]
```

### Pattern: Mandatory Sections

**When files must contain specific sections:**

```markdown
## Required Sections

MANDATORY in every file:
1. [Section name and purpose]
2. [Section name and purpose]

[Show complete example with all sections]
```

### Pattern: Reference Systems

**When project uses specific reference formats:**

```markdown
## Reference Format

Use @ notation: `@path/to/resource.ext`

Examples:
- `@agents/TECHNICAL_LEAD.xml`
- `@templates/task_template.xml`
```

### Pattern: Workflow Checklists

**When process has critical steps:**

```markdown
## Critical Workflow

ALWAYS follow this sequence:

1. [ ] Check existing files
2. [ ] Determine counter number
3. [ ] Validate format
4. [ ] Create file
5. [ ] Verify structure
```

### Pattern: Safety Requirements

**When project has safety rules:**

```markdown
## Safety Requirements

**MANDATORY - Cannot be omitted:**

- Rule 1 (with example)
- Rule 2 (with example)
- Rule 3 (with example)

These appear in every [file type].
```

## Multi-Skill Project Documentation

### Creating a Skills Index

Create `PROJECT_SKILLS_README.md` in project root:

```markdown
# Project-Specific Skills

## Available Skills

### skill-name-1
- Purpose: [What it does]
- When to use: [Trigger scenarios]
- Key features: [Capabilities]

### skill-name-2
[Same structure]

## Integration Workflows

[How Skills work together]

## Skill Development

[How to create/update project Skills]
```

### Skill Discovery Pattern

**Help Claude find the right Skill:**

**Good descriptions:**
```yaml
description: Generate XML task files with date-based naming (DD-MM-YYYY-[COUNTER]-name.xml), counter management, and mandatory safety requirements. Use when creating tasks, task files, or XML assignments.
```

**Include:**
- Specific formats and patterns
- Key terminology from project
- When phrases (creating, generating, managing)
- Project-specific terms (task files, counters, assignments)

## Example: Complete Project Skill

### task-creation Skill

**Purpose**: Generate XML task files following project conventions

**Key patterns documented:**
- File naming: `DD-MM-YYYY-[COUNTER]-name.xml`
- Counter management (daily reset, uniqueness)
- XML structure requirements
- Mandatory safety sections
- Error correction phases
- Agent references

**Structure:**
```
task-creation/
├── SKILL.md (workflow, quick reference)
└── references/
    └── task-template.md (complete XML template)
```

**Integration:**
- References `project-management` for structure
- References `agent-management` for agent paths
- Used by Task Manager agent

**Evaluations:**
1. Counter management workflow
2. XML structure validation
3. Agent assignment process

## Validation for Project Skills

### Project-Specific Checks

Beyond standard validation:
- [ ] Uses actual project terminology
- [ ] Examples match project reality
- [ ] File paths match project structure
- [ ] References existing project files
- [ ] Integrates with other project Skills
- [ ] Mandatory project rules emphasized
- [ ] Tested with real project scenarios

### Integration Validation

- [ ] Skills reference each other correctly
- [ ] No circular dependencies
- [ ] Handoff points clear
- [ ] Terminology consistent across Skills
- [ ] Examples compatible

## Maintenance Strategy

### When to Update Project Skills

**Update when:**
- Project patterns change
- New conventions adopted
- Workflows evolve
- Integration points modified
- Errors or omissions found

**Update process:**
1. Identify what changed in project
2. Update affected Skills
3. Update cross-references
4. Re-validate
5. Test with current scenarios
6. Document changes

### Versioning Project Skills

**Option 1: Version with project**
- Skills updated when project structure changes
- Keep Skills in project repository
- Version control tracks changes

**Option 2: Independent versioning**
- Skills maintained separately
- Note compatibility with project versions
- Update as needed

## Summary

**Project-specific Skills succeed when they:**
1. Document actual project patterns (not ideals)
2. Focus on non-obvious, repeatable workflows
3. Use concrete project examples
4. Make critical requirements impossible to miss
5. Integrate clearly with other Skills
6. Stay synchronized with project evolution

**Create project Skills to:**
- Encode unique project conventions
- Guide through project-specific workflows
- Ensure consistency in project patterns
- Reduce cognitive load for project work
- Enable Claude to work effectively in specialized project contexts

**Remember:**
- One Skill per clear concern
- Progressive disclosure (overview → details → references)
- Concrete examples from actual project
- Test with real project scenarios
- Update as project evolves
