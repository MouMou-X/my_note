---
tags:
  - 数学/因果推理
  - 反事实推理
type: reference
source: https://gemini.google.com/app/d51fc847ca7d5b4a
date: 2026-02-12
aliases:
  - Probability of Necessity
  - PN
  - Tian-Pearl Bounds
status: 🌱
---

# Probability of Necessity (PN)

## 定义

**PN** 衡量因果归因的必要性，回答"若非"(But-for)问题：

> 已知 $X=x$ 和 $Y=y$ 发生，如果 $X$ 未发生，$Y$ 还会发生吗？

$$PN = P(Y_{X=0} = 0 \mid X=1, Y=1)$$

**解读**：在观察到 $X=1$ 且 $Y=1$ 的条件下，反事实地将 $X$ 设为 0，则 $Y$ 变为 0 的概率。

---

## 一般情况：Tian-Pearl 界限

在无额外假设下，PN 通常不可点识别，仅能计算界限。

### 界限公式

**下界**： 
$$ PN \geq \max \left\{  0, \frac{P(Y=1|X=1) - P(Y=1|X=0)}{P(Y=1|X=1)} \right\} $$


**上界**： 
$$PN \leq \min\left\{1, \frac{P(Y=0|X=0)}{P(Y=1|X=1)}\right\}$$

等价形式： 
$$PN \leq \min\left\{1, \frac{1 - P(Y=1|X=0)}{P(Y=1|X=1)}\right\}$$

---

## 特殊情形 1：单调性 + 无混杂

### 假设条件

1. **单调性**：$Y_{X=1}(u) \geq Y_{X=0}(u)$ 对所有个体 $u$ 成立
2. **无混杂**：${Y_{X=0}, Y_{X=1}} \perp X$

### 点识别公式

在此假设下，PN **可点识别**，且仅需观测数据：

$$PN = \frac{P(Y=1|X=1) - P(Y=1|X=0)}{P(Y=1|X=1)}$$

**推导逻辑**：

- 无混杂 → $P(Y=1|X=x) = P(Y_{X=x}=1)$
- 单调性 → PN 下界成为精确值

---

## 特殊情形 2：单调性 + 有混杂

### 假设条件

1. **单调性**：$Y_{X=1}(u) \geq Y_{X=0}(u)$
2. **存在混杂**：${Y_{X=0}, Y_{X=1}} \not\perp X$

### 识别策略

**情况 A：有实验数据（RCT）**

点识别公式： $$PN = \frac{P(Y_1) - P(Y_0)}{P(Y_1)}$$

其中 $P(Y_x)$ 来自随机对照试验。

**情况 B：仅有观测数据**

需要额外方法控制混杂：

1. **调整协变量** $Z$：假设条件独立 ${Y_{X=0}, Y_{X=1}} \perp X \mid Z$ $$PN = \frac{\sum_z [P(Y=1|X=1,Z=z) - P(Y=1|X=0,Z=z)]P(Z=z|X=1,Y=1)}{\sum_z P(Y=1|X=1,Z=z)P(Z=z|X=1,Y=1)}$$
    
2. **工具变量** $IV$：满足相关性、排他性、单调性
    
3. **前门/后门准则**：根据因果图识别
    

---

## Python 实现

```python
def calculate_pn_bounds(p_y1_given_x1, p_y1_given_x0):
    """PN 界限（一般情况）
    
    Args:
        p_y1_given_x1: P(Y=1|X=1)
        p_y1_given_x0: P(Y=1|X=0)
    """
    lb = max(0, (p_y1_given_x1 - p_y1_given_x0) / p_y1_given_x1)
    ub = min(1, (1 - p_y1_given_x0) / p_y1_given_x1)
    return lb, ub

def calculate_pn_monotone_unconfounded(p_y1_given_x1, p_y1_given_x0):
    """PN 点识别（单调性 + 无混杂）
    
    Args:
        p_y1_given_x1: P(Y=1|X=1) [观测数据]
        p_y1_given_x0: P(Y=1|X=0) [观测数据]
    """
    return (p_y1_given_x1 - p_y1_given_x0) / p_y1_given_x1

def calculate_pn_monotone_confounded_rct(p_y1_do_x1, p_y1_do_x0):
    """PN 点识别（单调性 + 有混杂 + RCT数据）
    
    Args:
        p_y1_do_x1: P(Y_1) [实验数据]
        p_y1_do_x0: P(Y_0) [实验数据]
    """
    return (p_y1_do_x1 - p_y1_do_x0) / p_y1_do_x1

def calculate_pn_adjusted(p_y1_x1_z, p_y1_x0_z, p_z_given_x1y1):
    """PN 调整混杂（单调性 + 协变量调整）
    
    Args:
        p_y1_x1_z: dict {z: P(Y=1|X=1,Z=z)}
        p_y1_x0_z: dict {z: P(Y=1|X=0,Z=z)}
        p_z_given_x1y1: dict {z: P(Z=z|X=1,Y=1)}
    """
    numerator = sum((p_y1_x1_z[z] - p_y1_x0_z[z]) * p_z_given_x1y1[z] 
                    for z in p_y1_x1_z)
    denominator = sum(p_y1_x1_z[z] * p_z_given_x1y1[z] 
                      for z in p_y1_x1_z)
    return numerator / denominator

# 示例
print("=== 一般情况 ===")
lb, ub = calculate_pn_bounds(0.75, 0.50)
print(f"PN ∈ [{lb:.3f}, {ub:.3f}]")

print("\n=== 单调性 + 无混杂 ===")
pn = calculate_pn_monotone_unconfounded(0.75, 0.50)
print(f"PN = {pn:.3f}")

print("\n=== 单调性 + 有混杂 (RCT) ===")
pn_rct = calculate_pn_monotone_confounded_rct(0.70, 0.45)
print(f"PN = {pn_rct:.3f}")
```

---

## 应用场景

- **法律归责**：药物/治疗是否是康复的必要原因（>50% 标准）
- **医疗诊断**：症状消除是否必然依赖于治疗
- **故障分析**：某组件失效是否是系统崩溃的必要条件

---

## 相关链接

- [[Structural Causal Models|SCM (结构因果模型)]]
- [[Do-Calculus|Do-Calculus (Do 算子)]]
- [[Counterfactuals|Counterfactuals (反事实)]]
- [[Identifiability (可识别性)]]
- [[PS 充分性概率(Probability of Sufficiency)]]
- [[PNS 必要充分性概率 (Probability of Necessity and Sufficiency)]]
- [[Counterfactuals|反事实推理]]
- [[Monotonicity单调性假设]]
