import json
import re
from actions_example import FUNCTION_MAP, FUNCTION_DESCRIPTIONS
from llm_client import LLMClient

# ========== 最小示例函数 ==========
def execute_action(action_name:str, **kwargs):
    """根据名称执行对应的函数"""
    if action_name not in FUNCTION_MAP:
        return f"错误：未知操作'{action_name}'"

    func = FUNCTION_MAP[action_name]
    print(kwargs)
    return func(**kwargs)



def fake_llm_response(user_input:str,functions:list) -> str:
    """
    模拟LLM响应
    :param user_input: 用户输入
    :param functions: 可用函数列表
    :return: 模拟的LLM响应
    """
    if "你好" in user_input:
        return json.dumps({"name": None, "arguments": {}, "direct_response": "你好！有什么可以帮你的？"})
    if "天气" in user_input:
        #提取城市名（简单模拟）
        city = "北京"
        for c in ["北京", "上海", "广州", "深圳"]:
            if c in user_input:
                city = c
                break
        return json.dumps({"name": "get_weather", "arguments": {"city": city}})
    elif "加" in user_input or "+" in user_input or "计算" in user_input:
        # 简单提取数字
        numbers = re.findall(r'\d+', user_input)
        if len(numbers) >= 2:
            return json.dumps({"name": "add_number", "arguments": {"a": int(numbers[0]), "b": int(numbers[1])}})
    
    return json.dumps({"name": None, "arguments": {}})





# ========== 核心：执行函数调用 ==========
def execute_function_call(function_call: dict) -> str:
    """根据函数调用对象执行对应的函数"""
    # 如果有直接响应，不需要调用函数
    if "direct_response" in function_call:
        return function_call["direct_response"]

    func_name = function_call.get("name")
    arguments = function_call.get("arguments", {})

    if not func_name:
        return "我不知道该如何处理这个请求。"
    
    if func_name not in FUNCTION_MAP:
        return f"未知函数: {func_name}"
    
    # 🔥 核心：通过 FUNCTION_MAP 动态调用函数
    func = FUNCTION_MAP[func_name]
    result = func(**arguments)
    return result


# ========== 主循环 ==========
def main():
    print("=" * 50)
    print("🤖 AI 助手（输入 'quit' 退出）")
    print("支持的功能：查询天气、数字加法")
    print("=" * 50)   

    client = LLMClient()

    while True:
        user_input = input("\n你: ").strip()
        if user_input.lower() == 'quit':
            print("再见！")
            break
        
        # Step 1: LLM 决定调用哪个函数
        # llm_response = fake_llm_response(user_input, FUNCTION_DESCRIPTIONS)
        # function_call = json.loads(llm_response)

        function_call = client.get_function_call(user_input, FUNCTION_DESCRIPTIONS)
        
        print(f"[调试] LLM 决策: {function_call}")
        
        # Step 2: 执行函数调用
        result = execute_function_call(function_call)
        
        print(f"助手: {result}")

if __name__ == "__main__":
    main()
    # 模拟动态调用
    """
    print(execute_action("get_weather", city="上海"))
    print(execute_action("add_number", a=10, b=20))
    print(execute_action("not_exist"))
    """