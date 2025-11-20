# Evaluation 1: Agent Prompt Format Selection

## Scenario

User needs to create a new agent prompt and must decide between XML and Markdown formats.

## Test Prompt

"I want to create a new agent for database optimization tasks. Should I use XML or Markdown format for the agent prompt, and why?"

## Expected Behavior

Claude should:
1. Activate the `agent-management` Skill
2. Explain the difference between XML and Markdown formats
3. Provide guidance on when to use each
4. For this specific case (database optimization), recommend Markdown
5. Explain reasoning (narrative guidance, technical instructions)
6. Mention file naming convention

## Success Criteria

- [ ] Skill activates correctly
- [ ] Explains XML vs Markdown differences
- [ ] Provides clear selection criteria
- [ ] Makes appropriate recommendation (likely Markdown)
- [ ] Explains reasoning for recommendation
- [ ] Mentions file naming ({NAME}_PROMPT.{xml|md})
- [ ] Gives actionable guidance

## Actual Result

*To be filled in during testing*

## Pass/Fail

*To be determined during testing*

## Notes

Tests understanding of format selection criteria for agent prompts.
