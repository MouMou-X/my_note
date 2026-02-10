我按两个维度给你讲这个 CLI 的 `main`：

1. 这个命令入口整体“干了什么事”（执行流程）
2. 它支持的所有参数（按功能分组，把你需要记住的重点挑出来）

下面所有内容都对应你贴的 `opencompass/cli/main.py` 源码。

---

## 一、`main()` 整体干了什么？

`main()` 的核心流程：

```python
def main():
    args = parse_args()                    # 1. 解析命令行参数
    ...                                    # 2. 一些参数检查和默认处理
    cfg = get_config_from_arg(args)        # 3. 根据参数构造总配置 Config
    ...                                    # 4. 设置工作目录 & dump 配置到文件
    ...                                    # 5. 从 station 读取历史结果（可选）
    ...                                    # 6. Lark 机器人通知（可选）
    ...                                    # 7. infer 阶段（推理）
    ...                                    # 8. eval 阶段（打分）
    ...                                    # 9. 结果保存到 station（可选）
    ...                                    # 10. summarizer 汇总&可视化
```

更细一点：

1. **参数解析 `parse_args`**  
   - 支持“单一配置文件”模式，也支持“`--models + --datasets` 快捷模式”，还支持一堆运行控制参数（slurm / dlc / hf / 自定义数据集等）。

2. **构造 Config：`get_config_from_arg`（在 `opencompass/utils/run.py`）**  
   - 如果传了 `config` 位置参数：直接加载这个大 config。
   - 否则：根据 `--models` 在 `configs/models/` 里找模型配置，根据 `--datasets` 在 `configs/datasets/` 里找数据集配置，再根据 `--summarizer` 找 summarizer 配置，拼成一个总的 `cfg`。

3. **设置 work_dir & 时间戳**  
   - work_dir 默认是 `outputs/default`，在里面创建一个以时间戳命名的子目录；
   - 会把当前实际运行用的 cfg dump 成一个独立的 `.py` 文件再读回来，保证后续使用的是一个“纯配置”。

4. **读取 / 保存 station（可选）**  
   - 如果你指定了 `--read-from-station`，会从你的“结果站点”（station）读历史结果信息；
   - 如果设置了 `--station-path`，在任务结束时会把结果写回 station。

5. **Lark 通知（可选）**  
   - 如果 `--lark` 打开且 cfg 里有 `lark_bot_url`，会发一条“任务启动”消息给飞书机器人。

6. **infer 阶段**（`args.mode in ['all', 'infer']`）  
   - 如果 cfg 没有 infer 配置，或者你强制用 `--slurm/--dlc`，会调用 `fill_infer_cfg` 自动生成一套 infer 配置（runner、partitioner 等）。
   - 构造 partitioner → 生成一串 tasks（模型×数据集组合）；
   - 交给 runner（本地 / slurm / dlc）执行，对每个 task 运行 `OpenICLInferTask`，生成 `predictions/*.json`。

7. **eval 阶段**（`args.mode in ['all', 'eval']`）  
   - 同理，如果 cfg 没有 eval 配置或强制 slurm/dlc，调用 `fill_eval_cfg`；
   - 构造 partitioner → 生成 eval tasks；
   - runner 运行 `OpenICLEvalTask`，从 predictions 里读预测，与 ground truth 对比算指标，输出到 `results/*.json`。

8. **summarizer 汇总**  
   - 把各个数据集的结果按你的 summarizer 配置汇总（比如输出表格、排行榜等）；
   - 默认 summarizer 是 `DefaultSummarizer`。

---

## 二、`parse_args()` 支持的参数（按功能分组）

### 1. 最基础：配置文件 / 快捷模式

```python
parser.add_argument('config', nargs='?', help='Train config file path')
parser.add_argument('--models', nargs='+', help='', default=None)
parser.add_argument('--datasets', nargs='+', help='', default=None)
parser.add_argument('--summarizer', help='', default=None)
```

- `config`（可选位置参数）：  
  - 例：`python run.py configs/eval_TheoremQA.py`
  - 给一个大 config 文件，它内部会包含 models、datasets、summarizer 等所有信息。

- `--models`：一个或多个 **模型配置名**（不带 `.py`）  
  - 例：`--models qwen3_30b_a3b_thinking_2507`
  - 实际会去 `configs/models/` 和 `opencompass/configs/models/` 搜索对应的 `.py` 文件。

- `--datasets`：一个或多个 **数据集配置名**  
  - 例：`--datasets TheoremQA_gen`
  - 实际去 `configs/datasets/` 和 `configs/dataset_collections/` 里找同名 `.py`，然后取里面所有 `*_datasets` 的字段。

- `--summarizer`：汇总配置  
  - 默认值：`None`，会在 `get_config_from_arg` 中用默认 `example` summarizer；
  - 支持 `file/key` 形式，例如 `summary_for_TheoremQA/custom_summarizer`。

> 组合规则：  
> - 如果给了 `config`：优先使用这个 config，忽略 `--models/--datasets`  
> - 如果没给 config：必须给 `--models/--datasets` 或 HF 参数 + `--datasets`，否则会报错。

---

### 2. 运行模式和通用控制参数

```python
parser.add_argument('--debug', action='store_true', default=False, ...)
parser.add_argument('--dry-run', action='store_true', default=False, ...)
parser.add_argument(
    '-a', '--accelerator',
    choices=['vllm', 'lmdeploy', None],
    default=None,
)
parser.add_argument(
    '-m', '--mode',
    choices=['all', 'infer', 'eval', 'viz'],
    default='all',
)
parser.add_argument('-r', '--reuse', nargs='?', type=str, const='latest', ...)
parser.add_argument('-w', '--work-dir', default=None, type=str, ...)
...
parser.add_argument(
    '--config-dir',
    default='configs',
)
parser.add_argument(
    '--config-verbose',
    default=False,
    action='store_true',
)
parser.add_argument('-l', '--lark', action='store_true', default=False)
parser.add_argument('--max-num-workers', type=int, default=1)
parser.add_argument('--max-workers-per-gpu', type=int, default=1)
parser.add_argument('--retry', type=int, default=2)
parser.add_argument('--dump-eval-details', nargs='?', const=True, default=True, ...)
parser.add_argument('--dump-extract-rate', action='store_true')
```

逐个解释：

- `--debug`  
  - 打开 DEBUG 日志级别；
  - 同时让 runner 不把子进程输出重定向到日志文件，而直接打印出来，便于排查。

- `--dry-run`  
  - 不真正执行推理/评测，只构造 tasks 并打印出命令；
  - 在 `main` 里表现为：构造完 tasks 后 `if args.dry_run: return`。

- `--accelerator` (`vllm` / `lmdeploy`)  
  - 如果你用了 HF 系列模型或配置文件里是 HF 模型，会把模型配置转成对应的 VLLM/LMDeploy 后端。

- `--mode`  
  - `all`（默认）：先 infer 再 eval 再 summarize；
  - `infer`：只做推理，生成 predictions；
  - `eval`：只做评测（需要已有 predictions，或者从 station 读）；
  - `viz`：只做可视化/汇总（需要已有结果或 station）。

- `--reuse`  
  - 复用 `work_dir` 下已有的实验结果，主要配合 `eval` / `viz`。  
  - 不带参数：`--reuse` → 使用最新时间戳目录；  
  - 带参数：`--reuse 20251201_145235` → 使用指定时间戳的目录。

- `--work-dir`  
  - 设置顶层工作目录，默认是 `outputs/default`；
  - 实际使用的是 `work_dir/<time_str>`。

- `--config-dir`  
  - 默认 `configs`，用于指定自定义配置目录。  
  - 查找模型、数据集、summarizer 时，会同时在这个目录和内置 `opencompass/configs` 里找。

- `--config-verbose`  
  - 打印最终重新加载后的配置内容。

- `--lark`  
  - 开启后，如果 cfg 里提供了 `lark_bot_url`，会发一条“任务已启动”到飞书。

- `--max-num-workers`  
  - runner 同时跑的最大任务数，影响并发度；  
  - 在 `fill_infer_cfg` / `fill_eval_cfg` 中给 runner 和 partitioner 用。

- `--max-workers-per-gpu`  
  - 只在本地 runner 时生效；  
  - 控制每张 GPU 同时跑的任务数量。

- `--retry`  
  - 对于 slurm / dlc runner，失败时重试次数。

- `--dump-eval-details`（默认 True）  
  - 是否在 eval 阶段保存每个样本级的详细信息，比如每条题目的是否正确、bpb 等；  
  - 关闭方式：`--dump-eval-details False`。

- `--dump-extract-rate`  
  - 是否额外计算并保存“抽取率”等信息（对某些评测有用）。

---

### 3. 结果 station 相关参数

```python
parser.add_argument('-sp', '--station-path', type=str, default=None)
parser.add_argument('--station-overwrite', action='store_true')
parser.add_argument('--read-from-station', action='store_true')
```

- `--station-path`  
  - 指定结果 station 的路径（类似一个集中存放评测结果的仓库）。

- `--station-overwrite`  
  - 如果 station 上已存在同名结果，是否覆盖。

- `--read-from-station`  
  - eval / viz 模式时，可以不依赖本地 `work_dir`，直接从 station 读取结果进行评测/可视化。

在 `main` 中：

- eval/viz 模式且没 `--reuse` 也没 `--read-from-station` 会报错。

---

### 4. 复跑次数（多次 run 同一数据集）

```python
parser.add_argument('--dataset-num-runs', type=int, default=1)
```

- 对于支持多次随机 run 的数据集，可以统一设置每个数据集的 run 次数；
- 在 `get_config_from_arg` 里，会把每个数据集配置里的 `n`/`k` 改成这个值。

---

### 5. slurm 相关参数

```python
def parse_slurm_args(slurm_parser):
    slurm_parser.add_argument('-p', '--partition', type=str, default=None)
    slurm_parser.add_argument('-q', '--quotatype', type=str, default=None)
    slurm_parser.add_argument('--qos', type=str, default=None)
```

加上主参数：

```python
launch_method = parser.add_mutually_exclusive_group()
launch_method.add_argument('--slurm', action='store_true', default=False, ...)
```

- `--slurm`：  
  - 强制使用 slurm 调度，runner 会是 `SlurmRunner`；
  - 要求必须指定 `--partition`（分区名），代码里通过 `assert args.partition is not None` 强约束。

- `--partition` / `--quotatype` / `--qos`：  
  - 这些值会被写入 `cfg.infer.runner` / `cfg.eval.runner` 中的 slurm 配置。

---

### 6. dlc 相关参数

```python
launch_method.add_argument('--dlc', action='store_true', default=False, ...)
...
def parse_dlc_args(dlc_parser):
    dlc_parser.add_argument('--aliyun-cfg',
                            default='~/.aliyun.cfg',
                            type=str)
```

- `--dlc`：  
  - 强制使用阿里云 dlc 作为运行环境，runner 是 `DLCRunner`；
  - 要求 `--aliyun-cfg` 指向一个存在的配置文件，否则 `assert os.path.exists(args.aliyun_cfg)` 报错。

- `--aliyun-cfg`：  
  - 阿里云 dlc 的配置路径，默认 `~/.aliyun.cfg`。

---

### 7. HuggingFace 快捷模型参数（不通过 config 文件，而是直接指定模型）

```python
def parse_hf_args(hf_parser):
    hf_parser.add_argument('--hf-type', choices=['base', 'chat'], default='chat')
    hf_parser.add_argument('--hf-path', type=str, help='模型名或本地路径')
    hf_parser.add_argument('--model-kwargs', nargs='+', action=DictAction, default={})
    hf_parser.add_argument('--tokenizer-path', type=str)
    hf_parser.add_argument('--tokenizer-kwargs', nargs='+', action=DictAction, default={})
    hf_parser.add_argument('--peft-path', type=str)
    hf_parser.add_argument('--peft-kwargs', nargs='+', action=DictAction, default={})
    hf_parser.add_argument('--generation-kwargs', nargs='+', action=DictAction, default={})
    hf_parser.add_argument('--max-seq-len', type=int)
    hf_parser.add_argument('--max-out-len', type=int, default=256)
    hf_parser.add_argument('--min-out-len', type=int, default=1)
    hf_parser.add_argument('--batch-size', type=int, default=8)
    hf_parser.add_argument('--num-gpus', type=int, default=None)  # 已废弃
    hf_parser.add_argument('--hf-num-gpus', type=int, default=1)
    hf_parser.add_argument('--pad-token-id', type=int)
    hf_parser.add_argument('--stop-words', nargs='+', default=[])
```

使用方式示例（不依赖模型 config 文件）：

```bash
python run.py \
  --hf-path Qwen/Qwen2.5-7B-Instruct \
  --hf-type chat \
  --datasets TheoremQA_gen
```

注意：

- 如果你用 `--hf-*` 参数而不是 `--models`：
  - `get_config_from_arg` 会构造一个 HuggingFace 模型配置 dict 添加到 `models` 里；
  - 仍然需要 `--datasets` 或自定义数据集路径。

- `--num-gpus` 已废弃，`main()` 一开头就检查它，如果你传了，会直接抛异常，要求改用 `--hf-num-gpus`。

---

### 8. 自定义数据集（不用内置 configs）

```python
def parse_custom_dataset_args(custom_dataset_parser):
    custom_dataset_parser.add_argument('--custom-dataset-path', type=str)
    custom_dataset_parser.add_argument('--custom-dataset-meta-path', type=str)
    custom_dataset_parser.add_argument('--custom-dataset-data-type',
                                       type=str,
                                       choices=['mcq', 'qa'])
    custom_dataset_parser.add_argument('--custom-dataset-infer-method',
                                       type=str,
                                       choices=['gen', 'ppl'])
```

如果你不想用内置 `configs/datasets` 中的配置，而是直接拿一个自己的 json/csv：

- 用法示例：
  ```bash
  python run.py \
    --hf-path Qwen/... \
    --custom-dataset-path /path/to/mydata.json \
    --custom-dataset-data-type mcq \
    --custom-dataset-infer-method gen
  ```

- 在 `get_config_from_arg` 中：
  - 如果没给 `--datasets` 但给了 `--custom-dataset-path`，会构造一个 dataset dict，然后通过 `make_custom_dataset_config` 填完整配置。

---

## 三、`main()` 中与这些参数的关键交互点

你看源码时可以重点关注以下几个地方：

1. **参数校验**

   ```python
   if args.num_gpus is not None:
       raise ValueError('The `--num-gpus` argument is deprecated, ...')
   ...
   if args.slurm:
       assert args.partition is not None
   if args.dlc:
       assert os.path.exists(args.aliyun_cfg)
   ```

2. **work_dir + reuse 逻辑**

   ```python
   if args.work_dir is not None:
       cfg['work_dir'] = args.work_dir
   else:
       cfg.setdefault('work_dir', os.path.join('outputs', 'default'))

   cfg_time_str = dir_time_str = datetime.now().strftime('%Y%m%d_%H%M%S')
   if args.reuse:
       if args.reuse == 'latest':
           ...
           dir_time_str = sorted(dirs)[-1]
       else:
           dir_time_str = args.reuse
       logger.info(f'Reusing experiements from {dir_time_str}')
   elif args.mode in ['eval', 'viz'] and not args.read_from_station:
       raise ValueError(...)
   ```

3. **infer 阶段调用参数**

   - `--mode` 决定是否进入 infer；
   - `--slurm`/`--dlc`/`--max-num-workers`/`--max-workers-per-gpu`/`--retry` 影响 runner；
   - `--debug` 会把 `cfg.infer.runner.debug = True`；
   - `--lark` 会把 `cfg.infer.runner.lark_bot_url` 设成 cfg 里的值。

4. **eval 阶段调用参数**

   - 同上，但用的是 `fill_eval_cfg`，partitioner 默认 `NaivePartitioner`；
   - `--dump-eval-details`、`--dump-extract-rate` 转成 `cfg.eval.runner.task.dump_details/cal_extract_rate`；
   - `--mode` 控制是否执行 eval。

5. **summarizer 的使用**

   - 和 `--mode` 强相关：`['all', 'eval', 'viz']` 时才会运行 summarizer；
   - 如果 summarizer 是复杂的“主-子 summarizer”结构，会按数据集 prefix 分组分别 summarize，再在主 summarizer 里汇总。

---

如果你接下来想针对某个参数（比如 `--accelerator` 或 `--datasets`）顺着看它“一路传到哪里、最终如何影响模型/数据集”，我们可以继续沿着 `get_config_from_arg` → `fill_infer_cfg/fill_eval_cfg` → `partitioners` → `runners` → `tasks.openicl_*` 那条链具体看，比如专门画出“`--datasets TheoremQA_gen` 是如何找到你那几个 TheoremQA 配置项并跑起来的”。