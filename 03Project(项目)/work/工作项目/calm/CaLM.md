局限性：

当前benchmark往往局限于单一任务、单一指标（准确率）和单一语言（英文）

往往难以区分相关性和因果性

评估框架：

该框架共四个模块：[评估目标(Target)](https://alidocs.dingtalk.com/i/nodes/14lgGw3P8vxjwogPCvn1Ezj3V5daZ90D?utm_scene=team_space&iframeQuery=anchorId%3Duu_mkmfn57nm7u42bo470l)、[提示词策略(Prompt)](https://alidocs.dingtalk.com/i/nodes/14lgGw3P8vxjwogPCvn1Ezj3V5daZ90D?utm_scene=team_space&iframeQuery=anchorId%3Duu_mknlh0zfi6i8ql5mqvn)、[评估指标(Metric)](https://alidocs.dingtalk.com/i/nodes/14lgGw3P8vxjwogPCvn1Ezj3V5daZ90D?utm_scene=team_space&iframeQuery=anchorId%3Duu_mknlh24j716akm59mwq)、错误分析(Error)

## 评估目标(Target):

46种Tasks、中英2种语言，共92个数据集。

- 分为3类：
    
    - 自然语言描述的题目
        
    - 是否判断题目
        
    - 数学计算题目
        
- Task：（从容易到困难）
    
    - association (关联) ：观察变量间的统计依赖(What does the data say?)
        
        - correlation (相关性)
            
        - explaining_away_effect (解释消去效应)
            
    - causal_discovery (因果发现) ：从数据中发现因果关系(Is A connected to B?)
        
        - pairwise_causal_discovery ([[PCD成对因果发现]])
            
        - event_causality_identification (ECI, 事件因果识别)
            
        - causal_attribution (CA, 因果归因)
            
        - abstract_reasoning (AR, 抽象推理)
            
    - intervention (干预) ：采取行动改变变量(What if I do X?)
        
        - average_treatment_effect (ATE, 平均处理效应)
            
        - backdoor_adjustment_set (BAS, 后门调整集)
            
        - causal_effect_identification (FAS, 前门调整集)
            
        - collider_bias (IV, 工具变量)
            
        - controlled_direct_effect (CB, 对撞偏差)
            
        - frontdoor_adjustment_set (CEI, 因果效应识别)
            
        - instrumental_variable (CDE, 控制直接效应)
            
    - counterfactual (反事实) ：想象未发生的替代情景(What if I had done Y?)
        
        - actual_causality (AC, 实际因果)
            
        - causal_explanation_generation (CEG, 因果解释生成)
            
        - counterfactual_reasoning (CR, 反事实推理)
            
        - 以下任务属于数学/混合模式
            
        - effect_of_the_treatment_on_the_treated (ETT, 处理组的处理效应)
            
        - natural_direct_effect (NDE, 自然直接效应)
            
        - natural_indirect_effect (NIE, 自然间接效应)
            
        - probability_of_necessity (PN, 必要性概率)
            
        - probability_of_sufficiency (PS, 充分性概率)
            

## 提示词策略(Prompt):

|   |   |   |
|---|---|---|
|策略分类 (Category)|具体策略 (Specific Strategy)|描述 / 机制 (Description/Mechanism)|
|Basic Prompt<br><br>(基础提示)|Basic Prompt|直接将问题作为输入，不提供任何示例或额外指令。|
|Adversarial Prompt<br><br>(对抗性提示)|Adversarial-ignore<br><br>(对抗-忽略)|模型给出答案<br><br>提示“忽略你之前的答案，重新回答” 观察模型是否改变立场。|
||Adversarial-doubt<br><br>(对抗-质疑)|模型给出答案<br><br>提示“你之前的答案是错的，请重新回答” 观察模型是否盲目修改答案。|
|Chain-of-Thought<br><br>(CoT, 思维链)|0-shot CoT|在提示中添加指令："Let's think step by step"。|
||Manual CoT<br><br>(人工 CoT)|包含详细推理步骤的人工编写示例 (Few-shot)。|
|In-context Learning<br><br>(IcL, 上下文学习)|0-shot IcL|只提供任务背景描述，无示例。|
||1-shot IcL|提供 1 个示例。|
||3-shot IcL|提供 3 个示例。|
|Explicit Function<br><br>(EF, 显式功能)|Explicit Function|通过指令赋予模型特定角色或功能设定。<br><br>例如："You are a helpful assistant for causal reasoning..."|

## 评估指标(Metric):

准确率 (Accuracy)

鲁棒性 (Robustness)

可解性 (Solvability) （备注：待确认）

## 错误分析(Error):

准确率(Accuracy)

检查所有预测是否相同（Same response to all questions）

中文任务检测英文，英文任务检测中文（Language inconsistency）

检查回答格式是否标准（Limitation of instruction-following）

检测重复内容（Repetition）

检测空回复（Empty response）