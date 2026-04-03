---
date: 2026-02-11
tags:
  - LLM/Architecture
  - LLM/Training
  - Math/Numerical-Analysis
  - Causal-Inference
  - Obsidian/Notes
aliases:
  - System Message 失效的数值分析
  - LLM 训练中的浮点数精度陷阱
---

# LLM 深度解析：为什么 System Message 往往不如 User Prompt 有效？

> [!abstract] 核心结论
> **System Message 的失效不仅仅是语义理解问题，本质上是训练数据分布导致的数值计算问题。** > 由于 SFT 阶段 System Message 缺乏变化（低方差），导致模型对该位置的 Attention 权重更新不足。在 FP16 精度下，System 部分产生的微弱信号容易被数值噪声淹没，无法形成有效的特征表达。

## 1. 现象描述

在与业界专家的交流中，提到了一个反直觉的底层机制：
- **表象**：在模型架构层面，System 和 User 最终都被编码为 FP16 向量，理论上地位平等。
- **实际**：System Message 往往被模型“无视”，或者在推理时表现出高随机性。

## 2. 根本原因：数据分布与权重更新

### 2.1 训练数据的低方差 (Low Variance)
在 SFT（监督微调）数据集中，数据的典型结构是 `(System, User, Assistant)`。
- **User Prompt**：千变万化，涵盖各种任务。
- **System Prompt**：极度同质化（例如 90% 都是 *"You are a helpful assistant"*）。

由于 System 部分长期保持不变（Constant），在反向传播（Backpropagation）时，模型发现该位置的 token 变化对 Loss 的下降贡献极小。
$$\frac{\partial Loss}{\partial W_{system}} \approx 0$$
导致模型学会了**“忽略”** System 区域的信息。

### 2.2 浮点数精度的陷阱 (FP16 Precision Trap)

专家提到的核心观点是：“**在浮点数的尾部做区分，会引入一些随机性。**”

- **信号淹没**：当我们在推理时输入一个新的 System 指令，由于权重未充分更新，它在隐藏层产生的激活值变化量（$\Delta Activation$）非常微小。
- **尾数丢失**：FP16（半精度浮点数）只有 10 位尾数（Mantissa）。如果 User Prompt 产生的信号强度是 $10^2$ 级别，而 System 产生的 $\Delta$ 是 $10^{-4}$ 级别，在进行矩阵加法或 Softmax 归一化时，System 的信号可能会因为精度限制被**截断**或**舍入**。

> [!example] 形象比喻：迪厅里的耳语
> - **User Message**：迪厅里震耳欲聋的音乐（强信号，模型训练充分，对其敏感）。
> - **System Message**：你在角落里的耳语（弱信号，模型未充分学习）。
> - **FP16 噪声**：环境背景噪音。
> 
> 你的耳语（System）完全被背景噪音（FP16 误差）和音乐（User）淹没了。

## 3. [[Causal Inference|因果推断]]视角下的解读

结合因果推断的框架，我们可以更形式化地描述这个问题：

1.  **Treatment ($T$)**: System Message 的内容。
2.  **Outcome ($Y$)**: 模型的输出分布。
3.  **缺乏 Positivity (Positivity Violation)**: 
    在训练分布 $P_{train}$ 中，给定 User Input $X$，System Message $T$ 几乎取定值。这意味着我们没有足够的样本去观测“当 $T$ 改变时，$Y$ 会如何变化”。
    
    $$P(T=t | X) \approx 1 \quad (\text{for default system message})$$

4.  **ATE 估计失败**:
    模型无法学习到 System Message 对输出的平均处理效应（Average Treatment Effect, ATE）。在推理阶段引入新的 System Message 属于**OOD (Out-of-Distribution)** 泛化，且由于上述的数值精度问题，这种泛化极不稳定。

## 4. 解决方案与行动指南

如果需要模型严格遵循 System Message，需要在微调（Fine-tuning）阶段打破这种“惰性”：

- **增加 System 数据多样性**：在 SFT 数据中，强制混入大量不同的 System Prompts，即使它们对 User 任务没有直接帮助，也要强制模型去 attend 这个区域。
- **加权 Loss**：在计算 Loss 时，人为提高 System Message 区域 Token 的权重（虽然通常我们只计算 Completion 的 Loss，但可以通过 Attention Mask 或特殊机制强化 Context 的影响）。

---
**关联笔记**：
- [[Transformer Architecture]] - 了解 Attention 机制的计算细节。
- [[Numerical Stability in Deep Learning]] - 关于 FP16/BF16 的精度讨论。
- [[SFT Data Strategy]] - 数据配比策略。