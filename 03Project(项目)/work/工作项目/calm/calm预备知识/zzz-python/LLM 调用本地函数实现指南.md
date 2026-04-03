---
tags: [编程/Python]
type: note
status: 🌿
---

# LLM 调用本地函数实现指南

## 📌 概述

本文记录如何通过 **FUNCTION_MAP** 模式实现 LLM 动态调用本地函数，这是构建 AI Agent 工具调用能力的基础。

> [!tip] 核心思想
> 用字典将「函数名字符串」映射到「实际函数对象」，让 LLM 通过返回函数名来间接调用函数。

---

## 🏗️ 项目结构

```
my_tools_enhancer/
├── actions_example/       # 工具函数层
│   ├── __init__.py        # FUNCTION_MAP + 函数描述
│   ├── math.py            # 数学函数
│   └── weather.py         # 天气函数
├── llm_client.py          # LLM 交互层
└── main.py                # 主程序入口
```

> [!note] 设计原则
> - `actions_example/` → 做具体事情（工具函数）
> - `llm_client.py` → 决定调用什么（LLM 交互）
> - `main.py` → 串联一切（流程控制）

---

## 🔧 实现步骤

### Step 1: 定义 FUNCTION_MAP

```python
# actions_example/__init__.py
from .weather import get_weather
from .math import add_number

FUNCTION_MAP = {
    "get_weather": get_weather,
    "add_number": add_number
}
```

**作用**：字符串 → 函数对象的映射桥梁

---

### Step 2: 定义函数描述（供 LLM 理解）

```python
FUNCTION_DESCRIPTIONS = [
    {
        "name": "get_weather",
        "description": "查询指定城市的天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "城市名称"}
            },
            "required": ["city"]
        }
    },
    {
        "name": "add_number",
        "description": "计算两个数字的和",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "integer", "description": "第一个数字"},
                "b": {"type": "integer", "description": "第二个数字"}
            },
            "required": ["a", "b"]
        }
    }
]
```

---

### Step 3: 实现 LLM 客户端

```python
# llm_client.py
import os, json, time
from dashscope import Generation

class LLMClient:
    def __init__(self, model="qwen-plus"):
        self.model = model
        self.api_key = os.getenv("DASHSCOPE_API_KEY")
        self.last_call_time = 0
        self.min_interval = 1.0

    def _wait_if_needed(self):
        """确保请求间隔不会太短"""
        elapsed = time.time() - self.last_call_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)

    def get_function_call(self, user_input: str, functions: list) -> dict:
        prompt = f"""你是一个函数调用助手。根据用户输入，决定是否需要调用函数。
可用函数：
{json.dumps(functions, ensure_ascii=False, indent=2)}

用户输入：{user_input}

规则：
1. 如果需要调用函数，返回：{{"name": "函数名", "arguments": {{参数字典}}}}
2. 如果不需要调用函数，返回：{{"name": null, "direct_response": "你的回复"}}

请严格按 JSON 格式返回。"""

        try:
            self._wait_if_needed()
            response = Generation.call(
                model=self.model,
                api_key=self.api_key,
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                result_format="message"
            )
            self.last_call_time = time.time()
            
            if response.status_code == 200:
                return json.loads(response.output.choices[0].message.content)
            else:
                return {"name": None, "direct_response": f"API 调用失败: {response.message}"}
        except Exception as e:
            return {"name": None, "direct_response": f"发生错误: {str(e)}"}
```

---

### Step 4: 执行函数调用

```python
# main.py
def execute_function_call(function_call: dict) -> str:
    # 直接回复（不需要调用函数）
    if "direct_response" in function_call:
        return function_call["direct_response"]
    
    func_name = function_call.get("name")
    arguments = function_call.get("arguments", {})
    
    if not func_name:
        return "我不知道该如何处理这个请求。"
    
    if func_name not in FUNCTION_MAP:
        return f"未知函数: {func_name}"
    
    # 🔥 核心：通过 FUNCTION_MAP 动态调用
    func = FUNCTION_MAP[func_name]
    return func(**arguments)
```

---

### Step 5: 主循环

```python
def main():
    client = LLMClient()
    
    while True:
        user_input = input("你: ").strip()
        if user_input.lower() == 'quit':
            break
        
        # LLM 决策
        function_call = client.get_function_call(user_input, FUNCTION_DESCRIPTIONS)
        
        # 执行函数
        result = execute_function_call(function_call)
        
        print(f"助手: {result}")
```

---

## 📊 数据流图

```
用户输入 "北京天气怎么样"
       ↓
LLMClient + FUNCTION_DESCRIPTIONS
       ↓
LLM 返回 {"name": "get_weather", "arguments": {"city": "北京"}}
       ↓
FUNCTION_MAP["get_weather"]
       ↓
get_weather(city="北京")
       ↓
返回 "北京的天气是晴天，温度为25摄氏度。"
```

---

## ⚠️ 踩坑记录

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `ModuleNotFoundError` | 运行目录不对 | cd 到脚本所在目录运行 |
| `JSONDecodeError` | LLM 返回非 JSON | 统一返回 JSON 格式 |
| API 429 频率限制 | 重试机制导致请求翻倍 | 改为单次请求 + 间隔控制 |

> [!warning] 重试陷阱
> 带重试的代码在失败时会多次请求 API，一次失败可能消耗 3 次配额，快速耗尽限额。

---

## 🔗 相关概念

- [[FUNCTION_MAP 模式]]
- [[Prompt 工程]]
- [[DashScope API 调用]]
- [[AI Agent 架构]]

---

## ✅ 核心收获

1. **FUNCTION_MAP** = 动态函数调用的桥梁
2. **Prompt 工程** = 让 LLM 输出结构化 JSON
3. **模块化设计** = 职责分离，易于扩展
4. **API 调用** = 注意频率控制，避免重试陷阱

---

## 📚 扩展方向

- [ ] 添加更多工具函数（翻译、搜索、计算器）
- [ ] 实现多轮对话（函数结果反馈给 LLM 生成自然语言）
- [ ] 添加参数验证和错误处理
- [ ] 支持异步调用
