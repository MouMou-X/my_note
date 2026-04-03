---
tags:
  - LLM/PromptEng
type: note
status: 🌱
created: 2026-03-05
source: "[skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#how-skills-work)"
---
在agent领域“渐进式披露”（progressive disclosure）：仅在相关时加载指令，避免上下文膨胀。这可将Token消耗显著降低，并提升长文本任务准确率。

# 一、why 为什么需要渐进式披露
| 问题                     | 具体表现                           |
| ---------------------- | ------------------------------ |
| **注意力稀释**              | 模型在海量文本中"迷失"，关键指令被淹没           |
| **Lost-in-the-Middle** | 研究证明 LLM 对上下文中间部分的信息提取能力显著弱于首尾 |
| **Token 成本爆炸**         | 每次调用都携带全量上下文，费用线性甚至指数增长        |
| **幻觉率上升**              | 上下文越长，模型越容易"脑补"不存在的内容          |

---

# 二、本质
核心思想：把“静态的长上下文”变成“动态加载的短上下文”
不要在对话开始时加载所有可能用到的信息，而是：
```
当且仅当某条指令/工具/知识与当前步骤相关时，才将其注入上下文。
```

---

# 三、实现路径
要在Agent系统中实现这种策略，通常有以下几种工程方法：

#### A. 动态工具加载 (Dynamic Tool/Function Retrieval)
与其在初始化时向Agent注入几十个API工具的描述（JSON Schema），不如建立一个“工具注册表”。
- **流程**：当收到用户请求时，先用一个轻量级的方法（如向量检索或小模型路由）去匹配当前任务最可能需要的 3-5 个工具，然后再将这几个工具的定义注入到主Agent的上下文中。
- **场景**：当你构建一个全能型的个人助理Agent时，如果当前任务是清理一批评测基准数据，系统只需动态加载文件读写和数据过滤工具，而完全不需要加载日历或邮件发送工具。

#### B. 意图驱动的 SOP RAG (SOP Retrieval)
对于复杂的业务流程，不需要一开始就告诉Agent所有的步骤。
- **流程**：将长篇的操作指南拆解为节点。Agent在执行时，当前节点的状态（State）会作为Query，去检索下一步的详细指令（Instruction）。
- **优势**：这种基于状态机的“按需喂饭”策略，能极大提升Agent在多步骤长链条任务中的准确率。

#### C. 层级代理架构 (Hierarchical Multi-Agent)
这是渐进式披露在架构层面的体现，通常表现为“Router（大脑）+ Worker（执行者）”模式。
- **流程**：顶层Router Agent只有一个极其精简的Prompt，专门负责意图识别和任务拆解。它将拆解后的子任务分发给下游的Worker Agent。每个Worker Agent拥有非常垂直、深度的领域上下文（例如一个专门负责LLM通用调用的Agent，或者一个专门负责生成推理数据的Agent）。

---

# 四、具体实现框架：分层指令系统

## Layer 0 —— 永久核心层（~500 tokens）
始终存在，极度精简：
```
你是一个任务执行 Agent。
核心原则：[3-5条最关键的行为准则]
当前任务：{task}
可调用的能力模块：[列表，不含细节]
```

## Layer 1 —— 按需加载层（动态注入）
根据任务分类，动态拉取对应模块：
```python
def build_context(task, current_step):
    ctx = CORE_PROMPT  # 永远存在
    
    # 根据任务类型加载领域规则
    domain = classify_domain(task)  # e.g., "finance", "code", "search"
    ctx += load_domain_rules(domain)
    
    # 根据当前步骤加载工具文档
    needed_tools = predict_needed_tools(current_step)
    for tool in needed_tools:
        ctx += load_tool_doc(tool)  # 只加载即将用到的工具
    
    return ctx
```

## Layer 2 —— 即时检索层（RAG 驱动）
对于大型知识库（如 1000 条业务规则），用向量检索代替全量加载：
```python
# 不要这样做 ❌
context += ALL_BUSINESS_RULES  # 50,000 tokens

# 这样做 ✓
relevant_rules = vector_search(
    query=current_step_description,
    corpus=business_rules_db,
    top_k=5  # 只取最相关的 5 条
)
context += relevant_rules  # ~500 tokens
```

---

# 五、关键技术：触发机制设计
渐进式披露的难点不在"加载"，而在**判断"何时"加载"什么"**。

## 方法 A：规则路由（低延迟）
````python
ROUTING_TABLE = {
    "写代码": ["code_style_guide", "git_conventions", "test_requirements"],
    "查数据": ["sql_tool_doc", "data_privacy_rules"],
    "发邮件": ["email_templates", "tone_guidelines", "approval_workflow"],
}

def route(task_type):
    return ROUTING_TABLE.get(task_type, [])
```
优点：零延迟，可预测  
缺点：需要维护路由表，覆盖率有限

### 方法 B：LLM 意图分类（高灵活性）
用一个轻量模型（如 haiku/flash）先对任务做分类，再决定加载哪些模块：
```
[分类 Prompt]
任务: "{user_input}"
从以下模块中选出本任务需要的（可多选）：
- code_tools
- database_tools  
- communication_tools
- finance_rules
只输出模块名列表，JSON格式。
```

### 方法 C：步骤级动态注入（最精细）
不在任务开始时决定，而是**在每个 Agent 步骤前**动态更新上下文：
```
Step 1: Agent 决定"需要搜索网络"
  → 此时才注入 search_tool 的详细文档

Step 2: Agent 决定"需要写入数据库"  
  → 此时才注入 database_tool 文档
  → 同时可以移除 search_tool 文档（sliding window）
````

---

# 六、进阶模式：上下文的"增删改"
渐进式披露不只是"加"，还包括主动"删除"过时信息：

## Sliding Window 指令窗口
````python
class InstructionWindow:
    def __init__(self, max_tokens=2000):
        self.active_modules = []
        self.max_tokens = max_tokens
    
    def update(self, step_result, next_action):
        # 移除已完成步骤的工具文档
        self.evict_irrelevant(step_result)
        # 加载下一步需要的
        self.load_for_action(next_action)
        # 超出限制时按 LRU 淘汰
        self.enforce_limit()
```

### 摘要压缩（Summarization）
对于历史步骤，不保留原始内容，而是压缩成摘要：
```
# 原始（800 tokens）
Step 3 详细执行过程：调用了search_tool，参数为{...}，
返回结果为{大量原始数据}，然后进行了过滤...

# 压缩后（50 tokens）  
Step 3 ✓：搜索完成，找到3个相关结果，已存入 results 变量。
```

---

## 六、实测效果与数据参考

在实际 Agent 系统中，渐进式披露带来的收益相当显著：
```
场景：客服 Agent，知识库 200 条规则，20 个工具

传统方式（全量加载）：
  平均上下文：~15,000 tokens/次
  任务准确率：71%
  成本：$0.045/次对话

渐进式披露：
  平均上下文：~3,200 tokens/次 (↓79%)
  任务准确率：84% (↑13%)
  成本：$0.009/次对话 (↓80%)
````

准确率提升的原因：**更短的上下文 = 更高的信噪比 = 模型注意力更集中。**

---

## 七、工程实现的坑

| 坑             | 解决方案                                |
| ------------- | ----------------------------------- |
| 分类误判导致关键指令未加载 | 设置"安全兜底模块"，对低置信度的分类加载更多备用规则         |
| 步骤级动态注入增加延迟   | 预测性预加载（prefetch），在上一步执行时并行准备下一步的上下文 |
| 模块间依赖关系复杂     | 构建模块依赖图，加载 A 时自动检查并加载 A 的依赖         |
| 调试困难（上下文是动态的） | 完整记录每次调用时的实际上下文快照，用于复现和分析           |

---
