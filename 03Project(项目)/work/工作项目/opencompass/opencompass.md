---
tags: [LLM/Eval]
type: note
status: 🌿
---

 ###### 关联
添加[[Rescources]]       添加[[Notes]]       添加[[Tasks]]

---
# 主页
> [!columns-flex-3]
>
> > [!column]+ 教程
> > [[opencompass命令]]
> >
>
> > [!column]+ 数据集
> > [[TheoremQA]]
> > 
> > 
> >
>
> > [!column]+ 快捷命令
> > ### C栏
> >


```
python my_tools/eval_debugger.py ^ --config "outputs/default/TheoremQA_result/20251211_112822/configs/20251211_141302_5648.py" ^ --predictions "outputs/default/TheoremQA_result/20251211_112822/predictions/qwen3-30b-a3b-instruct-2507-api/TheoremQA.json" ^ --index 177 ^ --data "C:/Users/jun/.cache/opencompass/data/TheoremQA/theoremqa_test.json"
```


# 代码运行基础逻辑
### 1. 入口点与命令解析

当你运行这个命令时，入口点是 [main.py](file://d:\project\opencompass\opencompass\cli\main.py) 中的 `main()` 函数（在 `setup.py` 中定义的 console_scripts）。

**参数解析流程：**
- `--models qwen3_30b_a3b_instruct_2507` → 加载模型配置
- `--datasets TheoremQA_gen` → 加载数据集配置

### 2. 配置加载 (get_config_from_arg)

在 [run.py](file://d:\project\opencompass\opencompass\utils\run.py#L88-L239) 中的 `get_config_from_arg()` 函数负责加载配置：

**模型配置加载：**
- 搜索目录：`opencompass/configs/models/`
- 找到文件：[qwen3_30b_a3b_instruct_2507.py](file://d:\project\opencompass\opencompass\configs\models\qwen\qwen3_30b_a3b_instruct_2507.py)
- 模型类型：`Qwen`（阿里云 DashScope API 模型）
- 模型路径：`qwen3-30b-a3b-instruct-2507`

**数据集配置加载：**
- 搜索目录：`opencompass/configs/datasets/`
- 找到文件：[TheoremQA_gen.py](file://d:\project\opencompass\opencompass\configs\datasets\TheoremQA\TheoremQA_gen.py) → 继承自 [TheoremQA_5shot_gen_6f0af8.py](file://d:\project\opencompass\opencompass\configs\datasets\TheoremQA\TheoremQA_5shot_gen_6f0af8.py)

### 3. 配置内容详解

**模型配置：**
```python
models = [
    dict(
        abbr='qwen3-30b-a3b-instruct-2507-api',
        type=Qwen,                             # 使用 DashScope API
        path='qwen3-30b-a3b-instruct-2507',    # 模型名称
        key='ENV',                              # 从环境变量读取 DASHSCOPE_API_KEY
        max_out_len=2048,
        batch_size=8,
    ),
]
```

**数据集配置：**
```python
TheoremQA_datasets = [
    dict(
        abbr='TheoremQA',
        type=TheoremQADatasetV3,                    # 数据集类
        path='data/TheoremQA/theoremqa_test.json',  # 数据路径
        reader_cfg=...,                             # 读取配置
        infer_cfg=dict(                             # 推理配置
            prompt_template=...,                    # 5-shot 提示模板
            retriever=ZeroRetriever,                # 零样本检索器
            inferencer=GenInferencer,               # 生成式推理器
        ),
        eval_cfg=dict(                              # 评估配置
            evaluator=TheoremQAEvaluatorV3,         # 评估器
            pred_postprocessor=TheoremQA_postprocess_v3,  # 后处理器
        ),
    )
]
```

### 4. 主流程执行 (main.py)

```
main()
├── parse_args()                    # 解析命令行参数
├── get_config_from_arg(args)       # 加载配置 → Config(models=..., datasets=...)
├── 设置 work_dir                   # outputs/default/YYYYMMDD_HHMMSS
│
├── 【推理阶段】 mode='infer' or 'all'
│   ├── fill_infer_cfg()            # 填充推理配置
│   ├── partitioner = NumWorkerPartitioner.build()  # 创建任务分区器
│   ├── tasks = partitioner(cfg)    # 划分推理任务
│   └── runner(tasks)               # LocalRunner 执行推理任务
│
├── 【评估阶段】 mode='eval' or 'all'
│   ├── fill_eval_cfg()             # 填充评估配置
│   ├── partitioner = NaivePartitioner.build()
│   ├── tasks = partitioner(cfg)    # 划分评估任务
│   └── runner(tasks)               # LocalRunner 执行评估任务
│
└── 【汇总阶段】 mode='viz' or 'all'
    └── summarizer.summarize()      # 汇总结果
```

### 5. 推理任务执行 (OpenICLInferTask)

在 [openicl_infer.py](file://d:\project\opencompass\opencompass\tasks\openicl_infer.py) L64-L142中：

```
OpenICLInferTask.run()
├── 构建模型: Qwen 类实例
├── 构建数据集: TheoremQADatasetV3
├── _inference()
│   ├── 构建 PromptTemplate（5-shot 模板）
│   ├── 构建 ZeroRetriever
│   ├── 构建 GenInferencer
│   └── inferencer.inference()
│       ├── 遍历每个测试样本
│       ├── 使用模板生成 prompt
│       ├── 调用 Qwen.generate() → DashScope API
│       └── 保存预测结果到 predictions/qwen3-30b-a3b-instruct-2507-api/TheoremQA.json
```

### 6. 模型调用 (Qwen API)

在 [qwen_api.py](file://d:\project\opencompass\opencompass\models\qwen_api.py) L12-L210中：

```python
Qwen._generate(input)
├── 从环境变量读取 DASHSCOPE_API_KEY
├── 将 prompt 转换为 messages 格式
└── dashscope.Generation.call(model='qwen3-30b-a3b-instruct-2507', messages=...)
```

### 7. 评估任务执行 (OpenICLEvalTask)

在 [openicl_eval.py](file://d:\project\opencompass\opencompass\tasks\openicl_eval.py) L70-L107中：

```
OpenICLEvalTask.run()
├── _score()
│   ├── _load_and_preprocess_test_data()  # 加载测试数据
│   ├── _load_predictions()                # 加载预测结果
│   ├── _process_predictions()             # 应用 TheoremQA_postprocess_v3
│   ├── _evaluate_predictions()            # 使用 TheoremQAEvaluatorV3 评估
│   └── _save_results()                    # 保存结果到 results/
```

### 8. 输出目录结构

```
outputs/default/YYYYMMDD_HHMMSS/
├── configs/                           # 配置文件备份
├── predictions/
│   └── qwen3-30b-a3b-instruct-2507-api/
│       └── TheoremQA.json             # 模型预测结果
├── results/
│   └── qwen3-30b-a3b-instruct-2507-api/
│       └── TheoremQA.json             # 评估结果
└── summary/                           # 汇总结果
```

