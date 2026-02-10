---
工作区:
  - https://alidocs.dingtalk.com/i/nodes/ZX6GRezwJlzeYoPLFRQMaE3nWdqbropQ?corpId=dingd8e1123006514592&utm_medium=im_card&cid=1030821%3A5053772406&iframeQuery=utm_medium%3Dim_card%26utm_source%3Dim&utm_scene=person_space&utm_source=im
claude-trace-url:
  - https://www.npmjs.com/package/@mariozechner/claude-trace?activeTab=readme
  - https://www.npmjs.com/package/@loki-zhou/claude-trace
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
export ANTHROPIC_BASE_URL="https://idealab.alibaba-inc.com/api/openai/v1"  
# 如果你在大陆，用这个：  
# export ANTHROPIC_BASE_URL="https://api.minimaxi.com/anthropic"  
  
export ANTHROPIC_AUTH_TOKEN="8ff3eb569dd70344b2e033a1f7c7b488"   # 注意是 AUTH_TOKEN，不是 API_KEY  
  
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
```
set ANTHROPIC_BASE_URL="https://idealab.alibaba-inc.com/apps/anthropic"  

set ANTHROPIC_AUTH_TOKEN=8ff3eb569dd70344b2e033a1f7c7b488

set ANTHROPIC_DEFAULT_SONNET_MODEL=qwen3-coder-plus

set ANTHROPIC_DEFAULT_OPUS_MODEL=qwen3-coder-plus

set ANTHROPIC_DEFAULT_HAIKU_MODEL=qwen3-coder-plus
```
![[Pasted image 20260116105247.png]]



- 启动命令
```
claude-trace
```
- 命令增强
```
think
think hard
think harder
ultrathink
```
- 命令行模式
```
!
```
- 记忆模式
```
# 
分为项目级别、用户级别的记忆
```
- ide集成
```
/ide
```
- 非命令行模式
```
claude -p "今天几号了"
```
- MCP Servers
```
context7 暂时用不到
```
# 测试示例

```
Create an interesting typing game with a keyboard in the lower middle of the screen and some famous articles in the upper middle. When the user types a word correctly, a cool reaction should be given to encourage him. Design a modern soft color scheme inspired by macarons. Come up with a very creative solution first, and then start writing code.
The game should be able to support typing, and you need to neglect upcase and lowercase.
```
创建一个有趣的打字游戏，在屏幕中下部放置键盘，在上中部显示一些著名文章。当用户正确输入单词时，应给予酷炫的反应以鼓励他。设计一套受马卡龙启发的现代柔和色彩方案。首先提出一个非常有创意的解决方案，然后开始编写代码。该游戏应支持打字功能，并且需要忽略大小写。
```
**Issues to be fixed:**
1. **Keyboard Input Duplication Bug**
    - Problem: Under English input method, each key press outputs two identical letters
    - Need to fix keyboard event handling logic
2. **Particle Effect Overlap Issue**
    - Problem: Particle confetti effects are blocking the game interface content
    - Need to adjust particle system layering or positioning to avoid affecting gameplay experience
      
Bugs to resolve:

Word transition visual glitch

Problem: After completing one word, when loading the next word, the entire sentence briefly appears before being overwritten by the "word-input" element. This creates an unfriendly visual experience.
Requires redesign of the word transition mechanism
Input field not clearing on restart

Problem: When clicking the "Restart Game" button, the previous round's "word-input" content remains uncleared
Need to ensure input field is properly reset when restarting
Recommended fixes:

Implement smooth word transitions without showing full sentences
Add proper input field clearing in restart function
```


```
Please write a Python script to train an RL agent to achieve a high policy level in `MountainCar-v0`. Do not use a GPU, and ensure there are no bugs. Finally, visualize the trained policy with videos.
```
请编写一个Python脚本来训练一个RL智能体在`MountainCar-v0`中达到高水平的策略。不要使用GPU，并确保没有错误。最后，使用视频可视化训练好的策略。

```
Please write a Python script to train an RL agent to achieve a high policy level in `BipedalWalker-v3`. Do not use a GPU, and ensure there are no bugs. Finally, visualize the trained policy with videos.
```
请编写一个Python脚本来训练一个RL智能体在`BipedalWalker-v3`中达到高水平策略。不要使用GPU，并确保没有错误。最后，通过视频可视化训练好的策略。

```
Please help me develop a visually appealing and smoothly operable "big fish eats small fish" game that can be played on website, ensuring it is bug-free. Control my fish with keyboard, and there should be other fishes smaller or bigger than mine swimming in the screen.
```
请帮我开发一个视觉上吸引人且操作流畅的"大鱼吃小鱼"游戏，可以在网站上玩，并确保没有bug。用键盘控制我的鱼，屏幕上应该有其他比我大或比我的小的鱼在游动。

```
# 角色设定
你是一位精通 AI 应用架构的全栈工程师。请帮我自主规划并从零开发一个基于“即时知识渲染”理念的 Anki 闪卡 Web 应用。

# 项目核心目标
帮我写一个 **"A to UI" (从抽象到界面)** 的生成式应用。核心逻辑是：**界面结构不应被硬编码，而应由 LLM 根据对话内容动态定义。**
使用阿里 DashScope 
# 关键技术栈约束
1. **模型层**：必须使用阿里 DashScope (通义千问 `qwen-plus`) API。
2. **后端层**：使用 Python 搭建一个轻量级本地代理服务器（处理 API 鉴权与请求转发）。
3. **前端层**：纯 HTML/JS (推荐 Vue 或原生)，实现单页应用 (SPA)。

# 核心业务流程 (你的开发任务)
请根据以下两个阶段进行架构规划和代码实现：

## 阶段一：范式构建 (Schema Definition)
用户输入一个学习领域（如“雅思单词”或“Python算法”）。
模型需要自主规划该领域的 JSON 数据结构（Schema）。
* *要求*：Schema 必须包含“正面”、“背面”以及 3-5 个该领域特定的辅助字段（如词性、代码示例、易错点等）。
* *前端表现*：前端应根据模型返回的 Schema 动态生成字段预览。

## 阶段二：即时渲染 (Content Generation)
用户输入具体的一个知识点。
模型根据阶段一确定的 Schema，将非结构化的知识转化为结构化的 JSON 数据。
* *前端表现*：前端接收 JSON，自动渲染成一张可翻转的 3D 闪卡。

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

写一个anki记忆卡片。
要求：
1. 风格简约大方。
2. 可编辑，支持html渲染。
3. 支持艾宾浩斯遗忘曲线复习功能。
4. 支持随机卡片漫游
5. 创建10个初始anki卡片内容。