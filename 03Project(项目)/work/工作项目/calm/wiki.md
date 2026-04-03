---
tags: [数学/因果推理]
type: reference
status: 🌿
---

# CaLM (Causal Language Models Benchmark) 模块文档

## 1. 模块概述

CaLM (Causal Language Models Benchmark) 是 OpenCompass 框架中用于评估大型语言模型 (LLM) **因果推理能力**的综合性基准测试模块。该模块基于因果推理的理论框架，系统性地评估模型在不同层级因果任务上的表现。

### 主要特性

- **多层级因果任务**: 涵盖关联 (Association)、因果发现 (Causal Discovery)、反事实 (Counterfactual)、干预 (Intervention) 四大类任务
- **中英双语支持**: 所有任务均提供中文 (CN) 和英文 (EN) 版本
- **多样化提示工程**: 支持 basic、adversarial、CoT、IcL 等多种 prompt 风格
- **全面评估体系**: 包含核心指标计算和错误分析两大评估维度
- **灵活的评估方式**: 支持选择题、概率计算、开放式生成等多种答案类型

---

## 2. 目录结构

```
calm/
├── calm.py                     # 核心模块：CaLMDataset 和 CaLMEvaluator 类
├── __init__.py                 # 模块初始化，导出核心类
├── data_processing/            # 数据处理模块
│   ├── prompt/                 # 各任务的 prompt 模板 (30+ 个文件)
│   │   ├── ATE.py             # 平均处理效应任务 prompt
│   │   ├── NDE.py             # 自然直接效应任务 prompt
│   │   ├── NIE.py             # 自然间接效应任务 prompt
│   │   ├── ETT.py             # 处理效应任务 prompt
│   │   ├── CDE.py             # 控制直接效应任务 prompt
│   │   ├── PN.py              # 必要性概率任务 prompt
│   │   ├── PS.py              # 充分性概率任务 prompt
│   │   ├── AR-B_CaLM-AR.py    # 抽象推理任务 prompt
│   │   ├── BAS-B_backadj.py   # 后门调整集任务 prompt
│   │   ├── BAS-C_max-BAS.py   # 最大后门调整集任务 prompt
│   │   ├── BAS-C_min-BAS.py   # 最小后门调整集任务 prompt
│   │   ├── BAS-C_mix-BAS.py   # 混合后门调整集任务 prompt
│   │   ├── CA-B_FA.py         # 因果归因 (FA) 任务 prompt
│   │   ├── CA-B_FP.py         # 因果归因 (FP) 任务 prompt
│   │   ├── CB-B_collider-bias.py  # 碰撞偏差任务 prompt
│   │   ├── CEG-O_E-CARE.py    # 因果解释生成任务 prompt
│   │   ├── CEI-B.py           # 因果效应识别任务 prompt
│   │   ├── CORR-B_correlation.py  # 相关性任务 prompt
│   │   ├── CR-B_det-counterfactual.py  # 确定性反事实任务 prompt
│   │   ├── CR-C_CRASS.py      # CRASS 反事实推理任务 prompt
│   │   ├── EAE-B_exp-away.py  # 解释消除效应任务 prompt
│   │   ├── ECI-B_CTB.py       # 事件因果识别 (CTB) 任务 prompt
│   │   ├── ECI-B_ESC.py       # 事件因果识别 (ESC) 任务 prompt
│   │   ├── ECI-B_MAVEN-ERE.py # 事件因果识别 (MAVEN) 任务 prompt
│   │   ├── FAS-C_FAS.py       # 前门调整集任务 prompt
│   │   ├── IV-C_CaLM-IV.py    # 工具变量任务 prompt
│   │   ├── PCD-B_COPA.py      # 成对因果发现 (COPA) 任务 prompt
│   │   ├── PCD-B_E-CARE.py    # 成对因果发现 (E-CARE) 任务 prompt
│   │   ├── PCD-C_COPA.py      # 成对因果发现复杂版 (COPA) prompt
│   │   ├── PCD-C_E-CARE.py    # 成对因果发现复杂版 (E-CARE) prompt
│   │   └── AC-B_causal_judgement.py  # 实际因果判断任务 prompt
│   ├── generate_questions.py   # 问题生成器：根据任务和 prompt 风格生成问题
│   └── task_hiearchy.py        # 任务层级映射：定义任务到数据路径的映射
├── evaluation/                 # 评估模块
│   ├── accuracy/               # 准确率计算模块
│   │   ├── choice.py          # 选择题准确率计算
│   │   ├── prob.py            # 概率答案准确率计算
│   │   └── open-ended.py      # 开放式答案评估 (Rouge-L)
│   ├── error/                  # 错误分析模块
│   │   └── basic_adversarial/ # 基础和对抗性 prompt 的错误分析
│   │       ├── CLADDER.py     # CLADDER 类任务错误分析
│   │       ├── Natural.py     # 自然语言任务错误分析
│   │       ├── Probability.py # 概率任务错误分析
│   │       ├── AS.py          # 调整集任务错误分析
│   │       ├── AC-B_causal_judgement.py
│   │       ├── AR-B_CaLM-AR.py
│   │       ├── CA-B.py
│   │       ├── CEI-B.py
│   │       ├── CR-C_CRASS.py
│   │       ├── ECI.py
│   │       ├── PCD-B.py
│   │       └── PCD-C.py
│   ├── labeling/              # 答案标注和提取模块
│   │   ├── common_answers.py  # 通用答案模式定义
│   │   ├── CLADDER.py         # CLADDER 类任务标注
│   │   ├── Natural.py         # 自然语言任务标注
│   │   ├── Probability.py     # 概率任务标注
│   │   ├── AS.py              # 调整集任务标注
│   │   ├── CEG-O_E-CARE.py    # 因果解释生成标注
│   │   └── ...                # 其他任务特定标注模块
│   ├── core_metrics.py         # 核心指标计算：整合标注和准确率计算
│   └── errors.py               # 错误识别主逻辑：识别模型响应中的各类错误
└── utils/
    └── load_items.py           # 数据加载工具：从 JSON 文件加载数据实例
```

---

## 3. 核心组件

### 3.1 CaLMDataset 类

`CaLMDataset` 是数据集加载类，继承自 `BaseDataset`，通过 `@LOAD_DATASET.register_module()` 装饰器注册到 OpenCompass 框架。

**文件位置**: [calm.py](file:///d:/project/opencompass/opencompass/datasets/calm/calm.py)

```python
@LOAD_DATASET.register_module()
class CaLMDataset(BaseDataset):

    @staticmethod
    def load(path: str, prompt_style: str) -> datasets.Dataset:
        """加载 CaLM 数据集
        
        Args:
            path: 数据集 JSON 文件路径
            prompt_style: prompt 风格 (如 'basic', 'basic-CN', 'zero-shot-CoT' 等)
            
        Returns:
            datasets.Dataset: 包含问题和 ground truth 的数据集
        """
        question_list = generate_question_list(dataset_path=path, prompt_style=prompt_style)
        dataset = Dataset.from_list(question_list)
        return dataset
```

**参数说明**:

| 参数             | 类型  | 说明                        |
| -------------- | --- | ------------------------- |
| `path`         | str | 数据集 JSON 文件的路径，文件名需包含任务名称 |
| `prompt_style` | str | prompt 风格，决定问题的格式和语言      |

### 3.2 CaLMEvaluator 类

`CaLMEvaluator` 是评估器类，继承自 `BaseEvaluator`，通过 `@ICL_EVALUATORS.register_module()` 装饰器注册。

```python
@ICL_EVALUATORS.register_module()
class CaLMEvaluator(BaseEvaluator):

    def __init__(self, core_metrics, error_analysis, prompt_style, task) -> None:
        """初始化评估器
        
        Args:
            core_metrics: 是否计算核心指标 (准确率)
            error_analysis: 是否进行错误分析
            prompt_style: prompt 风格
            task: 任务名称
        """
        
    def score(self, predictions: List, references: List) -> dict:
        """计算评估分数
        
        Args:
            predictions: 模型预测结果列表
            references: ground truth 列表
            
        Returns:
            dict: 包含 Accuracy 和/或错误分析指标的字典
        """
```

**参数说明**:

| 参数 | 类型 | 说明 |
|------|------|------|
| `core_metrics` | bool | 是否计算核心指标 (Accuracy) |
| `error_analysis` | bool | 是否进行错误分析 |
| `prompt_style` | str | prompt 风格 |
| `task` | str | 任务名称，如 'ATE-B_ATE-natural_EN' |

**返回指标**:
- `Accuracy`: 准确率 (当 `core_metrics=True`)
- 错误分析指标 (当 `error_analysis=True`):
  - `Same response to all questions`: 所有问题相同回答
  - `Language inconsistency`: 语言不一致
  - `Limitation of instruction-following`: 指令遵从问题
  - `Repetition`: 重复内容
  - `Empty response`: 空回复

---

## 4. 数据处理模块

### 4.1 task_hiearchy.py - 任务层级映射

**文件位置**: [task_hiearchy.py](file:///d:/project/opencompass/opencompass/datasets/calm/data_processing/task_hiearchy.py)

定义了所有任务到其数据存储路径的映射关系，支持以下四大类任务：

#### Association (关联层级)
| 任务代码 | 任务名称 | 数据路径 |
|----------|----------|----------|
| CORR-B_correlation | 相关性判断 | association/correlation/ |
| EAE-B_exp-away | 解释消除效应 | association/explaining_away_effect/ |

#### Causal Discovery (因果发现层级)
| 任务代码 | 任务名称 | 数据路径 |
|----------|----------|----------|
| AR-B_CaLM-AR | 抽象推理 | causal_discovery/abstract_reasoning/ |
| CA-B_FA/FP | 因果归因 | causal_discovery/causal_attribution/ |
| ECI-B_CTB/ESC/MAVEN-ERE | 事件因果识别 | causal_discovery/event_causality_identification/ |
| PCD-B/C_COPA/E-CARE | 成对因果发现 | causal_discovery/pairwise_causal_discovery/ |

#### Counterfactual (反事实层级)
| 任务代码 | 任务名称 | 数据路径 |
|----------|----------|----------|
| AC-B_causal_judgement | 实际因果判断 | counterfactual/actual_causality/ |
| CEG-O_E-CARE | 因果解释生成 | counterfactual/causal_explanation_generation/ |
| CR-B_det-counterfactual | 确定性反事实 | counterfactual/counterfactual_reasoning/ |
| CR-C_CRASS | CRASS 反事实推理 | counterfactual/counterfactual_reasoning/ |
| ETT-B/P | 处理效应 | counterfactual/effect_of_the_treatment_on_the_treated/ |
| NDE-B/P | 自然直接效应 | counterfactual/natural_direct_effect/ |
| NIE-B/P | 自然间接效应 | counterfactual/natural_indirect_effect/ |
| PN-P | 必要性概率 | counterfactual/probability_of_necessity/ |
| PS-P | 充分性概率 | counterfactual/probability_of_sufficiency/ |

#### Intervention (干预层级)
| 任务代码 | 任务名称 | 数据路径 |
|----------|----------|----------|
| ATE-B/P | 平均处理效应 | intervention/average_treatment_effect/ |
| BAS-B/C | 后门调整集 | intervention/backdoor_adjustment_set/ |
| CEI-B | 因果效应识别 | intervention/causal_effect_identification/ |
| CB-B_collider-bias | 碰撞偏差 | intervention/collider_bias/ |
| CDE-B/P | 控制直接效应 | intervention/controlled_direct_effect/ |
| FAS-C_FAS | 前门调整集 | intervention/frontdoor_adjustment_set/ |
| IV-C_CaLM-IV | 工具变量 | intervention/instrumental_variable/ |

### 4.2 generate_questions.py - 问题生成器

**文件位置**: [generate_questions.py](file:///d:/project/opencompass/opencompass/datasets/calm/data_processing/generate_questions.py)

#### 核心函数

**`get_get_prompt_func(task)`**
```python
def get_get_prompt_func(task):
    """根据任务名称获取对应的 prompt 生成函数
    
    Args:
        task: 任务名称 (如 'ATE-B_ATE-natural_EN')
        
    Returns:
        function: 该任务的 prompt 生成函数
        
    Raises:
        NotImplementedError: 未找到对应任务的 prompt 函数
    """
```

**`generate_question_list(dataset_path, prompt_style)`**
```python
def generate_question_list(dataset_path, prompt_style):
    """从数据集生成问题列表
    
    Args:
        dataset_path: 数据集 JSON 文件路径
        prompt_style: prompt 风格
        
    Returns:
        list: 问题字典列表，每个字典包含 'question' 和 'gt_item'
        
    Raises:
        AssertionError: 任务语言与 prompt 风格语言不匹配
    """
```

**语言匹配规则**:
- 任务名称以 `_CN` 结尾时，`prompt_style` 必须以 `-CN` 结尾
- 任务名称以 `_EN` 结尾时，`prompt_style` 不能以 `-CN` 结尾

### 4.3 prompt 目录 - Prompt 模板

每个任务都有独立的 prompt 模板文件，包含多种 prompt 风格的模板定义。

**典型结构** (以 [ATE.py](file:///d:/project/opencompass/opencompass/datasets/calm/data_processing/prompt/ATE.py) 为例):

```python
base_prompt_dict = {
    'basic': """Input Info: %s
%s
Instruction: %s
Question: %s
Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:""",
    
    'basic-CN': """输入信息：%s
%s
指令：%s
问题：%s
请根据上述信息，给出计算结果（答案保留四位小数），并给出最终答案"是"或"否"。请以JSON格式返回最终结果，例如，{"ANSWER":"是","PROB":"0.1234"}：""",
    
    # ... 其他 prompt 风格
}

def get_prompt(task_name, prompt_style, item, prompt_style_str=''):
    """生成特定任务和风格的 prompt
    
    Args:
        task_name: 任务名称
        prompt_style: prompt 风格
        item: 数据项，包含 given_info, Background, Instruction, Question 等字段
        prompt_style_str: 可选的前缀字符串
        
    Returns:
        str: 完整的 prompt 字符串
    """
```

---

## 5. 评估体系

### 5.1 accuracy 目录 - 准确率计算

**文件位置**: `evaluation/accuracy/`

#### choice.py - 选择题准确率
```python
def compute_acc(gt_list, pred_list):
    """计算选择题准确率
    
    通过精确匹配比较预测答案和正确答案
    """
    correct_num = sum(pred == gt for gt, pred in zip(gt_list, pred_list))
    acc = correct_num / len(gt_list)
    return acc
```

**适用任务**: 大多数二分类 (是/否) 和多选题任务

#### prob.py - 概率准确率
```python
def compute_acc(gt_list, pred_list):
    """计算概率答案准确率
    
    比较四位小数精度的概率值
    """
    correct_num = 0
    for pred, gold in zip(pred_list, gt_list):
        kept_pred = round(pred, 4) if (pred is not None) else pred
        kept_gold = round(gold, 4)
        if kept_pred == kept_gold:
            correct_num += 1
    acc = correct_num / len(gt_list)
    return acc
```

**适用任务**: ATE-P, NDE-P, NIE-P, CDE-P, ETT-P, PN-P, PS-P 等概率计算任务

#### open-ended.py - 开放式答案评估
```python
def compute_acc(gt_list, pred_list):
    """计算开放式答案的 Rouge-L 分数
    
    支持中文 (使用 jieba 分词) 和英文文本
    """
    rouge = Rouge()
    rouge_l = 0
    for pred, gold in zip(pred_list, gt_list):
        if is_chinese(pred):
            prediction = ' '.join(jieba.cut(pred))
            gold = ' '.join(jieba.cut(gold))
        scores = rouge.get_scores(prediction, gold)
        rouge_l += scores[0]['rouge-l']['r']
    avg_rougel = rouge_l / len(gt_list)
    return avg_rougel
```

**适用任务**: CEG-O_E-CARE (因果解释生成)

### 5.2 labeling 目录 - 答案标注

**文件位置**: `evaluation/labeling/`

#### common_answers.py - 通用答案模式

定义了多种语言和格式的答案匹配模式：

```python
# 肯定答案模式 (中英文)
common_true_list = [
    'answer (yes or no?): yes', 'answer is yes', '答案是:是', '答案：是', ...
]

# 否定答案模式 (中英文)
common_false_list = [
    'answer (yes or no?): no', 'answer is no', '答案是:否', '答案：否', ...
]

# 选项答案模式
common_option_1_list = ['option 1', '选项一', ...]
common_option_2_list = ['option 2', '选项二', ...]
common_option_3_list = ['option 3', '选项三', ...]
common_option_4_list = ['option 4', '选项四', ...]
```

#### 任务特定标注模块

每个标注模块实现两个核心函数：

```python
def get_gt_label(item):
    """从数据项中提取 ground truth 标签"""
    
def get_pred_label(model_response, item, prompt_style, type):
    """从模型响应中提取预测标签"""
```

### 5.3 error 目录 - 错误分析

**文件位置**: `evaluation/error/basic_adversarial/`

#### 错误检测函数

```python
def check_standalization(model_response, prompt_style, type):
    """检查回答是否符合标准格式"""
    
def check_empty(model_response):
    """检查是否为空回复"""
    
def check_repetition(model_response):
    """检查是否存在重复内容"""
    
def contains_chinese(text):
    """检测是否包含中文字符"""
    
def contains_english(text):
    """检测是否包含英文字符"""
    
def check_abnormality(preds):
    """检查是否所有回答都相同 (全 Yes 或全 No)"""
```

### 5.4 core_metrics.py - 核心指标计算

**文件位置**: [core_metrics.py](file:///d:/project/opencompass/opencompass/datasets/calm/evaluation/core_metrics.py)

```python
def initialize_core_metric_evaluation_components(task):
    """初始化评估组件
    
    根据任务动态加载对应的标注模块和准确率计算模块
    
    Returns:
        tuple: (get_gt_label, get_pred_label, compute_acc) 函数三元组
    """

def compute_core_metrics(items, task, prompt_style, gt_items):
    """计算核心指标
    
    Args:
        items: 模型预测列表
        task: 任务名称
        prompt_style: prompt 风格
        gt_items: ground truth 列表
        
    Returns:
        tuple: (metrics_dict, pred_list)
    """
```

**任务到评估模块映射**:

| 评估类型 | 适用任务 |
|----------|----------|
| choice | CORR-B, EAE-B, AR-B, CA-B, ECI-B, PCD-B/C, AC-B, CR-B/C, ETT-B, NDE-B, NIE-B, ATE-B, BAS-B/C, CEI-B, CB-B, CDE-B, FAS-C, IV-C |
| prob | ETT-P, NDE-P, NIE-P, PN-P, PS-P, ATE-P, CDE-P |
| open-ended | CEG-O_E-CARE |

### 5.5 errors.py - 错误识别

**文件位置**: [errors.py](file:///d:/project/opencompass/opencompass/datasets/calm/evaluation/errors.py)

```python
def identify_model_errors(items, task, prompt_style, gt_items):
    """识别模型响应中的错误
    
    Returns:
        dict: {
            'Same response to all questions': 0/1,
            'Language inconsistency': float (0-1),
            'Limitation of instruction-following': float (0-1),
            'Repetition': float (0-1),
            'Empty response': float (0-1)
        }
    """
```

**错误类型说明**:

| 错误类型 | 说明 | 检测方法 |
|----------|------|----------|
| Same response to all questions | 所有问题给出相同答案 | 检查预测结果是否全为 Yes 或全为 No |
| Language inconsistency | 语言不一致 | 中文任务检测英文、英文任务检测中文 |
| Limitation of instruction-following | 指令遵从问题 | 检查回答是否以期望格式开头 |
| Repetition | 重复内容 | 检测是否重复问题或指令内容 |
| Empty response | 空回复 | 检查回复是否为空字符串 |

---

## 6. 工具函数

### 6.1 load_items.py - 数据加载

**文件位置**: [load_items.py](file:///d:/project/opencompass/opencompass/datasets/calm/utils/load_items.py)

```python
def load_query_instances(path):
    """从 JSON 文件加载查询实例
    
    Args:
        path: JSON 文件路径 (str 或 Path 对象)
        
    Returns:
        list: JSON 行格式的数据实例列表
        
    Note:
        文件格式为 JSON Lines (每行一个 JSON 对象)
    """
    if isinstance(path, str):
        path = Path(path)
    with path.open('r', encoding='utf-8') as f:
        item_list = [json.loads(line) for line in f.readlines()]
    return item_list
```

---

## 7. 提示工程 (Prompt Engineering)

CaLM 支持多种 prompt 风格，每种风格都有中文 (-CN) 和英文版本：

### 7.1 基础 Prompt (Basic)

**风格**: `basic` / `basic-CN`

最简洁的 prompt 格式，直接呈现问题信息和指令：

```
# 英文版
Input Info: {given_info}
{data_info}
Instruction: {instruction}
Question: {question}
Provide the calculation result...

# 中文版
输入信息：{given_info}
{data_info}
指令：{instruction}
问题：{question}
请根据上述信息...
```

**应用场景**: 基线测试，评估模型的基本因果推理能力

### 7.2 对抗性 Prompt (Adversarial)

**风格**: `adversarial-ignore` / `adversarial-ignore-CN` / `adversarial-doubt` / `adversarial-doubt-CN`

与基础 prompt 结构相同，但测试数据中包含干扰信息或误导性内容。

**应用场景**: 评估模型抵抗干扰的鲁棒性

### 7.3 上下文学习 (In-Context Learning)

**风格**: `zero-shot-IcL` / `one-shot-IcL` / `three-shot-IcL` (及 -CN 版本)

在问题前添加任务说明和示例：

```
# Zero-shot IcL
Answer questions about the Average Treatment Effect (ATE). Computing the Average 
Treatment Effect involves comparing the outcomes of two groups...

# One-shot IcL
{任务说明}
{示例问题和答案}

Input Info: {实际问题}
...

# Three-shot IcL
{任务说明}
{示例1}
{示例2}
{示例3}

Input Info: {实际问题}
...
```

**应用场景**: 评估模型的少样本学习能力

### 7.4 思维链 (Chain-of-Thought)

**风格**: `zero-shot-CoT` / `zero-shot-CoT-CN` / `manual-CoT` / `manual-CoT-CN`

#### Zero-shot CoT
在问题末尾添加 "Let's think step by step." / "请逐步思考。"

#### Manual CoT
提供详细的推理示例：

```
Here are three examples for math problems about average treatment effect(ATE) task with chain of thought.

Input Info: ...
Question: ...
Provide the calculation result...: With B represents nvcm and C represents sxxy, 
we find P(C=1|B=1)=0.8173; P(C=1|B=0)=0.7873; Considering there is a path B->C 
from B to C, and in this situation empty set is a valid backdoor adjustment set, 
we calculate ATE=P(C=1|do(B=1))-P(C=1|do(B=0))=0.8173-0.7873=0.0300>0. 
The answer is: {"ANSWER": "Yes", "PROB": "0.0300"}.
```

**应用场景**: 评估模型的推理能力和中间步骤展示

### 7.5 显式功能 (Explicit Function)

**风格**: `explicit-function` / `explicit-function-CN`

明确告知模型其角色：

```
You are a helpful assistant for math probability.
Input Info: ...

你是一个用于计算数学概率的得力助手。
输入信息：...
```

**应用场景**: 通过角色设定引导模型行为

---

## 8. 评估指标详解

### 8.1 任务类型与评估方式对照

| 任务类型后缀 | 答案格式 | 评估方式 | 示例任务 |
|--------------|----------|----------|----------|
| -B (Binary) | 是/否 或 选项 | choice (精确匹配) | ATE-B, NDE-B, CORR-B |
| -P (Probability) | JSON {ANSWER, PROB} | prob (四位小数匹配) | ATE-P, NDE-P, PN-P |
| -C (Complex) | 选项或集合 | choice | BAS-C, CR-C, PCD-C |
| -O (Open-ended) | 自由文本 | open-ended (Rouge-L) | CEG-O |

### 8.2 答案格式要求

#### 选择题 (Choice)
- 二分类: `Yes` / `No` 或 `是` / `否`
- 多选: `Option 1` / `Option 2` / ... 或 `选项一` / `选项二` / ...

#### 概率题 (Probability)
```json
{"ANSWER": "Yes", "PROB": "0.1234"}
{"ANSWER": "是", "PROB": "0.1234"}
```

#### 开放式 (Open-ended)
自由文本，使用 Rouge-L 评估与参考答案的相似度

---

## 9. 使用示例

### 9.1 配置文件示例

```python
from opencompass.datasets.calm import CaLMDataset, CaLMEvaluator

# 数据集配置
calm_datasets = [
    dict(
        type=CaLMDataset,
        abbr='calm_ate_en',
        path='path/to/ATE-B_ATE-natural_EN.json',
        prompt_style='basic',
        reader_cfg=dict(
            input_columns=['question'],
            output_column='gt_item'
        ),
        infer_cfg=dict(
            prompt_template=dict(
                type=PromptTemplate,
                template='{question}'
            ),
            retriever=dict(type=ZeroRetriever),
            inferencer=dict(type=GenInferencer)
        ),
        eval_cfg=dict(
            evaluator=dict(
                type=CaLMEvaluator,
                core_metrics=True,
                error_analysis=True,
                prompt_style='basic',
                task='ATE-B_ATE-natural_EN'
            ),
            pred_role='BOT'
        )
    )
]
```

### 9.2 多任务配置

```python
# 定义任务列表
tasks = [
    ('ATE-B_ATE-natural', 'basic'),
    ('NDE-P_NDE-basic', 'zero-shot-CoT'),
    ('CR-C_CRASS', 'one-shot-IcL'),
]

calm_datasets = []
for task, style in tasks:
    for lang in ['EN', 'CN']:
        task_full = f'{task}_{lang}'
        style_full = f'{style}-CN' if lang == 'CN' else style
        calm_datasets.append(
            dict(
                type=CaLMDataset,
                abbr=f'calm_{task_full}_{style_full}',
                path=f'data/calm/{task_full}.json',
                prompt_style=style_full,
                # ... 其他配置
                eval_cfg=dict(
                    evaluator=dict(
                        type=CaLMEvaluator,
                        core_metrics=True,
                        error_analysis=True,
                        prompt_style=style_full,
                        task=task_full
                    )
                )
            )
        )
```

### 9.3 评估结果示例

```json
{
    "Accuracy": 0.7523,
    "Same response to all questions": 0,
    "Language inconsistency": 0.0234,
    "Limitation of instruction-following": 0.0891,
    "Repetition": 0.0012,
    "Empty response": 0.0000
}
```

---

## 10. 任务命名规范

CaLM 任务采用统一的命名格式：`{类型}-{难度}_{数据源}_{语言}`

| 字段 | 说明 | 示例值 |
|------|------|--------|
| 类型 | 任务缩写 | ATE, NDE, NIE, CR, PCD 等 |
| 难度 | B=Binary, P=Probability, C=Complex, O=Open | B, P, C, O |
| 数据源 | 原始数据来源 | COPA, E-CARE, CRASS, CaLM-AR 等 |
| 语言 | 语言版本 | EN, CN |

**示例**:
- `ATE-B_ATE-natural_EN`: 英文版平均处理效应二分类任务
- `CR-C_CRASS_CN`: 中文版 CRASS 复杂反事实推理任务
- `PCD-B_COPA_EN`: 英文版 COPA 成对因果发现二分类任务

---

## 11. 注意事项

1. **语言一致性**: 确保任务语言 (_EN/_CN) 与 prompt 风格语言 (无后缀/-CN) 匹配
2. **CEG-O 任务限制**: `CEG-O_E-CARE` 任务不支持错误分析功能
3. **explicit-function 限制**: `explicit-function` 和 `explicit-function-CN` 风格不支持错误分析
4. **数据格式**: 数据文件采用 JSON Lines 格式 (每行一个 JSON 对象)
5. **概率精度**: 概率类任务答案需保留四位小数

---

## 12. 参考资料

- CaLM 论文: [Causal Language Models Benchmark](https://arxiv.org/abs/xxxx.xxxxx)
- OpenCompass 文档: [https://opencompass.org.cn](https://opencompass.org.cn)
- 因果推理基础: Pearl, J. (2009). Causality: Models, Reasoning, and Inference
