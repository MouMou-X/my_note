---
tags: [编程/ClaudeCode]
type: note
status: 🌱
---

**claude-trace** 是一个专门用来“偷看”/记录 **[[Claude Code]]**（Anthropic推出的命令行AI编程工具）内部通信的开源小工具。

简单来说，它就是一个 **Claude Code 的网络请求拦截器 + 可视化查看器**，能让你看到平时完全看不到的后台细节。

### 主要能看到什么？（超级实用）

- 真实的 **完整 system prompt**（系统提示词）——Claude Code 到底偷偷给你加了多少条“紧箍咒”
- 每次对话真正发给 Anthropic 的 **完整请求参数**（包括所有隐藏的 reminder、上下文压缩等）
- 用到的全部 **工具列表** 和每个工具的详细定义（经常有 90+ 个工具）
- 模型切换过程（比如一开始用 3.5，后来偷偷升到 4）
- 完整的 **多轮对话上下文** 是如何组织的
- 工具调用（tool use）的详细输入输出

#### 预设系统信息（systerm prompt）
- 角色设定
- 工具定义
- 安全边界

#### 思考过程和工具调用
- 工具调用的精确参数
- 工具返回的完整结果
- 思维链

#### 原始api通讯数据
- 上下文管理（压缩）
- token消耗
- 隐形注入（有时候 Claude Code 会在对话中途自动插入一些系统级的提醒（System Reminders），比如“记得检查代码风格”，这些在 trace 里都会现形。）




### 典型使用方式

```bash
# 正常启动并开始记录
claude-trace

# 记录所有请求（默认只记录比较长的对话）
claude-trace --include-all-requests

# 指定参数启动 Claude Code
claude-trace --run-with chat --model sonnet-3.5

# 事后把日志转成好看的网页
claude-trace --generate-html logs.jsonl report.html
```

运行后会在当前目录下生成 `.claude-trace/` 文件夹，里面有：

- `.jsonl` 日志文件（原始数据）
- **自包含的 .html 可视化报告**（直接浏览器打开就能看，很漂亮）

### 目前最常见的两个版本

- 原始作者：**@mariozechner/claude-trace**（国外开发者）
- 中文加强版：**@loki-zhou/claude-trace**（支持中文显示 + 可自定义代理地址）

一句话总结：

**想深度研究/优化 Claude Code 怎么思考、怎么调用工具、系统提示词到底写了什么？**  
装个 claude-trace 就行了，它相当于给 Claude Code 装了个“上帝视角”+“透视镜”。现在基本算是 Claude Code 重度用户/研究者的标配调试神器之一。