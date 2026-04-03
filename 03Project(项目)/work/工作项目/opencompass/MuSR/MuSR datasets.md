---
tags: [LLM/Eval]
type: note
status: 🌿
---

我来帮你理清整个项目的代码结构。让我先阅读核心模块的代码：
让我继续读取其他核心模块：
让我继续读取剩余模块：
现在我已经理清了整个项目的代码结构。以下是项目代码架构的完整梳理：

---

## **MuSR 项目代码架构**

这是一个**多步推理数据集构建**项目，用于生成三类推理任务的数据集：谋杀谜题、物品放置追踪、团队分配。

---

### **核心模块关系图**

```
┌─────────────────────────────────────────────────────────────────┐
│                    musr_dataset_scripts/                        │
│  (入口脚本: create_murder_mysteries.py 等)                       │
└───────────────────────────┬─────────────────────────────────────┘
                            │ 调用
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              src/dataset_types/                                  │
│  MurderMysteryDataset / ObjectPlacementsDataset /               │
│  TeamAllocationDataset  (继承 DatasetBuilder)                    │
└───────────────────────────┬─────────────────────────────────────┘
                            │ 继承
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              src/dataset_builder.py                              │
│  DatasetBuilder (核心基类)                                       │
│  - 递归推理树扩展算法 (Recursive Reasoning Tree Expansion)        │
│  - Madlib采样、树结构构建、LLM推理调用                            │
└──────────┬──────────────────┬────────────────┬──────────────────┘
           │                  │                │
           ▼                  ▼                ▼
┌──────────────────┐  ┌──────────────────┐  ┌───────────────────┐
│  src/logic_tree/ │  │   src/model/     │  │  src/validators/  │
│  LogicTree       │  │ OpenAIModel/     │  │ StructureValidator│
│  LogicNode       │  │ HFModel(Model)   │  │ ForbiddenTextVal..│
│  (推理树数据结构) │  │ (LLM接口封装)    │  │ ModelValidator    │
└──────────────────┘  └──────────────────┘  └───────────────────┘
           │
           ▼
┌──────────────────┐
│  src/madlib/     │
│  Madlib          │
│  (随机采样器)     │
└──────────────────┘
           │ 读取
           ▼
┌──────────────────┐
│  domain_seed/    │
│  names.json      │
│  motives.json    │
│  crime_scenes... │
│  (种子数据)       │
└──────────────────┘
```

---

### **各模块详细职责**

| 模块 | 核心类/文件 | 职责 |
|------|-------------|------|
| **src/dataset_builder.py** | `DatasetBuilder` | 数据集构建基类，包含：递归推理树扩展算法(`complete_structure`)、Madlib采样(`sample_madlib`)、树结构构建(`build_structure`)、LLM推理封装(`inference`) |
| **src/logic_tree/tree.py** | `LogicTree`, `LogicNode` | 推理树数据结构，支持填充(`populate`)、剪枝(`prune`)、序列化(`to_json`/`from_json`)、打印(`print_for_gpt`) |
| **src/dataset_types/** | 三个子类 | 各领域具体实现：<br>`MurderMysteryDataset`: 创建嫌疑人树(MMO+可疑事实)、章节树、故事章节<br>`ObjectPlacementsDataset`: 物品移动序列、观察推理树<br>`TeamAllocationDataset`: 技能/关系矩阵、最优分配 |
| **src/model/** | `Model`, `OpenAIModel`, `HFModel` | LLM接口抽象，支持OpenAI API和HuggingFace模型，含重试/缓存机制 |
| **src/validators/** | `Validator`, `StructureValidator`, `ForbiddenTextValidator`, `ModelValidator` | LLM输出校验器：结构校验、禁用词校验、模型语义校验 |
| **src/madlib/madlib.py** | `Madlib` | 从JSON种子文件随机采样（姓名、动机、凶器等） |
| **musr_dataset_scripts/** | 三个入口脚本 | 数据集生成入口，调用对应Dataset类生成JSON数据 |
| **eval/eval.py** | `main()` | 模型评估脚本，支持多模型、多数据集、多prompting策略(regular/cot/cot+) |
| **domain_seed/** | JSON文件 | 生成数据所需的种子数据（名字、场景、凶器等） |

---

### **数据流（以谋杀谜题为例）**

```
1. Madlib采样 → 受害者/嫌疑人信息
2. create_suspect_trees() → 为每个嫌疑人构建MMO+可疑事实的LogicTree
   └─ complete_structure() → 递归调用LLM填充树节点（推理树扩展算法）
3. create_chapter_trees() → 分离有罪树(3个MMO分支)和无辜树(2个MMO+可疑事实)
4. create_chapter() → 调用LLM为每棵树生成故事章节
5. 组装 → 多个章节 + intro → 完整谜题
6. create_dataset_question_object() → 输出标准JSON格式
```

---

### **关键算法：递归推理树扩展**

定义在 `DatasetBuilder.complete_structure()` 和 `iteratively_complete_v2()`：

1. 遍历树中所有有空值子节点的节点
2. 使用ICL prompt让LLM生成推导步骤（显式事实 + 常识知识）
3. 使用Validator校验输出
4. 递归处理所有子节点直至叶节点

---

如果需要我进一步解释某个模块的细节，请告诉我。