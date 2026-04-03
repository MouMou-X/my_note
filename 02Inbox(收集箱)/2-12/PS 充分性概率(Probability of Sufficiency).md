---
tags:
  - 数学/因果推理
  - 反事实推理
type: reference
source: https://claude.ai/chat/ef69dd85-e429-432e-9ddf-1e1d0cec9853
日期: 2026-02-12
aliases:
  - Probability of Sufficiency
  - PS
  - 充分性概率
status: 🌱
---

# Probability of Sufficiency (PS)

## 定义

**PS** 衡量因果关系的充分性，回答"如果"(What-if)问题：

> 已知 $X=0$ 和 $Y=0$，如果 $X$ 发生，$Y$ 会发生吗？

$$PS = P(Y_{X=1} = 1 \mid X=0, Y=0)$$

**解读**：在观察到 $X=0$ 且 $Y=0$ 的条件下，反事实地将 $X$ 设为 1，则 $Y$ 变为 1 的概率。

---

## 一般情况：Tian-Pearl 界限

在无额外假设下，PS 通常不可点识别，仅能计算界限。

### 界限公式

**下界**： $$PS \geq \max\left\{0, \frac{P(Y=1|X=1) - P(Y=1|X=0)}{P(Y=0|X=0)}\right\}$$

**上界**： $$PS \leq \min\left\{1, \frac{P(Y=1|X=1)}{P(Y=0|X=0)}\right\}$$

---

## 特殊情形 1：单调性 + 无混杂

### 假设条件

1. **单调性**：$Y_{X=1}(u) \geq Y_{X=0}(u)$ 对所有个体 $u$ 成立
2. **无混杂**：${Y_{X=0}, Y_{X=1}} \perp X$

### 点识别公式

在此假设下，PS **可点识别**，且仅需观测数据：

$$PS = \frac{P(Y=1|X=1) - P(Y=1|X=0)}{P(Y=0|X=0)}$$

等价形式： $$PS = \frac{P(Y=1|X=1) - P(Y=1|X=0)}{1 - P(Y=1|X=0)}$$

**推导逻辑**：

- 无混杂 → $P(Y=1|X=x) = P(Y_{X=x}=1)$
- 单调性 → PS 下界成为精确值

---

## 特殊情形 2：单调性 + 有混杂

### 假设条件

1. **单调性**：$Y_{X=1}(u) \geq Y_{X=0}(u)$
2. **存在混杂**：${Y_{X=0}, Y_{X=1}} \not\perp X$

### 识别策略

**情况 A：有实验数据（RCT）**

点识别公式： $$PS = \frac{P(Y_1) - P(Y_0)}{1 - P(Y_0)}$$

其中 $P(Y_x)$ 来自随机对照试验。

**情况 B：仅有观测数据**

需要额外方法控制混杂：

1. **调整协变量** $Z$：假设条件独立 ${Y_{X=0}, Y_{X=1}} \perp X \mid Z$ $$PS = \frac{\sum_z [P(Y=1|X=1,Z=z) - P(Y=1|X=0,Z=z)]P(Z=z|X=0,Y=0)}{\sum_z [1 - P(Y=1|X=0,Z=z)]P(Z=z|X=0,Y=0)}$$
    
2. **工具变量** $IV$：满足相关性、排他性、单调性
    
3. **前门/后门准则**：根据因果图识别
    

---

## Python 实现

```python
def calculate_ps_bounds(p_y1_given_x1, p_y1_given_x0):
    """PS 界限（一般情况）
    
    Args:
        p_y1_given_x1: P(Y=1|X=1)
        p_y1_given_x0: P(Y=1|X=0)
    """
    p_y0_given_x0 = 1 - p_y1_given_x0
    
    lb = max(0, (p_y1_given_x1 - p_y1_given_x0) / p_y0_given_x0)
    ub = min(1, p_y1_given_x1 / p_y0_given_x0)
    
    return lb, ub

def calculate_ps_monotone_unconfounded(p_y1_given_x1, p_y1_given_x0):
    """PS 点识别（单调性 + 无混杂）
    
    Args:
        p_y1_given_x1: P(Y=1|X=1) [观测数据]
        p_y1_given_x0: P(Y=1|X=0) [观测数据]
    """
    return (p_y1_given_x1 - p_y1_given_x0) / (1 - p_y1_given_x0)

def calculate_ps_monotone_confounded_rct(p_y1_do_x1, p_y1_do_x0):
    """PS 点识别（单调性 + 有混杂 + RCT数据）
    
    Args:
        p_y1_do_x1: P(Y_1) [实验数据]
        p_y1_do_x0: P(Y_0) [实验数据]
    """
    return (p_y1_do_x1 - p_y1_do_x0) / (1 - p_y1_do_x0)

def calculate_ps_adjusted(p_y1_x1_z, p_y1_x0_z, p_z_given_x0y0):
    """PS 调整混杂（单调性 + 协变量调整）
    
    Args:
        p_y1_x1_z: dict {z: P(Y=1|X=1,Z=z)}
        p_y1_x0_z: dict {z: P(Y=1|X=0,Z=z)}
        p_z_given_x0y0: dict {z: P(Z=z|X=0,Y=0)}
    """
    numerator = sum((p_y1_x1_z[z] - p_y1_x0_z[z]) * p_z_given_x0y0[z] 
                    for z in p_y1_x1_z)
    denominator = sum((1 - p_y1_x0_z[z]) * p_z_given_x0y0[z] 
                      for z in p_y1_x0_z)
    return numerator / denominator

# 示例
print("=== 一般情况 ===")
lb, ub = calculate_ps_bounds(0.75, 0.50)
print(f"PS ∈ [{lb:.3f}, {ub:.3f}]")

print("\n=== 单调性 + 无混杂 ===")
ps = calculate_ps_monotone_unconfounded(0.75, 0.50)
print(f"PS = {ps:.3f}")

print("\n=== 单调性 + 有混杂 (RCT) ===")
ps_rct = calculate_ps_monotone_confounded_rct(0.70, 0.45)
print(f"PS = {ps_rct:.3f}")
```

---

## 应用场景

- **政策评估**：实施某政策是否足以产生预期效果
- **营销策划**：推送广告是否足以促成购买
- **医学研究**：给予治疗是否足以治愈疾病

---

## PN vs PS 对比

|维度|PN (必要性)|PS (充分性)|
|:--|:--|:--|
|**问题**|去掉原因，结果消失？|加入原因，结果出现？|
|**条件**|$X=1, Y=1$|$X=0, Y=0$|
|**反事实**|$Y_{X=0}=0$|$Y_{X=1}=1$|
|**法律应用**|归责（tort law）|预防（preventive）|
|**单调性下**|$\frac{ATE}{P(Y\|X=1)}$|$\frac{ATE}{1-P(Y\|X=0)}$|

其中 $ATE = P(Y=1|X=1) - P(Y=1|X=0)$ 为平均处理效应。

---

## 相关笔记

- [[PN 必要性概率 (Probability of Necessity)]]
- [[PNS|必要充分性概率]]
- [[Counterfactuals|反事实推理]]
- [[Monotonicity|单调性假设]]