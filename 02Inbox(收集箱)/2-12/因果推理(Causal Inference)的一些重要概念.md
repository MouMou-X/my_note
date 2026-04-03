---
tags:
  - 数学/因果推理
type: reference
source: https://zhuanlan.zhihu.com/p/659630025
created: 2026-02-12
aliases:
  - Causal Inference
status: 🌱
---
### 1. Propensity Score Matching

PSM有效的前提假设：  
1. conditional independence (namely, that unobserved factors do not affect participation)。也称为可忽略性假定(Ignorability)  
2. sizable common support or overlap in propensity scores across the participant and nonparticipant samples  
3. banlancing condition

### 2. Faithfulness Condition

如果A和B是统计独立的，则A，B之间不存在因果关系。

### 3. Mining Causal Structures

CCC Algorithms：发现A->B->C、A->B->C、C->B->A. 类型的因果关系。

CCU Algorithms：发现 A->C<-B 类型的因果关系。

### 4. do演算定律(将do表达式转换为see表达式)

see表达式：可以从观测数据中直接估计出的[条件概率]。

### 5. 混淆因子要求统计调整，中介因子禁止统计调整

### 6. [因果推断]第一定律

-   
    潜在结果$Y_{x}(u)$可以通过下述方法来推断：建构模型$M_{x}$(确保删除所有指向$x$的箭头)，并计算结果$Y(u)$。 因果关系之梯第二层和第三层中的所有可估量都由此产生。

从[结构模型]中推到反事实分为3步：

1. 外展。根据待研究样本和其他样本的数据来估计待研究样本的特质因子。(待研究样本在回归方程中的误差项)
2. 干预。用$do$[算子]改变模型，以反映我们提出的反事实假设。
3. 预测。根据调整后的模型和有关[外生变量]（第一步得到的特质因子），计算在[反事实条件]下样本的输出。

[《[The Book of Why](https://zhida.zhihu.com/search?content_id=234712763&content_type=Article&match_order=1&q=The+Book+of+Why&zhida_source=entity)》第八章 反事实: 探索关于假如的世界 ]

### 7. [因果模型]的可测试性

- 模型是否能测试其与数据的兼容性。

在[结构因果模型]中，如果两个变量满足d-sep，则它们是[条件独立]的，如果在数据中没有满足这两个变量是条件独立的，说明我们假设的模型存在问题。

### 8. [潜在结果模型]要求满足的3个假设

1. 单位处理效应稳定假设(Stable Unit Treatment Value Assumption, SUTVA)。 无论其他个体接受何种处理，对于每个个体而言，其处理效应都是不变的。
2. 一致性假设。
3. 可忽略性假设。 给定某组(去)混杂因子$Z$的值，$Y_{x}$独立于(对象)实际接受的处理$X$。 例，如果[混杂因子]$Z$的任意一层，本该有潜在结果$Y_{x}=y$的病人与本该有潜在结果$Y_{x}=y^{'}$的病人都有同样的可能被分配到处理组和对照组，那么把病人指派处理组和对照组的做法就是可忽略的。

### 9. 干预和[反事实]的区别

是否有事后判断（知道现实世界发生了什么）是干预和反事实之间的关键区别。

没有事后判断【反事实】  和【干预】  之间就没有区别

### 10. 充分因(Probablity of Sufficiency, PS)

在已知X=0, Y=0的情况下，假如X=1，则Y=1的概率。PS的值表示X是Y的充分因的概率。即，PS越大，越表明X能够导致Y的发生。

### 11. 必要因(Probability of Necessity, PN)

在已知X=1, Y=1的情况下，假如X=0，则Y=0的概率。PN的值表示X是Y的必要因的概率。即，PN越大，越表明是Y发生的原因是X，如果X不发生，Y就不会发生。

### 12. 总效应、直接效应、间接效应

直接效应：不通过中介物 间接效应：通过中介物

### 13. 受控直接效应(Control Direct Effect, CDE)

[因果图]：  . X: 性别 M: 院系 Y: 录取

CDE的计算： 将do表达式通过do演算转变为see表达式。

### 12. 自然直接效应(Natural Direct Effect, NDE)

因果图：  . X: 性别 M: 院系 Y: 录取

表示，一个女性申请者如果报告她的性别位男性的话（即，  ），申请她想申请的院系  ，被录取的概率。这里院系的选择是由真实的性别决定的，而录取是由报告的性别决定的。

NDE的计算： 难点：需要调用反事实的语言，所以我们不能用do演算来估计它。 解决方法：使用中介公式(Mediation Formula)。

### 13. [中介分析] (Mediation Analysis)

反事实方法最受欢迎的一种应用。

中介分析的目的是将直接效应从间接效应中解析出来。

### 14. 中介公式

- 计算自然间接效应  . 中括号内的[表达式]代表X对M的影响，乘号后面的表达式代表M对Y的影响（当X=0时）。该表达式没有下标(反事实)和do算子(干预)，因此可以根据第一层级的数据直接估计出来。  
    
- 计算自然直接效应  
    

### 15. 反事实一致性(Counterfactual Consistency Rule)

当反事实与事实重合时，得到的结果就是事实的结果。 比如 fact 是昨天吃冰淇凌拉肚子，那么反事实问题“如果我昨天吃冰淇凌会怎么样呢？”的答案就是拉肚子。

### 16. 如何估计do表达式的概率

如果接受干预的变量x是[根节点]，则 

### 17. 什么是结构因果模型

SCM由[变量集合]U，变量集合V，结构方程集合F构成。 V中的每个变量通过某个[结构方程]和其他变量(包括V、U)得到一个赋值。 U是外生变量集合，其不包含可解释机制。