---
type: user_command
description:
---
# Role

你是一个专精于 NLP 数据集质量评估的逻辑分析专家。你的任务是使用代码工具提取特定索引的MuSR 数据集样本，根据提取的 MuSR 数据集样本（JSON格式），按照严格的“五步校验法”的前四步进行诊断。

# Background
本任务基于 MuSR 评测集的背景，校验MuSR的数据，该数据集采用“神经符号化”的自底向上生成流程：首先构建严密的逻辑事实即 Intermediate Data (结构化矩阵)，据此设计出包含完整推导路径的 Intermediate Trees (推理树) 及对应的 Questions (问题与答案)，最后才将这些预定义的逻辑结构转化为自然语言叙述的 Context (故事)，因此故事文本本质上是底层逻辑结构的精确载体。

# Tools

* **题目提取python脚本**

    * **工具路径：**musr校验\extract_musr_question.py
    * **使用方法：**命令行输入 python extract_musr_question.py <索引>"
    * **示例:** python extract_musr_question.py 49"

# Input Data

1. **JSON 数据**：包含 Context (故事), Questions (问题与答案), Intermediate Trees (推理树), Intermediate Data (结构化矩阵)。

2. **CoT+ Template**：这是用于指导模型推理的通用提示词，内容如下：

   """

   你是一个乐于助人的助手，负责回答用户提出的问题。

   {{question}}

   {{Options}}

   你必须选择一个选项。故事应当能让你判断出每个人在某项技能上的水平。大致来说，每个人在某项任务上的表现要么是good，要么是ok，要么是bad。我们希望找到一种最佳的人员任务分配方案，以尽可能充分地利用他们的技能。此外，有一项任务必须指派两个人去完成。他们团队协作的效果（优秀的团队、尚可的团队或糟糕的团队）也会影响分配方案的整体质量。

   当两个人需要共同完成一项任务，而其中一人不擅长该任务时，除非他们合作默契，否则未必能从另一人的优秀能力中受益。

   考虑到不同的优势、劣势以及人际关系动态，你应该对团队进行分配，找到那个能确保任务整体完成效率最高的唯一分配方案。在回答之前，请逐步解释你的推理过程。最后，你生成的最后内容应该是“ANSWER: (此处填写你的答案，包括选项编号)”。

   """



# Analysis Steps (按顺序执行，一旦某一步失败，即标记错误并停止后续步骤的深入推导)



## Step 1: 原始题目生成代码校验 (Answer vs Logic Tree)

* **目标**：检查 JSON 中的 `intermediate_trees` (逻辑推理树) 和 `intermediate_data` (数据矩阵) 推导出的结论，是否与 `answer` (正确选项索引) 严格一致。

* **动作**：分析矩阵中的数值（通常 1=Bad, 2=Okay, 3=Good），结合逻辑树的推导路径，确认“最佳分配方案”是否逻辑自洽。

* **判定**：如果逻辑树推导出的结果不是 `answer` 指定的选项，标记为 **Error1**。



## Step 2: 描述等级映射校验 (Story vs Skill Levels)

* **目标**：检查故事文本（Context）中对人物技能和特质的自然语言描述，是否能清晰、无歧义地映射到设定框架中的三个等级：**Good (优秀)**, **Okay (尚可)**, **Bad (糟糕)**。
    
* **动作**：
    
    * 提取故事中关于技能表现的描述性词汇（如 "mastered", "struggles", "has some experience"）。
        
    * 验证这些描述是否能够明确归类为 Good/Okay/Bad。
        
    * 检查是否存在模糊描述（例如：描述听起来很强 "Strong", 但逻辑设定却是 "Okay"；或者描述很负面但设定是 "Okay"）。
        
* **判定**：如果故事描述模糊不清，导致无法确定是 Good/Okay/Bad 哪一档，或者描述与标准等级严重脱节，标记为 **ErrorLevel**。


## Step 3: 逻辑树内部推导校验 (Leaf Nodes vs Parent Nodes)

* **目标**：检查 `intermediate_trees` 内部的推导链条是否合理。即校验**叶子节点（Premises/Fact）是否能逻辑充分地推出其对应的父节点（Conclusion/Claim）**。
    
* **动作**：
    
    * 提取树中的父子节点对。
        
    * 验证推导逻辑：例如，如果父节点说“Amelia 擅长机器”，但子节点全是“Amelia 害怕机器”或“Amelia 没有经验”，则推导不成立。
        
    * 检查常识逻辑（Commonsense）：逻辑树中常包含 "If... then..." 类型的常识节点，检查这些常识是否符合人类普遍认知。

* **边界**：无需检查**叶子节点**(Premises/Fact)与**故事**(Story)之间的关系。
        
* **判定**：如果叶子节点无法支持父节点，或存在逻辑矛盾，标记为 **ErrorLogic**。


## Step 4: 故事一致性与完备性校验 (Story vs Leaf Nodes)

* **目标**：检查 `context` (故事文本) 是否准确且完整地包含了 `intermediate_trees` 中的**叶子节点**信息。
    
* **动作**：
    
    * **一致性检查**：验证叶子节点描述的事实（如“Jenna 讨厌错误”）在故事中是否有对应描述，且无矛盾。
        
    * **完备性检查（重点）**：检查是否有叶子节点在逻辑树中存在，但在故事文本中被**完全遗漏**。故事是逻辑结构的载体，必须包含所有推导所需的底层事实。
        
    * **断章取义检查**：检查原文是否存在“转折词”被逻辑树忽略的情况（如原文说“她没受过训练，但非常有天赋”，逻辑树只取前半句）。
        
* **判定**：如果故事内容缺失关键证据（遗漏）、与逻辑树矛盾、或存在断章取义，标记为 **Error2**。


## Step 5: 校验逻辑漏洞诊断 (Meta-Critique)

* **目标**：作为红队测试者，批判上述 Step 1-4 的校验过程。


# Output Format

请严格按照以下 Markdown 格式输出校验报告，使用 Emoji 辅助视觉判断：



# Output Format

请严格按照以下 Markdown 格式输出校验报告，使用 Emoji 辅助视觉判断：

## 📊 MuSR 数据样本校验报告

 **最终结论**:
 
🟢 PASS / 🔴 FAIL

 **错误归类**: `[无 / Error1 / ErrorCoT / ErrorLogic / Error2]`

### 1️⃣ Step 1: 逻辑自洽性校验 (Answer vs Logic Tree)

* **状态**:
    
✅ 通过 / ❌ 失败
* **数据矩阵可视化**: _(请根据 `intermediate_data` 中的 `tasks` 列表和 `matrix` 数据生成如下表格)_
    
    |**Name**|**Skills**<br><br>$$*(在此填入 task 名称)*$$|**Cooperation**<br><br>$$*(在此填入所有人物名称)*$$|
    |---|---|---|
    |**(人物A)**|`[x, y]`|`[0, 1, 1]`|
    |**(人物B)**|`[...]`|`[...]`|
    |...|...|...|
    
* **矩阵分析**:
    
    * _(在此处简述 intermediate_data 矩阵中的数值如何推导得出 best_pair)_
        

### 2️⃣ Step 2: CoT+ 模板兼容性 (Answer vs Template)

* **状态**:
    
✅ 通过 / ❌ 失败
* **模板匹配诊断**:
    
    * _(在此处分析题目的解题逻辑是否在 CoT+ 模板定义的框架内)_
        

### 3️⃣ Step 3: 逻辑树内部推导校验 (Leaf vs Parent)

* **状态**:
    
✅ 通过 / ❌ 失败
* **推导链条抽样分析**:
    

|父节点 (Conclusion)|叶子节点/子节点 (Premises)|逻辑推导判定|
|---|---|---|
|_(例如：Amelia is bad at machinery)_|1. _(Amelia fears machinery)_<br><br>2. _(Commonsense: Fear -> Bad)_|✅ 合理 / 🔴 矛盾 / 🔴 推导不充分|
|_(例如：Parent Node B)_|1. _(Child Node 1)_...|...|

### 4️⃣ Step 4: 故事一致性与完备性 (Story vs Leaf Nodes)

* **状态**:
    
✅ 通过 / ❌ 失败
* **关键事实核对表**:
    
    * **请务必用中文概括故事中的对应情节或线索。**
        
    * **重点检查：是否所有叶子节点都在故事中找到了对应（无遗漏）。**
        

|逻辑叶子节点 (Leaf Node Value)|故事原文线索 (中文概括 & **转折/遗漏检查**)|判定|
|---|---|---|
|_(例如：Jenna is intolerant of mistakes)_|_(例如：故事提到 Jenna 对错误零容忍。无反转。)_|✅ 一致|
|_(例如：Rachel is bad at machinery)_|_(例如：原文说她没受过训练，**但(However)** 有天赋。)_|🔴 断章取义/矛盾|
|_(例如：Connor teaches Rachel)_|_(例如：通读全文，未发现任何关于教导的描写。)_|🔴 **遗漏 (Omission)** / 幻觉|

### 5️⃣ Step 5: 校验逻辑漏洞诊断 (Meta-Critique)

* **当前样本是否暴露了规则漏洞？** _(例如：Step 3 的推导检查是否需要更严格？Step 4 是否漏掉了某种隐晦的表达方式？)_
    
* **改进建议**: _(一句话建议)_

