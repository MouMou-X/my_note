---
tags:
  - 数学/因果推理
  - 反事实推理
type: reference
source: https://claude.ai/chat/ef69dd85-e429-432e-9ddf-1e1d0cec9853
日期: 2026-02-12
aliases:
  - Probability of Necessity and Sufficiency
  - 必要充分性概率
  - PNS
status: 🌱
---

# Probability of Necessity and Sufficiency (PNS)

## 定义

**PNS** 衡量因果关系的必要且充分性，回答"唯一决定"问题：

> $X$ 是 $Y$ 的唯一决定因素吗？

$$PNS = P(Y_{X=1} = 1, Y_{X=0} = 0)$$

**解读**：个体同时满足两个反事实条件的概率：

- 如果接受处理 $(X=1)$，结果发生 $(Y_{X=1}=1)$
- 如果不接受处理 $(X=0)$，结果不发生 $(Y_{X=0}=0)$

**与 PN、PS 的关系**： $$PNS \leq \min(PN, PS)$$

PNS 要求同时满足必要性和充分性，因此最为严格。

---

## 一般情况：Tian-Pearl 界限

在无额外假设下，PNS 不可点识别，仅能计算界限。

### 界限公式

**下界**： $$PNS \geq \max\left\{0, P(Y=1|X=1) - P(Y=1|X=0)\right\}$$

这是平均处理效应 (ATE) 的非负部分。

**上界**： $$PNS \leq \min{P(Y=1|X=1), P(Y=0|X=0)}$$

**更紧的界限**（结合 PN 和 PS）： $$PNS \geq \max{0, PN_{LB} + PS_{LB} - 1}$$ $$PNS \leq \min{PN_{UB}, PS_{UB}}$$

---

## 特殊情形 1：单调性 + 无混杂

### 假设条件

1. **单调性**：$Y_{X=1}(u) \geq Y_{X=0}(u)$ 对所有个体 $u$ 成立
2. **无混杂**：${Y_{X=0}, Y_{X=1}} \perp X$

### 点识别公式

在此假设下，PNS **可点识别**，且仅需观测数据：

$$PNS = P(Y=1|X=1) - P(Y=1|X=0) = ATE$$

**推导**：

- 单调性保证没有"损害者"（defiers）：$Y_{X=1}(u) < Y_{X=0}(u)$ 的个体不存在
- 无混杂保证 $P(Y=1|X=x) = P(Y_{X=x}=1)$
- 因此 $PNS$ 等于平均处理效应

**四类个体划分**（Principal Stratification）：

|类型|$Y_{X=0}$|$Y_{X=1}$|比例|
|:--|:-:|:-:|:--|
|Always-taker|1|1|$P(Y=1\|X=0)$|
|Complier (受益者)|0|1|$PNS = ATE$|
|Never-taker|0|0|$1-P(Y=1\|X=1)$|
|Defier (损害者)|1|0|0 (单调性排除)|

---

## 特殊情形 2：单调性 + 有混杂

### 假设条件

1. **单调性**：$Y_{X=1}(u) \geq Y_{X=0}(u)$
2. **存在混杂**：${Y_{X=0}, Y_{X=1}} \not\perp X$

### 识别策略

**情况 A：有实验数据（RCT）**

点识别公式： $$PNS = P(Y_1) - P(Y_0)$$

其中 $P(Y_x)$ 来自随机对照试验。这是实验版本的 ATE。

**情况 B：仅有观测数据**

需要额外方法控制混杂：

1. **调整协变量** $Z$：假设条件独立 ${Y_{X=0}, Y_{X=1}} \perp X \mid Z$ $$PNS = \sum_z [P(Y=1|X=1,Z=z) - P(Y=1|X=0,Z=z)]P(Z=z)$$
    
    这是条件平均处理效应的边际化。
    
2. **工具变量** (IV)：在 LATE 框架下 $$PNS_{compliers} = \frac{P(Y=1|Z=1) - P(Y=1|Z=0)}{P(X=1|Z=1) - P(X=1|Z=0)}$$
    
    注意：这仅识别 compliers 中的 PNS，不是总体 PNS。
    
3. **倾向得分匹配/加权**： $$PNS = E_{e(Z)}\left[\frac{XY}{e(Z)} - \frac{(1-X)Y}{1-e(Z)}\right]$$
    
    其中 $e(Z) = P(X=1|Z)$ 是倾向得分。
    

---

## Python 实现

```python
def calculate_pns_bounds(p_y1_given_x1, p_y1_given_x0):
    """PNS 界限（一般情况）
    
    Args:
        p_y1_given_x1: P(Y=1|X=1)
        p_y1_given_x0: P(Y=1|X=0)
    """
    # 基本界限
    lb_basic = max(0, p_y1_given_x1 - p_y1_given_x0)
    ub_basic = min(p_y1_given_x1, 1 - p_y1_given_x0)
    
    return lb_basic, ub_basic

def calculate_pns_bounds_tight(pn_lb, pn_ub, ps_lb, ps_ub):
    """PNS 更紧的界限（利用 PN 和 PS）
    
    Args:
        pn_lb, pn_ub: PN 的下界和上界
        ps_lb, ps_ub: PS 的下界和上界
    """
    lb = max(0, pn_lb + ps_lb - 1)
    ub = min(pn_ub, ps_ub)
    
    return lb, ub

def calculate_pns_monotone_unconfounded(p_y1_given_x1, p_y1_given_x0):
    """PNS 点识别（单调性 + 无混杂）
    
    Args:
        p_y1_given_x1: P(Y=1|X=1) [观测数据]
        p_y1_given_x0: P(Y=1|X=0) [观测数据]
    """
    return p_y1_given_x1 - p_y1_given_x0  # ATE

def calculate_pns_monotone_confounded_rct(p_y1_do_x1, p_y1_do_x0):
    """PNS 点识别（单调性 + 有混杂 + RCT数据）
    
    Args:
        p_y1_do_x1: P(Y_1) [实验数据]
        p_y1_do_x0: P(Y_0) [实验数据]
    """
    return p_y1_do_x1 - p_y1_do_x0  # Experimental ATE

def calculate_pns_adjusted(p_y1_x1_z, p_y1_x0_z, p_z):
    """PNS 调整混杂（单调性 + 协变量调整）
    
    Args:
        p_y1_x1_z: dict {z: P(Y=1|X=1,Z=z)}
        p_y1_x0_z: dict {z: P(Y=1|X=0,Z=z)}
        p_z: dict {z: P(Z=z)}
    """
    pns = sum((p_y1_x1_z[z] - p_y1_x0_z[z]) * p_z[z] 
              for z in p_y1_x1_z)
    return pns

def calculate_pns_iv(p_y1_z1, p_y1_z0, p_x1_z1, p_x1_z0):
    """PNS for compliers（工具变量识别）
    
    Args:
        p_y1_z1: P(Y=1|Z=1)
        p_y1_z0: P(Y=1|Z=0)
        p_x1_z1: P(X=1|Z=1)
        p_x1_z0: P(X=1|Z=0)
    """
    # LATE = Local Average Treatment Effect
    late = (p_y1_z1 - p_y1_z0) / (p_x1_z1 - p_x1_z0)
    return late

# 示例
print("=== 一般情况：基本界限 ===")
lb, ub = calculate_pns_bounds(0.75, 0.50)
print(f"PNS ∈ [{lb:.3f}, {ub:.3f}]")

print("\n=== 单调性 + 无混杂 ===")
pns = calculate_pns_monotone_unconfounded(0.75, 0.50)
print(f"PNS = ATE = {pns:.3f}")

print("\n=== 单调性 + 有混杂 (RCT) ===")
pns_rct = calculate_pns_monotone_confounded_rct(0.70, 0.45)
print(f"PNS = {pns_rct:.3f}")

print("\n=== 协变量调整 ===")
# 假设 Z 有两个水平
p_y1_x1_z = {0: 0.60, 1: 0.80}
p_y1_x0_z = {0: 0.40, 1: 0.55}
p_z = {0: 0.6, 1: 0.4}
pns_adj = calculate_pns_adjusted(p_y1_x1_z, p_y1_x0_z, p_z)
print(f"PNS (adjusted) = {pns_adj:.3f}")
```

---

## 应用场景

- **机制研究**：识别"受益者"（compliers）——那些只有在接受处理时才有正向结果的个体
- **精准医疗**：确定对特定治疗有完全响应的患者亚群
- **异质性处理效应**：区分 always-takers、compliers、never-takers
- **政策靶向**：识别政策干预的真正受益群体

---

## PN, PS, PNS 关系总结

| 指标      | 条件         | 反事实            | 单调性+无混杂                   | 含义    |
| :------ | :--------- | :------------- | :------------------------ | :---- |
| **PN**  | $X=1, Y=1$ | $Y_0=0$        | $\frac{ATE}{P(Y\|X=1)}$   | 必要性   |
| **PS**  | $X=0, Y=0$ | $Y_1=1$        | $\frac{ATE}{P(Y=0\|X=0)}$ | 充分性   |
| **PNS** | —          | $Y_1=1, Y_0=0$ | $ATE$                     | 必要且充分 |

**关键洞察**：

- $PNS = ATE$ （单调性+无混杂下）
- $PN \times P(X=1, Y=1) = PNS$
- $PS \times P(X=0, Y=0) = PNS$

---

## 相关笔记

- [[PN 必要性概率 (Probability of Necessity)]]
- [[PS 充分性概率(Probability of Sufficiency)]]
- [[平均处理效应|平均处理效应ATE]]
- [[LATE|局部平均处理效应]]
- [[Principal-Stratification|主分层]]
- [[Monotonicity|单调性假设]]