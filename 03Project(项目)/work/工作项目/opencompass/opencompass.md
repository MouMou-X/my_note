- 模型和数据集调用
模型和数据集以配置文件形式预先存储在`configs/models`和 中`configs/datasets`。用户可以使用 来查看或筛选当前可用的模型和数据集配置`tools/list_configs.py`
```
python tools/list_configs.py
```
```
python tools/list_configs.py qwen ifeval
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
