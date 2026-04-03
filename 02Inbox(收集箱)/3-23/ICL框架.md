## 报告 1：ICL框架（openicl/）深入源码分析

### 第一步：模块目录结构与文件概览

OpenCompass ICL框架位于 `d:\project\opencompass_inner\opencompass\openicl\`，包含以下核心子模块：

|子模块|文件数|核心功能|
|---|---|---|
|**icl_inferencer/**|17|推理引擎：文本生成、困惑度、多种评估策略|
|**icl_retriever/**|12|检索引擎：零样本、K-近邻、动态检索等|
|**icl_evaluator/**|19|评估器：准确率、F1、RougeScore等指标计算|
|**utils/**|3|工具函数：日志、提示符处理|
|**根目录文件**|5|核心模块：PromptTemplate、DatasetReader、RawPromptTemplate、**init**.py|

#### 文件详细列表

**根目录文件 (d:\project\opencompass_inner\opencompass\openicl/):**

- `icl_prompt_template.py` (260行) - 提示模板渲染和组装
- `icl_raw_prompt_template.py` (3.6KB) - 原始消息格式模板
- `icl_dataset_reader.py` (290行) - 数据集读取和数据分割
- `__init__.py` - 模块导出

**Inferencer模块 (icl_inferencer/):**

- `icl_base_inferencer.py` (210行) - 基类及输出处理器
- `icl_gen_inferencer.py` (362行) - 文本生成推理 **[核心]**
- `icl_ppl_inferencer.py` (188行) - 困惑度评估 **[核心]**
- `icl_chat_inferencer.py` (274行) - 多轮对话推理
- `icl_chatml_inferencer.py` (330行) - ChatML格式推理
- `icl_clp_inferencer.py` (152行) - 条件概率推理
- `icl_agent_inferencer.py` (4.9KB) - Agent推理
- `icl_attack_inferencer.py` (9.1KB) - 对抗攻击推理
- `icl_sc_inferencer.py` (8.5KB) - 自洽性推理
- `icl_tot_inferencer.py` (15.5KB) - 思维树推理
- `icl_ll_inferencer.py` (8.0KB) - 对数似然推理
- `icl_ppl_only_inferencer.py` (7.1KB) - 纯PPL推理
- `icl_inference_ppl_only_inferencer.py` (9.3KB) - 推理PPL推理
- `icl_mink_percent_inferencer.py` (7.2KB) - 最小K百分比推理
- `icl_sw_ce_loss_inferencer.py` (12.6KB) - 滑窗交叉熵推理

**Retriever模块 (icl_retriever/):**

- `icl_base_retriever.py` (325行) - 检索基类及辅助方法
- `icl_zero_retriever.py` (30行) - 零样本检索
- `icl_fix_k_retriever.py` (52行) - 固定K检索
- `icl_random_retriever.py` (1.3KB) - 随机检索
- `icl_topk_retriever.py` (206行) - TopK检索 **[核心]**
- `icl_sliding_k_retriever.py` (2.7KB) - 滑窗K检索
- `icl_bm25_retriever.py` (3.1KB) - BM25检索
- `icl_mdl_retriever.py` (8.3KB) - 最小描述长度检索
- `icl_dpp_retriever.py` (4.6KB) - 行列式点过程检索
- `icl_votek_retriever.py` (3.7KB) - 投票K检索

---

### 第二步：核心类详细分析

#### A. Inferencer 子模块

##### BaseInferencer 基类

**文件位置:** `d:\project\opencompass_inner\opencompass\openicl\icl_inferencer\icl_base_inferencer.py` (行 1-86)

**类定义:** `class BaseInferencer`

|属性|类型|默认值|说明|
|---|---|---|---|
|`model`|BaseModel|None|推理使用的模型|
|`max_seq_len`|int|None|最大序列长度|
|`batch_size`|int|1|批处理大小|
|`output_json_filepath`|str|'./icl_inference_output'|输出路径|
|`output_json_filename`|str|'predictions'|输出文件名|

**方法签名:**

python

`   ``` def __init__(     self,     model,     max_seq_len: Optional[int] = None,     batch_size: Optional[int] = 1,     output_json_filepath: Optional[str] = './icl_inference_output',     output_json_filename: Optional[str] = 'predictions',     fix_id_list: Optional[List[int]] = None,     **kwargs, ) -> None ```   `

**关键代码逻辑 (行 31-54):**

- 验证 `fix_id_list` 不为空（已废弃，应传递给 `FixKRetriever`）
- 保存模型、序列长度、批大小等配置
- 获取是否为主进程标志（分布式训练用）
- 创建输出目录

**核心接口方法:**

python

`   ``` def inference(     self,     retriever: BaseRetriever,     ice_template: Optional[PromptTemplate] = None,     prompt_template: Optional[PromptTemplate] = None,     output_json_filepath: Optional[str] = None,     output_json_filename: Optional[str] = None) -> List: ```   `

- **返回值:** 推理结果列表
- **实现:** 子类需重写此方法

**输出处理器类:**

|处理器类|用途|关键方法|
|---|---|---|
|`GenInferencerOutputHandler` (行 101-131)|生成式任务输出|`write_to_json()`, `save_results()`|
|`PPLInferencerOutputHandler` (行 133-172)|PPL评估输出|`save_ice()`, `save_predictions()`, `save_prompt_and_ppl()`|
|`CLPInferencerOutputHandler` (行 174-209)|条件概率输出|`save_prompt_and_condprob()`|

---

##### GenInferencer 文本生成推理

**文件位置:** `d:\project\opencompass_inner\opencompass\openicl\icl_inferencer\icl_gen_inferencer.py` (行 27-362)

**类定义:** `@ICL_INFERENCERS.register_module() class GenInferencer(BaseInferencer)`

**构造参数:**

|参数|类型|默认值|说明|
|---|---|---|---|
|`model`|BaseModel|-|推理模型|
|`max_out_len`|int|-|最大生成长度 **[必需]**|
|`stopping_criteria`|List[str]|[]|停止标准|
|`max_seq_len`|int|None|最大输入长度|
|`min_out_len`|int|None|最小生成长度|
|`batch_size`|int|1|批大小|
|`gen_field_replace_token`|str|''|生成字段替换令牌|
|`save_every`|int|1|每N步保存一次|

**inference() 完整流程 (行 86-362):**

plaintext

`   ``` 1. 初始化输出处理器    └─ GenInferencerOutputHandler()  2. 获取检索结果    └─ ice_idx_list = retriever.retrieve()    └─ 返回: [[idx1, idx2, ...], [idx3, idx4, ...], ...]  (每个测试样本对应的检索示例索引)  3. 生成提示词列表    └─ get_generation_prompt_list_from_retriever_indices()    │   ├─ 遍历检索索引列表    │   ├─ 调用 retriever.generate_ice() 生成上文示例    │   └─ 调用 retriever.generate_prompt_for_generate_task() 生成完整提示    └─ 与黄金答案配对 (如存在)  4. 检查临时文件，支持断点续传    └─ tmp_json_filepath = 'tmp_' + output_json_filename    └─ 如存在则加载已处理结果  5. 构建DataLoader进行批处理    └─ dataloader = get_dataloader(prompt_list[index:], batch_size)    └─ 支持动态批大小处理  6. 逐批推理核心循环 (行 143-235)    ├─ 解析模型输入: parsed_entries = model.parse_template(entry, mode='gen')    ├─ 模型生成: results = model.generate_from_template(    │   entry, max_out_len=self.max_out_len, **extra_gen_kwargs)    ├─ 批量保存结果到output_handler    ├─ 定期保存临时文件 (每save_every步)    └─ 统计样本数量  7. 输出最终结果    ├─ 主进程创建输出目录    ├─ 将结果写入JSON文件    └─ 删除临时文件  返回: predictions 列表 [str, str, ...] ```   `

**代码片段 (行 150-183):**

python

`   ``` # 5.1 检查模型生成方法签名，动态添加参数 extra_gen_kwargs = {} sig = inspect.signature(self.model.generate) if 'stopping_criteria' in sig.parameters:     extra_gen_kwargs['stopping_criteria'] = self.stopping_criteria if 'min_out_len' in sig.parameters:     extra_gen_kwargs['min_out_len'] = self.min_out_len  # 5.2 无梯度推理 with torch.no_grad():     parsed_entries = self.model.parse_template(entry, mode='gen')     results = self.model.generate_from_template(         entry, max_out_len=self.max_out_len, **extra_gen_kwargs)     generated = results ```   `

---

##### PPLInferencer 困惑度评估

**文件位置:** `d:\project\opencompass_inner\opencompass\openicl\icl_inferencer\icl_ppl_inferencer.py` (行 1-188)

**类定义:** `@ICL_INFERENCERS.register_module() class PPLInferencer(BaseInferencer)`

**构造参数:**

|参数|类型|默认值|说明|
|---|---|---|---|
|`model`|BaseModel|-|推理模型|
|`max_seq_len`|int|None|最大序列长度|
|`batch_size`|int|1|批大小|
|`labels`|List|None|候选标签列表|

**inference() 完整流程 (行 58-188):**

plaintext

`   ``` 1. 初始化输出处理器和数据结构    └─ output_handler = PPLInferencerOutputHandler()    └─ ppl = []  # 存储各标签的困惑度    └─ ice = []  # 存储上文示例  2. 获取检索结果    └─ ice_idx_list = retriever.retrieve()  3. 获取标签列表    ├─ 若labels为None，从模板中提取    └─ labels = retriever.get_labels(ice_template, prompt_template)  4. 为所有测试样本生成上文示例 (行 88-90)    └─ for idx in range(len(ice_idx_list)):          ice.append(retriever.generate_ice(...))    └─ output_handler.save_ice(model.parse_template(ice, mode='ppl'))  5. 对每个标签计算困惑度 (行 93-168)    ├─ for label in labels:    │   ├─ 为所有样本生成该标签的提示词    │   ├─ 检查并截断过长提示 (最大序列长度约束, 行 114-120)    │   ├─ 可选：归一化处理 (行 122-137)    │   │   └─ 分离上文和答案    │   │   └─ 计算归一化困惑度 = PPL(context+answer) - PPL(normstr+answer)    │   └─ 批处理计算PPL (行 148-167)    │       ├─ sub_res = model.get_ppl_from_template(sub_prompt_list)    │       └─ 保存prompt和PPL值    └─ ppl.append(sub_ppl_list)  6. 选择最小PPL类作为预测 (行 171-174)    └─ predictions = [labels[argmin(ppl)] for ppl in zip(*ppl)]  7. 保存黄金答案和输出结果 (行 177-185)    ├─ 若数据集包含输出列，保存为gold答案    └─ 主进程写入JSON文件  返回: predictions 列表 ```   `

**关键代码片段 (行 148-167):**

python

`   ``` # 5.2 批处理计算PPL for idx in trange(0, len(prompt_list), self.batch_size):     sub_prompt_list = prompt_list[idx:idx + self.batch_size]     with torch.no_grad():         if normalizing_str is not None:             # 归一化模式             res1 = self.model.get_ppl_from_template(                 sub_prompt_list, mask_length=sub_context_length_list)             res2 = self.model.get_ppl_from_template(                 sub_normalizing_prompt_list, mask_length=sub_normalizing_context_length_list)             sub_res = res1 - res2         else:             # 标准PPL模式             sub_res = self.model.get_ppl_from_template(sub_prompt_list).tolist()                  # 保存结果         for res, prompt in zip(sub_res, self.model.parse_template(sub_prompt_list, mode='ppl')):             sub_ppl_list.append(res) ```   `

---

##### 其他Inferencer类型总览

|类名|文件|用途|关键参数|
|---|---|---|---|
|**ChatInferencer**|icl_chat_inferencer.py|多轮对话推理|`infer_mode`: 'last'/'every'/'every_with_gt'|
|**ChatMLInferencer**|icl_chatml_inferencer.py|ChatML格式对话|`stopping_criteria`, `max_out_len`|
|**CLPInferencer**|icl_clp_inferencer.py|条件对数概率|-|
|**PPLOnlyInferencer**|icl_ppl_only_inferencer.py|纯PPL评估|-|
|**InferencePPLOnlyInferencer**|icl_inference_ppl_only_inferencer.py|推理阶段的PPL|-|
|**AgentInferencer**|icl_agent_inferencer.py|智能体推理|`agent_role`, `max_steps`|
|**AttackInferencer**|icl_attack_inferencer.py|对抗攻击评估|`adv_key`, `metric_key`|
|**SCInferencer**|icl_sc_inferencer.py|自洽性推理|`sc_size`, `infer_type`|
|**TOTInferencer**|icl_tot_inferencer.py|思维树推理|`method_generate`, `method_evaluate`, `method_select`|
|**LLInferencer**|icl_ll_inferencer.py|对数似然推理|-|
|**MinKPercentInferencer**|icl_mink_percent_inferencer.py|最小K%评估|-|
|**SWCELossInferencer**|icl_sw_ce_loss_inferencer.py|滑窗交叉熵|-|

---

#### B. Retriever 子模块

##### BaseRetriever 基类

**文件位置:** `d:\project\opencompass_inner\opencompass\openicl\icl_retriever\icl_base_retriever.py` (行 1-325)

**类定义:** `class BaseRetriever`

**构造参数:**

|参数|类型|默认值|说明|
|---|---|---|---|
|`dataset`|BaseDataset|-|数据集|
|`ice_separator`|str|'\n'|上文示例间的分隔符|
|`ice_eos_token`|str|'\n'|上文的结束标记|
|`ice_num`|int|1|上文示例数量|

**属性:**

python

`   ``` index_ds = None      # 训练集（用于检索） test_ds = None       # 测试集 dataset_reader       # DatasetReader实例 ice_separator        # 示例间分隔符 ice_eos_token        # 结束令牌 ice_num              # 示例数量 is_main_process      # 分布式训练标志 ```   `

**核心方法:**

|方法|行号|签名|返回值|说明|
|---|---|---|---|---|
|`retrieve()`|43|`retrieve() -> List[List[int]]`|检索索引列表|抽象方法，子类实现|
|`get_labels()`|47|`get_labels(ice_template, prompt_template) -> List[str]`|标签列表|从模板提取标签|
|`generate_ice()`|73|`generate_ice(idx_list, ice_template) -> str`|格式化上文|生成上文示例字符串|
|`generate_label_prompt()`|114|`generate_label_prompt(idx, ice, label, ...) -> str`|含标签的提示|PPL评估用|
|`generate_prompt_for_generate_task()`|157|`generate_prompt_for_generate_task(idx, ice, ...) -> str`|生成任务提示|生成式任务用|

**generate_ice() 实现 (行 73-112):**

python

`   ``` def generate_ice(     self,     idx_list: List[int],     ice_template: Optional[PromptTemplate] = None) -> str:          if ice_template is None:         assert len(idx_list) == 0, '必须指定ice_template'          # 根据模板类型设置分隔符     if ice_template.prompt_type == 'meta':         ice_separator, ice_eos_token = '', ''     else:         ice_separator = self.ice_separator         ice_eos_token = self.ice_eos_token          # 为每个索引生成示例     generated_ice_list = []     for idx in idx_list:         generated_ice_list.append(             ice_template.generate_ice_item(                 self.index_ds[idx],                 self.index_ds[idx][self.dataset_reader.output_column]))          # 组合示例（支持PromptList和字符串）     if isinstance(generated_ice_list[0], PromptList):         # PromptList模式         generated_ice = []         for ice in generated_ice_list:             generated_ice += ice + ice_separator         generated_ice.append(ice_eos_token)     else:         # 字符串模式         generated_ice = ice_separator.join(             generated_ice_list) + ice_eos_token          return generated_ice ```   `

---

##### ZeroRetriever 零样本检索

**文件位置:** `d:\project\opencompass_inner\opencompass\openicl\icl_retriever\icl_zero_retriever.py`

**类定义:** `@ICL_RETRIEVERS.register_module() class ZeroRetriever(BaseRetriever)`

**用途:** 不进行任何检索，为所有测试样本返回空示例列表

**实现 (行 22-29):**

python

`   ``` def __init__(self, dataset, ice_eos_token: Optional[str] = '') -> None:     super().__init__(dataset, '', ice_eos_token, 0)  def retrieve(self, id_list: List[int] = None) -> List[List]:     """返回空检索索引列表"""     if id_list is not None:         get_logger().warning('id_list is not empty, but will be ignored.')     rtr_idx_list = [[] for _ in range(len(self.test_ds))]     return rtr_idx_list ```   `

**返回格式:** `[[], [], [], ...]` (N个空列表，N为测试集大小)

---

##### FixKRetriever 固定K检索

**文件位置:** `d:\project\opencompass_inner\opencompass\openicl\icl_retriever\icl_fix_k_retriever.py`

**类定义:** `@ICL_RETRIEVERS.register_module() class FixKRetriever(BaseRetriever)`

**用途:** 为所有测试样本返回相同的K个检索示例

**构造参数:**

|参数|类型|说明|
|---|---|---|
|`dataset`|BaseDataset|数据集|
|`fix_id_list`|List[int]|固定的示例索引列表|

**实现 (行 34-51):**

python

`   ``` def __init__(self,              dataset,              fix_id_list: List[int],              ice_separator: Optional[str] = '\n',              ice_eos_token: Optional[str] = '\n',              ice_num: Optional[int] = 1) -> None:     super().__init__(dataset, ice_separator, ice_eos_token, ice_num)     self.fix_id_list = fix_id_list  def retrieve(self):     """每个测试样本返回相同的fix_id_list"""     num_idx = len(self.index_ds)     for idx in self.fix_id_list:         assert idx < num_idx, f'Index {idx} out of range {num_idx}'          rtr_idx_list = []     for _ in trange(len(self.test_ds), disable=not self.is_main_process):         rtr_idx_list.append(self.fix_id_list)     return rtr_idx_list ```   `

**返回格式:** `[[1, 5, 7], [1, 5, 7], ..., [1, 5, 7]]` (M个相同的列表，M为测试集大小)

---

##### TopkRetriever K近邻检索 **[核心实现]**

**文件位置:** `d:\project\opencompass_inner\opencompass\openicl\icl_retriever\icl_topk_retriever.py` (行 22-206)

**类定义:** `@ICL_RETRIEVERS.register_module() class TopkRetriever(BaseRetriever)`

**用途:** 基于向量相似度的K近邻检索，使用SentenceTransformer+FAISS

**构造参数:**

|参数|类型|默认值|说明|
|---|---|---|---|
|`sentence_transformers_model_name`|str|'all-mpnet-base-v2'|向量编码模型|
|`tokenizer_name`|str|'gpt2-xl'|分词器|
|`batch_size`|int|1|批处理大小|

**初始化流程 (行 48-84):**

plaintext

`   ``` 1. 加载SentenceTransformer模型    └─ 移动到GPU或CPU  2. 获取测试集输入    └─ gen_datalist = dataset_reader.generate_input_field_corpus(test_ds)  3. 初始化分词器    └─ AutoTokenizer.from_pretrained(tokenizer_name)    └─ 配置padding和padding_side  4. 编码测试数据    └─ DatasetEncoder: 将文本编码为token IDs + attention_mask  5. 创建DataLoader    └─ DataCollatorWithPaddingAndCuda用于GPU批处理  6. 创建FAISS索引    └─ create_index(): 编码训练集并构建IndexIDMap    └─ IndexFlatIP: 内积相似度搜索 ```   `

**检索方法 (行 86-206):**

python

`   ``` def create_index(self):     """为训练集构建FAISS索引"""     import faiss          # 1. 生成训练集输入语料     select_datalist = self.dataset_reader.generate_input_field_corpus(         self.index_ds)          # 2. 编码     encode_datalist = DatasetEncoder(select_datalist, tokenizer=...)     dataloader = DataLoader(encode_datalist, batch_size=..., collate_fn=...)          # 3. 构建FAISS索引     index = faiss.IndexIDMap(         faiss.IndexFlatIP(embedding_dim))          # 4. 编码并添加向量到索引     embeddings = forward(dataloader, tokenizer)  # 获取embed向量     index.add_with_ids(embeddings, ids)          return index  def retrieve(self, k: Optional[int] = 1):     """为每个测试样本找到K近邻"""     # 1. 获取测试集向量     test_embeddings = forward(test_dataloader, tokenizer)          # 2. 搜索K近邻     distances, indices = index.search(test_embeddings, k)          # 3. 返回检索索引列表     return [[idx1, idx2, ...], [idx3, idx4, ...], ...] ```   `

**返回格式:** `[[相似最高的k个训练索引], [相似最高的k个训练索引], ...]`

---

##### 其他Retriever类型总览

|类名|文件|检索策略|关键参数|
|---|---|---|---|
|**ZeroRetriever**|icl_zero_retriever.py|无检索|-|
|**FixKRetriever**|icl_fix_k_retriever.py|固定K个示例|`fix_id_list`|
|**RandomRetriever**|icl_random_retriever.py|随机选择K个|`k`|
|**TopkRetriever**|icl_topk_retriever.py|向量相似度TopK|`sentence_transformers_model_name`, `k`|
|**SlidingWindowRetriever**|icl_sliding_k_retriever.py|滑窗选择相邻K个|`k`|
|**BM25Retriever**|icl_bm25_retriever.py|BM25文本匹配|`k`|
|**MDLRetriever**|icl_mdl_retriever.py|最小描述长度|`k`, `model_name`|
|**DPPRetriever**|icl_dpp_retriever.py|行列式点过程采样|`k`|
|**VotekRetriever**|icl_votek_retriever.py|投票机制选择|`k`, `vote_k`|

---

#### C. PromptTemplate 模块

**文件位置:** `d:\project\opencompass_inner\opencompass\openicl\icl_prompt_template.py` (行 1-260)

**类定义:** `@ICL_PROMPT_TEMPLATES.register_module() class PromptTemplate`

**功能:** 模板化提示词生成，支持元模式（begin/round/end）和标签模式

**构造参数:**

|参数|类型|默认值|说明|
|---|---|---|---|
|`template`|Dict or str|-|模板定义|
|`ice_token`|str|None|上文示例替换标记|
|`sep_token`|str|None|分隔符标记|

**模板类型:**

|类型|结构|用途|示例|
|---|---|---|---|
|**meta提示**|Dict with keys: 'begin', 'round', 'end'|复杂多部分提示|ChatML格式|
|**标签提示**|Dict with label keys: 'A', 'B', 'C'|分类任务标签|MMLU多选题|
|**字符串提示**|直接字符串|简单模板|"{input}\nAnswer: {output}"|

**核心方法:**

|方法|行号|输入|输出|说明|
|---|---|---|---|---|
|`generate_ice_item()`|71|entry, label|str/PromptList|生成单个上文示例|
|`generate_label_prompt_item()`|-|entry, ice, label|str/PromptList|生成含标签的提示|
|`generate_item()`|-|entry, ice_field_replace_token|str/PromptList|生成完整提示|
|`_encode_template()`|209|prompt_template, ice|str/PromptList|编码模板为最终格式|

**_encode_template() 实现 (行 209-259):**

python

`   ``` def _encode_template(self, prompt_template, ice: bool) -> PromptType:     """将模板编码为字符串或PromptList"""          if isinstance(prompt_template, str):         return prompt_template          prompt = PromptList()          # 1. 添加begin部分（仅非ice模式）     if 'begin' in prompt_template and not ice:         prompt.append(dict(section='begin', pos='begin'))         prompt += prompt_template['begin']  # 支持列表或单字符串         prompt.append(dict(section='begin', pos='end'))          # 2. 添加round部分（主体内容）     if ice:         prompt.append(dict(section='ice', pos='begin'))     else:         prompt.append(dict(section='round', pos='begin'))     prompt += prompt_template['round']     if ice:         prompt.append(dict(section='ice', pos='end'))     else:         prompt.append(dict(section='round', pos='end'))          # 3. 添加end部分（仅非ice模式）     if 'end' in prompt_template and not ice:         prompt.append(dict(section='end', pos='end'))         prompt += prompt_template['end']         prompt.append(dict(section='end', pos='end'))          return prompt  # PromptList格式 ```   `

**PromptList结构:**

python

`   ``` PromptList = List[Dict[str, str]]  # 示例： [     {'section': 'begin', 'pos': 'begin'},     {'role': 'HUMAN', 'prompt': 'Question: {input}'},     {'role': 'ASSISTANT', 'prompt': '{output}'},     {'section': 'begin', 'pos': 'end'},     {'section': 'round', 'pos': 'begin'},     ...     {'section': 'round', 'pos': 'end'},     {'section': 'end', 'pos': 'end'}, ] ```   `

**generate_ice_item() 实现 (行 71-100):**

python

`   ``` def generate_ice_item(self, entry: Dict, label: Hashable) -> PromptType:     """生成单个上文示例"""          # 1. 选择对应的模板部分     if isinstance(self.template, str) or self.prompt_type == 'meta':         tp = self.template     else:         # 标签模式：template['A'], template['B'], ...         tp = self.template[label]          # 2. 编码模板     tp = self._encode_template(tp, ice=True)          # 3. 移除分隔符     if self.sep_token is not None:         tp.replace(self.sep_token, '')          # 4. 移除ice_token (上文中不需要此标记)     if self.ice_token is not None:         tp = tp.replace(self.ice_token, '')          # 5. 使用entry数据填充模板     if isinstance(tp, str):         tp = safe_format(tp, **entry)     else:         # PromptList模式         for item in tp:             if 'prompt' in item:                 item['prompt'] = safe_format(item['prompt'], **entry)          return tp ```   `

---

#### D. DatasetReader 模块

**文件位置:** `d:\project\opencompass_inner\opencompass\openicl\icl_dataset_reader.py` (行 1-290)

**类定义:** `@ICL_DATASET_READERS.register_module() class DatasetReader`

**功能:** 数据集读取、规范化、数据划分

**构造参数:**

|参数|类型|默认值|说明|
|---|---|---|---|
|`dataset`|Dataset/DatasetDict/str|-|数据集或路径|
|`input_columns`|List[str] or str|-|输入列名称|
|`output_column`|str|None|输出列名称|
|`input_template`|PromptTemplate|None|输入字段模板|
|`output_template`|PromptTemplate|None|输出字段模板|
|`train_split`|str|'train'|训练集分割名|
|`train_range`|int/float/str|None|训练数据范围|
|`test_split`|str|'test'|测试集分割名|
|`test_range`|int/float/str|None|测试数据范围|

**train_range/test_range 说明:**

|值类型|示例|含义|
|---|---|---|
|None|-|使用全部数据|
|int|100|随机选择100条|
|float|0.1|随机选择10%数据|
|str|"[:100]"|选择前100条|
|str|"[100:200]"|选择第100-200条|

**初始化流程 (行 58-97):**

plaintext

`   ``` 1. 参数验证    ├─ 检查input_columns类型    ├─ 检查output_column    └─ 检查模板对象有效性  2. 数据集规范化    ├─ 若为单Dataset，转换为DatasetDict{'train': ds, 'test': ds}    ├─ 若为DatasetDict，使用原始结构    └─ 若为字符串，从路径加载  3. 数据集划分    ├─ train_split → 'train'    ├─ test_split → 'test'    └─ 调用load_partial_dataset()应用size约束  4. 保存配置    └─ self.dataset = 规范化后的DatasetDict    └─ self.input_columns, output_column, input_template, output_template ```   `

**关键方法:**

|方法|行号|输入|输出|说明|
|---|---|---|---|---|
|`generate_input_field_prompt()`|99|entry: Dict|str|生成输入字段提示|
|`generate_output_field_prompt()`|140|entry: Dict|str|生成输出字段提示|
|`generate_input_field_corpus()`|117|dataset, split|List[str]|批量生成输入语料|
|`generate_output_field_corpus()`|158|dataset, split|List[str]|批量生成输出语料|

**load_partial_dataset() 函数 (行 218-244):**

python

`   ``` def load_partial_dataset(dataset: Dataset,                          size: Optional[Union[int, float, str]] = None) -> Dataset:     """加载数据集的子集"""          total_size = len(dataset)     index_list = list(range(total_size))          if isinstance(size, (int, float)):         # 整数或浮点数：随机采样         if size < 1:             # 浮点数：比例采样             size = int(size * total_size)         rand = random.Random(x=size)         rand.shuffle(index_list)         dataset = dataset.select(index_list[:size])          elif isinstance(size, str):         # 字符串：切片表达式         # "[:100]" → index_list[:100]         # "[100:200]" → index_list[100:200]         dataset = dataset.select(eval(f'index_list{size}'))          return dataset ```   `

---

### 第三步：模块协作流程与数据流

#### ICL完整工作流程图

plaintext

`   ``` ┌─────────────────────────────────────────────────────────────────┐ │                     OpenCompass ICL框架                          │ └─────────────────────────────────────────────────────────────────┘                            ┌──────────────┐                           │   Dataset    │                           │   (train+    │                           │   test)      │                           └──────┬───────┘                                  │                     ┌────────────┴────────────┐                     ▼                         ▼             ┌───────────────┐      ┌──────────────────┐             │ DatasetReader │      │ Data Partitioner │             │               │      │                  │             │ - input cols  │      │ train/test split │             │ - output col  │      │ - 数据范围规范化  │             │ - templates   │      │ - 数据标准化      │             └───────┬───────┘      └──────────────────┘                     │         ┌───────────┴───────────┐         │                       │         ▼                       ▼     ┌──────────┐          ┌──────────────┐     │ index_ds │          │  test_ds     │     │(train)   │          │(eval set)    │     └────┬─────┘          └────┬─────────┘          │                     │          │                     ▼          │              ┌──────────────────┐          │              │  Retriever       │          │              │                  │          │    ┌────────▶│  - retrieve()    │          │    │         │  ├─ Zero         │          │    │         │  ├─ FixK         │          │    │         │  ├─ TopK(FAISS) │          │    │         │  └─ ...          │          │    │         │                  │          │    │         │ 返回: ice_idx_   │          │    │         │ list [[1,2,...],│          │    │         │ [3,4,...], ...]  │          │    │         └────┬─────────────┘          │    │              │          └────┼──────────────┤               │              │               ▼              ▼          ┌────────────────────────────┐          │   PromptTemplate          │          │                            │          │  - ice_template            │          │  - prompt_template         │          │                            │          │  generate_ice_item()       │          │  ├─ 编码模板              │          │  ├─ 填充数据              │          │  └─ 返回格式化示例        │          │                            │          │  generate_label_prompt()   │          │  ├─ 将ice填入prompt       │          │  ├─ 替换标签              │          │  └─ 返回完整提示          │          └────────┬───────────────────┘                   │                   ▼         ┌─────────────────────┐         │   Inferencer        │         │                     │         │ - GenInferencer     │ ───▶ model.generate()         │ - PPLInferencer     │ ───▶ model.get_ppl()         │ - ChatInferencer    │ ───▶ model.chat()         │ - ...               │         │                     │         │ inference()方法:    │         │ 1. 获取ice_idx_list │         │ 2. 生成提示词列表   │         │ 3. 构建DataLoader   │         │ 4. 批推理           │         │ 5. 保存结果         │         └────────┬────────────┘                  │                  ▼         ┌────────────────────┐         │  Output Handler    │         │                    │         │ - results_dict     │         │ - write_to_json()  │         │ - save_results()   │         │ - save_predictions │         └────────┬───────────┘                  │                  ▼          ┌─────────────────┐          │  JSON输出文件   │          │                 │          │ {               │          │  "0": {         │          │   "prediction": │          │    "...",       │          │   "gold": "..." │          │  },             │          │  "1": {...},    │          │  ...            │          │ }               │          └─────────────────┘ ```   `

#### 数据流示例（MMLU多选题）

plaintext

`   ``` 输入数据: {   "input": "Which protein is...",   "A": "Hemoglobin",   "B": "Myoglobin",   "C": "Collagen",   "D": "Elastin",   "target": "A" }  Step 1: DatasetReader.generate_input_field_prompt() ├─ input_columns = ['input', 'A', 'B', 'C', 'D'] ├─ 生成: "Which protein is...\nA) Hemoglobin\nB) Myoglobin\nC) Collagen\nD) Elastin" └─ 返回: str  Step 2: Retriever.retrieve() ├─ TopkRetriever通过向量搜索 ├─ 返回: [[5, 12, 8], [3, 15, 9], ...]  (为每个测试样本检索3个相似训练样本) └─ 访问: index_ds[5], index_ds[12], index_ds[8]...  Step 3: Retriever.generate_ice() ├─ 对于ice_idx_list[0] = [5, 12, 8] ├─ 获取训练集样本: index_ds[5], index_ds[12], index_ds[8] ├─ 使用ice_template.generate_ice_item()生成格式化示例 ├─ 样本结合: │  sample 5: "Which atom...\nA) Carbon\n..." (ice_template处理) │  sample 12: "Which bond...\nA) Ionic\n..."  │  sample 8: "Which molecule...\nA) Water\n..." ├─ 用sep_token分隔: sample5 + '\n' + sample12 + '\n' + sample8 + ice_eos_token └─ 返回: str (完整上文示例)  Step 4: Retriever.generate_prompt_for_generate_task() ├─ 输入: idx=0, ice=(上文示例), test_ds[0] ├─ 调用prompt_template.generate_item() ├─ 模板中ice_token(如'</E>')被替换为ice字符串 ├─ 输出列被生成字段替换标记替换 ├─ 完整提示: │  "Answer the following: </E> │   [上文示例3个样本] │   </E> │   Which protein is... │   A) Hemoglobin │   B) Myoglobin │   C) Collagen │   D) Elastin │   ANSWER: "  ← 生成字段 └─ 返回: str  Step 5: GenInferencer.inference() ├─ 构建DataLoader，批大小=4 ├─ Batch 1: [prompt0, prompt1, prompt2, prompt3] ├─ model.generate_from_template(batch, max_out_len=10) ├─ 返回: ["A", "B", "D", "C"] ├─ output_handler.save_results()保存 ├─ 输出: │  { │    "0": {"prediction": "A", "gold": "A", ...}, │    "1": {"prediction": "B", "gold": "B", ...}, │    ... │  } └─ 返回: ["A", "B", "D", "C"] ```   `

#### GenInferencer 和 PPLInferencer 的区别

|维度|GenInferencer|PPLInferencer|
|---|---|---|
|**任务类型**|开放式生成|多分类任务|
|**输入**|问题+上文|问题+标签候选+上文|
|**模型调用**|`model.generate()`|`model.get_ppl()`|
|**输出**|生成的文本序列|困惑度分数|
|**预测方式**|直接生成结果|选择PPL最低的标签|
|**评估对象**|任意长生成|固定的多选项|
|**样本特例**|MMLU数据集（标签生成）|CMNLI(含/蕴/中立分类)|

---

### 第四步：调用关系与交互模式

#### Inferencer ← Retriever ← Template 调用链

python

`   ``` # 配置示例 infer_cfg = dict(     prompt_template=dict(         type=PromptTemplate,         template=dict(             round=[dict(role='HUMAN', prompt=QUERY_TEMPLATE)],         ),         ice_token='</E>',     ),     retriever=dict(type=ZeroRetriever),     inferencer=dict(         type=GenInferencer,         max_out_len=256,         batch_size=8,     ), )  # 构建过程 prompt_template = ICL_PROMPT_TEMPLATES.build(infer_cfg['prompt_template']) # → PromptTemplate instance  retriever_cfg = infer_cfg['retriever'].copy() retriever_cfg['dataset'] = dataset retriever = ICL_RETRIEVERS.build(retriever_cfg) # → ZeroRetriever instance (包含dataset内的train/test)  inferencer = ICL_INFERENCERS.build(infer_cfg['inferencer']) inferencer.model = model # → GenInferencer instance  # 执行推理 results = inferencer.inference(     retriever=retriever,     ice_template=None,     prompt_template=prompt_template, ) # 内部调用流程: # 1. ice_idx_list = retriever.retrieve() # 2. for ice_idx in ice_idx_list: #      ice = retriever.generate_ice(ice_idx, ice_template) #      prompt = retriever.generate_prompt_for_generate_task(idx, ice, ...) # 3. model.generate_from_template(prompt, max_out_len=...) # 4. output_handler.save_results(...) ```   `

---

## 报告 2：Dataset模块（datasets/）深入源码分析

### 第一步：目录结构与文件分类

OpenCompass数据集模块位于 `d:\project\opencompass_inner\opencompass\datasets\`，包含170+个数据集文件和38个子目录。

#### 根目录文件分类

|文件类型|数量|示例|
|---|---|---|
|**直接数据集类**|80+|`mmlu.py`, `arc.py`, `gsm8k.py`, `ceval.py`, `cmnli.py`|
|**子目录数据集**|30+|`agieval/`, `apps/`, `babilong/`, `datasets/`, `llm_compression/`|
|**通用数据集**|5+|`huggingface.py`, `jsonl.py`, `custom.py`, `base.py`, `generic.py`|
|**汇总/别名**|20+|`__init__.py`, 各模块导出|

#### 数据集子目录结构（10个代表性目录）

|目录|文件数|用途|数据集类型|
|---|---|---|---|
|**agieval/**|9|AGIEval多题型|考试/推理|
|**apps/**|8|APPS代码生成|代码评估|
|**babilong/**|5|Babi长文本|长文本理解|
|**llm_compression/**|2|LLM压缩评估|效率评估|
|**IFBench/**|6|Instruction Following|指令跟随|
|**IFEval/**|7|IFEval指令|指令评估|
|**NPHardEval/**|13|NP难问题|推理复杂性|
|**PMMEval/**|10|模型混合|多模型评估|
|**SciReasoner/**|15|科学推理|科学领域|
|**TheoremQA/**|6|定理问答|数学推理|

---

### 第二步：数据集加载机制与基类

#### BaseDataset 基类

**文件位置:** `d:\project\opencompass_inner\opencompass\datasets\base.py` (行 1-61)

**类定义:** `class BaseDataset`

**构造参数:**

|参数|类型|默认值|说明|
|---|---|---|---|
|`reader_cfg`|Dict|{}|DatasetReader配置|
|`k`|int/List[int]|1|数据复制因子|
|`n`|int|1|数据集翻倍数|
|`**kwargs`|-|-|其他参数（传递给load()）|

**初始化流程 (行 13-45):**

python

`   ``` def __init__(self, reader_cfg: Optional[Dict] = {}, k: Union[int, List[int]] = 1, n: int = 1, **kwargs):     # 1. 提取abbr和加载数据集     abbr = kwargs.pop('abbr', 'dataset')     dataset = self.load(**kwargs)  # 子类实现load()          # 2. 验证k和n的有效性     max_k = max(k) if isinstance(k, List) else k     assert max_k <= n, 'Maximum value of k must <= n'          # 3. 为数据集添加标记信息并复制     if isinstance(dataset, Dataset):         # Dataset情况：单一数据集         dataset = dataset.map(             lambda x, idx: {                 'subdivision': abbr,                 'idx': idx             },             with_indices=True,             writer_batch_size=16,             load_from_cache_file=False         )         dataset = concatenate_datasets([dataset] * n)         self.dataset = dataset     else:         # DatasetDict情况：多分割数据集         self.dataset = DatasetDict()         for key in dataset:             dataset[key] = dataset[key].map(                 lambda x, idx: {                     'subdivision': f'{abbr}_{key}',                     'idx': idx                 },                 with_indices=True,                 writer_batch_size=16,                 load_from_cache_file=False             )             dataset[key] = concatenate_datasets([dataset[key]] * n)             self.dataset[key] = dataset[key]          # 4. 初始化DatasetReader     self._init_reader(**reader_cfg)  def _init_reader(self, **kwargs):     self.reader = DatasetReader(self.dataset, **kwargs)  @property def train(self):     return self.reader.dataset['train']  @property def test(self):     return self.reader.dataset['test']  @staticmethod def load(**kwargs) -> Union[Dataset, DatasetDict]:     """子类需实现此方法加载数据"""     pass ```   `

**关键概念:**

- `k`: 用于few-shot学习，指从训练集中选取的示例数量（后续由Retriever使用）
- `n`: 数据集重复因子，用于数据增强
- `subdivision`: 数据来源标记，用于追踪样本源头

---

#### 数据集注册机制

**注册表:** `LOAD_DATASET` (opencompass/registry.py)

**注册方式:**

python

`   ``` @LOAD_DATASET.register_module() class XXXDataset(BaseDataset):     @staticmethod     def load(**kwargs) -> Union[Dataset, DatasetDict]:         # 数据加载逻辑         return Dataset.from_list([...]) 或 DatasetDict({...}) ```   `

**注册示例:**

python

`   ``` # 1. HuggingFace数据集 @LOAD_DATASET.register_module() class HFDataset(BaseDataset):     @staticmethod     def load(**kwargs):         if 'data_files' in kwargs:             kwargs['data_files'] = get_data_path(kwargs['data_files'])         return load_dataset(**kwargs)  # 2. 本地JSON数据集 @LOAD_DATASET.register_module() class GSMHardDataset(BaseDataset):     @staticmethod     def load(path):         path = get_data_path(path)         dataset = []         with open(path, 'r', encoding='utf-8') as f:             for line in f:                 line = json.loads(line.strip())                 dataset.append({'question': line['input'], 'answer': str(line['target'])})         return Dataset.from_list(dataset)  # 3. 自定义预处理 @LOAD_DATASET.register_module() class CMNLIDatasetV2(BaseDataset):     @staticmethod     def load(path, local_mode: bool = False):         # 可选从ModelScope或本地加载         path = get_data_path(path, local_mode=local_mode)         data = []         with open(path, 'r', encoding='utf-8') as f:             for line in f:                 line = json.loads(line)                 if line['label'] == '-':  # 过滤                     continue                 # 标签映射                 line['label'] = {                     'entailment': 'A',                     'contradiction': 'B',                     'neutral': 'C',                 }[line['label']]                 data.append(line)         return Dataset.from_list(data) ```   `

---

### 第三步：代表性数据集配置分析

#### MMLU 数据集配置

**配置目录:** `d:\project\opencompass_inner\opencompass\configs\datasets\mmlu\`

**文件结构:**

- `mmlu_gen.py` - 通用配置入口
- `mmlu_openai_simple_evals_gen_b618ea.py` - 具体实现
- `mmlu_all_sets.py` - 子集列表
- 其他变体...

**mmlu_openai_simple_evals_gen_b618ea.py 详细解析 (60行):**

python

`   ``` # 1. 导入依赖 from mmengine.config import read_base from opencompass.openicl.icl_prompt_template import PromptTemplate from opencompass.openicl.icl_retriever import ZeroRetriever from opencompass.openicl.icl_inferencer import GenInferencer from opencompass.openicl.icl_evaluator import AccEvaluator from opencompass.datasets import MMLUDataset from opencompass.utils.text_postprocessors import match_answer_pattern  # 2. 读取基础配置 (mmlu_all_sets: ['astronomy', 'abstract_algebra', ...]) with read_base():     from .mmlu_all_sets import mmlu_all_sets  # 3. 查询模板 (完整多选题提示) QUERY_TEMPLATE = """ Answer the following multiple choice question. The last line of your response should be of the following format: 'ANSWER: $LETTER' (without quotes) where LETTER is one of ABCD. Think step by step before answering.  {input}  A) {A} B) {B} C) {C} D) {D} """.strip()  # 4. 数据集读取配置 mmlu_reader_cfg = dict(     input_columns=['input', 'A', 'B', 'C', 'D'],  # 输入的各个部分     output_column='target',  # 正确答案列     train_split='dev'  # 使用dev集作为训练集（示例） )  # 5. 推理配置（零样本） mmlu_infer_cfg = dict(     prompt_template=dict(         type=PromptTemplate,         template=dict(             round=[                 dict(role='HUMAN', prompt=QUERY_TEMPLATE),             ],         ),     ),     retriever=dict(type=ZeroRetriever),  # 无示例学习     inferencer=dict(type=GenInferencer),  # 生成式评估 )  # 6. 评估配置 mmlu_eval_cfg = dict(     evaluator=dict(type=AccEvaluator),  # 准确率评估     pred_postprocessor=dict(         type=match_answer_pattern,         answer_pattern= ```   `


以下是实际应用中使用的激活函数。由于各种原因，我希望选择一个其一阶导数无法表示为关于 sigmoid 函数 $\sigma(x) = \frac{1}{1 + e^{-x}}$ 的函数的激活函数。其他项可以出现，但该函数不应与 sigmoid 函数有任何关联。哪一个函数满足这一性质？ $T_{1}(x) = \frac{x}{1 + e^{-\beta x}}$  $T_{2}(x) = \frac{(-1 + (1 + e^x)^2) x}{1 + (1 + e^x)^2}$  $T_{3}(x) = \log{(1 + e^{x})}$  $T_{4}(x) = 0.5x\left(1 + \frac{e^{2\left(\sqrt{\frac{2}{\pi}}(x + 0.044715x^{3})\right)} - 1}{e^{2\left(\sqrt{\frac{2}{\pi}}(x + 0.044715x^{3})\right)} + 1}\right)$ 答案选项：  A. $T_{1}$  B. $T_{2}$  C. $T_{3}$  D. $T_{4}$  E. 以上皆非