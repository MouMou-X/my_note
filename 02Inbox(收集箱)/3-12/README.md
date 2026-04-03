# opencompass_plus

OpenCompass 评测框架扩展包，提供工程化的数据集扩展机制、可复用的评估逻辑和便捷的后处理工具。

## 特性

- **数据集扩展** — 基于 `BaseDataset` 的增强基类，内置 JSONL/JSON/CSV 加载工具，支持字段映射和多数据源切换
- **增强型评估器** — 模板方法模式，子类只需实现 `_compute_metrics()` 即可创建新评估器，自动生成 per-sample 详情
- **通用后处理函数** — 去答案前缀、提取选项字母、空白规范化，均注册到 OpenCompass `TEXT_POSTPROCESSORS`
- **结果增强器** — `SimpleEnhancer` 包装任意评估器，自动添加详情信息
- **框架兼容** — 全部组件通过 `LOAD_DATASET`、`ICL_EVALUATORS`、`TEXT_POSTPROCESSORS` 注册器集成，OpenCompass 可无缝发现

## 包结构

```
opencompass_plus/
├── __init__.py                  # 包入口，统一导出所有公开接口
├── Enhancer.py                  # 评估结果增强器（SimpleEnhancer）
├── setup.py                     # 安装配置
├── test.py                      # 集成测试
├── custom_datasets/             # 数据集扩展模块
│   ├── __init__.py
│   ├── base.py                  # PlusBaseDataset 基类 + 加载工具
│   └── example_mcq.py           # 示例：多选题数据集
├── evaluators/                  # 评估器扩展模块
│   ├── __init__.py
│   ├── base.py                  # PlusBaseEvaluator 基类（模板方法）
│   ├── acc_detail.py            # AccDetailEvaluator — 带详情准确率
│   └── exact_match.py           # ExactMatchEvaluator — 精确匹配
├── postprocessors/              # 后处理函数模块
│   ├── __init__.py
│   └── common.py                # strip_answer_prefix / extract_option / normalize_whitespace
└── configs/                     # 配置模板
    └── example_mcq_gen.py       # 示例评测配置
```

## 安装

确保已安装 [OpenCompass](https://github.com/open-compass/opencompass) 主框架，然后以开发模式安装：

```bash
cd opencompass_plus
pip install -e .
```

## 快速开始

### 导入公开接口

```python
from opencompass_plus import (
    # 数据集
    PlusBaseDataset,
    ExampleMCQDataset,
    # 评估器
    PlusBaseEvaluator,
    AccDetailEvaluator,
    ExactMatchEvaluator,
    # 后处理
    strip_answer_prefix,
    extract_option,
    normalize_whitespace,
    # 增强器
    SimpleEnhancer,
)
```

### 使用评估器

```python
from opencompass_plus import AccDetailEvaluator

evaluator = AccDetailEvaluator()
result = evaluator.score(
    predictions=['A', 'B', 'A', 'C', 'D'],
    references=['A', 'B', 'C', 'C', 'D'],
)
print(result['accuracy'])   # 80.0
print(result['details'])    # per-sample 详情列表
```

```python
from opencompass_plus import ExactMatchEvaluator

evaluator = ExactMatchEvaluator(ignore_case=True, normalize_whitespace=True)
result = evaluator.score(
    predictions=['Hello  World', 'foo bar'],
    references=['hello world', 'Foo Bar'],
)
print(result['exact_match'])  # 100.0
```

### 使用后处理函数

```python
from opencompass_plus import strip_answer_prefix, extract_option, normalize_whitespace

strip_answer_prefix('答案是B')           # 'B'
strip_answer_prefix('The answer is C')   # 'C'
extract_option('我认为答案是B', options='ABCD')  # 'B'
normalize_whitespace('  hello   world  ')        # 'hello world'
```

### 在 OpenCompass 配置中使用

```python
# 在你的评测配置文件中引入示例配置
from opencompass_plus.configs.example_mcq_gen import example_mcq_datasets

datasets = [*example_mcq_datasets]
```

或手动组合配置：

```python
from opencompass_plus.custom_datasets import ExampleMCQDataset
from opencompass_plus.evaluators import AccDetailEvaluator
from opencompass_plus.postprocessors import extract_option

eval_cfg = dict(
    evaluator=dict(type=AccDetailEvaluator),
    pred_postprocessor=dict(type=extract_option, options='ABCD'),
)
```

## 扩展指南

### 新增数据集

1. 在 `custom_datasets/` 下创建新文件（参照 `example_mcq.py`）
2. 继承 `PlusBaseDataset`，实现 `load(**kwargs) -> datasets.Dataset` 静态方法
3. 使用 `@LOAD_DATASET.register_module()` 注册
4. 在 `custom_datasets/__init__.py` 中导出

```python
from datasets import Dataset
from opencompass.registry import LOAD_DATASET
from .base import PlusBaseDataset

@LOAD_DATASET.register_module()
class MyDataset(PlusBaseDataset):

    @staticmethod
    def load(path: str, **kwargs) -> Dataset:
        return PlusBaseDataset.load_jsonl(path)
```

可用的辅助加载方法：

| 方法 | 说明 |
|------|------|
| `PlusBaseDataset.load_jsonl(path, field_mapping=None)` | 从 JSONL 文件加载 |
| `PlusBaseDataset.load_json(path, data_key=None, field_mapping=None)` | 从 JSON 文件加载 |
| `PlusBaseDataset.load_csv(path, field_mapping=None)` | 从 CSV 文件加载 |

`field_mapping` 参数支持字段重命名，如 `{'stem': 'question', 'answerKey': 'answer'}`。

### 新增评估器

1. 在 `evaluators/` 下创建新文件
2. 继承 `PlusBaseEvaluator`，实现 `_compute_metrics()` 方法
3. 可选重写 `_is_correct()` 自定义单条样本比较逻辑
4. 使用 `@ICL_EVALUATORS.register_module()` 注册
5. 在 `evaluators/__init__.py` 中导出

```python
from opencompass.registry import ICL_EVALUATORS
from .base import PlusBaseEvaluator

@ICL_EVALUATORS.register_module()
class MyEvaluator(PlusBaseEvaluator):

    def _compute_metrics(self, predictions, references):
        correct = sum(self._is_correct(p, r) for p, r in zip(predictions, references))
        total = len(predictions)
        return {'accuracy': correct / total * 100 if total else 0.0}

    def _is_correct(self, prediction, reference):
        return str(prediction).strip() == str(reference).strip()
```

`score()` 方法会自动完成：长度校验 → 调用 `_compute_metrics()` → 生成 per-sample details → 返回结果字典。

### 新增后处理函数

1. 在 `postprocessors/common.py` 中添加函数（或创建新文件）
2. 函数签名遵循 `(text: str, **kwargs) -> str`
3. 使用 `@TEXT_POSTPROCESSORS.register_module()` 注册

```python
from opencompass.registry import TEXT_POSTPROCESSORS

@TEXT_POSTPROCESSORS.register_module()
def my_postprocessor(text: str) -> str:
    return text.strip().upper()
```

## 运行测试

```bash
python test.py
```

测试覆盖：导入检查、评估器计算验证、后处理函数验证、SimpleEnhancer 兼容性验证。

## 组件与 OpenCompass 注册器对应关系

| 组件 | 基类 | 注册器 | 核心方法 |
|------|------|--------|----------|
| 数据集 | `PlusBaseDataset` ← `BaseDataset` | `LOAD_DATASET` | `load(**kwargs) -> Dataset` |
| 评估器 | `PlusBaseEvaluator` ← `BaseEvaluator` | `ICL_EVALUATORS` | `score(predictions, references) -> dict` |
| 后处理 | 独立函数 | `TEXT_POSTPROCESSORS` | `(text: str) -> str` |

## 依赖

- Python >= 3.8
- [opencompass](https://github.com/open-compass/opencompass)（及其依赖：mmengine、datasets 等）
