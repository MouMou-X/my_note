## 请求体
### 1. model  `string` （必选）
模型名称。
支持的模型：Qwen 大语言模型（商业版、开源版）、Qwen-VL、Qwen-Coder、千问Audio、数学模型。
**具体模型名称和计费，请参见**文本生成-千问。

---

### 2. messages `array`（必选）
传递给大模型的上下文，按对话顺序排列。
> 通过HTTP调用时，请将**messages** 放入 **input** 对象中。

**消息类型：**
#### 2.1 System Message`object`（可选）
系统消息，用于设定大模型的角色、语气、任务目标或约束条件等。一般放在`messages`数组的第一位。
> QwQ模型不建议设置 System Message，QVQ 模型设置 System Message不会生效。

**属性：**
##### 2.1.1 content `string`（必选）
消息内容。

##### 2.1.2 role `string` （必选）
系统消息的角色，固定为`system`。

#### 2.2 User Message`object`（必选）
用户消息，用于向模型传递问题、指令或上下文等。
**属性：**

##### content `string 或 array`（必选）
消息内容。若输入只有文本，则为 string 类型；若输入包含图像等多模态数据，或启用显式缓存，则为 array 类型。
**属性：**

###### text `string`（必选）
输入的文本。

###### image`string`（可选）
指定用于图片理解的图像文件，图像支持以下三种方式传入：
公网 URL：公网可访问的图像链接
图片的 Base64 编码，格式为 `data:image/<format>;base64,<data>`
本地文件：本地文件的绝对路径
适用模型：Qwen-VL、QVQ
示例值：`{"image":"https://xxxx.jpeg"}`

###### video`array 或 string`（可选）
使用Qwen-VL 模型或QVQ模型传入的视频。
若传入图像列表，则为`*array*`类型；
若传入视频文件，则为`*string*`类型*。*
传入本地文件请参见本地文件（Qwen-VL）或本地文件（QVQ）。
示例值：
图像列表：`{"video":["https://xx1.jpg",...,"https://xxn.jpg"]} `
视频文件：`{"video":"https://xxx.mp4"} `

###### fps`float`（可选）
每秒抽帧数。取值范围为 [0.1, 10]，默认值为2.0。
**功能说明**
fps有两个功能：
- 输入视频文件时，控制抽帧频率，每 fps1​秒抽取一帧。
	**适用于Qwen-VL 模型与QVQ模型。**
- 告知模型相邻帧之间的时间间隔，帮助其更好地理解视频的时间动态。同时适用于输入视频文件与图像列表时。该功能同时支持视频文件和图像列表输入，适用于事件时间定位或分段内容摘要等场景。
	**支持`Qwen2.5-VL`、`Qwen3-VL`模型与QVQ模型。**
较大的`fps`适合高速运动的场景（如体育赛事、动作电影等），较小的`fps`适合长视频或内容偏静态的场景。
**示例值**
图像列表传入：`{"video":["https://xx1.jpg",...,"https://xxn.jpg"]，"fps":2}`
视频文件传入：`{"video": "https://xx1.mp4"，"fps":2}`

###### max_frames`integer`（可选）
视频抽取帧数的上限。当按`fps`计算的帧数超过 `max_frames`时，系统将自动调整为：在`max_frames`内均匀抽帧，确保总帧数不超过限制。
**取值范围**
`qwen3-vl-plus`系列、`qwen3-vl-flash`系列、`qwen3-vl-235b-a22b-thinking`、`qwen3-vl-235b-a22b-instruct`：最大值和默认值均为 2000
`qwen-vl-max`、`qwen-vl-max-latest`、`qwen-vl-max-0813`、`qwen-vl-plus`、`qwen-vl-plus-latest`、`qwen-vl-plus-0815``、qwen-vl-plus-0710`：最大值和默认值均为 512。
**示例值**
`{"type": "video_url","video_url": {"url":"https://xxxx.mp4"},"max_frame": 2000}`
**使用 OpenAI 兼容API调用时，不支持自定义`max_frames`参数，API 将自动使用各模型对应的默认值。**

###### min_pixels`integer`（可选）
设定输入图像或视频帧的最小像素阈值。当输入图像或视频帧的像素小于`min_pixels`时，会将其进行放大，直到总像素高于`min_pixels`。
**取值范围**
- **输入图像：**
	`Qwen3-VL`：默认值和最小值均为：`65536`
	`qwen-vl-max`、`qwen-vl-max-latest`、`qwen-vl-max-0813`、`qwen-vl-plus`、`qwen-vl-plus-latest`、`qwen-vl-plus-0815``、qwen-vl-plus-0710`：默认值和最小值均为`4096`
	其他`qwen-vl-plus`模型、其他`qwen-vl-max`模型、`Qwen2.5-VL`开源系列及`QVQ`系列模型：默认值和最小值均为`3136`
- **输入视频文件或图像列表：**
	Qwen3-VL（包括商业版和开源版）、`qwen-vl-max`、`qwen-vl-max-latest`、`qwen-vl-max-0813`、`qwen-vl-plus`、`qwen-vl-plus-latest`、`qwen-vl-plus-0815``、qwen-vl-plus-0710`：默认值为`65536`，最小值为`4096`
	其他`qwen-vl-plus`模型、其他`qwen-vl-max`模型、`Qwen2.5-VL`开源系列及`QVQ`系列模型：默认值为`50176`，最小值为`3136`
**示例值**
- 输入图像：`{"type": "image_url","image_url": {"url":"https://xxxx.jpg"},"min_pixels": 65536}`
- 输入视频文件时：`{"type": "video_url","video_url": {"url":"https://xxxx.mp4"},"min_pixels": 65536}`
- 输入图像列表时：`{"type": "video","video": ["https://xx1.jpg",...,"https://xxn.jpg"],"min_pixels": 65536}`

###### max_pixels`integer` （可选）
用于设定输入图像或视频帧的最大像素阈值。当输入图像或视频的像素在`[min_pixels, max_pixels]`区间内时，模型会按原图进行识别。当输入图像像素大于`max_pixels`时，会将图像进行缩小，直到总像素低于`max_pixels`。
**取值范围**
- **输入图像：**
  `max_pixels` 的取值与是否开启`vl_high_resolution_images`参数有关。
	- 当`vl_high_resolution_images`为`False`时：
		- `Qwen3-VL`：默认值为`2621440`，最大值为：`16777216`
		- `qwen-vl-max`、`qwen-vl-max-latest`、`qwen-vl-max-0813`、`qwen-vl-plus`、`qwen-vl-plus-latest`、`qwen-vl-plus-0815``、qwen-vl-plus-0710`：默认值为`1310720`，最大值为：`16777216`
		- 其他`qwen-vl-plus`模型、其他`qwen-vl-max`模型、`Qwen2.5-VL`开源系列及`QVQ`系列模型：默认值为`1003520`  ，最大值为`12845056`
	- 当`vl_high_resolution_images`为`True`时：
		- `Qwen3-VL`、`qwen-vl-max`、`qwen-vl-max-latest`、`qwen-vl-max-0813`、`qwen-vl-plus`、`qwen-vl-plus-latest`、`qwen-vl-plus-0815``、qwen-vl-plus-0710`：`max_pixels`无效，输入图像的最大像素固定为`16777216`
		- 其他`qwen-vl-plus`模型、其他`qwen-vl-max`模型、`Qwen2.5-VL`开源系列及`QVQ`系列模型：`max_pixels`无效，输入图像的最大像素固定为`12845056`
- **输入视频文件或图像列表：**
	- `qwen3-vl-plus`系列、`qwen3-vl-flash`系列、`qwen3-vl-235b-a22b-thinking`、`qwen3-vl-235b-a22b-instruct`：默认值为`655360`，最大值为`2048000`
	- 其他`Qwen3-VL`开源模型、`qwen-vl-max`、`qwen-vl-max-latest`、`qwen-vl-max-0813`、`qwen-vl-plus`、`qwen-vl-plus-latest`、`qwen-vl-plus-0815``、qwen-vl-plus-0710`：默认值`655360`，最大值为`786432`
	- 其他`qwen-vl-plus`模型、其他`qwen-vl-max`模型、`Qwen2.5-VL`开源系列及`QVQ`系列模型：默认值为`501760`，最大值为`602112`
**示例值**
- 输入图像：`{"type": "image_url","image_url": {"url":"https://xxxx.jpg"},"max_pixels": 8388608}`
- 输入视频文件时：`{"type": "video_url","video_url": {"url":"https://xxxx.mp4"},"max_pixels": 655360}`
- 输入图像列表时：`{"type": "video","video": ["https://xx1.jpg",...,"https://xxn.jpg"],"max_pixels": 655360}`

###### total_pixels`integer`（可选）
用于限制从视频中抽取的所有帧的总像素（单帧图像像素 × 总帧数）。如果视频总像素超过此限制，系统将对视频帧进行缩放，但仍会确保单帧图像的像素值在`[min_pixels, max_pixels]`范围内。适用于 Qwen-VL、QVQ 模型。
对于抽帧数量较多的长视频，可适当降低此值以减少Token消耗和处理时间，但这可能会导致图像细节丢失。
**取值范围**
- `qwen3-vl-plus`系列、`qwen3-vl-flash`系列、`qwen3-vl-235b-a22b-thinking`、`qwen3-vl-235b-a22b-instruct`：默认值和最小值均为134217728，该值对应 `131072` 个图像 Token（每 32×32 像素对应 1 个图像 Token）。
- 其他`Qwen3-VL`开源模型、`qwen-vl-max`、`qwen-vl-max-latest`、`qwen-vl-max-0813`、`qwen-vl-plus`、`qwen-vl-plus-latest`、`qwen-vl-plus-0815``、qwen-vl-plus-0710`：默认值和最小值均为`67108864`，该值对应 `65536` 个图像 Token（每 32×32 像素对应 1 个图像 Token）。
- 其他`qwen-vl-plus`模型、其他`qwen-vl-max`模型、`Qwen2.5-VL`开源系列及`QVQ`系列模型：默认值和最小值均为`51380224`，该值对应 `65536` 个图像 Token（每 28×28 像素对应 1 个图像 Token）。
**示例值**
- 输入视频文件时：`{"type": "video_url","video_url": {"url":"https://xxxx.mp4"},"total_pixels": 134217728}`
- 输入图像列表时：`{"type": "video","video": ["https://xx1.jpg",...,"https://xxn.jpg"],"total_pixels": 134217728}`

###### audio`string`
**模型为音频理解时，是必选参数，如模型为qwen2-audio-instruct等。**
使用音频理解功能时，传入的音频文件。
示例值：`{"audio":"https://xxx.mp3"}`

###### cache_control`object` （可选）
仅支持显式缓存的模型支持，用于开启显式缓存。
**属性**
- **type** `*string*`**（必选）**
	固定为`ephemeral`。

##### role`string`（必选）
用户消息的角色，固定为`user`。

#### 2.3 Assistant Message `object`（可选）
模型对用户消息的回复。
**属性**

##### 2.3.1 content `string`（可选）
消息内容。仅当助手消息中指定`tool_calls`参数时非必选。

##### 2.3.2 role`string` （必选）
固定为`assistant`。

##### 2.3.3 partial`boolean` （可选）
是否开启前缀续写。相关文档：前缀续写。
**支持的模型**
- **千问Max 系列**
	qwen3-max、qwen3-max-2025-09-23、qwen3-max-preview（非思考模式）、qwen-max、qwen-max-latest、qwen-max-2024-09-19及之后的快照模型
- **千问Plus 系列（非思考模式）**
	qwen-plus、qwen-plus-latest、qwen-plus-2024-12-20及之后的快照模型
- **千问Flash 系列（非思考模式）**
	qwen-flash、qwen-flash-2025-07-28及之后的快照模型
- **千问Coder 系列**
	qwen3-coder-plus、qwen3-coder-flash、qwen3-coder-480b-a35b-instruct、qwen3-coder-30b-a3b-instruct、qwen-coder-plus、qwen-coder-plus-latest、qwen-coder-plus-2024-11-06、qwen-coder-turbo、qwen-coder-turbo-latest、qwen-coder-turbo-2024-09-19、qwen2.5-coder-32b-instruct、qwen2.5-coder-14b-instruct、qwen2.5-coder-7b-instruct、qwen2.5-coder-3b-instruct、qwen2.5-coder-1.5b-instruct、qwen2.5-coder-0.5b-instruct
- **千问VL 系列**
	- **qwen3-vl-plus 系列（非思考模式）**
		qwen3-vl-plus、qwen3-vl-plus-2025-09-23及之后的快照模型
	- **qwen3-vl-flash 系列（非思考模式）**
		qwen3-vl-flash、qwen3-vl-flash-2025-10-15及之后的快照模型
	- **qwen-vl-max 系列**
		qwen-vl-max、qwen-vl-max-latest、qwen-vl-max-2024-11-19及之后的快照模型
	- **qwen-vl-plus 系列**
		qwen-vl-plus、qwen-vl-plus-latest、qwen-vl-plus-2025-01-02及之后的快照模型
- **千问Turbo 系列（非思考模式）**
	qwen-turbo、qwen-turbo-latest、qwen-turbo-2024-11-01及之后的快照模型
- **千问开源系列**
	Qwen3 开源模型（非思考模式）、qwen2.5-72b-instruct、qwen2.5-32b-instruct、qwen2.5-14b-instruct、qwen2.5-7b-instruct、qwen2.5-3b-instruct、qwen2.5-1.5b-instruct、qwen2.5-0.5b-instruct、Qwen3-VL开源模型（非思考模式）
- **千问Math 系列**
qwen-math-plus、qwen-math-plus-latest、qwen-math-plus-0919、qwen-math-turbo、qwen-math-turbo-latest、qwen-math-turbo-0919、qwen2.5-math-72b-instruct、qwen2.5-math-7b-instruct、qwen2.5-math-1.5b-instruct

##### 2.3.4 tool_calls`array`（可选）
发起 Function Calling 后，返回的工具与入参信息，包含一个或多个对象。由上一轮模型响应的`tool_calls`字段获得。
**属性**

###### id `string`
工具响应的ID。

###### type `string`
工具类型，当前只支持设为`function`。

###### function `object`
工具与入参信息。
**属性**
####### name `string`
工具名称。
####### arguments `string`
入参信息，为JSON格式字符串。

###### index `integer`
当前工具信息在`tool_calls`数组中的索引。

#### 2.4 Tool Message `object`（可选）
工具的输出信息。
**属性**
##### 2.4.1 content `string` （必选）
工具函数的输出内容，必须为字符串格式。

##### 2.4.2 role `string` （必选）
固定为`tool`。

##### 2.4.3 tool_call_id `string` （可选）
发起 Function Calling 后返回的 id，可以通过`response.output.choices[0].message.tool_calls[$index]["id"]`获取，用于标记 Tool Message 对应的工具。

  

### 3. temperature `float`（可选）
采样温度，控制模型生成文本的多样性。
temperature越高，生成的文本更多样，反之，生成的文本更确定。
取值范围： [0, 2)
**temperature默认值**:
- Qwen3（非思考模式）、Qwen3-Instruct系列、Qwen3-Coder系列、qwen-max系列、qwen-plus系列（非思考模式）、qwen-flash系列（非思考模式）、qwen-turbo系列（非思考模式）、qwen开源系列、qwen-coder系列、qwen2-audio-instruct、qwen-doc-turbo、qwen-vl-max-2025-08-13、Qwen3-VL（非思考）：0.7；
- QVQ系列 、qwen-vl-plus-2025-07-10、qwen-vl-plus-2025-08-15 : 0.5；
- qwen-audio-turbo系列：0.00001；
- qwen-vl系列、qwen2.5-omni-7b、qvq-72b-preview：0.01；
- qwen-math系列：0；
- Qwen3（思考模式）、Qwen3-Thinking、Qwen3-Omni-Captioner、QwQ 系列：0.6；
- qwen3-max-preview（思考模式）、qwen-long系列： 1.0；
- qwen-plus-character：0.92
- qwen3-omni-flash系列：0.9
- Qwen3-VL（思考模式）：0.8
**通过HTTP调用时，请将 temperature 放入 parameters 对象中。**
**不建议修改QVQ模型的默认 temperature 值。**


### 4. top_p `float`（可选）
核采样的概率阈值，控制模型生成文本的多样性。
top_p越高，生成的文本更多样。反之，生成的文本更确定。
取值范围：（0,1.0]。
**top_p默认值**
- Qwen3（非思考模式）、Qwen3-Instruct系列、Qwen3-Coder系列、qwen-max系列、qwen-plus系列（非思考模式）、qwen-flash系列（非思考模式）、qwen-turbo系列（非思考模式）、qwen开源系列、qwen-coder系列、qwen-long、qwen-doc-turbo、qwq-32b-preview、qwen-audio-turbo系列、qwen-vl-max-2025-08-13、Qwen3-VL（非思考模式）：0.8；
- qwen-vl-max-2024-11-19、qwen2-vl-72b-instruct、qwen-omni-turbo 系列：0.01；
- qwen-vl-plus系列、qwen-vl-max、qwen-vl-max-latest、qwen-vl-max-2025-04-08、qwen-vl-max-2025-04-02、qwen-vl-max-2025-01-25、qwen-vl-max-2024-12-30、qvq-72b-preview、qwen2-vl-2b-instruct、qwen2-vl-7b-instruct、qwen2.5-vl-3b-instruct、qwen2.5-vl-7b-instruct、qwen2.5-vl-32b-instruct、qwen2.5-vl-72b-instruct：0.001；
- QVQ系列、qwen-vl-plus-2025-07-10、qwen-vl-plus-2025-08-15 、qwen2-audio-instruct：0.5；
- qwen3-max-preview（思考模式）、qwen-math系列、Qwen3-Omni-Flash系列：1.0；
- Qwen3（思考模式）、Qwen3-VL（思考模式）、Qwen3-Thinking、QwQ 系列、Qwen3-Omni-Captioner、qwen-plus-character：0.95
**Java SDK中为topP。通过HTTP调用时，请将 top_p 放入 parameters对象中。**
**不建议修改QVQ模型的默认 top_p 值。**

### 5. top_k `integer`（可选）
生成过程中采样候选集的大小。例如，取值为50时，仅将单次生成中得分最高的50个Token组成随机采样的候选集。取值越大，生成的随机性越高；取值越小，生成的确定性越高。取值为None或当top_k大于100时，表示不启用top_k策略，此时仅有top_p策略生效。
取值需要大于或等于0。
**top_k默认值**
- QVQ系列、qwen-vl-plus-2025-07-10、qwen-vl-plus-2025-08-15：10；
- QwQ 系列：40；
- qwen-math 系列、其余qwen-vl-plus系列、qwen-vl-max-2025-08-13之前的模型、qwen-audio-turbo系列、qwen2.5-omni-7b、qvq-72b-preview：1；
- Qwen3-Omni-Flash系列：50
- 其余模型均为20；
**Java SDK中为topK。通过HTTP调用时，请将 top_k 放入 parameters 对象中。**
**不建议修改QVQ模型的默认 top_k 值。**

### 6. enable_thinking `boolean` （可选）
使用混合思考模型时，是否开启思考模式，适用于 Qwen3 、Qwen3-VL模型。相关文档：深度思考
可选值：
`true`：开启
**开启后，思考内容将通过`reasoning_content`字段返回。**
`false`：不开启
不同模型的默认值：支持的模型
**Java SDK 为enableThinking；通过HTTP调用时，请将 enable_thinking放入 parameters 对象中。

### 7. thinking_budget `integer` （可选）
思考过程的最大长度。适用于Qwen3-VL、Qwen3 的商业版与开源版模型。相关文档：限制思考长度。
默认值为模型最大思维链长度，请参见：模型列表
**Java SDK 为 thinkingBudget。通过HTTP调用时，请将 thinking_budget 放入 parameters 对象中。**
**默认值为模型最大思维链长度。**

### 8. enable_code_interpreter `boolean` （可选）默认值为 `false`
是否开启代码解释器功能。仅支持思考模式下的 qwen3-max与 qwen3-max-2026-01-23、qwen3-max-preview。相关文档：代码解释器
可选值：
`true`：开启
`false`：不开启
**不支持 Java SDK。通过HTTP调用时，请将 enable_code_interpreter 放入 parameters 对象中。**

### 9. repetition_penalty `float` （可选）
模型生成时连续序列中的重复度。提高repetition_penalty时可以降低模型生成的重复度，1.0表示不做惩罚。没有严格的取值范围，只要大于0即可。
**repetition_penalty默认值**
- qwen-max、qwen-max-latest、qwen-max-2024-09-19、qwen-math系列、qwen-vl-max系列、qvq-72b-preview、qwen2-vl-72b-instruct、qwen-vl-plus-2025-01-02、qwen-vl-plus-2025-05-07、qwen-vl-plus-2025-07-10、qwen-vl-plus-2025-08-15、qwen-vl-plus-latest、qwen2.5-vl-3b-instruct、qwen2.5-vl-7b-instruct、qwen2.5-vl-32b-instruct、qwen2.5-vl-72b-instruct、qwen-audio-turbo系列、QVQ系列、QwQ系列、qwq-32b-preview、Qwen3-VL： 1.0；
- qwen-coder系列、qwen2.5-1.5b-instruct、qwen2.5-0.5b-instruct、qwen2-1.5b-instruct、qwen2-0.5b-instruct、qwen2-vl-2b-instruct、qwen2-vl-7b-instruct、qwen2.5-omni-7b、qwen2-audio-instruct：1.1；
- qwen-vl-plus、qwen-vl-plus-2025-01-25：1.2；
- 其余模型为1.05。
**Java SDK中为repetitionPenalty。通过HTTP调用时，请将 repetition_penalty 放入 parameters 对象中。**
**使用qwen-vl-plus_2025-01-25模型进行文字提取时，建议设置repetition_penalty为1.0。**
**不建议修改QVQ模型的默认 repetition_penalty 值。**

### 10. presence_penalty `float`（可选）
控制模型生成文本时的内容重复度。
取值范围：[-2.0, 2.0]。正值降低重复度，负值增加重复度。
在创意写作或头脑风暴等需要多样性、趣味性或创造力的场景中，建议调高该值；在技术文档或正式文本等强调一致性与术语准确性的场景中，建议调低该值。
**presence_penalty默认值**
- qwen3-max-preview（思考模式）、Qwen3（非思考模式）、Qwen3-Instruct系列、qwen3-0.6b/1.7b/4b（思考模式）、QVQ系列、qwen-max、qwen-max-latest、qwen-max-latest、qwen-max-2024-09-19、qwen2.5-vl系列、qwen-vl-max系列、qwen-vl-plus、qwen2-vl-72b-instruct、qwen-vl-plus-2025-01-02、Qwen3-VL（非思考）：1.5；
- qwen-vl-plus-latest、qwen-vl-plus-2025-08-15、qwen-vl-plus-2025-07-10：1.2
- qwen-vl-plus-2025-01-25：1.0；
- qwen3-8b/14b/32b/30b-a3b/235b-a22b（思考模式）、qwen-plus/qwen-plus-latest/2025-04-28（思考模式）、qwen-turbo/qwen-turbo/2025-04-28（思考模式）：0.5；
- 其余均为0.0。
**原理介绍**
	如果参数值是正数，模型将对目前文本中已存在的Token施加一个惩罚值（惩罚值与文本出现的次数无关），减少这些Token重复出现的几率，从而减少内容重复度，增加用词多样性。
**示例**
	提示词：把这句话翻译成中文“This movie is good. The plot is good, the acting is good, the music is good, and overall, the whole movie is just good. It is really good, in fact. The plot is so good, and the acting is so good, and the music is so good.”
	参数值为2.0：这部电影很好。剧情很棒，演技棒，音乐也非常好听，总的来说，整部电影都好得不得了。实际上它真的很优秀。剧情非常精彩，演技出色，音乐也是那么的动听。
	参数值为0.0：这部电影很好。剧情好，演技好，音乐也好，总的来说，整部电影都很好。事实上，它真的很棒。剧情非常好，演技也非常出色，音乐也同样优秀。
	参数值为-2.0：这部电影很好。情节很好，演技很好，音乐也很好，总的来说，整部电影都很好。实际上，它真的很棒。情节非常好，演技也非常好，音乐也非常好。
**使用qwen-vl-plus-2025-01-25模型进行文字提取时，建议设置presence_penalty为1.5。不建议修改QVQ模型的默认presence_penalty值。**
**Java SDK不支持设置该参数。通过HTTP调用时，请将 presence_penalty 放入 parameters 对象中。

### 11. vl_high_resolution_images `boolean`（可选）默认值为`false`
是否将输入图像的像素上限提升至 16384 Token 对应的像素值。相关文档：处理高分辨率图像。
- `vl_high_resolution_images：true`，使用固定分辨率策略，忽略 `max_pixels` 设置，超过此分辨率时会将图像总像素缩小至此上限内。
**点击查看各模型像素上限**
	- `vl_high_resolution_images`为`True`时，不同模型像素上限不同：
	- `Qwen3-VL系列`、`qwen-vl-max`、`qwen-vl-max-latest`、`qwen-vl-max-0813`、`qwen-vl-plus`、`qwen-vl-plus-latest`、`qwen-vl-plus-0815``、qwen-vl-plus-0710`模型：`16777216`（每`Token`对应`32*32`像素，即`16384*32*32`）
	- `QVQ系列`、其他`Qwen2.5-VL系列`模型：`12845056`（每`Token`对应`28*28`像素，即 `16384*28*28`）
- `vl_high_resolution_images`为`false`，像素上限由 `max_pixels` 决定，输入图像的像素超过`max_pixels`会将图像缩小至`max_pixels`内。各模型的默认像素上限即`max_pixels`的默认值。
**Java SDK 为 vlHighResolutionImages（需要的最低版本为2.20.8）。通过HTTP调用时，请将 vl_high_resolution_images 放入 parameters 对象中。

### 12. vl_enable_image_hw_output `boolean`（可选）默认值为 `false`
是否返回图像缩放后的尺寸。模型会对输入的图像进行缩放处理，配置为 True 时会返回图像缩放后的高度和宽度，开启流式输出时，该信息在最后一个数据块（chunk）中返回。支持Qwen-VL模型。
**Java SDK中为 vlEnableImageHwOutput，Java SDK最低版本为2.20.8。通过HTTP调用时，请将 vl_enable_image_hw_output 放入 parameters 对象中。

### 13. max_tokens `integer`（可选）
用于限制模型输出的最大 Token 数。若生成内容超过此值，生成将提前停止，且返回的`finish_reason`为`length`。
默认值与最大值均为模型的最大输出长度，请参见文本生成-千问。
适用于需控制输出长度的场景，如生成摘要、关键词，或用于降低成本、缩短响应时间。
触发 `max_tokens `时，响应的 finish_reason 字段为 `length`。
**`max_tokens`不限制思考模型思维链的长度。**
**Java SDK中为maxTokens（模型为千问VL/Audio时，Java SDK中为maxLength，在 2.18.4 版本之后支持也设置为 maxTokens）。通过HTTP调用时，请将 max_tokens 放入 parameters 对象中。

### 14. seed `integer`（可选）
随机数种子。用于确保在相同输入和参数下生成结果可复现。若调用时传入相同的 `seed` 且其他参数不变，模型将尽可能返回相同结果。
取值范围：`[0,2^31−1]`。
**seed默认值**
- qwen-vl-plus-2025-01-02、qwen-vl-max、qwen-vl-max-latest、qwen-vl-max-2025-04-08、qwen-vl-max-2025-04-02、qwen-vl-max-2024-12-30、qvq-72b-preview、qvq-max系列：3407；
- qwen-vl-max-2025-01-25、qwen-vl-max-2024-11-19、qwen-vl-max-2024-02-01、qwen2-vl-72b-instruct、qwen2-vl-2b-instruct、qwen-vl-plus、qwen-vl-plus-latest、qwen-vl-plus-2025-05-07、qwen-vl-plus-2025-01-25：无默认值；
- 其余模型均为1234。
**通过HTTP调用时，请将 seed 放入 parameters 对象中。

### 15. stream `boolean`（可选）默认值为`false`
是否流式输出回复。参数值：
false：模型生成完所有内容后一次性返回结果。
true：边生成边输出，即每生成一部分内容就立即输出一个片段（chunk）。
**该参数仅支持Python SDK。通过Java SDK实现流式输出请通过`streamCall`接口调用；通过HTTP实现流式输出请在Header中指定`X-DashScope-SSE`为`enable`。**
**Qwen3商业版（思考模式）、Qwen3开源版、QwQ、QVQ只支持流式输出。 **

### 16. incremental_output `boolean`（可选）
默认为`false`（Qwen3-Max、Qwen3-VL、Qwen3 开源版、QwQ 、QVQ模型默认值为 `true`）
在流式输出模式下是否开启增量输出。推荐您优先设置为`true`。
参数值：
- false：每次输出为当前已经生成的整个序列，最后一次输出为生成的完整结果。
```
I
I like
I like apple
I like apple.
```
- true（推荐）：增量输出，即后续输出内容不包含已输出的内容。您需要实时地逐个读取这些片段以获得完整的结果。
```
I
like
apple
.
```
**Java SDK中为incrementalOutput。通过HTTP调用时，请将 incremental_output 放入 parameters 对象中。
**QwQ 模型与思考模式下的 Qwen3 模型只支持设置为 `true`。由于 Qwen3 商业版模型默认值为`false`，您需要在思考模式下手动设置为 `true`。**
**Qwen3 开源版模型不支持设置为 `false`。**

### 16. response_format `object` （可选） 默认值为`{"type": "text"}`
返回内容的格式。可选值：
`{"type": "text"}`：输出文字回复；
`{"type": "json_object"}`：输出标准格式的JSON字符串。
`{"type": "json_schema","json_schema": {...} }`：输出指定格式的JSON字符串。
**相关文档：结构化输出。**
**支持的模型参见[支持的模型](https://help.aliyun.com/zh/model-studio/qwen-structured-output?spm=a2c4g.11186623.0.0.174d220f1NOZBu#7a8e438e89xeq)。**
**若指定为`{"type": "json_object"}`，需在提示词中明确指示模型输出JSON，如：“请按照json格式输出”，否则会报错。**
**Java SDK中为responseFormat。通过HTTP调用时，请将 response_format 放入 parameters 对象中。
**属性**
#### 16.1 type `string`（必选）
返回内容的格式。可选值：
`text`：输出文字回复；
`json_object`：输出标准格式的JSON字符串；
`json_schema`：输出指定格式的JSON字符串。

#### 16.2 json_schema `object`
当 type 为 json_schema 时，该字段为必选，用于定义结构化输出的配置。
**属性**
##### 16.2.1 name `string` （必选）
Schema 的唯一标识名称。仅支持字母（不区分大小写）、数字、下划线和短横线，最长 64 个字符。

##### 16.2.2 description `string`（可选）
描述 Schema 的用途，帮助模型理解输出的语义上下文。

##### 16.2.3 schema `object`（可选）
符合 JSON Schema 标准的对象，定义模型输出的数据结构。
**构建JSON Schema 方法参加：[JSON Schema](https://json-schema.org/)**

##### 16.2.4 strict `boolean` （可选）默认值为`false`
控制是否强制模型严格遵守 Schema 的所有约束。
**true（推荐）**
模型严格遵循字段类型、必填项、格式等所有约束，确保输出 100% 合规。
**false（不推荐）**
模型仅大致遵循 Schema，可能生成不符合规范的输出，导致验证失败。

### 17. result_format `string`（可选）
默认为`text`（Qwen3-Max、Qwen3-VL、QwQ 模型、Qwen3 开源模型（除了qwen3-next-80b-a3b-instruct）与 Qwen-Long 模型默认值为 message）
返回数据的格式。推荐您优先设置为`message`，可以更方便地进行多轮对话。
- **平台后续将统一调整默认值为`message`。**
- **Java SDK中为**resultFormat***。*通过HTTP调用时，请将 **result_format **放入 **parameters** 对象中。**
- **模型为千问VL/QVQ/Audio时，设置`text`不生效。**
- **Qwen3-Max、Qwen3-VL、思考模式下的 Qwen3 模型只能设置为`message`，由于 Qwen3 商业版模型默认值为`text`，您需要将其设置为`message`。**
- **如果您使用 Java SDK 调用Qwen3 开源模型，并且传入了 `text`，依然会以 `message`格式进行返回。**

### 18. logprobs `boolean` （可选）默认值为 `false`
是否返回输出 Token 的对数概率，可选值：
- `true`
	返回
- `false`
	不返回
支持以下模型：
- qwen-plus系列的快照模型（不包含稳定版模型）
- qwen-turbo 系列的快照模型（不包含稳定版模型）
- qwen3-vl-plus系列（包含稳定版模型）
- qwen3-vl-flash系列（包含稳定版模型）
- Qwen3 开源模型
**通过HTTP调用时，请将 **logprobs **放入 **parameters** 对象中。**

### 19. top_logprobs `integer` （可选）默认值为0
指定在每一步生成时，返回模型最大概率的候选 Token 个数。
取值范围：[0,5]
仅当 `logprobs` 为 `true` 时生效。
**Java SDK中为**topLogprobs**。通过HTTP调用时，请将 **top_logprobs** 放入 **parameters** 对象中。

### 20. n `integer`（可选） 默认值为1
生成响应的个数，取值范围是`1-4`。对于需要生成多个响应的场景（如创意写作、广告文案等），可以设置较大的 n 值。
**当前仅支持 Qwen3（非思考模式）、qwen-plus-character 模型，且在传入 tools 参数时固定为1。**
**设置较大的 n 值不会增加输入 Token 消耗，会增加输出 Token 的消耗。**
**通过HTTP调用时，请将 n放入 parameters 对象中。**

### 21. stop `string 或 array `（可选）
用于指定停止词。当模型生成的文本中出现`stop` 指定的字符串或`token_id`时，生成将立即终止。
可传入敏感词以控制模型的输出。
**stop为数组时，不可将`token_id`和字符串同时作为元素输入，比如不可以指定为`["你好",104307]`。**
**通过HTTP调用时，请将 stop 放入 parameters 对象中。**

### 22. tools `array`（可选）
包含一个或多个工具对象的数组，供模型在 Function Calling 中调用。相关文档：Function Calling
使用 `tools` 时，必须将`result_format`设为`message`。
发起 Function Calling，或提交工具执行结果时，都必须设置`tools`参数。
**属性**
#### 22.1 type `string`（必选）
工具类型，当前仅支持`function`。

#### 22.2 function `object`（必选）
**属性**
##### 22.2.1 name `string` （必选）
工具函数的名称，必须是字母、数字，可以包含下划线和短划线，最大长度为64。

##### 22.2.2 description `string` （必选）
工具函数的描述，供模型选择何时以及如何调用工具函数。

##### 22.2.3 parameters `object`（可选）默认值为 `{}`
工具的参数描述，需要是一个合法的JSON Schema。JSON Schema的描述可以见链接。若`parameters`参数为空，表示该工具没有入参（如时间查询工具）。
**为提高工具调用的准确性，建议传入 `parameters`。**

**通过HTTP调用时，请将 tools 放入 parameters 对象中。暂时不支持qwen-vl与qwen-audio系列模型。**

#### 22.3 tool_choice `string 或 object `（可选）默认值为 `auto`
工具选择策略。若需对某类问题强制指定工具调用方式（例如始终使用某工具或禁用所有工具），可设置此参数。
- `auto`
大模型自主选择工具策略；
- `none`
若在特定请求中希望临时禁用工具调用，可设定`tool_choice`参数为`none`；
- `{"type": "function", "function": {"name": "the_function_to_call"}}`
若希望强制调用某个工具，可设定`tool_choice`参数为`{"type": "function", "function": {"name": "the_function_to_call"}}`，其中`the_function_to_call`是指定的工具函数名称。
**思考模式的模型不支持强制调用某个工具。**

**Java SDK中为toolChoice。通过HTTP调用时，请将 tool_choice 放入 parameters 对象中。**

#### 22.4 parallel_tool_calls `boolean` （可选）默认值为 `false`
是否开启并行工具调用。
可选值：
`true`：开启
`false`：不开启。
并行工具调用详情请参见：[并行工具调用](https://help.aliyun.com/zh/model-studio/qwen-function-calling?spm=a2c4g.11186623.0.0.174d240a79HpEr#cb6b5c484bt4x)。
**Java SDK中为parallelToolCalls。通过HTTP调用时，请将 parallel_tool_calls 放入 parameters 对象中。**
  

#### 22.5 enable_search `boolean`（可选）默认值为`false`
模型在生成文本时是否使用互联网搜索结果进行参考。取值如下：
- true：启用互联网搜索，模型会将搜索结果作为文本生成过程中的参考信息，但模型会基于其内部逻辑判断是否使用互联网搜索结果。
	**若开启后未联网搜索，可优化提示词，或设置`search_options`中的`forced_search`参数开启强制搜索。**
- false：关闭互联网搜索。
计费信息请参见计费说明。
**Java SDK中为enableSearch。通过HTTP调用时，请将 enable_search 放入 parameters 对象中。**
**启用互联网搜索功能可能会增加 Token 的消耗。**

#### 22.6 search_options `object`（可选）
联网搜索的策略。仅当`enable_search`为`true`时生效。详情参见联网搜索。
**通过HTTP调用时，请将 search_options 放入 parameters 对象中。Java SDK中为searchOptions。**
**属性**
##### 22.6.1 enable_source `boolean`（可选）默认值为`false`
在返回结果中是否展示搜索到的信息。参数值：
true：展示；
false：不展示。

##### 22.6.2 enable_citation `boolean`（可选）默认值为`false`
是否开启[1]或[ref_1]样式的角标标注功能。在`enable_source`为`true`时生效。参数值：
true：开启；
false：不开启。

##### 22.6.3 citation_format `string`（可选）默认值为`"[<number>]"`
角标样式。在`enable_citation`为`true`时生效。参数值：
- `[<number>]`：角标形式为`[1]`；
- `[ref_<number>]`：角标形式为`[ref_1]`。

##### 22.6.4 forced_search** `boolean`（可选）默认值为`false`
是否强制开启搜索。参数值：
- true：强制开启；
- false：不强制开启。

##### 22.6.5 search_strategy `string`（可选）默认值为`turbo`
搜索互联网信息的策略。
可选值：
- `turbo` （默认）: 兼顾响应速度与搜索效果，适用于大多数场景。
- `max`: 采用更全面的搜索策略，可调用多源搜索引擎，以获取更详尽的搜索结果，但响应时间可能更长。
- `agent`：可多次调用联网搜索工具与大模型，实现多轮信息检索与内容整合。
	该策略仅适用于 qwen3-max与 qwen3-max-2026-01-23 的思考模式（仅支持流式）、qwen3-max-2026-01-23的非思考模式、qwen3-max-2025-09-23。
	启用该策略时，仅支持**返回搜索来源**（`enable_source: true`），其他联网搜索功能不可用。
- `agent_max`：在`agent`策略基础上支持网页抓取，参见：[网页抓取](https://help.aliyun.com/zh/model-studio/web-extractor?spm=a2c4g.11186623.0.0.174d240a79HpEr)。
	**该策略仅适用于 qwen3-max与 qwen3-max-2026-01-23 的思考模式。**
	**启用该策略时，仅支持**返回搜索来源**（`enable_source: true`），其他联网搜索功能不可用。**

##### 22.6.6 enable_search_extension `boolean`（可选）默认值为`false`
是否开启特定领域增强。参数值：
- `true`
	开启。
- `false`（默认值）
	不开启。

##### 22.6.7 prepend_search_result** `*boolean*`（可选）默认值为`false`
在流式输出且`enable_source`为`true`时，可通过`prepend_search_result`配置**第一个返回的数据包**是否只包含搜索来源信息。可选值：
- `true`
	只包含搜索来源信息。
- `false`（默认值）
	包含搜索来源信息与大模型回复信息。
**暂不支持 DashScope Java SDK。**

#### 22.6 X-DashScope-DataInspection `string` （可选）
在千问 API 的内容安全能力基础上，是否进一步识别输入输出内容的违规信息。取值如下：
- `'{"input":"cip","output":"cip"}'`：进一步识别；
- 不设置该参数：不进一步识别。
通过 HTTP 调用时请放入请求头：`-H "X-DashScope-DataInspection: {\"input\": \"cip\", \"output\": \"cip\"}"`；
通过 Python SDK 调用时请通过`headers`配置：`headers={'X-DashScope-DataInspection': '{"input":"cip","output":"cip"}'}`。
详细使用方法请参见内容审核。
**不支持通过 Java SDK 设置。**
**不适用于Qwen-Audio 系列模型。**

## chat响应对象（流式与非流式输出格式一致）

### 1. status_code `string`
本次请求的状态码。200 表示请求成功，否则表示请求失败。
**Java SDK不会返回该参数。调用失败会抛出异常，异常信息为status_code和message的内容。**

### 2. request_id `string`
本次调用的唯一标识符。
**Java SDK返回参数为requestId。


### 3. code `string`
错误码，调用成功时为空值。
**只有Python SDK返回该参数。**

### 4. output `object`
调用结果信息。
**属性**
#### 4.1 text `string`
模型生成的回复。当设置输入参数**result_format**为**text**时将回复内容返回到该字段。

#### 4.2 finish_reason `string`
当设置输入参数**result_format**为**text**时该参数不为空。
有四种情况：
- 正在生成时为null；
- 因模型输出自然结束，或触发输入参数中的stop条件而结束时为stop；
- 因生成长度过长而结束为length；
- 因发生工具调用为tool_calls。

#### 4.3 choices `array`
模型的输出信息。当result_format为message时返回choices参数。
**属性**
##### 4.3.1 finish_reason `string`
有四种情况：
- 正在生成时为null；
- 因模型输出自然结束，或触发输入参数中的stop条件而结束时为stop；
- 因生成长度过长而结束为length；
- 因发生工具调用为tool_calls。

##### 4.3.2 message `object`
模型输出的消息对象。
**属性**
###### 4.3.2.1 role `string`
输出消息的角色，固定为assistant。

###### 4.3.2.2 content `string或array`
输出消息的内容。当使用qwen-vl或qwen-audio系列模型时为`array`，其余情况为`string`。
**如果发起Function Calling，则该值为空。**
**属性**
####### 4.3.2.2.1 text `string`
当使用qwen-vl或qwen-audio系列模型时，输出消息的内容。

####### 4.3.2.2.2 image_hw `array`
当Qwen-VL系列模型启用 vl_enable_image_hw_output 参数时，有两种情况：
图像输入：返回图像的高度和高度（数值单位：像素）
视频输入：返回空数组

###### 4.3.2.3 reasoning_content `string`
模型的深度思考内容。

###### 4.3.2.4 tool_calls `array`
若模型需要调用工具，则会生成tool_calls参数。
**属性**
####### 4.3.2.4.1 function `object`
调用工具的名称，以及输入参数。
**属性**
######## 4.3.2.4.1.1 name `string`
调用工具的名称

######## 4.3.2.4.1.2 arguments `string`
需要输入到工具中的参数，为JSON字符串。
	**由于大模型响应有一定随机性，输出的JSON字符串并不总满足于您的函数，建议您在将参数输入函数前进行参数的有效性校验。**

####### 4.3.2.4.2 index `integer`
当前**tool_calls**对象在tool_calls数组中的索引。

####### 4.3.2.4.3 id `string`
本次工具响应的ID。

####### 4.3.2.4.4 type `string`
工具类型，固定为`function`。

##### 4.3.3 logprobs `object`
当前 choices 对象的概率信息。
**属性**
###### 4.3.3.1 content** `array`
带有对数概率信息的 Token 数组。
**属性**
####### 4.3.3.1.1 token** `string`
当前 Token。

####### 4.3.3.1.2 bytes `array`
当前 Token 的 UTF‑8 原始字节列表，用于精确还原输出内容，在处理表情符号、中文字符时有帮助。

####### 4.3.3.1.3 logprob `float`
当前 Token 的对数概率。返回值为 null 表示概率值极低。

####### 4.3.3.1.4 top_logprobs `array`
当前 Token 位置最可能的若干个 Token 及其对数概率，元素个数与入参的`top_logprobs`保持一致。
**属性**
######## 4.3.3.1.4.1 token `string`
当前 Token。

######## 4.3.3.1.4.2 bytes `array`
当前 Token 的 UTF‑8 原始字节列表，用于精确还原输出内容，在处理表情符号、中文字符时有帮助。

######## 4.3.3.1.4.3 logprob `float`
当前 Token 的对数概率。返回值为 null 表示概率值极低。

#### 4.4 search_info `object`
联网搜索到的信息，在设置`search_options`参数后会返回该参数。
**属性**
##### 4.4.1 search_results `array`
联网搜索到的结果。
**属性**
###### 4.4.1.1 site_name `string`
搜索结果来源的网站名称。

###### 4.4.1.2 icon `string`
来源网站的图标URL，如果没有图标则为空字符串。

###### 4.4.1.3 index `integer`
搜索结果的序号，表示该搜索结果在`search_results`中的索引。

###### 4.4.1.4 title `string`
搜索结果的标题。

###### 4.4.1.5 url `string`
搜索结果的链接地址。

  

##### 4.4.2 extra_tool_info `array`
开启`enable_search_extension`参数后返回的领域增强信息。
**属性**
###### 4.4.2.1 result `string`
领域增强工具输出信息。

###### 4.4.2.2 resulttool `string`
领域增强使用的工具。

### 5. usage `map`
本次chat请求使用的Token信息。
**属性**
#### 5.1 input_tokens `integer`
用户输入内容转换成Token后的长度。

#### 5.2 output_tokens `integer`
模型输出内容转换成Token后的长度。

#### 5.3 input_tokens_details `integer`
使用Qwen-VL 模型或QVQ模型时，输入内容转换成Token后的长度详情。
**属性**
##### 5.3.1 text_tokens `integer`
使用Qwen-VL 模型或QVQ模型时，为输入的文本转换为Token后的长度。

##### 5.3.2 image_tokens `integer`
输入的图像转换为Token后的长度。

##### 5.3.3 video_tokens `integer`
输入的视频文件或图像列表转换为Token后的长度。

#### 5.4 total_tokens `integer`
当输入为纯文本时返回该字段，为**input_tokens**与**output_tokens**之和。

#### 5.5 image_tokens `integer`
输入内容包含`image`时返回该字段。为用户输入图片内容转换成Token后的长度。

#### 5.6 video_tokens `integer`
输入内容包含`video`时返回该字段。为用户输入视频内容转换成Token后的长度。

#### 5.7 audio_tokens `integer`
输入内容包含`audio`时返回该字段。为用户输入音频内容转换成Token后的长度。

#### 5.8 output_tokens_details `integer`
输出内容转换成 Token后的长度详情。
**属性**
##### 5.8.1 text_tokens `integer`
输出的文本转换为Token后的长度。

##### 5.8.2 reasoning_tokens `integer`
Qwen3 模型思考过程转换为Token后的长度。

  

#### 5.9 prompt_tokens_details `object`
输入 Token 的细粒度分类。
**属性**
##### 5.9.1 cached_tokens `integer`
命中 Cache 的 Token 数。Context Cache 详情请参见上下文缓存。

##### 5.9.2 cache_creation `object`
显式缓存创建信息。
**属性**
###### 5.9.2.1 ephemeral_5m_input_tokens `integer`
用于创建5分钟有效期显式缓存的 Token 长度。

##### 5.9.3 cache_creation_input_tokens `integer`
用于创建显式缓存的 Token 长度。

##### 5.9.\4 cache_type `string`
使用显式缓存时，参数值为`ephemeral`，否则该参数不存在。

## 错误码
如果模型调用失败并返回报错信息，请参见[错误信息](https://help.aliyun.com/zh/model-studio/error-code?spm=a2c4g.11186623.0.0.174d240a79HpEr)进行解决。

  