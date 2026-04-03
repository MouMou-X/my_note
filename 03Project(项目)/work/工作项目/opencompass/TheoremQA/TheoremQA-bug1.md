---
tags: [LLM/Eval]
type: note
status: 🌿
---

![[Pasted image 20251211145619.png]]

![[Pasted image 20251211153944.png]]

## 🎯 判决结论

  * **最终判定：** 🟢 **模型正确** (判卷程序 Bug)
  * **一句话归因：** 评测代码 (`utils.py`) 在对比列表类型的答案时，**硬编码只识别圆括号 `(...)` 包裹的元组格式**，无法识别方括号 `[...]` 包裹的列表格式，导致直接判错。

## 📝 题目概览

  * **中文题意：** 计算两个线积分 $\int_K xy dx$ 和 $\int_L xy dx$，其中 $K$ 是从 $(0,0)$ 到 $(1,1)$ 的直线，$L$ 是从 $(0,0)$ 到 $(1,1)$ 的抛物线 $y=x^2$。结果以列表形式返回。
  * **核心考点：** 曲线积分 (Line Integral)、参数方程。

## 🔍 深度比对表

| 来源 | 提取/计算数值 | 专家点评 |
| :--- | :--- | :--- |
| **专家推导 (你)** | **[1/3, 1/4]** (即 [0.3333..., 0.25]) | 积分计算无误：<br>1. $\int_0^1 x(x)dx = 1/3$<br>2. $\int_0^1 x(x^2)dx = 1/4$ |
| **Gold (标准)** | [0.333, 0.25] | 答案正确（精度稍低）。 |
| **Prediction (模型)** | **[0.3333, 0.25]** | 模型推导严谨，结果完全正确。 |

## 💡 根因详细分析 (Root Cause Analysis)

### 1\. 为什么模型被判错？

模型的预测结果提取为字符串 `"[0.3333, 0.25]"`（注意是**方括号**）。
然而，`TheoremQA` 的判题代码在处理“列表对比”时，存在一个极其低级的格式限制。

请看 `utils.py` 文件中的 `compare_answer_with_groundtruth` 函数（第 60 行左右）：

```python
        else:
            # 🔴 致命缺陷：只检查是否以 '(' 开头且以 ')' 结尾
            if answer.startswith('(') and answer.endswith(')'):
                try:
                    answer = list(eval(answer))
                    answer = [number_it(a) for a in answer]
                except Exception as e:
                    return False
                return compare_two_list(answer, groundtruth_num)
            else:
                return False  # ❌ 遇到方括号 [...] 直接返回 False
```

**逻辑漏洞：**

  * 代码假定所有的列表/向量答案都必须是 **Python 元组 (Tuple)** 的字符串形式（例如 `(0.333, 0.25)`）。
  * 当模型输出标准的 **Python 列表 (List)** 格式（例如 `[0.333, 0.25]`）时，`answer.startswith('(')` 为假，代码直接进入 `else` 分支返回 `False`。

### 2\. 修复方案

你需要修改 `TheoremQA.zip/utils.py` 中的判定逻辑，使其同时支持圆括号和方括号。

**建议修改代码：**

```python
        else:
            # ✅ 修复：同时支持列表 [...] 和 元组 (...) 格式
            if (answer.startswith('(') and answer.endswith(')')) or \
               (answer.startswith('[') and answer.endswith(']')):
                try:
                    # eval 同时支持解析 (1,2) 和 [1,2]
                    answer = list(eval(answer)) 
                    answer = [number_it(a) for a in answer]
                except Exception as e:
                    return False
                return compare_two_list(answer, groundtruth_num)
            else:
                return False
```

修改后，模型正确的答案 `[0.3333, 0.25]` 将被正确解析并与标准答案匹配成功。