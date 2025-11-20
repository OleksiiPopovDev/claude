# Evaluation Structure for Agent Skills

How to create effective evaluations for testing Skills.

## Purpose

Evaluations verify that Skills:
- Activate when expected
- Provide correct guidance
- Improve Claude's performance
- Work across different Claude models

## Evaluation Format

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

## Fields

### skills (required)
Array of Skill names to load for this evaluation.

```json
"skills": ["processing-pdfs"]
```

For testing multiple Skills together:
```json
"skills": ["processing-pdfs", "analyzing-spreadsheets"]
```

### query (required)
The user request that should trigger the Skill. Use realistic language users would actually use.

**Good examples**:
```json
"query": "Extract all text from this PDF file and save it to output.txt"
```

```json
"query": "Create a pivot table showing sales by region from this Excel file"
```

```json
"query": "Help me write a commit message for these changes"
```

**Bad examples** (too vague):
```json
"query": "Process this file"
```

```json
"query": "Do the thing"
```

### files (optional)
Array of file paths to include in the evaluation context.

```json
"files": ["test-data/document.pdf"]
```

```json
"files": ["test-data/sales.xlsx", "test-data/regions.csv"]
```

### expected_behavior (required)
Array of specific, measurable behaviors Claude should demonstrate.

**Good examples** (specific, measurable):
```json
"expected_behavior": [
  "Successfully reads the PDF file using an appropriate PDF processing library or command-line tool",
  "Extracts text content from all pages in the document without missing any pages",
  "Saves the extracted text to a file named output.txt in a clear, readable format"
]
```

**Bad examples** (vague, unmeasurable):
```json
"expected_behavior": [
  "Does the task correctly",
  "Produces good output"
]
```

## Creating Effective Evaluations

### Step 1: Identify what to test

Test scenarios where the Skill should:
- **Activate correctly**: Does Claude recognize when to use this Skill?
- **Provide guidance**: Does the Skill help Claude complete the task?
- **Handle edge cases**: Does it work with unusual inputs?

### Step 2: Write realistic queries

Use language real users would use:
- "Extract the text from this PDF"
- "Summarize this spreadsheet data"
- "Create a report from these files"

Avoid artificial phrasing:
- "Utilize the PDF extraction functionality"
- "Engage skill processing mode"

### Step 3: Define measurable behaviors

Each expected behavior should be:
- **Specific**: "Extracts text from all pages" not "Works correctly"
- **Measurable**: You can verify it happened
- **Achievable**: Within Claude's capabilities with the Skill

### Step 4: Include test files

For Skills that process files:
- Include representative test files
- Test edge cases (empty files, large files, corrupted files)
- Use realistic data

### Step 5: Test multiple scenarios

Minimum 3 evaluations per Skill:
1. **Basic usage**: Common, straightforward case
2. **Advanced usage**: Complex or multi-step case
3. **Edge case**: Unusual input or error condition

## Evaluation Examples

### Example 1: PDF Processing Skill

```json
{
  "skills": ["processing-pdfs"],
  "query": "Extract all text from this PDF file and save it to output.txt",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "Successfully reads the PDF file using an appropriate PDF processing library or command-line tool",
    "Extracts text content from all pages in the document without missing any pages",
    "Saves the extracted text to a file named output.txt in a clear, readable format"
  ]
}
```

### Example 2: PDF Form Filling (Advanced)

```json
{
  "skills": ["processing-pdfs"],
  "query": "Fill in the name field with 'John Smith' and the date field with '2025-11-20' in this PDF form",
  "files": ["test-files/application-form.pdf"],
  "expected_behavior": [
    "Uses the form-filling utilities from the Skill's scripts directory",
    "Successfully identifies the name and date form fields in the PDF",
    "Fills the specified fields with the provided values",
    "Generates a new filled PDF file without corrupting the original",
    "Validates that the filled fields contain the correct values"
  ]
}
```

### Example 3: Error Handling (Edge Case)

```json
{
  "skills": ["processing-pdfs"],
  "query": "Extract text from this PDF",
  "files": ["test-files/encrypted.pdf"],
  "expected_behavior": [
    "Detects that the PDF is encrypted or password-protected",
    "Provides a clear error message explaining the issue",
    "Suggests potential solutions (requesting password, using different tool)",
    "Does not crash or produce a stack trace"
  ]
}
```

### Example 4: Multi-Skill Integration

```json
{
  "skills": ["processing-pdfs", "analyzing-spreadsheets"],
  "query": "Extract tables from this PDF and create an Excel file with the data",
  "files": ["test-files/financial-report.pdf"],
  "expected_behavior": [
    "Uses PDF processing skill to extract table data",
    "Uses spreadsheet skill to create Excel file",
    "Preserves table structure (rows, columns, headers)",
    "Formats the Excel file appropriately with headers and data",
    "Saves the result with a descriptive filename"
  ]
}
```

## Running Evaluations

While Anthropic doesn't provide a built-in evaluation runner, you can create your own:

### Manual Testing
1. Load the Skill
2. Send the query to Claude
3. Check if behavior matches expected_behavior array
4. Document results

### Automated Testing (Custom)
Create a test runner that:
1. Loads specified Skills
2. Sends query to Claude API with Skills attached
3. Analyzes response for expected behaviors
4. Reports pass/fail for each behavior

### Model Comparison
Test the same evaluation across models:
- Claude Haiku (fast, economical)
- Claude Sonnet (balanced)
- Claude Opus (powerful reasoning)

Document which models pass which evaluations.

## Evaluation-Driven Development

Use evaluations to drive Skill development:

1. **Before writing Skill**:
   - Create evaluations for target scenarios
   - Run without Skill (establish baseline)
   - Document what Claude gets wrong

2. **While writing Skill**:
   - Add minimal content to pass first evaluation
   - Run evaluation, iterate until it passes
   - Move to next evaluation

3. **After writing Skill**:
   - Run all evaluations
   - Compare to baseline performance
   - Refine Skill based on results

4. **Ongoing**:
   - Add evaluations for new use cases
   - Update Skill when evaluations fail
   - Track performance over time

## Best Practices

### Do:
- Create at least 3 evaluations per Skill
- Test both success and failure cases
- Use realistic queries and data
- Make expected behaviors specific and measurable
- Test across multiple Claude models
- Update evaluations as Skill evolves

### Don't:
- Test only happy path (test errors too)
- Use vague expected behaviors
- Skip edge cases
- Assume one evaluation is enough
- Forget to re-run evaluations after changes

## Evaluation Checklist

Before finalizing evaluations:

- [ ] At least 3 evaluations created
- [ ] Queries use realistic user language
- [ ] Test files are representative
- [ ] Expected behaviors are specific and measurable
- [ ] Includes basic, advanced, and edge case scenarios
- [ ] Tests both success and failure paths
- [ ] Evaluations cover main Skill features
- [ ] Tested with target Claude model(s)
