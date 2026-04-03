# 报告 1：OpenCompass Evaluator 模块深入分析

## 概述

OpenCompass Evaluator 模块由三个主要层级组成：

1. **ICL评估器基础层** (`opencompass/openicl/icl_evaluator/`) - 提供统一的评估接口和具体实现
2. **高级评估器层** (`opencompass/evaluator/`) - 提供LLM判断和级联评估等高级功能
3. **指标计算层** (`opencompass/metrics/`) - 提供MME、SEEDBench等专用指标

---

## 第一部分：文件清单与功能概览

### 1.1 ICL评估器 (`opencompass/openicl/icl_evaluator/`)

|文件|功能描述|类型|
|---|---|---|
|`icl_base_evaluator.py`|所有评估器的基类，定义evaluate()和score()接口|基类|
|`icl_em_evaluator.py`|精确匹配(Exact Match)评估|基础评估器|
|`icl_hf_evaluator.py`|HuggingFace evaluate集成，包含Accuracy、Rouge等|复合评估器|
|`icl_aucroc_evaluator.py`|AUC-ROC分类评估|基础评估器|
|`icl_circular_evaluator.py`|圆形选项评估(多圆形偏移)|特殊评估器|
|`icl_bpc_evaluator.py`|比特数/字符(BPC)评估，用于预训练模型|基础评估器|
|`icl_jieba_rouge_evaluator.py`|中文分词+ROUGE评估|特殊评估器|
|`icl_judge_evaluator.py`|判断类(Judge/RMB)评估|基础评估器|
|`icl_toxic_evaluator.py`|毒性检测(Perspective API)|外部API评估器|
|`icl_plugin_evaluator.py`|TEval插件评估器|插件评估器|
|`icl_agent_evaluator.py`|智能代理(ToolBench)评估|复杂评估器|
|`icl_korbench_evaluator.py`|KorBench韩文基准评估|专用评估器|
|`lm_evaluator.py`|多模型对比评估(LMEvaluator)|高级评估器|
|`pi_llm_evaluator.py`|Procedural Instruction LLM评估|特殊评估器|
|`code_evaluator.py`|代码执行和评估|特殊评估器|
|`hf_metrics/`|HuggingFace指标本地缓存(4项)|指标库|
|`__init__.py`|模块导出|配置|

### 1.2 高级评估器 (`opencompass/evaluator/`)

|文件|功能描述|场景|
|---|---|---|
|`generic_llm_evaluator.py`|通用LLM判断评估器，使用Judge LLM评分|主观评估|
|`cascade_evaluator.py`|级联评估，先规则后LLM|复合评估|
|`math_evaluator.py`|数学表达式验证(支持LaTeX)|数学任务|
|`__init__.py`|模块导出|配置|

### 1.3 指标计算 (`opencompass/metrics/`)

|文件|功能描述|依赖|
|---|---|---|
|`dump_results.py`|结果转储指标|mmengine|
|`mme_score.py`|MME(多模态模型评估)得分|mmengine BaseMetric|
|`seedbench.py`|SEED-Bench视觉评估|mmengine BaseMetric|
|`__init__.py`|模块导出|-|

---

## 第二部分：核心类详细分析

### 2.1 BaseEvaluator 基类

**文件位置：** `d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\icl_base_evaluator.py`

**关键方法签名：**

python

`   ``` class BaseEvaluator:     def __init__(self, pred_postprocessor=None) -> None          def evaluate(         self,         k: Union[int, List[int]],         n: int,         original_dataset: Dataset,         **score_kwargs,     ) -> Dict          def score(self):  # 抽象方法，由子类实现         raise NotImplementedError()          def pred_postprocess(self, predictions: List) -> Dict          def group(self, n: int, details: List[Dict], test_set: Dataset) -> Dict          def reduce(self, details: List[Dict]) -> Dict ```   `

**核心功能详解：**

|方法|行号|功能|关键逻辑|
|---|---|---|---|
|`__init__()`|47-49|初始化|设置pred_postprocessor，初始化dataset_replica_idx为0|
|`evaluate()`|104-233|完整评估流程|(1)遍历n个副本数据集 (2)调用score()计算指标 (3)合并副本结果 (4)计算G-Pass@k统计量|
|`score()`|235-236|评估接口|抽象方法，子类必须实现；签名：`score(predictions, references, test_set=None)`|
|`pred_postprocess()`|95-102|预测后处理|使用TEXT_POSTPROCESSORS注册表应用后处理函数|
|`group()`|60-71|按示例分组|根据subdivision和idx将多个副本结果分组，用于多轮评估|
|`reduce()`|73-93|归约统计|按subdivision计算G-Pass@k、mG-Pass@k等高级指标|

**输入输出格式：**

python

`   ``` # 输入（通过evaluate()的score_kwargs） {     'predictions': List[str],  # 模型预测     'references': List[str or List],  # 参考答案     'test_set': Optional[Dataset],  # 原始数据集 }  # 输出（score()返回字典） {     'accuracy': float,  # 或其他主指标名     'details': List[Dict],  # 样本级详细结果     # 可选：G-Pass@k、mG-Pass@k等 } ```   `

**关键参数解释：**

- `k`: Pass@k的k值，用于多副本评估时计算通过概率
- `n`: 数据集副本数，用于稳定性评估
- `pred_postprocessor`: 预测文本规范化配置（如lowercase、general_postprocess）

---

### 2.2 GenericLLMEvaluator 高级评估器

**文件位置：** `d:\project\opencompass_inner\opencompass\evaluator\generic_llm_evaluator.py`

**类定义：**

python

`   ``` @ICL_EVALUATORS.register_module() class GenericLLMEvaluator(BaseEvaluator):     """通用LLM评估器 - 使用LLM作为裁判进行主观评估"""          def __init__(         self,         prompt_template: ConfigDict,         judge_cfg: ConfigDict,         dataset_cfg: Optional[ConfigDict] = None,         pred_postprocessor: Optional[ConfigDict] = None,         dict_postprocessor: Optional[ConfigDict] = None,         keep_predictions: bool = False,     ) -> None ```   `

**核心方法：**

|方法|行号|功能|参数|
|---|---|---|---|
|`__init__()`|35-59|初始化|prompt_template(提示模板), judge_cfg(Judge LLM配置), dataset_cfg(数据集配置)|
|`build_inferencer()`|61-84|构建推理器|从judge_cfg构建LLM模型和GenInferencer|
|`score()`|86-166|评分主流程|predictions(预测), references(参考), test_set(数据集)|
|`pred_postprocess()`|168-174|预测后处理|应用TEXT_POSTPROCESSORS|
|`output_postprocess()`|176-193|输出后处理|应用DICT_POSTPROCESSORS，支持injection dataset参数|

**score()方法完整执行流程：**

plaintext

`   ``` 1. 验证predictions和references长度一致 (行100-101) 2. build_inferencer() - 创建LLM推理器，获得output_path (行104) 3. pred_postprocess() - 规范化预测文本 (行106) 4. 构建prediction_dict: {'prediction': predictions, 'obj_gold': references} (行109) 5. build_dataset_from_cfg() - 创建评估数据集，添加prediction和reference列 (行112-157)    - 若dataset_cfg存在：加载数据集，添加列    - 若test_set存在：用test_set作为基础，添加列    - 否则：创建LMEvalDataset with prediction_dict 6. 配置retriever为ZeroRetriever (行160) 7. inferencer.inference() - 执行LLM推理，生成output_path (行162-163) 8. mmengine.load(output_path) - 加载LLM评估结果 (行165) 9. output_postprocess() - 处理输出字典 (行166) ```   `

**judge_cfg配置详解（行196-221）：**

python

`   ``` DEFAULT_JUDGE_CFG = {     'type': OpenAISDK,  # 判断模型类型     'path': os.environ['OC_JUDGE_MODEL'],  # 模型名/路径     'key': os.environ['OC_JUDGE_API_KEY'],  # API密钥     'openai_api_base': ['https://api.openai.com/v1/'],  # API端点     'meta_template': {  # 模板配置         'round': [             {'role': 'HUMAN', 'api_role': 'HUMAN'},             {'role': 'BOT', 'api_role': 'BOT', 'generate': True},         ]     },     'query_per_second': 16,  # QPS限流     'batch_size': 1024,  # 批处理大小（注意：某些模型不支持）     'temperature': 0.001,  # 采样温度     'tokenizer_path': 'gpt-4o-2024-05-13',  # 分词器     'verbose': True,  # 详细日志     'max_out_len': 16384,  # 最大输出长度     'max_seq_len': 49152,  # 最大序列长度 } ```   `

**重要注意：** 参数兼容性问题

- 某些参数(如batch_size、max_out_len、temperature)不是模型**init**的参数
- build_model_from_cfg会将整个dict传给构造函数，导致TypeError
- 应通过generation_kwargs或其他机制传递运行时参数

---

### 2.3 CascadeEvaluator 级联评估器

**文件位置：** `d:\project\opencompass_inner\opencompass\evaluator\cascade_evaluator.py`

**设计思想：** 先用规则评估，失败案例转给LLM重新评估，提高效率

**类定义：**

python

`   ``` @ICL_EVALUATORS.register_module() class CascadeEvaluator(BaseEvaluator):     """级联评估器          流程：规则评估 → 失败案例 → LLM再评估 → 合并结果     """          def __init__(         self,         llm_evaluator: Dict,         rule_evaluator: Optional[Dict] = None,         sample_score_fn: Optional[Callable] = None,         parallel: bool = True,     ) -> None ```   `

**核心方法执行流程：**

|阶段|行号|操作|输出|
|---|---|---|---|
|**初始化**|30-60|初始化llm_evaluator和rule_evaluator|self.llm_evaluator, self.rule_evaluator|
|**规则评估**|147-164|逐样本调用sample_score()或rule_evaluator.score()|details[rule_evaluation]|
|**计算初始精度**|166-175|统计规则通过数和通过率|initial_correct, initial_accuracy|
|**标记失败样本**|147-164|收集失败(或parallel模式下所有)样本|failed_predictions, failed_indices|
|**LLM评估**|183-246|若有失败样本，创建subset并调用llm_evaluator.score()|llm_results with details|
|**结果合并**|266-302|根据评估模式(parallel/cascade)合并结果，计算最终精度|cascade_correct标志|
|**输出**|328-359|返回包含cascade_stats和details的结果dict|包含详细统计|

**关键参数说明：**

|参数|类型|默认值|说明|
|---|---|---|---|
|`llm_evaluator`|Dict|必需|LLM判断器配置(GenericLLMEvaluator)|
|`rule_evaluator`|Dict|None|规则评估器(如EMEvaluator)，与sample_score_fn二选一|
|`sample_score_fn`|Callable|None|自定义样本评分函数，与rule_evaluator二选一|
|`parallel`|bool|True|评估模式：True=并行(所有样本送LLM)，False=级联(仅失败样本)|

**cascade_stats输出详解：**

python

`   ``` {     'total_samples': int,  # 总样本数     'rule_correct': int,  # 规则评估通过数     'rule_accuracy': float,  # 规则评估精度(%)     'llm_evaluated': int,  # LLM评估样本数     'llm_correct': int,  # LLM评估通过数     'llm_accuracy': float,  # LLM评估精度(%)     'final_correct': int,  # 最终通过数     'final_accuracy': float,  # 最终精度(%)     'parallel_mode': bool,  # 评估模式标志 } ```   `

**重要方法：**

python

`   ``` def _get_llm_correctness(self, llm_detail: Dict) -> bool:     """解析LLM评估结果中的判断(行101-120)          检查字段优先级：     1. 'prediction' / 'llm_judge': 'A'或以'CORRECT'开头     2. 'correct': 布尔值     3. 'score': > 0.5判为正确     """ ```   `

---

### 2.4 具体评估器示例

#### 2.4.1 EMEvaluator (精确匹配)

**文件：** `icl_em_evaluator.py` (42行)

python

`   ``` @ICL_EVALUATORS.register_module() class EMEvaluator(BaseEvaluator):     def score(self, predictions: List, references: List) -> Dict:         # predictions: 模型输出字符串列表         # references: 参考答案（可能含多个等价表述）         # 返回: {'score': float, 'details': List[Dict]}                  # 流程：         # 1. 对predictions和references应用general_postprocess规范化         # 2. 逐样本检查predictions[i]是否在references[i]中         # 3. 统计匹配数计算精度 ```   `

#### 2.4.2 AccuracyEvaluator (准确率)

**文件：** `icl_hf_evaluator.py` (行100-147)

python

`   ``` @ICL_EVALUATORS.register_module() class AccEvaluator(HuggingfaceEvaluator):     """基于HuggingFace evaluate.load('accuracy')的准确率评估"""          def __init__(self, pred_postprocessor=None):         super().__init__(metric='accuracy', pred_postprocessor=pred_postprocessor)          def _preprocess(self, predictions, references, test_set=None) -> Dict:         # 1. 从references中提取所有唯一标签，创建标签→索引映射         # 2. 将predictions中未见标签也加入映射         # 3. 返回 {         #     'predictions': [map_pred_to_idx],         #     'references': [map_ref_to_idx]         #   }          def _postprocess(self, scores) -> Dict:         # HF返回0-1范围，乘以100转为百分比         scores['accuracy'] *= 100         return scores ```   `

#### 2.4.3 AUCROCEvaluator (分类评估)

**文件：** `icl_aucroc_evaluator.py` (43行)

python

`   ``` def score(self, predictions: List, references: List) -> Dict:     # predictions: 各类概率矩阵 shape=(N, num_classes)     # references: 真实标签 shape=(N,)     # 返回: {     #     'auc_score': float (0-100范围),     #     'accuracy': float (0-100范围)     # }          auc_score = roc_auc_score(references, np.array(predictions)[:, 1])  # 二分类     accuracy = sum(references == np.argmax(predictions, axis=1)) / len(references)     return {'auc_score': auc_score * 100, 'accuracy': accuracy * 100} ```   `

#### 2.4.4 CircularEvaluator (圆形选项评估)

**文件：** `icl_circular_evaluator.py` (107行)

python

`   ``` def score(self, predictions, references) -> Dict:     # references: 格式为 "index--ref--circular_pattern"     #   index: 问题ID     #   ref: 标准答案(A/B/C/D)     #   circular_pattern: 'ABCD'(无旋转)或'BCDA'等(有旋转)     # 计算多种指标：     # - acc_4: 4种旋转模式准确率     # - acc_1: 无旋转准确率     # - more_i_j: 有j个及以上正确的样本比率(i=1,4)     # - vote_i: 投票准确率(i=1,4)     # - prior_X: 选择X的频率(X=A/B/C/D/-) ```   `

---

## 第三部分：Metrics 模块详解

### 3.1 MMEMetric (多模态模型评估)

**文件：** `mme_score.py` (93行)

python

`   ``` @METRICS.register_module() class MMEMetric(BaseMetric):     """MME(Multimodal Model Evaluation)多模态评估指标          任务分类：     - Perception: existence, count, position, color, posters, celebrity,                    scene, landmark, artwork, OCR (10项)     - Cognition: commonsense_reasoning, numerical_calculation,                   text_translation, code_reasoning (4项)     """          def compute_metrics(self, results: List[Dict]) -> Dict:         # 输出: {         #     '<task>': {         #         'acc': float,      # 单pass准确率         #         'acc_plus': float, # 双pass准确率         #         'score': float,    # 综合分数         #     },         #     'Perception': float,   # 感知类综合分         #     'Cognition': float,    # 认知类综合分         #     'Overall': float,      # 总分         # } ```   `

### 3.2 SEEDBenchAcc (SEED基准评估)

**文件：** `seedbench.py` (68行)

python

`   ``` @METRICS.register_module() class SEEDBenchAcc(BaseMetric):     """SEED-Bench视觉理解基准 - 12类视觉任务评估          任务维度(EVAL_DIM_MAPPING)：     1. Scene Understanding       6. Spatial Relations     2. Instance Identity         7. Instance Interaction     3. Instance Attributes       8. Visual Reasoning     4. Instance Location         9. Text Recognition     5. Instance Counting         10. Action Recognition                                  11. Action Prediction                                  12. Procedure Understanding     """          def compute_metrics(self, results) -> Dict:         # 输出: {         #     'Data type {id} - {category}': float (各任务准确率),         #     'Total accuracy': float,  # 总准确率         #     'answer_records': List,   # 详细结果         # } ```   `

---

## 第四部分：评估器调用关系与数据流

### 4.1 调用层级

plaintext

`   ``` ┌─────────────────────────────────────────────────┐ │          OpenCompass CLI Main (run.py)          │ └────────────────────┬────────────────────────────┘                      │         ┌────────────┴──────────────┐         │                           │    推理阶段(Inference)      评估阶段(Evaluation)         │                           │         └────────────┬──────────────┘                      │         ┌────────────▼──────────────────────┐         │   opencompass.tasks.openicl_eval  │         │   (Task Execution)                 │         └────────────┬──────────────────────┘                      │         ┌────────────▼──────────────────────┐         │   Partitioner + Runner            │         │   (并行分片执行)                   │         └────────────┬──────────────────────┘                      │         ┌────────────▼──────────────────────┐         │   BaseEvaluator.evaluate()        │         │   或 score()                       │         └────────────┬──────────────────────┘                      │         ┌────────────▼──────────────────────┐         │   具体评估器实现                   │         │   (EMEvaluator/AccEvaluator等)    │         └────────────┬──────────────────────┘                      │         ┌────────────▼──────────────────────┐         │   HuggingFace evaluate 或         │         │   自定义指标计算                   │         └──────────────────────────────────┘ ```   `

### 4.2 数据流示例（以GenericLLMEvaluator为例）

plaintext

`   ``` 输入数据：   predictions: ["Yes, the answer is 42", ...]   references: ["42 is the answer", ...]   test_set: Dataset with original questions              │              ▼   ┌─────────────────────────────────────┐   │ 1. Postprocess predictions          │   │    (normalize text)                  │   └─────────────────────────────────────┘              │              ▼   ┌─────────────────────────────────────┐   │ 2. Build dataset with columns       │   │    - prediction (from predictions)  │   │    - obj_gold (from references)     │   │    - other original columns         │   └─────────────────────────────────────┘              │              ▼   ┌─────────────────────────────────────┐   │ 3. Create ZeroRetriever             │   │    (no in-context examples)         │   └─────────────────────────────────────┘              │              ▼   ┌─────────────────────────────────────┐   │ 4. GenInferencer.inference()        │   │    - Apply prompt_template          │   │    - Call judge LLM                 │   │    - Save results to JSON           │   └─────────────────────────────────────┘              │              ▼   ┌─────────────────────────────────────┐   │ 5. Load JSON results                │   │    {                                 │   │      'predictions': [...],           │   │      'details': [...]                │   │    }                                 │   └─────────────────────────────────────┘              │              ▼   ┌─────────────────────────────────────┐   │ 6. Apply output_postprocessor       │   │    (optional processing)            │   └─────────────────────────────────────┘              │              ▼   输出数据：   {     'accuracy': 85.5,     'details': [       {         'pred': 'A',         'answer': 'A',         'correct': True       },       ...     ]   } ```   `

### 4.3 CascadeEvaluator 的数据流

plaintext

`   ``` 输入：predictions, references, test_set  Stage 1: 规则评估   ├─ for each (pred, ref, test_item)   ├─   result = sample_score_fn(pred, ref, test_item)   ├─   details[i] = {'rule_evaluation': result}   └─   if NOT result['correct'] or parallel_mode:         └─ 加入failed列表  Stage 2: LLM评估 (若有失败样本)   ├─ failed_subset = test_set.select(failed_indices)   ├─ failed_subset.add_column('prediction', failed_predictions)   ├─ failed_subset.add_column('reference', failed_references)   ├─ llm_evaluator.score(failed_predictions, failed_references, failed_subset)   └─ llm_results = {        'details': [          {'prediction': 'A', 'correct': True},          ...        ]      }  Stage 3: 结果合并   ├─ for each llm_detail:   │  ├─ original_index = failed_indices[i]   │  ├─ details[original_index]['llm_evaluation'] = llm_detail   │  ├─ is_correct = _get_llm_correctness(llm_detail)   │  └─ if cascade_mode:   │     └─ final_correct += (not rule_correct and is_correct)   │     else (parallel_mode):   │     └─ final_correct += (rule_correct or is_correct)   └─ 返回 cascade_stats 和 details  输出： {   'accuracy': final_accuracy,   'cascade_stats': {     'total_samples': N,     'rule_correct': X,     'llm_correct': Y,     'final_correct': Z,     ...   },   'details': [{     'rule_evaluation': {...},     'llm_evaluation': {...},     'cascade_correct': bool   }, ...] } ```   `

---

## 第五部分：评估器注册与扩展

### 5.1 注册机制

所有评估器使用 `@ICL_EVALUATORS.register_module()` 装饰器注册到全局注册表：

python

`   ``` from opencompass.registry import ICL_EVALUATORS  @ICL_EVALUATORS.register_module() class MyCustomEvaluator(BaseEvaluator):     def score(self, predictions, references, test_set=None):         # 实现评估逻辑         pass ```   `

**注册表查询方式：**

python

`   ``` # 配置中指定评估器 eval_cfg = ConfigDict(     evaluator=dict(         type='AccEvaluator',  # 自动查询ICL_EVALUATORS注册表         # 其他参数...     ) ) ```   `

### 5.2 自定义评估器开发模板

python

`   ``` from opencompass.registry import ICL_EVALUATORS from opencompass.openicl.icl_evaluator import BaseEvaluator  @ICL_EVALUATORS.register_module() class CustomEvaluator(BaseEvaluator):     """自定义评估器说明"""          def __init__(self, param1=None, param2=None):         super().__init__()         self.param1 = param1         self.param2 = param2          def score(self, predictions: List, references: List,                test_set=None) -> Dict:         """必须实现此方法                  Args:             predictions: 模型输出列表             references: 参考答案列表             test_set: 原始数据集(可选)                  Returns:             {                 'primary_metric': float,  # 主要指标                 'details': [              # 样本级详情                     {                         'pred': str,                         'answer': str,                         'correct': bool,                         ...                     }                 ]             }         """         # 必需检查：长度一致性         if len(predictions) != len(references):             return {'error': 'predictions and references have different length'}                  # 评估逻辑         results = []         for pred, ref in zip(predictions, references):             # 你的评估代码             correct = (pred == ref)             results.append({                 'pred': pred,                 'answer': ref,                 'correct': correct             })                  # 计算聚合指标         score = sum(r['correct'] for r in results) / len(results) * 100                  return {             'accuracy': score,             'details': results         } ```   `

---

## 第六部分：关键文件路径索引

### ICL评估器基类与工具

- 基类定义：`d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\icl_base_evaluator.py`
- 模块导出：`d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\__init__.py`

### 具体评估器实现

- 精确匹配：`d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\icl_em_evaluator.py`
- HuggingFace集成：`d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\icl_hf_evaluator.py`
- AUC-ROC：`d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\icl_aucroc_evaluator.py`
- 圆形评估：`d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\icl_circular_evaluator.py`
- BPC评估：`d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\icl_bpc_evaluator.py`
- 毒性检测：`d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\icl_toxic_evaluator.py`
- 代理评估：`d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\icl_agent_evaluator.py`
- LM评估：`d:\project\opencompass_inner\opencompass\openicl\icl_evaluator\lm_evaluator.py`

### 高级评估器

- LLM判断：`d:\project\opencompass_inner\opencompass\evaluator\generic_llm_evaluator.py`
- 级联评估：`d:\project\opencompass_inner\opencompass\evaluator\cascade_evaluator.py`
- 数学验证：`d:\project\opencompass_inner\opencompass\evaluator\math_evaluator.py`
- 模块导出：`d:\project\opencompass_inner\opencompass\evaluator\__init__.py`

### 指标模块

- MME指标：`d:\project\opencompass_inner\opencompass\metrics\mme_score.py`
- SEED指标：`d:\project\opencompass_inner\opencompass\metrics\seedbench.py`
- 结果转储：`d:\project\opencompass_inner\opencompass\metrics\dump_results.py`
- 模块导出：`d:\project\opencompass_inner\opencompass\metrics\__init__.py`

---

# 报告 2：OpenCompass Summarizer 模块深入分析

## 概述

Summarizer 模块负责评估任务完成后的结果汇总、可视化和报告生成。模块包含多个汇总器实现，支持不同的结果展示和分析需求。

---

## 第一部分：文件清单与功能概览

### 1.1 Summarizer 目录结构

|文件|功能描述|类型|输出格式|
|---|---|---|---|
|`default.py`|默认汇总器，支持txt/csv/md多格式|核心|txt/csv/md|
|`default_subjective.py`|主观评估汇总器，处理多个judge模型|扩展|txt/csv/md|
|`circular.py`|圆形评估汇总器，多指标展示|专用|txt/csv/md|
|`multi_model.py`|多模型对比汇总器，Rich表格展示|可视化|Rich表格|
|`multi_faceted.py`|多维度汇总器，按profile分组输出|分组|CSV分别存储|
|`llm_compression.py`|LLM压缩评估汇总器，支持Pivot展示|数据处理|txt/csv/pivot|
|`needlebench.py`|Needle Bench长文本评估汇总器|专用|json/图表|
|`summarizer_pretrain.py`|预训练模型评估汇总器|专用|txt/json|
|`subjective/`|主观评估汇总器集合(25项)|模块|多种|
|`__init__.py`|模块导出|配置|-|

---

## 第二部分：核心类详细分析

### 2.1 DefaultSummarizer 默认汇总器

**文件位置：** `d:\project\opencompass_inner\opencompass\summarizers\default.py` (404行)

**类定义与初始化：**

python

`   ``` class DefaultSummarizer:     """默认汇总器 - OpenCompass标准评估结果汇总          处理流程：     1. 从work_dir/results/目录读取所有评估结果JSON文件     2. 按模型×数据集矩阵组织结果     3. 计算分组指标(平均、加权平均、调和平均等)     4. 生成txt/csv/markdown三种格式报告     5. 发送通知(可选Lark Bot)     """          def __init__(         self,         config: ConfigDict,         dataset_abbrs: Optional[List[str]] = None,         summary_groups: List = [],         prompt_db = None     ) -> None ```   `

**初始化参数详解（行41-58）：**

|参数|类型|说明|
|---|---|---|
|`config`|ConfigDict|完整评估配置，包含models、datasets、work_dir等|
|`dataset_abbrs`|List[str]|要在汇总表中显示的数据集名称，None则显示所有|
|`summary_groups`|List[Dict]|分组聚合配置，每个dict含name、subsets、weights等|
|`prompt_db`|-|已弃用，保留向后兼容|

**summary_groups 配置格式：**

python

`   ``` summary_groups = [     {         'name': 'mmlu',  # 分组名称         'subsets': ['mmlu_stem', 'mmlu_humanities', 'mmlu_social_science'],         'metric': 'accuracy',  # 可选：指定聚合指标，否则使用smart选择         'weights': {  # 可选：加权平均             'mmlu_stem': 0.5,             'mmlu_humanities': 0.25,             'mmlu_social_science': 0.25         }     },     {         'name': 'reasoning',         'subsets': ['codeexec', 'math'],         'harmonic_mean': True  # 可选：使用调和平均     } ] ```   `

### 2.2 DefaultSummarizer 核心方法

#### 2.2.1 _pick_up_results() 结果收集

**行号：** 67-135

**功能：** 从磁盘读取所有评估结果JSON文件，组织为三维数据结构

python

`   ``` def _pick_up_results(self):     """     返回四个字典：     1. raw_results: {model_abbr: {dataset_abbr: result_dict}}        - 包含所有字段(包括'details')的原始结果          2. parsed_results: {model_abbr: {dataset_abbr: {metric: score}}}        - 仅包含数值指标，用于汇总表展示        - 忽略METRIC_BLACKLIST中的字段('bp', 'sys_len', 'ref_len', 'type')          3. dataset_metrics: {dataset_abbr: [metric_names]}        - 各数据集包含的指标列表        - 按METRIC_WHITELIST排序(优先级)          4. dataset_eval_mode: {dataset_abbr: 'gen'|'ppl'|'ll'|'unknown'}        - 推理模式(生成/困惑度/Log-Likelihood)     """ ```   `

**核心逻辑（行86-135）：**

plaintext

`   ``` for each model_cfg:     model_abbr = get_abbr(model_cfg)     for each dataset_cfg:         dataset_abbr = get_abbr(dataset_cfg)         filepath = work_dir/results/{model_abbr}/{dataset_abbr}/...json                  if filepath exists:             result = load(filepath)             result.pop('details')  # 移除样本级详情                          raw_results[model_abbr][dataset_abbr] = result  # 原始结果                          # 解析为指标字典             for metric, score in result.items():                 if metric not in BLACKLIST and is_numeric(score):                     parsed_results[model_abbr][dataset_abbr][metric] = score                     dataset_metrics[dataset_abbr].append(metric)                          # 指标排序：按METRIC_WHITELIST优先级             dataset_metrics[dataset_abbr] = sorted(                 dataset_metrics[dataset_abbr],                 key=lambda m: WHITELIST.index(m) if m in WHITELIST else len(WHITELIST)             ) ```   `

**METRIC_WHITELIST (行19)：** 指定优先级顺序

python

`   ``` ['score', 'auc_score', 'accuracy', 'humaneval_pass@1', 'rouge1',   'avg_toxicity_score', 'bleurt_diff', 'matthews_correlation', 'truth', 'f1',   'exact_match', 'extract_rate'] ```   `

#### 2.2.2 _calculate_group_metrics() 分组聚合

**行号：** 137-245

**功能：** 根据summary_groups配置计算分组指标，支持多种聚合方法

python

`   ``` def _calculate_group_metrics(     self,     raw_results,     parsed_results,     dataset_metrics,     dataset_eval_mode ):     """为每个summary_group中的所有model计算聚合指标""" ```   `

**聚合策略详解（行163-235）：**

|聚合方法|触发条件|计算公式|
|---|---|---|
|**weighted_average**|`'weights'` in sg|Σ(score[i] * weight[i]) / Σ(weight[i])|
|**harmonic_mean**|`sg.get('harmonic_mean')=True`|n / Σ(1/score[i])|
|**standard_deviation**|`sg.get('std')=True`|sqrt(Σ(score[i]-mean)²/n)|
|**sum**|`sg.get('sum')=True`|Σ(score[i])|
|**naive_average**|默认|Σ(score[i]) / n|

**关键代码段（行179-244）：**

python

`   ``` for metric in scores:  # scores={'metric_name': {dataset@metric: value}}     if default_metric == 'standard_deviation':         avg = sum(scores[metric].values()) / len(scores[metric])         variance = sum((v - avg) ** 2 for v in scores[metric].values()) / len(scores[metric])         result[metric] = math.sqrt(variance)          elif default_metric == 'harmonic_mean':         numerator = len(scores[metric])         denominator = sum(1 / max(score, 1) for score in scores[metric].values())         result[metric] = numerator / denominator          elif default_metric == 'weighted_average':         numerator = sum(scores[metric][k] * sg['weights'][k] for k in sg['weights'] if sg['weights'][k] != 0)         denominator = sum(sg['weights'].values())         result[metric] = numerator / denominator          else:  # naive_average         result[metric] = sum(scores[metric].values()) / len(scores[metric])  # 更新global结果 raw_results[model_abbr][sg['name']] = result parsed_results[model_abbr][sg['name']] = result dataset_metrics[sg['name']].extend(group_metrics) ```   `

#### 2.2.3 _format_table() 表格格式化

**行号：** 247-297

**功能：** 将parsed_results转换为二维表格(dataset×metric×models)

python

`   ``` def _format_table(     self,     parsed_results,     dataset_metrics,     dataset_eval_mode,     required_dataset_abbrs=None,     skip_all_slash=False ) -> List[List[str]]: ```   `

**表格结构：**

plaintext

`   ``` ┌──────────────┬─────────┬────────┬──────────┬──────────┬──────────┐ │ dataset      │ version │ metric │ mode     │ model-A  │ model-B  │ ├──────────────┼─────────┼────────┼──────────┼──────────┼──────────┤ │ mmlu         │ a1b2c3  │ accuracy│ gen     │  85.23   │  87.45   │ │ mmlu         │ a1b2c3  │ f1     │ gen     │  82.11   │  84.67   │ │ ceval        │ d4e5f6  │ accuracy│ gen     │  73.45   │  75.89   │ └──────────────┴─────────┴────────┴──────────┴──────────┴──────────┘ ```   `

**核心逻辑（行247-297）：**

python

`   ``` # 确定要显示的(dataset, metric)对 if required_dataset_abbrs is None:     # 显示所有     for dataset_abbr in dataset_abbrs:         for metric in dataset_metrics[dataset_abbr]:             summarizer_dataset_abbrs.append((dataset_abbr, metric))     # 加上分组结果     for dataset_abbr in dataset_metrics:         for metric in dataset_metrics[dataset_abbr]:             if (dataset_abbr, metric) not in summarizer_dataset_abbrs:                 summarizer_dataset_abbrs.append((dataset_abbr, metric)) else:     # 按指定顺序     for item in required_dataset_abbrs:         if isinstance(item, str):             summarizer_dataset_abbrs.append((item, None))  # None表示用默认指标         else:             summarizer_dataset_abbrs.append((item[0], item[1]))  # (dataset, metric)  # 构建表格 table = [['dataset', 'version', 'metric', 'mode'] + model_abbrs] for dataset_abbr, metric in summarizer_dataset_abbrs:     if metric is None:         metric = dataset_metrics[dataset_abbr][0]  # 使用首个指标(优先级最高)          row = [dataset_abbr, prompt_version.get(dataset_abbr, '-'), metric, dataset_eval_mode.get(dataset_abbr, '-')]     for model_abbr in model_abbrs:         if dataset_abbr in parsed_results[model_abbr] and metric in parsed_results[model_abbr][dataset_abbr]:             row.append('{:.02f}'.format(parsed_results[model_abbr][dataset_abbr][metric]))         else:             row.append('-')     table.append(row) ```   `

#### 2.2.4 summarize() 主流程

**行号：** 376-403

**功能：** 完整汇总执行流程

python

`   ``` def summarize(     self,     output_path: str = None,     time_str: str = datetime.now().strftime('%Y%m%d_%H%M%S') ) -> None:     """     执行流程：     1. _pick_up_results() - 读取所有JSON结果     2. _calculate_group_metrics() - 计算分组指标     3. _format_table() - 生成表格     4. _format_raw_txt() - 生成原始文本     5. 屏幕输出表格     6. _output_to_file() - 保存为txt/csv/md文件     7. 发送Lark通知(可选)     """ ```   `

#### 2.2.5 _output_to_file() 文件输出

**行号：** 327-374

**功能：** 将结果输出为多种格式

python

`   ``` def _output_to_file(     self,     output_path: str,     time_str: str,     table: List[List[str]],     raw_txts: str ) -> None: ```   `

**输出文件格式：**

|格式|文件名|用途|
|---|---|---|
|TXT|`summary_{time_str}.txt`|可读性最好，包含多种展示格式|
|CSV|`summary_{time_str}.csv`|易导入Excel/Python分析|
|MD|`summary_{time_str}.md`|GitHub/Wiki友好，可在线渲染|

**TXT文件结构（行343-362）：**

plaintext

`   ``` {time_str} tabulate format ^^^^...^^^^^(128个^) ┌─────────┬──────────┬─────────┐ │ dataset │ accuracy │ model-A │ └─────────┴──────────┴─────────┘ ...  $$$$...$$$$ THIS IS A DIVIDER $$$$...$$$  csv format ^^^^...^^^^^ dataset,accuracy,model-A mmlu,85.23,85.23 ...  $$$$...$$$$ THIS IS A DIVIDER $$$$...$$$  markdown format ^^^^...^^^^^ | dataset | accuracy | model-A | |---------|----------|---------| | mmlu    | 85.23    | 85.23   | ...  $$$$...$$$$ THIS IS A DIVIDER $$$$...$$$  raw format ^^^^...^^^^^ ------------------------------- Model: model-A mmlu: {'accuracy': 85.23, ...} ... ```   `

---

### 2.3 DefaultSubjectiveSummarizer 主观评估汇总器

**文件位置：** `d:\project\opencompass_inner\opencompass\summarizers\default_subjective.py` (408行)

**特殊功能：** 支持多个Judge模型的主观评估结果汇总

python

`   ``` class DefaultSubjectiveSummarizer(DefaultSummarizer):     """主观评估汇总器          区别于DefaultSummarizer：     1. 支持eval_models（被评估模型）列表     2. 支持judge_models（多个评判模型）     3. 结果路径含judge_abbr: {dataset}_{judged-by--judge_abbr}     4. 支持base_models聚合(平均不同base model的结果)     """ ```   `

**初始化差异（行42-71）：**

python

`   ``` def __init__(self, config, dataset_abbrs=None, summary_groups=[], prompt_db=None):     self.eval_model_cfgs = self.cfg['eval']['partitioner']['models']  # 被评估模型     self.eval_model_abbrs = [model_abbr_from_cfg(m) for m in self.eval_model_cfgs]     self.judge_models = self.cfg.get('judge_models', None)  # 多个Judge配置     # ...其他初始化 ```   `

**_pick_up_results()差异（行73-150）：**

python

`   ``` def _pick_up_results(self, judge_abbr):  # 需要指定judge_abbr     """     查询路径包含judge信息：     origin_path = results/{model_abbr}/{dataset_abbr}/...     actual_path = results/{base_model_abbr}_{dataset_abbr}_judged-by--{judge_abbr}/...     """          # 对于多个base_models，计算移动平均：     for idx, base_model_abbr in enumerate(base_models_list):         # 加权平均：(prev * idx + new) / (idx + 1)         raw_results[model_abbr][dataset_abbr][key] = \             (raw_results[model_abbr][dataset_abbr][key] * idx + value) / (idx + 1) ```   `

---

### 2.4 CircularSummarizer 圆形评估汇总器

**文件位置：** `d:\project\opencompass_inner\opencompass\summarizers\circular.py` (58行)

**特殊功能：** 支持多种circular metrics同时展示

python

`   ``` class CircularSummarizer(DefaultSummarizer):     """圆形评估汇总器 - 处理多种circular metrics"""          def __init__(self, config, dataset_abbrs=None, summary_groups=[],                   prompt_db=None, metric_types=None):         # metric_types: ['acc_4', 'acc_1', 'vote_4', 'vote_1', ...]         self.metric_types = metric_types  # 指定要显示的metrics ```   `

**表格格式（行22-57）：**

plaintext

`   ``` ┌──────────┬─────────┬──────┬────────────┬────────────┬────────────┐ │ dataset  │ version │ mode │ model-A    │            │ model-B    │ ├──────────┼─────────┼──────┼─────┬──────┼─────┬──────┼─────┬──────┤ │          │         │      │acc_4│acc_1 │acc_4│acc_1 │acc_4│acc_1 │ ├──────────┼─────────┼──────┼─────┼──────┼─────┼──────┼─────┼──────┤ │ arc_cir  │ a1b2c3  │ gen  │ 85.2│ 88.3 │ 87.5│ 89.1 │ 83.4│ 86.7 │ └──────────┴─────────┴──────┴─────┴──────┴─────┴──────┴─────┴──────┘ ```   `

---

### 2.5 LLMCompressionSummarizer LLM压缩汇总器

**文件位置：** `d:\project\opencompass_inner\opencompass\summarizers\llm_compression.py` (201行)

**特殊功能：** 支持Pivot表格，便于对比BPC指标

python

`   ``` class LLMCompressionSummarizer(DefaultSummarizer):     """LLM压缩评估汇总器"""          def _format_table_pivot(self, table, decimals=4) -> pd.DataFrame:         """         原始表格：         dataset, version, metric, mode, model-A, model-B                  Pivot后：         metric, version, model, commoncraw, python, arxiv_math, average         BPC    , v1      , A    , 2.3456  , 1.2345, 1.5678    , 1.7159         BPC    , v1      , B    , 2.2345  , 1.1234, 1.4567    , 1.6049         """ ```   `

**输出文件：**

- `summary_{time_str}.txt` - 标准格式
- `summary_{time_str}.csv` - 标准格式
- `summary_pivot_{time_str}.csv` - Pivot后的数据框

---

### 2.6 MultiFacetedSummarizer 多维度汇总器

**文件位置：** `d:\project\opencompass_inner\opencompass\summarizers\multi_faceted.py` (47行)

**特殊功能：** 为不同profile生成独立的CSV文件

python

`   ``` class MultiFacetedSummarizer(DefaultSummarizer):     """多维度汇总器 - 按profile分别生成报告"""          def __init__(self, config, dataset_abbrs_list=None, summary_groups=[]):         # dataset_abbrs_list: [         #   {'name': 'reasoning', 'dataset_abbrs': ['mmlu', 'ceval', ...]},         #   {'name': 'knowledge', 'dataset_abbrs': ['triviaqa', ...]},         # ]         self.dataset_abbrs_list = dataset_abbrs_list          def summarize(self, output_path=None, time_str=...):         """为每个profile生成独立CSV"""         for profile in dataset_abbrs_list:             output_csv_path = f'{work_dir}/summary/summary_{time_str}/{profile_name}.csv'             # 调用_format_table(required_dataset_abbrs=profile['dataset_abbrs']) ```   `

---

### 2.7 PretrainSummarizer 预训练汇总器

**文件位置：** `d:\project\opencompass_inner\opencompass\summarizers\summarizer_pretrain.py` (339行)

**特殊功能：** 为预训练模型评估设计，支持多种预训练指标

python

`   ``` class PretrainSummarizer:     """预训练模型评估汇总器"""          def summarize(self, output_path=None, time_str=...):         """         特点：         1. 直接存储scores为列表(不是字典)         2. 支持pass@1指标(代码评估)         3. 生成json和txt报告         """ ```   `

---

## 第三部分：数据流与调用关系

### 3.1 Summarizer 在评估流程中的位置

plaintext

`   ``` ┌───────────────────────────────────────────┐ │   OpenCompass 评估任务完成                  │ │   work_dir/results/{model}/{dataset}/*.json│ └──────────────────┬──────────────────────────┘                    │         ┌──────────▼──────────┐         │  Summarizer.summarize()         │  选择合适的汇总器     │         └──────────┬──────────┘                    │     ┌──────────────┼──────────────┐     │              │              │     ▼              ▼              ▼ DefaultSummarizer | DefaultSubjectiveSummarizer | 其他     │              │              │     ▼              ▼              ▼   _pick_up_results() → parsed_results   _calculate_group_metrics() → 分组指标   _format_table() → 表格数据   _format_raw_txt() → 原始文本                       │         ┌──────────▼──────────┐         │  输出文件生成        │         │ txt/csv/md/json     │         │ summary/目录        │         └─────────────────────┘ ```   `

### 3.2 数据转换流程

plaintext

`   ``` 磁盘JSON文件   results/   ├── model-A/   │   ├── mmlu/   │   │   └── result.json: {   │   │       'accuracy': 85.23,   │   │       'f1': 82.11,   │   │       'details': [...]   │   │     }   │   └── ceval/   │       └── result.json: {   │           'accuracy': 73.45,   │           ...   │         }   └── model-B/       └── ...         │         ▼   _pick_up_results()      raw_results = {     'model-A': {       'mmlu': {'accuracy': 85.23, 'f1': 82.11},       'ceval': {'accuracy': 73.45, ...}     },     'model-B': {...}   }      parsed_results = {     'model-A': {       'mmlu': {'accuracy': 85.23, 'f1': 82.11},  # 仅保留数值       'ceval': {'accuracy': 73.45}     }   }      dataset_metrics = {     'mmlu': ['accuracy', 'f1'],  # 按优先级排序     'ceval': ['accuracy']   }         │         ▼   _calculate_group_metrics()      # 添加聚合行   parsed_results['model-A']['mmlu_avg'] = 83.67  # (85.23 + 82.11) / 2         │         ▼   _format_table()      [     ['dataset', 'version', 'metric', 'mode', 'model-A', 'model-B'],     ['mmlu',    'hash1',   'accuracy', 'gen', '85.23',  '87.45'],     ['mmlu',    'hash1',   'f1',       'gen', '82.11',  '84.67'],     ['ceval',   'hash2',   'accuracy', 'gen', '73.45',  '75.89'],     ['mmlu_avg','hash1',   'accuracy', 'gen', '83. ```   `