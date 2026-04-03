import dashscope
from dashscope import Generation
import os
import json
import time


class LLMClient:
    def __init__(self, model="qwen-flash"):
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
        """让 LLM 根据用户输入决定调用哪个函数"""
        prompt = f"""你是一个函数调用助手。根据用户输入，决定是否需要调用函数。
可用函数：
{json.dumps(functions, ensure_ascii=False, indent=2)}

用户输入：{user_input}

规则：
1. 如果需要调用函数，返回：{{"name": "函数名", "arguments": {{参数字典}}}}
2. 如果不需要调用函数（如打招呼），返回：{{"name": null, "direct_response": "你的回复"}}

请严格按 JSON 格式返回，不要包含其他内容。"""

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
                content = response.output.choices[0].message.content
                return json.loads(content)
            else:
                return {"name": None, "direct_response": f"API 调用失败: {response.message}"}
                
        except Exception as e:
            return {"name": None, "direct_response": f"发生错误: {str(e)}"}
