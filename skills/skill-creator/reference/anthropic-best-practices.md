# Anthropic Best Practices for Agent Skills

Complete guide following Anthropic's official best practices for creating high-quality Agent Skills.

## Core Principles

### 1. Concise is Key

Only add context Claude doesn't already have. Challenge each piece of information:
- "Does Claude really need this explanation?"
- "Can I assume Claude knows this?"
- "Does this paragraph justify its token cost?"

The context window is shared with system prompt, conversation history, other Skills' metadata, and the actual request.

### 2. Progressive Disclosure

Structure Skills with three levels:
1. **Metadata** (always loaded): name and description (~100 tokens)
2. **Instructions** (loaded when triggered): SKILL.md body (under 5k tokens, ideally <500 lines)
3. **Resources** (loaded as needed): bundled files executed via bash

### 3. Appropriate Degrees of Freedom

Match specificity to task fragility:
- **High freedom**: Multiple approaches valid, context-dependent decisions
- **Medium freedom**: Preferred pattern exists, some variation acceptable
- **Low freedom**: Fragile operations, consistency critical, specific sequence required

## YAML Frontmatter Requirements

### name field
- Maximum 64 characters
- Lowercase letters, numbers, hyphens only
- No XML tags
- No reserved words: "anthropic", "claude"
- Use gerund form: `processing-data`, `analyzing-code`

### description field
- Maximum 1024 characters
- Non-empty
- No XML tags
- Third person voice (not first/second person)
- Must include WHAT the Skill does AND WHEN to use it

**Good examples**:
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

**Bad examples**:
```yaml
description: Helps with documents
description: I can help you process PDFs
description: You can use this for files
```

## Progressive Disclosure Patterns

### Pattern 1: High-level guide with references

```markdown
## Quick start
[Basic usage here]

## Advanced features
**Feature 1**: See [FEATURE1.md](references/FEATURE1.md)
**Feature 2**: See [FEATURE2.md](references/FEATURE2.md)
```

### Pattern 2: Domain-specific organization

```
skill/
├── SKILL.md (overview)
└── references/
    ├── domain1.md
    ├── domain2.md
    └── domain3.md
```

### Pattern 3: Conditional details

```markdown
## Basic usage
[Simple instructions]

**For advanced use**: See [references/advanced.md](references/advanced.md)
**For API reference**: See [references/api.md](references/api.md)
```

**Keep references one level deep** - avoid nested references.

## Bundling Utility Scripts

Include scripts for:
- Operations that are error-prone
- Deterministic transformations
- Complex validations
- Repeated utility functions

**Benefits**:
- More reliable than generated code
- Save tokens (no code in context)
- Save time (no code generation)
- Ensure consistency

**Script best practices**:
- Handle errors explicitly (don't punt to Claude)
- Document configuration values (no "voodoo constants")
- Use forward slashes in paths (Unix-style)
- Provide helpful error messages

## Evaluation-Driven Development

1. **Identify gaps**: Run Claude without Skill, document failures
2. **Create evaluations**: Build 3+ scenarios testing these gaps
3. **Establish baseline**: Measure performance without Skill
4. **Write minimal instructions**: Just enough to pass evaluations
5. **Iterate**: Execute evaluations, compare, refine

### Evaluation Structure

```json
{
  "skills": ["skill-name"],
  "query": "User request that should trigger the Skill",
  "files": ["path/to/test-file.ext"],
  "expected_behavior": [
    "Specific expected behavior 1",
    "Specific expected behavior 2",
    "Specific expected behavior 3"
  ]
}
```

Minimum 3 evaluations per Skill:
1. Basic usage scenario
2. Advanced/complex scenario
3. Edge case/error handling scenario

## Common Anti-Patterns

### Windows-style paths
❌ Avoid: `scripts\helper.py`, `references\guide.md`
✓ Use: `scripts/helper.py`, `references/guide.md`

### Too many options
❌ Avoid: "You can use pypdf, or pdfplumber, or PyMuPDF..."
✓ Use: "Use pdfplumber. For scanned PDFs, use pdf2image with pytesseract."

### Vague descriptions
❌ Avoid: "Helps with documents"
✓ Use: "Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."

### Deeply nested references
❌ Avoid: SKILL.md → advanced.md → details.md → content
✓ Use: SKILL.md → {advanced.md, reference.md, examples.md}

### Punting to Claude in scripts
❌ Avoid: Just fail and let Claude figure it out
✓ Use: Handle errors explicitly with clear messages

## Quality Checklist

Before finalizing a Skill:

**Core quality**:
- [ ] Description specific with key terms
- [ ] Description includes what AND when
- [ ] SKILL.md body under 500 lines
- [ ] No time-sensitive information
- [ ] Consistent terminology throughout
- [ ] Examples concrete, not abstract
- [ ] File references one level deep
- [ ] Progressive disclosure used appropriately

**Scripts** (if applicable):
- [ ] Scripts solve problems, not punt to Claude
- [ ] Error handling explicit and helpful
- [ ] No "voodoo constants" (values justified)
- [ ] Required packages listed
- [ ] Scripts documented clearly
- [ ] No Windows-style paths

**Testing**:
- [ ] At least 3 evaluations created
- [ ] Tested with relevant Claude models
- [ ] Tested with real usage scenarios

## File Size Limits

- Total Skill size: Under 8MB
- SKILL.md body: Under 500 lines (recommended)
- name field: Maximum 64 characters
- description field: Maximum 1024 characters
