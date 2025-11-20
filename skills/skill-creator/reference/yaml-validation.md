# YAML Frontmatter Validation Rules

Complete validation requirements for SKILL.md YAML frontmatter.

## Required Fields

Every SKILL.md must have both fields in YAML frontmatter:

```yaml
---
name: skill-name-here
description: Description text here
---
```

## name Field Validation

### Maximum Length
- **64 characters maximum**
- Validation fails if longer

### Allowed Characters
- Lowercase letters (a-z)
- Numbers (0-9)
- Hyphens (-)

### Disallowed Patterns
- ❌ No uppercase letters: `Processing-Data`
- ❌ No underscores: `processing_data`
- ❌ No spaces: `processing data`
- ❌ No XML tags: `<skill>processing</skill>`
- ❌ No reserved words: `anthropic`, `claude`

### Valid Examples
- ✓ `processing-pdfs`
- ✓ `analyzing-spreadsheets`
- ✓ `managing-databases`
- ✓ `testing-code`
- ✓ `writing-documentation`
- ✓ `data-analysis-2`

### Invalid Examples
- ✗ `Processing-PDFs` (uppercase)
- ✗ `processing_pdfs` (underscore)
- ✗ `pdf helper` (space)
- ✗ `claude-assistant` (reserved word)
- ✗ `anthropic-tools` (reserved word)

## description Field Validation

### Maximum Length
- **1024 characters maximum**
- Validation fails if longer

### Required Content
- Must be non-empty
- No XML tags allowed
- Should be written in third person
- Should include WHAT the Skill does
- Should include WHEN to use it

### Voice Guidelines

**Third Person** (correct):
- ✓ "Processes Excel files and generates reports"
- ✓ "Analyzes data and creates visualizations"

**First Person** (incorrect):
- ✗ "I can help you process Excel files"
- ✗ "I analyze data and create visualizations"

**Second Person** (incorrect):
- ✗ "You can use this to process Excel files"
- ✗ "Helps you analyze data"

### What + When Pattern

Include both WHAT and WHEN:

**Good examples**:
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

```yaml
description: Analyze Excel spreadsheets, create pivot tables, generate charts. Use when analyzing Excel files, spreadsheets, tabular data, or .xlsx files.
```

```yaml
description: Generate descriptive commit messages by analyzing git diffs. Use when the user asks for help writing commit messages or reviewing staged changes.
```

**Bad examples** (missing WHEN):
```yaml
description: Helps with documents
```

```yaml
description: Processes data
```

```yaml
description: Does stuff with files
```

### Key Terms for Discovery

Include specific terms that trigger the Skill:

For PDF Skill:
- "PDF", "PDFs", "forms", "document extraction"

For Excel Skill:
- "Excel", "spreadsheets", "tabular data", ".xlsx files"

For Git Commit Skill:
- "commit messages", "staged changes", "git diffs"

These terms help Claude discover the Skill when users mention them.

## Common Validation Errors

### Error: name too long
```yaml
# ✗ This name is 72 characters (exceeds 64 limit)
name: this-is-a-very-long-skill-name-that-exceeds-the-maximum-allowed-length
```

Fix: Shorten to 64 characters or less

### Error: name contains uppercase
```yaml
# ✗ Contains uppercase letters
name: Processing-PDFs
```

Fix: Use lowercase only
```yaml
# ✓ Correct
name: processing-pdfs
```

### Error: name contains reserved word
```yaml
# ✗ Contains reserved word
name: claude-helper
```

Fix: Remove reserved word
```yaml
# ✓ Correct
name: pdf-helper
```

### Error: description too long
```yaml
# ✗ Exceeds 1024 characters
description: [very long description text...]
```

Fix: Shorten to 1024 characters or less. Move detailed content to SKILL.md body.

### Error: description contains XML
```yaml
# ✗ Contains XML tags
description: <skill>Processes PDFs</skill>
```

Fix: Remove XML tags
```yaml
# ✓ Correct
description: Processes PDFs and extracts text
```

## Naming Conventions

### Gerund Form (Recommended)

Use verb + -ing form:
- `processing-pdfs`
- `analyzing-spreadsheets`
- `managing-databases`
- `testing-code`
- `writing-documentation`

### Alternative Forms

**Noun phrases** (acceptable):
- `pdf-processing`
- `spreadsheet-analysis`
- `database-management`

**Action-oriented** (acceptable):
- `process-pdfs`
- `analyze-spreadsheets`
- `manage-databases`

### Avoid

- Vague: `helper`, `utils`, `tools`
- Generic: `documents`, `data`, `files`
- Inconsistent patterns within collection

## Validation Script

Use the bundled validation script:

```bash
python scripts/validate_skill.py path/to/SKILL.md
```

Returns:
- Success: "SKILL.md is valid"
- Failure: Specific error messages

## Quick Reference

| Rule | Requirement | Example |
|------|------------|---------|
| **name max length** | 64 chars | `processing-pdfs` |
| **name characters** | Lowercase, numbers, hyphens | `data-analysis-2` |
| **name reserved** | No "anthropic", "claude" | `pdf-processing` |
| **description max** | 1024 chars | [See examples above] |
| **description voice** | Third person | "Processes files" |
| **description content** | What + When | "Does X. Use when Y." |
| **XML tags** | None allowed | No `<tag>` in any field |
