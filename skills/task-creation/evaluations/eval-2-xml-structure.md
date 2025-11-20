# Evaluation 2: Task XML Structure Knowledge

## Scenario

User needs to create a task file and wants to know what sections are required.

## Test Prompt

"What sections must be included in a task XML file? What are the required elements?"

## Expected Behavior

Claude should:
1. Activate the `task-creation` Skill
2. List all required sections (header, objective, context, etc.)
3. Emphasize mandatory sections (repository_safety_requirements, error_correction_phase)
4. Explain status attributes (pending, unchecked)
5. Mention the reference template in references/task-template.md
6. Provide a brief example or point to template

## Success Criteria

- [ ] Skill activates correctly
- [ ] Lists all required sections
- [ ] Emphasizes repository safety requirements are MANDATORY
- [ ] Emphasizes error correction phase is MANDATORY
- [ ] Explains status attribute system
- [ ] References the template file
- [ ] Provides enough detail to create valid XML

## Actual Result

*To be filled in during testing*

## Pass/Fail

*To be determined during testing*

## Notes

Tests knowledge of complete task structure requirements.
