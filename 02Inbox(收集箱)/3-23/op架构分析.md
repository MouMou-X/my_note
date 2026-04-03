以下是基于源代码分析的系统性架构概述：

---

## OpenCompass 项目完整架构与执行流程

### 一、整体架构概览

OpenCompass 采用**模块化设计**和**数据流驱动**架构，核心执行流程为：

```
命令行输入 → 配置构建 → 任务分割 → 推理执行 → 评估计算 → 结果汇总
```

所有模块通过 **MMEngine 注册表机制**（[registry.py](file:///d:/project/opencompass_inner/opencompass/registry.py)）实现动态发现和加载，包括
`MODELS`、
`PARTITIONERS`、
`RUNNERS`、
`TASKS`、
`LOAD_DATASET`、
`ICL_INFERENCERS`、
`ICL_RETRIEVERS`、
`ICL_EVALUATORS`、
`METRICS` 
等注册表。

---

### 二、核心模块划分

| 模块                | 路径                                                                                                                                                                            | 职责                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **[[cli入口]]**     | [cli/main.py](file:///d:/project/opencompass_inner/opencompass/cli/main.py)                                                                                                   | 命令行解析、配置构建、流程调度                                              |
| **[[配置工具]]**      | [utils/run.py](file:///d:/project/opencompass_inner/opencompass/utils/run.py)                                                                                                 | `get_config_from_arg()`、`fill_infer_cfg()`、`fill_eval_cfg()` |
| **Partitioner**   | [partitioners/](file:///d:/project/opencompass_inner/opencompass/partitioners/)                                                                                               | 将 (Model, Dataset) 对分割为可调度任务                                 |
| **[[Runner]]**    | [runners/](file:///d:/project/opencompass_inner/opencompass/runners/)                                                                                                         | 任务调度与并行执行（Local/Slurm/DLC）                                   |
| **Task**          | [tasks/](file:///d:/project/opencompass_inner/opencompass/tasks/)                                                                                                             | 推理任务 `OpenICLInferTask` 和评估任务 `OpenICLEvalTask`              |
| **[[Model]]**     | [models/](file:///d:/project/opencompass_inner/opencompass/models/)                                                                                                           | 模型抽象层，52+ 种实现（HF/VLLM/API等）                                  |
| **[[ICL框架]]**     | [openicl/](file:///d:/project/opencompass_inner/opencompass/openicl/)                                                                                                         | Inferencer + Retriever + PromptTemplate                      |
| **Dataset**       | [datasets/](file:///d:/project/opencompass_inner/opencompass/datasets/)                                                                                                       | 70+ 数据集定义与加载                                                 |
| **[[Evaluator]]** | [openicl/icl_evaluator/](file:///d:/project/opencompass_inner/opencompass/openicl/icl_evaluator/) + [evaluator/](file:///d:/project/opencompass_inner/opencompass/evaluator/) | 指标计算（精确匹配、LLM评判等）                                            |
| **Summarizer**    | [summarizers/](file:///d:/project/opencompass_inner/opencompass/summarizers/)                                                                                                 | 结果汇总与报告生成                                                    |

---

### 三、配置(Config)构建过程

#### 3.1 三种配置来源（优先级从高到低）

1. **指定 config 文件** → `Config.fromfile(args.config)` 直接加载
2. **--models + --datasets 参数** → 从 `opencompass/configs/` 目录下查找并组合
3. **HuggingFace 快速参数**（`--hf-path` 等）→ 命令行参数动态构建模型配置

核心函数是 [utils/run.py](file:///d:/project/opencompass_inner/opencompass/utils/run.py) 中的 `get_config_from_arg(args)`。

#### 3.2 `read_base()` 机制

配置文件通过 MMEngine 的 `read_base()` 实现继承和组合：

```python
from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.demo.demo_gsm8k_base_gen import gsm8k_datasets
    from opencompass.configs.models.hf_internlm.hf_internlm2_1_8b import models

datasets = gsm8k_datasets + math_datasets
models = models
```

这本质上是 Python 的 import 机制——每个配置文件都是一个独立的 Python 模块，通过 `read_base()` 上下文管理器将其中定义的变量引入当前作用域。

#### 3.3 models 和 datasets 字段

**models** 是模型配置字典列表，每项包含 `type`（注册类名）、`path`（模型路径）、`max_out_len`、`batch_size` 等参数。

**datasets** 是数据集配置字典列表，每项包含三个关键子配置：
- `reader_cfg`：定义 `input_column`、`output_column`、`split`、`test_range`
- `infer_cfg`：定义 `prompt_template`、`retriever`、`inferencer`（推理方式）
- `eval_cfg`：定义 `evaluator`（评估方式）

#### 3.4 自动补全

配置加载后，系统通过 `fill_infer_cfg(cfg, args)` 和 `fill_eval_cfg(cfg, args)` 自动补充用户未显式指定的 `infer` 和 `eval` 段（Partitioner + Runner 配置），确保最终配置完整可执行。

---

### 四、完整执行流程（按阶段）

#### 阶段 1：命令行解析 → 配置构建

```
python run.py config.py --mode all
       ↓
parse_args() → args 对象
       ↓
get_config_from_arg(args) → cfg 对象
       ↓
fill_infer_cfg(cfg) + fill_eval_cfg(cfg) → 完整配置
       ↓
cfg.dump(output_path) → 配置持久化到 work_dir/configs/
```

#### 阶段 2：推理（Infer）

**输入**：完整配置中的 `cfg.models` + `cfg.datasets` + `cfg.infer`

```
Partitioner(cfg.infer.partitioner)
    → 将 M个模型 × N个数据集 分割为若干任务组
       ↓
Runner(cfg.infer.runner)
    → 调度任务（LocalRunner 多进程/GPU 分配；SlurmRunner 集群提交）
       ↓
OpenICLInferTask.run()  [对每个任务]
    ├─ build_model_from_cfg(model_cfg)     → 实例化模型
    ├─ build_dataset_from_cfg(dataset_cfg) → 加载数据集
    ├─ Retriever.retrieve()                → 检索 ICL 示例
    ├─ PromptTemplate.format()             → 组装 prompt
    └─ Model.generate() / get_ppl()        → 推理
       ↓
输出: predictions/{model}_{dataset}.json
```

**关键数据流**：模型配置中的 `max_out_len`、`batch_size` 等参数会被分离出来，传递给 Inferencer 而非模型构造函数。

#### 阶段 3：评估（Eval）

**输入**：推理阶段的 predictions JSON + 原始数据集 + `cfg.eval`

```
Partitioner(cfg.eval.partitioner)
    → NaivePartitioner 生成评估任务
       ↓
Runner(cfg.eval.runner)
    → 调度评估任务
       ↓
OpenICLEvalTask.run()  [对每个任务]
    ├─ _load_predictions()              → 加载推理结果
    ├─ _process_predictions()           → 后处理（角色提取、格式化）
    │   ├─ extract_role_pred()          → 多角色输出提取
    │   ├─ pred_postprocessor (模型级)  → 模型输出清洗
    │   └─ eval_cfg.pred_postprocessor  → 数据集级后处理
    ├─ Evaluator.score(pred, ref)       → 计算指标
    └─ 保存结果
       ↓
输出: results/{model}_{dataset}.json
```

#### 阶段 4：汇总（Summary）

**输入**：所有 results JSON 文件

```
DefaultSummarizer.summarize()
    ├─ _pick_up_results()      → 收集所有评估结果
    ├─ _parse_results()        → 解析指标
    ├─ _calc_summary_stats()   → 汇总统计
    └─ _visualize()            → 生成报告
       ↓
输出: summary/{summary.txt, summary.json, summary.html}
```

---

### 五、你可能忽略的重要步骤

除了你提到的 config → task → infer → eval → summary 流程外，以下是**容易被忽略的关键机制**：

1. **Partitioner 分割层**：这是 task 构建和 runner 执行之间的关键中间层，负责将 M×N 的笛卡尔积合理分组（`NumWorkerPartitioner` 按 worker 数均分，`SizePartitioner` 按数据集大小动态分割）

2. **Runner 调度层**：`LocalRunner` 实现 GPU 级别的资源分配（读取 `CUDA_VISIBLE_DEVICES` 分配 GPU）；`SlurmRunner` 和 `DLCRunner` 支持集群/云端提交

3. **分布式推理**：当 `num_gpus > 1` 时，Task 会自动生成 `torch.distributed.run` 命令

4. **缓存与断点续评**：数据集大小缓存在 [.cache/dataset_size.json](file:///d:/project/opencompass_inner/.cache/dataset_size.json)；predictions 和 results 的持久化支持跳过已完成的评估

5. **结果站点同步**：支持 `--station-path` 将结果上传到远端存储，以及 `--read-from-station` 从远端读取

6. **Lark 机器人通知**：任务完成后可自动发送飞书通知

7. **模板解析器（LMTemplateParser）**：处理复杂的多轮对话模板和 `meta_template` 机制，支持角色转换和生成停止点

8. **数据集采样**：`reader_cfg.test_range` 支持 Python 切片语法（如 `'[0:100]'`），用于快速验证

---

### 六、完整数据流全景

```
┌─────────────────────────────────────────────────────────┐
│                    命令行 / 配置文件                       │
└────────────────────────┬────────────────────────────────┘
                         ↓
              ┌─────────────────────┐
              │  Config 构建与补全    │
              │  (models + datasets) │
              └──────────┬──────────┘
                         ↓
        ┌────────────────┴────────────────┐
        ↓                                 ↓
 ┌──────────────┐                 ┌──────────────┐
 │ Infer 阶段    │                 │ Eval 阶段    │ (依赖Infer输出)
 ├──────────────┤                 ├──────────────┤
 │ Partitioner  │                 │ Partitioner  │
 │     ↓        │                 │     ↓        │
 │ Runner       │                 │ Runner       │
 │     ↓        │                 │     ↓        │
 │ InferTask    │                 │ EvalTask     │
 │  ├ Model     │                 │  ├ 加载pred   │
 │  ├ Dataset   │                 │  ├ 后处理     │
 │  ├ Retriever │                 │  └ Evaluator  │
 │  ├ Template  │                 └──────┬───────┘
 │  └ Inferencer│                        ↓
 └──────┬───────┘               results/*.json
        ↓                                ↓
 predictions/*.json             ┌──────────────┐
                                │ Summarizer   │
                                │  → txt/json  │
                                │  → html报告   │
                                └──────────────┘
```

---

### 七、关键文件索引

| 功能 | 文件 |
|------|------|
| 程序入口 | [run.py](file:///d:/project/opencompass_inner/run.py) |
| CLI与主流程 | [cli/main.py](file:///d:/project/opencompass_inner/opencompass/cli/main.py) |
| 配置构建 | [utils/run.py](file:///d:/project/opencompass_inner/opencompass/utils/run.py) |
| 注册表 | [registry.py](file:///d:/project/opencompass_inner/opencompass/registry.py) |
| 模型基类 | [models/base.py](file:///d:/project/opencompass_inner/opencompass/models/base.py) |
| 推理任务 | [tasks/openicl_infer.py](file:///d:/project/opencompass_inner/opencompass/tasks/openicl_infer.py) |
| 评估任务 | [tasks/openicl_eval.py](file:///d:/project/opencompass_inner/opencompass/tasks/openicl_eval.py) |
| 结果汇总 | [summarizers/default.py](file:///d:/project/opencompass_inner/opencompass/summarizers/default.py) |
| 模型构建 | [utils/build.py](file:///d:/project/opencompass_inner/opencompass/utils/build.py) |

如果你需要针对某个特定模块（如 ICL 推理框架、模板解析器、或某种具体的 Partitioner 策略）做更深入的分析，请告诉我。