---
类型: map
status:
  - seed
tags:
  - "#LLM/工程/Agent/React_Agent"
---
# ReAct 范式深度解析：大语言模型中推理与行动的协同架构研究报告

## 1. 执行摘要与引言

大语言模型（LLM）的兴起标志着人工智能领域从模式识别向生成式问题解决的根本性转变。然而，早期 LLM 在实际部署中面临着显著的二元对立：即**推理（Reasoning）**与**行动（Acting）**的割裂。推理能力指的是模型利用思维链（Chain-of-Thought, CoT）进行多步逻辑推演的内在过程；而行动能力则指模型通过调用外部工具（如搜索引擎、计算器、API）与环境交互的外在表现。传统的单模态方法——仅依靠推理会导致事实幻觉，仅依靠行动则导致缺乏规划的低效执行。

**ReAct（Reason+Act）** 范式由 Yao 等人于 2023 年提出，它通过一种巧妙的提示工程（Prompt Engineering）与执行架构，打破了这种隔阂 1。ReAct 的核心思想在于将推理轨迹（Thought）与行动执行（Action）在同一个交互循环中交织（Interleave）。通过“推理以指导行动”（Reason to Act）和“行动以修正推理”（Act to Reason）的双向反馈机制，ReAct 赋予了 AI 智能体（Agent）处理复杂、多跳（Multi-hop）任务的能力，使其表现出更接近人类认知的解决问题路径 1。

本报告将对 ReAct Agent 的架构进行详尽的解构，从认知科学的理论基础出发，深入剖析其提示词结构、核心组件、执行循环机制，以及从传统的循环脚本（Loop Script）向现代图计算架构（Graph Architecture）的工程演进。同时，我们将探讨 ReAct 与现代 Function Calling（函数调用）技术的融合与分野，分析其在上下文窗口、错误传播等方面的局限性，并展望其在多智能体系统中的未来形态。

---

## 2. 理论基础与认知架构

要深入理解 ReAct 的结构，首先必须理解它试图解决的认知缺陷。在 ReAct 出现之前，大模型的应用主要集中在静态的问答或单纯的工具触发上，这两者都无法独立承担复杂的自主任务。

### 2.1 推理与行动的二分法及其局限

在 ReAct 提出之前，学术界和工业界主要沿用两种独立的范式：

1. **纯推理范式（Reasoning-Only / Chain-of-Thought）：**
    
    - **机制：** 以思维链（CoT）为代表，通过提示模型生成“中间步骤”来引导最终答案。
        
    - **局限性 - 事实幻觉（Hallucination）：** CoT 极度依赖模型预训练的参数化知识（Parametric Knowledge）。当模型面临其训练数据之外的知识盲区（如实时新闻、私有数据库）时，它倾向于通过编造事实来维持逻辑链条的完整性。例如，在回答“最新的 iPhone 价格是多少”时，CoT 可能会基于两年前的数据进行推演，得出错误的结论 1。
        
    - **局限性 - 错误传播（Error Propagation）：** 一旦思维链的起始步骤出错（例如错误的假设），后续所有的逻辑推演都会基于这个错误基础，且模型在内部无法自我纠正，因为缺乏外部反馈源。
        
2. **纯行动范式（Acting-Only / Reactive）：**
    
    - **机制：** 模型被训练或提示直接生成特定的动作（Action），如 API 调用指令。
        
    - **局限性 - 缺乏规划（Aimlessness）：** 纯行动模型类似于“条件反射”系统（System 1）。它看到问题直接触发工具，缺乏对任务的高层规划。例如，面对一个需要多步检索的复杂问题，模型可能会不断重复相同的搜索查询，或者无法将第一步搜索的结果有效地整合到第二步的查询中 1。
        

### 2.2 ReAct 假设：交织协同产生的涌现能力

ReAct 论文的核心假设是：**推理轨迹与行动计划的显式协同，能够产生优于两者之和的效果。** 这种协同在认知科学上对应着人类的元认知过程——我们在行动前会进行心理模拟（Reasoning），行动后会根据结果更新心理模型（Observation）4。

ReAct 引入了一个动态的轨迹空间 $\tau$，形式化定义为：

$$\tau = (o_1, t_1, a_1, o_2, t_2, a_2,..., o_n, t_n, a_n)$$

其中：

- $t_i$ 是基于当前上下文 $(o_1,..., o_i)$ 生成的**推理轨迹（Thought）**。
    
- $a_i$ 是基于推理 $t_i$ 生成的**行动（Action）**。
    
- $o_{i+1}$ 是行动 $a_i$ 执行后，环境反馈的**观察结果（Observation）** 1。
    

这种结构使得模型能够：

1. **动态规划（Dynamic Planning）：** 在 $t_i$ 阶段，模型可以根据当前的观察结果 $o_i$ 调整原本的计划，处理例外情况。
    
2. **外部记忆注入（External Memory Injection）：** $o_i$ 将外部世界的真实信息注入到模型的上下文窗口中，修正模型的参数化记忆，从而抑制幻觉。
    

### 2.3 认知系统映射：系统 2 的显式化

从丹尼尔·卡尼曼的《思考，快与慢》视角来看，传统的 Zero-shot Prompting 类似于直觉式的**系统 1（System 1）**——快速但易错。而 ReAct 强制模型在行动前生成 `Thought:`，实际上是在强迫模型调用**系统 2（System 2）**——慢速、审慎、逻辑化。这种“强制思考”的延迟（Latency）是 ReAct 架构成功的关键，它为模型提供了检视自身逻辑、分解复杂问题的缓冲区 4。

---

## 3. ReAct Agent 的解剖结构

一个完整的 ReAct Agent 并非仅仅是一个 LLM，而是一个由多个组件精密咬合的**复合系统（Compound System）**。我们可以将其结构拆解为四个核心支柱：**大语言模型（大脑）**、**工具集（肢体）**、**提示模板（规则）**和**输出解析器（翻译官）**。

### 3.1 核心驱动：大语言模型（LLM）

LLM 是整个架构的决策引擎。在 ReAct 框架中，LLM 扮演着双重角色：

1. **语义规划者（Semantic Planner）：** 模型必须理解用户的模糊意图，并将其映射到具体的工具功能上。
    
2. **上下文合成器（Context Synthesizer）：** 模型必须阅读历史的推理轨迹和工具返回的冗长结果，保持逻辑的一致性 6。
    

**模型能力的影响：** 研究表明，ReAct 范式对模型的基础能力有门槛要求。较小的模型（如早期的 GPT-3 或参数量较小的 Llama）往往难以严格遵循 ReAct 的格式要求，容易出现“格式崩坏”（例如忘记生成 `Action:` 标签）或“幻觉观察”（即模型自己编造了 `Observation:` 而不是等待工具执行）1。相比之下，GPT-4、Claude 3.5 Sonnet 等强模型在指令遵循和长上下文推理上表现更佳，能够维持长达数十步的 ReAct 循环而不迷失。

### 3.2 交互接口：提示模板（Prompt Template）

提示模板是 ReAct Agent 的“操作系统”内核，它定义了模型与环境交互的协议。一个标准的 ReAct 提示通常包含以下几个关键部分 7：

1. **系统指令（System Instruction）：** 定义 Agent 的角色（例如“你是一个乐于助人的研究助手”）。
    
2. **工具描述（Tool Definitions）：** 极其关键的一环。必须清晰地列出可用工具的名称、功能描述和参数格式。例如：
    
    > _Wikipedia: A wrapper around Wikipedia. Useful for when you need to answer general questions..._
    
3. **格式约束（Format Constraints）：** 强制模型遵循 Thought-Action-Observation 的序列。这是 ReAct 的标志性特征。
    
    > Use the following format:
    > 
    > Question: the input question you must answer
    > 
    > Thought: you should always think about what to do
    > 
    > Action: the action to take, should be one of [{tool_names}]
    > 
    > Action Input: the input to the action
    > 
    > Observation: the result of the action
    > 
    > ... (this Thought/Action/Action Input/Observation can repeat N times)
    > 
    > Thought: I now know the final answer
    > 
    > Final Answer: the final answer to the original input question
    
4. **少样本示例（Few-Shot Examples）：** 提供 1-3 个完整的成功交互轨迹（Trajectory），帮助模型进行上下文学习（In-Context Learning），理解何时该搜索、何时该计算 7。
    
5. **当前暂存区（Agent Scratchpad）：** 这是一个动态变量，用于存储当前对话中已经发生的推理和行动历史。
    

### 3.3 执行肢体：工具（Tools）

工具是 Agent 突破“参数围墙”的手段。在代码层面，工具通常由一个**函数（Function）**和一个**输入模式（Input Schema）**组成 10。

**表 1：工具定义的关键要素**

|**组件**|**说明**|**对 ReAct Agent 的作用**|
|---|---|---|
|**函数名**|如 `calculator`|Agent 用于调用的唯一标识符。|
|**描述 (Docstring)**|如 "用于执行数学计算，输入必须是有效的数学表达式"|决定了 Agent **何时**使用该工具。描述越精准，Agent 的规划越合理。|
|**参数 Schema**|如 `{"query": str}` (Pydantic 模型)|决定了 Agent **如何**构造参数。Agent 会尝试生成符合此 JSON 结构的输入。|
|**执行逻辑**|Python 函数体|实际的业务逻辑（查询数据库、调用 API），对 LLM 而言是黑盒。|

在 LangChain 等框架中，通常使用 `@tool` 装饰器或 Pydantic 的 `BaseModel` 来严格定义这些工具，以确保 LLM 生成的参数能够被代码正确解析 12。

### 3.4 协议转换：输出解析器（Output Parser）

这是 ReAct 架构中最脆弱但也最关键的组件。LLM 本质上是一个文本生成器，它输出的是一串非结构化的字符串。输出解析器的任务是从这段字符串中提取出结构化的指令 14。

- **Regex 解析（经典方法）：** 早期的 ReAct 实现依赖正则表达式（Regex）来捕获 `Action:` 和 `Action Input:` 之间的内容。
    
    - _典型正则模式：_ `r"Action\s*\d*\s*:(.*?)\nAction\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"` 16。
        
    - _脆弱性：_ 如果模型在生成时多加了一个空格、换行符，或者因为“喋喋不休”在 Action Input 后添加了解释性文字，正则匹配就会失败，导致 `OutputParserException` 异常 17。
        
- **结构化输出（现代方法）：** 随着 OpenAI Function Calling 等能力的引入，现代解析器更多地依赖模型直接输出 JSON 对象，大大降低了格式错误的概率（详见第 6 节）。
    

---

## 4. ReAct 的工作机理：执行循环（The Loop）

ReAct 的核心并非静态的结构，而是一个动态的、迭代的执行循环。我们可以通过一个具体的案例——“找出 Apple 公司现任 CEO 的年龄的 0.23 次方是多少？”——来详细拆解这个循环的每一个微观步骤 4。

### 步骤 1：初始化与提示构建

用户输入查询。系统（AgentExecutor）将查询填入 Prompt 模板，此时 `agent_scratchpad` 为空。

### 步骤 2：第一轮推理（Reasoning Trace 1）

LLM 接收 Prompt，开始生成。由于 Prompt 中有 Few-shot 示例的引导，模型不会直接回答（因为它不知道 CEO 是谁），而是生成推理：

> **Thought:** 我需要先查出 Apple 公司的现任 CEO 是谁，然后查他的年龄，最后进行计算。

### 步骤 3：第一轮行动决策（Action 1）

紧接着 Thought，模型生成行动指令：

> Action: Search
> 
> Action Input: "current CEO of Apple"

此时，模型停止生成（或是被解析器截断）。

### 步骤 4：解析与工具执行（Tool Execution）

系统（Python 代码）拦截到 `Action: Search`。解析器提取出工具名 `Search` 和参数 `"current CEO of Apple"`。系统调用 Google Search API。

### 步骤 5：环境反馈（Observation 1）

API 返回结果：

> _"Tim Cook is the chief executive officer of Apple Inc..."_

系统将这个结果标记为 **Observation**，并将其**追加**到 `agent_scratchpad` 中。此时，Prompt 的历史记录变长了。

### 步骤 6：循环迭代（Reasoning Trace 2）

系统再次调用 LLM。这次 LLM 看到的 Prompt 包含了它刚才的思考、行动以及**最新的观察结果**。基于“Tim Cook”这个新信息，模型生成新的思考：

> Thought: 搜索结果显示 CEO 是 Tim Cook。现在我需要去查 Tim Cook 的年龄。
> 
> Action: Search
> 
> Action Input: "Tim Cook age"

### 步骤 7：再次执行与反馈（Observation 2）

系统执行搜索，返回：

> _"Tim Cook is 63 years old (born November 1, 1960)"_

### 步骤 8：计算与终结（Reasoning Trace 3）

系统再次将观察结果追加到 Prompt。LLM 再次被调用：

> Thought: 我知道了 Tim Cook 是 63 岁。现在我需要计算 63 的 0.23 次方。
> 
> Action: Calculator
> 
> Action Input: 63^0.23

工具执行返回结果（Observation）：`2.59...`。

最后一次调用 LLM，模型判断任务完成：

> Thought: 我已经得到了最终结果。
> 
> Final Answer: Apple CEO Tim Cook 的年龄的 0.23 次方约等于 2.59。

解析器识别到 `Final Answer` 标记，终止循环，将结果返回给用户 8。

---

## 5. 工程演进：从脚本循环到图计算

ReAct 的概念虽然简单，但在工程实现上经历了从简单的 `while` 循环到复杂的图（Graph）状态机的演变。这一演变主要是为了解决状态管理、持久化和多路径分支的问题。

### 5.1 第一代架构：AgentExecutor (LangChain Legacy)

在 LangChain 的早期版本（v0.1及以前），ReAct 主要通过 `AgentExecutor` 类实现。

- **机制：** 这是一个高度封装的 Python `while` 循环。它不断地调用 Agent -> Parse -> Tool -> Loop。
    
- **硬编码逻辑：** 循环的逻辑被硬编码在库中，开发者很难插入自定义逻辑（例如“如果在搜索前先请求人类确认”）。
    
- **状态隐晦：** 它的中间状态（Intermediate Steps）是一组临时的变量列表，难以序列化或持久化。这意味着如果程序崩溃，Agent 就会“失忆” 20。
    
- **无限循环风险：** 依靠 `max_iterations`（最大迭代次数）或 `max_execution_time` 来强制中断死循环 22。
    

### 5.2 第二代架构：LangGraph (State Machine)

随着 Agent 需求的复杂化，LangChain 推出了 **LangGraph**，将 Agent 建模为**有向有环图（Cyclic Graph）**。这是 ReAct 工程实现的重大飞跃 23。

#### 5.2.1 状态模式（State Schema）

LangGraph 显式定义了 Agent 的“内存”结构，通常是一个 `TypedDict`。

Python

```
class AgentState(TypedDict):
    # messages 列表存储所有的 Thought, Action, Observation
    # add_messages 是一个 Reducer 函数，负责将新消息追加而非覆盖
    messages: Annotated, add_messages]
```

这种显式的状态定义使得 Agent 的记忆可以被轻松地快照（Checkpoint）、保存到数据库甚至回滚（Time Travel） 25。

#### 5.2.2 节点（Nodes）与边（Edges）

ReAct 循环被拆解为图中的节点和边：

- **Agent Node:** 负责调用 LLM，生成 Thought 和 Action。
    
- **Tools Node:** 负责执行工具。
    
- **Conditional Edge (路由):** 这是一个逻辑判断函数。
    
    - 如果 LLM 输出包含 Tool Calls -> 路由到 Tools Node。
        
    - 如果 LLM 输出包含 Final Answer -> 路由到 END 节点 27。
        

#### 5.2.3 图架构的优势

与 `AgentExecutor` 相比，LangGraph 架构允许更复杂的控制流：

- **人机协同（Human-in-the-loop）：** 可以在执行工具前插入一个“人类审核节点”，暂停图的执行，等待人类批准后再继续。
    
- **多智能体协作：** 图的一个节点本身可以是另一个子图（Subgraph）。这使得构建“ReAct Agent 团队”成为可能，例如一个负责研究，一个负责写作 23。
    

---

## 6. ReAct 与 Function Calling：范式的融合与辨析

在当前的开发环境中，开发者常常困惑于“ReAct Agent”与“Tool Calling Agent”（如 OpenAI Assistants）的区别。事实上，这两者正在趋于融合。

### 6.1 技术实现的差异

- **传统 ReAct (Text-based):** 依赖 Prompt 中的 Few-shot 示例教导模型输出 `Action: ToolName` 文本。解析依赖正则。这在没有针对性微调的通用模型上很常见。
    
- **Function/Tool Calling (API-based):** OpenAI 等模型厂商在预训练或微调阶段，专门强化了模型输出结构化 JSON 的能力。开发者不再需要写复杂的 Prompt 来描述工具格式，而是直接将 JSON Schema 传给 API（如 `bind_tools`）29。
    

### 6.2 范式的融合

Function Calling 并没有杀死 ReAct，而是优化了它的“行动”环节。

即使使用了 Function Calling，ReAct 的核心精神——“先思考，再行动”——依然至关重要。

- **裸 Function Calling 的问题：** 如果直接将工具传给模型，很多模型会省略推理步骤，直接输出 JSON 调用。这退化回了“纯行动范式”（System 1），导致参数选择鲁莽或错误。
    
- **现代 ReAct 实现：** 最佳实践是结合两者。
    
    1. 使用 **Prompt** 强制模型在调用工具前输出一段推理文本（在 OpenAI o1 中是内部思维链，在 GPT-4 中可以是显式的文本消息）。
        
    2. 使用 **Function Calling** 机制来生成精确的工具参数。
        
    3. 将工具的返回结果作为 `ToolMessage` 传回模型，维持 ReAct 的观察循环 31。
        

因此，LangChain 的 `create_react_agent` 在新版中实际上是在编排一个图，这个图利用了模型的 Tool Calling 能力，但通过流程设计保留了 ReAct 的推理-观察循环特性 10。

---

## 7. 挑战、局限与失效模式

尽管 ReAct 极大地增强了 LLM 的能力，但在实际生产环境中，它面临着严峻的挑战。

### 7.1 上下文窗口爆炸（Context Window Explosion）

ReAct 极其消耗 Token。每一次循环，历史的 Thought、Action 和 verbose 的 Observation（有时包含整页 HTML 代码）都会被累积到 Prompt 中。

- **后果：** 随着对话进行，Prompt 迅速逼近模型的上下文上限（如 8k 或 32k tokens）。一旦超限，最早期的指令或记忆会被截断，导致 Agent 忘记任务目标或工具定义 34。
    
- **对策：** 需要引入记忆压缩（Memory Summarization）或将观察结果存入向量数据库（Vector Store），仅检索相关片段放入 Prompt，而非全量拼接。
    

### 7.2 错误传播与死循环（Loops & Error Propagation）

ReAct Agent 容易陷入逻辑死胡同。

- **典型场景：** Agent 搜索关键词 A，结果为空。它推理“我应该重试”，然后**完全相同**地再次搜索关键词 A。如此往复，直到 Token 耗尽或触发最大迭代次数限制。
    
- **原因：** LLM 对“重复动作无效”这一点的元认知能力较弱。
    
- **对策：** 需要在 Prompt 中加入“反思”（Reflexion）机制，或者在代码层检测重复的 Action Input 并强制中断 35。
    

### 7.3 解析错误与指令遵循

即使是强模型，偶尔也会生成不符合格式的输出。例如，在 Thought 中包含了 Action 的内容，或者忘记了 `Action Input:` 的前缀。这会导致解析器抛出异常，中断整个 Agent 进程。虽然 Function Calling 缓解了 JSON 格式错误，但模型仍可能生成不符合 Schema 校验（如类型错误）的参数 17。

---

## 8. 未来展望

### 8.1 推理的内化（Internalized Reasoning）

随着 OpenAI o1 等“推理模型”（Reasoning Models）的发布，ReAct 的显式过程正在被模型内化。o1 模型在输出最终 token 前，会在内部进行高密度的思维链推演（Hidden CoT）。这意味着未来的 Agent 可能不再需要在 Prompt 层面强制 `Thought:` 步骤，因为模型本身已经具备了 System 2 的思考能力。开发者可能只需要关注 Tool 的定义和结果的反馈 32。

### 8.2 多智能体系统（Multi-Agent Systems）

单体 ReAct Agent 的复杂度有限。未来的方向是将 ReAct Agent 作为一个“节点”，编织成庞大的多智能体网络。

- **层级化 ReAct：** 一个“经理 Agent”负责拆解任务，分发给多个“工人工 Agent”。
    
- **角色化分工：** 不同的 ReAct Agent 挂载不同的工具集（如一个挂载 Python 解释器负责计算，一个挂载搜索引擎负责检索），通过图架构协同工作。
    

### 8.3 概念辨析：Open Source "React Agent"

需要特别注意的是，在开源社区中存在一个名为 **"React Agent" (ReactAgent)** 的项目 3。该项目是一个基于 LLM 的代码生成工具，专门用于将用户故事（User Stories）转化为 **React.js** 前端组件。它与本报告讨论的 **ReAct (Reasoning + Acting) 认知架构** 是两个完全不同的概念，仅因命名相似而容易混淆。研究者和开发者在检索资料时需仔细甄别。

---

## 9. 结论

ReAct Agent 结构的提出，是 LLM 发展史上的一个里程碑。它并没有改变模型的底层参数，而是通过一种架构模式，释放了模型潜在的规划与反思能力。通过将**推理（内省）**与**行动（交互）**显式地耦合在同一个轨迹中，ReAct 解决了大模型“懂道理但没手脚”和“有手脚但没脑子”的困境。

尽管面临上下文消耗大、解析脆弱等工程挑战，但随着 LangGraph 等图计算框架的成熟以及模型自身推理能力的进化，ReAct 及其变体已成为构建自主 AI 应用（Autonomous Agents）的事实标准。理解 ReAct 的每一个微观步骤——从 Prompt 的构建到状态机的流转——是掌握现代 AI Agent 开发的关键。

---

## 数据引用表

| **核心概念 / 声明**                        | **引用来源 ID** |
| ------------------------------------ | ----------- |
| **ReAct 论文与核心定义**                    | 1           |
| **推理与行动的二分法与局限**                     | 1           |
| **提示模板结构 (Thought-Action)**          | 7           |
| **LangChain AgentExecutor 机制**       | 14          |
| **LangGraph 图架构与状态管理**               | 23          |
| **解析器 (Regex) 问题与 Function Calling** | 16          |
| **工具定义 (Pydantic/Docstrings)**       | 10          |
| **上下文窗口与错误传播挑战**                     | 34          |
| **同名开源项目 ReactAgent 辨析**             | 3           |
| **认知科学基础 (System 1 vs 2)**           | 4           |

