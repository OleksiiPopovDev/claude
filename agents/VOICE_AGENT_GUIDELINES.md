# Voice Agent Prompt Guidelines

## Target Models

**Optimized for:** Gemini 2.5 Flash, GPT-4o mini, GPT-4.1 mini

These models require explicit step-by-step instructions. Don't assume they'll infer - be explicit.

---

## Overview

These guidelines apply to voice agent prompts (like HeyVail). Voice agents have unique requirements because they operate in real-time conversations with customers who cannot see any interface.

**Critical Context:**
- Customer hears ONLY what agent says out loud
- Tools execute silently in the background
- Agent must distinguish between natural language (customer) and technical formats (system)

---

## Format Requirements

### The SAY:/DO: Structure

**MANDATORY:** All voice agent prompts must use this consistent format:

**SAY:** = Words the customer hears
- Natural, conversational language
- No technical terms, codes, or timestamps
- How a human would speak

**DO:** = Silent actions the agent takes
- Tool calls
- Waiting/pausing
- Data storage
- Logic operations
- Variable extraction

**Example - CORRECT:**
```markdown
**SAY:** "I'll call you back in two hours. Talk to you soon!"
**DO:** Wait for user to say goodbye
**SAY:** "Goodbye."
**DO:** Execute reschedule_call with duration_text="two hours"
**DO:** Extract scheduled_time from tool response
**DO:** Execute call_outcome with scheduled_call_time="2025-10-08T17:43:55.683Z"
**DO:** Execute end_call
```

**Example - WRONG:**
```markdown
Say: "I'll call you back in two hours"
[Wait for goodbye]
Execute reschedule_call("two hours")
```

### Conditional Logic Format

Use **IF/THEN** structure with clear indentation:

```markdown
**IF** condition:
  **SAY:** "customer hears this"
  **DO:** silent action
  
  **IF** nested condition:
    **SAY:** "nested speech"
    **DO:** nested action
  
  **IF** alternative nested condition:
    **SAY:** "alternative speech"
```

**Rules:**
- Always indent nested conditions
- Always use **SAY:** and **DO:** inside conditionals
- Never use brackets like [WAIT] or [STOP] - use **DO:** instead

---

## Three Critical Layers

Voice agents operate on three separate layers. **NEVER conflate them:**

### Layer 1: What Agent SPEAKS (Customer Hears)
```markdown
**SAY:** "I'll call you back tomorrow at 2pm. Talk to you soon!"
```
- Natural, conversational language
- No technical details
- No timestamps, codes, or tool names

### Layer 2: What Agent EXECUTES (Silent Background)
```markdown
**DO:** Execute reschedule_call with duration_text="tomorrow at 2pm"
```
- Tool invocations
- Function calls
- Silent operations

### Layer 3: What Agent STORES (Technical Format)
```markdown
**DO:** scheduled_call_time="2025-10-09T14:00:00.000Z"
```
- ISO timestamps
- Outcome codes
- Database values
- API parameters

**Customer only experiences Layer 1. Layers 2 and 3 are invisible.**

---

## Tool Execution Rules

### Tool Silence is Critical

**NEVER have agent announce tool usage:**

❌ **WRONG:**
```markdown
**SAY:** "Let me check the knowledge base..."
**SAY:** "I'm calculating the time..."
**SAY:** "The system shows..."
**SAY:** "With the available data, the current time is 2025-10-08T15:43:55.683Z"
```

✅ **CORRECT:**
```markdown
**DO:** Execute knowledge_base_search silently
**DO:** Execute reschedule_call silently
**SAY:** "I'll call you back tomorrow." (no mention of tools)
```

### Multi-Step Tool Flows

When tools depend on each other, use explicit STEP numbering:

```markdown
**DO:** STEP 1 - Execute reschedule_call with duration_text="two hours"
**DO:** STEP 2 - Tool returns: {"scheduled_time": "2025-10-08T17:43:55.683Z", "success": true}
**DO:** STEP 3 - Extract the scheduled_time value (the ISO timestamp)
**DO:** STEP 4 - Execute call_outcome with scheduled_call_time=[ISO timestamp from STEP 3]
**DO:** Execute end_call

**CRITICAL:** The scheduled_call_time parameter MUST be the ISO format from STEP 3, NOT the customer's phrase.
```

**Why this matters:**
- Prevents agent from skipping steps
- Makes dependencies explicit
- Shows example tool return format
- Clarifies which value goes where

### Tool Return Values

When tools return data that must be used elsewhere:

1. Show the return format as an example
2. Explicitly state "Extract X from response"
3. Show what gets used where
4. Add CRITICAL warning if confusion is likely

**Example:**
```markdown
**DO:** STEP 1 - Execute get_user_info
**DO:** STEP 2 - Tool returns: {"user_id": "12345", "email": "john@example.com"}
**DO:** STEP 3 - Extract user_id value ("12345")
**DO:** STEP 4 - Use user_id in next tool: create_ticket(user_id="12345")

**CRITICAL:** Use the user_id VALUE from step 3, not the string "user_id"
```

---

## Mandatory Gates

When agent MUST collect information before proceeding, use a "mandatory gate" pattern with retry logic:

```markdown
**Mandatory Name Collection (When {{first_name}} is empty):**

**Attempt 1:**
**SAY:** "May I ask who I'm speaking with?"
**DO:** Wait for complete response

**IF** they give an actual name:
  **DO:** Store as contact_name
  **DO:** Proceed to next section

**IF** they dodge/ask questions:
  **SAY:** "This is Vail from HeyVail. I'm calling about AI solutions. And may I ask who I'm speaking with?"
  **DO:** Wait for complete response
  
  **IF** they give name now:
    **DO:** Store as contact_name
    **DO:** Proceed to next section

**IF** they dodge again:
  **SAY:** "I'm sorry, but I need to know who I'm speaking with before we can proceed. What's your name?"
  **DO:** Wait for complete response
  
  **IF** they give name:
    **DO:** Store as contact_name
    **DO:** Proceed to next section
  
  **IF** they refuse:
    **SAY:** "I understand. Have a great day."
    **DO:** Execute call_outcome "bad-fit" → Execute end_call

**CRITICAL:** NEVER proceed without storing actual name when {{first_name}} was empty
```

**Key elements:**
- Multiple attempts (usually 3)
- Escalating explanations
- Clear exit condition (end call if refuse)
- CRITICAL rule stating what cannot be skipped
- Makes it impossible to bypass the gate

---

## Common Patterns

### Waiting for User Response

```markdown
**SAY:** "Do you have a few minutes to chat?"
**DO:** Wait for complete response
```

**Rules:**
- Always explicit "Wait for complete response" after questions
- Never assume silence duration
- If silence exceeds 6 seconds: "{{first_name}}, are you still there?"

### Goodbye Sequences

```markdown
**SAY:** "I'll call you back tomorrow. Talk to you soon!"
**DO:** Wait for user to say goodbye/bye/thanks
**SAY:** "Goodbye."
**DO:** Execute call_outcome
**DO:** Execute end_call
```

**Critical order:**
1. Agent says goodbye confirmation
2. WAIT for user acknowledgment
3. Agent says "Goodbye"
4. THEN execute tools
5. THEN end call

**Never hang up without saying goodbye first.**

### Reschedule Pattern

```markdown
**IF** user requests callback:
  **SAY:** "I'll call you back [timeframe]. Talk to you soon!"
  **DO:** Wait for user goodbye
  **SAY:** "Goodbye."
  **DO:** STEP 1 - Execute reschedule_call(duration_text="[customer phrase]")
  **DO:** STEP 2 - Tool returns scheduled_time in ISO format
  **DO:** STEP 3 - Extract ISO timestamp
  **DO:** STEP 4 - Execute call_outcome(scheduled_call_time=[ISO from step 3])
  **DO:** Execute end_call
```

---

## Editing Voice Agent Prompts

### Process for Making Changes

1. **Read the request carefully**
2. **Explain what you understood**
3. **List ALL proposed changes:**
    - Authorized (user requested)
    - Unauthorized (bugs/improvements you found)
4. **Get approval for unauthorized changes**
5. **Implement only approved changes**
6. **Produce complete prompt** (no partial updates)
7. **List summary of what changed**

### What to Look For

When reviewing voice agent prompts, check for:

**Format Issues:**
- Inconsistent **SAY:**/**DO:** usage
- Brackets like [WAIT] instead of **DO:** blocks
- Tool names in **SAY:** blocks

**Logic Issues:**
- Agent can proceed without required data
- Missing exit conditions
- Circular logic or infinite loops
- Agent says goodbye after end_call

**Tool Issues:**
- Agent announces tool usage
- Tool return values not extracted/used
- Natural language stored where ISO format required
- Steps can be skipped

**Flow Issues:**
- No wait after questions
- Abrupt endings without goodbye
- No retry logic for critical data collection

### Testing Mindset

**Ask yourself:**
- Could LLM misinterpret this instruction?
- Is every step explicit enough?
- Can any step be accidentally skipped?
- Does agent say anything technical to customer?
- Are tool return values clearly extracted and used?

**If answer is "maybe" to any question, make it more explicit.**

---

## Forbidden Practices

**Never do these:**

❌ Use brackets for stage directions: `[WAIT 3 seconds]`
❌ Mix instruction formats in same section
❌ Put tool names in customer dialogue
❌ Say timestamps or codes out loud
❌ Create partial updates with "[unchanged]"
❌ Add meta-commentary like "this helps because..."
❌ Make assumptions about what LLM will infer
❌ Skip the change approval process

---

## Checklist for Complete Voice Agent Prompts

Before finalizing any voice agent prompt:

- ☐ All dialogue uses **SAY:**
- ☐ All actions use **DO:**
- ☐ All conditionals use **IF/THEN** with indentation
- ☐ Multi-step tools use STEP 1, 2, 3, 4 format
- ☐ Tool return values explicitly shown and extracted
- ☐ No tool names in **SAY:** blocks
- ☐ No technical details spoken to customer
- ☐ Goodbye always before end_call
- ☐ Mandatory gates have retry logic
- ☐ All questions followed by "Wait for complete response"
- ☐ CRITICAL warnings for confusing situations
- ☐ Complete output (no partial sections)
- ☐ Summary of changes at end (if changes made)
