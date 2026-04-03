---
tags: [数学/因果推理]
type: note
status: 🌿
---

要深入理解成对因果发现（Pairwise Causal Discovery, PCD），你无法仅依靠传统的基于条件独立性测试（Constraint-based）的方法，因为在仅有两个变量 $X$ 和 $Y$ 的情况下，马尔可夫等价类（Markov Equivalence Class）导致 $X \rightarrow Y$ 和 $Y \rightarrow X$ 在统计上往往是无法区分的。

PCD 的核心在于**利用分布的不对称性**或**函数形式的假设**来打破这种对称性。根据你的要求，以下是按照专业层级划分的必要知识体系：

### 1. 概率论与数理统计基础

这是分析数据分布特征的基石。

- **统计独立性（Statistical Independence）：** 必须深刻理解 $P(X, Y) = P(X)P(Y)$ 的定义以及如何在连续变量中度量它。
    
- **高阶矩（Higher-order Moments）：** 均值和方差不足以描述非高斯分布。你需要掌握偏度（Skewness）和峰度（Kurtosis），因为许多 PCD 方法（如 LiNGAM）依赖于数据的非高斯性（Non-Gaussianity）。
    
- **核方法（Kernel Methods）：** 掌握希尔伯特-施密特独立性准则（**HSIC**, Hilbert-Schmidt Independence Criterion）。这是目前衡量变量间（特别是残差与输入变量间）非线性独立性的标准工具。
    

### 2. 因果推断核心理论

理解为什么传统的图模型方法在两变量下失效，以及 PCD 如何解决这一问题。

- **结构因果模型（Structural Causal Models, SCM）：**
    
    理解形式 $Y = f(X, N_Y)$，其中 $N_Y$ 是外生噪声变量。
    
- **可识别性（Identifiability）：**
    
    这是 PCD 的核心概念。你需要知道在什么条件下，模型 $X \rightarrow Y$ 是可识别的，而逆向模型 $Y \rightarrow X$ 是被拒绝的。
    
    - 例如：如果是线性高斯模型（Linear Gaussian），则不可识别；如果是线性非高斯（Linear Non-Gaussian）或非线性加性噪声（Non-linear Additive Noise），则是可识别的。
        
- **马尔可夫等价（Markov Equivalence）：** 理解在没有额外假设的情况下，两个变量的联合分布 $P(X, Y)$ 可以被分解为 $P(Y|X)P(X)$ 或 $P(X|Y)P(Y)$，这在数学上是等价的。
    

### 3. 基于函数模型的假设（Functional Causal Models）

这是目前 PCD 领域最主流的方法论，通过对 $f$ 和 $N$ 的形式施加限制来推断方向。

- **加性噪声模型（Additive Noise Models, ANM）：**
    
    假设 $Y = f(X) + N$，且 $N \perp \!\!\! \perp X$（噪声独立于原因）。
    
    - **知识点：** 你需要掌握如何进行非线性回归（如高斯过程回归或神经网络回归），计算残差 $\hat{N} = Y - \hat{f}(X)$，并测试 $\hat{N}$ 是否独立于 $X$。
        
- **后非线性模型（Post-Nonlinear Models, PNL）：**
    
    假设 $Y = f_2(f_1(X) + N)$。这是 ANM 的推广，考虑了传感器失真或非线性观测的影响。
    
    - **知识点：** 涉及更复杂的独立性测试和可逆函数的数学性质。
        

### 4. 基于几何与信息论的方法

这类方法不依赖具体的函数形式，而是基于“原因和机制独立”的哲学假设。

- **信息几何因果推断（IGCI, Information Geometric Causal Inference）：**
    
    基于假设：$P(X)$（原因的分布）与 $P(Y|X)$（机制，通常表现为函数 $f$ 的斜率）是不相关的（Orthogonal/Uncorrelated）。
    
    - **知识点：** 熵（Entropy）、微分熵、对数变换以及分布的“峰值”与函数导数之间的关系。
        
- **柯尔莫哥洛夫复杂性（Kolmogorov Complexity）：**
    
    基于“奥卡姆剃刀”原则，认为正确的因果方向具有更低的描述复杂性。即 $K(P(X)) + K(P(Y|X)) < K(P(Y)) + K(P(X|Y))$。
    

### 5. 优化与算法实现

在实际应用中，PCD 往往转化为优化问题或分类问题。

- **回归分析（Regression Analysis）：** 熟练掌握各种回归技术（Kernel Ridge Regression, Gaussian Processes），用于拟合潜在的因果机制。
    
- **分类器设计：** 了解如何构建监督学习模型（如 GNN 或 CNN），将 PCD 视为二分类问题（输入 $X, Y$ 的样本，输出 1 代表 $X \rightarrow Y$，0 代表 $Y \rightarrow X$），这是近年来（如 RCC, NCC 算法）的研究热点。
    

---

**其他的学习路径：**

1. 先从 **ANM（加性噪声模型）** 入手，这是最直观且数学上最容易推导的框架。
    
2. 重点研究 **Hoyer (2009)** 关于非线性加性噪声模型的论文，它是该领域的奠基之作。
    
