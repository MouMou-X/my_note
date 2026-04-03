---
tags: [数学/因果推理, LLM/Eval]
type: note
status: 🌿
---

**局限性：**
当前benchmark往往局限于单一任务、单一指标（准确率）和单一语言（英文）
往往难以区分相关性和因果性
**评估框架：**
该框架共四个模块：**评估目标(Target)**、**提示词策略(Prompt)**、**评估指标(Metric)**、**错误分析(Error)**


# 评估目标(Target)
- 评估目标(Target): 46种Tasks、中英2种语言，共92个数据集。
    - 分为3类：
        - 自然语言描述的题目
        - 符号化题目
        - 数学化题目
- Task：
    - [[association(关联)]]
        - correlation(相关性)
        - explaining_away_effect(解释消去效应)
    - [[causal_discovery(因果发现)]]
        - abstract_reasoning(AR, 抽象推理)
        - causal_attribution(CA, 因果归因)
        - event_causality_identification(ECI, 事件因果识别)
        - pairwise_causal_discovery(PCD, 成对因果发现)
    - [[counterfactual(反事实)]]
        - actual_causality(AC, 实际因果)
        - causal_explanation_generation(CEG, 因果解释生成)
        - counterfactual_reasoning(CR, 反事实推理)
        - effect_of_the_treatment_on_the_treated(ETT, 处理组的处理效应)
        - natural_direct_effect(NDE, 自然直接效应)
        - natural_indirect_effect(NIE, 自然间接效应)
        - probability_of_necessity(PN, 必要性概率)
        - probability_of_sufficiency(PS, 充分性概率)
    - [[intervention(干预)]]
        - average_treatment_effect(ATE, 平均处理效应)
        - backdoor_adjustment_set(BAS, 后门调整集)
        - causal_effect_identification(FAS, 前门调整集)
        - collider_bias(IV, 工具变量)
        - controlled_direct_effect(CB, 对撞偏差)
        - frontdoor_adjustment_set(CEI, 因果效应识别)
        - instrumental_variable(CDE, 控制直接效应)

# 提示词策略(Prompt)
- CaLM 从上述分类中筛选并实施了 5 大类、共 9 种 具体的[[提示词策略]]。
	- Basic Prompt 
	- Adversarial Prompt
		- Adversarial-ignore
		- Adversarial-doubt 
	- Chain-of-Thought 
		- 0-shot CoT
		- Manual CoT 
	- In-context Learning 
		- 0-shot IcL
		- 1-shot IcL
		- 3-shot IcL
	- Explicit Function 

<table> <thead> <tr> <th>策略分类 (Category)</th> <th>具体策略 (Specific Strategy)</th> <th>描述 / 机制 (Description/Mechanism)</th> </tr> </thead> <tbody> <tr> <td><strong>Basic Prompt</strong><br>(基础提示)</td> <td><strong>Basic Prompt</strong></td> <td>直接将问题作为输入，不提供任何示例或额外指令。</td> </tr> <tr> <td rowspan="2"><strong>Adversarial Prompt</strong><br>(对抗性提示)</td> <td><strong>Adversarial-ignore</strong><br>(对抗-忽略)</td> <td>模型给出答案 &rarr; 提示“忽略你之前的答案，重新回答” &rarr; 观察模型是否改变立场。</td> </tr> <tr> <td><strong>Adversarial-doubt</strong><br>(对抗-质疑)</td> <td>模型给出答案 &rarr; 提示“你之前的答案是错的，请重新回答” &rarr; 观察模型是否盲目修改答案。</td> </tr> <tr> <td rowspan="2"><strong>Chain-of-Thought</strong><br>(CoT, 思维链)</td> <td><strong>0-shot CoT</strong></td> <td>在提示中添加指令："Let's think step by step"。</td> </tr> <tr> <td><strong>Manual CoT</strong><br>(人工 CoT)</td> <td>包含详细推理步骤的人工编写示例 (Few-shot)。</td> </tr> <tr> <td rowspan="3"><strong>In-context Learning</strong><br>(IcL, 上下文学习)</td> <td><strong>0-shot IcL</strong></td> <td>只提供任务背景描述，无示例。</td> </tr> <tr> <td><strong>1-shot IcL</strong></td> <td>提供 1 个示例。</td> </tr> <tr> <td><strong>3-shot IcL</strong></td> <td>提供 3 个示例。</td> </tr> <tr> <td><strong>Explicit Function</strong><br>(EF, 显式功能)</td> <td><strong>Explicit Function</strong></td> <td>通过指令赋予模型特定角色或功能设定。<br>例如："You are a helpful assistant for causal reasoning..."</td> </tr> </tbody> </table>
