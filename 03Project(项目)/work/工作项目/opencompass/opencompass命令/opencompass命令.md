---
type:
  - note
父任务: "[[opencompass]]"
---
![[opencompass#关联]]

---

## OpenCompass CLI 参数详解

### 一、基本配置参数

#### 1. `config` (位置参数)
```bash
# 使用配置文件
opencompass examples/eval_chat_demo.py
```
**源码位置**: [main.py#L23](file://d:\project\opencompass\opencompass\cli\main.py#L23)
- 直接传入 Python 配置文件路径，包含完整的 models 和 datasets 定义

#### 2. `--models` 和 `--datasets`
```bash
# 使用预定义配置
opencompass --models hf_internlm2_chat_1_8b qwen3_30b_a3b_instruct_2507 --datasets TheoremQA_gen demo_gsm8k_chat_gen
```
**源码位置**: [run.py#L179-L186](file://d:\project\opencompass\opencompass\utils\run.py#L179-L186)
- 从 `opencompass/configs/models/` 和 `opencompass/configs/datasets/` 搜索匹配的配置文件
- 支持多个模型和数据集同时评测

#### 3. `--summarizer`
```bash
opencompass --models ... --datasets ... --summarizer example
```
**源码位置**: [run.py#L213-L237](file://d:\project\opencompass\opencompass\utils\run.py#L213-L237)
- 指定汇总器配置，从 `opencompass/configs/summarizers/` 加载
- 支持 `summarizer/key` 格式指定特定的汇总器键

---

### 二、运行模式参数

#### 1. `-m / --mode`
```bash
# 只运行推理
opencompass --models ... --datasets ... -m infer

# 只运行评估（需要 -r 复用已有推理结果）
opencompass --models ... --datasets ... -m eval -r latest

# 只可视化结果
opencompass --models ... --datasets ... -m viz -r latest

# 完整流程（默认）
opencompass --models ... --datasets ... -m all
```
**源码位置**: [main.py#L63-L71](file://d:\project\opencompass\opencompass\cli\main.py#L63-L71) 和 [main.py#L317-L400](file://d:\project\opencompass\opencompass\cli\main.py#L317-L400)

| 模式 | 执行阶段 |
|------|----------|
| `all` | infer → eval → viz（完整流程）|
| `infer` | 只推理，生成 predictions |
| `eval` | 只评估，需要已有 predictions |
| `viz` | 只汇总可视化 |

#### 2. `-r / --reuse`
```bash
# 复用最新结果
opencompass --models ... --datasets ... -r

# 复用指定时间戳的结果
opencompass --models ... --datasets ... -r 20231215_143025
```
**源码位置**: [main.py#L72-L81](file://d:\project\opencompass\opencompass\cli\main.py#L72-L81) 和 [main.py#L267-L277](file://d:\project\opencompass\opencompass\cli\main.py#L267-L277)
- 复用已有的 predictions 和 results，只运行缺失的任务
- 不指定参数时默认复用最新结果 (`latest`)

#### 3. `--debug`
```bash
opencompass --models ... --datasets ... --debug
```
**源码位置**: [main.py#L45-L50](file://d:\project\opencompass\opencompass\cli\main.py#L45-L50) 和 [local.py#L97-L152](file://d:\project\opencompass\opencompass\runners\local.py#L97-L152)
- 单进程运行，方便调试
- 输出不重定向到文件，直接打印到控制台
- 可以设置断点调试

#### 4. `--dry-run`
```bash
opencompass --models ... --datasets ... --dry-run
```
**源码位置**: [main.py#L51-L56](file://d:\project\opencompass\opencompass\cli\main.py#L51-L56) 和 [main.py#L346-L347](file://d:\project\opencompass\opencompass\cli\main.py#L346-L347)
- 只打印将要执行的命令，不实际运行任务
- 自动启用 debug 模式

---

### 三、工作目录与配置

#### 1. `-w / --work-dir`
```bash
opencompass --models ... --datasets ... -w outputs/my_experiment
```
**源码位置**: [main.py#L82-L90](file://d:\project\opencompass\opencompass\cli\main.py#L82-L90) 和 [main.py#L260-L263](file://d:\project\opencompass\opencompass\cli\main.py#L260-L263)
- 指定输出目录，默认为 `outputs/default`
- 实际路径为 `work_dir/YYYYMMDD_HHMMSS/`

#### 2. `--config-dir`
```bash
opencompass --models ... --datasets ... --config-dir my_configs
```
**源码位置**: [main.py#L91-L96](file://d:\project\opencompass\opencompass\cli\main.py#L91-L96) 和 [run.py#L128-L134](file://d:\project\opencompass\opencompass\utils\run.py#L128-L134)
- 使用自定义配置目录代替默认的 `opencompass/configs/`
- 会同时搜索自定义目录和默认目录

#### 3. `--config-verbose`
```bash
opencompass --models ... --datasets ... --config-verbose
```
**源码位置**: [main.py#L97-L101](file://d:\project\opencompass\opencompass\cli\main.py#L97-L101) 和 [main.py#L313-L315](file://d:\project\opencompass\opencompass\cli\main.py#L313-L315)
- 详细打印配置内容，用于调试配置问题

---

### 四、并行与资源控制

#### 1. `--max-num-workers`
```bash
# 最多 4 个任务并行
opencompass --models ... --datasets ... --max-num-workers 4
```
**源码位置**: [main.py#L107-L112](file://d:\project\opencompass\opencompass\cli\main.py#L107-L112) 和 [local.py#L192-L194](file://d:\project\opencompass\opencompass\runners\local.py#L192-L194)
- 控制最大并行任务数
- 默认值为 1

#### 2. `--max-workers-per-gpu`
```bash
# 每个 GPU 上最多运行 2 个任务
opencompass --models ... --datasets ... --max-workers-per-gpu 2
```
**源码位置**: [main.py#L113-L117](file://d:\project\opencompass\opencompass\cli\main.py#L113-L117) 和 [local.py#L154-L158](file://d:\project\opencompass\opencompass\runners\local.py#L154-L158)
- 仅在 LocalRunner 中生效
- 用于 API 模型或显存较小的任务

---

### 五、推理加速

#### 1. `-a / --accelerator`
```bash
# 使用 vLLM 加速
opencompass --models hf_internlm2_chat_1_8b --datasets ... -a vllm

# 使用 LMDeploy 加速
opencompass --models hf_internlm2_chat_1_8b --datasets ... -a lmdeploy
```
**源码位置**: [main.py#L57-L62](file://d:\project\opencompass\opencompass\cli\main.py#L57-L62) 和 [run.py#L242-L360](file://d:\project\opencompass\opencompass\utils\run.py#L242-L360)
- 将 HuggingFace 模型转换为 vLLM 或 LMDeploy 后端
- 自动转换模型配置，包括 `engine_config` 和 `gen_config`

---

### 六、评估结果控制

#### 1. `--dump-eval-details`
```bash
# 导出详细评估信息（默认开启）
opencompass --models ... --datasets ... --dump-eval-details

# 禁用详细评估信息
opencompass --models ... --datasets ... --dump-eval-details False
```
**源码位置**: [main.py#L124-L132](file://d:\project\opencompass\opencompass\cli\main.py#L124-L132) 和 [main.py#L369-L373](file://d:\project\opencompass\opencompass\cli\main.py#L369-L373)
- 导出每个样本的预测结果、正确性等详细信息
- 存储在 `results/` 目录的 JSON 文件中

#### 2. `--dump-extract-rate`
```bash
opencompass --models ... --datasets ... --dump-extract-rate
```
**源码位置**: [main.py#L133-L138](file://d:\project\opencompass\opencompass\cli\main.py#L133-L138) 和 [main.py#L374-L375](file://d:\project\opencompass\opencompass\cli\main.py#L374-L375)
- 计算并输出答案提取成功率

---

### 七、结果持久化（Station）

#### 1. `-sp / --station-path`
```bash
# 保存结果到数据站
opencompass --models ... --datasets ... -sp /shared/results
```
**源码位置**: [main.py#L139-L145](file://d:\project\opencompass\opencompass\cli\main.py#L139-L145) 和 [result_station.py#L11-L112](file://d:\project\opencompass\opencompass\utils\result_station.py#L11-L112)
- 将评测结果保存到共享目录
- 格式：`station_path/dataset_name/model_name.json`

#### 2. `--station-overwrite`
```bash
# 覆盖已有结果
opencompass --models ... --datasets ... -sp /shared/results --station-overwrite
```
**源码位置**: [main.py#L147-L150](file://d:\project\opencompass\opencompass\cli\main.py#L147-L150)

#### 3. `--read-from-station`
```bash
# 从数据站读取已有结果，避免重复评测
opencompass --models ... --datasets ... -sp /shared/results --read-from-station
```
**源码位置**: [main.py#L152-L157](file://d:\project\opencompass\opencompass\cli\main.py#L152-L157) 和 [result_station.py#L241-L375](file://d:\project\opencompass\opencompass\utils\result_station.py#L241-L375)

---

### 八、集群运行（Slurm/DLC）

#### 1. Slurm 模式
```bash
# 使用 Slurm 集群
opencompass --models ... --datasets ... --slurm -p gpu_partition -q auto --qos high
```
**源码位置**: [main.py#L28-L33](file://d:\project\opencompass\opencompass\cli\main.py#L28-L33)、[main.py#L189-L204](file://d:\project\opencompass\opencompass\cli\main.py#L189-L204) 和 [slurm.py](file://d:\project\opencompass\opencompass\runners\slurm.py)

| 参数 | 说明 |
|------|------|
| `--slurm` | 启用 Slurm 模式 |
| `-p / --partition` | Slurm 分区名（必须） |
| `-q / --quotatype` | 配额类型 |
| `--qos` | 服务质量 |
| `--retry` | 失败重试次数（默认 2） |

#### 2. DLC 模式（阿里云）
```bash
# 使用阿里云 DLC
opencompass --models ... --datasets ... --dlc --aliyun-cfg ~/.aliyun.cfg
```
**源码位置**: [main.py#L34-L39](file://d:\project\opencompass\opencompass\cli\main.py#L34-L39) 和 [dlc.py](file://d:\project\opencompass\opencompass\runners\dlc.py)

---

### 九、HuggingFace 模型参数

```bash
# 快速评测自定义 HuggingFace 模型
opencompass --datasets demo_gsm8k_chat_gen \
    --hf-type chat \
    --hf-path Qwen/Qwen2-7B-Instruct \
    --hf-num-gpus 2 \
    --batch-size 16 \
    --max-out-len 1024 \
    --model-kwargs device_map=auto \
    --generation-kwargs do_sample=True temperature=0.7 \
    --stop-words '<|im_end|>'
```
**源码位置**: [main.py#L215-L232](file://d:\project\opencompass\opencompass\cli\main.py#L215-L232) 和 [run.py#L187-L208](file://d:\project\opencompass\opencompass\utils\run.py#L187-L208)

| 参数 | 说明 |
|------|------|
| `--hf-type` | 模型类型：`base` 或 `chat` |
| `--hf-path` | HuggingFace 模型路径 |
| `--hf-num-gpus` | 模型需要的 GPU 数量 |
| `--batch-size` | 批大小 |
| `--max-out-len` | 最大输出长度 |
| `--max-seq-len` | 最大序列长度 |
| `--model-kwargs` | 模型构建参数 |
| `--tokenizer-path` | Tokenizer 路径 |
| `--tokenizer-kwargs` | Tokenizer 参数 |
| `--generation-kwargs` | 生成参数 |
| `--stop-words` | 停止词列表 |
| `--peft-path` | PEFT/LoRA 模型路径 |

---

### 十、自定义数据集参数

```bash
# 评测自定义数据集（自动解析格式）
opencompass --models ... \
    --custom-dataset-path my_data.jsonl \
    --custom-dataset-data-type mcq \
    --custom-dataset-infer-method gen
```
**源码位置**: [main.py#L235-L244](file://d:\project\opencompass\opencompass\cli\main.py#L235-L244) 和 [custom.py#L535-L550](file://d:\project\opencompass\opencompass\datasets\custom.py#L535-L550)

| 参数 | 说明 |
|------|------|
| `--custom-dataset-path` | 数据集文件路径（.jsonl 或 .csv）|
| `--custom-dataset-meta-path` | 元数据文件路径（可选）|
| `--custom-dataset-data-type` | 数据类型：`mcq`（选择题）或 `qa`（问答）|
| `--custom-dataset-infer-method` | 推理方法：`gen`（生成式）或 `ppl`（困惑度）|

**数据格式示例**（jsonl）:
```json
{"question": "What is 2+2?", "A": "3", "B": "4", "C": "5", "D": "6", "answer": "B"}
```

---

### 十一、常用命令组合示例

```bash
# 1. 基础评测
opencompass --models hf_internlm2_chat_1_8b --datasets demo_gsm8k_chat_gen

# 2. 多模型多数据集 + vLLM 加速
opencompass --models hf_llama3_8b_instruct hf_qwen2_7b_instruct \
    --datasets mmlu_gen gsm8k_gen humaneval_gen \
    -a vllm --max-num-workers 4

# 3. 调试模式
opencompass --models qwen3_30b_a3b_instruct_2507 --datasets TheoremQA_gen --debug

# 4. 复用推理结果，只重新评估
opencompass --models ... --datasets ... -m eval -r latest

# 5. Slurm 集群运行
opencompass --models ... --datasets ... --slurm -p gpu -q auto --max-num-workers 16

# 6. 快速评测自定义 HF 模型
opencompass --datasets demo_gsm8k_chat_gen \
    --hf-type chat --hf-path meta-llama/Llama-3-8B-Instruct
```

这就是 OpenCompass CLI 所有参数的详细使用说明，每个参数都标注了对应的源码位置供你进一步查看实现细节。