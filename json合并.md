



```python
import json

class DatasetMerger:
    """
    用于合并评测 prediction 和 results 的工具
    """
    def __init__(self, prediction_json_str, results_json_str):
        """
        初始化时传入两个 json 字符串。
        """
        # prediction_json: 包含 "0": {...} 的详细数据 (你希望这个排前面)
        self.prediction_json = json.loads(prediction_json_str)
        # results_json: 包含 "details": [...] 的摘要数据 (你希望这个排后面)
        self.results_json = json.loads(results_json_str)
        
        # 最终结果初始化为字典
        self.merged_result = {}

    def merge(self):
        """
        执行合并逻辑。
        返回：一个以索引为 Key 的字典，且 prediction 字段在前。
        """
        # 1. 获取 results 里的列表
        raw_list = self.results_json.get("details", [])
        
        # 2. 遍历列表
        for index, result_item in enumerate(raw_list):
            lookup_key = str(index)
            
            # --- 核心修改开始：控制字段顺序 ---
            
            # A. 先尝试获取 prediction 数据 (如果没找到就给个空字典)
            # 使用 .get() 防止报错，同时 .copy() 确保不修改原始数据
            prediction_item = self.prediction_json.get(lookup_key, {}).copy()
            
            # B. 现在的 prediction_item 已经是基础了
            # 我们把 result_item (摘要数据) update 进去
            # 这样，prediction 的字段会保留在前面，result 的字段会追加在后面
            prediction_item.update(result_item)
            
            # C. 将合并好的字典存入结果
            self.merged_result[lookup_key] = prediction_item
            
            # --- 核心修改结束 ---
        
        return self.merged_result

    def save_to_file(self, file_name):
        """
        辅助功能：把结果保存成新的 JSON 文件
        """
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.merged_result, f, ensure_ascii=False, indent=4)
        print(f"✅ 成功保存 {len(self.merged_result)} 条数据到 {file_name}")

if __name__ == "__main__":
    # 模拟数据
    # 1. 摘要数据 (Results) - 包含 pred, is_correct
    json_str_results = """
    {
        "score": 24.875,
        "details": [
            {"example_abbr": "TheoremQA_0", "pred": ["False"], "is_correct": [false]},
            {"example_abbr": "TheoremQA_1", "pred": ["False"], "is_correct": [false]}
        ]
    }
    """
    
    # 2. 详情数据 (Prediction) - 包含 origin_prompt, gold
    json_str_prediction = """
    {
        "0": {"origin_prompt": "问题0...", "gold": "答案0"},
        "1": {"origin_prompt": "问题1...", "gold": "答案1"}
    }
    """

    # 实例化
    merger = DatasetMerger(json_str_prediction, json_str_results)

    # 合并
    final_data = merger.merge()

    # 打印结果验证顺序
    print("合并后的第一条数据：")
    print(json.dumps(final_data, indent=4, ensure_ascii=False))
```
