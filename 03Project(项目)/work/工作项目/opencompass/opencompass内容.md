---
tags: [LLM/Eval]
type: note
status: 🌿
---

- 模型和数据集调用
模型和数据集以配置文件形式预先存储在`configs/models`和 中`configs/datasets`。用户可以使用 来查看或筛选当前可用的模型和数据集配置`tools/list_configs.py`
```
python tools/list_configs.py
```
```
python tools/list_configs.py qwen ARC
```


- 查询包的指向
```
Get-Command opencompass
```


- debug
```
opencompass --models qwen_api_plus --datasets demo_gsm8k_chat_gen --debug
```
```
opencompass --models qwen_api_plus --datasets demo_gsm8k_chat_gen
```
```
opencompass --models qwen_api_flash --datasets demo_gsm8k_chat_gen
```
```
opencompass --models qwen3_30b_a3b_instruct_2507 --datasets demo_gsm8k_chat_gen
```
```
opencompass --models qwen3_30b_a3b_thinking_2507 --datasets demo_gsm8k_chat_gen
```

测试gpt
```
opencompass --models gpt_4o_2024_05_13 --datasets demo_gsm8k_chat_gen --debug
```

```
opencompass examples/eval_qwen_api_demo.py
```
```
opencompass examples/eval_api_demo.py
```


```
opencompass --models qwen3_30b_a3b_instruct_2507 --datasets calm -m infer -r <时间戳>
```

```
opencompass --models qwen3_30b_a3b_instruct_2507 --datasets calm -m eval -r 20260120_151123
```

```
opencompass --models qwen_plus --datasets calm
```
```
opencompass --models qwen_flash --datasets calm --enhance --reuse
```
```
opencompass --models qwen3_30b_a3b_instruct_2507 --datasets calm
```
```
opencompass --models qwen3_30b_a3b_thinking_2507 --datasets calm
```


# 实用工具
## prompt viewer
本工具允许你在不启动完整训练流程的情况下，直接查看生成的 prompt。如果传入的配置仅为数据集配置（如 `configs/datasets/nq/nq_gen_3dcea1.py`），则展示数据集配置中定义的原始 prompt。若为完整的评测配置（包含模型和数据集），则会展示所选模型运行时实际接收到的 prompt。

运行方式：
```
python tools/prompt_viewer.py configs\datasets\TheoremQA\TheoremQA_5shot_gen_6f0af8.py [-n] [-a] [-p PATTERN]
```

```
python tools/prompt_viewer.py opencompass\configs\datasets\bbh\bbh_gen_ee62e9.py -a
```

- `-n`: 不进入交互模式，默认选择第一个 model （如有）和 dataset。
    
- `-a`: 查看配置中所有模型和所有数据集组合接收到的 prompt。
    
- `-p PATTERN`: 不进入交互模式，选择所有与传入正则表达式匹配的数据集。
	
- **完全非交互、只打印 Ruin_Names 的 prompt：**

``` python
tools/prompt_viewer.py opencompass/configs/datasets/bbh/bbh_gen_4a31fa.py -n -p "bbh-ruin_names" 
```   


## 正确的使用方法

根据源码（第18-34行），`prompt_viewer.py` 支持以下参数：

1. **必需参数**：
    - `config`: 配置文件路径
2. **可选参数**：
    - `-n` 或 `--non-interactive`: 非交互模式
    - `-a` 或 `--all`: 显示所有
    - `-p PATTERN` 或 `--pattern PATTERN`: 匹配数据集名称的模式
    - `-c COUNT` 或 `--count COUNT`: 打印的提示数量（默认为1）

## 正确的命令示例

以下是几种正确的使用方式：

### 1. **交互式模式（windows系统无法使用）** 
```cmd
python tools/prompt_viewer.py opencompass\configs\datasets\TheoremQA\TheoremQA_5shot_gen_6f0af8.py
```

### 2. **非交互模式（自动选择第一个）**
```cmd
python tools/prompt_viewer.py opencompass\configs\datasets\TheoremQA\TheoremQA_5shot_gen_6f0af8.py -n
```

### 3. **显示所有数据集的提示**
```cmd
python tools/prompt_viewer.py opencompass\configs\datasets\TheoremQA\TheoremQA_5shot_gen_6f0af8.py -a 
```

### 4. **使用模式匹配**
```cmd
python tools/prompt_viewer.py opencompass\configs\datasets\TheoremQA\TheoremQA_5shot_gen_6f0af8.py -p "TheoremQA*" 
```

### 5. **显示多个提示（例如3个）**
```cmd
python tools/prompt_viewer.py opencompass\configs\datasets\TheoremQA\TheoremQA_5shot_gen_6f0af8.py -c 3
```

### 6. **组合使用**
```cmd
python tools/prompt_viewer.py opencompass\configs\datasets\TheoremQA\TheoremQA_5shot_gen_6f0af8.py -n -c 3
```

---

