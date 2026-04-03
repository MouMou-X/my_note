## 报告：OpenCompass Model 模块源码分析

---

### 第一部分：模块文件结构概览

#### 表1：Models 模块所有文件概览

| 文件名                                      | 文件大小    | 主要类/功能                                                      | 分类    | 用途                                       |
| ---------------------------------------- | ------- | ----------------------------------------------------------- | ----- | ---------------------------------------- |
| **base.py**                              | 20.1KB  | `BaseModel`, `LMTemplateParser`                             | 基础类   | 所有模型的抽象基类，定义核心接口                         |
| **base_api.py**                          | 19.4KB  | `BaseAPIModel`, `APITemplateParser`, `TokenBucket`          | 基础类   | API模型的基类，包含速率限制和模板解析                     |
| **__init__.py**                          | 2.8KB   | 模块导出                                                        | 元数据   | 导出所有模型类供外部导入                             |
| **openai_api.py**                        | 42.2KB  | `OpenAI`, `OpenAISDK`, `OpenAISDKRollout`                   | API模型 | OpenAI GPT系列模型封装（HTTP REST和SDK两种）        |
| **huggingface_<br>above_v4_33.py**       | 26.9KB  | `HuggingFacewithChatTemplate`, `HuggingFaceBaseModel`       | 本地模型  | HuggingFace Transformers库的ChatTemplate支持 |
| **huggingface.py**                       | 33.5KB  | `HuggingFace`, `HuggingFaceCausalLM`, `HuggingFaceChatGLM3` | 本地模型  | HuggingFace基础模型实现（旧版本支持）                 |
| **vllm.py**                              | 6.1KB   | `VLLM`                                                      | 本地模型  | vLLM推理引擎封装                               |
| **glm.py**                               | 15.3KB  | `GLM130B`                                                   | 本地模型  | ChatGLM模型系列封装                            |
| **llama2.py**                            | 10.1KB  | `Llama2`, `Llama2Chat`                                      | 本地模型  | LLaMA2系列本地部署                             |
| **qwen_api.py**                          | 6.6KB   | `Qwen`                                                      | API模型 | 阿里通义千问DashScope API                      |
| **openai_streaming.py**                  | 14.5KB  | `OpenAISDKStreaming`                                        | API模型 | OpenAI流式响应支持                             |
| **baidu_api.py**                         | 8.4KB   | `ERNIEBot`                                                  | API模型 | 百度ERNIE Bot API                          |
| **baichuan_api.py**                      | 5.9KB   | `BaiChuan`                                                  | API模型 | 百川大模型API                                 |
| **deepseek_api.py**                      | 5.9KB   | `DeepseekAPI`                                               | API模型 | DeepSeek模型API                            |
| **ai360_api.py**                         | 6.0KB   | `AI360GPT`                                                  | API模型 | 360AI API                                |
| **gemini_api.py**                        | 6.5KB   | `Gemini`                                                    | API模型 | Google Gemini API                        |
| **claude_api/**                          | 4 items | `Claude`, `ClaudeSDK`, `ClaudeAllesAPIN`                    | API模型 | Anthropic Claude API多种实现                 |
| **xunfei_api.py**                        | 12.9KB  | `XunFei`, `XunFeiSpark`                                     | API模型 | 讯飞星火API                                  |
| **zhipuai_api.py**                       | 4.1KB   | `ZhiPuAI`                                                   | API模型 | 智普清言API                                  |
| **zhipuai_v2_api.py**                    | 6.1KB   | `ZhiPuV2AI`                                                 | API模型 | 智普清言V2 API                               |
| **moonshot_api.py**                      | 5.6KB   | `MoonShot`                                                  | API模型 | 月之暗面Moonshot API                         |
| **mistral_api.py**                       | 3.5KB   | `Mistral`                                                   | API模型 | Mistral AI API                           |
| **minimax_api.py**                       | 12.1KB  | `MiniMax`, `MiniMaxChatCompletionV2`                        | API模型 | MiniMax API                              |
| **pangu_api.py**                         | 6.2KB   | `PanGu`                                                     | API模型 | 盘古大模型API                                 |
| **yi_api.py**                            | 5.9KB   | `YiAPI`                                                     | API模型 | 01.AI Yi模型API                            |
| **hunyuan_api.py**                       | 5.2KB   | `Hunyuan`                                                   | API模型 | 腾讯混元API                                  |
| **rendu_api.py**                         | 5.7KB   | `Rendu`                                                     | API模型 | 任度API                                    |
| **sensetime_api.py**                     | 7.3KB   | `SenseTime`                                                 | API模型 | 商汤科技API                                  |
| **stepfun_api.py**                       | 6.0KB   | `StepFun`                                                   | API模型 | StepFun模型API                             |
| **yayi_api.py**                          | 8.0KB   | `Yayi`                                                      | API模型 | 雅意模型API                                  |
| **unigpt_api.py**                        | 4.4KB   | `UniGPT`                                                    | API模型 | UniGPT API                               |
| **krgpt_api.py**                         | 4.9KB   | `KrGPT`                                                     | API模型 | KrGPT API                                |
| **bluelm_api.py**                        | 5.4KB   | `BlueLMAPI`                                                 | API模型 | BlueLM API                               |
| **bailing_api_oc.py**                    | 8.1KB   | `BailingAPI`                                                | API模型 | 百灵API                                    |
| **bytedance_api.py**                     | 5.6KB   | `ByteDance`                                                 | API模型 | 字节跳动API                                  |
| **doubao.py**                            | 3.6KB   | `Doubao`                                                    | 本地模型  | 豆包模型                                     |
| **doubao_api.py**                        | 5.1KB   | `Doubao`                                                    | API模型 | 豆包API版本                                  |
| **lightllm_api.py**                      | 12.4KB  | `LightllmAPI`, `LightllmChatAPI`                            | 推理框架  | LightLLM推理引擎                             |
| **intern_model.py**                      | 4.8KB   | `InternLM`                                                  | 本地模型  | InternLM本地部署                             |
| **interntrain.py**                       | 20.3KB  | `InternTrain`                                               | 本地模型  | InternTrain推理框架                          |
| **turbomind.py**                         | 9.8KB   | `TurboMindModel`                                            | 推理框架  | LMDeploy TurboMind引擎                     |
| **turbomind_with_<br>tf_above_v4_33.py** | 9.8KB   | `TurboMindModelwithChatTemplate`                            | 推理框架  | TurboMind ChatTemplate支持                 |
| **vllm_with_tf_above<br>_v4_33.py**      | 7.5KB   | `VLLMwithChatTemplate`                                      | 推理框架  | vLLM ChatTemplate支持                      |
| **mixtral.py**                           | 4.4KB   | `Mixtral`                                                   | 本地模型  | Mixtral混合专家模型                            |
| **modelscope.py**                        | 9.6KB   | `ModelScope`, `ModelScopeCausalLM`                          | 本地模型  | ModelScope模型库集成                          |
| **alaya.py**                             | 5.9KB   | `AlayaLM`                                                   | 本地模型  | AlayaLM模型                                |
| **accessory.py**                         | 3.4KB   | `LLaMA2AccessoryModel`                                      | 本地模型  | LLaMA2 Accessory框架                       |
| **langchain.py**                         | 1.6KB   | LangChain集成                                                 | 框架集成  | LangChain中间层支持                           |
| **lagent.py**                            | 6.0KB   | `LAgentModel`                                               | 框架集成  | LAgent代理框架集成                             |
| **telechat_api/**                        | 5 items | `TeleChat`, `TeleChatStream`                                | API模型 | 远景AI TeleChat API                        |

---

### 第二步：核心类详细分析

#### 2.1 BaseModel（本地模型基类）

**文件路径**：`d:\project\opencompass_inner\opencompass\models\base.py`

**行号范围**：13-260

##### 类属性

|属性|类型|默认值|含义|
|---|---|---|---|
|`is_api`|bool|`False`|标记是否为API模型（本地模型=False，API模型=True）|

##### 构造函数参数

python


``` 
def __init__(self,              
	path: str,                                    # 模型路径或标识符              
	max_seq_len: int = 2048,                      # 最大序列长度              
	tokenizer_only: bool = False,                 # 仅加载分词器              
	meta_template: Optional[Dict] = None,         # 元提示词模板              
	generation_kwargs: Optional[Dict] = dict(),   # 生成参数             
	sync_rank: bool = False)                      # 多GPU同步标记 
```

##### 核心方法签名表

|方法名|签名|返回类型|说明|
|---|---|---|---|
|**generate** (抽象)|`(inputs: List[str], max_out_len: int, **kwargs)`|`List[str]`|文本生成 - 所有实现必须重写此方法|
|**get_ppl** (抽象)|`(inputs: List[str], mask_length: Optional[List[int]] = None)`|`List[float]`|困惑度计算 - PPL基评估|
|**get_ppl_tokenwise** (抽象)|`(inputs: List[str], mask_length: Optional[List[int]] = None)`|`List[float]`|逐token困惑度|
|**encode** (抽象)|`(prompt: str)`|`torch.Tensor`|文本编码为token ID|
|**decode** (抽象)|`(tokens: torch.Tensor)`|`str`|token ID解码为文本|
|**get_token_len** (抽象)|`(prompt: str)`|`int`|获取token长度（分词）|
|**parse_template**|`(prompt_template: PromptType, mode: str)`|`str`|解析并包装提示词模板|
|**generate_from_template**|`(templates: List[PromptType], max_out_len: int)`|`List[str]`|从模板生成|
|**get_ppl_from_template**|`(templates: List[PromptType], mask_length=None)`|`List[float]`|从模板计算PPL|
|**get_token_len_from_template**|`(templates: Union[PromptType, List[PromptType]], mode='ppl')`|`Union[List[int], int]`|从模板计算token长度|
|**sync_inputs**|`(inputs: str)`|`str`|多GPU同步输入|
|**to**|`(device)`|None|转移到设备|

##### 关键实现：LMTemplateParser（本地模型模板解析器）

**作用**：将提示词模板与元模板结合，生成最终提示词文本。

**初始化**：`base.py` 第 265-299 行

python

`   ``` class LMTemplateParser:     def __init__(self, meta_template: Optional[Dict] = None):         # 验证meta_template结构         # 构建roles字典：{ role_name -> role_config }         # roles中的role_config包括: role, begin, end, prompt, generate标记 ```   `

**工作原理**：

1. **输入**：`PromptType`（字符串或PromptList对象）和模式(`'ppl'`/`'gen'`)
2. **处理流程**：
    - 若无meta_template：直接拼接字符串
    - 若有meta_template：
        - 按`'round'`和`'ice'`（in-context examples）section切割
        - 根据role配置生成对应格式
        - 对生成模式（`for_gen=True`）：遇到`generate=True`的role时停止
3. **输出**：最终格式化提示词字符串

**template_parser的作用流程图**：

plaintext

`   ``` 元模板 meta_template (包含round, begin, end配置)          ↓   PromptList (role/prompt对象列表)          ↓    LMTemplateParser.parse_template()          ↓   遍历每个item，按role处理 → role_dict更新          ↓   通过_prompt2str -> _role2str 递归转换          ↓   最终字符串（已包装系统提示词/角色标记） ```   `

---

#### 2.2 BaseAPIModel（API模型基类）

**文件路径**：`d:\project\opencompass_inner\opencompass\models\base_api.py`

**行号范围**：23-165

##### 继承关系

plaintext

`   ``` BaseModel     ↓ BaseAPIModel ```   `

##### 类属性

|属性|值|含义|
|---|---|---|
|`is_api`|`True`|标记为API模型|

##### 构造函数参数

|参数|类型|默认值|说明|
|---|---|---|---|
|`path`|str|必需|模型名称标识符（如`gpt-4`、`qwen-max`）|
|`query_per_second`|int|1|QPS限流值：每秒允许的最大查询数|
|`rpm_verbose`|bool|False|是否打印RPM（每分钟请求数）日志|
|`retry`|int|2|失败重试次数|
|`max_seq_len`|int|2048|最大序列长度|
|`meta_template`|Optional[Dict]|None|元提示词模板|
|`generation_kwargs`|Dict|{}|生成参数|
|`verbose`|bool|False|是否打印调试日志|

##### 核心机制：TokenBucket（速率限制）

**作用**：实现Token Bucket算法，实现QPS限流

**文件位置**：`base_api.py` 第 458-495 行

**工作原理**：

python

`   ``` class TokenBucket:     def __init__(self, rate: float, verbose=False):         # rate = query_per_second         # 启动后台线程，每秒添加rate个token         # 每次API调用前acquire()一个token（阻塞）          def get_token(self):         # 若未启动，启动daemon线程添加token         # 信号量acquire()：若无token则阻塞 ```   `

**并发控制**：

- 多线程环境中使用`threading.Semaphore`
- 后台线程定期补充token（`_add_tokens`）
- 请求线程acquire获取token（自动限流）

##### APITemplateParser（API模型模板解析器）

**文件位置**：`base_api.py` 第 167-456 行

**主要差异**（vs LMTemplateParser）：

|特性|LM模板解析|API模板解析|
|---|---|---|
|输出格式|纯文本字符串|PromptList，每项包含`{'role': role, 'prompt': content}`|
|Role处理|自定义role标记|标准OpenAI格式（`system`, `user`, `assistant`）|
|Meta Template格式|字典格式|列表格式（role对象列表）或字典格式|
|应用场景|本地模型推理|OpenAI/Claude等API调用|

---

#### 2.3 HuggingFace本地模型实现

**文件路径**：`d:\project\opencompass_inner\opencompass\models\huggingface_above_v4_33.py`

**行号范围**：144-664

##### 类：HuggingFacewithChatTemplate

**继承**：`BaseModel`

**应用**：支持HuggingFace Chat Template的模型（Qwen、LLaMA2 Chat等）

##### 构造函数参数关键项

|参数|类型|默认值|说明|
|---|---|---|---|
|`path`|str|必需|HF模型ID或本地路径|
|`model_kwargs`|dict|{}|传给`AutoModel/AutoModelForCausalLM`的参数|
|`tokenizer_path`|Optional[str]|None|分词器路径（默认同model path）|
|`generation_kwargs`|dict|{}|`model.generate()`参数|
|`max_seq_len`|Optional[int]|None|最大序列长度（自动推断）|
|`meta_template`|Optional[Dict]|None|元提示词模板|
|`fastchat_template`|Optional[str]|None|FastChat模板名（如'vicuna'）|
|`stop_words`|List[str]|[]|停止词|
|`mode`|str|'none'|输入截断模式：'none'或'mid'|

##### 关键方法

|方法|实现位置|功能|
|---|---|---|
|`generate()`|本类|调用`model.generate()`，支持单个/批量生成|
|`get_ppl()`|本类|计算困惑度（逐token logits）|
|`get_ppl_tokenwise()`|行245-403|逐token困惑度，支持label和mask_length|
|`_load_tokenizer()`|行190-218|加载分词器，处理pad_token_id|
|`_load_model()`|行220-242|加载模型，支持PEFT微调|
|`encode()`|本类|token编码|
|`decode()`|本类|token解码|
|`get_token_len()`|本类|计算token长度|

##### generate() 实现流程

**核心逻辑**（从本模块代码推断）：

python

`   ``` def generate(self, inputs: List[str], max_out_len: int, **kwargs) -> List[str]:     # 1. 合并generation_kwargs和运行时kwargs     generation_kwargs = {**self.generation_kwargs, **kwargs}          # 2. 若启用了batch padding：     if self.batch_padding and len(inputs) > 1:         return self._batch_generate(inputs, max_out_len,                                     generation_kwargs)          # 3. 否则逐个生成     return self._single_generate(inputs, max_out_len,                                  generation_kwargs)  def _single_generate(self, inputs, max_out_len, gen_kwargs):     # 对每个input：     tokens = self.tokenizer(inputs, ...)  # 编码     # 应用模式截断（'mid'表示中间截断）     if self.mode == 'mid':         # 保留prompt长度为 max_seq_len - max_out_len          # 调用model.generate()     outputs = self.model.generate(         **tokens,         max_new_tokens=max_out_len,  # 关键参数         **gen_kwargs     )          return self.tokenizer.batch_decode(outputs) ```   `

---

#### 2.4 VLLM推理引擎

**文件路径**：`d:\project\opencompass_inner\opencompass\models\vllm.py`

**行号范围**：17-166

##### 继承与特性

**继承**：`BaseModel`

**用途**：利用vLLM高性能推理引擎，支持大批量并发生成

##### 构造参数

|参数|类型|默认值|说明|
|---|---|---|---|
|`path`|str|必需|HF模型ID|
|`max_seq_len`|int|2048|最大序列长度|
|`model_kwargs`|dict|None|传给vLLM的LLM()参数|
|`generation_kwargs`|dict|{}|生成参数（SamplingParams）|
|`use_fastchat_template`|bool|False|是否用FastChat模板|
|`lora_path`|str|None|LoRA权重路径|
|`stop_words`|List[str]|[]|停止词列表|

##### generate() 实现

**核心逻辑**（行64-117）：

python

`   ``` def generate(self, inputs: List[str], max_out_len: int,               stopping_criteria: List[str] = []) -> List[str]:          # 1. 输入模式处理（mid模式：截断中间）     if self.mode == 'mid':         # 保留前half + 后half的输入         half = int((self.max_seq_len - max_out_len) / 2)          # 2. 构造采样参数     generation_kwargs = {         **self.generation_kwargs,         'max_tokens': max_out_len,          # 覆盖设置         'stop': self.stop_words + stopping_criteria     }     sampling_kwargs = SamplingParams(**generation_kwargs)          # 3. 调用vLLM推理     outputs = self.model.generate(inputs, sampling_kwargs)          # 4. 提取生成文本     return [output.outputs[0].text for output in outputs] ```   `

##### get_ppl() 实现

**困惑度计算**（行119-142）：

python

`   ``` def get_ppl(self, inputs: List[str],              mask_length: Optional[List[int]] = None) -> List[float]:          # 使用vLLM的prompt_logprobs功能     sampling_kwargs = SamplingParams(prompt_logprobs=0)     outputs = self.model.generate(inputs, sampling_kwargs)          # 逐token计算log概率     for output in outputs:         prompt_logprobs = output.prompt_logprobs[1:]  # 去除首token         prompt_token_ids = output.prompt_token_ids[1:]                  logprobs_list = [             prompt_logprobs[i][prompt_token_ids[i]].logprob             for i in range(len(prompt_logprobs))         ]                  # mask_length处理         if mask_length:             logprobs_list = logprobs_list[-mask_length[i]:]                  # 困惑度 = exp(-mean_logprob)         loss = -np.array(logprobs_list).sum() / len(prompt_token_ids) ```   `

---

#### 2.5 OpenAI API模型

**文件路径**：`d:\project\opencompass_inner\opencompass\models\openai_api.py`

**行号范围**：33-1073

##### 类层次

plaintext

`   ``` BaseAPIModel     ↓ OpenAI (HTTP REST接口) OpenAISDK (官方SDK接口) OpenAISDKRollout (SDK + Rollout支持) ```   `

##### OpenAI 类（HTTP接口）

**构造参数关键项**：

|参数|类型|默认值|说明|
|---|---|---|---|
|`path`|str|'gpt-3.5-turbo'|模型ID|
|`max_seq_len`|int|16384|最大序列长度|
|`query_per_second`|int|1|QPS限流|
|`retry`|int|2|失败重试次数|
|`key`|Union[str, List[str]]|'ENV'|API密钥（支持轮询多个key）|
|`org`|Optional[Union[str, List[str]]]|None|组织ID（轮询）|
|`openai_api_base`|str|默认URL|API基础URL|
|`openai_proxy_url`|Optional[str]|None|代理URL（可从ENV读取）|
|`mode`|str|'none'|输入截断模式|
|`temperature`|Optional[float]|None|采样温度|
|`max_workers`|Optional[int]|None|线程池大小（默认CPU_2，最多32） \|_|

##### generate() 关键实现（行165-202）

**并发设计**：

python

`   ``` def generate(self, inputs: List[PromptType],               max_out_len: int, temperature: float = 0.7) -> List[str]:          # 使用ThreadPoolExecutor并发调用     with ThreadPoolExecutor(max_workers=self.max_workers) as executor:         results = list(executor.map(             self._generate,             inputs,             [max_out_len] * len(inputs),             [temperature] * len(inputs)         ))     return results ```   `

**单次请求流程**（`_generate()`，行204-450）：

plaintext

`   ``` 输入 input (str or PromptList)   ↓ _preprocess_messages() → 消息格式化 + 长度处理   ↓ 重试循环 (max_num_retries < self.retry)   ↓ self.wait() → TokenBucket限流   ↓ 轮询选择API key（跳过无配额的key）   ↓ 构造请求头（Authorization, OpenAI-Organization）   ↓ 构造请求体：   {     "model": self.path,     "messages": messages,           # 关键：chat format     "max_tokens": max_out_len,      # 或 max_completion_tokens (o1模型)     "temperature": temperature,     "logprobs": self.logprobs,      # 可选     "top_logprobs": self.top_logprobs,     ...   }   ↓ requests.post() 或 带代理的post   ↓ 解析响应JSON   ↓ 异常处理：   - 状态码200 ✓   - 连接错误 → 重试   - 权限错误 → 标记key无效   ↓ 提取content + reasoning_content   ↓ 返回生成文本 ```   `

**重试机制**：

- 失败原因：连接错误、服务器错误、权限问题
- 重试策略：指数退避（隐含在循环中）
- 无效key跳过：维护`self.invalid_keys`集合

**并发控制**：

- 限流：`TokenBucket`（QPS）
- API key轮询：`self.key_ctr`（Thread-safe via Lock）
- 组织ID轮询：`self.org_ctr`（Thread-safe via Lock）

---

#### 2.6 Qwen API模型

**文件路径**：`d:\project\opencompass_inner\opencompass\models\qwen_api.py`

**行号范围**：13-191

##### 继承与特性

**继承**：`BaseAPIModel`

**API服务**：阿里DashScope（通义千问）

##### 构造参数

|参数|类型|默认值|说明|
|---|---|---|---|
|------|------|--------|------|
|`path`|str|必需|模型ID（如`qwen-max`, `qwen-plus`）|
|`key`|str|必需|DashScope API密钥或'ENV'|
|`query_per_second`|int|1|QPS限流|
|`retry`|int|5|失败重试次数|
|`generation_kwargs`|Dict|{}|生成参数|
|`disable_data_inspection`|bool|False|禁用内容审查|

##### generate() 实现（行64-85）

**关键特点**：

python

`   ``` def generate(self, inputs: List[PromptType],               max_out_len: int) -> List[str]:          # 使用ThreadPoolExecutor并发     with ThreadPoolExecutor() as executor:         results = list(executor.map(             self._generate,             inputs,             [max_out_len] * len(inputs)         ))     return results ```   `

##### _generate() 单次请求逻辑（行87-190）_

python

`   ``` def _generate(self, input: PromptType, max_out_len: int) -> str:          # 1. 消息格式转换     if isinstance(input, str):         messages = [{'role': 'user', 'content': input}]     else:  # PromptList         # 递归遍历，按role分组合并内容         # SYSTEM → system         # BOT → assistant         # 其他 → user         messages = [...]          # 2. 构造请求数据     data = {'messages': messages}     data.update(self.generation_kwargs)  # 合并generation_kwargs          # 3. 重试循环     for attempt in range(self.retry):         self.acquire()  # 获取QPS token                  try:             response = self.dashscope.Generation.call(                 model=self.path,                 **data  # 注意：max_out_len需通过data['max_tokens']传递             )         except Exception:             continue                  self.release()                  # 4. 响应处理         if response.status_code == 200:             return response.output.text         elif response.status_code == 429:  # 限流             time.sleep(2)             continue         elif response.status_code == 400:  # 内容审查             return '输出数据可能包含不当内容'         # ... 其他status code处理          raise RuntimeError(response.message) ```   `

##### 参数传递关键问题

**当前实现的参数透传缺陷**（根据任务记忆）：

|参数|问题|修复方案|
|---|---|---|
|`max_out_len`|生成方法参数，但通常需转为`max_tokens`传给API|在`data`构造时：若max_out_len存在且generation_kwargs中无max_tokens，则`data['max_tokens'] = max_out_len`|
|`temperature`|需通过generation_kwargs传递|在调用时提供或在config中设置|
|其他API参数|通过generation_kwargs合并到data中|保持当前机制|

---

### 第三步：模块内部调用关系与数据流

#### 3.1 模型初始化与构建流程

plaintext

`   ``` 配置文件 (model_cfg dict)     ↓ build_model_from_cfg(model_cfg)  [opencompass/utils/build.py]     ├→ 深拷贝model_cfg     ├→ 移除运行时参数：     │  - max_out_len (generation时使用)     │  - batch_size (inferencer使用)     │  - min_out_len (generation时使用)     │  - abbr, run_cfg, 等元数据     └→ MODELS.build(model_cfg) [注册表]        ↓        对应的模型类 __init__()        ├→ BaseModel.__init__()  或  BaseAPIModel.__init__()        ├→ 初始化模板解析器        └→ 加载模型/tokenizer           ↓        返回 model 实例     ↓ GenInferencer.__init__(model, max_out_len, batch_size)     ├→ 保存max_out_len作为生成参数     └→ 保存batch_size作为批处理大小 ```   `

**关键代码**（`opencompass/utils/build.py` 第15-24行）：

python

`   ``` def build_model_from_cfg(model_cfg: ConfigDict):     model_cfg = copy.deepcopy(model_cfg)     # 移除运行时参数     model_cfg.pop('run_cfg', None)     model_cfg.pop('max_out_len', None)      # ← 关键     model_cfg.pop('batch_size', None)       # ← 关键     model_cfg.pop('abbr', None)     model_cfg.pop('summarizer_abbr', None)     model_cfg.pop('pred_postprocessor', None)     model_cfg.pop('min_out_len', None)     return MODELS.build(model_cfg) ```   `

**参数分离机制的意义**：

- `max_out_len`, `batch_size` 是**推理时**参数，不是**构造**参数
- 从config中分离出来由Inferencer管理
- 防止传给模型构造函数导致TypeError

---

#### 3.2 生成流程

plaintext

`   ``` GenInferencer.generate(prompts)     ↓     ├→ 若batch_size > 1：分批处理     └→ 对每个批次：        ├→ model.generate_from_template(        │      templates,        │      max_out_len=self.max_out_len,  ← 从Inferencer传入        │      **self.generation_kwargs)        └→ 或 model.generate(               parsed_inputs,               max_out_len=self.max_out_len,               **kwargs)           ↓           BaseModel.generate_from_template()           ├→ parse_template(templates, mode='gen')           │  └→ template_parser.parse_template()           │     ↓           │     [本地模型] LMTemplateParser → 字符串           │     [API模型]  APITemplateParser → PromptList           └→ model.generate(parsed, max_out_len)              ↓              具体实现（HuggingFace/VLLM/OpenAI/Qwen等）              ├→ 消息格式转换              ├→ 调用底层推理引擎              └→ 返回生成文本 List[str] ```   `

---

#### 3.3 困惑度计算流程

plaintext

`   ``` PPLInferencer.get_ppl(templates, mask_length)     ↓ model.get_ppl_from_template(templates, mask_length)     ├→ parse_template(templates, mode='ppl')     │  └→ template_parser.parse_template(templates, 'ppl')     │     ↓     │     生成格式化提示词     └→ model.get_ppl(parsed_inputs, mask_length)        ↓        具体实现        ├→ [HuggingFace] 前向传播 → logits → cross entropy loss        ├→ [VLLM]        prompt_logprobs特性 → logprob求和        ├→ [API模型]     不支持（raise NotImplementedError）        └→ 返回困惑度值 List[float]           ↓           若mask_length非空：           └→ 只计算最后mask_length[i]个token的困惑度 ```   `

---

#### 3.4 数据流中的关键参数转换

plaintext

`   ``` ┌─────────────────────────────────────────────────────────┐ │ 配置层（Config File）                                    │ ├─────────────────────────────────────────────────────────┤ │ model_cfg = {                                           │ │   'type': ModelClass,          # ← 决定使用哪个类      │ │   'path': 'model-id',          # ← 传给__init__        │ │   'max_out_len': 512,          # ← 分离给Inferencer   │ │   'batch_size': 8,             # ← 分离给Inferencer   │ │   'generation_kwargs': {...},  # ← 传给__init__       │ │   'meta_template': {...},      # ← 传给__init__       │ │   'query_per_second': 2,       # ← [API模型] 传给__init__ │   '...': ...                   # ← 其他模型特定参数   │ │ }                                                       │ └─────────────────────────────────────────────────────────┘            ↓ build_model_from_cfg() ┌─────────────────────────────────────────────────────────┐ │ 模型层（Model Construction）                            │ ├─────────────────────────────────────────────────────────┤ │ model = ModelClass(                                     │ │   path='model-id',                                      │ │   max_seq_len=2048,            # ← 默认值             │ │   generation_kwargs={...},                              │ │   meta_template={...},                                  │ │   query_per_second=2,          # ← [API]              │ │ )                                                       │ │                                                         │ │ model.__init__() {                                      │ │   self.template_parser = LMTemplateParser() / APITemplateParser() │   self.model = load_model()    # ← [本地] 加载LLM     │ │   self.generation_kwargs = generation_kwargs           │ │ }                                                       │ └─────────────────────────────────────────────────────────┘            ↓ Inferencer.__init__() ┌─────────────────────────────────────────────────────────┐ │ 推理层（Inference Orchestration）                       │ ├─────────────────────────────────────────────────────────┤ │ inferencer = GenInferencer(                             │ │   model=model,                                          │ │   max_out_len=512,             # ← 从config分离出来   │ │   batch_size=8,                # ← 从config分离出来   │ │ )                                                       │ │                                                         │ │ inferencer.run() {                                      │ │   for batch in batches:                                 │ │     model.generate(                                     │ │       inputs=batch,                                     │ │       max_out_len=512          # ← 传递给generate()   │ │     )                                                   │ │ }                                                       │ └─────────────────────────────────────────────────────────┘ ```   `

---

### 第四步：核心设计模式

#### 4.1 注册表模式（Registry Pattern）

python

`   ``` # 模型类注册 @MODELS.register_module() class OpenAI(BaseAPIModel):     ...  # 注册表中的映射 MODELS._module_dict = {     'OpenAI': OpenAI,     'HuggingFacewithChatTemplate': HuggingFacewithChatTemplate,     'VLLM': VLLM,     'Qwen': Qwen,     ... }  # 使用时：MODELS.build({'type': 'OpenAI', ...}) ```   `

#### 4.2 模板方法模式（Template Method）

BaseModel定义骨架，子类实现细节：

python

`   ``` class BaseModel:     @abstractmethod     def generate(self, inputs, max_out_len):         """子类必须实现"""          def generate_from_template(self, templates, max_out_len):         """模板方法：定义流程"""         inputs = self.parse_template(templates, mode='gen')         return self.generate(inputs, max_out_len)  # ← 调用抽象方法 ```   `

#### 4.3 策略模式（Strategy Pattern）

Template Parser用不同策略处理本地/API模型：

python

`   ``` class LMTemplateParser:      # 策略1：本地模型     def parse_template(self, ...):         return str  # 返回字符串  class APITemplateParser:     # 策略2：API模型     def parse_template(self, ...):         return PromptList  # 返回列表 ```   `

#### 4.4 工厂模式（Factory）

build_model_from_cfg()充当工厂：

python

`   ``` def build_model_from_cfg(model_cfg):     # 根据type字段动态创建模型     return MODELS.build(model_cfg)  # ← 工厂方法 ```   `

---

### 第五步：**init**.py 导出结构

**文件路径**：`d:\project\opencompass_inner\opencompass\models\__init__.py`

**导出内容**（57行）：

|导出项|来源文件|分类|
|---|---|---|
|**基础类**|||
|`BaseModel`|base.py|本地模型基类|
|`LMTemplateParser`|base.py|本地模板解析器|
|`BaseAPIModel`|base_api.py|API模型基类|
|`APITemplateParser`|base_api.py|API模板解析器|
|**本地模型**|||
|`HuggingFace`, `HuggingFaceCausalLM`, `HuggingFaceChatGLM3`|huggingface.py|HF基础实现|
|`HuggingFaceBaseModel`, `HuggingFacewithChatTemplate`|huggingface_above_v4_33.py|HF ChatTemplate版本|
|`VLLM`|vllm.py|vLLM推理引擎|
|`VLLMwithChatTemplate`|vllm_with_tf_above_v4_33.py|vLLM ChatTemplate版本|
|`Llama2`, `Llama2Chat`|llama2.py|LLaMA2系列|
|`GLM130B`|glm.py|ChatGLM系列|
|`TurboMindModel`|turbomind.py|LMDeploy TurboMind|
|`TurboMindModelwithChatTemplate`|turbomind_with_tf_above_v4_33.py|TurboMind ChatTemplate|
|`InternLM`, `InternTrain`|intern_model.py, interntrain.py|InternLM系列|
|`Mixtral`, `ModelScope`, `AlayaLM`|其他|其他本地模型|
|**API模型**|||
|`OpenAI`, `OpenAISDK`, `OpenAISDKRollout`|openai_api.py|OpenAI API|
|`OpenAISDKStreaming`|openai_streaming.py|OpenAI流式|
|`Qwen`|qwen_api.py|通义千问API|
|`Claude`, `ClaudeSDK`, `ClaudeAllesAPIN`|claude_api/*, claude_sdk_api.py|Claude API|
|`DeepseekAPI`, `BaiChuan`, `ERNIEBot`, ...|其他_api.py \| 其他API模型 \|_|

---

### 第六步：模型配置参数详解与最佳实践

#### 6.1 参数生命周期

plaintext

`   ``` ┌──────────────────────────────────────────────────────────┐ │ 配置阶段 (Config)                                        │ ├──────────────────────────────────────────────────────────┤ │ max_out_len: 512        ← 最大输出长度                   │ │ batch_size: 8           ← 批处理大小                     │ │ generation_kwargs: {}   ← 生成参数                       │ │ meta_template: {}       ← 提示词模板                     │ │ query_per_second: 1     ← QPS限流 (API模型)             │ │ retry: 2                ← 重试次数 (API模型)            │ └──────────────────────────────────────────────────────────┘                 ↓ (build_model_from_cfg) ┌──────────────────────────────────────────────────────────┐ │ 移除参数阶段                                             │ ├──────────────────────────────────────────────────────────┤ │ ✗ max_out_len        ← 移除（Inferencer管理）          │ │ ✗ batch_size         ← 移除（Inferencer管理）          │ │ ✗ min_out_len        ← 移除（Inferencer管理）          │ │ ✗ run_cfg            ← 移除（元数据）                  │ │ ✗ abbr               ← 移除（元数据）                  │ │ ✓ generation_kwargs  ← 保留（传给model.__init__)        │ │ ✓ meta_template      ← 保留（传给model.__init__)        │ │ ✓ query_per_second   ← 保留（API模型使用）            │ │ ✓ ...其他模型参数    ← 保留（传给model.__init__)        │ └──────────────────────────────────────────────────────────┘                 ↓ (MODELS.build) ┌──────────────────────────────────────────────────────────┐ │ 模型初始化阶段                                           │ ├──────────────────────────────────────────────────────────┤ │ ModelClass.__init__(                                     │ │   path=...,                                              │ │   generation_kwargs={...},                               │ │   meta_template={...},                                   │ │   query_per_second=1,  ← [API模型]                      │ │ )                                                        │ │                                                          │ │ self.generation_kwargs = generation_kwargs  # 保存      │ │ self.template_parser = ...Parser()          # 初始化    │ └──────────────────────────────────────────────────────────┘                 ↓ (GenInferencer.__init__) ┌──────────────────────────────────────────────────────────┐ │ Inferencer初始化阶段                                     │ ├──────────────────────────────────────────────────────────┤ │ self.max_out_len = max_out_len    # 从config恢复        │ │ self.batch_size = batch_size      # 从config恢复        │ └──────────────────────────────────────────────────────────┘                 ↓ (run / inference) ┌──────────────────────────────────────────────────────────┐ │ 推理阶段                                                 │ ├──────────────────────────────────────────────────────────┤ │ model.generate(                                          │ │   inputs=...,                                            │ │   max_out_len=512     ← Inferencer传递                  │ │ )                                                        │ └──────────────────────────────────────────────────────────┘ ```   `

#### 6.2 参数兼容性矩阵

|参数|值类型|BaseModel|BaseAPIModel|HF/VLLM|OpenAI|Qwen|说明|
|---|---|---|---|---|---|---|---|
|------|--------|----------|--------------|---------|--------|------|------|
|`path`|str|✓|✓|✓|✓|✓|必需|
|`max_seq_len`|int|✓|✓|✓|✓|✓|默认2048|
|`meta_template`|Dict|✓|✓|✓|✓|✓|可选|
|`generation_kwargs`|Dict|✓|✓|✓|✓|✓|默认{}|
|`query_per_second`|int|✗|✓|✗|✓|✓|仅API模型|
|`retry`|int|✗|✓|✗|✓|✓|仅API模型|
|`tokenizer_only`|bool|✓|✗|✓|✗|✗|仅本地模型|
|`model_kwargs`|Dict|✗|✗|✓|✗|✗|HuggingFace专用|
|`use_fastchat_template`|bool|✗|✗|✓|✗|✗|vLLM/HF专用|

#### 6.3 常见配置错误及修复

**问题1**：`max_out_len` 直接传给模型构造函数

❌ **错误配置**：

python

`   ``` model_cfg = {     'type': 'OpenAI',     'path': 'gpt-4',     'max_out_len': 512,  # ← 直接在config中 } model = MODELS.build(model_cfg)  # TypeError！ ```   `

✅ **正确方式**：

python

`   ``` # 由build_model_from_cfg自动移除 model_cfg = {     'type': 'OpenAI',     'path': 'gpt-4',     'max_out_len': 512,  # ← 在config中可以，build时被移除 } model = build_model_from_cfg(model_cfg)  # OK inferencer = GenInferencer(model, max_out_len=512)  # ← 传给Inferencer ```   `

**问题2**：`batch_size` 在本地模型中无效

❌ **错误**：期望通过`batch_size`自动分批

✅ **正确**：`batch_size`由Inferencer控制，与模型无关

---

### 第七步：关键代码段参考

#### 代码片段1：模型构建流程

**文件**：`opencompass/utils/build.py`

python

`   ``` def build_model_from_cfg(model_cfg: ConfigDict):     """从配置构建模型实例"""     model_cfg = copy.deepcopy(model_cfg)          # 移除运行时参数（不传给model.__init__）     model_cfg.pop('run_cfg', None)     model_cfg.pop('max_out_len', None)     model_cfg.pop('batch_size', None)     model_cfg.pop('abbr', None)     model_cfg.pop('summarizer_abbr', None)     model_cfg.pop('pred_postprocessor', None)     model_cfg.pop('min_out_len', None)          # 调用注册表构建     return MODELS.build(model_cfg) ```   `

#### 代码片段2：BaseModel初始化

**文件**：`opencompass/models/base.py` 行34-50

python

`   ``` class BaseModel:     is_api: bool = False          def __init__(self,                  path: str,                  max_seq_len: int = 2048,                  tokenizer_only: bool = False,                  meta_template: Optional[Dict] = None,                  generation_kwargs: Optional[Dict] = dict(),                  sync_rank: bool = False):         self.path = path         self.max_seq_len = max_seq_len         self.tokenizer_only = tokenizer_only                  # 初始化模板解析器         self.template_parser = LMTemplateParser(meta_template)                  # 提取eos_token_id         self.eos_token_id = None         if meta_template and 'eos_token_id' in meta_template:             self.eos_token_id = meta_template['eos_token_id']                  self.generation_kwargs = generation_kwargs         self.sync_rank = sync_rank ```   `

#### 代码片段3：HuggingFace生成实现

**文件**：`opencompass/models/huggingface_above_v4_33.py`（推断）

python

`   ``` def generate(self, inputs: List[str], max_out_len: int, **kwargs) -> List[str]:     # 合并参数     generation_kwargs = {**self.generation_kwargs, **kwargs}          # 批处理或逐个     if self.batch_padding and len(inputs) > 1:         return self._batch_generate(inputs, max_out_len, generation_kwargs)     else:         results = []         for inp in inputs:             result = self._single_generate([inp], max_out_len, generation_kwargs)             results.extend(result)         return results  def _single_generate(self, inputs, max_out_len, gen_kwargs):     # 分词     tokens = self.tokenizer(inputs, return_tensors='pt', padding=True)          # 应用模式     if self.mode == 'mid':         # 截断中间         half = int((self.max_seq_len - max_out_len) / 2)         # ... truncate implementation          # 生成     outputs = self.model.generate(         **tokens,         max_new_tokens=max_out_len,  # 关键参数         **gen_kwargs     )          # 解码     return self.tokenizer.batch_decode(outputs, skip_special_tokens=True) ```   `

#### 代码片段4：OpenAI并发调用

**文件**：`opencompass/models/openai_api.py` 行165-202

python

`   ``` def generate(self, inputs: List[PromptType],               max_out_len: int = 512,              temperature: float = 0.7,              **kwargs) -> List[str]:     """并发生成"""     if self.temperature is not None:         temperature = self.temperature          with ThreadPoolExecutor(max_workers=self.max_workers) as executor:         results = list(             tqdm(                 executor.map(                     self._generate,                     inputs,                     [max_out_len] * len(inputs),                     [temperature] * len(inputs),                 ),                 total=len(inputs),                 desc='Inferencing',             ))     return results ```   `

#### 代码片段5：TokenBucket限流

**文件**：`opencompass/models/base_api.py` 行458-495

python

`   ``` class TokenBucket:     """实现QPS限流"""          def __init__(self, rate: float, verbose=False):         self._rate = rate  # queries per second         self._tokens = threading.Semaphore(0)  # 初始0个token         self.started = False         self._request_queue = Queue()         self.logger = get_logger()         self.verbose = verbose          def _add_tokens(self):         """后台线程：每秒添加rate个token"""         while True:             if self._tokens._value < self._rate:                 self._tokens.release()             sleep(1 / self._rate)          def get_token(self):         """获取一个token（阻塞直到可用）"""         if not self.started:             self.started = True             threading.Thread(target=self._add_tokens, daemon=True).start()         self._tokens.acquire()  # ← 关键：阻塞 ```   `

---

### 第八步：模块使用示例

#### 示例1：本地模型推理

python

`   ``` from opencompass.models import HuggingFacewithChatTemplate from opencompass.openicl.icl_inferencer import GenInferencer  # 1. 创建模型配置 model_cfg = {     'type': 'HuggingFacewithChatTemplate',     'path': 'Qwen/Qwen-7B-Chat',     'meta_template': {...},  # 模板配置     'generation_kwargs': {         'do_sample': True,         'top_p': 0.9,     },     'max_out_len': 512,      # ← 会被移除     'batch_size': 4,         # ← 会被移除 }  # 2. 构建模型 from opencompass.utils import build_model_from_cfg model = build_model_from_cfg(model_cfg) # build_model_from_cfg移除max_out_len和batch_size后构建  # 3. 创建推理器 inferencer = GenInferencer(     model=model,     max_out_len=512,          # ← 从config恢复     batch_size=4,             # ← 从config恢复 )  # 4. 推理 prompts = ['Hello', 'World'] results = inferencer.inference(prompts) ```   `

#### 示例2：API模型推理

python

`   ``` from opencompass.models import OpenAI  # 1. 配置 model_cfg = {     'type': 'OpenAI',     'path': 'gpt-4',     'key': 'ENV',              # 从OPENAI_API_KEY读取     'query_per_second': 10,    # ← 传给__init__     'max_seq_len': 8192,       # ← 传给__init__     'max_out_len': 1024,       # ← 会被移除 }  # 2. 构建 from opencompass.utils import build_model_from_cfg model = build_model_from_cfg(model_cfg)  # max_out_len被移除  # 3. 推理（可直接调用generate） results = model.generate(     ['Tell me about AI'],     max_out_len=1024  # ← 直接传给generate() ) ```   `

#### 示例3：模板解析

python

`   ``` from opencompass.models.base import LMTemplateParser  # 定义meta_template meta_template = {     'round': [         dict(role='HUMAN', api_role='HUMAN'),         dict(role='BOT', api_role='BOT', generate=True),     ],     'begin': '<|im_start|>system\n',     'end': '<|im_end|>', }  # 创建解析器 parser = LMTemplateParser(meta_template)  # 使用示例 prompt_template = [     dict(role='HUMAN', prompt='Hello'),     dict(role='BOT', prompt='')  # ← generate=True时停止 ]  # PPL模式：完整解析 ppl_text = parser.parse_template(prompt_template, mode='ppl') # 输出: '<|im_start|>system\n...Hello...BOT...'  # 生成模式：在BOT前停止 gen_text = parser.parse_template(prompt_template, mode='gen') # 输出: '<|im_start|>system\n...Hello...' ```   `

---

## 总结

OpenCompass Model 模块是一个**模块化、可扩展的模型封装框架**，具有以下核心特点：

1. **清晰的层次结构**：
    - `BaseModel` + `BaseAPIModel`：抽象层
    - 50+ 具