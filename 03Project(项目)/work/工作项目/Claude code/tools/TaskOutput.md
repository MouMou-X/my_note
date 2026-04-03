---
tags: [编程/ClaudeCode]
type: note
status: 🌿
---

# * **TaskOutput**

- Retrieves output from a running or completed task (background shell, agent, or remote session)
- Takes a task_id parameter identifying the task
- Returns the task output along with status information
- Use block=true (default) to wait for task completion
- Use block=false for non-blocking check of current status
- Task IDs can be found using the /tasks command
- Works with all task types: background shells, async agents, and remote sessions

Parameters:

task_id [string] (required) - The task ID to get output from

block [boolean] (required) - Whether to wait for completion

timeout [number] (required) - Max wait time in ms
