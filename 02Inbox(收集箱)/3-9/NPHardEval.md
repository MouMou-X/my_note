---
type: paper
source:
  - "[arxiv](https://arxiv.org/html/2312.14890?_immersive_translate_auto_translate=1)"
  - "[claude](https://claude.ai/chat/64f7be74-e6b7-44af-b161-24c4b3a102f4)"
  - "[gemini](https://gemini.google.com/app/428eb2c8bace0e9b)"
---
# NPHardEval：基于复杂度类别的大型语言模型推理能力动态基准测试

Lizhou Fan†*, Wenyue Hua‡*, Lingyao Li†, Haoyang Ling†, Yongfeng Zhang‡  
†School of Information, University of Michigan, Ann Arbor, MI 48103  
‡Department of Computer Science, Rutgers University, New Brunswick, NJ 08854  
lizhouf@umich.edu, wenyue.hua@rutgers.edu, {lingyaol, hyfrankl}@umich.edu, yongfeng.zhang@rutgers.edu *Lizhou Fan and Wenyue Hua contribute equally

## Abstract  摘要
复杂推理能力是当前大型语言模型（LLMs）最重要的特征之一，它也在复杂决策任务中发挥着不可或缺的作用。因此，对 LLMs 推理能力的研究至关重要：目前已建立了众多基准来评估 LLMs 的推理能力。然而，当前的基准在严格评估 LLMs 所能达到的全部推理能力方面存在不足。它们也容易面临过拟合的风险，因为这些基准是公开可访问且静态的，使得模型可能针对特定基准指标调整其响应，从而夸大其性能。针对这些局限性，我们的研究引入了一个名为 NPHardEval 的新基准。该基准旨在通过涵盖高达 NP-Hard 复杂度类别的 900 个算法问题，全面评估 LLMs 的推理能力。这些问题经过精心挑选，代表了 NP-hard 复杂度类别之下的广泛复杂度类别，为 LLMs 的推理能力提供了严格的衡量标准。 通过本研究，我们揭示了 LLMs 在推理能力方面的现状，通过比较 LLMs 在不同复杂度类别中的表现，提供了一个客观且严谨的视角。我们的发现对于理解 LLMs 在推理任务中的当前能力具有重要意义，并为未来提升这些模型的推理能力奠定了基础。此外，该基准测试设计有动态更新机制，数据点每月刷新一次。这种定期更新对于降低 LLMs 对基准测试过拟合的风险至关重要，有助于更准确、更可靠地评估其推理能力。NPHardEval 的基准数据集和代码可在 https://github.com/casmlab/NPHardEval 上获取。

## 1 引言

LLMs 的进步引领了人工智能研究进入一个变革时代 [fan2023bibliometric](NPHardEval#[1])。许多研究者认为，这些模型展现出的无与伦比的推理能力是其一大优势 [zhao2023survey](NPHardEval#[2])。尽管已经实施了多种基准测试来评估推理能力 [cobbe2021training](NPHardEval#[3]); [valmeekam2022large](NPHardEval#[4]); [chen2023theoremqa](NPHardEval#[5]); [hendrycks2020measuring](NPHardEval#[6]); [hendrycksmath2021](NPHardEval#[7])，但现有方法仍存在一些局限性。这些局限性包括对推理能力的精确刻画不足、模型可能对特定基准测试过拟合的风险 [schaeffer2023pretraining](NPHardEval#[8])，以及在某些情况下对人工评估方法的依赖 [frieder2023mathematical](NPHardEval#[9])。此外，从理论上探讨 LLMs 能在多大程度上解决计算复杂性层次结构中的问题 [johnson1990catalog](NPHardEval#[10])，特别是 NP-hard或 NP-complete问题，也颇具意义。 针对这些问题与挑战，我们推出了全新基准测试 NPHardEval，该基准基于成熟的计算复杂度理论框架，旨在为大型语言模型的推理能力提供更严谨、可量化的评估体系。

我们的基准测试经过精心设计，旨在评估大型语言模型（LLMs）的推理能力，包含了 9 个精心挑选的推理任务。这些任务根据 [johnson1990catalog](NPHardEval#[10]) 中概述的复杂度类别进行划分，每个类别包含 100 个实例，分布在 10 个不同的难度级别。这种结构化的方法使得对 LLMs 推理能力的评估既全面又可量化。我们基准测试中问题的选择尤为重要，因为它也反映了现实世界决策和优化场景的细微差别，包括物流、调度、网络设计以及其他多个领域，这些领域的最优解决方案具有重大的经济和实际意义。随着 LLMs 在复杂问题解决场景中的应用日益增多，对其推理能力进行准确而严格的评估变得至关重要。这样的评估是衡量其能力的关键且可靠的指标，指导其在各种情境下的有效整合与应用。 我们也能更深入地洞察其计算推理能力的优势与局限。


我们基准测试的另一项新颖特性在于其端到端的自动化流程，涵盖了任务生成与结果验证的全过程。这一自动化得益于基准测试中采用的经典任务，这些任务已有成熟且完善的算法提供解决方案。这种系统化的方法确保了评估过程的高度准确性和可靠性，同时也便于基准测试中数据点的更新。这一自动化框架使得基准测试内的数据点更新变得轻而易举。因此，我们设计的基准测试每月更新其数据点，有效降低了模型对数据集过拟合的可能性。这种动态更新机制对于长期保持基准测试的严谨性和相关性至关重要。我们欢迎通过 [HuggingFace](https://huggingface.co/spaces/NPHardEval/NPHardEval-leaderboard) 上的 NPHardEval 排行榜直接提交模型性能至我们的基准测试：

总的来说，我们的基准测试相较于现有基准具备多项优势：

  
- 基准测试所采用的问题植根于成熟的计算复杂性层级理论——这是理论计算机科学领域深入研究的概念。这一理论基础使我们能够借助现有研究成果，对 LLM 的逻辑推理能力进行严格且量化的评估。
	
-  我们为这些问题设计了自动检查机制，因为它们基于可通过算法计算的问题。无需人工干预即可判定 LLM 回答的正确性。
	
- 该方法支持自动生成问题，使我们能够每月更新基准测试。这种月度刷新的基准测试有助于防止模型过拟合，因为我们始终可以生成具有不同难度等级的新问题用于评估。
	
- 该基准排除了对 LLM 而言尤为困难的数值计算问题。这种聚焦方式能更准确地评估 LLM 的纯粹逻辑推理能力，因为数值计算可能会干扰此类评估。
	
- 我们的方法论为领域内一个长期存在的有趣问题提供了新视角：LLM 在多大程度上能够处理归类为 NP 难或 NP 完全的问题。

通过运用该基准开展研究，我们旨在从三个关键维度评估和理解 LLM（基础模型）的推理能力：

1. 模型性能对比：我们的基准测试比较了 12 个闭源模型（包括 GPT 4 Turbo、Claude 2、GPT 3.5 Turbo、Claude Instant 和 PaLM 2）与开源模型（包括 Yi-34b、Qwen-14b、Mistral-7b、Phi-2、MPT-30b、Vicuna-13b 和 Phi-1.5）在三个复杂度类别（P 类、NP 完全类和 NP 难类）及 10 个难度级别上的推理能力。这一对比能够揭示这些模型的相对优势与不足，并确定它们在解决逐步挑战性问题上的熟练程度，从而评估其处理复杂度递增任务的能力。
	
2. 基准评估的稳健性：本研究探讨算法基准的频繁更新是否能有效防止“破解”基准的风险。基准的动态更新被提出作为一种策略，以降低 LLMs 对这些基准过拟合的可能性。然而，一个相关的问题随之产生：基于上个月的基准对 LLMs 进行微调，是否会导致对特定问题类型的过拟合？为探究此问题，我们进行了一项实验，其中三个开源模型——Phi-2、Mistral-7b 和 Qwen-14b——在五个不同版本的基准上进行了微调。这些模型的性能在两个版本的基准上进行了评估，每个版本在难度级别上有所不同。这种方法使我们能够评估微调是否使模型能够“破解”不同复杂度的基准。
	
3. 通过上下文学习实现泛化：在给定上下文示例的情况下，LLMs 是否能够真正学习并应用上下文示例中呈现的算法技能，而不仅仅是模仿问题解决过程 [wei2023larger](NPHardEval#[11]); [min2022rethinking](NPHardEval#[12])？我们通过评估 LLMs 在接触示例后，能否将解决方案泛化到同一任务中不同难度级别的新问题，来区分“学习”与“模仿”。我们的假设是，如果 LLM 真正掌握了底层的算法技能，它应该能够处理同一任务中不同难度级别的问题。反之，如果 LLM 仅仅是模仿，那么当面对问题难度的变化时，其性能可能会下降。

本文的贡献如下：我们提出了首个基于复杂度类别的推理基准 NPHardEval。该基准能够对 LLMs 在不同难度级别的广泛复杂推理任务上的能力进行严格评估。通过上述研究问题，我们旨在对 LLMs 的推理能力进行全面分析，探索其在真正理解和应用复杂问题解决技能方面的潜力。

![Refer to caption](https://arxiv.org/html/2312.14890v4/extracted/5404715/Fig/NP-hard.jpg)
图 1：计算复杂度类别 P、NP 完全与 NP 难及其对应任务

## 2 相关工作

### 2.1 LLMs 的推理能力

LLMs [brown2020language](NPHardEval#[13]); [chowdhery2023palm](NPHardEval#[14]); [chung2022scaling](NPHardEval#[15]) 在自然语言处理及相关领域取得了显著进展。近期研究强调了 LLMs 在从生物医学、人机交互研究到人文社科等多个领域展现出的前所未有的推理能力 [huang2022towards](NPHardEval#[16]); [hua2023war](NPHardEval#[17]); [fan2023datachat](NPHardEval#[18]); [gao2023examining](NPHardEval#[19]); [li2023hot](NPHardEval#[20])。有讨论指出，这些模型在规模足够大时表现出“涌现”行为，包括“推理”能力 [wei2022emergent](NPHardEval#[21]); [schaeffer2023emergent](NPHardEval#[22])。通过使用简单的提示“让我们一步步思考”为模型提供思维链，这些模型能够以明确的推理步骤回答问题 [wei2022chain](NPHardEval#[23])。由于推理能力是人类智能的标志，这引发了学术界的广泛兴趣。目前已发展出多种思维链的变体来激发模型的推理能力 [kojima2022large](NPHardEval#[24]); [wang2022iteratively](NPHardEval#[25]); [hua2022system](NPHardEval#[26])，例如思维树 [yao2023tree](NPHardEval#[27])、思维图 [besta2023graph](NPHardEval#[28])、自我启发技术 [wang2023recmind](NPHardEval#[29])。

Later, various self-critique methods have been proposed to enhance LLM’s reasoning performance. The Recursively Criticizes and Improves (RCI) approach, for example, iteratively refines outputs, proving more effective in automating computer tasks and elevating reasoning capabilities [kim2023language](https://arxiv.org/html/2312.14890v4#bib.bib30). Similarly, backward verification proposes an intuitive human-like mechanism for LLMs to self-check and improve their conclusions, reducing errors in reasoning tasks [weng2022large](https://arxiv.org/html/2312.14890v4#bib.bib31). Moreover, the interplay of reasoning and action showcases LLMs’ outstanding synergistic ability. For instance, the “ReAct” approach highlights that reasoning can enhance action plans, while actions can help the model interface with external sources for better reasoning [yao2022react](https://arxiv.org/html/2312.14890v4#bib.bib32). In addition, the capability of LLMs to learn from feedback also indicates their reasoning potential. “Reflexion” is a workflow that reinforces LLMs through linguistic feedback without updating model weights [shinn2023reflexion](https://arxiv.org/html/2312.14890v4#bib.bib33). In robotic contexts, LLMs demonstrate enhanced performance with environment feedback, creating an internal “monologue” to assist decision-making [huang2022inner](https://arxiv.org/html/2312.14890v4#bib.bib34).  
随后，各种自我批判方法被提出以提升 LLM 的推理性能。例如，递归批判与改进（RCI）方法通过迭代优化输出，在自动化计算机任务和提升推理能力方面被证明更为有效 kim2023language。类似地，反向验证为 LLMs 提出了一种直观的类人机制，使其能够自我检查并改进结论，从而减少推理任务中的错误 weng2022large。此外，推理与行动的交互展示了 LLMs 卓越的协同能力。例如，“ReAct”方法强调推理可以增强行动计划，而行动则能帮助模型与外部资源交互以实现更好的推理 [yao2022react](NPHardEval#[32])。另外，LLMs 从反馈中学习的能力也表明了其推理潜力。“Reflexion”是一种通过语言反馈强化 LLMs 的工作流程，无需更新模型权重 [shinn2023reflexion](NPHardEval#[33])。在机器人领域，LLMs 借助环境反馈展现出增强的性能，通过创建内部“独白”来辅助决策 huang2022inner。

Despite the impressive performance exhibited by LLMs, there remains a gap in our rigorous understanding of the extent and depth of reasoning these models are capable of. Our paper aims to address this gap by providing a framework to study the reasoning abilities of LLMs within the well-established hierarchy of computational complexity. This approach seeks to systematically evaluate and quantify their reasoning capabilities in a more structured and academically rigorous manner.  
尽管 LLMs 展现出了令人瞩目的性能，但我们对其推理能力的广度和深度仍缺乏严谨的理解。本文旨在通过提供一个框架，在计算复杂性这一成熟的理论体系内研究 LLMs 的推理能力，从而弥补这一空白。该方法试图以更具结构性和学术严谨性的方式，系统地评估和量化它们的推理能力。

### 2.2Benchmarks of LLMs’ Performance  
2.2 LLMs 性能基准测试

The advancement of LLMs has catalyzed the evolution of a range of general-purpose AI technologies, underscoring the importance of accurately assessing these models’ reasoning capabilities. Existing evaluation approaches predominantly rely on datasets comprising human-generated questions and their standard answers. For instance, MMLU [hendrycks2020measuring](https://arxiv.org/html/2312.14890v4#bib.bib6) and GAOKAO [zhang2023evaluating](https://arxiv.org/html/2312.14890v4#bib.bib35) both utilize human exam questions in their automated evaluations. Additionally, datasets such as the French National Math Exam, Hungarian National High School Exam11https://huggingface.co/datasets/keirp/hungarian_national_hs_finals_exam  
LLMs 的进步推动了一系列通用人工智能技术的发展，这凸显了准确评估这些模型推理能力的重要性。现有的评估方法主要依赖于包含人类生成问题及其标准答案的数据集。例如，MMLU（hendrycks2020measuring）和 GAOKAO（zhang2023evaluating）都在其自动化评估中使用了人类考试题目。此外，像法国国家数学考试、匈牙利国家高中考试等数据集也被用于此目的。, and GHOST (Graduate-Level High-Order Skill Tests)[frieder2023mathematical](https://arxiv.org/html/2312.14890v4#bib.bib9) are utilized to assess LLMs’ reasoning proficiency. [zhu2023dyval](https://arxiv.org/html/2312.14890v4#bib.bib36) proposes a dynamic graph-based reasoning benchmark. These sources aim to ensure the absence of data leakage. Nonetheless, the requirement for manual verification of answers in these datasets limits their practical utility. In general, these datasets are commonly employed as benchmarks in the field; however, they lack a quantitative metric for assessing the difficulty level of the questions and the extent of reasoning necessary to answer them. This absence of precise measurement criteria results in a limited understanding of the logical reasoning capabilities of large language models.  
以及 GHOST（研究生级高阶技能测试）frieder2023mathematical 被用来评估 LLMs 的推理能力。zhu2023dyval 提出了一个基于动态图的推理基准。这些资源旨在确保不存在数据泄露。然而，这些数据集中需要人工验证答案，这限制了它们的实际效用。总的来说，这些数据集通常被用作该领域的基准；但它们缺乏一个量化指标来评估问题的难度级别以及回答这些问题所需的推理程度。这种精确测量标准的缺失导致了对大型语言模型逻辑推理能力的理解有限。

Other Benchmarks such as AlpacaEval [dubois2023alpacafarm](https://arxiv.org/html/2312.14890v4#bib.bib37) and SuperCLUE [xu2023superclue](https://arxiv.org/html/2312.14890v4#bib.bib38) have attempted to incorporate open-ended questions in English and Chinese, respectively, to capture a diverse breadth of possible answers and enhance the comprehensiveness of LLM’s evaluation. However, they are not universal and are often constrained by language barriers and cultural contexts, potentially skewing the evaluation of reasoning abilities toward a specific scenario. reasoning tasks should transcend linguistic and cultural specifics, focusing instead on universal logical principles. Big-Bench Hard [suzgun2022challenging](https://arxiv.org/html/2312.14890v4#bib.bib39), DROP [dua2019drop](https://arxiv.org/html/2312.14890v4#bib.bib40), and HellaSwag [zellers2019hellaswag](https://arxiv.org/html/2312.14890v4#bib.bib41), while valuable, predominantly target multi-step reasoning, reading comprehension, and commonsense reasoning, respectively. They do not adequately prioritize complex logical reasoning in their assessment criteria.  
其他基准测试，如 AlpacaEval dubois2023alpacafarm 和 SuperCLUE xu2023superclue，分别尝试在英语和中文中融入开放式问题，以捕捉答案的多样性并提升 LLM 评估的全面性。然而，这些基准并非普适，常常受限于语言障碍和文化背景，可能导致推理能力的评估偏向特定情境。推理任务应超越语言和文化的具体细节，转而聚焦于普适的逻辑原则。Big-Bench Hard suzgun2022challenging、DROP dua2019drop 和 HellaSwag zellers2019hellaswag 虽然各有价值，但主要分别针对多步推理、阅读理解和常识推理。它们在评估标准中并未充分优先考虑复杂的逻辑推理。

The prevalent focus on question answering and math problems in current benchmarks may insufficiently capture the essence of reasoning - the ability to logically process and deduce information beyond memorized knowledge. It also falls short on providing a rigorous metric on the reasoning ability. This gap highlights the need for a paradigm expansion in LLM evaluation, calling for logic-based reasoning benchmarks to complete the traditional utility-based approach, where we have quantitative evaluation on the computational complexity of the questions, indicating the amount of reasoning ability required.  
当前基准测试普遍聚焦于问答和数学问题，可能不足以捕捉推理能力的本质——即超越记忆知识、进行逻辑处理和推演信息的能力。同时，这些测试也未能提供衡量推理能力的严谨指标。这一差距凸显了在 LLM 评估中扩展范式的必要性，呼吁引入基于逻辑的推理基准，以完善传统的基于实用性的评估方法。在新范式中，我们将对问题的计算复杂度进行量化评估，从而揭示所需推理能力的程度。

## 3Benchmark Construction  3 基准构建

### 3.1Complexity Classes  3.1 复杂度类别

In our study, we employ the concept of complexity classes to categorize the reasoning tasks for LLMs. These classes are defined based on the computational resources, such as time or memory, required to solve the problems they contain [johnson1990catalog](https://arxiv.org/html/2312.14890v4#bib.bib10). Primarily, most complexity classes comprise decision problems that can be solved using a Turing machine, with differentiation based on their time or space (memory) requirements. For example, the class P includes decision problems that a deterministic Turing machine can solve in polynomial time. Tasks within this class often pose multi-dimensional cognitive challenges, enriching the evaluation framework of LLMs. This structured approach not only aids in assessing the reasoning capabilities of LLMs but also holds substantial relevance in various practical applications, particularly in optimization and high-level decision-making scenarios.  
在我们的研究中，我们采用复杂度类别的概念来对 LLMs 的推理任务进行分类。这些类别是基于解决其中问题所需的计算资源（如时间或内存）来定义的 johnson1990catalog。主要来说，大多数复杂度类别包含决策问题，这些问题可以通过图灵机解决，并根据其时间或空间（内存）需求进行区分。例如，P 类包含确定性图灵机可以在多项式时间内解决的决策问题。此类中的任务通常带来多维度的认知挑战，丰富了 LLMs 的评估框架。这种结构化方法不仅有助于评估 LLMs 的推理能力，而且在各种实际应用中，特别是在优化和高级决策场景中，具有重要的相关性。

In particular, we use three complexity classes to define the task complexity in the benchmark, including P (polynomial time), NP-complete (nondeterministic polynomial-time complete), and NP-hard, which are increasingly complex in both the intrinsic difficulty and the resources needed to solve them. Figure [1](https://arxiv.org/html/2312.14890v4#S1.F1 "Figure 1 ‣ 1 Introduction ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes") shows their relation regarding computational complexity in an Euler diagram. This approach aims to delineate the extent of complex reasoning achievable by LLMs, thus for each complexity class, we only choose tasks from the non-overlapping subset of the complexity class. In our selection criteria, we intentionally exclude tasks that demand intensive mathematical computations, such as matrix multiplication and logarithmic calculations. Thus, we do not list NP class (questions in NP but not P and not NP-complete), which is exemplified by the discrete logarithm and integer factorization problems, as the majority of such problems are characterized by their calculation-intensive nature (see details in Appendix [B](https://arxiv.org/html/2312.14890v4#A2 "Appendix B Choices of Problems ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes")).  
具体而言，我们采用三个复杂度类别来定义基准测试中的任务复杂度，包括 P 类（多项式时间）、NP 完全类（非确定性多项式时间完全）和 NP 难类，它们在内在难度和所需解决资源上依次递增。图 1 以欧拉图形式展示了它们在计算复杂度方面的关系。该方法旨在界定 LLMs 可实现的复杂推理范围，因此针对每个复杂度类别，我们仅选取该类别非重叠子集中的任务。在我们的筛选标准中，我们有意排除了需要密集数学计算的任务，例如矩阵乘法和对数运算。因此，我们未列出 NP 类（属于 NP 但不属于 P 且非 NP 完全的问题），其典型代表包括离散对数和整数分解问题，因为此类问题大多以计算密集型为特征（详见附录 B）。

#### 3.1.1P (Polynomial time) Tasks  
3.1.1 P 类（多项式时间）任务

This class consists of tasks that can be solved by a deterministic Turing machine in polynomial time. Essentially, it represents tasks that are efficiently solvable. We include three P problems in the benchmark, namely Sorted Array Search (SAS), Edit Distance Problem (EDP), and Shortest Path Problem (SPP).  
此类任务可由确定性图灵机在多项式时间内解决。本质上，它代表了可高效求解的任务。我们在基准测试中包含了三个 P 类问题，即有序数组搜索（SAS）、编辑距离问题（EDP）和最短路径问题（SPP）。

##### Sorted Array Search (SAS)  
有序数组搜索（SAS）

SAS is about finding the position of a target value after sorting a given array. Given an array A of n elements and a target value T, the goal is to determine the index at which T is located in A after sorting. Renowned algorithms like binary search efficiently accomplish this task by iteratively halving the search interval, operating in logarithmic time. The problem can be formally stated as finding an index i such that A⁢[i]=T, or determining that no such index exists. It is commonly used in databases and search engines to quickly find specific data within a large dataset [kipf2019sosd](https://arxiv.org/html/2312.14890v4#bib.bib42).  
SAS（排序后搜索）旨在确定给定数组排序后目标值的位置。给定一个包含 n 个元素的数组 A 和目标值 T ，目标是在排序后的数组 A 中找到 T 所在的索引。著名的算法如二分搜索通过迭代地将搜索区间减半，以对数时间复杂度高效完成此任务。该问题可形式化表述为：寻找索引 i 使得 A⁢[i]=T 成立，或确定不存在这样的索引。它常用于数据库和搜索引擎中，以快速在大型数据集中查找特定数据 kipf2019sosd。

##### Edit Distance Problem (EDP)  
编辑距离问题（EDP）

EDP is about finding the minimum number of operations required to transform one string into another. Given two strings, A and B, of lengths m and n respectively, the aim is to determine the minimum number of operations needed to convert A into B. The allowable operations are insertion, deletion, and substitution of a single character. Formally, the problem can be defined as finding a minimum number d such that string A can be transformed into string B using d operations. This algorithm has a time complexity of 𝒪⁢(a⁢b) where a and b are the lengths of the strings. When the full dynamic programming table is constructed, its space complexity is also 𝒪⁢(a⁢b). EDP has widespread applications, especially in fields like computational biology for sequence alignment, natural language processing for spell checking and correction, and in data analysis for measuring similarity between data strings.  
编辑距离问题旨在计算将一个字符串转换为另一个字符串所需的最少操作次数。给定两个长度分别为 m 和 n 的字符串 A 和 B ，目标是确定将 A 转换为 B 所需的最小操作数。允许的操作包括插入、删除和替换单个字符。形式化地，该问题可定义为寻找最小数值 d ，使得字符串 A 能够通过 d 次操作转换为字符串 B 。该算法的时间复杂度为 𝒪⁢(a⁢b) ，其中 a 和 b 分别为字符串的长度。当构建完整的动态规划表时，其空间复杂度同样为 𝒪⁢(a⁢b) 。编辑距离问题具有广泛的应用，特别是在计算生物学中的序列比对、自然语言处理中的拼写检查与纠正，以及数据分析中用于衡量数据字符串间相似性等领域。

##### Shortest Path Problem (SPP)  
最短路径问题（SPP）

SPP is about finding the shortest path between two nodes in a non-negative weighted graph. In our experiments, we ask for the shortest path between the first and last nodes. Given a graph G=(V,E) with a weight function w:E→ℝ assigning weights to edges, and two vertices u and v in V, the task is to find the path from u to v that minimizes the total weight. This is often solved using Dijkstra’s algorithm which systematically expands the shortest path from the starting node until it reaches the target node. Formally, the problem is to find a path P=(v1,v2,…,vk), where v1=u and vk=v, such that the sum of weights of consecutive edges in P, ∑i=1k−1w⁢(vi,vi+1), is minimized. This problem can be used in network routing, GPS navigation systems, and logistics to find the shortest or most efficient path between two points. It helps in reducing travel time and costs in transportation and communication networks.  
SPP 涉及在非负加权图中寻找两个节点之间的最短路径。在我们的实验中，我们要求找出第一个节点与最后一个节点之间的最短路径。给定一个图 G=(V,E) 及其为边分配权重的权重函数 w:E→ℝ ，以及 V 中的两个顶点 u 和 v ，任务是找到从 u 到 v 的路径，使得总权重最小。这通常使用 Dijkstra 算法解决，该算法系统地扩展从起始节点出发的最短路径，直至到达目标节点。形式上，该问题是要找到一条路径 P=(v1,v2,…,vk) ，其中 v1=u 且 vk=v ，使得 P 中连续边的权重之和 ∑i=1k−1w⁢(vi,vi+1) 最小化。此问题可用于网络路由、GPS 导航系统和物流领域，以找到两点之间最短或最高效的路径。它有助于减少运输和通信网络中的旅行时间和成本。

#### 3.1.2NP-complete problems  
3.1.2 NP 完全问题

This is a subset of NP. A problem is NP-complete if it is in NP and as hard as any problem in NP. If any NP-complete problem can be solved in polynomial time, then every problem in NP can also be solved in polynomial time. We include three NP-complete problems that are not in P in the benchmark, namely Traveling Salesman Problem Decision Version (TSP-D), Graph Coloring Problem Decision Version (GCP-D), and Knapsack Problem (KSP).  
这是 NP 的一个子集。如果一个问题是 NP 问题，并且与 NP 中的任何问题一样难，那么它就是 NP 完全问题。如果任何 NP 完全问题可以在多项式时间内解决，那么 NP 中的每个问题也都可以在多项式时间内解决。我们在基准测试中包含了三个不在 P 中的 NP 完全问题，即旅行商问题决策版本（TSP-D）、图着色问题决策版本（GCP-D）和背包问题（KSP）。

##### Traveling Salesman Problem (Decision Version, TSP-D)  
旅行商问题（决策版本，TSP-D）

TSP-D is concerned with determining if a salesman can complete a route, visiting each city at least once, with the total travel distance being less than a specified value. Given a complete graph G=(V,E) with vertices V representing cities and edges E representing paths between cities, each edge (i,j) is assigned a distance d⁢(i,j). The decision version of this problem asks whether there exists a tour (a sequence of cities) such that the total distance of the tour is less than or equal to a given value D. Formally, the problem can be stated as finding a permutation P of the set of cities 1,2,…,n that satisfies the condition ∑i=1n−1d⁢(P⁢(i),P⁢(i+1))+d⁢(P⁢(n),P⁢(1))≤D. This problem is useful in logistics and supply chain management in planning efficient delivery routes and schedules [roberti2021exact](https://arxiv.org/html/2312.14890v4#bib.bib43).  
TSP-D 问题关注的是判断一名销售员能否完成一条路线，要求至少访问每个城市一次，且总旅行距离小于指定值。给定一个完全图 G=(V,E) ，其顶点 V 代表城市，边 E 代表城市间的路径，每条边 (i,j) 被赋予一个距离 d⁢(i,j) 。该问题的决策版本询问是否存在一条旅行路线（城市序列），使得路线的总距离小于或等于给定值 D 。形式化地，该问题可表述为寻找城市集合 1,2,…,n 的一个排列 P ，满足条件 ∑i=1n−1d⁢(P⁢(i),P⁢(i+1))+d⁢(P⁢(n),P⁢(1))≤D 。此问题在物流和供应链管理中，对于规划高效的配送路线和时间表具有实用价值。

##### Graph Coloring Problem (Decision Version, GCP-D)  
图着色问题（决策版本，GCP-D）

GCP-D involves determining if it is possible to color the vertices of a graph using a given number of colors so that no two adjacent vertices share the same color. Given an undirected graph G=(V,E), with V representing vertices and E representing edges, the goal is to find out if there is a way to assign one of k colors to each vertex such that for any edge (u,v)∈E, the vertices u and v have different colors. The formal statement is to determine if there exists a coloring function c:V→1,2,…,k such that for every edge (u,v)∈E, c⁢(u)≠c⁢(v). It has wide applications in Round-Robin Sports Scheduling, Aircraft scheduling, and Biprocessor tasks [ahmed2012applications](https://arxiv.org/html/2312.14890v4#bib.bib44).  
GCP-D 问题涉及判断是否能够使用给定数量的颜色对图的顶点进行着色，使得任意两个相邻顶点不共享相同颜色。给定一个无向图 G=(V,E) ，其中 V 表示顶点， E 表示边，目标是确定是否存在一种方式，为每个顶点分配 k 种颜色中的一种，使得对于任意边 (u,v)∈E ，顶点 u 和 v 具有不同的颜色。形式化表述为：判断是否存在一个着色函数 c:V→1,2,…,k ，使得对于每条边 (u,v)∈E ，满足 c⁢(u)≠c⁢(v) 。该问题在循环赛程安排、飞机调度和双处理器任务等领域有广泛应用（ahmed2012applications）。

##### Knapsack Problem (KSP)  背包问题（KSP）

KSP asks whether a subset of items can be chosen to fit into a knapsack of fixed capacity without exceeding it, while also maximizing the total value of the selected items. Consider a set of items, each with a weight wi and a value vi, and a knapsack with a weight capacity W. The problem is to select a subset of these items such that the total weight does not exceed W and the total value is maximized. Formally, let xi be a binary variable indicating whether item i is included in the knapsack (xi=1) or not (xi=0). The problem can be stated as maximizing ∑i=1nvi⁢xi subject to the constraint ∑i=1nwi⁢xi≤W, where n is the number of items. It is used in resource allocation and budgeting where the goal is to maximize the total value of a selection under a weight or cost constraint. Applications include cargo loading, and electric vehicle charging [sun2020competitive](https://arxiv.org/html/2312.14890v4#bib.bib45); [cho2019knapsack](https://arxiv.org/html/2312.14890v4#bib.bib46).  
KSP 问题询问是否可以选择一个物品子集，在不超过固定容量的情况下装入背包，同时最大化所选物品的总价值。考虑一组物品，每个物品具有重量 wi 和价值 vi ，以及一个重量容量为 W 的背包。问题在于选择这些物品的一个子集，使得总重量不超过 W ，并且总价值最大化。形式上，令 xi 为一个二元变量，表示物品 i 是否被包含在背包中（ xi=1 表示包含， xi=0 表示不包含）。该问题可以表述为最大化 ∑i=1nvi⁢xi ，同时满足约束条件 ∑i=1nwi⁢xi≤W ，其中 n 是物品的数量。它被用于资源分配和预算制定中，目标是在重量或成本约束下最大化选择的总价值。应用场景包括货物装载和电动汽车充电（sun2020competitive; cho2019knapsack）。

#### 3.1.3NP-hard problems  3.1.3 NP 难问题

These problems are at least as hard as the hardest problems in NP. They may not necessarily be in NP (i.e., they may not have solutions verifiable in polynomial time) but solving an NP-hard problem in polynomial time would imply that P = NP. We include three NP-hard problems that are not reducible to NP-complete problems in the benchmark, namely Traveling Salesman Problem Optimization Version (TSP), Graph Coloring Problem Optimization Version (GCP), and Meeting Scheduling Problem (MSP).  
这些问题至少与 NP 中最难的问题一样困难。它们不一定属于 NP 类（即，它们的解可能无法在多项式时间内验证），但若能在多项式时间内解决一个 NP 难问题，则意味着 P = NP。我们在基准测试中包含了三个无法归约为 NP 完全问题的 NP 难问题，即旅行商问题优化版本（TSP）、图着色问题优化版本（GCP）和会议调度问题（MSP）。

##### Traveling Salesman Problem (Optimization Version, TSP)  
旅行商问题（优化版本，TSP）

TSP-O involves finding the shortest route for a salesman to visit each city exactly once and return to the starting city. Given a complete graph Kn with n vertices, where each vertex represents a city and each edge (i,j) is assigned a non-negative cost or distance d⁢(i,j), the problem is to find the shortest possible route that visits each city exactly once and returns to the origin city. Formally, let P be a permutation of the set of cities 1,2,…,n representing the order in which the cities are visited. The traveling salesman problem can be formulated as finding the permutation P that minimizes the total travel cost, given by the function f⁢(P)=d⁢(P⁢(n),P⁢(1))+∑i=1n−1d⁢(P⁢(i),P⁢(i+1)). This problem is important in operational research and logistics to find the most efficient route to visit multiple locations and return to the origin, particularly route planning for delivery services, maintenance operations, and sales.  
旅行商问题（优化版本，TSP-O）涉及为销售员找到一条最短路径，使其恰好访问每个城市一次并返回起点城市。给定一个具有 n 个顶点的完全图 Kn ，其中每个顶点代表一个城市，每条边 (i,j) 被分配一个非负成本或距离 d⁢(i,j) ，问题在于找到一条可能的最短路径，该路径恰好访问每个城市一次并返回起点城市。形式上，令 P 为城市集合 1,2,…,n 的一个排列，表示访问城市的顺序。旅行商问题可以表述为找到排列 P ，使得由函数 f⁢(P)=d⁢(P⁢(n),P⁢(1))+∑i=1n−1d⁢(P⁢(i),P⁢(i+1)) 给出的总旅行成本最小化。这个问题在运筹学和物流学中非常重要，用于找到访问多个地点并返回起点的最有效路径，特别是在配送服务、维护操作和销售的路由规划中。

##### Graph Coloring Problem (Optimization Version, GCP)  
图着色问题（优化版本，GCP）

GCP-O refers to the problem of coloring vertices of a graph in such a way that no two adjacent vertices have the same color. Given an undirected graph G=(V,E), where V is the set of vertices and E is the set of edges, assign a color to each vertex such that no two adjacent vertices have the same color. Formally, let c:V→C be a function that assigns a color from a set of colors C to each vertex in V. The graph coloring problem can be formulated as finding a proper coloring, i.e., a function c such that for every edge (u,v)∈E, c⁢(u)≠c⁢(v). This problem is used in constraint satisfaction problems and applied in exam timetabling and register allocation in compilers [lintzmayer2011register](https://arxiv.org/html/2312.14890v4#bib.bib47).  
GCP-O 问题指的是对图的顶点进行着色，使得任意两个相邻顶点不具有相同颜色。给定一个无向图 G=(V,E) ，其中 V 是顶点集合， E 是边集合，为每个顶点分配一种颜色，使得任意两个相邻顶点颜色不同。形式化地，设 c:V→C 为一个函数，将颜色集合 C 中的颜色分配给 V 中的每个顶点。图着色问题可以表述为寻找一个合法着色，即一个函数 c ，使得对于每条边 (u,v)∈E ，满足 c⁢(u)≠c⁢(v) 。该问题用于约束满足问题，并应用于考试时间表安排和编译器中的寄存器分配 lintzmayer2011register。

##### Meeting Scheduling Problem (MSP)  
会议调度问题（MSP）

MSP deals with allocating time slots for meetings such that all constraints, including participant availability and room capacity, are satisfied without overlaps. Given a set of n participants and their availability for m time slots, find a schedule that maximizes the number of participants who can attend the meeting. Formally, let A=a1,a2,…,an be the set of participants and T=t1,t2,…,tm be the set of time slots. For each participant ai, let Si be a subset of T representing the times when ai is available and mi be a subset of meetings that are required to attend. The meeting scheduling problem can be formulated as finding a subset S⊆T such that |ai∈A|Si∩S≠∅| is maximized. In other words, the aim is to find a scheduling subset Si where the collective availability of participants intersects with Si, ensuring maximum participation. This problem is crucial in organizational management for scheduling meetings involving multiple participants with varying availability. It ensures optimal utilization of time and resources and is used in corporate scheduling systems and collaborative software [bofill2022constraint](https://arxiv.org/html/2312.14890v4#bib.bib48).  
MSP 处理会议时间分配问题，需满足所有约束条件，包括参与者可用性和会议室容量，且无时间冲突。给定一组 n 参与者及其在 m 个时间段内的可用性，需找到一种安排方案，使能参加会议的参与者数量最大化。形式化地，设 A=a1,a2,…,an 为参与者集合， T=t1,t2,…,tm 为时间段集合。对于每个参与者 ai ，令 Si 为 T 的子集，表示 ai 可用的时间段， mi 为必须参加的会议子集。会议调度问题可表述为寻找子集 S⊆T ，使得 |ai∈A|Si∩S≠∅| 最大化。换言之，目标是找到一个调度子集 Si ，其中参与者的集体可用性与 Si 相交，确保参与度最大化。该问题在组织管理中至关重要，用于调度涉及多个可用性不同的参与者的会议。它能确保时间和资源的最优利用，并应用于企业调度系统和协作软件中。

### 3.2Difficulty Level for Tasks  
3.2 任务难度等级

NPHardEval  
NPHardEval 将其提出的挑战按难度层级进行分类，从最简单到最复杂。该结构为每个任务划分了 10 个不同的难度等级，初始等级被设计为 LLM 可能面临的最基础挑战。这种分级方式能够细致评估 LLM 在日益复杂的任务谱系中的问题解决能力。例如，GCP-D 问题的难度等级为 1 至 10，对应的问题分别具有 6、8、10、12、14、16、18、20、22 和 24 条平均边数，以及 6、7、8、9、10、11、12、13、14 和 15 个节点。从具有 6 个节点和 6 条边的图开始，每个后续等级增加 2 条边和 1 个节点，最终在最挑战性等级达到具有 24 条边和 15 个节点的图。 categorizes the challenges it presents into a hierarchy of difficulty, spanning from the simplest to the most complex. This structure is divided into 10 distinct levels of difficulty for each task, with the initial level being designed as the most basic challenge that an LLM might face. This gradation allows for a nuanced assessment of an LLM’s problem-solving abilities across a spectrum of increasingly complex tasks. For instance, the GCP-D problem has difficulty levels 1 to 10 with questions of 6, 8, 10, 12, 14, 16, 18, 20, 22, and 24 average edges and 6, 7, 8, 9, 10, 11, 12, 13, 14, and 15 nodes. Beginning with graphs of 6 nodes and 6 edges, each subsequent level incorporates an additional 2 edges and 1 node, culminating in graphs of 24 edges and 15 nodes at the most challenging level.  
NPHardEval 将其提出的挑战按难度层级进行分类，从最简单到最复杂依次排列。该结构为每个任务划分了 10 个不同的难度等级，初始等级被设计为 LLM 可能面临的最基础挑战。这种分级方式能够细致评估 LLM 在日益复杂的任务谱系中的问题解决能力。以 GCP-D 问题为例，其难度等级 1 至 10 分别对应平均边数为 6、8、10、12、14、16、18、20、22、24 的图结构，以及节点数为 6、7、8、9、10、11、12、13、14、15。从 6 个节点和 6 条边的图开始，每个后续等级增加 2 条边和 1 个节点，最终在最难等级形成包含 24 条边和 15 个节点的图结构。

The difficulty level is not strictly bound to a linear scaling of difficulty; rather, it is designed to explore the nuances of performance degradation. By observing how LLMs cope with an escalating series of challenges, we aim to identify the inflection point where the performance notably diminishes. This approach provides a comprehensive understanding of where LLMs excel and where they falter, informing potential pathways for the enhancement of their reasoning capabilities.  
难度等级并非严格遵循线性递增的难度设定，而是旨在探究性能下降的细微差别。通过观察 LLMs 如何应对一系列逐步升级的挑战，我们的目标是找出性能显著下降的转折点。这种方法能够全面理解 LLMs 在哪些方面表现出色，在哪些方面存在不足，从而为提升其推理能力提供潜在的改进方向。

### 3.3Data Synthesis  3.3 数据合成

In the context of data synthesis for complex tasks, the approach can be categorized into two distinct methodologies, each corresponding to a different type of data structure: graph data (e.g., GCP) and linear data (e.g., MSP). The synthesis process in both cases is governed by a progression of complexity across a spectrum of predefined levels. This structured approach enables the creation of diverse datasets, suitable for evaluating and benchmarking LLMs’ reasoning ability. We provide examples of the synthesized data and how thay are used in prompts in Appendix [A](https://arxiv.org/html/2312.14890v4#A1 "Appendix A Examples of Synthesized Data, the Corresponding Prompts, and LLMs’ Outputs ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes").  
在复杂任务的数据合成背景下，该方法可分为两种不同的方法论，每种方法对应不同类型的数据结构：图数据（例如 GCP）和线性数据（例如 MSP）。在这两种情况下，合成过程都遵循一系列预定义难度级别的复杂性递进。这种结构化的方法能够创建多样化的数据集，适用于评估和基准测试 LLMs 的推理能力。我们在附录 A 中提供了合成数据的示例及其在提示词中的使用方式。

##### Graph Data Synthesis  图数据合成

The complexity in graph data synthesis escalates through a series of levels, each defined by a set of parameters that dictate the graph’s size and intricacy. These parameters typically include the number of vertices, the number of edges, and the range of edge weights. At lower levels, graphs are simpler with fewer vertices and edges, and a limited range of edge weights. As the level increases, the graphs become progressively more complex, featuring more vertices, a higher density of edges, and a wider variety of edge weights. The synthesis process is as follows:  
图数据合成的复杂性通过一系列层级逐步提升，每个层级由一组参数定义，这些参数决定了图的规模和复杂程度。这些参数通常包括顶点数量、边数量以及边权重的范围。在较低层级，图结构较为简单，顶点和边数量较少，边权重的范围也有限。随着层级的提高，图结构逐渐变得更加复杂，包含更多顶点、更高的边密度以及更多样化的边权重。合成过程如下：

- • 
    
    A generative function is employed to construct individual graph instances. This function adheres to the principles of graph theory, ensuring the creation of simple graphs without self-loops and duplicate edges, and respecting the parameters dictated by the current difficulty level.
    
      
    • 采用生成函数构建单个图实例。该函数遵循图论原理，确保生成无自环和重复边的简单图，并遵守当前难度级别所规定的参数。
- • 
    
    A batch synthesis function then iteratively employs the generative function to produce multiple graph instances across the spectrum of difficulty levels.
    
      
    • 随后，批量合成函数迭代使用生成函数，在多个难度级别范围内生成多个图实例。
- • 
    
    Finally, the synthesized graph instances are preserved in a tabulated format (in a CSV file), facilitating subsequent utilization and analysis.
    
      
    • 最后，合成的图实例以表格形式（存储在 CSV 文件中）保存，便于后续使用和分析。

##### Linear Data Synthesis  线性数据合成

In linear data synthesis, complexity is modulated by manipulating the length of the data array and the range of its constituent elements. Initial levels are characterized by shorter arrays with elements drawn from a narrow range. As the difficulty level ascends, the arrays lengthen, and the range of possible element values expands, thus introducing greater variability and complexity to the problem. The synthesis process is as follows:  
在线性数据合成中，复杂度通过调整数据数组的长度及其构成元素的范围来调节。初始级别以较短的数组为特征，数组元素取自一个狭窄的范围。随着难度级别的提升，数组长度增加，可能的元素值范围扩大，从而为问题引入更大的变异性和复杂性。合成过程如下：

- • 
    
    A linear data instance generation function is first utilized. This function produces sorted arrays of random numbers within a defined range, and selects a target number, ensuring its presence within the array to guarantee solvability.
    
      
    • 首先采用线性数据实例生成函数。该函数在指定范围内生成随机数的排序数组，并选定一个目标数字，确保该数字存在于数组中以保证问题可解。
- • 
    
    Multiple instances are generated through an iterative process, adhering to the difficulty levels outlined.
    
      
    • 通过迭代过程生成多个实例，严格遵循所设定的难度等级。
- • 
    
    These instances are then systematically recorded in a structured format (in a JSON file) for easy access and analysis.
    
      
    • 随后将这些实例以结构化格式（存储在 JSON 文件中）系统性地记录，以便于访问和分析。

## 4Experimental Setting  4 实验设置

This section presents the experiment setting to answer the three research questions. Our approach assessed 10 distinct LLMs, with a dichotomy between five proprietary (closed-source) models and five open-source models, including GPT 4 Turbo, Claude 2, GPT 3.5 Turbo, Claude Instant 1.2, PaLM 2, Vicuna-13b, Yi-34b, Mistral-7b, MPT-30b, and Phi-1.5.  
本节介绍了为回答三个研究问题而设计的实验设置。我们评估了 10 种不同的 LLMs，其中包括五种专有（闭源）模型和五种开源模型，具体涵盖 GPT 4 Turbo、Claude 2、GPT 3.5 Turbo、Claude Instant 1.2、PaLM 2、Vicuna-13b、Yi-34b、Mistral-7b、MPT-30b 和 Phi-1.5。

### 4.1Experiment 1: Model Performance Comparison  
4.1 实验一：模型性能比较

To evaluate the reasoning abilities of different LLMs through the NPHardEval benchmark, we employed a comparative experimental design. We use zero-shot prompts as the foundational measure of performance. These prompts comprise a task description and a specific question, presented without any preceding examples, to gauge the base capability of the model.  
为通过 NPHardEval 基准评估不同 LLMs 的推理能力，我们采用了对比实验设计。我们使用零样本提示作为性能的基础衡量标准。这些提示包含任务描述和具体问题，且不提供任何前置示例，以评估模型的基础能力。

The complexity of the problems presented to the models spanned from polynomial-time (P) to NP-complete and NP-hard levels. To ensure comprehensive coverage, we utilize the full set of 900 problems in NPHardEval, capturing the multifaceted nature of real-world challenges that typically exceed the capabilities of straightforward algorithmic approaches. Each model’s performance was evaluated based on two primary metrics: weighted accuracy and failure rate across the different complexity classes of problems, as we discussed in Section [4.4](https://arxiv.org/html/2312.14890v4#S4.SS4 "4.4 Evaluation Metrics ‣ 4 Experimental Setting ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes").  
模型所面临的问题复杂度从多项式时间（P）级别延伸至 NP 完全和 NP 难级别。为确保全面覆盖，我们利用了 NPHardEval 中的全部 900 个问题，以捕捉现实世界挑战的多面性，这些挑战通常超出了简单算法方法的能力范围。如第 4.4 节所述，每个模型的性能基于两个主要指标进行评估：加权准确率以及在不同复杂度类别问题上的失败率。

To evaluate across task complexity, specifically comparing the complexity among P, NP-Complete, and NP-Hard pairs, we initially pinned the data based on complexity levels. Subsequently, we applied the Wilcoxon test to each pair of complexity sets. Wilcoxon is a non-parametric statistical hypothesis test that allows us to compare two populations with matched samples. To evaluate problem difficulty, aiming to discern differences among problems within the complexity category, we pinned the data based on the specific problems and then used the Wilcoxon test to compare pairs of different problem sets.  
为评估任务复杂度，特别是比较 P 类、NP 完全类和 NP 难类问题对之间的复杂度差异，我们首先根据复杂度等级对数据进行固定。随后，我们对每对复杂度集合应用了威尔科克森检验。威尔科克森检验是一种非参数统计假设检验方法，使我们能够比较两个具有匹配样本的总体。为评估问题难度，旨在识别同一复杂度类别内不同问题之间的差异，我们基于具体问题对数据进行固定，然后使用威尔科克森检验来比较不同问题集合对。

### 4.2Experiment 2: Benchmark Robustness  
4.2 实验二：基准测试的稳健性

The primary objective of this experiment is to ascertain whether it is possible to “hack” our benchmark by finetuning models on its previous versions. To simulate this, we constructed five versions of the benchmark, maintaining a consistent difficulty level. Additionally, we utilize two distinct versions of the benchmark, each varying in difficulty, to evaluate the potential for hacking under varying conditions. To replicate the progression of time, models were finetuned sequentially on one to five benchmarks, each finetuned checkpoint is tested on the two distinct benchmarks for evaluation.  
本实验的主要目的是探究是否可能通过针对先前版本的基准测试进行模型微调来“破解”我们的基准。为模拟这一情况，我们构建了五个版本的基准测试，并保持一致的难度水平。此外，我们使用了两个不同版本的基准测试，每个版本的难度各异，以评估在不同条件下被破解的可能性。为模拟时间推移的过程，模型依次在一个至五个基准测试上进行微调，每个微调后的检查点均在两个不同的基准测试上进行评估。

The experiment involved finetuning three high-performing open-source models: Phi-2, Mistral-7b, and Qwen-14b. Due to constraints in computing resources, the Yi-34b model was not included in the finetuning process. For the finetuning process, we employed the QLoRA technique, applying specific hyperparameters: batch size set to 8, a single epoch, a warmup proportion of 0.03, a learning rate of 1e-4, lora_r at 64, lora_alpha at 16, and a lora_dropout of 0.1. This approach aims to rigorously test the robustness of our benchmark against potential overfitting strategies.  
实验涉及对三个高性能开源模型进行微调：Phi-2、Mistral-7b 和 Qwen-14b。由于计算资源限制，Yi-34b 模型未纳入微调过程。在微调过程中，我们采用了 QLoRA 技术，并设置了特定的超参数：批处理大小为 8，单轮训练周期，预热比例为 0.03，学习率为 1e-4，lora_r 设为 64，lora_alpha 设为 16，lora_dropout 设为 0.1。此方法旨在严格测试我们基准测试对潜在过拟合策略的鲁棒性。

### 4.3Experiment 3: Comparative Analysis of Learnability by In-context Learning  
4.3 实验三：基于上下文学习可习得性的比较分析

A prevalent approach in current few-shot learning involves using examples that bear similarity to the test question. However, this raises a question about the extent to which the model is replicating the problem-solving process from the examples as opposed to genuinely acquiring reasoning skills. Consequently, it becomes pertinent to investigate whether the problem-solving abilities developed through example-based learning are generalizable.  
当前少样本学习的一种普遍方法是使用与测试问题相似的示例。然而，这引发了一个问题：模型在多大程度上是在复制示例中的解题过程，而非真正习得推理能力。因此，探究通过基于示例的学习所培养的解题能力是否具有普适性变得尤为重要。

To delve deeper into the models’ in-context learning abilities, we utilize various few-shot in-context learning prompts to discern whether the model is “learning” from the few-shot examples or merely “mimicking” the behavior. In our benchmark, since we distinctly classify the difficulty level of each question, it allows for the use of questions from the same task but with varying difficulty levels as few-shot examples. The crux of this analysis lies in varying the difficulty levels of examples within the prompts. Since the fundamental algorithmic skill required to solve a question remains constant across varying difficulty levels under the same task, a model that truly learns this skill should show consistent performance irrespective of the example difficulty in the prompt. We propose the following hypotheses about the relationship between in-context learning ability and the difference of difficulty level between the given examples and the question being asked in context:  
为了深入探究模型在上下文中的学习能力，我们采用了多种少样本上下文学习提示，以辨别模型是从少样本示例中“学习”还是仅仅“模仿”其行为。在我们的基准测试中，由于我们明确划分了每个问题的难度等级，因此可以使用同一任务中不同难度级别的问题作为少样本示例。这一分析的关键在于改变提示中示例的难度级别。由于在同一任务下，解决一个问题所需的基本算法技能在不同难度级别中保持不变，真正掌握该技能的模型应表现出稳定的性能，而不受提示中示例难度的影响。我们提出以下关于上下文学习能力与给定示例和所提问题之间难度差异关系的假设：

- • 
    
    Models possessing optimal generalization capabilities should demonstrate consistent performance improvement regardless of the difficulty level of the prompt examples in context. This assumption is based on the premise that models with robust learning abilities are capable of discerning and applying the intrinsic problem-solving skills learned in the examples. Given that questions within the same task fundamentally require similar skills, variations in difficulty are unlikely to significantly affect the model’s performance.
    
      
    • 具备最优泛化能力的模型，无论上下文提示示例的难度如何，都应展现出持续的性能提升。这一假设基于一个前提：拥有强大学习能力的模型能够识别并应用从示例中学到的内在问题解决技能。鉴于同一任务中的问题本质上需要相似的技能，难度变化不太可能显著影响模型的表现。
- • 
    
    If a model exhibits the ability to generalize only from some types of examples but is unable to extend this learning to others, it reveals a deficiency in its capacity for generalization in terms of reasoning. This suggests that the model is not genuinely acquiring problem-solving skills from the examples but merely recognizing and applying patterns from examples that are of equal or greater complexity to the problem at hand.
    
      
    • 如果模型仅能从某些类型的示例中展现泛化能力，却无法将这种学习扩展到其他类型，这表明其在推理方面的泛化能力存在不足。这意味着模型并非真正从示例中习得问题解决技能，而仅仅是识别并应用那些与当前问题复杂度相当或更高的示例中的模式。
- • 
    
    If a model is unable to generalize from either more difficult or easier examples and is restricted to examples of the same difficulty level, it strongly suggests that the model is merely replicating the process presented in the context rather than internalizing any fundamental problem-solving techniques or pattern recognition embedded within the examples. This behavior indicates a profound deficiency in the model’s ability to comprehend and understand the underlying principles. It points to an absence of transferable, logic-learning skills, reflecting a superficial form of learning that is limited to surface-level imitation rather than a deeper, conceptual grasp.
    
      
    • 如果模型既无法从更困难也无法从更简单的示例中泛化，且仅限于相同难度级别的示例，这强烈表明模型只是在复制上下文呈现的过程，而非内化示例中蕴含的任何基本问题解决技巧或模式识别能力。这种行为表明模型在理解和把握底层原理方面存在严重缺陷，意味着缺乏可迁移的逻辑学习技能，反映出一种肤浅的学习形式，仅限于表面模仿而非更深层次的概念性掌握。

We categorize the few-shot prompts into three types:  
我们将少样本提示分为三种类型：

- • 
    
    Few-shot prompts with examples of the same difficulty level: Here, the model is provided with five examples in the prompt, all of which are at the same difficulty level and distinct from the question being asked.
    
      
    • 包含同等难度示例的少样本提示：在此设置中，模型会在提示中获得五个示例，这些示例均与所提问题处于相同难度级别且内容互不相同。
- • 
    
    Few-shot prompts with examples that are easier than the question: This set comprises five variations of prompts, each with examples that are 1, 2, 3, 4, and 5 levels easier than the question, respectively.
    
      
    • 包含比问题更简单示例的少样本提示：此组包含五种不同的提示变体，每种变体中的示例分别比问题简单 1、2、3、4 和 5 个难度等级。
- • 
    
    Few-shot prompts with examples that are more challenging than the question: Similarly, we prepare five sets of prompts, each containing examples that are 1, 2, 3, 4, and 5 levels more difficult than the question, offering a gradient of increased challenge.
    
      
    • 包含比问题更具挑战性示例的少样本提示：同样地，我们准备了五组提示，每组包含的示例分别比问题困难 1、2、3、4 和 5 个难度等级，形成逐级递增的挑战梯度。

Through this diverse array of prompts, we aim to provide a nuanced understanding of the LLMs’ ability to learn from examples, thereby offering valuable insights into their underlying learning capabilities.  
通过这种多样化的提示设计，我们旨在细致探究 LLMs 从示例中学习的能力，从而为理解其内在学习机制提供有价值的见解。

### 4.4Evaluation Metrics  4.4 评估指标

To evaluate the reasoning ability of LLMs, we utilize two metrics, the Weighted Accuracy and the Failure Rate, to comprehensively quantify the correctness of LLMs’ reasoning outputs.  
为评估 LLMs 的推理能力，我们采用加权准确率与失败率两项指标，全面量化 LLMs 推理输出的正确性。

##### Weighted Accuracy (WA)  加权准确率（WA）

is calculated for each problem either through the comparison with the correct answer or through step-by-step results checking, for those problems without the only answer. To better represent the comparative accuracy, we assign weights to different difficulty levels so that each level has a weight corresponding to its relative importance or challenge. Higher difficulty levels are given more weight in a linear manner (e.g., level 1 has weight 1, level 2 has weight 2, etc.). The Weighted Accuracy is formally defined as:  
通过比对标准答案或逐步结果验证（针对无唯一解的问题）进行计算。为更准确反映相对正确率，我们为不同难度层级分配权重，使每个层级的权重与其相对重要性或挑战性相匹配。更高难度层级以线性方式获得更大权重（例如：难度 1 级权重为 1，2 级权重为 2，依此类推）。加权准确率的正式定义为：

|   |   |   |
|---|---|---|
||W⁢A=∑i=110(wi×Ai)∑i=110wi||

where wi represents the weight assigned to difficulty level i, from 1 to 10, and Ai is the accuracy at that level.  
其中 wi 代表分配给难度等级 i 的权重，范围从 1 到 10，而 Ai 是该难度等级下的准确率。

##### Failure Rate (FR)  失败率（FR）

is a measure used to assess the frequency of unsuccessful outcomes across the different problems and difficulty levels. It is particularly useful for identifying cases where an LLM’s result does not comply with the expected output format. The Failure Rate is calculated by considering the proportion of failed attempts relative to the total number of attempts for each difficulty level. An attempt is defined as failed if the model generates results that cannot be successfully parsed in all endpoint calls, and we set the maximum times of try as 10. For each problem, the Failure Rate is then aggregated across all difficulty levels, taking into account the total 10 attempts at each level. The formal definition of Failure Rate is given by:  
是一种用于评估不同问题和难度等级下失败结果发生频率的度量指标。它特别适用于识别 LLM 输出结果不符合预期格式的情况。失败率的计算基于每个难度等级下失败尝试次数占总尝试次数的比例。若模型在所有端点调用中生成的结果均无法成功解析，则该次尝试被判定为失败，我们设定最大尝试次数为 10。对于每个问题，失败率将汇总所有难度等级的数据，并考虑每个难度等级下的总计 10 次尝试。失败率的正式定义如下：

|   |   |   |
|---|---|---|
||F⁢R=∑i=110Fi100||

where Fi denotes the number of failed attempts at difficulty level i.  
其中 Fi 表示在难度等级 i 上的失败尝试次数。

## 5Results  5 结果

### 5.1Reasoning Ability of Foundation Models  
5.1 基础模型的推理能力

Experiment 1 focuses on a comprehensive comparison among various foundation models and across complexity classes and difficulty levels. In Figure [2](https://arxiv.org/html/2312.14890v4#S5.F2 "Figure 2 ‣ 5.1 Reasoning Ability of Foundation Models ‣ 5 Results ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes"), we present the overall zero-shot accuracy for each problem, providing a visual representation of the performance of different models.  
实验 1 重点比较了各类基础模型在不同复杂度类别和难度级别上的表现。图 2 展示了每个问题的整体零样本准确率，直观呈现了不同模型的性能表现。

![Refer to caption](https://arxiv.org/html/2312.14890v4/extracted/5404715/Fig/zeroshot_heatmap.png)

Figure 2:Zero-shot model performance on the nine tasks from P to NP-Complete bottom-up.  
图 2：从 P 类到 NP 完全类自底向上的九项任务中，零样本模型的表现。

Our observations reveal that closed-source models generally demonstrate higher accuracy and a lower rate of failure compared to their open-source counterparts. Notably, GPT-4 Turbo often emerges as the frontrunner in performance across the majority of tasks, indicating its superior problem-solving capabilities, while Claude 2, on the other hand, often performs the best on medium-level (NP-complete) complexity in zero-shot settings.  
我们的观察显示，闭源模型通常比开源模型展现出更高的准确率和更低的失败率。值得注意的是，GPT-4 Turbo 在大多数任务中常常表现领先，这表明其卓越的问题解决能力；而 Claude 2 则在零样本设置下，往往在中等复杂度（NP 完全）问题上表现最佳。

Within the realm of open-source models, Yi-34b, Qwen-14b, and Mistral-7b distinguish themselves by significantly outperforming other models in this category. We observe a disparity between the performance of these three models and other open-source options, highlighting a notable performance gap and suggesting that these models possess more advanced reasoning abilitie.  
在开源模型领域，Yi-34b、Qwen-14b 和 Mistral-7b 表现突出，显著超越了同类其他模型。我们观察到这三款模型与其他开源选项之间存在性能差异，突显了显著的性能差距，并表明这些模型具备更高级的推理能力。

In particular, we use the weighted accuracy and the failure rate metrics to further quantify different models’ performance. The trends observed below in both weighted accuracy and failure rates point to a nuanced understanding of the capabilities and limitations of current LLMs. We also utilize performance comparison tests within and across complexity classes, to further explore the model performance differences among complexity classes.  
具体而言，我们采用加权准确率和失败率指标来进一步量化不同模型的性能表现。下文在加权准确率和失败率两方面观察到的趋势，有助于我们细致理解当前 LLMs 的能力与局限。我们还利用复杂度类别内部及跨类别的性能对比测试，进一步探究不同复杂度类别间的模型性能差异。

##### Weighted Accuracy  加权准确率

As Figure [3](https://arxiv.org/html/2312.14890v4#S5.F3 "Figure 3 ‣ Weighted Accuracy ‣ 5.1 Reasoning Ability of Foundation Models ‣ 5 Results ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes")(a) shows, upon analysis of the weighted accuracy for different models across problem complexities, we observed a general trend where all models experienced a decrease in accuracy as problem complexity increased. Notably, there are two detailed findings for overall reasoning ability change. First, regarding the performance decay speed, among the 12 models we tested, the average performance demonstrated a higher accuracy at the P and NP-Complete complexity levels (with similar weighted accuracies of 0.24 and 0.25) but saw a sharper decline as the problems became more complex when proceeding to the NP-hard level (with a weighted accuracy of 0.02). There is a performance decay on average when models are tested against NP-Hard problems. Second, close-source models usually perform better than open-source models – there are more triangles in the upper locations than squares in Figure [3](https://arxiv.org/html/2312.14890v4#S5.F3 "Figure 3 ‣ Weighted Accuracy ‣ 5.1 Reasoning Ability of Foundation Models ‣ 5 Results ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes")(a).  
如图 3(a)所示，通过对不同模型在各类问题复杂度下的加权准确率进行分析，我们观察到一个普遍趋势：随着问题复杂度的增加，所有模型的准确率均呈现下降态势。值得注意的是，关于整体推理能力的变化，我们发现了两个具体现象。首先，在性能衰减速度方面，在我们测试的 12 个模型中，平均表现在 P 类和 NP 完全复杂度层级上保持了较高的准确率（加权准确率分别为 0.24 和 0.25 且数值相近），但当问题复杂度提升至 NP 难解层级时，模型性能出现急剧下滑（加权准确率降至 0.02）。面对 NP 难解问题时，模型普遍存在性能衰减现象。其次，闭源模型通常表现优于开源模型——图 3(a)中位于图表上部的三角形标记数量明显多于方形标记。

![Refer to caption](https://arxiv.org/html/2312.14890v4/extracted/5404715/Fig/weighted_accuracy_failed.png)

Figure 3:Model performance on different complexity problems: (a) weighted accuracy (b) (weighted) failure rate. Open models are denoted in squares and close models are denoted in triangles. Trends of metrics are demonstrated for models with outstanding performances in both weighted accuracy and failure rate, including both close-source (GPT 4 Turbo and Claude 2) and open-source (Mistral-7B and Phi-2) models.  
图 3：不同复杂度问题上的模型性能：(a) 加权准确率 (b) (加权) 失败率。开放模型用正方形表示，闭源模型用三角形表示。图中展示了在加权准确率和失败率两方面均表现突出的模型指标趋势，包括闭源模型（GPT 4 Turbo 和 Claude 2）和开源模型（Mistral-7B 和 Phi-2）。

##### Failure Rate  失败率

As Figure [3](https://arxiv.org/html/2312.14890v4#S5.F3 "Figure 3 ‣ Weighted Accuracy ‣ 5.1 Reasoning Ability of Foundation Models ‣ 5 Results ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes")(b) indicates, the failure rates mirrored the trends observed in weighted accuracy but in reverse. On average, the models showed an increase in failure rates corresponding to the complexity of the problems. Similar to the weighted accuracy, open-source models fail more often (with more squares on the top) than the close-source models (with more triangles on the bottom), indicating close-source’s models advanced ability in following the prompt to understand the reasoning problems and generate answers with correct format.  
如图 3(b)所示，失败率呈现出与加权准确率相反的趋势。平均而言，模型失败率的上升与问题复杂度呈正相关。与加权准确率类似，开源模型（顶部更多方块标识）比闭源模型（底部更多三角标识）更容易失败，这表明闭源模型在遵循提示理解推理问题并生成正确格式答案方面具备更先进的能力。

#### 5.1.1Performance across Task Complexity and Difficulty Levels  
5.1.1 不同任务复杂度与难度级别的表现

Figure [4](https://arxiv.org/html/2312.14890v4#S5.F4 "Figure 4 ‣ 5.1.1 Performance across Task Complexity and Difficulty Levels ‣ 5.1 Reasoning Ability of Foundation Models ‣ 5 Results ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes") shows the accuracy of each model across different complexity levels. The test results reveal statistical significance (p<0.05) in the p-values between P and NP-Hard, as well as NP-Complete and NP-Hard. These findings indicate that our investigated LLMs performed significantly worse when confronted with NP-Hard problems compared to P and NP-Complete problems.  
图 4 展示了各模型在不同复杂度级别上的准确率。测试结果显示 P 类与 NP-Hard 类问题之间，以及 NP-Complete 类与 NP-Hard 类问题之间的 p 值具有统计学显著性（ p<0.05 ）。这些发现表明，相较于 P 类和 NP-Complete 类问题，我们所研究的 LLMs 在处理 NP-Hard 类问题时表现显著更差。

![Refer to caption](https://arxiv.org/html/2312.14890v4/extracted/5404715/Fig/Complexity.png)

Figure 4:Models’ performance on each complexity level. (a) GPT 4 Turbo. (b) Claude 2. (c) GPT 3.5 Turbo. (d) Claude Instant 1.2. (e) PaLM 2. (f) Yi-34b. (g) Qwen-14b. (h) Mistral-7b. (i) Phi-2. (j) MPT-30b. (k) Vicuna-13b. (l) Phi-1.5.  
图 4：各模型在不同复杂度等级上的表现。(a) GPT 4 Turbo。(b) Claude 2。(c) GPT 3.5 Turbo。(d) Claude Instant 1.2。(e) PaLM 2。(f) Yi-34b。(g) Qwen-14b。(h) Mistral-7b。(i) Phi-2。(j) MPT-30b。(k) Vicuna-13b。(l) Phi-1.5。

![Refer to caption](https://arxiv.org/html/2312.14890v4/extracted/5404715/Fig/Problem.png)

Figure 5:Models’ performance on tasks across complexity levels. (a) GPT 4 Turbo. (b) Claude 2. (c) GPT 3.5 Turbo. (d) Claude Instant 1.2. (e) PaLM 2. (f) Yi-34b. (g) Qwen-14b. (h) Mistral-7b. (i) Phi-2. (j) MPT-30b. (k) Vicuna-13b. (l) Phi-1.5.  
图 5：各模型在不同复杂度任务上的表现。(a) GPT 4 Turbo。(b) Claude 2。(c) GPT 3.5 Turbo。(d) Claude Instant 1.2。(e) PaLM 2。(f) Yi-34b。(g) Qwen-14b。(h) Mistral-7b。(i) Phi-2。(j) MPT-30b。(k) Vicuna-13b。(l) Phi-1.5。

Figure [6](https://arxiv.org/html/2312.14890v4#S5.F6 "Figure 6 ‣ 5.2 Evaluating Benchmark Robustness ‣ 5 Results ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes") presents the accuracy of each model across various problems associated with P, NP-Complete, and NP-Hard complexities. Regarding P complexity, notable differences emerged among the models. GPT 3.5 Turbo, GPT 4 Turbo, Yi-34b, and Qwen-14b models exhibited significantly superior performance on the SAS problem compared to the other two problems. GPT 3.5 Turbo, Yi-34b, and Vicuna-13b models demonstrated markedly better performance on the EDP problem compared to the SPP problem. Only the Vicuna-13b model displayed slightly better performance, although not significant, on the EDP problem compared to SAS across all investigated models.  
图 6 展示了各模型在 P、NP 完全和 NP 难复杂度相关各类问题上的准确率表现。在 P 复杂度问题上，各模型间呈现出显著差异。GPT 3.5 Turbo、GPT 4 Turbo、Yi-34b 和 Qwen-14b 模型在 SAS 问题上的表现明显优于另外两类问题。GPT 3.5 Turbo、Yi-34b 和 Vicuna-13b 模型在 EDP 问题上的表现显著优于 SPP 问题。在所有被研究的模型中，仅有 Vicuna-13b 模型在 EDP 问题上相较于 SAS 问题表现出略微优势，但该差异并不显著。

Other observations include: GPT 4 Turbo showcased very similar performance between the EDP and SPP problems, while Claude Instant 1.2 exhibited similar performance for all these three problems. Yi-34b, Owen-14b, GPT 3.5 Turbo, and GPT 4 Turbo displayed remarkably high accuracy specifically for the SAS task. MPT-30b and Phi-1.5 showed very limited performance in identifying these three problems.  
其他观察包括：GPT 4 Turbo 在 EDP 和 SPP 问题上表现出非常相似的性能，而 Claude Instant 1.2 在这三个问题上均展现出相近的表现。Yi-34b、Owen-14b、GPT 3.5 Turbo 和 GPT 4 Turbo 在 SAS 任务上表现出极高的准确率。MPT-30b 和 Phi-1.5 在识别这三个问题上的表现则非常有限。

Regarding NP-Complete complexity, there are several observations to highlight. Still, neither MPT-30b nor Phi-1.5 could deliver any identification for problems in the NP-Complete complexity. In the case of GCP-D and TSP-D problems, the performance of these models varied significantly. Phi-2, Vicuna-13b and GPT 4 Turbo outperformed in the GCP-D problem compared to TSP-D, whereas Claude Instant 1.2, Claude 2, and PaLM 2 exhibited better performance in TSP-D over GCP-D. On the other hand, models like Mistral-7b, Yi-34b, Qwen-14b, and GPT 3.5 Turbo showcased relatively similar performance between these two tasks. For the KSP task, only GPT 4 Turbo demonstrated promising performance, while the remaining models faltered.  
关于 NP 完全复杂度，有几个观察值得强调。然而，无论是 MPT-30b 还是 Phi-1.5，都无法对 NP 完全复杂度问题提供任何识别。在 GCP-D 和 TSP-D 问题上，这些模型的表现差异显著。与 TSP-D 相比，Phi-2、Vicuna-13b 和 GPT 4 Turbo 在 GCP-D 问题上表现更优；而 Claude Instant 1.2、Claude 2 和 PaLM 2 则在 TSP-D 问题上表现优于 GCP-D。另一方面，Mistral-7b、Yi-34b、Qwen-14b 和 GPT 3.5 Turbo 等模型在这两项任务中表现相对接近。对于 KSP 任务，只有 GPT 4 Turbo 展现出有前景的性能，其余模型则表现不佳。

Considering NP-Hard complexity as the most intricate task set among the three (as evidenced in Figure [4](https://arxiv.org/html/2312.14890v4#S5.F4 "Figure 4 ‣ 5.1.1 Performance across Task Complexity and Difficulty Levels ‣ 5.1 Reasoning Ability of Foundation Models ‣ 5 Results ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes")), many of the examined models encountered challenges in identifying tasks within this complexity. For the GCP task, Mistral-7b, PaLM 2, GPT 3.5 Turbo, and GPT 4 Turbo exhibited some potential, while Vicuna-13b and Claude Instant 1.2 showed limited performance. For the TSP task, identification was observed only in Claude 2 and GPT 4 Turbo. Of all the investigated models, GPT 4 Turbo exhibited promise in identifying these three tasks within the NP-Hard complexity. However, the performance in GCP and TSP identification significantly surpassed that of the MSP task across these models. For the MSP task, only GPT 4 Turbo displayed some ability for identification, while with notably low accuracy.  
考虑到 NP-Hard 复杂度是三者中最为复杂的任务集（如图 4 所示），许多被考察的模型在识别此类复杂度的任务时遇到了挑战。在图着色问题（GCP）任务中，Mistral-7b、PaLM 2、GPT 3.5 Turbo 和 GPT 4 Turbo 展现出一定潜力，而 Vicuna-13b 和 Claude Instant 1.2 的表现则较为有限。在旅行商问题（TSP）任务中，仅 Claude 2 和 GPT 4 Turbo 展现出识别能力。在所有被研究的模型中，GPT 4 Turbo 在识别 NP-Hard 复杂度下的这三类任务时显示出潜力。然而，这些模型在 GCP 和 TSP 识别上的表现显著优于最大子数组问题（MSP）任务。对于 MSP 任务，仅 GPT 4 Turbo 展现出一定的识别能力，但准确率明显偏低。

### 5.2Evaluating Benchmark Robustness  
5.2 基准测试稳健性评估

![Refer to caption](https://arxiv.org/html/2312.14890v4/extracted/5404715/Fig/rq3_weighted_accuracy.png)

Figure 6:Model’s robustness on different problems and difficulty levels.  
图 6：模型在不同问题和难度级别上的鲁棒性。

In Experiment 2, we explore the robustness of benchmark against hacking attempts through a process of finetuning on pairs of question and gold answer. We experiment using 3 well-performing open-source models: Qwen-14b, Mistral-7b, and Phi-2 on two versions of benchmarks. Figure [6](https://arxiv.org/html/2312.14890v4#S5.F6 "Figure 6 ‣ 5.2 Evaluating Benchmark Robustness ‣ 5 Results ‣ NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes") presents the result22We do not present the result on MSP as this problem does not have a fixed solution and we do not conduct finetuning on it.  
我们未展示 MSP 问题的结果，因为该问题没有固定解，且我们未对其进行微调。  
在实验二中，我们通过微调问题与标准答案配对的方式，探究基准测试对破解尝试的鲁棒性。我们使用三个性能优异的开源模型——Qwen-14b、Mistral-7b 和 Phi-2，在两个版本的基准测试上进行了实验。图 6 展示了结果 2: each problem has two graph with one displaying evaluation results at difficulty levels 1-10 and one displaying evaluation results at difficulty levels 11-20. In each graph, the first row of indicate the accuracy mean of each model, averaged over outcomes at 5 finetuning checkpoints, ranging from tuning using zero (no finetuning) to five distinct benchmarks.  
：每个问题包含两张图表，一张展示难度级别 1-10 的评估结果，另一张展示难度级别 11-20 的评估结果。在每张图表中，第一行表示每个模型的平均准确率，该数值是在 5 个微调检查点（从零微调到使用五个不同基准测试进行微调）的结果上取平均得出的。

  
我们的发现具有双重性：(1) 尽管微调在解决多项式时间问题上带来了改进，但其对更复杂的 NP 完全和 NP 难问题的影响却是负面的。这表明，通过基础的问答式微调来破解 NP 完全问题（可能还包括 NP 难问题）具有内在的困难性。手动标注思维链（这在基准测试中并未提供）可能提升效果，尽管标注本身存在挑战。(2) 微调似乎有利于在同一难度级别（所有 P 问题）内的表现，但显示出有限的分布外适应性，并且除了 SAS 之外，难以泛化到更困难的问题（如图 a 和图 c 所示）。例如，Qwen-14b 在微调后对 1-10 级的 SPP 挑战表现出显著的能力；其性能与 GPT-4 相当。然而，在 11-20 级的 SPP 问题上，其性能显著下降，甚至不及未微调的检查点。 这表明在这些基准测试上进行微调只能对非常简单的题目（如 SAS）有益，但可能会损害泛化能力，并使微调技巧变得无效。Our findings are twofold: (1) While finetuning yields improvements in solving polynomial-time problems, its impact on the more complex NP-complete and NP-hard problems are negative. This suggests the inherent difficulty of hacking NP-complete, and potentially NP-hard, problems through the basic finetuning with question-and-answer approach. Manual annotation of the chain-of-thought, which is not provided in the benchmarks, could potentially enhance effectiveness, albeit with challenges in annotation. (2) Finetuning appears beneficial for performance within the same difficulty level all P problems, yet shows limited out-of-distribution (OOD) adaptability and struggles to generalize to more difficult problems (as evidenced in graphs a and c) except SAS. For instance, Qwen-14b demonstrates notable proficiency on SPP challenges at levels 1-10 following finetuning; its performance is comparable to that of GPT-4. However, its performance significantly diminishes on SPP problems at levels 11-20, even underperforming compared to its unfinetuned checkpoint. This indicates that finetuning on these benchmarks can only benefit very simple questions such as SAS but could potentially impede generalization capabilities and renders finetuning hacking useless.  
我们的发现具有双重性：（1）尽管微调在解决多项式时间问题上带来了改进，但其对更复杂的 NP 完全和 NP 难问题的影响却是负面的。这表明，通过基础的问答式微调来破解 NP 完全问题（可能还包括 NP 难问题）存在固有的困难。虽然基准测试中未提供思维链的人工标注，但手动标注可能提升效果，尽管标注本身面临挑战。（2）微调似乎对同一难度级别内的所有 P 问题性能有益，但在分布外（OOD）适应性方面表现有限，且难以泛化到更困难的问题（如图 a 和 c 所示，SAS 除外）。例如，Qwen-14b 在微调后对 1-10 级的 SPP 挑战表现出显著熟练度；其性能与 GPT-4 相当。然而，在 11-20 级的 SPP 问题上，其性能显著下降，甚至不及未微调的检查点。 这表明在这些基准测试上进行微调只能对非常简单的题目（如 SAS）有益，但可能会损害泛化能力，并使微调技巧变得无效。

  
总而言之，我们的基准测试之所以难以被破解，主要基于两个因素：(1) NP 完全和 NP 难问题的固有复杂性，仅从问答对中学习这些问题是困难的；(2) P 问题在微调这些问答对时容易过拟合，而通过提高问题难度，真正的“推理”能力可以轻易暴露出来。基于这些结论，我们计划定期策略性地更新我们的基准测试，调整不同难度级别，以最大限度地减少被破解的可能性。In conclusion, our benchmark is challenging to hack due to two primary factors: (1) the inherent complexity of NP-complete and NP-hard problems, which are difficult to learn solely from question-answer pairs, and (2) the propensity for P problems to become overfitted through finetuning on these pairs, while the real “reasoning” ability can be easily exposed by increasing the problem difficulty level. Based on these conclusions, we intend to periodically update our benchmarks strategetically with varying difficulty levels to minimize the potential for hacking.  
总而言之，我们的基准测试难以被破解，主要基于两个因素：(1) NP 完全和 NP 难问题的固有复杂性，仅从问答对中学习这些问题是困难的；(2) P 问题在微调这些问答对时容易过拟合，而通过提高问题难度水平，真正的“推理”能力可以轻易暴露出来。基于这些结论，我们计划定期策略性地更新我们的基准测试，调整不同难度水平，以最小化被破解的可能性。

### 5.3  
5.3 少样本示例难度对推理能力提升的影响Effects of Few-shot Examples’ Difficulty on Reasoning Ability Enhancement  
5.3 少样本示例难度对推理能力提升的影响

  
在实验 3 中，我们聚焦于 SAS 和 EDP 任务，以探究 LLMs 上下文学习能力的本质。该实验从经验上区分了 LLMs 在上下文学习场景中表现出的“学习”与“模仿”行为。我们的发现还揭示了闭源模型与开源模型在从示例中学习和泛化的方法上存在明显的二分法。In Experiment 3, we focused on the tasks of SAS and EDP to investigate the nature of the in-context learning capabilities of LLMs. This experiment empirically distinguishes between “learning” and “mimicking” as exhibited by LLMs during in-context learning scenarios. Our findings also revealed a clear dichotomy in the approach to learning and generalization from examples between closed-source and open-source models.  
在实验三中，我们聚焦于 SAS 和 EDP 任务，以探究 LLMs 在上下文学习中所展现能力的本质。该实验从经验层面区分了 LLMs 在上下文学习场景中表现出的“学习”与“模仿”行为。我们的发现还揭示了闭源模型与开源模型在从示例中学习和泛化的方法上存在明显的二分性。

For closed-source models, including GPT 4 Turbo, Claude 2, GPT 3.5 Turbo, PaLM 2, and Claude Instant 1.2, the results were notably close to the ideal scenario. We observed minimal variation in performance across different levels of difficulty in the examples provided. This consistency suggests that these models are not merely mimicking the solutions but are indeed learning the algorithmic skills presented in the context of the examples.  
对于闭源模型，包括 GPT 4 Turbo、Claude 2、GPT 3.5 Turbo、PaLM 2 和 Claude Instant 1.2，其结果与理想情况非常接近。我们观察到，在所提供的示例中，不同难度级别的性能变化极小。这种一致性表明，这些模型并非仅仅模仿解决方案，而是确实在示例的上下文中学习了算法技能。

  
相比之下，开源模型的表现，尤其是 Yi-34b 和 Mistral-7b，呈现出一种清晰的模式：这些模型通常能从比给定问题更具挑战性的示例中较好地泛化，但在处理更简单的示例时却显得力不从心。其他开源模型虽未展现出如此鲜明的模式，但一个显著趋势依然明显：这些模型在一定程度上能够从较难问题向较简单问题泛化，但在从简单问题向复杂问题泛化时则表现欠佳。在 EDP 任务中，Phi-1.5 模型是个例外，它在某些难度级别上似乎从简单示例中泛化的效果优于从困难示例中泛化。然而，总体而言，没有任何开源模型能够持续地从更难和更易的示例中同时学习。难度级别显著影响了模型的性能，这表明这些模型更倾向于模仿模式，而非真正从上下文中进行学习。In contrast, the performance of open-source models, particularly Yi-34b and Mistral-7b, exhibits a clear pattern where the models generally generalize well from examples that are more challenging than the given question, yet they struggle to do so from simpler examples. Other open-source models display less distinct patterns, but a notable trend is still evident: these models demonstrate some capacity to generalize from more challenging to simpler questions, but they are less successful in generalizing from simpler to more complex questions. An exception is observed with the Phi-1.5 model in EDP, where it appears to generalize better from easier examples than from harder examples at certain difficulty levels. However, broadly speaking, none of the open-source models consistently learn from both harder and easier examples. The difficulty level significantly influences the models’ performance, suggesting a tendency for these models to mimic patterns rather than engage in genuine learning from the context.  
相比之下，开源模型的表现，尤其是 Yi-34b 和 Mistral-7b，呈现出一种清晰的模式：这些模型通常能够从比给定问题更具挑战性的示例中较好地泛化，但在从更简单的示例中泛化时却显得力不从心。其他开源模型展现的模式不那么明显，但仍可观察到一种显著趋势：这些模型展现出从较难问题向较简单问题泛化的能力，但在从简单问题向复杂问题泛化时则不太成功。Phi-1.5 模型在 EDP 任务中是个例外，在某些难度级别上，它似乎从较易示例中的泛化能力优于从较难示例中的泛化。然而，总体而言，没有任何开源模型能够持续地从更难和更易的示例中同时学习。难度级别显著影响了模型的性能，这表明这些模型倾向于模仿模式，而非真正从上下文中进行学习。

  
这一现象表明，强大的闭源模型与开源模型之间的差异不仅在于其原始推理能力，更显著地体现在它们从上下文示例中学习的能力。这一见解突显了在评估 LLMs 的有效性和潜在应用时，同时考虑推理能力和学习能力的重要性。This phenomenon underscores that the differentiation between powerful closed-source and open-source models lies not only in their raw reasoning ability but also significantly in their capacity to learn from in-context examples. This insight highlights the importance of considering both reasoning and learning abilities when evaluating the effectiveness and potential applications of LLMs.  
这一现象表明，强大闭源模型与开源模型之间的差异不仅在于其原始推理能力，更显著地体现在它们从上下文示例中学习的能力。这一洞见凸显了在评估 LLMs 的有效性和潜在应用时，必须同时考量其推理与学习能力的重要性。

![Refer to caption](https://arxiv.org/html/2312.14890v4/extracted/5404715/Fig/ablation_1.png)

Figure 7:Heatmap of SAS and EDP task for each model.  
图 7：各模型在 SAS 和 EDP 任务上的热力图。

|   |   |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Accuracy  准确率|GPT 4 Turbo|Claude 2|GPT 3.5 Turbo|Claude Instant|PaLM 2|Yi-34b|Qwen-14b|Mistral-7b|Phi-2|MPT-30b|Vicuna-13b|Phi-1.5|
|Prompts on SAS  SAS 提示词|||||||||||||
|Zeroshot  零样本|1.000|0.445|0.942|0.442|0.416|0.620|0.706|0.149|0.191|0.000|0.113|0.000|
|Fewshot (-5)  少样本（-5）|0.978|0.685|0.920|0.735|0.603|0.065|0.103|0.043|0.095|0.165|0.085|0.155|
|Fewshot (-4)  少样本（-4）|1.000|0.662|0.902|0.667|0.516|0.093|0.189|0.129|0.149|0.156|0.084|0.118|
|Fewshot (-3)  少样本 (-3)|0.982|0.694|0.831|0.769|0.496|0.143|0.114|0.153|0.116|0.131|0.067|0.084|
|Fewshot (-2)  少样本 (-2)|1.000|0.771|0.910|0.710|0.617|0.102|0.070|0.094|0.073|0.117|0.037|0.087|
|Fewshot (-1)  少样本 (-1)|0.987|0.770|0.896|0.589|0.607|0.048|0.126|0.085|0.107|0.157|0.087|0.057|
|Fewshot (0)  少样本 (0)|0.984|0.671|0.846|0.651|0.660|0.598|0.255|0.413|0.222|0.258|0.089|0.098|
|Fewshot (1)|0.991|0.580|0.878|0.696|0.455|0.593|0.455|0.386|0.287|0.233|0.055|0.109|
|Fewshot (2)|1.000|0.675|0.829|0.587|0.656|0.647|0.444|0.296|0.260|0.175|0.067|0.056|
|Fewshot (3)|0.993|0.736|0.800|0.598|0.489|0.662|0.427|0.318|0.275|0.144|0.093|0.098|
|Fewshot (4)|1.000|0.729|0.869|0.580|0.471|0.638|0.251|0.287|0.195|0.269|0.053|0.106|
|Fewshot (5)  少样本（5 个示例）|1.000|0.671|0.844|0.602|0.607|0.167|0.387|0.356|0.196|0.202|0.055|0.064|
|Prompts on EDP  关于 EDP 的提示|||||||||||||
|Zeroshot  零样本|0.536|0.120|0.318|0.176|0.033|0.166|0.269|0.058|0.009|0.002|0.147|0.000|
|Fewshot (-5)  少样本（-5 个示例）|0.387|0.075|0.417|0.048|0.170|0.000|0.000|0.015|0.210|0.000|0.000|0.205|
|Fewshot (-4)|0.556|0.209|0.367|0.102|0.207|0.000|0.000|0.000|0.300|0.000|0.044|0.284|
|Fewshot (-3)|0.500|0.178|0.386|0.167|0.235|0.029|0.000|0.029|0.327|0.000|0.108|0.331|
|Fewshot (-2)|0.462|0.173|0.479|0.210|0.208|0.146|0.065|0.090|0.329|0.000|0.154|0.335|
|Fewshot (-1)  少样本 (-1)|0.485|0.200|0.513|0.246|0.289|0.135|0.069|0.098|0.348|0.011|0.248|0.328|
|Fewshot (0)  少样本 (0)|0.518|0.209|0.564|0.253|0.238|0.282|0.227|0.182|0.320|0.022|0.164|0.293|
|Fewshot (1)|0.535|0.184|0.535|0.355|0.205|0.089|0.266|0.089|0.115|0.013|0.160|0.115|
|Fewshot (2)|0.545|0.209|0.544|0.238|0.196|0.195|0.266|0.042|0.098|0.015|0.093|0.087|
|Fewshot (3)|0.536|0.189|0.449|0.315|0.182|0.127|0.140|0.067|0.060|0.007|0.191|0.051|
|Fewshot (4)|0.538|0.209|0.507|0.305|0.200|0.247|0.186|0.095|0.009|0.000|0.129|0.000|
|Fewshot (5)  少样本（5 个示例）|0.531|0.205|0.449|0.244|0.167|0.271|0.146|0.055|0.015|0.009|0.202|0.000|

Table 1:Weighted accuracy of Zero-shot and Few-shot on SAS and EDP. The best performance for each column is highlighted with bold font (respectively for SAS and EDP).  
表 1：SAS 和 EDP 上零样本和少样本的加权准确率。每列的最佳性能用粗体标出（分别对应 SAS 和 EDP）。

|   |   |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Failure Rate  失败率|GPT 4 Turbo|Claude 2|GPT 3.5 Turbo|Claude Instant|PaLM 2|Yi-34b|Qwen-14b|Mistral-7b|Phi-2|MPT-30b|Vicuna-13b|Phi-1.5|
|Prompts on SAS  SAS 提示词|||||||||||||
|Zeroshot  零样本|0.000|0.260|0.000|0.400|0.110|0.330|0.200|0.070|0.150|1.000|0.480|1.000|
|Fewshot (-5)  少样本（-5 个示例）|0.000|0.060|0.020|0.000|0.000|0.940|0.900|0.480|0.920|0.160|0.640|0.860|
|Fewshot (-4)|0.000|0.033|0.000|0.000|0.017|0.917|0.817|0.617|0.867|0.117|0.633|0.900|
|Fewshot (-3)|0.000|0.057|0.057|0.014|0.000|0.871|0.886|0.471|0.886|0.043|0.600|0.914|
|Fewshot (-2)|0.000|0.075|0.025|0.000|0.013|0.888|0.913|0.538|0.900|0.063|0.613|0.888|
|Fewshot (-1)  少样本 (-1)|0.000|0.044|0.022|0.000|0.011|0.911|0.856|0.622|0.878|0.078|0.589|0.933|
|Fewshot (0)  少样本 (0)|0.000|0.060|0.020|0.000|0.020|0.300|0.640|0.380|0.670|0.040|0.540|0.880|
|Fewshot (1)|0.000|0.040|0.020|0.010|0.010|0.290|0.500|0.420|0.700|0.060|0.520|0.830|
|Fewshot (2)|0.000|0.040|0.040|0.000|0.010|0.290|0.510|0.440|0.710|0.030|0.640|0.910|
|Fewshot (3)|0.000|0.020|0.050|0.010|0.030|0.280|0.450|0.460|0.670|0.030|0.650|0.830|
|Fewshot (4)|0.000|0.050|0.030|0.000|0.040|0.280|0.570|0.530|0.700|0.080|0.630|0.850|
|Fewshot (5)  少样本（5 个示例）|0.000|0.050|0.040|0.000|0.020|0.680|0.520|0.440|0.740|0.050|0.650|0.900|
|Prompts on EDP  关于 EDP 的提示|||||||||||||
|Zeroshot  零样本|0.000|0.000|0.000|0.000|0.440|0.000|0.000|0.040|0.000|0.960|0.160|0.950|
|Fewshot (-5)  少样本（-5 个示例）|0.000|0.000|0.000|0.140|0.160|0.000|0.320|0.140|0.540|0.880|0.460|0.640|
|Fewshot (-4)|0.000|0.000|0.000|0.100|0.150|0.000|0.233|0.050|0.400|0.817|0.383|0.483|
|Fewshot (-3)|0.000|0.043|0.000|0.057|0.100|0.000|0.100|0.029|0.300|0.871|0.329|0.400|
|Fewshot (-2)|0.000|0.038|0.000|0.025|0.075|0.000|0.038|0.025|0.263|0.700|0.238|0.350|
|Fewshot (-1)  少样本 (-1)|0.000|0.011|0.000|0.056|0.033|0.000|0.022|0.000|0.167|0.667|0.200|0.256|
|Fewshot (0)  少样本 (0)|0.000|0.020|0.000|0.060|0.000|0.000|0.040|0.000|0.130|0.730|0.190|0.200|
|Fewshot (1)|0.000|0.000|0.000|0.070|0.000|0.000|0.010|0.000|0.100|0.800|0.190|0.210|
|Fewshot (2)|0.000|0.040|0.000|0.050|0.000|0.000|0.020|0.000|0.000|0.750|0.090|0.100|
|Fewshot (3)|0.000|0.020|0.000|0.060|0.040|0.000|0.000|0.000|0.010|0.710|0.040|0.100|
|Fewshot (4)|0.000|0.030|0.000|0.030|0.000|0.000|0.000|0.000|0.000|0.810|0.000|0.000|
|Fewshot (5)  少样本（5 个示例）|0.000|0.050|0.000|0.030|0.000|0.000|0.000|0.000|0.000|0.820|0.030|0.000|

Table 2:Weighted failure rate of Zero-shot and Few-shot on SAS and EDP.  
表 2：零样本和少样本在 SAS 和 EDP 上的加权失败率。

## 6Conclusions and Discussion  
6 结论与讨论

In this study, we present a novel benchmark, NPHardEval, designed to rigorously evaluate LLMs’ reasoning capabilities across a spectrum of complex tasks, up to the complexity class of NP-hard. By eschewing standard QA formats in favor of complex, logic-oriented problems, this benchmark aims to provide a more accurate measure of a model’s reasoning prowess. This approach is crucial for developing LLMs capable of handling sophisticated, real-world tasks that demand high-level cognitive processing, steering the evaluation of LLMs from potentially “useful" to fundamentally “logical".  
在本研究中，我们提出了一个新颖的基准测试——NPHardEval，旨在严格评估 LLMs 在一系列复杂任务中的推理能力，直至 NP-hard 复杂度级别。该基准摒弃了标准问答格式，转而采用复杂的逻辑导向问题，旨在更准确地衡量模型的推理能力。这种方法对于开发能够处理需要高级认知处理的复杂现实世界任务的 LLMs 至关重要，从而将 LLMs 的评估从潜在的“有用”转向根本上的“逻辑”。

In addition to developing the benchmark, we compare different foundation models’ reasoning ability across task complexity and experimented with different prompt styles to understand their in-context learnability. Our study reveals a notable disparity in performance between closed-source and open-source models not only on general reasoning ability but also the disparity between “learning” and “mimicking”.  
除了开发基准测试外，我们还比较了不同基础模型在不同任务复杂度下的推理能力，并尝试了不同的提示风格以理解它们的上下文学习能力。我们的研究揭示了闭源模型与开源模型在性能上的显著差异，不仅体现在一般推理能力上，还体现在“学习”与“模仿”之间的差异上。

With regard to models’ performance across different complexity classes and difficulty levels, all models show decreased accuracy and increased failure rates as task complexity rises, with a marked performance decay at NP-Hard complexity levels. But the transition from P to NP-Complete complexity did not uniformly affect model performance; while some models showed little difference, others exhibited significant performance variations. Specifically, models like GPT 4 Turbo and Claude Instant 1.2 showed noteworthy performance shifts between these two complexity classes. Detailed performance analysis across specific tasks revealed that certain models had strengths in particular types of tasks within each complexity category, with a notable decline in model performance as they addressed more complex NP-Hard tasks.  
关于模型在不同复杂度类别和难度级别上的表现，随着任务复杂度的提升，所有模型的准确率均有所下降，失败率则相应增加，尤其在 NP-Hard 复杂度级别上表现出明显的性能衰减。然而，从 P 类到 NP-Complete 复杂度的转变并未对模型性能产生一致影响；部分模型表现差异不大，而另一些则显示出显著的性能波动。具体而言，像 GPT 4 Turbo 和 Claude Instant 1.2 这类模型在这两个复杂度类别之间表现出值得注意的性能变化。针对具体任务的详细性能分析揭示，某些模型在各类复杂度任务中的特定类型上具有优势，但随着处理更复杂的 NP-Hard 任务，模型性能出现显著下降。

Finally, we used the tasks of SAS and EDP to understand how the difficulty of few-shot examples affects the in-context learning capabilities. Closed-source models like GPT 4 Turbo and Claude 2 demonstrated minimal performance variation and high consistency across different difficulty levels, suggesting a robust ability to learn algorithmic skills from examples. Conversely, open-source models showed varied adaptability, with some like Yi-34b and Mistral-7b performing well on more challenging examples but struggling with simpler ones.  
最后，我们通过 SAS 和 EDP 任务探究了少样本示例的难度如何影响上下文学习能力。闭源模型如 GPT 4 Turbo 和 Claude 2 在不同难度级别上表现出极小的性能波动和高度一致性，显示出从示例中学习算法技能的强大能力。相反，开源模型展现出不同程度的适应性，其中 Yi-34b 和 Mistral-7b 等模型在更具挑战性的示例上表现良好，却在简单示例上遇到困难。

### 6.1Limitations  6.1 局限性

While our study offers a novel approach to assessing the reasoning abilities of LLMs, it is paramount to reflect on the limitations of our current methodology to provide a comprehensive understanding and guide future research.  
虽然我们的研究为评估 LLMs 的推理能力提供了一种新颖方法，但反思当前方法的局限性至关重要，这有助于全面理解并为未来研究提供指导。

##### Task Complexity’s Comparison  
任务复杂度的比较

A significant limitation lies in the scope of our task selection and the definition of complexity within our benchmark. While we have delineated criteria for task selection in the appendix, a more resource-intensive approach could involve the inclusion of a larger variety of questions for each task type, enhancing the depth and breadth of our evaluation. Additionally, our current approach to defining complexity is based on a linear increment of weights. This simplistic weighting heuristic may not accurately represent the nuanced complexity increase in real-world tasks. More experimental work is needed to refine this approach and determine the most effective weight assignment that truly reflects the intricacies of task complexity.  
一个显著的局限在于我们任务选择的范围以及基准测试中对复杂度的定义。尽管我们在附录中阐述了任务选择的标准，但更耗费资源的方法可能涉及为每种任务类型纳入更多样化的问题，从而增强评估的深度和广度。此外，我们当前定义复杂度的方法基于权重的线性递增。这种简化的加权启发式方法可能无法准确反映现实任务中细微的复杂度增长。需要更多的实验工作来完善这一方法，并确定最能真实反映任务复杂性细微差别的最有效权重分配方案。

##### Randomness  随机性

Another critical aspect to consider is the inherent randomness in the generation of responses by LLMs. This randomness can introduce variability in performance, making it challenging to draw consistent conclusions about a model’s reasoning capabilities. Notably, decision questions in the NP-complete level, including GCP-D and TSP-D, use true or false results as the evaluation criteria. Thus, it is hard to directly rule out the random positive cases, although the model may not go through a correct reasoning process, leading to potentially inflated performance. Addressing this issue requires a more nuanced approach to evaluating responses, possibly through repeated trials or the incorporation of statistical methods to account for this variability.  
另一个需要考虑的关键方面是 LLMs 生成答案时固有的随机性。这种随机性可能导致性能表现出现波动，使得难以就模型的推理能力得出稳定一致的结论。值得注意的是，NP 完全难度级别中的决策问题，包括 GCP-D 和 TSP-D，使用真或假的结果作为评估标准。因此，即使模型可能并未经历正确的推理过程，也很难直接排除随机产生的正面案例，这可能导致性能评估被高估。解决这一问题需要采用更精细的方法来评估答案，例如通过重复试验或引入统计方法来解释这种变异性。

##### Model Updates and Emergence  
模型更新与涌现

The fast-paced evolution of LLMs also presents a significant challenge. With the continuous version updates and emergence of advanced models like Gemini Ultra [Gemini](https://arxiv.org/html/2312.14890v4#bib.bib49) and Phi-2 [Phi-2](https://arxiv.org/html/2312.14890v4#bib.bib50), as well as an increasing number of open-source options, the analysis based on our benchmark may quickly become outdated. Thus we will monitor and experiment on new models, together with the LLMs research community, to keep pace with these rapid developments is crucial for maintaining the relevance and applicability of our findings. This dynamic nature of the field necessitates a flexible and adaptable approach to benchmarking, where updates and revisions are integral to the evaluation process.  
LLMs 的快速发展也带来了重大挑战。随着版本持续更新以及 Gemini Ultra、Phi-2 等先进模型的出现，加上开源选项日益增多，基于我们基准的分析可能很快会过时。因此，我们将与研究社区共同监测并测试新模型，跟上这些快速发展的步伐对于保持研究结果的相关性和适用性至关重要。该领域的动态特性要求采用灵活适应的基准测试方法，更新与修订必须成为评估流程的有机组成部分。

Future research should aim to expand the scope and depth of task selection, refine the complexity definition, account for generation randomness, and adapt to the evolving landscape of LLMs. Addressing these challenges will enhance the accuracy and relevance of our benchmark, contributing to the development of LLMs that are capable of sophisticated reasoning in complex, real-world scenarios.  
未来的研究应致力于拓展任务选择的广度和深度，完善复杂度定义，考虑生成随机性，并适应 LLMs 不断发展的格局。应对这些挑战将提升我们基准测试的准确性和相关性，从而推动能够应对复杂现实场景中高级推理的 LLMs 的发展。

### 6.2Research Outlook  6.2 研究展望

Our research outlook includes future investigations that can extend and enrich our understanding of the reasoning abilities of LLMs.  
我们的研究展望包括未来可扩展和丰富我们对 LLMs 推理能力理解的研究方向。

##### Fine-grained Time Complexity under Polynomial (P) with Big 𝒪 notation  
多项式时间（P）复杂度下的细粒度时间复杂度分析（采用大 𝒪 表示法）

We will further the investigation of the P complexity class with fine-grained time complexity notation, the Big 𝒪 notation. For example, the time complexity of SAS is 𝒪⁢(log⁡n), while the time complexity of the Dijkstra algorithm, the solution to SPP, is 𝒪⁢(V⁢log⁡V+E) with Fibonacci heaps [cormen2022introduction](https://arxiv.org/html/2312.14890v4#bib.bib51). This approach will enable a detailed evaluation of models within the same complexity, proving a complement perspective to the current difficulty levels and enabling a possible cross-comparison among different tasks’ difficulty levels.  
我们将进一步探究多项式（P）复杂度类，采用细粒度时间复杂度表示法——大 𝒪 表示法。例如，SAS 算法的时间复杂度为 𝒪⁢(log⁡n) ，而解决 SPP 问题的 Dijkstra 算法在使用斐波那契堆时的复杂度为 𝒪⁢(V⁢log⁡V+E) （cormen2022introduction）。这种方法能对同一复杂度类别内的模型进行精细化评估，为现有难度分级体系提供补充视角，并实现不同任务难度级别的跨任务比较。

##### Self-correction for Reasoning  
推理能力的自我修正机制

Another promising avenue is the enhancement of LLM reasoning abilities. A key strategy here is the implementation of iterative self-correction mechanisms. Pioneered by self-correction experiments in [huang2023large](https://arxiv.org/html/2312.14890v4#bib.bib52); [stechly2023gpt](https://arxiv.org/html/2312.14890v4#bib.bib53), allowing LLMs to go through multiple rounds (e.g., ranging from 1 to 10) of self-correction, we can observe how the refinement process affects the accuracy and sophistication of their responses. This iterative process mimics human problem-solving, where multiple drafts and revisions lead to improved outcomes.  
另一个值得探索的方向是提升 LLM 的推理能力。其中关键策略在于实施迭代式自我修正机制。借鉴 huang2023large 和 stechly2023gpt 开创的自我修正实验，通过让 LLM 进行多轮（例如 1 到 10 轮）自我修正，我们可以观察优化过程如何影响其回答的准确性与精细度。这种迭代过程模拟了人类解决问题的方式——通过多次草拟和修订来提升最终成果。

##### Multi-agent Systems for Reasoning  
多智能体推理系统

Moreover, exploring a multi-agent system [wu2023autogen](https://arxiv.org/html/2312.14890v4#bib.bib54); [chan2023chateval](https://arxiv.org/html/2312.14890v4#bib.bib55); [ge2023openagi](https://arxiv.org/html/2312.14890v4#bib.bib56); [ge2023llm](https://arxiv.org/html/2312.14890v4#bib.bib57) approach could significantly advance LLMs’ reasoning abilities. In such a system, different LLM agents, each potentially specialized in certain types of reasoning or knowledge areas, collaborate to solve complex problems. This collaborative approach could mimic a team of experts, each contributing their expertise, leading to more comprehensive and nuanced solutions. It also opens the door to understanding how LLMs can interact and augment each other’s capabilities, which is crucial for their application in real-world, multi-faceted problem-solving scenarios.  
此外，探索多智能体系统方法（Wu 等人，2023；Chan 等人，2023；Ge 等人，2023a；Ge 等人，2023b）可能显著提升 LLMs 的推理能力。在这种系统中，不同的 LLM 智能体（每个可能专精于特定类型的推理或知识领域）协作解决复杂问题。这种协作方式可以模拟专家团队，每个成员贡献其专业知识，从而产生更全面、更细致的解决方案。这也为理解 LLMs 如何互动并增强彼此能力打开了大门，这对于它们在现实世界、多层面问题解决场景中的应用至关重要。

These future research directions hold the potential not only to deepen our understanding of the current capabilities and limitations of LLMs but also to drive forward the development of more sophisticated and reliable AI systems. By focusing on robustness testing and enhancing reasoning abilities through innovative methods like iterative self-correction and multi-agent systems, we can make significant strides towards realizing the full potential of LLMs in complex decision-making and problem-solving tasks.  
这些未来的研究方向不仅有望深化我们对 LLMs 当前能力与局限性的理解，还将推动更复杂、更可靠的人工智能系统的发展。通过专注于稳健性测试，并借助迭代自我修正和多智能体系统等创新方法来增强推理能力，我们能够在实现 LLMs 在复杂决策和问题解决任务中的全部潜力方面取得重大进展。

## 7Acknowledgement  7 致谢

We extend our sincere gratitude to Libby Hemphill for her invaluable support in this work. We also thank Jinkui Chi, who kindly contributed to the maintenance of the benchmark’s code repository and user guidance. Additionally, we are grateful for the diverse feedback we received from Siqi Liu and many others, which illuminated our path towards enhancing the quality of this paper.  
我们衷心感谢 Libby Hemphill 对本工作提供的宝贵支持。同时，我们感谢 Jinkui Chi 对基准测试代码库维护和用户指导的慷慨贡献。此外，我们感谢 Siqi Liu 及众多同仁提出的多样化反馈，这些意见为我们提升本文质量指明了方向。

## References

###### [1]
Lizhou Fan, Lingyao Li, Zihui Ma, Sanggyu Lee, Huizi Yu, and Libby Hemphill.A bibliometric review of large language models research from 2017 to 2023.arXiv preprint arXiv:2304.02020, 2023.
###### [2]
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, et al.A survey of large language models.arXiv preprint arXiv:2303.18223, 2023.
###### [3]
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al.Training verifiers to solve math word problems.arXiv preprint arXiv:2110.14168, 2021.
###### [4]
Karthik Valmeekam, Alberto Olmo, Sarath Sreedharan, and Subbarao Kambhampati.Large language models still can’t plan (a benchmark for llms on planning and reasoning about change).arXiv preprint arXiv:2206.10498, 2022.
###### [5]
Wenhu Chen, Ming Yin, Max Ku, Pan Lu, Yixin Wan, Xueguang Ma, Jianyu Xu, Xinyi Wang, and Tony Xia.Theoremqa: A theorem-driven question answering dataset.arXiv preprint arXiv:2305.12524, 2023.
###### [6]
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt.Measuring massive multitask language understanding.arXiv preprint arXiv:2009.03300, 2020.
###### [7]
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt.Measuring mathematical problem solving with the math dataset.NeurIPS, 2021.
###### [8]
Rylan Schaeffer.Pretraining on the test set is all you need.arXiv preprint arXiv:2309.08632, 2023.
###### [9]
Simon Frieder, Luca Pinchetti, Ryan-Rhys Griffiths, Tommaso Salvatori, Thomas Lukasiewicz, Philipp Christian Petersen, Alexis Chevalier, and Julius Berner.Mathematical capabilities of chatgpt.arXiv preprint arXiv:2301.13867, 2023.
###### [10]
David S Johnson.A catalog of complexity classes.In Algorithms and complexity, pages 67–161. Elsevier, 1990.
###### [11]
Jerry Wei, Jason Wei, Yi Tay, Dustin Tran, Albert Webson, Yifeng Lu, Xinyun Chen, Hanxiao Liu, Da Huang, Denny Zhou, et al.Larger language models do in-context learning differently.arXiv preprint arXiv:2303.03846, 2023.
###### [12]
Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi, and Luke Zettlemoyer.Rethinking the role of demonstrations: What makes in-context learning work?arXiv preprint arXiv:2202.12837, 2022.
###### [13]
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al.Language models are few-shot learners.Advances in neural information processing systems, 33:1877–1901, 2020.
###### [14]
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al.Palm: Scaling language modeling with pathways.Journal of Machine Learning Research, 24(240):1–113, 2023.
###### [15]
Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, et al.Scaling instruction-finetuned language models.arXiv preprint arXiv:2210.11416, 2022.
###### [16]
Jie Huang and Kevin Chen-Chuan Chang.Towards reasoning in large language models: A survey.arXiv preprint arXiv:2212.10403, 2022.
###### [17]
Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei, Jianchao Ji, Yingqiang Ge, Libby Hemphill, and Yongfeng Zhang.War and peace (waragent): Large language model-based multi-agent simulation of world wars.arXiv preprint arXiv:2311.17227, 2023.
###### [18]
Lizhou Fan, Sara Lafia, Lingyao Li, Fangyuan Yang, and Libby Hemphill.Datachat: Prototyping a conversational agent for dataset search and visualization.arXiv preprint arXiv:2305.18358, 2023.
###### [19]
Zhenxiang Gao, Lingyao Li, Siyuan Ma, Qinyong Wang, Libby Hemphill, and Rong Xu.Examining the potential of chatgpt on biomedical information retrieval: Fact-checking drug-disease associations.Annals of Biomedical Engineering, pages 1–9, 2023.
###### [20]
Lingyao Li, Lizhou Fan, Shubham Atreja, and Libby Hemphill."hot" chatgpt: The promise of chatgpt in detecting and discriminating hateful, offensive, and toxic comments on social media.arXiv preprint arXiv:2304.10619, 2023.
###### [21]
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, et al.Emergent abilities of large language models.arXiv preprint arXiv:2206.07682, 2022.
###### [22]
Rylan Schaeffer, Brando Miranda, and Sanmi Koyejo.Are emergent abilities of large language models a mirage?arXiv preprint arXiv:2304.15004, 2023.
###### [23]
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al.Chain-of-thought prompting elicits reasoning in large language models.Advances in Neural Information Processing Systems, 35:24824–24837, 2022.
###### [24]
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa.Large language models are zero-shot reasoners.Advances in neural information processing systems, 35:22199–22213, 2022.
###### [25]
Boshi Wang, Xiang Deng, and Huan Sun.Iteratively prompt pre-trained language models for chain of thought.arXiv preprint arXiv:2203.08383, 2022.
###### [26]
Wenyue Hua and Yongfeng Zhang.System 1+ system 2= better world: Neural-symbolic chain of logic reasoning.In Findings of the Association for Computational Linguistics: EMNLP 2022, pages 601–612, 2022.
###### [27]
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L Griffiths, Yuan Cao, and Karthik Narasimhan.Tree of thoughts: Deliberate problem solving with large language models.arXiv preprint arXiv:2305.10601, 2023.
###### [28]
Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Lukas Gianinazzi, Joanna Gajda, Tomasz Lehmann, Michal Podstawski, Hubert Niewiadomski, Piotr Nyczyk, et al.Graph of thoughts: Solving elaborate problems with large language models.arXiv preprint arXiv:2308.09687, 2023.
###### [29]
Yancheng Wang, Ziyan Jiang, Zheng Chen, Fan Yang, Yingxue Zhou, Eunah Cho, Xing Fan, Xiaojiang Huang, Yanbin Lu, and Yingzhen Yang.Recmind: Large language model powered agent for recommendation.arXiv preprint arXiv:2308.14296, 2023.
###### [30]
Geunwoo Kim, Pierre Baldi, and Stephen McAleer.Language models can solve computer tasks.arXiv preprint arXiv:2303.17491, 2023.
###### [31]
Yixuan Weng, Minjun Zhu, Shizhu He, Kang Liu, and Jun Zhao.Large language models are reasoners with self-verification.arXiv preprint arXiv:2212.09561, 2022.
###### [32]
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.React: Synergizing reasoning and acting in language models.arXiv preprint arXiv:2210.03629, 2022.
###### [33]
Noah Shinn, Federico Cassano, Beck Labash, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.Reflexion: Language agents with verbal reinforcement learning.arXiv preprint arXiv:2303.11366, 14, 2023.
###### [34]
Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng, Jonathan Tompson, Igor Mordatch, Yevgen Chebotar, et al.Inner monologue: Embodied reasoning through planning with language models.arXiv preprint arXiv:2207.05608, 2022.
###### [35]
Xiaotian Zhang, Chunyang Li, Yi Zong, Zhengyu Ying, Liang He, and Xipeng Qiu.Evaluating the performance of large language models on gaokao benchmark.arXiv preprint arXiv:2305.12474, 2023.
###### [36]
Kaijie Zhu, Jiaao Chen, Jindong Wang, Neil Zhenqiang Gong, Diyi Yang, and Xing Xie.Dyval: Graph-informed dynamic evaluation of large language models.arXiv preprint arXiv:2309.17167, 2023.
###### [37]
Yann Dubois, Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin, Percy Liang, and Tatsunori B Hashimoto.Alpacafarm: A simulation framework for methods that learn from human feedback.arXiv preprint arXiv:2305.14387, 2023.
###### [38]
Liang Xu, Anqi Li, Lei Zhu, Hang Xue, Changtai Zhu, Kangkang Zhao, Haonan He, Xuanwei Zhang, Qiyue Kang, and Zhenzhong Lan.Superclue: A comprehensive chinese large language model benchmark.arXiv preprint arXiv:2307.15020, 2023.
###### [39]
Mirac Suzgun, Nathan Scales, Nathanael Schärli, Sebastian Gehrmann, Yi Tay, Hyung Won Chung, Aakanksha Chowdhery, Quoc V Le, Ed H Chi, Denny Zhou, et al.Challenging big-bench tasks and whether chain-of-thought can solve them.arXiv preprint arXiv:2210.09261, 2022.
###### [40]
Dheeru Dua, Yizhong Wang, Pradeep Dasigi, Gabriel Stanovsky, Sameer Singh, and Matt Gardner.Drop: A reading comprehension benchmark requiring discrete reasoning over paragraphs.arXiv preprint arXiv:1903.00161, 2019.
###### [41]
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi.Hellaswag: Can a machine really finish your sentence?arXiv preprint arXiv:1905.07830, 2019.
###### [42]
Andreas Kipf, Ryan Marcus, Alexander van Renen, Mihail Stoian, Alfons Kemper, Tim Kraska, and Thomas Neumann.Sosd: A benchmark for learned indexes, 2019.
###### [43]
Roberto Roberti and Mario Ruthmair.Exact methods for the traveling salesman problem with drone.Transportation Science, 55(2):315–335, 2021.
###### [44]
Shamim Ahmed.Applications of graph coloring in modern computer science.International Journal of Computer and Information Technology, 3(2):1–7, 2012.
###### [45]
Bo Sun, Ali Zeynali, Tongxin Li, Mohammad Hajiesmaili, Adam Wierman, and Danny HK Tsang.Competitive algorithms for the online multiple knapsack problem with application to electric vehicle charging.Proceedings of the ACM on Measurement and Analysis of Computing Systems, 4(3):1–32, 2020.
###### [46]
Michael Cho.The knapsack problem and its applications to the cargo loading problem.Anal. Appl. Math, 13:48–63, 2019.
###### [47]
Carla Negri Lintzmayer, Mauro Henrique Mulati, and Anderson Faustino da Silva.Register allocation with graph coloring by ant colony optimization.In 2011 30th International Conference of the Chilean Computer Science Society, pages 247–255. IEEE, 2011.
###### [48]
Miquel Bofill, Jordi Coll, Marc Garcia, Jesús Giráldez-Cru, Gilles Pesant, Josep Suy, and Mateu Villaret.Constraint solving approaches to the business-to-business meeting scheduling problem.Journal of Artificial Intelligence Research, 74:263–301, 2022.
###### [49]
Google DeepMind.Gemini.
###### [50]
Mojan Javaheripi and Sébastien Bubeck.Phi-2.
###### [51]
T.H. Cormen, C.E. Leiserson, R.L. Rivest, and C. Stein.Introduction to Algorithms, fourth edition.MIT Press, 2022.
###### [52]
Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou.Large language models cannot self-correct reasoning yet.arXiv preprint arXiv:2310.01798, 2023.
###### [53]
Kaya Stechly, Matthew Marquez, and Subbarao Kambhampati.Gpt-4 doesn’t know it’s wrong: An analysis of iterative prompting for reasoning problems.arXiv preprint arXiv:2310.12397, 2023.
###### [54]
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang, Xiaoyun Zhang, and Chi Wang.Autogen: Enabling next-gen llm applications via multi-agent conversation framework.arXiv preprint arXiv:2308.08155, 2023.
###### [55]
Chi-Min Chan, Weize Chen, Yusheng Su, Jianxuan Yu, Wei Xue, Shanghang Zhang, Jie Fu, and Zhiyuan Liu.Chateval: Towards better llm-based evaluators through multi-agent debate.arXiv preprint arXiv:2308.07201, 2023.
###### [56]
Yingqiang Ge, Wenyue Hua, Jianchao Ji, Juntao Tan, Shuyuan Xu, and Yongfeng Zhang.Openagi: When llm meets domain experts.arXiv preprint arXiv:2304.04370, 2023.
###### [57]
Yingqiang Ge, Yujie Ren, Wenyue Hua, Shuyuan Xu, Juntao Tan, and Yongfeng Zhang.Llm as os (llmao), agents as apps: Envisioning aios, agents and the aios-agent ecosystem.arXiv preprint arXiv:2312.03815, 2023.

## Appendix AExamples of Synthesized Data, the Corresponding Prompts, and LLMs’ Outputs  
附录 A 合成数据示例、对应提示词及 LLMs 输出

To further demonstrate the synthesized Data, the corresponding prompts, and LLMs’ outputs, we choose two specific problems with different attributes, including the EDP problem from the P complexity class with linear data synthesis and the GCP problem from the NP-Hard complexity class with graph data synthesis. We provide the zero-shot prompt for these questions and the output based on the GPT 4 Turbo. The details of all prompts and results available at [https://github.com/casmlab/NPHardEval](https://github.com/casmlab/NPHardEval).  
为进一步展示合成数据、对应提示词及 LLMs 的输出结果，我们选取了两个具有不同特性的具体问题：包括来自 P 复杂度类且采用线性数据合成的 EDP 问题，以及来自 NP-Hard 复杂度类且采用图数据合成的 GCP 问题。我们提供了这些问题的零样本提示词及基于 GPT-4 Turbo 生成的输出。所有提示词与结果的详细内容可在 https://github.com/casmlab/NPHardEval 查看。

### A.1Example for P: EDP  A.1 P 类问题示例：EDP

1# Synthesized Data

2{

3    "string_a": "cef",

4    "string_b": "ccb"

5}

6

7# Prompt with Synthesized Data

8The Edit Distance Problem (EDP) involves finding the minimum number of operations required to transform one string into another, where each operation is either an insertion, deletion, or substitution of a single character.

9Find the minimum number of operations required to transform the first string cef into the second string ccb. The operations are insertion, deletion, and substitution of a single character, each requiring 1 edit operation.

10Please provide the minimum number of operations required to transform the first string into the second string. Offer a brief explanation of your methodology. Keep your response concise and focused.

11Enclose your output within <root></root> tags. Present your reasoning in <reasoning>reasoning> tags and the final minimum number of operations in <final_answer></final_answer> tags, like <final_answer>{’Operations’: ’MINIMUM_NUMBER_OF_OPERATIONS’}</final_answer>.

12

13# Output (formatted for easier reading)

14<root>

15    <reasoning>

16        To transform \"cef\" into \"ccb\", we can follow these steps:\n

17        1. Substitute ’e’ with ’c’ (cef -> ccf)\n

18        2. Substitute ’f’ with ’b’ (ccf -> ccb)\n

19        This results in two substitution operations.

20    reasoning>

21    <final_answer>

22        {"Operations": 2}

23    </final_answer>

24</root>

Listing 1: EDP Example  列表 1：EDP 示例

### A.2Example for NP-Hard: GCP  
A.2 NP-Hard 问题示例：图着色问题

1# Synthesized Data

2c This is a generated graph with chromatic number 2

3p edge 6 4

4e 1 6

5e 2 6

6e 3 4

7e 3 5

8

9# Prompt with Synthesized Data

10Graph coloring refers to the problem of coloring vertices of a graph in such a way that no two adjacent vertices have the same color.

11There are 6 vertices 1 to 6 in a graph. You may use 4 colors with alphabats from A, B, C,... to color the graph.

12Please label every vertex, even if it is disconnected from the rest of the graph. Please provide each vertex’s color. Do not skip any vertices. You should also provide very short step by step reasoning. Do not use multiple lines and try your best to save output tokens.

13Your output should contain two parts enclosed by <root></root>. First, your step by step reasoning wraped by <reasoning>reasoning>. Second, the final output of all vertex numbers and their associated colors, wrapped by final_answer tag, like <final_answer>{0:’COLOR_1’, 1:’COLOR_2’, ...}</final_answer>.

14The graph is below:

15    Vertex 1 is connected to vertex 6.

16    Vertex 2 is connected to vertex 6.

17    Vertex 3 is connected to vertex 4.

18    Vertex 3 is connected to vertex 5.

19

20# Output (formatted for easier reading)

21<root>

22    <reasoning>

23        Start with vertex 1, color it A; color adjacent vertex 3 with B; vertex 2 can be A as it’s not adjacent to 1; vertex 4 connected to 2 must be different, use B; vertex 5 connected to both 2 and 3, use C; vertex 6 connected to 3 and 4, use A.

24    reasoning>

25    <final_answer>

26        {1:’A’, 2:’A’, 3:’B’, 4:’B’, 5:’C’, 6:’A’}

27    </final_answer>

28</root>

Listing 2: GCP Example  代码清单 2：图着色问题示例

## Appendix BChoices of Problems  
附录 B 问题选择依据

In the benchmark, we exclude calculation-only (math intensive) tasks for each of the complexity classes, due to the overlap with already exist benchmarks and the known uncertainty of LLMs’ math ability. For other reasoning, we provide detailed explanations and highlight them in bold.  
在本基准测试中，我们排除了各复杂度类别中纯计算型（数学密集型）任务，因其与现有基准测试存在重叠，且 LLMs 的数学能力存在已知的不确定性。对于其他推理任务，我们提供详细说明并以**粗体**形式突出标注。

### B.1Excluded P problems  B.1 排除的 P 问题

##### Prime Number Determination  
质数判定

Using algorithms like AKS primality test to determine if a given number is prime. Reason: Math-intensive.  
使用 AKS 素性测试等算法判断给定数字是否为素数。原因：数学密集型。

##### Solving Linear Equations  求解线性方程组

Finding solutions for a system of linear equations. Reason: Math-intensive.  
寻找线性方程组的解。原因：数学密集型。

##### Maximum Flow Problem  最大流问题

Finding the maximum flow from a source node to a sink node in a flow network. A flow network is a directed graph G=(V,E) where each edge (u,v)∈E has a capacity c⁢(u,v) and flow f⁢(u,v), with a designated source s and sink t. The objective is to maximize the total flow from s to t under the constraints that the flow on an edge does not exceed its capacity and the incoming flow is equal to the outgoing flow for every vertex except s and t. Reason: Most open source algorithms cannot follow the question and the prompt to provide outputs with mostly correct formats.  
在流网络中寻找从源节点到汇节点的最大流。流网络是一个有向图 G=(V,E) ，其中每条边 (u,v)∈E 具有容量 c⁢(u,v) 和流量 f⁢(u,v) ，并指定了源节点 s 和汇节点 t 。目标是在约束条件下最大化从 s 到 t 的总流量，这些约束包括：每条边上的流量不超过其容量，且除 s 和 t 外，每个顶点的流入流量等于流出流量。原因：大多数开源算法无法遵循问题和提示来提供格式基本正确的输出。

### B.2Excluded NP-Complete problems  
B.2 排除的 NP 完全问题

##### 3-SAT Problem  3-SAT 问题

Deciding whether a given Boolean formula in conjunctive normal form with three literals per clause is satisfiable. Reason: Math-intensive.  
判断一个给定的合取范式布尔公式（每个子句包含三个文字）是否可满足。原因：数学密集。

### B.3Excluded NP-hard problems  
B.3 排除的 NP 难问题

##### Integer Linear Programming  
整数线性规划

Finding the best integer solution for a set of linear equations and inequalities. Reason: Math-intensive.  
为一组线性方程和不等式寻找最优整数解。原因：数学密集型。