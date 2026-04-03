---
tags: [编程/ClaudeCode]
type: note
status: 🌿
---

# * **Skill**

Execute a skill within the main conversation

When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively. Skills provide specialized capabilities and domain knowledge.

When users ask you to run a "slash command" or reference `"/<something>"` (e.g., "/commit", "/review-pr"), they are referring to a skill. Use this tool to invoke the corresponding skill.

Example:  
User: "run /commit"  
Assistant: [Calls Skill tool with skill: "commit"]

How to invoke:

- Use this tool with the skill name and optional arguments
- Examples:
    - `skill: &quot;pdf&quot;` - invoke the pdf skill
    - `skill: &quot;commit&quot;, args: &quot;-m &#39;Fix bug&#39;&quot;` - invoke with arguments
    - `skill: &quot;review-pr&quot;, args: &quot;123&quot;` - invoke with arguments
    - `skill: &quot;ms-office-suite:pdf&quot;` - invoke using fully qualified name

Important:

- When a skill is relevant, you must invoke this tool IMMEDIATELY as your first action
- NEVER just announce or mention a skill in your text response without actually calling this tool
- This is a BLOCKING REQUIREMENT: invoke the relevant Skill tool BEFORE generating any other response about the task
- Only use skills listed in "Available skills" below
- Do not invoke a skill that is already running
- Do not use this tool for built-in CLI commands (like /help, /clear, etc.)
- If you see a `<command-name>` tag in the current conversation turn (e.g., `<command-name>/commit</command-name>`), the skill has ALREADY been loaded and its instructions follow in the next message. Do NOT call this tool - just follow the skill instructions directly.

Available skills:

Parameters:

skill [string] (required) - The skill name. E.g., "commit", "review-pr", or "pdf"

args [string] - Optional arguments for the skill
