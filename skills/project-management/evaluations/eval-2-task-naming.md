# Evaluation 2: Task Naming Convention Understanding

## Scenario

User needs to understand the task file naming convention and how counters work.

## Test Prompt

"I see some files named like '20-11-2025-[001]-auth-system.xml'. Can you explain this naming pattern and how I should name a new task file today?"

## Expected Behavior

Claude should:
1. Activate the `project-management` Skill
2. Explain the date-based naming format (DD-MM-YYYY)
3. Describe the counter system ([001], [002], etc.)
4. Explain that counters reset daily
5. Explain the task name part (kebab-case)
6. Mention the .xml extension
7. Provide an example for today's date

## Success Criteria

- [ ] Skill activates correctly
- [ ] Explains all components of the naming format
- [ ] Correctly describes counter behavior
- [ ] Explains daily reset of counters
- [ ] Mentions need to check existing files
- [ ] Provides concrete example with current date

## Actual Result

*To be filled in during testing*

## Pass/Fail

*To be determined during testing*

## Notes

This tests understanding of the task naming convention which is critical for proper file creation.
