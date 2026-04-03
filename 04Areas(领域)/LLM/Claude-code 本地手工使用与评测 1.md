---
tags: [编程/ClaudeCode]
type: note
status: 🌿
---

# Step 0 安装[[Claude-code]]
使用[[Claude-trace]]来执行。
- 安装[[Claude-trace]]
```bash
npm install -g @mariozechner/claude-trace
```
- 安装原版[[Claude-code]]
```bash
npm install -g @anthropic-ai/claude-code
```
npm uninstall -g @mariozechner/claude-trace
# Step 1 执行[[Claude-code]]
1. 在终端修改环境变量
```bash
# 清空原有 Anthropic key 防止冲突（很重要！）  
unset ANTHROPIC_API_KEY  
  
# MiniMax 配置（国际用户）  
export ANTHROPIC_BASE_URL=""  
# 如果你在大陆，用这个：  
# export ANTHROPIC_BASE_URL="https://api.minimaxi.com/anthropic"  
  
export ANTHROPIC_AUTH_TOKEN=""   # 注意是 AUTH_TOKEN，不是 API_KEY  
  
# 超时设置（建议大一点，M2 推理有时较慢）  
# export API_TIMEOUT_MS=3000000  
  
# 屏蔽一些非必要流量（可选，省钱+提速）  
# export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1  

# 指定模型（目前最强的是 MiniMax-M2 或 M2.1，根据你账号支持的写）  
# export ANTHROPIC_MODEL="MiniMax-M2"  
# export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M2"  
export ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder-plus"  
export ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder-plus"  
export ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder-plus"  
```

# windows bug
- where与windows不兼容
```node
    try {
        //let claudePath = require("child_process")
        //    .execSync("which claude", {
        //    encoding: "utf-8",
        //})
        //    .trim();
        let claudePath = "C:\\Users\\jun\\AppData\\Roaming\\npm\\node_modules\\@anthropic-ai\\claude-code\\cli.js"
        // Handle shell aliases (e.g., "claude: aliased to /path/to/claude")
        const aliasMatch = claudePath.match(/:\s*aliased to\s+(.+)$/);
        if (aliasMatch && aliasMatch[1]) {
            claudePath = aliasMatch[1];
        }
```

# api测试
- 个人私钥✔
```
set ANTHROPIC_BASE_URL="https://dashscope.aliyuncs.com/apps/anthropic"  

set ANTHROPIC_AUTH_TOKEN="sk-54155d45270b4d438c99aae259f5349d"

set ANTHROPIC_DEFAULT_SONNET_MODEL="qwen3-coder-plus"  

set ANTHROPIC_DEFAULT_OPUS_MODEL="qwen3-coder-plus"  

set ANTHROPIC_DEFAULT_HAIKU_MODEL="qwen3-coder-plus"  
```
- ideal talk免费密钥✔

- 启动命令
```
claude-trace
```


# 测试示例

```
Create an interesting typing game with a keyboard in the lower middle of the screen and some famous articles in the upper middle. When the user types a word correctly, a cool reaction should be given to encourage him. Design a modern soft color scheme inspired by macarons. Come up with a very creative solution first, and then start writing code.
The game should be able to support typing, and you need to neglect upcase and lowercase.
```


```
Please write a Python script to train an RL agent to achieve a high policy level in `MountainCar-v0`. Do not use a GPU, and ensure there are no bugs. Finally, visualize the trained policy with videos.
```


```
Please write a Python script to train an RL agent to achieve a high policy level in `BipedalWalker-v3`. Do not use a GPU, and ensure there are no bugs. Finally, visualize the trained policy with videos.
```


```
Please help me develop a visually appealing and smoothly operable "big fish eats small fish" game that can be played on website, ensuring it is bug-free. Control my fish with keyboard, and there should be other fishes smaller or bigger than mine swimming in the screen.
```


# trace结构
## System prompt

---

## Tools
- Task
- TaskOutput
- Bash
- Glob
- Grep
- ExitPlanMode
- Read
- Edit
- Write
- NotebookEdit
- WebFetch
- TodoWrite
- WebSearch
- KillShell
- AskUserQuestion
- Skill
- EnterPlanMode

---

## user
### system Reminder
`{System prompt}`

---

## assistant

