# Evaluation 3: Agent Role Assignment

## Scenario

User is creating a task and needs to assign it to the appropriate agent.

## Test Prompt

"I'm creating a task for implementing a new API feature. Which agent should I assign this to, and how do I reference them in the task file?"

## Expected Behavior

Claude should:
1. Activate the `task-creation` Skill (may also activate agent-management)
2. Suggest Technical Lead agent for API implementation
3. Explain the @ notation for referencing agents
4. Provide the correct path format (@agents/TECHNICAL_LEAD_PROMPT.xml)
5. Show the XML element (<target_agent_role>)
6. Mention where to find available agents

## Success Criteria

- [ ] Skill activates correctly
- [ ] Recommends appropriate agent (Technical Lead)
- [ ] Explains @ notation
- [ ] Provides correct path format
- [ ] Shows XML element structure
- [ ] Mentions where agents are located (agents/ directory)
- [ ] Includes file extension in path

## Actual Result

*To be filled in during testing*

## Pass/Fail

*To be determined during testing*

## Notes

Tests agent assignment knowledge and proper referencing format.
