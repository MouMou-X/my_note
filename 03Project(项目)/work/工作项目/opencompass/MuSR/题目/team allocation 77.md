---
tags: [LLM/Eval]
type: note
status: 🌿
---

## 📊 MuSR 数据样本校验报告 (索引77)

> **最终结论**:
> 
> 🔴 FAIL

> **错误归类**: `Error2` (故事遗漏关键叶子节点)

---

### 1️⃣ Step 1: 逻辑自洽性校验 (Answer vs Logic Tree)

* **状态**: ✅ 通过

* **数据矩阵可视化**: (1=Bad, 2=Okay, 3=Good)
    
    | **Name** | **Skills** [Front Desk, Housekeeping] | **Cooperation** [Emily, Alex, Molly] |
    |---|---|---|
    | Emily | `[1, 1]` | `[0, 1, 1]` |
    | Alex | `[3, 3]` | `[1, 0, 3]` |
    | Molly | `[1, 3]` | `[1, 3, 0]` |
    
* **矩阵分析**:
    
    - **best_pair**: `[[Emily], [Alex, Molly]]` → 选项2: "Front Desk: Emily, Housekeeping: Alex and Molly"
    - **三种方案评估**:
      - **选项0** (Alex前台, Emily+Molly家政): Alex前台=3(Good)，但Emily+Molly合作=1(Bad)，且Emily家政=1(Bad)
      - **选项1** (Molly前台, Alex+Emily家政): Molly前台=1(Bad)，Alex+Emily合作=1(Bad)
      - **选项2** (Emily前台, Alex+Molly家政): Emily前台=1(Bad)，但Alex+Molly合作=3(Good)，且双方家政=3+3(Good)
    - **逻辑**: 虽然选项2的前台人员技能差，但根据CoT+模板规则——"当两人共同完成任务时，如果合作不默契，则无法从另一人优秀能力中受益"，选项0的Emily+Molly(Bad合作)会拖累整体。选项2的Alex+Molly(Good合作+双Good技能)形成最强家政团队，牺牲前台换取更高整体效率。**逻辑自洽**。

---

### 2️⃣ Step 2: 描述等级映射校验 (Story vs Skill Levels)

* **状态**: ✅ 通过

* **模板匹配诊断**:

| 人物 | 技能 | 矩阵等级 | 故事描述 | 映射判定 |
|---|---|---|---|---|
| Alex | Front Desk | Good(3) | "sociable, always seen interacting with guests ensuring their comfort and satisfaction" + "management role at a local hotel" | ✅ 清晰映射Good |
| Alex | Housekeeping | Good(3) | "meticulous about cleanliness" + "janitor at a daycare" | ✅ 清晰映射Good |
| Emily | Front Desk | Bad(1) | "prone to mixing up bookings" + "struggle to grasp the software systems" | ✅ 清晰映射Bad |
| Emily | Housekeeping | Bad(1) | "dust and dirt in corners and under furniture were missed" + "forgetting to stock up supplies" | ✅ 清晰映射Bad |
| Molly | Front Desk | Bad(1) | "overwhelmed by confrontational guests" + "difficulty handling multiple people" | ✅ 清晰映射Bad |
| Molly | Housekeeping | Good(3) | "pristine home" + "part-time college job where she cleaned dorm rooms" | ✅ 清晰映射Good |

| 合作关系 | 矩阵等级 | 故事描述 | 映射判定 |
|---|---|---|---|
| Emily-Alex | Bad(1) | "accusing Alex for her own mistakes" | ✅ 清晰映射Bad |
| Emily-Molly | Bad(1) | "leaving extra work for Molly" + "disrespect she felt" | ✅ 清晰映射Bad |
| Alex-Molly | Good(3) | "respected Alex, often seeking advice" + "Alex was often seen helping Molly" | ✅ 清晰映射Good |

---

### 3️⃣ Step 3: 逻辑树内部推导校验 (Leaf vs Parent)

* **状态**: ✅ 通过

* **推导链条抽样分析**:

| 父节点 (Conclusion) | 叶子节点/子节点 (Premises) | 逻辑推导判定 |
|---|---|---|
| Alex is good at housekeeping | 1. Alex is meticulous about cleanliness<br>2. Alex used to work as a janitor<br>3. Commonsense: 爱清洁+专业经验→擅长家政 | ✅ 合理 |
| Emily is bad at front desk | 1. Emily struggles with software systems<br>2. Emily is prone to mix up bookings<br>3. Commonsense: 容易出错+不熟软件→不擅长前台 | ✅ 合理 |
| Alex is good at front desk | 1. Alex enjoys guest interaction<br>2. Alex previously worked as hotel manager<br>3. Commonsense: 酒店管理经验+喜欢客户互动→擅长前台 | ✅ 合理 |
| Molly is good at housekeeping | 1. Single mother, keeps spotless home<br>2. Part-time job cleaning dorm rooms<br>3. Commonsense: 专业清洁经验+带娃仍保持整洁→擅长家政 | ✅ 合理 |
| Emily and Molly work badly together | 1. Molly feels burdened and disrespected<br>2. Emily leaves extra work for Molly<br>3. Commonsense: 推卸工作→合作差 | ✅ 合理 |
| Emily and Alex work badly together | 1. Alex has confronted Emily<br>2. Emily blames Alex for her mistakes<br>3. Commonsense: 甩锅+冲突未解决→合作差 | ⚠️ 详见下方 |
| Molly is bad at front desk | 1. Difficulty with confrontational guests<br>2. Overwhelmed by multiple people<br>3. Commonsense: 怕冲突+怕多人→不擅前台 | ✅ 合理 |
| Alex and Molly work well together | 1. Molly respects Alex, seeks advice<br>2. Alex helps Molly finish tasks<br>3. Commonsense: 互相尊重+帮助→合作好 | ✅ 合理 |
| Emily is bad at housekeeping | 1. Overlooks dust and dirt<br>2. Forgets to pick up supplies<br>3. Commonsense: 忘准备+忽略细节→不擅家政 | ✅ 合理 |

---

### 4️⃣ Step 4: 故事一致性与完备性 (Story vs Leaf Nodes)

* **状态**: ❌ 失败

* **关键事实核对表**:

| 逻辑叶子节点 (Leaf Node) | 故事原文线索 (中文概括) | 判定 |
|---|---|---|
| Alex is meticulous about cleanliness in his personal life | "His attention-to-detail made him especially meticulous about cleanliness" | ✅ 一致 |
| Alex used to work as a janitor at a day care | "his days as a janitor at a daycare" | ✅ 一致 |
| Emily struggles with using the software systems | "Her struggle to grasp the software systems we used" | ✅ 一致 |
| Emily is prone to mix up bookings on high stress days | "On days when the pressure built up, Emily was prone to mixing up bookings" | ✅ 一致 |
| Alex enjoys interacting with guests and ensuring their comfort | "sociable, always seen interacting with guests ensuring their comfort and satisfaction" | ✅ 一致 |
| Alex previously worked as a manager at a smaller local hotel | "cemented by his management role at a local hotel" | ✅ 一致 |
| Molly is a single mother and keeps a spotless home despite having two young kids | "a single mother and yet managed to maintain a pristine home" | ⚠️ **部分遗漏**: 故事说"single mother"+"pristine home"，但**未提及"two young kids"** |
| Molly had a part-time job in college where she cleaned dorm rooms | "her part-time college job where she cleaned dorm rooms" | ✅ 一致 |
| Molly feels burdened and disrespected by Emily's habit | "the disrespect she felt from Emily's habit of leaving her extra work" | ✅ 一致 |
| Emily often leaves extra work for Molly to finish | "her habit of leaving extra work for Molly" | ✅ 一致 |
| **Alex has confronted Emily about her behavior on multiple occasions** | 故事中**未发现任何关于Alex质问Emily的描写**，只提到Emily指责Alex | 🔴 **遗漏 (Omission)** |
| Emily often blames Alex for her own mistakes | "Blame-games were common, with her often accusing Alex for her own mistakes" | ✅ 一致 |
| Molly had difficulty dealing with confrontational guests in a simulated front desk situation | 故事说"overwhelmed by confrontational guests"，但**未提及是模拟情境** | ⚠️ **轻微遗漏** |
| Molly gets overwhelmed easily in situations that require interactions with multiple people | "difficulty handling multiple people at the same time" | ✅ 一致 |
| Molly respects Alex and often seeks his advice on how to handle difficult cleaning tasks | "She respected Alex, often seeking advice on complex cleaning tasks" | ✅ 一致 |
| Alex often helps Molly finish her tasks when he is done with his | "Alex was often seen helping Molly finish her tasks once he had completed his own" | ✅ 一致 |
| Emily overlooks dust and dirt in corners and under furniture | "dust and dirt in corners and under furniture were missed" | ✅ 一致 |
| Emily often forgets to pick up supplies before starting her shift | "forgetting to stock up supplies before her shifts" | ✅ 一致 |

**关键问题**:
1. 🔴 **严重遗漏**: 叶子节点"Alex has confronted Emily about her behavior on multiple occasions"在故事中完全没有对应描写。这是支撑"Emily and Alex work badly together"结论的关键事实之一。
2. ⚠️ 叶子节点提到Molly有"two young kids"，但故事中只说她是single mother，未提及孩子数量。
3. ⚠️ 叶子节点提到"simulated front desk situation"，但故事未明确是模拟场景。

---

### 5️⃣ Step 5: 校验逻辑漏洞诊断 (Meta-Critique)

* **当前样本暴露的规则漏洞**:
    - Step 4 发现叶子节点"Alex has confronted Emily"是**幻觉信息**——逻辑树假设了故事中不存在的事实。这说明数据集生成流程中，逻辑树的叶子节点未能严格从故事文本中提取/验证。
    - 虽然"Emily blames Alex"单独也能支撑"合作差"的结论（常识节点只需部分条件满足），但叶子节点声称的事实必须在故事中存在，否则违反数据集的"神经符号化"一致性原则。

* **改进建议**: 数据生成流程应增加"叶子节点→故事文本"的回溯验证步骤，确保每个explicit类型叶子节点在故事中有明确对应。


错误类型：故事内容与逻辑树叶子节点：故事遗漏了叶子节点
1、逻辑树：莫莉是一位单身母亲，尽管有两个年幼的孩子，她仍保持家中一尘不染。
1、故事原文：一位单身母亲，却仍能保持家中整洁如新。（遗漏了部分内容，轻微不影响答题）
2、逻辑树：Alex曾多次就Emily的行为与她对质。
2、故事原文：故事中未发现任何关于Alex质问Emily的描写，只提到Emily指责Alex

总结：gpt-4在编写故事时，没有严格遵循叶子节点的内容。叶子节点有遗漏。
错误2是较为关键的遗漏。