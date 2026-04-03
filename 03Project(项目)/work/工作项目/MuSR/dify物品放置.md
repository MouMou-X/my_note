---
tags: [LLM/Eval]
type: note
status: 🌿
---

### 关联文档
[[MuSR物品放置代码解析逻辑]]


> [!quote] # USER:
> 我想用dify的工作流来重新搭建这一套流程，你觉得我应该分成几个模块？


这是一个非常棒的工程挑战。正如我们刚才分析的，MuSR 的核心在于 **“神经-符号”（Neuro-Symbolic）** 架构：LLM 负责创意，Python 负责逻辑。

要在 Dify 中复刻这一流程，你不能只靠一串 LLM 节点，必须充分利用 Dify 的 **代码节点（Code Node）** 和 **迭代节点（Iteration Node）**。

建议将工作流拆分为 **4 个核心模块**。以下是详细的架构设计：

### 模块一：世界构建器 (The Generator)

目标：生成故事的“骨架”数据（JSON 格式）。

对应原流程：Madlib Prompt

- **节点 1：LLM (JSON模式)**
    
    - **提示词**：类似于原脚本的 Madlib Prompt。要求生成 3 个角色、2 个物品、4 个地点，以及 3 个具体的移动步骤（Move 1, Move 2, Move 3）。
        
    - **关键约束**：强制要求输出严格的 JSON 格式。
        
- **节点 2：代码节点 (Validator)**
    
    - **功能**：接收节点 1 的 JSON，校验格式是否正确（例如：是否有 3 个移动？地点是否在列表中？）。如果格式错误，抛出错误让工作流重试或终止。
        

### 模块二：上帝逻辑模拟器 (The Simulator) —— **最核心部分**

目标：确立“绝对真理”（Ground Truth）。决定谁看到了什么，物品最终在哪里。

对应原流程：Python 脚本中的 event_structure 和状态机逻辑。

- **警告**：**千万不要用 LLM 来做这一步**。LLM 记不住状态，容易产生幻觉（例如：明明A不在场，LLM却说A看到了）。
    
- **节点 3：代码节点 (Python State Machine)**
    
    - **输入**：模块一生成的 JSON（移动序列、角色位置）。
        
    - **逻辑（用 Python 编写）**：
        
        1. 初始化物品位置。
            
        2. 模拟 3 次移动。更新物品坐标。
            
        3. **计算可见性矩阵**：这是关键。你可以写死规则（例如：随机决定谁在场，或者设定规则“如果角色不是执行者，有 50% 概率看见”）。
            
        4. **输出**：生成一个结构化的任务列表（List），准备传给下一个模块。
            
        
        - _输出示例结构_：
            
            JSON
            
            ```
            [
              {"step": 1, "action": "A移X到Y", "observer": "B", "did_see": true},
              {"step": 1, "action": "A移X到Y", "observer": "C", "did_see": false},
              ...
            ]
            ```
            

### 模块三：推理引擎 (The Reasoner)

目标：为模块二产生的“真理”生成合理的解释（思维链）。

对应原流程：Entailment Tree 生成步骤。

- **节点 4：迭代节点 (Iteration)**
    
    - **输入**：模块二输出的任务列表。
        
    - **内部逻辑**：
        
        - **LLM 节点 (Reasoning)**：
            
            - **提示词**：你是一个逻辑推理大师。已知事实：[角色] [看到了/没看到] 这个动作。请生成一条“故事事实”（Story Fact）和一条“常识”（Commonsense）来支持这个结论。
                
            - **输入变量**：来自迭代器的 `item.action`, `item.observer`, `item.did_see`。
                
    - **输出**：一个包含所有推理逻辑的列表。
        

### 模块四：叙事渲染器 (The Renderer)

目标：将所有零散信息包装成自然语言故事。

对应原流程：Opening Prompt 和最终输出组装。

- **节点 5：LLM (Opening Generator)**
    
    - **提示词**：根据模块一的初始状态，写一段开场白。必须明确说明所有人都知道物品的初始位置。
        
- **节点 6：代码节点 (Assembler)**
    
    - **功能**：将“开场白”（节点 5）、“移动过程”（模块一）和“推理逻辑”（模块三）拼接成最终的数据集格式。
        

---

### Dify 工作流编排建议图

为了帮助你理解，这里是一个可视化的逻辑流：

1. **Start** ->
    
2. **LLM (Madlib)** -> [JSON: 角色, 物品, 移动计划] ->
    
3. **Code (State Machine)** -> [Python 计算出：谁在什么时候看见了什么] ->
    
4. **Iteration (Loop over Visibility Events)**:
    
    - Inside Loop: **LLM (Reasoning)** -> [生成：因为他在睡觉，所以没看见]
        
5. **LLM (Opening Writer)** -> [生成：开场白] ->
    
6. **Template (Final Output)** -> **End**
    

### 你需要注意的三个坑

1. 上下文隔离：
    
    在“模块三（推理）”中，Prompt 必须严格。不要让 LLM 只有“他没看见”这一个信息，要告诉 LLM 这一步发生了什么动作。否则 LLM 会瞎编理由（比如“他没看见是因为他在月球上”，但这可能与故事背景冲突）。
    
2. 代码节点的健壮性：
    
    Dify 的 Code Node 是沙箱环境，通常不支持安装额外的庞大库（如 pandas/numpy）。你的状态机逻辑最好用纯 Python (List/Dict 操作) 实现，保持轻量。
    
3. JSON 解析的稳定性：
    
    第一个 LLM 节点生成的 JSON 经常会带有 Markdown 标记（json ... ）。在进入代码节点前，记得写一段简单的字符串处理代码把这些标记清洗掉，否则 json.loads() 会报错。
    

### 我可以为你做的下一步

如果你准备动手了，**我可以为你写“模块二：上帝逻辑模拟器”的 Python 代码**。这是整个流程中最复杂、最容易出错的部分，它需要处理状态更新和可见性逻辑。你需要吗？


---

# 数据结构
```
# 初始化数据容器
items = []           # 物品列表
people = []          # 人物列表
people_data = []     # 人物详细信息
moves = []           # 移动数据
move_strs = []       # 移动描述字符串
locations = []       # 位置列表
world_state = []     # 物品初始位置

---

people_data = [
    {'name': 'Sarah', 'role': 'The Barista', 'motivation': '...'},
    {'name': 'Luis', 'role': 'A customer', 'motivation': '...'},
    {'name': 'John', 'role': 'A cafe worker', 'motivation': '...'}
]
people = ['Sarah', 'Luis', 'John']

---

# 抽象出的moves数据结构
moves = [
    {'mover': 'Luis', 'item': 'almond milk', 'from': 'fridge', 'to': 'back shelves', 'justification': '...'},
    {'mover': 'Sarah', 'item': 'coffee bag', 'from': 'back shelves', 'to': 'front counter', 'justification': '...'},
    {'mover': 'Sarah', 'item': 'almond milk', 'from': 'back shelves', 'to': 'fridge', 'justification': '...'}
]

items = ['almond milk', 'coffee bag']  
locations = ['back shelves', 'fridge', 'front counter']  
world_state = [['almond milk', 'fridge'], ['coffee bag', 'back shelves']]  # 初始位置


```