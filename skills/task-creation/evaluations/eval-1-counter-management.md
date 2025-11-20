# Evaluation 1: Counter Management Workflow

## Scenario

User needs to create a new task file and must determine the correct counter number.

## Test Prompt

"I need to create a new task file for today. How do I figure out what counter number to use?"

## Expected Behavior

Claude should:
1. Activate the `task-creation` Skill
2. Explain the need to check existing files for today
3. Describe the process: list directory, filter by date, find highest counter
4. Explain counter format (3 digits with leading zeros)
5. Explain that if no files exist for today, start with 001
6. Provide concrete bash commands or steps to check

## Success Criteria

- [ ] Skill activates correctly
- [ ] Emphasizes checking existing files FIRST
- [ ] Describes filtering by today's date
- [ ] Explains finding highest counter
- [ ] Mentions adding 1 to highest
- [ ] Explains 001 if no files exist
- [ ] Provides actionable steps (bash commands or clear procedure)

## Actual Result

*To be filled in during testing*

## Pass/Fail

*To be determined during testing*

## Notes

This is critical workflow knowledge for preventing duplicate counters.
