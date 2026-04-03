两个文件的完整源码已经附上，且前一轮研究已覆盖了相关上下文。以下是基于源码的详细讲解：

---

## 第一步：各函数功能概览

### 1. `run.py` — 程序总入口

```python
from opencompass.cli.main import main
if __name__ == '__main__':
    main()
```

极简入口，仅导入并调用 [main.py](file:///d:/project/opencompass_inner/opencompass/cli/main.py) 中的 `main()` 函数。所有真正的逻辑都在 `cli/main.py` 中。

### 2. `cli/main.py` 中的函数

| 函数 | 行号 | 功能 |
|------|------|------|
| **`parse_args()`** | L21-195 | 主参数解析器，定义所有命令行参数，并调用下面四个子解析函数，最终返回 `args` 对象 |
| **`parse_slurm_args()`** | L198-213 | 定义 SLURM 集群调度相关参数（`--partition`、`--quotatype`、`--qos`） |
| **`parse_dlc_args()`** | L216-221 | 定义阿里云 DLC 平台相关参数（`--aliyun-cfg`） |
| **`parse_hf_args()`** | L224-241 | 定义 HuggingFace 模型快速构建参数（`--hf-path`、`--hf-type`、`--batch-size` 等） |
| **`parse_custom_dataset_args()`** | L244-253 | 定义自定义数据集快速接入参数（`--custom-dataset-path`、`--custom-dataset-data-type` 等） |
| **`main()`** | L256-459 | **核心调度函数**，完成从参数解析 → 配置构建 → 推理 → 评估 → 汇总的完整流程 |

---

## 第二步：所有命令行参数详解

### 2.1 基础参数

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `config` | 位置参数, 可选 | 无 | 配置文件路径（如 `examples/eval_base_demo.py`）。是最主要的输入方式。`nargs='?'` 表示可以不提供，此时需要通过 `--models`+`--datasets` 或 `--hf-path` 来构建配置 |
| `--models` | 字符串列表 | None | 指定模型名称列表，系统会从 `configs/models/` 目录下查找对应配置。与 `config` 互补使用 |
| `--datasets` | 字符串列表 | None | 指定数据集名称列表，系统会从 `configs/datasets/` 目录下查找对应配置 |
| `--summarizer` | 字符串 | None | 指定汇总器名称，用于自定义结果汇总方式 |

### 2.2 运行控制参数

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `--slurm` | 布尔 | False | 强制使用 SLURM 集群调度。与 `--dlc` 互斥。启用时必须指定 `--partition` |
| `--dlc` | 布尔 | False | 强制使用阿里云 DLC 调度。与 `--slurm` 互斥。启用时需要 `~/.aliyun.cfg` |
| `-m`/`--mode` | 选择 | `'all'` | 运行模式：**`all`**=推理+评估+汇总；**`infer`**=仅推理；**`eval`**=仅评估（需 `--reuse`）；**`viz`**=仅汇总可视化（需 `--reuse`） |
| `-r`/`--reuse` | 字符串, 可选 | 无 | 复用已有结果。不带参数时默认 `'latest'`（使用最新结果）；也可指定时间戳如 `20230516_144254`。在 `eval`/`viz` 模式下**必须**指定 |
| `--debug` | 布尔 | False | 调试模式：单进程运行，输出不重定向到文件，方便调试 |
| `--dry-run` | 布尔 | False | 干跑模式：只验证配置和生成任务，不实际执行。会自动启用 `--debug` |
| `-a`/`--accelerator` | 选择 | None | 推理加速器：`vllm` 或 `lmdeploy`。指定后会用对应加速框架替代默认推理方式 |

### 2.3 工作目录与配置参数

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `-w`/`--work-dir` | 字符串 | None | 工作目录路径，所有输出（日志、预测、结果、汇总）都保存在此目录下。不指定时默认为 `outputs/default` |
| `--config-dir` | 字符串 | `'configs'` | 自定义配置搜索目录，用于覆盖默认的 `configs/` 目录来查找模型和数据集配置 |
| `--config-verbose` | 布尔 | False | 是否打印详细的配置信息，方便确认最终使用的完整配置 |

### 2.4 任务调度参数

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `--max-num-workers` | 整数 | 1 | 最大并行任务数。控制同时运行的推理/评估进程数量。会被配置文件中的同名字段覆盖 |
| `--max-workers-per-gpu` | 整数 | 1 | 单个 GPU 上最大并行任务数，仅 LocalRunner 生效 |
| `--retry` | 整数 | 2 | SLURM/DLC 模式下任务失败的重试次数。会被配置文件中的同名字段覆盖 |

### 2.5 结果输出参数

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `--dump-eval-details` | 布尔 | True | 是否保存评估详情（每个样本的正误、BPB 值等）。**默认开启**，会占用额外存储空间。传 `False` 关闭 |
| `--dump-res-length` | 布尔 | False | 是否记录模型响应的长度信息 |
| `--dump-extract-rate` | 布尔 | False | 是否计算并保存答案提取率（衡量从模型输出中成功提取答案的比例） |
| `--dump-only-message-path` | 字符串 | None | 仅导出 prompt 消息到指定路径，不实际执行推理（用于调试 prompt） |

### 2.6 结果持久化参数

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `-sp`/`--station-path` | 字符串 | None | 结果站路径，用于将评估结果上传到远端共享存储 |
| `--station-overwrite` | 布尔 | False | 是否覆盖结果站中已有的结果 |
| `--read-from-station` | 布尔 | False | 是否从结果站读取已有结果，避免重复评估 |

### 2.7 其他参数

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `-l`/`--lark` | 布尔 | False | 是否将运行状态通过飞书（Lark）机器人通知 |
| `--dataset-num-runs` | 整数 | 1 | 每个数据集执行几次（多次运行取平均，提高评估稳定性） |

### 2.8 SLURM 集群参数（`parse_slurm_args` 组）

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `-p`/`--partition` | 字符串 | None | SLURM 分区名称（如 `gpu`、`a100` 等），使用 `--slurm` 时必填 |
| `-q`/`--quotatype` | 字符串 | None | SLURM 配额类型（如 `spot`、`reserved`） |
| `--qos` | 字符串 | None | SLURM 服务质量等级 |

### 2.9 DLC 参数（`parse_dlc_args` 组）

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `--aliyun-cfg` | 字符串 | `'~/.aliyun.cfg'` | 阿里云配置文件路径，使用 `--dlc` 时需要该文件存在 |

### 2.10 HuggingFace 快速构建参数（`parse_hf_args` 组）

这组参数允许**不写配置文件**，直接通过命令行快速评估一个 HuggingFace 模型：

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `--hf-type` | 选择 | `'chat'` | 模型类型：`base`（基座模型）或 `chat`（对话模型），决定评估方式 |
| `--hf-path` | 字符串 | 无 | HuggingFace 模型路径（如 `"meta-llama/Llama-2-7b-chat-hf"`），是快速模式的核心参数 |
| `--model-kwargs` | 字典 | `{}` | 传给模型构造函数的额外参数（如 `device_map=auto trust_remote_code=True`） |
| `--tokenizer-path` | 字符串 | 无 | 分词器路径，不指定时默认与 `--hf-path` 相同 |
| `--tokenizer-kwargs` | 字典 | `{}` | 传给分词器构造函数的额外参数 |
| `--peft-path` | 字符串 | 无 | PEFT/LoRA 适配器路径 |
| `--peft-kwargs` | 字典 | `{}` | PEFT 加载的额外参数 |
| `--generation-kwargs` | 字典 | `{}` | 生成参数（如 `temperature=0.7 top_p=0.9`） |
| `--max-seq-len` | 整数 | 无 | 模型最大输入序列长度 |
| `--max-out-len` | 整数 | 256 | 模型最大输出 token 数 |
| `--min-out-len` | 整数 | 1 | 模型最小输出 token 数 |
| `--batch-size` | 整数 | 8 | 推理批处理大小 |
| `--num-gpus` | 整数 | None | **已废弃**，使用会直接报错 |
| `--hf-num-gpus` | 整数 | 1 | 使用的 GPU 数量 |
| `--pad-token-id` | 整数 | 无 | 填充 token 的 ID |
| `--stop-words` | 字符串列表 | `[]` | 停止词列表，遇到这些词时停止生成 |

### 2.11 自定义数据集参数（`parse_custom_dataset_args` 组）

| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `--custom-dataset-path` | 字符串 | 无 | 自定义数据集文件路径 |
| `--custom-dataset-meta-path` | 字符串 | 无 | 自定义数据集元信息文件路径 |
| `--custom-dataset-data-type` | 选择 | 无 | 数据类型：`mcq`（多选题）或 `qa`（问答题） |
| `--custom-dataset-infer-method` | 选择 | 无 | 推理方式：`gen`（生成式）或 `ppl`（困惑度式） |

---

## 第三步：`main()` 函数完整执行逻辑

`main()` 函数（L256-459）是整个框架的调度中枢。下面按执行顺序逐段讲解：

### 阶段 1：参数解析与初始化（L257-266）

```
args = parse_args()
    ↓
检查 --num-gpus 是否被使用（已废弃，直接报错）
    ↓
如果 --dry-run，自动开启 --debug
    ↓
初始化 logger（debug模式用DEBUG级别，否则INFO级别）
```

### 阶段 2：配置构建（L268-306）

这是最关键的初始化阶段：

```
get_config_from_arg(args) → cfg 对象
```

`get_config_from_arg()`（来自 [utils/run.py](file:///d:/project/opencompass_inner/opencompass/utils/run.py)）按优先级构建配置：
1. 如果指定了 `config` 文件 → `Config.fromfile(args.config)`
2. 如果指定了 `--models` + `--datasets` → 从 `configs/` 目录查找并组合
3. 如果指定了 `--hf-path` → 动态构建 HuggingFace 模型配置

接下来处理工作目录：

```python
# 设置 work_dir（默认 outputs/default）
cfg['work_dir'] = args.work_dir or 'outputs/default'

# 生成时间戳
cfg_time_str = datetime.now().strftime('%Y%m%d_%H%M%S')  # 如 20260323_170000

# 处理 --reuse 逻辑
if args.reuse:
    if args.reuse == 'latest':
        dir_time_str = sorted(os.listdir(work_dir))[-1]  # 取最新目录
    else:
        dir_time_str = args.reuse  # 使用指定的时间戳

# 最终 work_dir = outputs/default/20260323_170000
cfg['work_dir'] = osp.join(cfg.work_dir, dir_time_str)
```

**重要**：如果 `mode` 是 `eval` 或 `viz` 且没有指定 `--reuse` 或 `--read-from-station`，会直接报错（L287-291），因为这两种模式需要已有的推理结果。

配置持久化与重加载（L298-306）：

```python
# 创建 configs/ 子目录
os.makedirs(osp.join(cfg.work_dir, 'configs'), exist_ok=True)

# 将配置导出为 .py 文件（便于复现）
cfg.dump(output_config_path)

# 重新加载——关键步骤！
# 目的：避免配置中已初始化的Python类型对象无法序列化的问题
cfg = Config.fromfile(output_config_path, format_python_code=False)
```

### 阶段 3：外部数据源读取（L309-312）

```python
if args.read_from_station:
    existing_results_list = read_from_station(cfg, args)
    cfg['rs_exist_results'] = rs_exist_results  # 标记已有结果，后续跳过
```

从远端结果站拉取已有结果，避免重复评估。

### 阶段 4：通知与日志（L315-324）

```python
# 飞书通知
if args.lark and cfg.get('lark_bot_url'):
    LarkReporter(cfg['lark_bot_url']).post(f"{user}'s task has been launched!")

# 详细配置打印
if args.config_verbose:
    pretty_print_config(cfg)
```

### 阶段 5：推理阶段 — Infer（L327-369）

**触发条件**：`mode in ['all', 'infer']`

```
[1] 配置补全
    ↓
如果使用 --slurm/--dlc，或配置中没有 infer 段
    → fill_infer_cfg(cfg, args)  自动补充默认的 partitioner + runner 配置
    ↓
[2] 参数注入
    ↓
cfg.infer.runner.debug = True       (如果 --debug)
cfg.infer.runner.lark_bot_url = ... (如果 --lark)
cfg.infer.partitioner.out_dir = work_dir/predictions/
    ↓
[3] 任务分割
    ↓
partitioner = PARTITIONERS.build(cfg.infer.partitioner)
    → 通常是 NumWorkerPartitioner
tasks = partitioner(cfg)
    → 将 M个模型 × N个数据集 分割为若干任务组
    → 每个 task 包含一组 (model_cfg, [dataset_cfgs]) 对
    ↓
[4] 干跑检查
    ↓
if args.dry_run: return  # 到此为止，不实际执行
    ↓
[5] 额外配置注入
    ↓
- attack 配置（对抗评估）
- dump_res_length 标记
- dump_only_message_path 标记
    ↓
[6] 任务执行
    ↓
runner = RUNNERS.build(cfg.infer.runner)
    → LocalRunner / SlurmRunner / DLCRunner
runner(tasks)
    → 调度所有推理任务并行执行
    → 每个任务内部: 构建模型 → 加载数据 → ICL推理 → 保存 predictions JSON
```

**Partitioner 的工作机制**：

`NumWorkerPartitioner` 将笛卡尔积 `models × datasets` 按 `max_num_workers` 分组。例如 2个模型 × 5个数据集 = 10对，如果 `max_num_workers=4`，则分为约4个任务组，每组包含若干 (model, dataset) 对。

**Runner 的工作机制**：

`LocalRunner` 管理本地多进程执行，核心逻辑是 GPU 分配——读取 `CUDA_VISIBLE_DEVICES`，为每个任务分配所需数量的 GPU，然后以子进程方式启动 `OpenICLInferTask`。任务完成后收集退出码并汇总。

### 阶段 6：评估阶段 — Eval（L372-415）

**触发条件**：`mode in ['all', 'eval']`

```
[1] 配置补全（同推理阶段逻辑）
    ↓
fill_eval_cfg(cfg, args) → 补充评估的 partitioner + runner
    ↓
[2] 评估详情控制
    ↓
cfg.eval.runner.task.dump_details = True      (默认开启)
cfg.eval.runner.task.cal_extract_rate = True  (如果 --dump-extract-rate)
    ↓
[3] 任务分割
    ↓
partitioner = PARTITIONERS.build(cfg.eval.partitioner)
    → 通常是 NaivePartitioner（1个任务包含所有model-dataset对）
tasks = partitioner(cfg)
    ↓
[4] 任务执行
    ↓
runner = RUNNERS.build(cfg.eval.runner)

# 特殊处理：主观评估的 meta-review-judge
if tasks 是嵌套列表（List[List]）:
    for task_part in tasks:
        runner(task_part)     # 分阶段执行（先judge，再meta-review）
else:
    runner(tasks)             # 普通评估，一次性执行
```

**嵌套列表的含义**（L410-415）：主观评估（如 CompassArena）可能有多轮评判流程。第一轮由 LLM Judge 给出初步评分，第二轮由 Meta-Review Judge 综合多个评分给出最终结果。这种情况下 Partitioner 返回 `[[第一轮任务], [第二轮任务]]`，必须按顺序执行。

### 阶段 7：结果持久化（L418-419）

```python
if args.station_path or cfg.get('station_path'):
    save_to_station(cfg, args)  # 将结果上传到远端结果站
```

### 阶段 8：汇总与可视化 — Summarize（L422-454）

**触发条件**：`mode in ['all', 'eval', 'viz']`

这里有两条分支：

**分支 A：主观评估汇总**（L426-448）

当配置中 `summarizer.function` 存在时，表示这是主观评估：

```
[1] 按数据集前缀分组（如 compassarena_* 分为一组）
[2] 每组使用对应的 Summarizer 独立汇总
[3] 收集各组分数到 dataset_score_container
[4] 最后用主 Summarizer 做全局汇总
```

**分支 B：标准客观评估汇总**（L449-454）

```python
# 如果没指定 summarizer type，默认使用 DefaultSummarizer
summarizer_cfg['type'] = DefaultSummarizer
summarizer_cfg['config'] = cfg
summarizer = build_from_cfg(summarizer_cfg)
summarizer.summarize(time_str=cfg_time_str)
```

`DefaultSummarizer.summarize()` 会：
1. 扫描 `work_dir/results/` 下所有 JSON 结果文件
2. 解析各数据集的指标分数
3. 生成汇总表格（文本 + JSON + HTML）
4. 输出到 `work_dir/summary/` 目录

---

### 完整执行流程图

```
python run.py config.py --mode all
    │
    ▼
┌─────────────────────────────────────┐
│ parse_args() → args                 │
│ get_config_from_arg(args) → cfg     │
│ fill_infer_cfg / fill_eval_cfg      │
│ cfg.dump() → 配置持久化              │
│ Config.fromfile() → 配置重加载       │
└──────────────┬──────────────────────┘
               │
    ┌──────────▼──────────┐
    │ mode == 'infer'/'all'│
    │                      │
    │  Partitioner.build() │
    │  → 分割为任务列表     │
    │  Runner.build()      │
    │  → 并行执行推理       │
    │  → predictions/*.json│
    └──────────┬───────────┘
               │
    ┌──────────▼──────────┐
    │ mode == 'eval'/'all' │
    │                      │
    │  Partitioner.build() │
    │  → 分割为评估任务     │
    │  Runner.build()      │
    │  → 执行评估           │
    │  → results/*.json    │
    └──────────┬───────────┘
               │
    ┌──────────▼──────────────┐
    │ save_to_station (可选)   │
    └──────────┬──────────────┘
               │
    ┌──────────▼──────────────────┐
    │ mode == 'eval'/'viz'/'all'  │
    │                              │
    │  Summarizer.build()          │
    │  → 收集 + 解析 + 汇总        │
    │  → summary/*.{txt,json,html} │
    └──────────────────────────────┘
```

### 错误处理与保护机制

1. **`--num-gpus` 废弃保护**（L258-261）：使用旧参数直接 `raise ValueError`
2. **SLURM/DLC 前置检查**（L187-194）：`--slurm` 必须有 `--partition`；`--dlc` 必须有配置文件
3. **eval/viz 模式保护**（L287-291）：必须指定 `--reuse` 或 `--read-from-station`
4. **配置 dump-reload**（L301-306）：通过序列化-反序列化消除运行时对象，确保配置可复现
5. **slurm/dlc 覆盖警告**（L331-335, L376-380）：当配置文件已定义 infer/eval 但又用了 `--slurm/--dlc` 时，给出覆盖警告

如需进一步深入某个具体函数（如 `fill_infer_cfg` 的实现细节、或 `NumWorkerPartitioner` 的分割算法），请告诉我。