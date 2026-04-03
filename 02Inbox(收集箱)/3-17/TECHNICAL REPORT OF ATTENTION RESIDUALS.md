# TECHNICAL REPORT OF ATTENTION RESIDUALS  
注意力残差技术报告

# Kimi Team  Kimi 团队

 [https://github.com/MoonshotAI/Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals)

# ABSTRACT  摘要

Residual connections [12] with PreNorm [60] are standard in modern LLMs, yet they accumulate all layer outputs with fixed unit weights. This uniform aggregation causes uncontrolled hidden-state growth with depth, progressively diluting each layer’s contribution [27]. We propose Attention Residuals (AttnRes), which replaces this fixed accumulation with softmax attention over preceding layer outputs, allowing each layer to selectively aggregate earlier representations with learned, inputdependent weights. To address the memory and communication overhead of attending over all preceding layer outputs for large-scale model training, we introduce Block AttnRes, which partitions layers into blocks and attends over block-level representations, reducing the memory footprint while preserving most of the gains of full AttnRes. Combined with cache-based pipeline communication and a two-phase computation strategy, Block AttnRes becomes a practical drop-in replacement for standard residual connections with minimal overhead.  
在现代 LLMs 中，带有 PreNorm 的残差连接已成为标准配置，但它们以固定的单位权重累加所有层的输出。这种均匀聚合会导致隐藏状态随深度增长而失控，逐渐稀释每一层的贡献。我们提出了注意力残差，它用对先前层输出的 softmax 注意力取代了这种固定累加，使每一层能够通过学习的、输入依赖的权重有选择地聚合早期表示。为了解决在大规模模型训练中关注所有先前层输出所带来的内存和通信开销，我们引入了块注意力残差，它将层划分为块并关注块级表示，从而在保留完整注意力残差大部分优势的同时减少了内存占用。结合基于缓存的流水线通信和两阶段计算策略，块注意力残差成为一种实用的即插即用替代方案，能以最小开销取代标准残差连接。

Scaling law experiments confirm that the improvement is consistent across model sizes, and ablations validate the benefit of content-dependent depth-wise selection. We further integrate AttnRes into the Kimi Linear architecture [69] (48B total / 3B activated parameters) and pre-train on 1.4T tokens, where AttnRes mitigates PreNorm dilution, yielding more uniform output magnitudes and gradient distribution across depth, and improves downstream performance across all evaluated tasks.  
缩放定律实验证实，这种改进在不同模型规模下具有一致性，消融实验验证了内容相关深度选择机制的有效性。我们进一步将 AttnRes 集成至 Kimi Linear 架构[69]（总参数量 480 亿/激活参数量 30 亿），并在 1.4 万亿词元上进行预训练。实验表明 AttnRes 有效缓解了 PreNorm 稀释问题，使各层输出的量级与梯度分布更趋均匀，并在所有评估的下游任务中均取得性能提升。

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/be34e97cc54accc7e2bf0e61d372914f0621c8b3f145308bad9132ed2ee9e0f5.jpg)

(a) Standard Residuals  (a) 标准残差连接

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/4ca070c35ca4619f08c6af08654dfab9b7f54a5751e2104f1b0a28192cb3a0dd.jpg)

(b) Full Attention Residuals  
(b) 全注意力残差

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/ef2152d49fc76ab3032a93823db7917af5534d38eb523aa1bf2bcd918c0da0dc.jpg)

(c) Block Attention Residuals  
(c) 块注意力残差

Figure 1: Overview of Attention Residuals. (a) Standard Residuals: standard residual connections with uniform additive accumulation. (b) Full AttnRes: each layer selectively aggregates all previous layer outputs via learned attention weights. (c) Block AttnRes: layers are grouped into blocks, reducing memory from O(Ld) to O(Nd) .  
图 1：注意力残差概览。(a) 标准残差：采用均匀加性累积的标准残差连接。(b) 全注意力残差：每层通过学习的注意力权重选择性聚合所有先前层的输出。(c) 块注意力残差：将层分组为块，将内存从 O(Ld) 减少到 O(Nd) 。

第 1 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

# 1 Introduction  1 引言

Standard residual connections [12] are the de facto building block of modern LLMs [35, 51, 9]. The update hl​= hl−1​+fl−1​(hl−1​) is widely understood as a gradient highway that lets gradients bypass transformations via identity mappings, enabling stable training at depth. Yet residuals also play a second role that has received less attention. Unrolling the recurrence shows that every layer receives the same uniformly-weighted sum of all prior layer outputs; residuals define how information aggregates across depth. Unlike sequence mixing and expert routing, which now employ learnable input-dependent weighting [53, 20, 9], this depth-wise aggregation remains governed by fixed unit weights, with no mechanism to selectively emphasize or suppress individual layer contributions.  
标准残差连接[12]是现代 LLMs[35, 51, 9]事实上的构建模块。更新 hl​= hl−1​+fl−1​(hl−1​) 被广泛理解为梯度高速公路，通过恒等映射让梯度绕过变换，从而实现深度稳定训练。然而残差连接还承担着另一项较少受到关注的作用。展开递归过程可见，每一层都接收所有先前层输出的相同均匀加权和；残差连接定义了信息如何在深度维度上聚合。与当前采用可学习的输入依赖加权[53, 20, 9]的序列混合和专家路由机制不同，这种深度方向的聚合仍由固定单位权重控制，缺乏选择性强调或抑制特定层贡献的机制。

In practice, PreNorm [60] has become the dominant paradigm, yet its unweighted accumulation causes hidden-state magnitudes to grow as O(L) with depth, progressively diluting each layer’s relative contribution [27]. Early-layer information is buried and cannot be selectively retrieved; empirically, a significant fraction of layers can be pruned with minimal loss [11]. Recent efforts such as scaled residual paths [54] and multi-stream recurrences [72] remain bound to the additive recurrence, while methods that do introduce cross-layer access [36, 56] are difficult to scale. The situation parallels the challenges that recurrent neural networks (RNNs) faced over the sequence dimension before attention mechanism provided an alternative.  
在实践中，PreNorm [60]已成为主导范式，但其未加权的累积导致隐藏状态幅度随深度以 O(L) 增长，逐渐稀释了每一层的相对贡献[27]。早期层的信息被埋没，无法被选择性检索；经验表明，大部分层可以在损失最小的情况下被剪枝[11]。最近的努力，如缩放残差路径[54]和多流递归[72]，仍然受限于加法递归，而确实引入跨层访问的方法[36, 56]则难以扩展。这种情况类似于循环神经网络（RNNs）在注意力机制提供替代方案之前，在序列维度上所面临的挑战。

We observe a formal duality between depth-wise accumulation and the sequential recurrence in RNNs. Building on this duality, we propose Attention Residuals (AttnRes), which replaces the fixed accumulation hl​=∑i​vˉi​​ with hl​=∑i​αil​αˉ⋅vi​​ , where αi→l​ are softmax attention weights computed from a single learned pseudo-query wl​∈Rd per layer. This lightweight mechanism enables selective, content-aware retrieval across depth with only one d -dimensional vector per layer. Indeed, standard residual connections and prior recurrence-based variants can all be shown to perform depth-wise linear attention; AttnRes generalizes them to depth-wise softmax attention, completing for depth the same linear-to-softmax transition that proved transformative over sequences (§6.2, §6.1).  
我们观察到深度累积与 RNN 中的顺序递归之间存在形式上的对偶性。基于这一对偶性，我们提出了注意力残差（AttnRes），它将固定的累积 hl​=∑i​vˉi​​ 替换为 hl​=∑i​αil​αˉ⋅vi​​ ，其中 αi→l​ 是由每层单个学习到的伪查询 wl​∈Rd 计算出的 softmax 注意力权重。这种轻量级机制通过每层仅一个 d 维向量，实现了跨深度的选择性、内容感知检索。实际上，标准的残差连接和先前基于递归的变体都可以被证明执行的是深度线性注意力；AttnRes 将其推广到深度 softmax 注意力，为深度完成了与序列上被证明具有变革性的线性到 softmax 相同的转变（§6.2，§6.1）。

In standard training, Full AttnRes adds negligible overhead, since the layer outputs it requires are already retained for backpropagation. At scale, however, activation recomputation and pipeline parallelism are routinely employed, and these activations must now be explicitly preserved and communicated across pipeline stages. We introduce Block AttnRes to maintain efficiency in this regime: layers are partitioned into N blocks, each reduced to a single representation via standard residuals, with cross-block attention applied only over the N block-level summaries. This brings both memory and communication down to O(Nd) , and together with infrastructure optimizations (§4), Block AttnRes serves as a drop-in replacement for standard residual connections with marginal training cost and negligible inference latency overhead.  
在标准训练中，全注意力残差连接（Full AttnRes）带来的开销微乎其微，因为它所需的层输出在反向传播过程中已被保留。然而，在大规模训练中，通常会采用激活重计算和流水线并行技术，此时这些激活必须显式地保存并在流水线阶段之间传递。我们引入了块注意力残差连接（Block AttnRes）以在此场景下保持效率：将层划分为 N 个块，每个块通过标准残差连接简化为单一表示，仅对 N 个块级摘要应用跨块注意力。这将内存占用和通信开销降至 O(Nd) ，结合基础设施优化（§4），块注意力残差连接可作为标准残差连接的即插即用替代方案，仅带来边际训练成本与可忽略的推理延迟开销。

Scaling law experiments confirm that AttnRes consistently outperforms the baseline across compute budgets, with Block AttnRes matching the loss of a baseline trained with 1.25× more compute. We further integrate AttnRes into the Kimi Linear architecture [69] (48B total / 3B activated parameters) and pre-train on 1.4T tokens. Analysis of the resulting training dynamics reveals that AttnRes mitigates PreNorm dilution, with output magnitudes remaining bounded across depth and gradient norms distributing more uniformly across layers. On downstream benchmarks, our final model improves over the baseline across all evaluated tasks.  
扩展定律实验证实，在各类计算预算下，注意力残差机制始终优于基线模型，其中分块注意力残差机制的性能损失与基线模型在增加 1.25× 倍计算量后的训练结果相当。我们进一步将注意力残差机制整合至 Kimi 线性架构[69]（总参数量 480 亿/激活参数量 30 亿），并在 1.4 万亿词元上进行预训练。对训练动态的分析表明，注意力残差机制有效缓解了预归一化稀释问题，其输出幅度在深度维度上保持有界，且梯度范数在各层间分布更为均匀。在下游任务基准测试中，我们的最终模型在所有评估任务上均超越基线表现。

# Contributions  贡献

• Attention Residuals. We propose AttnRes, which replaces fixed residual accumulation with learned softmax attention over depth, and its scalable variant Block AttnRes that reduces memory and communication from O(Ld) to O(Nd) . Through a unified structured-matrix analysis, we show that standard residuals and prior recurrence-based variants correspond to depth-wise linear attention, while AttnRes performs depth-wise softmax attention.  
• 注意力残差机制。我们提出注意力残差机制，该机制通过基于深度的可学习 softmax 注意力替代固定的残差累积，并进一步提出其可扩展变体——分块注意力残差机制，将内存与通信开销从 O(Ld) 降低至 O(Nd) 。通过统一的结构化矩阵分析，我们证明标准残差机制及先前基于循环的变体均对应深度维度上的线性注意力，而注意力残差机制实现了深度维度上的 softmax 注意力。

• Infrastructure for scale. We develop system optimizations that make Block AttnRes practical and efficient at scale, including cross-stage caching that eliminates redundant transfers under pipeline parallelism and a two-phase inference strategy that amortizes cross-block attention via online softmax [31]. The resulting training overhead is marginal, and the inference latency overhead is less than 2% on typical inference workloads.  
• 规模化基础设施。我们开发了系统优化方案，使 Block AttnRes 在大规模应用中既实用又高效，包括消除流水线并行下冗余传输的跨阶段缓存，以及通过在线 softmax[31]分摊跨块注意力计算的两阶段推理策略。由此产生的训练开销微乎其微，在典型推理工作负载下，推理延迟开销低于 2% 。

• Comprehensive evaluation and analysis. We validate AttnRes through scaling law experiments, component ablations, and downstream benchmarks on a 48B-parameter model pre-trained on 1.4T tokens, demonstrating consistent improvements over standard residual connections. Training dynamics analysis further reveals that AttnRes mitigates PreNorm dilution, yielding bounded hidden-state magnitudes and more uniform gradient distribution across depth.  
• 综合评估与分析。我们通过扩展定律实验、组件消融研究，以及基于 1.4T 词元预训练的 480 亿参数模型的下游基准测试，对 AttnRes 进行了验证，结果表明其相较于标准残差连接具有持续性的改进。训练动态分析进一步揭示，AttnRes 能够缓解 PreNorm 稀释问题，从而产生有界的隐藏状态幅度，并在深度维度上实现更均匀的梯度分布。

2

第 2 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

# 2 Motivation  2 研究动机

Notation. Consider a batch of input sequences with shape B×T×d , where B is the batch size, T is the sequence length, and d is the hidden dimension. For clarity, we write formulas for a single token: hl​∈Rd denotes the hidden state entering layer l , where l∈{1,…,L} is the layer index and L is the total number of layers. The token embedding is h1​ . The function fl​ represents the transformation applied by layer l . In Transformer models, we treat each self-attention or MLP as an individual layer.  
符号说明。考虑一批形状为 B×T×d 的输入序列，其中 B 为批次大小， T 为序列长度， d 为隐藏维度。为清晰起见，我们针对单个词元书写公式： hl​∈Rd 表示进入第 l 层的隐藏状态，其中 l∈{1,…,L} 为层索引， L 为总层数。词元嵌入为 h1​ 。函数 fl​ 代表第 l 层所应用的变换。在 Transformer 模型中，我们将每个自注意力机制或 MLP 视为独立的层。

# 2.1 Training Deep Networks via Residuals  
2.1 通过残差连接训练深度网络

Residual Learning. Residual learning [12] proves to be a critical technique in training deep networks as it allows gradients to bypass transformations. Specifically, each layer updates the hidden state as:  
残差学习。残差学习[12]被证明是训练深度网络的关键技术，因为它允许梯度绕过变换。具体来说，每一层更新隐藏状态的方式为：

hl​=hl−1​+fl−1​(hl−1​)

Expanding this recurrence, the hidden state at layer l is the sum of the embedding and all preceding layer outputs: hl​=h1​+∑i=1l−1​fi​(hi​)​ . The key insight behind residual connections is identity mapping: each layer preserves a direct path for both information and gradients to flow unchanged. During back-propagation, the gradient with respect to an intermediate hidden state is:  
展开这个递推关系，第 l 层的隐藏状态是嵌入向量与所有前序层输出的总和： hl​=h1​+∑i=1l−1​fi​(hi​)​ 。残差连接背后的核心思想是恒等映射：每一层都保留了一条直接路径，使得信息和梯度能够原封不动地流动。在反向传播过程中，关于中间隐藏状态的梯度为：

∂hl​∂L​=∂hL​∂L​⋅j=l∏L−1​(I+∂hj​∂fj​​)

Expanding this product yields I plus higher-order terms involving the layer Jacobians ∂fj​/∂hj​ . The identity term is always preserved, providing a direct gradient path from the loss to any layer regardless of depth.  
展开该乘积得到单位矩阵加上涉及层雅可比矩阵 ∂fj​/∂hj​ 的高阶项。恒等项始终保留，无论深度如何，都能提供从损失函数到任意层的直接梯度路径。

Generalizing Residuals. While effective, the fixed unit coefficients in the residual update treat every layer’s contribution uniformly, offering no mechanism to adapt the mixing across depth. Highway networks [45] relax this by introducing learned element-wise gates:  
广义残差结构。虽然残差更新中的固定单位系数有效，但它对所有层的贡献一视同仁，缺乏根据深度调整混合比例的机制。高速公路网络[45]通过引入可学习的逐元素门控机制来放宽这一限制：

hl​=(1−gl​)⊙hl−1​+gl​⊙fl−1​(hl−1​)

where gl​∈[0,1]d interpolates between the transformation and the identity path. More generally, both are instances of a weighted recurrence hl​=αl​⋅hl−1​+βl​⋅fl−1​(hl−1​) , with residual setting αl​=βl​=1 and Highway setting αl​=1−gl​ , βl​=gl​ .  
其中 gl​∈[0,1]d 在变换路径与恒等路径之间进行插值。更一般地，这两种结构都属于加权递归 hl​=αl​⋅hl−1​+βl​⋅fl−1​(hl−1​) 的特例：残差网络对应 αl​=βl​=1 参数设置，高速公路网络对应 αl​=1−gl​ 和 βl​=gl​ 参数设置。

Limitations. Whether fixed or gated, both approaches share a fundamental constraint: each layer can only access its immediate input hl−1​ , a single compressed state that conflates all earlier layer outputs, rather than the individual outputs themselves. This entails several limitations: (1) no selective access: different layer types (e.g., attention vs. MLP) receive the same aggregated state, despite potentially benefiting from different weightings; (2) irreversible loss: information lost through aggregation cannot be selectively recovered in deeper layers; and (3) output growth: later layers learn increasingly larger outputs to gain influence over the accumulated residual, which can destabilize training. These limitations motivate a mechanism that lets each layer selectively aggregate information from all preceding layers.  
局限性。无论是固定门控还是可学习门控，这两种方法都存在一个根本性约束：每个层只能访问其直接输入 hl−1​ ——这是一个将所有先前层输出压缩融合的单一状态，而非各层原始输出本身。这导致了几项局限：(1) 无法选择性访问：不同类型的层（如注意力层与 MLP 层）接收相同的聚合状态，尽管它们可能从差异化的加权中获益；(2) 信息不可逆丢失：通过聚合丢失的信息无法在深层中被选择性恢复；(3) 输出膨胀：后续层为增强对累积残差的影响力会学习生成越来越大的输出，这可能破坏训练稳定性。这些局限性促使我们寻求一种新机制，使每个层能够选择性地聚合来自所有前置层的信息。

# 3 Attention Residuals: A Unified View of Time and Depth  
3 注意力残差：时间与深度的统一视角

The limitations discussed above are reminiscent of similar bottlenecks in sequence modeling, suggesting that we seek similar solutions for the depth dimension.  
上述讨论的局限性让人联想到序列建模中类似的瓶颈，这表明我们应为深度维度寻求类似的解决方案。

The Duality of Time and Depth. Like RNNs over time, residual connections compress all prior information into a single state hl​ over depth. For sequence modeling, the Transformer improved upon RNNs by replacing recurrence with attention [3, 52], allowing each position to selectively access all previous positions with data-dependent weights. We propose the same methodology for depth:  
时间与深度的双重性。如同 RNN 在时间维度上的处理，残差连接将所有先前的信息压缩成一个单一的状态 hl​ ，这一过程发生在深度维度上。对于序列建模，Transformer 通过用注意力机制[3, 52]替代循环结构，改进了 RNN，使得每个位置能够根据数据依赖的权重，有选择地访问所有先前的位置。我们提出将同样的方法应用于深度维度：

hl​=α0→l​⋅h1​+i=1∑l−1​αi→l​⋅fi​(hi​)(1)

where αi→l​ are layer-specific attention weights satisfying ∑i=0l−1​αi→l​=1​ . Unlike sequence length (which can reach millions of tokens), network depth is typically modest L<1000) , making O(L2) attention over depth computationally feasible. We call this approach Attention Residuals, abbreviated as AttnRes.  
其中 αi→l​ 是特定于层的注意力权重，满足 ∑i=0l−1​αi→l​=1​ 。与序列长度（可能达到数百万个标记）不同，网络深度通常较为有限 L<1000) ，这使得在深度维度上进行 O(L2) 注意力计算在计算上是可行的。我们将这种方法称为注意力残差，简称 AttnRes。

3

第 3 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

# 3.1 Full Attention Residuals  
3.1 完全注意力残差

The attention weights can be written as αi→l​=ϕ(ql​,ki​) for a kernel function ϕ:Rd×Rd→R≥0​. , where ql​ and ki​ are query and key vectors [23, 70]. Different choices of ϕ recover different residual variants (§6.2); we adopt ϕ(q,k)˙​=˙exp˙​(q⊤RMSNorm(k)˙​) [66] with normalization, yielding softmax attention over depth:  
注意力权重可以表示为核函数 ϕ:Rd×Rd→R≥0​. 的 αi→l​=ϕ(ql​,ki​) ，其中 ql​ 和 ki​ 分别是查询向量和键向量[23, 70]。不同的 ϕ 选择对应不同的残差变体（§6.2）；我们采用带归一化的 ϕ(q,k)˙​=˙exp˙​(q⊤RMSNorm(k)˙​) [66]，从而得到基于深度的 softmax 注意力：

αi→l​=∑j=0l−1​ϕ(ql​,kj​)ϕ(ql​,ki​)​(2)

For each layer l , we define:  
对于每个层 l ，我们定义：

ql​=wl​,ki​=vi​={h1​fi​(hi​)​i=01≤i≤l−1​(3)

where the query ql​=wl​ is a layer-specific learnable vector in Rd . The RMSNorm inside ϕ prevents layers with large-magnitude outputs from dominating the attention weights. The input to layer l is then:  
其中查询 ql​=wl​ 是 Rd 中特定于层的可学习向量。 ϕ 内部的 RMSNorm 防止了具有大幅值输出的层主导注意力权重。那么，层 l 的输入为：

hl​=i=0∑l−1​αi→l​⋅vi​(4)

We call this form full attention residuals. For each token, Full AttnRes requires O(L2d) arithmetic and O(Ld) memory to store layer outputs. Since depth is far smaller than sequence length, the arithmetic cost is modest.  
我们称这种形式为完全注意力残差。对于每个标记，完全注意力残差需要 O(L2d) 的算术运算和 O(Ld) 的内存来存储层输出。由于深度远小于序列长度，算术成本是适中的。

Overhead. The O(Ld) memory overlaps entirely with the activations already retained for backpropagation, so Full AttnRes introduces no additional memory overhead in vanilla training. At scale, however, activation recomputation and pipeline parallelism are widely adopted: layer outputs that would otherwise be freed and recomputed must now be kept alive for all subsequent layers, and under pipeline parallelism each must further be transmitted across stage boundaries. Both the memory and communication overhead then grow as O(Ld) .  
开销。 O(Ld) 内存与已为反向传播保留的激活完全重叠，因此在普通训练中，Full AttnRes 不会引入额外的内存开销。然而，在大规模训练中，激活重计算和流水线并行被广泛采用：原本会被释放并重新计算的层输出现在必须为所有后续层保持存活，并且在流水线并行下，每个输出还必须跨阶段边界传输。此时，内存和通信开销都会随着 O(Ld) 增长。

Blockwise optimization. A deliberate design choice in Full AttnRes is that the pseudo-query wl​ is a learned parameter decoupled from the layer’s forward computation. This independence means that attention weights for any group of layers can be computed in parallel without waiting for their sequential outputs, and in particular permits grouping the L layers into N blocks of S layers each and batching the attention computation within each block, reducing per-layer memory I/O from O(Ld) to O˙((S+N)d) (we defer the detailed two-phase strategy to  S4 ). Under current distributed training regimes, however, the dominant cost is not local memory bandwidth but cross-stage communication under pipeline parallelism: every layer output must still be transmitted between stages, and this O(Ld) communication overhead cannot be alleviated by local batching. This motivates the Block AttnRes variant introduced below, which reduces the number of cross-stage representations from L to N . We anticipate that future interconnect improvements will make the full O(Ld) communication practical, fully realizing the potential of Full AttnRes.  
分块优化。Full AttnRes 中一个深思熟虑的设计选择是，伪查询 wl​ 是一个与层的前向计算解耦的学习参数。这种独立性意味着任何一组层的注意力权重都可以并行计算，而无需等待它们的顺序输出，特别是允许将 L 层分组为 N 个块，每个块包含 S 层，并在每个块内批量计算注意力，从而将每层的内存 I/O 从 O(Ld) 减少到 O˙((S+N)d) （我们将详细的两阶段策略推迟到  S4 中讨论）。然而，在当前的分布式训练机制下，主要成本不是本地内存带宽，而是流水线并行下的跨阶段通信：每个层的输出仍然必须在阶段之间传输，而这种 O(Ld) 通信开销无法通过本地批处理来缓解。这促使我们引入了下面介绍的 Block AttnRes 变体，它将跨阶段表示的数量从 L 减少到 N 。我们预计未来的互连改进将使完整的 O(Ld) 通信变得可行，从而充分发挥 Full AttnRes 的潜力。

# 3.2 Block Attention Residuals  
3.2 块注意力残差

We propose Block Attention Residuals, which partitions the L layers into N blocks: within each block, the layer outputs are reduced to a single representation via summation, and across blocks, we apply full attention over only N block-level representations and the token embedding. This reduces both memory and communication overhead from O(Ld) to O(Nd)ˉ​ .  
我们提出块注意力残差方法，该方法将 L 层划分为 N 个块：在每个块内部，通过求和将层输出简化为单一表示；在块之间，我们仅对 N 个块级表示和词元嵌入应用完整注意力机制。这将内存和通信开销从 O(Ld) 降低至 O(Nd)ˉ​ 。

Intra-Block Accumulation. Specifically, we divide the L layers into N blocks of S=L/N layers each, assuming L is divisible by N ; otherwise, the last block contains the remaining L mod N layers. Let Bn​ denote the set of layer indices in block n (n=1,…,N) . To form a block, we sum all of its layer outputs:  
块内累积。具体来说，我们将 L 层划分为 N 个块，每个块包含 S=L/N 层，假设 L 能被 N 整除；否则，最后一个块包含剩余的 L mod N 层。设 Bn​ 表示块 n (n=1,…,N) 中的层索引集合。为了形成一个块，我们对其所有层的输出进行求和：

bn​=j∈Bn​∑​fj​(hj​)(5)

We further denote bni​ as the partial sum over the first i layers in Bn​ , so that bn​=bnS​ . When L is not divisible by N the final partial sum is taken as the last block’s representation. As in Full AttnRes, the RMSNorm inside ϕ prevents magnitude differences between complete blocks and partial sums from biasing the attention weights.  
我们进一步将 bni​ 表示为 Bn​ 中前 i 层的部分和，使得 bn​=bnS​ 。当 L 不能被 N 整除时，最后一个部分和被视为最后一个块的表示。与 Full AttnRes 中一样， ϕ 内部的 RMSNorm 防止了完整块和部分和之间的幅度差异对注意力权重产生偏差。

4

第 4 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

python复制

`def block_attn_res(blocks: list[Tensor], partial_block: Tensor, proj: Linear, norm: RMSNorm) -> Tensor:     ''''    Inter-block attention: attend over block reps + partial sum.    blocks:        N tensors of shape [B, T, D]: completed block representations for each previous block    partial_block:        [B, T, D]: intra-block partial sum (b_n^i)    ''''    V = torch.stack(blocks + [partial_block]) # [N+1, B, T, D]    K = norm(V)    logits = torch.einsum('d, n b t d -> n b t', proj.weight.squeeze(), K)    h = torch.einsum('n b t, n b t d -> b t d', logits softmax(0), V)    return h def forward(self, blocks: list[Tensor], hidden_states: Tensor) -> tuple[list[Tensor], Tensor]:     partial_block = hidden_states    # apply block attnres before attn    # blocks already include token embedding    h = block_attn_res(blocks, partial_block, self.attn_res_prog, self.attn_res_norm)    # if reaches block boundary, start new block    # block_size counts ATTN + MLP; each transformer layer has 2    if self(layer_number % (self.block_size // 2) == 0:        blocks.append(partial_block)        partial_block = None    # self-attention layer    attn_out = self.attn(self.attn_norm(h))    partial_block = partial_block + attn_out if partial_block is not None else attn_out    # apply block attnres before MLP    h = block_attn_res(blocks, partial_block, self.mlp_res_prog, self.mlp_res_norm)    # MLP layer    mlp_out = self.mlp(self.mlp_norm(h))    partial_block = partial_block + mlp_out    return blocks, partial_block` 

Figure 2: PyTorch-style pseudo code for Block Attention Residuals. block_attn_res computes softmax attention over block representations using a learned pseudo-query wl​ ; forward is a single-layer pass that maintains partial_block bni​ , intra-block residual) and blocks ([b0​,…,bn−1​] , inter-block history).  
图 2：块注意力残差的 PyTorch 风格伪代码。block_attn_res 使用学习到的伪查询 wl​ 计算块表示的 softmax 注意力；forward 是单层前向传播，维护 partial_block bni​ （块内残差）和 blocks ([b0​,…,bn−1​] （块间历史）。

Inter-Block Attention. In Full AttnRes, the input to layer l is computed by attending over all outputs up to fl−1​(hl−1​) . The block-wise variant replaces these individual outputs with block representations, defining b0​=h1​ so that the token embedding is always included as a source. For the i -th layer in block n , the value matrix is:  
块间注意力机制。在完全注意力残差网络中，第 l 层的输入是通过关注直到 fl−1​(hl−1​) 的所有输出计算得出的。块级变体将这些单独的输出替换为块表示，定义 b0​=h1​ 以确保词元嵌入始终作为源被包含。对于块 n 中的第 i 层，其值矩阵为：

V={[b0​,b1​,…,bn−1​]⊤[b0​,b1​,…,bn−1​,bni−1​]⊤​i fi=1(f i r s t l a y e r o f b l o c kn)i fi≥2(s u b s e q u e n t l a y e r s)​(6)

Keys and attention weights follow Eq. 3 and Eq. 2. The input of the very first layer of the network is the token embeddings, i.e. b0​=h1​ . In each block, the first layer receives the previous block representations and the token embeddings, and the subsequent layers additionally attend to the partial sum bni−1​ . The final output layer aggregates all N block representations. Fig. 2 provides PyTorch-style pseudocode for Block AttnRes.  
键和注意力权重遵循公式 3 和公式 2。网络最初始层的输入是词元嵌入，即 b0​=h1​ 。在每个块中，第一层接收前一个块的表示和词元嵌入，而后续层额外关注部分和 bni−1​ 。最终输出层聚合所有 N 块表示。图 2 提供了 Block AttnRes 的 PyTorch 风格伪代码。

Efficiency. Since each layer now attends over N block representations rather than L individual outputs, memory reduces from O(L) to O(N) and computation from O(L2) to O(N2) . The block count N interpolates between two extremes: N=L recovers Full AttnRes, while N=1 reduces to standard residual connections with the embedding isolated as b0​ . Empirically, we find that N≈8 recovers most of the benefit across model scales, requiring only eight stored hidden states per token (see  S5 ).  
效率。由于每一层现在关注的是 N 块表示而非 L 单个输出，内存占用从 O(L) 降至 O(N) ，计算量从 O(L2) 减至 O(N2) 。块数量 N 在两个极端之间插值： N=L 恢复为完整注意力残差连接，而 N=1 则退化为标准残差连接，嵌入层被隔离为 b0​ 。实验表明， N≈8 能在不同模型规模下恢复大部分性能优势，每个词元仅需存储八个隐藏状态（参见  S5 ）。

Beyond memory and computation, the block structure also benefits inference latency: block boundaries define the dispatch granularity for the blockwise optimization described in  S3 , and the fixed block count N bounds the KV cache size. The parallel inter-block results are merged with the sequential intra-block partial sums via online softmax [31], preserving exact equivalence (§4).  
除了内存和计算效率，块结构还有助于降低推理延迟：块边界定义了  S3 中描述的块级优化的调度粒度，固定块数 N 限制了 KV 缓存的大小。通过在线 softmax[31]将并行块间结果与顺序块内部分和合并，保持了精确等价性（§4）。

# 4 Infrastructure Design  4 基础设施设计

Block AttnRes introduces additional system challenges compared to standard residual connections. For large-scale model training, block representations must be propagated across pipeline stages, causing heavy communication in a  
与标准残差连接相比，块注意力残差模块引入了额外的系统挑战。在大规模模型训练中，块表示必须在流水线阶段之间传播，这会导致严重的通信开销。

5

第 5 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/35bdfb0e33aed58ea99f0bcc8a2cca30f47cc4319c1e73f60214fbe9a94113fd.jpg)

Figure 3: Cache-based pipeline communication example with 4 physical ranks and 2 virtual stages per rank, where hatched boxes denote end of AttnRes blocks. Numbers indicate micro-batch indices. Each rank caches previously received blocks; stage transitions only transmit incremental blocks (+[b1​,b2​]) instead of the full history.  
图 3：基于缓存的流水线通信示例，包含 4 个物理层级和每层级 2 个虚拟阶段，其中阴影框表示注意力残差块的结束位置。数字代表微批次索引。每个层级会缓存先前接收的块；阶段转换时仅传输增量块 (+[b1​,b2​]) 而非完整历史记录。

naïve implementation. During inference, repeated access to accumulated block representations increases latency, while long-context prefilling amplifies the memory cost of caching block representations. We address these challenges with cross-stage caching in training, and with a two-phase computation strategy together with a memory-efficient prefilling scheme in inference.  
朴素实现。在推理过程中，重复访问累积的块表示会增加延迟，而长上下文预填充则会放大缓存块表示的内存开销。我们通过训练中的跨阶段缓存，以及推理中的两阶段计算策略与内存高效预填充方案来解决这些挑战。

# 4.1 Training  4.1 训练

For small-scale training, AttnRes adds a tiny computation overhead and no extra memory usage, as the activations need to be saved for backpropagation regardless. Under large-scale distributed training, pipeline parallelism poses the primary infrastructure challenge for AttnRes. Full AttnRes requires all L layer outputs to be transmitted across stages; Block AttnRes reduces this to N block representations, and the optimizations below further minimize the remaining overhead.  
对于小规模训练，AttnRes 仅增加极小的计算开销，且不产生额外的内存占用，因为无论是否使用 AttnRes，激活值都需要保存以进行反向传播。在大规模分布式训练中，流水线并行是 AttnRes 面临的主要基础设施挑战。完整的 AttnRes 需要所有 L 层输出跨阶段传输；而分块 AttnRes 将此减少为 N 块表示，并且通过以下优化措施，可以进一步最小化剩余的开销。

Pipeline communication. With standard residual connections, pipeline parallelism [18] transfers a fixed-size hidden state between adjacent stages, independent of pipeline depth. Block AttnRes requires all accumulated block representations at each stage for inter-block attention, and naïvely transmitting the full history at every transition incurs redundant communication.  
流水线通信。采用标准残差连接时，流水线并行技术[18]在相邻阶段间传输固定大小的隐藏状态，与流水线深度无关。而 Block AttnRes 机制需要在每个阶段获取所有已累积的块表示以进行块间注意力计算，若在每个转换节点简单传输完整历史记录，将产生冗余通信开销。

Consider an interleaved pipeline schedule [33] with P physical stages and V virtual stages per physical stage. For simplicity, assume each physical stage produces on average Np​ block representations of dimension d per token.1 With C=PV total chunks (each physical stage in each virtual stage), the j -th chunk accumulates jNp​ blocks. Naïvely transmitting all accumulated blocks at every transition incurs per-token communication cost:  
考虑一个交错流水线调度方案[33]，包含 P 个物理阶段，每个物理阶段包含 V 个虚拟阶段。为简化分析，假设每个物理阶段平均为每个令牌生成 Np​ 个维度为 d 的块表示。1 在总共 C=PV 个数据块（每个虚拟阶段的每个物理阶段）的情况下，第 j 个数据块会累积 jNp​ 个块。若在每个转换点天真地传输所有累积块，将产生每个令牌的通信成本：

Commn a i v e​=j=1∑C−1​jNp​⋅d=2C(C−1)​Np​d.(7)

Cross-stage caching. Since each physical stage processes multiple virtual stages in succession, we can eliminate this redundancy by caching blocks locally: blocks received during earlier virtual stages remain in local memory and need not be re-transmitted. The first virtual stage v=1 ) has no cache and accumulates normally; for v≥2 , each transition conveys only the ∼PNp​ incremental blocks accumulated since the receiver’s corresponding chunk in the previous virtual stage. Total communication reduces to:  
跨阶段缓存。由于每个物理阶段连续处理多个虚拟阶段，我们可以通过本地缓存块来消除这种冗余：在早期虚拟阶段接收到的块保留在本地内存中，无需重新传输。第一个虚拟阶段 v=1 没有缓存，正常累积；对于 v≥2 ，每次传输仅传递自接收方在前一个虚拟阶段对应块以来累积的 ∼PNp​ 增量块。总通信量减少为：

Commc a c h e d​=f i r s t v i r t u a l s t a g e2P(P−1)​Np​d​​+s u b s e q u e n t v i r t u a l s t a g e s(V−1)P2Np​d​​.(8)

Caching reduces peak per-transition cost from O(C) to O(P) , a V× improvement that enables full overlap with computation during steady-state 1F1B. The backward pass benefits from the same scheme. Fig. 3 illustrates this optimization with P=4 and V=2 : for the second virtual stage, caching eliminates 6 redundant block transmissions.  
缓存机制将每次转换的峰值成本从 O(C) 降低至 O(P) ，实现 V× 的性能提升，使得在稳态 1F1B 期间能够与计算完全重叠。反向传播过程同样受益于此方案。图 3 通过 P=4 和 V=2 展示了该优化效果：在第二个虚拟阶段，缓存机制消除了 6 次冗余块传输。

1In practice, block boundaries need not align with physical stage boundaries. For example, in Fig. 3, each block spans two physical stages, so only every other transition involves a newly completed block.  
在实践中，区块边界无需与物理阶段边界对齐。例如，在图 3 中，每个区块跨越两个物理阶段，因此只有每隔一次转换才涉及一个新完成的区块。

6

第 6 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

Algorithm 1: Two-phase computation for block n  
算法 1：块 n 的双阶段计算

Input: Pseudo queries {wl​}l∈Bn​​ , block representations {b0​,…,bn−1​} /* Phase 1: Parallel inter-block attention */ Q ←[wl​]l∈Bn​​ // [S,d] K,V ←[b0​;…;bn−1​] // [n,d] {ol(1)​,ml(1)​,ℓl(1)​}l∈Bn​​← ATTNWITHSTATS(Q,K,V) // Return LSE  
输入：伪查询 {wl​}l∈Bn​​ ，块表示 {b0​,…,bn−1​} /* 阶段 1：并行块间注意力 */ Q ←[wl​]l∈Bn​​ // [S,d] K,V ←[b0​;…;bn−1​] // [n,d] {ol(1)​,ml(1)​,ℓl(1)​}l∈Bn​​← 带统计的注意力计算(Q,K,V) // 返回 LSE  
4 /* Phase 2: Sequential intra-block attention + Online softmax merge */  
4 /* 阶段 2：顺序块内注意力 + 在线 softmax 合并 */  
5 i ←0 6 for l∈Bn​ do if i=0 then hl​←ol(1)​/ℓl(1)​​​//​ Inter-block only else  
5 i ←0 6 对于 l∈Bn​ 执行 如果 i=0 那么 hl​←ol(1)​/ℓl(1)​​​//​ 仅块间否则  
10 ol(2)​,ml(2)​,ℓl(2)​​←ATTNWITHSTATS(wl​,bni​,bni​)​//​ Intra-block  10 ol(2)​,ml(2)​,ℓl(2)​​←ATTNWITHSTATS(wl​,bni​,bni​)​//​ 块内  
11 ml​←max(ml(1)​,ml(2)​) 12 \begin{array}{rlr}{\bf h}_l\gets \frac{e^{m_l^{(1)} - m_l}{\bf o}_l^{(1)} + e^{m_l^{(2)} - m_l}{\bf o}_l^{(2)}}{e^{m_l^{(1)} - m_l}\ell_l^{(1)} + e^{m_l^{(2)} - m_l}\ell_l^{(2)}}} & \mathrm{/ / }\end{array} Online softmax merge  
11 ml​←max(ml(1)​,ml(2)​) 12 \begin{array}{rlr}{\bf h}_l\gets \frac{e^{m_l^{(1)} - m_l}{\bf o}_l^{(1)} + e^{m_l^{(2)} - m_l}{\bf o}_l^{(2)}}{e^{m_l^{(1)} - m_l}\ell_l^{(1)} + e^{m_l^{(2)} - m_l}\ell_l^{(2)}}} & \mathrm{/ / }\end{array} 在线 Softmax 合并  
13 i←i+1 14 bni​←bni−1​+fl​(hl​) // Update partial sum; bn0​:=0 15 return {hl​}l∈Bn​​  
13 i←i+1 14 bni​←bni−1​+fl​(hl​) // 更新部分和； bn0​:=0 15 返回 {hl​}l∈Bn​​

Memory overhead. With cross-stage caching, each block is stored exactly once across all V virtual stages, which becomes negligible relative to standard per-layer activation cache. Crucially, the per-layer activation footprint remains identical to standard architectures, as activation checkpointing eliminates all inter-block attention intermediates, and the checkpointed input pl​ matches the memory size of the hidden state hl​ it replaces.  
内存开销。通过跨阶段缓存，每个块在所有 V 虚拟阶段中仅存储一次，相对于标准的逐层激活缓存而言变得微不足道。关键在于，逐层激活的内存占用与标准架构保持一致，因为激活检查点消除了所有块间注意力中间结果，且检查点输入 pl​ 的内存大小与其所替换的隐藏状态 hl​ 相匹配。

In terms of wall-clock time, Block AttnRes adds negligible training overhead when pipeline parallelism is not enabled; under pipeline parallelism, the measured end-to-end overhead is less than 4% .  
在挂钟时间方面，当未启用流水线并行时，Block AttnRes 增加的训练开销可忽略不计；在流水线并行下，实测端到端开销小于 4% 。

# 4.2 Inference  4.2 推理

The two-phase computation strategy described below applies to both Full and Block AttnRes: in either case, layers are grouped into blocks of size S , with Phase 1 batching the inter-block queries and Phase 2 handling sequential intra-block lookback. For Full AttnRes, this reduces per-layer I/O from O(Ld) to O((S+N)d) (detailed derivation shown in Appendix B); Block AttnRes further reduces the stored representations from L to N , since each block is compressed into a single vector. In what follows, we focus on Block AttnRes and detail the two-phase computation strategy together with a sequence-sharded prefilling scheme for long-context inputs.  
下文所述的两阶段计算策略同时适用于完整注意力残差（Full AttnRes）与分块注意力残差（Block AttnRes）：无论采用哪种方式，网络层均按 S 的规模分组为块，第一阶段批量处理块间查询，第二阶段则按序处理块内回溯查询。对于完整注意力残差，该策略将每层 I/O 从 O(Ld) 降至 O((S+N)d) （详细推导见附录 B）；而分块注意力残差通过将每个块压缩为单个向量，进一步将存储表征从 L 缩减至 N 。接下来我们将聚焦于分块注意力残差，详细阐述其两阶段计算策略，并针对长上下文输入提出序列分片预填充方案。

Two-phase computation strategy. The layer-wise attention computation of Block AttnRes resembles autoregressive decoding, where block representations serve as a shared KV cache reused across layers. A naïve implementation computes the attention residual at every layer, each requiring a full pass over all preceding blocks, resulting in O(L⋅N) memory accesses. Since the pseudo-query vectors are decoupled from the forward computation (§3), all S=L/N queries within a block can be batched into a single matrix multiplication, amortizing memory access from S reads to 1.  
两阶段计算策略。Block AttnRes 的逐层注意力计算类似于自回归解码，其中块表示作为跨层复用的共享 KV 缓存。一种简单实现是在每一层计算注意力残差，每层都需要对所有前序块进行完整遍历，导致 O(L⋅N) 次内存访问。由于伪查询向量与正向计算解耦（§3），一个块内的所有 S=L/N 查询可以批量处理为单个矩阵乘法，将内存访问从 S 次读取摊销为 1 次。

Algorithm 1 instantiates a two-phase computation strategy exploiting this property.  
算法 1 利用这一特性实例化了一个两阶段计算策略。

• Phase 1 computes inter-block attention for all S layers simultaneously via a single batched query against the cached block representations, returning both outputs and softmax statistics (max and log-sum-exp). This amortizes the memory access cost, reducing reads from S times to just once per block.  
• 第一阶段通过单次批处理查询计算所有 S 层的块间注意力，同时访问缓存的块表示，返回输出结果及 softmax 统计量（最大值与对数求和指数）。这一操作平摊了内存访问开销，将读取次数从每块 S 次降至仅一次。

• Phase 2 computes intra-block attention sequentially for each layer using the evolving partial sum, then merges with Phase 1 outputs through online softmax [31]. Because the online-softmax merge is elementwise, this phase naturally admits kernel fusion with surrounding operations, further reducing I/O overhead.  
• 第二阶段利用演化的部分和，为每个层顺序计算块内注意力，然后通过在线 softmax [31] 与第一阶段输出合并。由于在线 softmax 合并是逐元素进行的，此阶段自然允许与周围操作进行内核融合，进一步减少 I/O 开销。

With the two-phase design, Phase 2 preserves an I/O footprint similar to that of standard residual connections, whereas the main additional cost arises from Phase 1 inter-block attention. Because these inter-block reads are amortized across  
通过两阶段设计，第二阶段保持了与标准残差连接相似的 I/O 占用，而主要额外成本来自第一阶段块间注意力机制。由于这些块间读取操作被分摊到

7

第 7 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

all layers in a block through batching, the total per-layer memory access cost remains only (SN​+3)d reads and 2d writes (Table 1). This is substantially lower than the residual-stream I/O of prior residual generalizations such as (m)HC under typical settings. In practice, Phase 1 can also partially overlap with the computation of the first layer in the block, further reducing its wall-clock impact. As a result, the end-to-end inference latency overhead is less than 2% on typical inference workloads.  
通过批处理处理块中的所有层，每层的总内存访问成本仅为 (SN​+3)d 次读取和 2d 次写入（表 1）。这显著低于先前残差泛化方法（如 (m)HC ）在典型设置下的残差流 I/O。实际上，阶段 1 也可以与块中第一层的计算部分重叠，进一步减少其实际时间影响。因此，在典型的推理工作负载中，端到端推理延迟开销小于 2% 。

Table 1: Memory access cost per token per layer incurred by the residual mechanism under each scheme. The internal I/O of the layer function fl​ is excluded. For AttnRes, both Full and Block variants use the two-phase inference schedule described in Appendix B; amortized costs are averaged over N layers within a block. Typical values: L=128 , N=8 , S=L/N=16 , m=4 .  
表 1：每种方案下残差机制每层每个令牌的内存访问成本。层函数 fl​ 的内部 I/O 未计入。对于 AttnRes，完整版和块版均使用附录 B 中描述的两阶段推理调度；摊销成本按块内 N 层平均计算。典型值： L=128 、 N=8 、 S=L/N=16 、 m=4 。

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
||   |Operation  操作|Read  读取|Write  写入|Total I/O  总输入/输出|   |
|Symbolic  符号化|Typical  典型|
|Standard Residuals  标准残差|   |Residual Merge  残差合并|2d  二维|d|3d  三维|3d  3 天|
|mHC (m streams)  mHC（m 个流）|   |Compute αl, βl, A1  计算αl、βl、A1|md|m2+2m|||
|Apply αl  应用αl|md+m|d|(8m+2)d+2m2+4m|34d  34 天|
|Apply βl  应用 βl|d+m|md|
|Apply A1  应用 A1|md+m2|md|
|Residual Merge  残差合并|2md|md|
|AttnRes  注意力残差|Full  完整|Phase 1 (amortized)  第一阶段（摊销）|(N-1)d|d|(S+N)d|24d  24 天|
|Phase 2  第二阶段|(S-1)d  (S-1)天|d|
|Block  区块|Phase 1 (amortized)  阶段 1（摊销）|N/Sd|d|(N/S+5)d|5.5d  5.5 天|
|Phase 2  第二阶段|3d  3 天|d|

Memory-efficient prefilling. Storing block representations during prefilling requires N⋅T⋅d elements, which incurs 15 GB of memory for a 128K-token sequence with 8 blocks. We mitigate this by sharding these representations along the sequence dimension across P tensor-parallel devices, allowing Phase 1 to execute independently on local sequence shards. The Phase 2 online-softmax merge then integrates into the standard TP all-reduce communication path: the output is reduce-scattered, merged locally, and reconstructed via all-gather, naturally admitting kernel fusion with operations like RMSNorm. This reduces the per-device memory footprint to N⋅(T/P)⋅d —lowering the 128K-context example from 15 GB to roughly 1.9 GB per device. Combined with chunked prefill (e.g., 16K chunk size), the overhead further reduces to under 0.3 GB per device.  
内存高效的预填充。在预填充过程中存储块表示需要 N⋅T⋅d 个元素，对于一个包含 8 个块的 128K 令牌序列，这将占用 15 GB 内存。我们通过将这些表示沿序列维度分片到 P 个张量并行设备上来缓解此问题，使得第一阶段可以在本地序列分片上独立执行。随后，第二阶段在线 softmax 合并会集成到标准的 TP 全归约通信路径中：输出经过归约分散、本地合并，并通过全收集重建，自然地与 RMSNorm 等操作进行内核融合。这将每个设备的内存占用减少到 N⋅(T/P)⋅d ——将 128K 上下文示例从 15 GB 降低到每个设备约 1.9 GB。结合分块预填充（例如，16K 块大小），开销进一步降低到每个设备 0.3 GB 以下。

# 5 Experiments  5 实验

Architecture Details. Our architecture is identical to Kimi Linear [69], a Mixture-of-Experts (MoE) Transformer following the Moonlight [28] / DeepSeek-V3 [9] design, which interleaves Kimi Delta Attention (KDA) and Multi-Head Latent Attention (MLA) layers in a 3:1 ratio, each followed by an MoE feed-forward layer. The only modification is the addition of AttnRes to the residual connections; all other components (model depth, hidden dimensions, expert routing, and MLP structure) remain unchanged. AttnRes introduces only one RMSNorm and one pseudo-query vector wl​∈Rd per layer, amounting to a negligible fraction of the total parameter count. Crucially, all pseudo-query vectors must be initialized to zero. This ensures that the initial attention weights αi→l​ are uniform across source layers, which reduces AttnRes to an equal-weight average at the start of training and prevents training volatility, as we validated empirically.  
架构细节。我们的架构与 Kimi Linear [69]完全相同，这是一个遵循 Moonlight [28]/DeepSeek-V3 [9]设计的混合专家（MoE）Transformer，它以 3:1 的比例交错排列 Kimi Delta Attention（KDA）层和多头潜在注意力（MLA）层，每一层后面都跟着一个 MoE 前馈层。唯一的修改是在残差连接中加入了 AttnRes；所有其他组件（模型深度、隐藏维度、专家路由和 MLP 结构）保持不变。AttnRes 每层仅引入一个 RMSNorm 和一个伪查询向量 wl​∈Rd ，占总参数量的比例微乎其微。关键的是，所有伪查询向量必须初始化为零。这确保了初始注意力权重 αi→l​ 在源层之间是均匀的，从而在训练开始时将 AttnRes 简化为等权重平均，并防止训练波动，这一点我们已通过实验验证。

# 5.1 Scaling Laws  5.1 缩放定律

We sweep five model sizes (Table 2) and train three variants per size: a PreNorm baseline, Full AttnRes, and Block AttnRes with ≈8 blocks. They are trained with an 8192-token context window and a cosine learning rate schedule. Within each scaling law size group, all variants share identical hyperparameters selected under the baseline to ensure fair comparison; this setup intentionally favors the baseline and thus makes the comparison conservative. Following standard practice, we fit power-law curves of the form L=A×C−α [22, 15], where L is validation loss and C is compute measured in PFLOP/s-days.  
我们测试了五种模型规模（表 2），并为每种规模训练了三种变体：PreNorm 基线、Full AttnRes 以及包含 ≈8 个块的 Block AttnRes。所有模型均采用 8192 个标记的上下文窗口和余弦学习率调度进行训练。在每个规模扩展定律组内，所有变体共享基线模型下选定的相同超参数，以确保公平比较；这种设置有意偏向基线模型，从而使比较结果更为保守。遵循标准实践，我们拟合了形式为 L=A×C−α 的幂律曲线[22, 15]，其中 L 代表验证损失， C 代表以 PFLOP/s-天为单位的计算量。

Scaling Behavior. Fig. 4 presents the fitted scaling curves. The Baseline follows L=1.891×C−0.057 , while Block AttnRes fits L=1.870ˉ×Cˉ−0.058 , and Full AttnRes fits L=1.865×C−0.057 . All three variants exhibit a similar slope, but AttnRes consistently achieves lower loss across the entire compute range. Based on the fitted curves, at 5.6  
缩放行为。图 4 展示了拟合的缩放曲线。基线遵循 L=1.891×C−0.057 ，而块注意力残差拟合 L=1.870ˉ×Cˉ−0.058 ，全注意力残差拟合 L=1.865×C−0.057 。所有三种变体都表现出相似的斜率，但注意力残差在整个计算范围内始终实现更低的损失。根据拟合曲线，在 5.6

8

第 8 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

Table 2: Baseline vs Block AttnRes N=8 ) vs Full AttnRes vs mHC(-lite) [64]: Model configurations, Hyperparameters, and Validation Loss.  
表 2：基线 vs 块注意力残差 N=8 vs 完整注意力残差 vs mHC(-lite) [64]：模型配置、超参数和验证损失。

|   |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|# Act. Params†  # 激活参数†|Tokens  词元|Lb|H|dmodel  模型维度|df  数据帧|lr  学习率|batch size‡  批次大小‡|Val. Loss  验证损失|   |   |   |
|Baseline  基线|Block AttnRes  块注意力残差|Full AttnRes  全注意力残差|mHC(-lite)|
|194M|38.7B|12|12|896|400|2.99 × 10-3  2.99 × 10⁻³|192|1.931|1.909|1.899|1.906|
|241M|45.4B|13|13|960|432|2.80 × 10-3  2.80 × 10⁻³|256|1.895|1.875|1.874|1.869|
|296M|62.1B|14|14|1024|464|2.50 × 10-3  2.50 × 10⁻³|320|1.829|1.809|1.804|1.807|
|436M|87.9B|16|16|1168|528|2.20 × 10-3  2.20 × 10⁻³|384|1.766|1.746|1.737|1.747|
|528M|119.0B|17|17|1264|560|2.02 × 10-3|432|1.719|1.693|1.692|1.694|

† Denotes the number of activated parameters in our MoE models, excluding embeddings.  
† 表示我们 MoE 模型中激活的参数数量，不包括嵌入层。

‡ All models were trained with a context length of 8192.  
‡ 所有模型均以 8192 的上下文长度进行训练。

⋆ Lb​=L/2 denotes the number of Transformer blocks.  
⋆ Lb​=L/2 表示 Transformer 块的数量。

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/290b799452028e18c4066d679b8f3f2bf69a7175de3f8d6222581dc95917e610.jpg)

Figure 4: Scaling law curves for Attention Residuals. Both Full and Block AttnRes consistently outperform the baseline across all scales. Block AttnRes closely tracks Full AttnRes, recovering most of the gain at the largest scale.  
图 4：注意力残差的缩放定律曲线。在所有规模上，完整注意力残差和分块注意力残差均持续优于基线。分块注意力残差与完整注意力残差表现高度一致，在最大规模下恢复了大部分增益。

PFLOP/s-days, Block AttnRes reaches 1.692 versus the Baseline’s 1.714, equivalent to a 1.25× compute advantage. The gap between Full and Block AttnRes narrows with scale, shrinking to just 0.001 at the largest size. We also list mHC(-lite) [64] in Table 2 for reference. Full AttnRes outperforms mHC, while Block AttnRes matches it at lower memory I/O per layer: 5.5d versus 34d for mHC with m=4 streams (Table 1).  
PFLOP/s-days，Block AttnRes 达到 1.692，而 Baseline 为 1.714，相当于 1.25× 的计算优势。Full 和 Block AttnRes 之间的差距随规模扩大而缩小，在最大规模时缩小至仅 0.001。我们还在表 2 中列出了 mHC(-lite) [64]以供参考。Full AttnRes 优于 mHC，而 Block AttnRes 在每层内存 I/O 较低的情况下与之相当： 5.5d 对比 mHC 的 34d （使用 m=4 流，见表 1）。

# 5.2 Main Results  5.2 主要结果

Training recipe. The largest models we study are based on the full Kimi Linear 48B configuration: 27 Transformer blocks (54 layers) with 8 out of 256 routed experts plus 1 shared expert, yielding 48B total and 3B activated parameters. This model applies Block AttnRes with 6 layers per block, producing 9 blocks plus the token embedding for a total of 10 depth-wise sources.  
训练方案。我们研究的最大模型基于完整的 Kimi Linear 48B 配置：27 个 Transformer 块（54 层），其中 256 个路由专家中的 8 个加上 1 个共享专家，总计 48B 参数和 3B 激活参数。该模型应用 Block AttnRes，每块 6 层，产生 9 个块加上词嵌入，总计 10 个深度方向源。

We follow the same data and training recipe as the Kimi Linear 1.4T-token runs [69]: all models are pre-trained with a 4096-token context window, the Muon optimizer [28], and a WSD (Warmup–Stable–Decay) learning rate schedule [16], with a global batch size of 8M tokens. Training of the final model proceeds in two stages: (i) a WSD pre-training phase on 1T tokens, followed by (ii) a mid-training phase on ≈400B high-quality tokens, following the annealing recipe of Moonlight [28].  
我们遵循与 Kimi Linear 1.4T-token 运行[69]相同的数据和训练方案：所有模型均使用 4096-token 上下文窗口、Muon 优化器[28]以及 WSD（预热-稳定-衰减）学习率调度[16]进行预训练，全局批处理大小为 800 万 token。最终模型的训练分为两个阶段：(i) 在 1T token 上进行 WSD 预训练阶段，随后(ii) 按照 Moonlight[28]的退火方案，在 ≈400B 高质量 token 上进行中期训练阶段。

After mid-training, we continue training with progressively longer sequence length of 32K tokens. Since our architecture uses hybrid KDA/MLA attention [69], where MLA operates without positional encodings (NoPE) [61], context extension requires no modifications such as YaRN [37] or attention temperature rescaling.  
在中期训练后，我们继续使用逐步增长的 32K 令牌序列长度进行训练。由于我们的架构采用了混合 KDA/MLA 注意力机制[69]，其中 MLA 无需位置编码（NoPE）即可运行[61]，因此上下文扩展无需进行诸如 YaRN[37]或注意力温度重新缩放等修改。

9

第 9 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

(a) Validation Loss  (a) 验证损失

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/63b5202f80a075c6fee0c17396ca598886d6ffb2beb21ae1f76af076ed6710d5.jpg)

(b) Output Magnitude  (b) 输出幅度

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/7832f6f4db276db404f982373cb32ab490e1dd04b470f1ac29fd3e6e1456e370.jpg)

(c) Gradient Magnitude (×10−5  
(c) 梯度幅度 (×10−5

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/6b903f56ca6531592f9f7c5554093ed8c8f955c3e4bb9c37ca12c261108ecf0a.jpg)

Figure 5: Training dynamics of Baseline and Block AttnRes. (a) Validation loss during training. (b) Each transformer block’s output magnitude at the end of training. (c) Each transformer block’s gradient magnitude.  
图 5：基线模型与块注意力残差模型的训练动态。(a) 训练过程中的验证损失。(b) 训练结束时各 Transformer 块的输出幅度。(c) 各 Transformer 块的梯度幅度。

Training dynamics. We compare the training dynamics of our final Baseline and Block AttnRes models over 1T tokens in Fig. 5.  
训练动态。我们在图 5 中比较了最终基线模型和 Block AttnRes 模型在 1T 标记上的训练动态。

• Validation loss: AttnRes achieves consistently lower validation loss throughout training, with the gap widening during the decay phase and resulting in a notably lower final loss.  
• 验证损失：在整个训练过程中，AttnRes 始终保持着更低的验证损失，这一差距在衰减阶段进一步扩大，最终实现了显著更低的最终损失。

• Output magnitude: The Baseline suffers from the PreNorm dilution problem [60, 27]: as hidden-state magnitudes grow monotonically with depth, deeper layers are compelled to learn increasingly large outputs from fixed-scale normalized inputs to remain influential. Block AttnRes confines this growth within each block, as selective aggregation at block boundaries resets the accumulation, yielding a bounded periodic pattern.  
• 输出幅度：基线模型存在 PreNorm 稀释问题[60, 27]：随着隐藏状态幅度随深度单调增长，深层网络被迫从固定尺度的归一化输入中学习越来越大的输出以保持影响力。块注意力残差将这种增长限制在每个块内，因为块边界的选择性聚合会重置累积效应，从而产生有界的周期性模式。

• Gradient magnitude: With all residual weights fixed to 1, the Baseline provides no means of regulating gradient flow across depth, leading to disproportionately large gradients in the earliest layers. The learnable softmax weights in Block AttnRes (Fig. 8) introduce competition among sources for probability mass, resulting in a substantially more uniform gradient distribution.  
• 梯度幅度：当所有残差权重固定为 1 时，基线模型无法调节跨深度的梯度流动，导致最浅层出现不成比例的大梯度。块注意力残差中的可学习 softmax 权重（图 8）在多个源之间引入概率质量的竞争，从而产生显著更均匀的梯度分布。

Table 3: Performance comparison of AttnRes with the baseline, both after the same pre-training recipe. Best per-row results are bolded.  
表 3：注意力残差与基线模型在相同预训练方案下的性能对比。每行最佳结果已加粗标注。

|   |   |   |   |
|---|---|---|---|
|||Baseline  基线|AttnRes  注意力残差|
|General  通用|MMLU|73.5|74.6|
|MMLU-Pro  MMLU 专业版|52.2|52.2|
|GPQA-Diamond  GPQA 钻石版|36.9|44.4|
|BBH|76.3|78.0|
|ARC-Challenge  ARC 挑战|64.6|65.7|
|HellaSwag  地狱级难度|83.2|83.4|
|TriviaQA  冷知识问答|69.9|71.8|
|Math & Code  数学与编程|GSM8K|81.7|82.4|
|MGSM|64.9|66.1|
|Math  数学|53.5|57.1|
|CMath|84.7|85.1|
|HumanEval|59.1|62.2|
|MBPP|72.0|73.9|
|Chinese  中文|CMMLU|82.0|82.9|
|C-Eval|79.6|82.5|

Downstream performance. Following the evaluation protocol of Kimi Linear [69], we assess both models across three areas (Table 3):  
下游性能表现。遵循 Kimi Linear [69]的评估协议，我们在三个领域对两种模型进行了评估（表 3）：

10

第 10 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

Table 4: Ablation on key components of AttnRes (16-layer model).  
表 4：AttnRes 关键组件的消融实验（16 层模型）。

|   |   |   |
|---|---|---|
|Variant  变体|   |Loss  损失|
|Baseline (PreNorm)  基线（预归一化）|   |1.766|
|DenseFormer [36]|   |1.767|
|mHC [59]|   |1.747|
|AttnRes  注意力残差|Full  完整|1.737|
||w/ input-dependent query  带输入相关查询|1.731|
||w/ input-independent mixing  <br>采用输入无关的混合方式|1.749|
||w/ sigmoid  使用 sigmoid 函数|1.741|
||w/o RMSNorm  无 RMSNorm|1.743|
||SWA (W = 1 + 8)|1.764|
||Block (S = 4)  块 (S = 4)|1.746|
||w/ multihead (H = 16)  <br>带多头注意力 (H = 16)|1.752|
||w/o RMSNorm  不带 RMSNorm|1.750|

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/473cd1159dd2c8fb18c41e0ce36e26823bc84c82484cd54631234492e1335e43.jpg)

Figure 6: Effect of block size on validation loss (16-layer model).  
图 6：块大小对验证损失的影响（16 层模型）。

• Language understanding and reasoning: MMLU [13], MMLU-Pro Hard [55], GPQA-Diamond [41], BBH [48], ARC-Challenge [6], HellaSwag [65], and TriviaQA [21].  
• 语言理解与推理：MMLU [13]、MMLU-Pro Hard [55]、GPQA-Diamond [41]、BBH [48]、ARC-Challenge [6]、HellaSwag [65] 以及 TriviaQA [21]。

• Reasoning (Code and Math): GSM8K [7], MGSM [44], Math [25], CMath [14], HumanEval [5], and MBPP [1].  
• 推理（代码与数学）：GSM8K [7]、MGSM [44]、Math [25]、CMath [14]、HumanEval [5] 和 MBPP [1]。

• Chinese language understanding: CMMLU [26] and C-Eval [19].  
• 中文理解能力：CMMLU [26] 与 C-Eval [19]。

As shown in Table 3, Block AttnRes matches or outperforms the baseline on all benchmarks. The improvements are particularly pronounced on multi-step reasoning tasks such as GPQA-Diamond (+7.5) and Minerva Math (+3.6) , as well as code generation such as HumanEval (+3.1) , while knowledge-oriented benchmarks such as MMLU (+1.1) and TriviaQA (+1.9) also show solid gains. This pattern is consistent with the hypothesis that improved depth-wise information flow benefits compositional tasks, where later layers can selectively retrieve and build upon earlier representations.  
如表 3 所示，Block AttnRes 在所有基准测试中均达到或超越了基线水平。改进效果在需要多步推理的任务（如 GPQA-Diamond (+7.5) 和 Minerva Math (+3.6) ）以及代码生成任务（如 HumanEval (+3.1) ）中尤为显著，同时面向知识的基准测试（如 MMLU (+1.1) 和 TriviaQA (+1.9) ）也展现出稳健的提升。这一模式与以下假设相符：增强的深度信息流有利于组合型任务，使后续层能够有选择地检索并基于早期表征进行构建。

# 5.3 Ablation Study  5.3 消融研究

We conduct ablation studies on the 16-head model from Table 2 to validate key design choices in AttnRes (Table 4). All models share identical hyperparameters and compute budget.  
我们对表 2 中的 16 头模型进行了消融研究，以验证 AttnRes 中关键设计选择的有效性（表 4）。所有模型均采用相同的超参数和计算预算。

Comparison with prior methods. We compare AttnRes against the PreNorm baseline (loss 1.766) and two representative methods that generalize residual connections. DenseFormer [36] grants each layer access to all previous outputs but combines them with fixed, input-independent scalar coefficients; it shows no gain over the baseline (1.767), highlighting the importance of input-dependent weighting. mHC [59] introduces input dependence through m parallel streams with learned mixing matrices, improving to 1.747. AttnRes takes this further with explicit content-dependent selection via softmax attention: Full AttnRes achieves 1.737 and Block AttnRes 1.746, outperforming both methods with only a single query vector per layer.  
与先前方法的比较。我们将 AttnRes 与 PreNorm 基线（损失值 1.766）以及两种具有代表性的残差连接泛化方法进行对比。DenseFormer [36]允许每一层访问所有先前输出，但使用固定的、与输入无关的标量系数进行组合；该方法未显示出相对于基线的改进（1.767），突显了输入依赖性加权的重要性。mHC [59]通过 m 并行流引入输入依赖性，并采用学习得到的混合矩阵，将损失值提升至 1.747。AttnRes 通过基于 softmax 注意力的显式内容依赖性选择进一步推进：完整版 AttnRes 达到 1.737，分块版 AttnRes 达到 1.746，在每层仅使用单个查询向量的情况下超越了这两种方法。

Cross-layer access. We compare three granularities of cross-layer access. Full AttnRes follows directly from the time–depth duality (§ 3), applying attention over all previous layers, and achieves the lowest loss (1.737). A simple way to reduce its memory cost is sliding-window aggregation (SWA), which retains only the most recent W=8 layer outputs plus the token embedding; it improves over baseline (1.764) but falls well short of both Full and Block AttnRes, suggesting that selectively accessing distant layers matters more than attending to many nearby ones.  
跨层访问。我们比较了三种粒度的跨层访问方式。完全注意力残差直接源自时间-深度对偶性（§3），对所有先前层应用注意力，实现了最低损失（1.737）。降低其内存成本的一种简单方法是滑动窗口聚合，仅保留最近的 W=8 层输出加上词元嵌入；它相比基线（1.764）有所改进，但远不及完全和块注意力残差，这表明选择性访问远层比关注多个近层更为重要。

Block AttnRes offers a better trade-off: with block size S=4 it reaches 1.746 while keeping memory overhead constant per layer. Fig. 6 sweeps S across the full spectrum from S=1 (i.e. Full AttnRes) to increasingly coarse groupings. Loss degrades gracefully as S grows, with S=2,4,8 all landing near 1.746 while larger blocks S=16,32 ) move toward baseline. In practice, we fix the number of blocks to ≈8 for infrastructure efficiency ( S4) . As future hardware alleviates memory capacity constraints, adopting finer-grained block sizes or Full AttnRes represents a natural pathway to further improve performance.  
块注意力残差提供了更好的权衡：当块大小为 S=4 时，其达到 1.746，同时保持每层内存开销恒定。图 6 在从 S （即全注意力残差）到逐渐粗化的分组的整个范围内扫描 S=1 。随着 S 的增长，损失逐渐增加， S=2,4,8 均落在 1.746 附近，而较大的块 S=16,32 则向基线靠拢。在实践中，我们固定块数为 ≈8 以提高基础设施效率 ( S4) 。随着未来硬件缓解内存容量限制，采用更细粒度的块大小或全注意力残差是进一步提高性能的自然途径。

11

第 11 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/47e4914083b9f537d3c3c278131100f7bd915ec1c6002eba24c54b815081a744.jpg)

(a) Baseline  (a) 基线

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/d5764ede39f272805d2900763e2f16cc737a60b740ece99a10d7fad44fd1d967.jpg)

(b) Attention Residuals  (b) 注意力残差

Figure 7: Architecture sweep under fixed compute ≈6.5×1019 FLOPs, ≈2.3×108 active parameters). Each cell reports validation loss for a (dmodel​/Lb​ , H/Lb​) configuration, where Lb​=L/2 is the number of Transformer blocks; the star marks the optimum.  
图 7：固定计算量下的架构扫描（ ≈6.5×1019 FLOPs， ≈2.3×108 激活参数）。每个单元格报告 (dmodel​/Lb​ 、 H/Lb​) 配置的验证损失，其中 Lb​=L/2 表示 Transformer 块的数量；星号标记最优配置。

Component design. We further ablate individual components of the attention mechanism:  
组件设计。我们进一步对注意力机制的各个组件进行消融研究：

• Input-dependent query. A natural extension is to make the query input-dependent by projecting it from the current hidden state. This further lowers loss to 1.731, but introduces a d×d projection per layer and requires sequential memory access during decoding, so we default to the learned query.  
• 输入依赖型查询。一个自然的扩展是通过从当前隐藏状态投影来使查询依赖于输入。这进一步将损失降低至 1.731，但每层引入了 d×d 投影，并在解码过程中需要顺序内存访问，因此我们默认采用学习型查询。

• Input-independent mixing. We removed the query and key and replaced them with learnable, input-independent scalars to weigh previous layers, which hurts performance (1.749 vs. 1.737).  
• 输入无关型混合。我们移除了查询和键，并用可学习的、与输入无关的标量来加权先前层，这损害了性能（1.749 对比 1.737）。

• softmax vs. sigmoid. Replacing softmax with sigmoid degrades performance (1.741). We attribute this to softmax’s competitive normalization, which forces sharper selection among sources.  
• softmax 对比 sigmoid。用 sigmoid 替换 softmax 会降低性能（1.741）。我们将此归因于 softmax 的竞争性归一化，它迫使在不同来源之间进行更尖锐的选择。

• Multihead attention. We test per-head depth aggregation H=16 on Block AttnRes, allowing different channel groups to attend to different source layers. This hurts performance (1.752 vs. 1.746), indicating that the optimal depth-wise mixture is largely uniform across channels: when a layer’s output is relevant, it is relevant as a whole.  
• 多头注意力。我们在 Block AttnRes 上测试了每头深度聚合 H=16 ，允许不同的通道组关注不同的源层。这损害了性能（1.752 对比 1.746），表明最优的深度混合在通道间基本是均匀的：当某一层的输出相关时，它作为一个整体都是相关的。

• RMSNorm on keys. Removing RMSNorm degrades both Full AttnRes (1.743) and Block AttnRes (1.750). For Full AttnRes, it prevents individual layers with naturally larger outputs from dominating the softmax. This becomes even more critical for Block AttnRes, as block-level representations accumulate over more layers and can develop large magnitude differences; RMSNorm prevents these from biasing the attention weights.  
• 对键向量应用 RMSNorm。移除 RMSNorm 会同时降低完整注意力残差（1.743）和分块注意力残差（1.750）的性能。对于完整注意力残差，它能防止自然输出值较大的单层主导 softmax 计算。这对分块注意力残差更为关键，因为分块级表征会在更多层中累积，可能产生巨大的量级差异；RMSNorm 能防止这些差异对注意力权重产生偏差。

# 5.4 Analysis  5.4 分析

# 5.4.1 Optimal Architecture  
5.4.1 最优架构

To understand how AttnRes reshapes optimal architectural scaling, we perform a controlled capacity reallocation study under a fixed compute and parameter budget. Our central question is whether AttnRes alters the preferred depth–width–attention trade-off, and in particular, given its potential strength on the depth dimension, whether it favors deeper models compared to conventional Transformer design heuristics. To isolate structural factors directly coupled to depth, we fix the per-expert MLP expansion ratio based on internal empirical observations (dff​/dmodel​≈⋅0.45⋅) ). We further fix total training compute (FLOPs≈6.5×1019) and active parameters (≈2.3×108) ), ensuring that any performance variation arises purely from architectural reallocation rather than overall capacity differences. Under this constrained budget, we enumerate 25 configurations on a 5×5 grid over dmodel​/Lb​∈⋅​{15,30,45,60,75} and H/Lb​∈{0.3,0.4,0.5ˉ,0.6,0.7} , where Lb​=L/2 is the number of Transformer blocks and H the number of attention heads. The results are shown in Fig. 7.  
为了理解 AttnRes 如何重塑最优架构的缩放规律，我们在固定的计算和参数预算下进行了一项受控容量再分配研究。我们的核心问题是：AttnRes 是否改变了深度、宽度与注意力之间的优选权衡关系？特别是考虑到其在深度维度上的潜在优势，与传统 Transformer 设计启发式方法相比，它是否更倾向于支持更深的模型？为了分离与深度直接相关的结构因素，我们基于内部经验观察固定了每个专家 MLP 的扩展比率（ (dff​/dmodel​≈⋅0.45⋅) ）。我们进一步固定了总训练计算量（ (FLOPs≈6.5×1019) ）和激活参数数量（ (≈2.3×108) ），确保任何性能变化纯粹源于架构再分配，而非整体容量差异。在此约束预算下，我们在 5×5 网格上枚举了 25 种配置，网格参数为 dmodel​/Lb​∈⋅​{15,30,45,60,75} 和 H/Lb​∈{0.3,0.4,0.5ˉ,0.6,0.7} ，其中 Lb​=L/2 表示 Transformer 块的数量， H 表示注意力头的数量。结果如图 7 所示。

Both heatmaps exhibit a shared pattern: loss decreases with growing dmodel​/Lb​ and shrinking H/Lb​ , and both methods reach their optima at H/Lb​≈0.3 . Despite this shared trend, AttnRes achieves a lower loss than the baseline in each of the 25 configurations, by 0.019–0.063. The most apparent difference lies in the location of the optimum: the baseline achieves its lowest loss at dmodel​/Lb​≈60 (1.847), whereas AttnRes shifts it to dmodel​/Lb​≈45 (1.802). Under a fixed  
两张热力图都展现出相同的模式：随着 dmodel​/Lb​ 增大和 H/Lb​ 减小，损失值逐渐降低，两种方法均在 H/Lb​≈0.3 处达到最优。尽管存在这一共同趋势，但在全部 25 种配置中，AttnRes 的损失值始终低于基线方法，差距在 0.019 至 0.063 之间。最显著的差异体现在最优解的位置：基线方法在 dmodel​/Lb​≈60 处取得最低损失值（1.847），而 AttnRes 将其转移至 dmodel​/Lb​≈45 处（1.802）。在固定

12

第 12 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/118a68c8856eebbd92224569a1fa0172f3429e0b4ee5594d4964ea81137cfcb1.jpg)

Figure 8: Depth-wise attention weight distributions for a 16-head model with full (top) and block (bottom) Attention Residuals, averaged over tokens. The model has 16 attention and 16 MLP layers. Each row shows how the lth attention (left) or MLP (right) layer distributes weight over previous sources. Diagonal dominance indicates locality remains the primary information pathway, while persistent weights on source 0 (embedding) and occasional off-diagonal concentrations reveal learned skip connections. Block attention N=8 ) recovers the essential structure with sharper, more decisive weight distributions.  
图 8：采用完整（上）和分块（下）注意力残差的 16 头模型深度注意力权重分布，按词元平均。该模型包含 16 个注意力层和 16 个 MLP 层。每行展示第 l 个注意力层（左）或 MLP 层（右）如何将权重分配到先前的源上。对角线主导表明局部性仍是主要信息通路，而源 0（嵌入层）的持续权重及偶尔出现的非对角线集中则揭示了学习到的跳跃连接。分块注意力 N=8 以更清晰、更确定的权重分布恢复了基本结构。

parameter budget, a lower dmodel​/Lb​ corresponds to a deeper, narrower network, suggesting that AttnRes can exploit additional depth more effectively. We note that this preference for depth does not directly translate to a deployment recommendation, as deeper models generally incur higher inference latency due to their sequential computation [39]. Rather, this sweep serves as a diagnostic that reveals where AttnRes benefits most, and this depth preference can be factored into the architecture selection alongside inference cost.  
在参数预算固定的情况下，较低的 dmodel​/Lb​ 值对应着更深、更窄的网络结构，这表明 AttnRes 能够更有效地利用额外的深度。需要指出的是，这种对深度的偏好并不直接转化为部署建议，因为更深的模型通常由于其顺序计算特性会导致更高的推理延迟[39]。相反，这种参数扫描可作为一种诊断手段，揭示 AttnRes 在哪些方面获益最大，而这种深度偏好可以与推理成本一同纳入架构选择的考量因素。

# 5.4.2 Analyzing Learned AttnRes Patterns  
5.4.2 分析已学习的注意力残差模式

We visualize the learned weights αi→l​ in Fig. 8 for the 16-head model (from Table 2) with both full and block ( N=8) ) AttnRes. Each heatmap shows how the lth attention or MLP layer (rows) allocates its attention over previous sources (columns), with pre-attention and pre-MLP layers shown separately. We highlight three key observations:  
我们在图 8 中可视化了 16 头模型（来自表 2）在完整和分块注意力残差（ N=8) ）设置下学习到的权重 αi→l​ 。每个热力图展示了第 l 层注意力或 MLP 层（行）如何在前序来源（列）上分配注意力，其中注意力层前和 MLP 层前的可视化结果分别呈现。我们重点突出三个关键观察结果：

• Preserved locality. Each layer attends most strongly to its immediate predecessor, yet selective off-diagonal concentrations emerge (e.g., layer 4 attending to early sources, layers 15–16 reaching back under the block setting), indicating learned skip connections beyond the standard residual path.  
• 保持局部性。每一层主要关注其直接前驱层，但出现了选择性非对角集中现象（例如第 4 层关注早期源层，第 15-16 层在块设置下向后延伸），这表明学习到了超越标准残差路径的跳跃连接。

• Layer specialization. The embedding h1​ retains non-trivial weight throughout, especially in pre-attention layers. Pre-MLP inputs show sharper diagonal reliance on recent representations, while pre-attention inputs maintain broader receptive fields, consistent with attention routing information across layers and MLPs operating locally.  
• 层间专业化。嵌入表示 h1​ 在整个过程中保持显著权重，特别是在注意力层之前。MLP 层前的输入对近期表征呈现更明显的对角线依赖特征，而注意力层前的输入则保持更广泛的感受野，这与注意力机制跨层路由信息、MLP 层局部运算的特性相符。

• Block AttnRes preserves structure. Diagonal dominance, embedding persistence, and layer specialization all transfer from the full to the block variant, suggesting that block-wise compression acts as implicit regularization while preserving the essential information pathways.  
• 分块注意力残差结构保持原有特性。对角线主导性、嵌入持久性和层间专业化特征均从完整模型延续至分块变体，表明分块压缩在保留核心信息通路的同时，起到了隐式正则化的作用。

13

第 13 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

Table 5: Comparison of residual update mechanisms. Weight: whether the mixing coefficients are architecture-fixed, learned-static (fixed after training), or input-dependent (dynamic). Source: which earlier representations layer l can access. Normalization is omitted from most formulas for clarity.  
表 5：残差更新机制对比。权重：混合系数是否为架构固定、学习静态（训练后固定）或输入相关（动态）。来源：第 l 层可访问的早期表征。为清晰起见，大多数公式中省略了归一化处理。

|   |   |   |   |
|---|---|---|---|
|Method  方法|Update rule  更新规则|Weight  权重|Source  来源|
|Single-state recurrence: layer l receives only hl-1  <br>单状态递归：第 l 层仅接收 hl-1|   |   |   |
|Residual [12]  残差 [12]|hl=hl-1+f1-1(hl-1)|Fixed  固定|hl-1|
|ReZero [2]|hl=hl-1+αl·fl-1(hl-1)|Static  静态|hl-1|
|LayerScale [50]  层缩放 [50]|hl=hl-1+diag(λl)·fl-1(hl-1)  <br>hl = hl-1 + diag(λl) · fl-1(hl-1)|Static  静态|hl-1|
|Highway [45]  高速公路 [45]|hl=(1-gl) ⊙ hl-1+gl ⊙ fl-1(hl-1)|Dynamic  动态|hl-1|
|DeepNorm [54]|hl=Norm(αhl-1+fl-1(hl-1))|Fixed  固定|hl-1|
|KEEL [4]|hl=Norm(αhl-1+fl-1(Norm(hl-1)))|Fixed  固定|hl-1|
|Multi-state recurrence: layer l receives m streams  <br>多状态循环：第 l 层接收 m 个流|   |   |   |
|SiameseNorm [27]|hl=Norm(h1-l+yl-1);hl=hl-1+yl-1|Fixed  固定|2 streams  2 个流|
|HC/mHC [72, 59]|Hl=Hl-1A l+fl-1(Hl-1αl-1)βl-1|Dynamic  动态|m streams  m 流|
|DDL [67]|Hl=(I-βlklkT)Hl-1+βlklvT|Dynamic  动态|dv streams  dv 流|
|Cross-layer access: layer l can access individual earlier-layer outputs  <br>跨层访问：第 l 层可以访问早期各层的单独输出|   |   |   |
|DenseNet [17]|hl=ConvPool([h1; f1(h1); ...; f1-1(h1-1)])|Static  静态|[hl, ..., hl-1]|
|DenseFormer [36]|hl=α0→l h1+∑i=1l-1αi→l fi(hi)|Static  静态|[hl, ..., hl-1]|
|MRLA [10]1|hl=∑i=1l-1σ(ConvPool(f1-1(h1-1)))Tσ(ConvPool(fi(hi)))Conv(fi(hi))|Dynamic  动态|[hl, ..., hl-1]|
|AttnRes (ours)|Full2|Dynamic  动态|[hl, ..., hl-1]|
|Block3  区块 3|Dynamic  动态|[b0, ..., bn-1, bnj]|

1 ConvPool: pooling operation followed by convolution (channel projection).  
1 ConvPool：池化操作后接卷积（通道投影）。

2ϕ(q,k)=exp⋅​(q⊤RMSNorm^(k)) ; ki​=vi​ ; v0​=h1​ , vi≥1​=fi​(hi​) . softmax jointly normalized over all sources.  
2ϕ(q,k)=exp⋅​(q⊤RMSNorm^(k)) ； ki​=vi​ ； v0​=h1​ ， vi≥1​=fi​(hi​) 。softmax 在所有源上联合归一化。

3 Same ϕ and normalization as Full; vi = bi, vnj​=bnj​  
3 与 Full 相同的 ϕ 和归一化；vi = bi， vnj​=bnj​

# 6 Discussions  6 讨论

# 6.1 Sequence-Depth Duality  
6.1 序列-深度对偶性

Residual connections propagate information over depth via a fixed recurrence hl​=hl−1​+fl−1​(hl−1​) , much as RNNs propagate information over time. Test-Time Training (TTT) [46] formalizes the sequence side of this analogy (cf. Fast Weight Programmers [43, 32]), casting each recurrent step as gradient descent on a self-supervised loss:  
残差连接通过固定的递归关系 hl​=hl−1​+fl−1​(hl−1​) 在深度维度上传播信息，这与循环神经网络在时间维度上传播信息的方式非常相似。测试时训练（TTT）[46] 形式化了这一类比中的序列侧（参见快速权重编程器[43, 32]），将每个循环步骤视为基于自监督损失的梯度下降过程。

Wt​=Wt−1​−η∇ℓ(Wt−1​;xt​),(9)

where a slow network parameterizes ℓ and the state W is updated once per token. When f is linear, this reduces to vanilla linear attention Sˉt​=St−1​+kt​vt⊤​​ . The standard residual exhibits the same additive form along depth, with hl​ serving as the state and each layer fl​ acting as one “gradient step.”  
其中缓慢网络参数化 ℓ ，状态 W 每处理一个标记更新一次。当 f 为线性时，这简化为经典的线性注意力 Sˉt​=St−1​+kt​vt⊤​​ 。标准残差沿深度呈现相同的加法形式， hl​ 作为状态，每个层 fl​ 充当一次“梯度步进”。

As noted by [4], this duality extends to richer variants (Table 5). Data-dependent gates on the sequence side [47, 63] correspond to Highway networks [45] on the depth side; the delta rule [42, 62, 69] corresponds to DDL [67]; and MRLA [10] mirrors GLA’s [63] gated linear attention. These methods all refine the recurrent update while remaining within the recurrence paradigm. AttnRes goes a step further and replaces depth-wise recurrence with direct cross-layer attention, just as Transformers replaced temporal recurrence with self-attention. Since the number of layers in current architectures remains well within the practical regime of softmax attention, we adopt vanilla depth-wise attention. Incorporating more expressive yet memory-efficient (e.g. linear-complexity) alternatives is a natural direction for future work.  
正如[4]所指出的，这种二元性延伸至更丰富的变体（表 5）。序列侧的数据依赖门控[47, 63]对应深度侧的高速网络[45]；增量规则[42, 62, 69]对应 DDL[67]；而 MRLA[10]则与 GLA[63]的门控线性注意力形成镜像。这些方法均在循环范式内优化了循环更新机制。AttnRes 更进一步，用直接的跨层注意力取代了深度方向的循环，正如 Transformer 用自注意力取代了时间循环。由于当前架构中的层数仍完全处于 softmax 注意力的实际可行范围内，我们采用了经典的深度方向注意力。融入更具表现力且内存高效（例如线性复杂度）的替代方案，是未来工作的自然方向。

# 6.2 Residual Connections as Structured Matrices  
6.2 残差连接作为结构化矩阵

The residual variants discussed above can all be viewed as weighted aggregations over previous layer outputs. We formalize this with a depth mixing matrix M∈RL×L , where Mil​ is the weight that layer l assigns to the output of layer i . The variants differ in how these weights arise (fixed, learned, or input-dependent) and whether M is constrained to low rank or allowed to be dense. The semiseparable rank of M [8] offers a unified lens for comparing them.  
上述讨论的残差变体均可视为对前一层输出的加权聚合。我们通过深度混合矩阵 M∈RL×L 对此进行形式化描述，其中 Mil​ 表示第 l 层分配给第 i 层输出的权重。这些变体的差异在于权重生成方式（固定、学习或输入相关）以及矩阵 M 是否被约束为低秩或允许稠密。矩阵 M 的半可分秩[8]为比较这些变体提供了统一视角。

Concretely, the input to layer l is hl​=∑i=0l−1​Mil​vi​​ , where v0​=h1​ (embedding) and vi​=fi​(hi​) for i≥1 . Fig. 9 visualizes M for representative methods; we derive each below.  
具体而言，第 l 层的输入为 hl​=∑i=0l−1​Mil​vi​​ ，其中 v0​=h1​ （嵌入）且 vi​=fi​(hi​) 适用于 i≥1 。图 9 展示了代表性方法的 M 可视化；下文将逐一推导。

14

第 14 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/6e6db72ff03c344ea15f420a51490aa581a0dee1589f9604a9eb089a9580869a.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/ce299f24274a750e3615a42b3fe986292ee3793fc7a0ebd642ba4cb72347bc23.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/065d8510c43840c696333f29bc36976affb9d8863aa93288a677015bd7fb342d.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2026-03-16/7e7cfa22-303e-428f-b9bf-5baa317f38db/531370a54fe93138180de1dd39350b2a90361f89b6124616896c67fe80ce660e.jpg)

Figure 9: Depth mixing matrices M for four residual variants L=4 ; Block AttnRes uses block size S=2 ). Highway is shown with scalar gates for clarity. AttnRes panels show unnormalized ϕ scores; background colors group entries that share the same source (Full AttnRes) or the same source block (Block AttnRes).  
图 9：四种残差变体的深度混合矩阵 M L=4 ；块注意力残差使用块大小 S=2 ）。为清晰起见，高速公路以标量门形式展示。注意力残差面板显示未归一化的 ϕ 分数；背景颜色将共享相同源（全注意力残差）或相同源块（块注意力残差）的条目分组。

• Standard residual [12], hl​=hl−1​+fl−1​(hl−1​) . Expanding gives hl​=∑i=0l−1​vi​​ , so Mi→l​=1 for all i<l and M is an all-ones lower-triangular matrix:  
• 标准残差[12]， hl​=hl−1​+fl−1​(hl−1​) 。展开得 hl​=∑i=0l−1​vi​​ ，因此对所有 i<l 有 Mi→l​=1 ，且 M 是一个全 1 的下三角矩阵：

​h1​h2​⋮hL​​​=​11⋮1​1⋮1​⋱…​1​​​v0​v1​⋮vL−1​​​

• Highway [45], hl​=(1−gl​)hl−1​+gl​fl−1​(hl−1​) (written here with scalar gates for clarity; the element-wise extension is straightforward). Defining the carry product γil×​:=∏j=i+1l​(1−gj​)​ , the weights are M0l​=γ1l×​ for the embedding and Mil​=gi+1​γi+1l×​ for i≥1 . Since the cumulative products factor through scalar gates, M is 1-semiseparable [8], the same rank as the standard residual but with input-dependent weights. The weights sum to one by construction, making Highway a softmax-free depth-wise instance of stick-breaking attention [49].  
• Highway [45]， hl​=(1−gl​)hl−1​+gl​fl−1​(hl−1​) （此处为清晰起见使用标量门表示；逐元素扩展是直接的）。定义进位乘积 γil×​:=∏j=i+1l​(1−gj​)​ ，嵌入的权重为 M0l​=γ1l×​ ， i≥1 的权重为 Mil​=gi+1​γi+1l×​ 。由于累积乘积通过标量门进行因子分解，M 是 1-半可分离的[8]，其秩与标准残差相同但具有输入依赖的权重。通过构造，权重总和为一，使得 Highway 成为无需 softmax 的深度方向 stick-breaking 注意力实例[49]。

• (m)HC [72, 59] maintain m parallel streams Hl​∈Rd×m , updated via  
• (m)HC [72, 59] 维持 m 条并行流 Hl​∈Rd×m ，通过以下方式更新：

Hl​=Hl−1​Al​+fl−1​(Hl−1​αl−1​)βl−1⊤​,

where Al​∈Rm×m is a learned transition matrix, αl−1​∈Rm mixes streams into a single input for fl−1​ , and βl−1​∈Rm distributes the output back across streams. Unrolling the recurrence gives the effective weight  
其中 Al​∈Rm×m 是学习到的转移矩阵， αl−1​∈Rm 将各流混合为 fl−1​ 的单一输入，而 βl−1​∈Rm 将输出重新分配至各流。展开递归关系即可得到有效权重。

Mi→l​=βi⊤​Ai+1→l×​αl​,(10)

where Aij×​:=∏k=i+1j​Ak​​ . The m×m transitions render M m -semiseparable [8]. mHC [59, 64] further constrains each Al​ to be doubly stochastic, stabilizing the cumulative products across depth.  
其中 Aij×​:=∏k=i+1j​Ak​​ 。 m×m 的转换使 M 呈现 m -半可分特性 [8]。mHC [59, 64] 进一步约束每个 Al​ 为双随机矩阵，从而稳定跨深度的累积乘积。

• Full AttnRes computes Mil​=αil​ via ϕ(wl​,ki​)=exp(wl⊤​RMSNorm(ki​)) with normalization, where ki​=vi​ are input-dependent layer outputs, yielding a dense, rank- L M.  
• Full AttnRes 通过 ϕ(wl​,ki​)=exp(wl⊤​RMSNorm(ki​)) 计算 Mil​=αil​ 并进行归一化，其中 ki​=vi​ 为输入相关的层输出，生成一个稠密的秩为 L 的矩阵 M。

• Block AttnRes partitions layers into N blocks B1​,…,BN​ . For sources i in a completed earlier block Bn​ , all share the block-level key/value bn​ , so Mil​=αnl​ for every i∈Bn​ . Within the current block, each layer additionally attends over the evolving partial sum bni−1​ , introducing one extra distinct source per intra-block position. The effective rank of M therefore lies between N and N+S (where S is the block size), interpolating between standard residual ( N=1 and Full AttnRes N=L) .  
• Block AttnRes 将层划分为 N 个块 B1​,…,BN​ 。对于已完成较早块 Bn​ 中的源 i ，所有源共享块级键/值 bn​ ，因此对于每个 i∈Bn​ ， Mil​=αnl​ 成立。在当前块内，每个层额外关注不断演化的部分和 bni−1​ ，为每个块内位置引入一个额外的独立源。因此，M 的有效秩介于 N 和 N+S 之间（其中 S 是块大小），在标准残差（ N=1 ）和完整 AttnRes（ N=L) ）之间进行插值。

Practicality. The structured-matrix perspective serves two purposes. First, it enables analytical insights that are not apparent from the recurrence form alone. The input-dependent M of AttnRes, for instance, reveals depth-wise attention sinks (§5.4.2), where certain layers consistently attract high weight regardless of input, mirroring the same phenomenon in sequence-wise attention [57]. Second, it informs new designs by exposing which properties of the kernel ϕ matter. For example, when ϕ decomposes as ϕ(q,k)=φ(q)⊤φ(k) for some feature map φ [23], depth-wise attention collapses into a recurrence—precisely the structure underlying the MRLA–GLA and DDL–DeltaNet correspondences noted above.  
实用性。结构化矩阵视角具有双重目的。首先，它能够提供仅从递归形式中无法获得的解析洞察。例如，AttnRes 中依赖于输入的 M 揭示了深度注意力汇聚现象（§5.4.2），即某些层无论输入如何都会持续吸引高权重，这与序列注意力中的相同现象相呼应[57]。其次，通过揭示核 ϕ 的哪些特性至关重要，它为新的设计提供了依据。例如，当 ϕ 可分解为某个特征映射 φ 的 ϕ(q,k)=φ(q)⊤φ(k) 时[23]，深度注意力便坍缩为一种递归结构——这正是上述 MRLA–GLA 与 DDL–DeltaNet 对应关系所基于的核心架构。

15

第 15 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

Prior Residuals as Depth-Wise Linear Attention The structured-matrix perspective further relates to the sequencedepth duality by showing that existing residual variants are, in effect, instances of linear attention over the depth axis. For example, the unrolled (m)HC weight Mil​=βi⊤​Ai+1l×​αl​ (Eq. 10) admits a natural attention interpretation in which αl​ plays the role of a query issued by layer l , βi​ serves as a key summarizing the contribution of layer i , and the cumulative transition Ai+1l×​ acts as a depth-relative positional operator [69] governing the query–key interaction across intervening layers. Notably, the m parallel streams correspond to state expansion [40, 29] along the depth axis, expanding the recurrent state from d to d×m and thereby increasing the semiseparable rank of M. [58] show that replacing Aˉi+1l×​ with the identity matrix still yields competitive performance, highlighting the role of state expansion. Through this lens, methods like (m)HC thus act as depth-wise linear attention with matrix-valued states, while AttnRes acts as depth-wise softmax attention.  
先验残差作为深度方向线性注意力 结构化矩阵视角进一步揭示了序列-深度对偶性，表明现有残差变体本质上是沿深度轴的线性注意力实例。例如，展开的权重矩阵（公式 10）可自然解释为注意力机制：其中层发出的查询向量扮演查询角色，层贡献摘要矩阵充当键向量，累积转移矩阵则作为深度相对位置算子[69]，调控跨中间层的查询-键交互。值得注意的是，并行流对应沿深度轴的状态扩展[40, 29]，将循环状态从维度扩展至维度，从而提升矩阵的半可分秩。[58]研究表明，将替换为单位矩阵仍能保持竞争力，凸显了状态扩展的作用。由此观之，类方法实质是采用矩阵值状态的深度方向线性注意力，而注意力残差则相当于深度方向的 Softmax 注意力。

# 7 Related Work  7 相关工作

Normalization, Scaling, and Depth Stability. The standard residual update hl+1​=hl​+fl​(hl​) [12] presents a fundamental tension between normalization placement and gradient propagation. PostNorm [52] maintains bounded magnitudes but distorts gradients, as repeated normalization on the residual path compounds into gradient vanishing at depth [60]. PreNorm [34, 60] restores a clean identity path yet introduces unbounded magnitude growth: since ∥hˉl​∥ grows as O(L) , each layer’s relative contribution shrinks, compelling deeper layers to produce ever-larger outputs and limiting effective depth [27]. Subsequent work reconciles both desiderata via scaled residual paths [54], hybrid normalization [73], amplified skip connections [4], or learned element-wise gates [45] (see Table 5). AttnRes sidesteps this tension by replacing the additive recurrence with selective aggregation over individual earlier-layer outputs, avoiding both the cumulative magnitude growth of PreNorm and the repeated scale contraction of PostNorm.  
归一化、缩放与深度稳定性。标准残差更新 hl+1​=hl​+fl​(hl​) [12]揭示了归一化位置与梯度传播之间的根本性矛盾。后归一化[52]能保持幅度有界但会扭曲梯度，因为残差路径上的重复归一化会累积导致深度梯度消失[60]。前归一化[34, 60]恢复了纯净的恒等路径，却引入了无界的幅度增长：由于 ∥hˉl​∥ 以 O(L) 速率增长，每层的相对贡献逐渐萎缩，迫使更深层必须产生越来越大的输出，从而限制了有效深度[27]。后续研究通过缩放残差路径[54]、混合归一化[73]、增强跳跃连接[4]或可学习的逐元素门控[45]来协调这两个需求（见表 5）。注意力残差机制通过用对早期各层输出的选择性聚合替代加法递归，巧妙规避了这一矛盾，既避免了前归一化的累积幅度增长，也绕过了后归一化的重复尺度收缩问题。

Multi-State Recurrence. All single-state methods above condition layer l only on hl−1​ , from which individual earlier-layer contributions cannot be selectively retrieved. Several methods address this by widening the recurrence to multiple parallel streams: Hyper-Connections [72] and its stabilized variant mHC [59] maintain m streams with learned mixing matrices; DDL [67] maintains a matrix state updated via a delta-rule erase-and-write mechanism; SiameseNorm [27] maintains two parameter-shared streams—one PreNorm and one PostNorm—to preserve identity gradients and bounded representations. While these methods alleviate information compression, they still condition on the immediate predecessor’s state; AttnRes is orthogonal, providing selective access to individual earlier-layer outputs while remaining compatible with any normalization or gating scheme. We discuss the formal connection to Hyper-Connections in  S6.2 .  
多状态递归。上述所有单状态方法仅基于 hl−1​ 来调节第 l 层，无法从中选择性提取各早期层的贡献。为解决此问题，多种方法通过扩展递归至多个并行流来实现：超连接[72]及其稳定变体 mHC[59]维护 m 个流并采用学习型混合矩阵；DDL[67]通过增量规则擦除-写入机制维护矩阵状态更新；SiameseNorm[27]维护两个参数共享流——一个预归一化流和一个后归一化流——以保持恒等梯度与有界表示。虽然这些方法缓解了信息压缩问题，但仍依赖于直接前驱状态；而 AttnRes 采用正交方法，在保持与任何归一化或门控方案兼容的同时，提供对单个早期层输出的选择性访问。我们将在  S6.2 中讨论其与超连接的形式化关联。

Cross-Layer Connectivity. A separate line of work bypasses the single-state bottleneck by giving each layer direct access to individual earlier-layer outputs. The simplest approach uses static weights: DenseNet [17] concatenates all preceding feature maps; ELMo [38] computes a softmax-weighted sum of layer representations with learned scalar weights; DenseFormer [36] and ANCRe [68] assign learned per-layer scalar coefficients fixed after training. For input-dependent aggregation, MUDDFormer [56] generates position-dependent weights via a small MLP across four decoupled streams; MRLA [10] applies element-wise sigmoid gating over all previous layers, though its separable query–key product is closer to linear attention than softmax-based retrieval. Other methods trade full cross-layer access for more targeted designs: Value Residual Learning [71] accesses only a single earlier layer; LAuReL [30] augments the residual with low-rank projections over the previous k activations; Dreamer [24] combines sequence attention with depth attention and sparse experts. AttnRes combines softmax-normalized, input-dependent weights with selective access to all preceding layers through a single d -dimensional pseudo-query per layer, and introduces a block structure reducing cost from O(ˇ​L25​) to O(LN) . Cache-based pipeline communication and a two-phase computation strategy (§ 4) make Block AttnRes practical at scale with negligible overhead.  
跨层连接。另一类研究通过让每一层直接访问早期各层的输出，绕过了单状态瓶颈。最简单的方法是使用静态权重：DenseNet [17] 将所有先前的特征图拼接起来；ELMo [38] 通过学习的标量权重计算层表示的 softmax 加权和；DenseFormer [36] 和 ANCRe [68] 则为每层分配在训练后固定的学习标量系数。对于输入依赖的聚合，MUDDFormer [56] 通过一个小型 MLP 在四个解耦流中生成位置相关的权重；MRLA [10] 对所有先前层应用逐元素的 sigmoid 门控，尽管其可分离的查询-键乘积更接近线性注意力而非基于 softmax 的检索。其他方法则用更针对性的设计换取完全的跨层访问：Value Residual Learning [71] 仅访问单个早期层；LAuReL [30] 通过先前 k 激活的低秩投影增强残差；Dreamer [24] 将序列注意力与深度注意力及稀疏专家相结合。 AttnRes 结合了经过 softmax 归一化的输入依赖权重，并通过每层一个 d 维伪查询实现对所有前序层的选择性访问，同时引入块状结构将计算成本从 O(ˇ​L25​) 降低至 O(LN) 。基于缓存的流水线通信与两阶段计算策略（§4）使块状 AttnRes 能够在大规模应用中高效运行，且额外开销可忽略不计。

# Conclusion  结论

Inspired by the duality between sequence and depth, we introduce AttnRes, which replaces fixed, uniform residual accumulation with learned, input-dependent depth-wise attention. We validate the method through ablation studies and scaling law experiments, showing that its gains persist across scales. Because Full AttnRes must access all preceding layer outputs at every layer, the memory footprint of cross-layer aggregation grows as O(Ld) , which is prohibitive for large-scale models on current hardware. We therefore introduce Block AttnRes, which partitions layers into N blocks and attends over block-level representations. Empirically, using about 8 blocks recovers most of the gains of Full AttnRes, while finer-grained blocking remains a promising direction as future hardware constraints relax. Together with cross-stage caching and a two-phase computation strategy, Block AttnRes is practical at scale, incurring only marginal training overhead and minimal inference overhead.  
受序列与深度二元性的启发，我们提出了 AttnRes 方法，该方法通过可学习的、输入依赖的深度注意力机制，取代了固定且均匀的残差累积。我们通过消融实验和缩放定律实验验证了该方法，证明其增益在不同规模下均能持续存在。由于完整版 AttnRes 必须在每一层访问所有先前层的输出，跨层聚合的内存占用会以 O(Ld) 的速度增长，这对当前硬件上的大规模模型而言是难以承受的。因此，我们引入了分块 AttnRes，将层划分为 N 个块，并在块级表示上进行注意力计算。实验表明，使用约 8 个块即可恢复完整版 AttnRes 的大部分增益，而更细粒度的分块在未来硬件限制放宽后仍是一个有前景的方向。结合跨阶段缓存和两阶段计算策略，分块 AttnRes 在大规模应用中具有实用性，仅带来微小的训练开销和极低的推理开销。

16

第 16 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

# References  参考文献

[1]Jacob Austin et al. Program Synthesis with Large Language Models. 2021. arXiv: 2108.07732 [cs.PL]. URL: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732).  
Jacob Austin 等人。《基于大型语言模型的程序合成》。2021 年。arXiv: 2108.07732 [cs.PL]。网址：https://arxiv.org/abs/2108.07732。

[2]Thomas Bachlechner et al. ReZero is All You Need: Fast Convergence at Large Depth. 2020. arXiv: 2003.04887 [cs.LG]. URL: [https://arxiv.org/abs/2003.04887](https://arxiv.org/abs/2003.04887).  
Thomas Bachlechner 等人。ReZero 即所需一切：深度网络中的快速收敛。2020 年。arXiv: 2003.04887 [cs.LG]。网址：https://arxiv.org/abs/2003.04887。

[3]Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural Machine Translation by Jointly Learning to Align and Translate. 2016. arXiv: 1409.0473 [cs.CL]. URL: [https://arxiv.org/abs/1409.0473](https://arxiv.org/abs/1409.0473).  
Dzmitry Bahdanau、Kyunghyun Cho 和 Yoshua Bengio。通过联合学习对齐与翻译的神经机器翻译。2016 年。arXiv: 1409.0473 [cs.CL]。网址：https://arxiv.org/abs/1409.0473。

[4]Chen Chen and Lai Wei. Post-LayerNorm Is Back: Stable, ExpressivE, and Deep. 2026. arXiv: 2601.19895 [cs.LG]. URL: [https://arxiv.org/abs/2601.19895](https://arxiv.org/abs/2601.19895).  
陈晨与赖伟。《后层归一化回归：稳定、表达力强且深度》。2026 年。arXiv: 2601.19895 [cs.LG]。网址：https://arxiv.org/abs/2601.19895。

[5]Mark Chen et al. Evaluating Large Language Models Trained on Code. 2021. arXiv: 2107.03374 [cs.LG]. URL: [https://arxiv.org/abs/2107.03374](https://arxiv.org/abs/2107.03374).  
马克·陈等人。《评估基于代码训练的大型语言模型》。2021 年。arXiv: 2107.03374 [cs.LG]。网址：https://arxiv.org/abs/2107.03374。

[6]Peter Clark et al. “Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge”. In: arXiv:1803.05457v1 (2018).  
Peter Clark 等人。"认为你已经解决了问答问题？试试 ARC，AI2 推理挑战赛"。收录于：arXiv:1803.05457v1 (2018)。

[7]Karl Cobbe et al. Training Verifiers to Solve Math Word Problems. 2021. arXiv: 2110.14168 [cs.LG]. URL: [https://arxiv.org/abs/2110.14168](https://arxiv.org/abs/2110.14168).  
Karl Cobbe 等人。训练验证器解决数学文字问题。2021 年。arXiv: 2110.14168 [cs.LG]。网址：https://arxiv.org/abs/2110.14168。

[8]Tri Dao and Albert Gu. “Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality”. In: CoRR abs/2405.21060 (2024). DOI: 10.48550/ARXIV.2405.21060. arXiv: 2405.21060. URL: [https://doi.org/10.48550/arXiv.2405.21060](https://doi.org/10.48550/arXiv.2405.21060).  
Tri Dao 与 Albert Gu。"Transformer 即状态空间模型：通过结构化状态空间对偶实现广义模型与高效算法"。收录于：CoRR abs/2405.21060 (2024)。DOI：10.48550/ARXIV.2405.21060。arXiv：2405.21060。网址：https://doi.org/10.48550/arXiv.2405.21060。

[9]DeepSeek-AI et al. DeepSeek-V3 Technical Report. 2025. arXiv: 2412.19437 [cs.CL]. URL: [https://arxiv](https://arxiv/). org/abs/2412.19437.  
DeepSeek-AI 等人。DeepSeek-V3 技术报告。2025 年。arXiv: 2412.19437 [cs.CL]。网址：https://arxiv.org/abs/2412.19437。

[10]Yanwen Fang et al. Cross-Layer Retrospective Retrieving via Layer Attention. 2023. arXiv: 2302 . 03985 [cs.CV]. URL: [https://arxiv.org/abs/2302.03985](https://arxiv.org/abs/2302.03985).  
Yanwen Fang 等人。通过层注意力进行跨层回顾检索。2023 年。arXiv: 2302.03985 [cs.CV]。网址：https://arxiv.org/abs/2302.03985。

[11]Andrey Gromov et al. The Unreasonable Ineffectiveness of the Deeper Layers. 2025. arXiv: 2403 . 17887 [cs.CL]. URL: [https://arxiv.org/abs/2403.17887](https://arxiv.org/abs/2403.17887).  
安德烈·格罗莫夫等人。《深层网络的不合理低效性》。2025 年。arXiv: 2403.17887 [cs.CL]。网址：https://arxiv.org/abs/2403.17887。

[12]Kaiming He et al. Deep Residual Learning for Image Recognition. 2015. arXiv: 1512.03385 [cs.CV]. URL: [https://arxiv.org/abs/1512.03385](https://arxiv.org/abs/1512.03385).  
何恺明等人。《用于图像识别的深度残差学习》。2015 年。arXiv: 1512.03385 [cs.CV]。网址：https://arxiv.org/abs/1512.03385。

[13]Dan Hendrycks et al. Measuring Massive Multitask Language Understanding. 2021. arXiv: 2009 . 03300 [cs.CY]. URL: [https://arxiv.org/abs/2009.03300](https://arxiv.org/abs/2009.03300).  
Dan Hendrycks 等人。《大规模多任务语言理解能力评测》。2021 年。arXiv: 2009 . 03300 [cs.CY]。网址：https://arxiv.org/abs/2009.03300。

[14]Dan Hendrycks et al. Measuring Mathematical Problem Solving With the MATH Dataset. 2021. arXiv: 2103. 03874 [cs.LG]. URL: [https://arxiv.org/abs/2103.03874](https://arxiv.org/abs/2103.03874).  
Dan Hendrycks 等人。《使用 MATH 数据集衡量数学问题解决能力》。2021 年。arXiv：2103.03874 [cs.LG]。网址：https://arxiv.org/abs/2103.03874。

[15]Jordan Hoffmann et al. Training Compute-Optimal Large Language Models. 2022. arXiv: 2203.15556 [cs.CL]. URL: [https://arxiv.org/abs/2203.15556](https://arxiv.org/abs/2203.15556).  
Jordan Hoffmann 等人。《训练计算最优的大型语言模型》。2022 年。arXiv：2203.15556 [cs.CL]。网址：https://arxiv.org/abs/2203.15556。

[16]Shengding Hu et al. MiniCPM: Unveiling the Potential of Small Language Models with Scalable Training Strategies. 2024. arXiv: 2404.06395 [cs.CL]. URL: [https://arxiv.org/abs/2404.06395](https://arxiv.org/abs/2404.06395).  
盛鼎虎等人。MiniCPM：通过可扩展训练策略揭示小型语言模型的潜力。2024 年。arXiv: 2404.06395 [cs.CL]。URL: https://arxiv.org/abs/2404.06395。

[17]Gao Huang et al. Densely Connected Convolutional Networks. 2018. arXiv: 1608 . 06993 [cs.CV]. URL: [https://arxiv.org/abs/1608.06993](https://arxiv.org/abs/1608.06993).  
高黄等人。密集连接卷积网络。2018 年。arXiv: 1608 . 06993 [cs.CV]。网址：https://arxiv.org/abs/1608.06993。

[18]Yanping Huang et al. “GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism”. In: Advances in NeurIPS. 2019.  
黄燕萍等人。“GPipe：使用流水线并行高效训练巨型神经网络”。载于：NeurIPS 进展。2019 年。

[19]Yuzhen Huang et al. “C-eval: A multi-level multi-discipline chinese evaluation suite for foundation models”. In: Advances in NeurIPS 36 (2023), pp. 62991–63010.  
黄雨真等人。"C-eval：面向基础模型的多层次多学科中文评估套件"。载于：《神经信息处理系统进展》第 36 卷（2023 年），第 62991–63010 页。

[20]Robert A. Jacobs et al. “Adaptive Mixtures of Local Experts”. In: Neural Computation 3.1 (1991), pp. 79–87. DOI: 10.1162/neco.1991.3.1.79.  
罗伯特·A·雅各布斯等人。"自适应局部专家混合模型"。载于：《神经计算》第 3 卷第 1 期（1991 年），第 79–87 页。DOI：10.1162/neco.1991.3.1.79。

[21]Mandar Joshi et al. “Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension”. In: arXiv preprint arXiv:1705.03551 (2017).  
Mandar Joshi 等人。"Triviaqa：一个用于阅读理解的大规模远程监督挑战数据集"。收录于：arXiv 预印本 arXiv:1705.03551（2017）。

[22]Jared Kaplan et al. Scaling Laws for Neural Language Models. 2020. arXiv: 2001.08361 [cs.LG]. URL: [https://arxiv.org/abs/2001.08361](https://arxiv.org/abs/2001.08361).  
Jared Kaplan 等人。神经语言模型的缩放定律。2020。arXiv：2001.08361 [cs.LG]。网址：https://arxiv.org/abs/2001.08361。

[23]Angelos Katharopoulos et al. “Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention”. In: Proceedings of ICML. Ed. by Hal Daumé III and Aarti Singh. PMLR, 2020, pp. 5156–5165. URL: https: //proceedings.mlr.press/v119/katharopoulos20a.html.  
Angelos Katharopoulos 等人。“Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention”。收录于：ICML 会议论文集。由 Hal Daumé III 和 Aarti Singh 编辑。PMLR，2020 年，第 5156–5165 页。网址：https://proceedings.mlr.press/v119/katharopoulos20a.html。

[24]Jonas Knupp et al. Depth-Recurrent Attention Mixtures: Giving Latent Reasoning the Attention it Deserves. 2026. arXiv: 2601.21582 [cs.AI]. URL: [https://arxiv.org/abs/2601.21582](https://arxiv.org/abs/2601.21582).  
乔纳斯·克努普等人。《深度循环注意力混合：赋予潜在推理应有的关注》。2026 年。arXiv: 2601.21582 [cs.AI]。网址：https://arxiv.org/abs/2601.21582。

[25]Aitor Lewkowycz et al. Solving Quantitative Reasoning Problems with Language Models. 2022. arXiv: 2206. 14858 [cs.CL]. URL: [https://arxiv.org/abs/2206.14858](https://arxiv.org/abs/2206.14858).  
Aitor Lewkowycz 等人。《利用语言模型解决定量推理问题》。2022 年。arXiv: 2206.14858 [cs.CL]。网址：https://arxiv.org/abs/2206.14858。

17

第 17 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

[26]Haonan Li et al. “CMMLU: Measuring massive multitask language understanding in Chinese”. In: Findings of the Association for Computational Linguistics: ACL 2024. Ed. by Lun-Wei Ku, Andre Martins, and Vivek Srikumar. Bangkok, Thailand: Association for Computational Linguistics, Aug. 2024, pp. 11260–11285. DOI: 10 . 18653 / v1 / 2024 . findings - acl . 671. URL: https : / / aclanthology . org / 2024 . findings - acl.671/.  
李浩南等人。"CMMLU：中文大规模多任务语言理解能力评测"。载于：《计算语言学协会 2024 年 ACL 会议论文集》。由古伦伟、安德烈·马丁斯和维韦克·斯里库马尔编辑。泰国曼谷：计算语言学协会，2024 年 8 月，第 11260–11285 页。DOI：10.18653/v1/2024.findings-acl.671。网址：https://aclanthology.org/2024.findings-acl.671/。

[27]Tianyu Li et al. SiameseNorm: Breaking the Barrier to Reconciling Pre/Post-Norm. 2026. arXiv: 2602.08064 [cs.LG]. URL: [https://arxiv.org/abs/2602.08064](https://arxiv.org/abs/2602.08064).  
Tianyu Li 等人。SiameseNorm：打破前/后归一化融合的壁垒。2026 年。arXiv：2602.08064 [cs.LG]。网址：https://arxiv.org/abs/2602.08064。

[28]Jingyuan Liu et al. Muon is Scalable for LLM Training. 2025. arXiv: 2502.16982 [cs.LG]. URL: https: //arxiv.org/abs/2502.16982.  
Jingyuan Liu 等人。Muon 可扩展用于 LLM 训练。2025 年。arXiv：2502.16982 [cs.LG]。网址：https://arxiv.org/abs/2502.16982。

[29]Brian Mak and Jeffrey Flanigan. Residual Matrix Transformers: Scaling the Size of the Residual Stream. 2025. arXiv: 2506.22696 [cs.LG]. URL: [https://arxiv.org/abs/2506.22696](https://arxiv.org/abs/2506.22696).  
Brian Mak 与 Jeffrey Flanigan。残差矩阵变换器：扩展残差流的规模。2025 年。arXiv: 2506.22696 [cs.LG]。网址：https://arxiv.org/abs/2506.22696。

[30]Gaurav Menghani, Ravi Kumar, and Sanjiv Kumar. LAuReL: Learned Augmented Residual Layer. 2025. arXiv: 2411.07501 [cs.LG]. URL: [https://arxiv.org/abs/2411.07501](https://arxiv.org/abs/2411.07501).  
Gaurav Menghani、Ravi Kumar 和 Sanjiv Kumar。LAuReL：学习增强残差层。2025 年。arXiv：2411.07501 [cs.LG]。网址：https://arxiv.org/abs/2411.07501。

[31]Maxim Milakov and Natalia Gimelshein. Online normalizer calculation for softmax. 2018. arXiv: 1805.02867 [cs.PF]. URL: [https://arxiv.org/abs/1805.02867](https://arxiv.org/abs/1805.02867).  
Maxim Milakov 与 Natalia Gimelshein。在线归一化器计算用于 Softmax。2018 年。arXiv：1805.02867 [cs.PF]。网址：https://arxiv.org/abs/1805.02867。

[32]Tsendsuren Munkhdalai et al. “Metalearned Neural Memory”. In: ArXiv abs/1907.09720 (2019). URL: https: //api.semanticscholar.org/CorpusID:198179407.  
Tsendsuren Munkhdalai 等人。“元学习神经记忆”。载于：ArXiv abs/1907.09720（2019 年）。网址：https://api.semanticscholar.org/CorpusID:198179407。

[33]Deepak Narayanan et al. Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM. 2021. arXiv: 2104.04473 [cs.CL]. URL: [https://arxiv.org/abs/2104.04473](https://arxiv.org/abs/2104.04473).  
Deepak Narayanan 等人。使用 Megatron-LM 在 GPU 集群上高效进行大规模语言模型训练。2021 年。arXiv: 2104.04473 [cs.CL]。URL: https://arxiv.org/abs/2104.04473。

[34]Toan Q. Nguyen and Julian Salazar. “Transformers without Tears: Improving the Normalization of Self-Attention”. In: Proceedings of IWSLT. Ed. by Jan Niehues et al. 2019. URL: https : / / aclanthology . org/2019.iwslt-1.17/.  
Toan Q. Nguyen 和 Julian Salazar。《无需泪水的 Transformer：改进自注意力归一化》。载于：IWSLT 会议论文集。由 Jan Niehues 等人编辑。2019 年。网址：https://aclanthology.org/2019.iwslt-1.17/。

[35]OpenAI et al. GPT-4 Technical Report. 2024. arXiv: 2303.08774 [cs.CL]. URL: [https://arxiv.org/abs/](https://arxiv.org/abs/) 2303.08774.  
OpenAI 等人。GPT-4 技术报告。2024 年。arXiv：2303.08774 [cs.CL]。网址：https://arxiv.org/abs/2303.08774。

[36]Matteo Pagliardini et al. DenseFormer: Enhancing Information Flow in Transformers via Depth Weighted Averaging. 2024. arXiv: 2402.02622 [cs.CL]. URL: [https://arxiv.org/abs/2402.02622](https://arxiv.org/abs/2402.02622).  
Matteo Pagliardini 等人。DenseFormer：通过深度加权平均增强 Transformer 中的信息流。2024 年。arXiv：2402.02622 [cs.CL]。网址：https://arxiv.org/abs/2402.02622。

[37]Bowen Peng et al. “Yarn: Efficient context window extension of large language models”. In: arXiv preprint arXiv:2309.00071 (2023).  
Bowen Peng 等人。"Yarn: 大型语言模型的高效上下文窗口扩展"。载于：arXiv 预印本 arXiv:2309.00071 (2023)。

[38]Matthew E. Peters et al. “Deep Contextualized Word Representations”. In: Proceedings of NAACL. 2018, pp. 2227–2237. URL: [https://aclanthology.org/N18-1202/](https://aclanthology.org/N18-1202/).  
Matthew E. Peters 等人。"深度上下文化词表示"。载于：NAACL 会议论文集。2018 年，第 2227–2237 页。网址：https://aclanthology.org/N18-1202/。

[39]Reiner Pope et al. Efficiently Scaling Transformer Inference. 2022. arXiv: 2211.05102 [cs.LG].  
Reiner Pope 等人。高效扩展 Transformer 推理。2022 年。arXiv: 2211.05102 [cs.LG]。

[40]Zhen Qin et al. HGRN2: Gated Linear RNNs with State Expansion. 2024. arXiv: 2404.07904 [cs.CL].  
秦臻 等人。HGRN2：具有状态扩展的门控线性 RNN。2024 年。arXiv: 2404.07904 [cs.CL]。

[41]David Rein et al. “Gpqa: A graduate-level google-proof q&a benchmark”. In: First Conference on Language Modeling. 2024.  
David Rein 等人。《Gpqa：一个研究生级别的防谷歌问答基准测试》。载于：第一届语言建模会议。2024 年。

[42]Imanol Schlag, Kazuki Irie, and Jürgen Schmidhuber. “Linear Transformers Are Secretly Fast Weight Programmers”. In: Proceedings of ICML. Ed. by Marina Meila and Tong Zhang. PMLR, 2021, pp. 9355–9366. URL: [https://proceedings.mlr.press/v139/schlag21a.html](https://proceedings.mlr.press/v139/schlag21a.html).  
Imanol Schlag、Kazuki Irie 和 Jürgen Schmidhuber。《线性变换器是秘密的快速权重编程器》。载于：ICML 会议论文集。Marina Meila 和 Tong Zhang 编辑。PMLR，2021 年，第 9355–9366 页。网址：https://proceedings.mlr.press/v139/schlag21a.html。

[43]Jürgen Schmidhuber. “Learning to control fast-weight memories: An alternative to dynamic recurrent networks”. In: Neural Computation 4.1 (1992), pp. 131–139.  
Jürgen Schmidhuber. “学习控制快速权重记忆：动态循环网络的替代方案”。载于：Neural Computation 4.1 (1992)，第 131–139 页。

[44]Freda Shi et al. Language Models are Multilingual Chain-of-Thought Reasoners. 2022. arXiv: 2210.03057 [cs.CL]. URL: [https://arxiv.org/abs/2210.03057](https://arxiv.org/abs/2210.03057).  
Freda Shi 等人. 语言模型是多语言思维链推理器。2022. arXiv: 2210.03057 [cs.CL]. URL: https://arxiv.org/abs/2210.03057.

[45]Rupesh Kumar Srivastava, Klaus Greff, and Jürgen Schmidhuber. Highway Networks. 2015. arXiv: 1505.00387 [cs.LG]. URL: [https://arxiv.org/abs/1505.00387](https://arxiv.org/abs/1505.00387).  
Rupesh Kumar Srivastava、Klaus Greff 与 Jürgen Schmidhuber。高速公路网络。2015 年。arXiv: 1505.00387 [cs.LG]。网址：https://arxiv.org/abs/1505.00387。

[46]Yu Sun et al. “Learning to (Learn at Test Time): RNNs with Expressive Hidden States”. In: ArXiv abs/2407.04620 (2024). URL: [https://api.semanticscholar.org/CorpusID:271039606](https://api.semanticscholar.org/CorpusID:271039606).  
Yu Sun 等人。"学习（在测试时学习）：具有表达性隐藏状态的 RNN"。载于：ArXiv abs/2407.04620 (2024)。网址：https://api.semanticscholar.org/CorpusID:271039606。

[47]Yutao Sun et al. Retentive Network: A Successor to Transformer for Large Language Models. 2023. arXiv: 2307.08621 [cs.CL].  
Yutao Sun 等人。Retentive Network：大型语言模型中 Transformer 的继任者。2023。arXiv：2307.08621 [cs.CL]。

[48]Mirac Suzgun et al. “Challenging big-bench tasks and whether chain-of-thought can solve them”. In: arXiv preprint arXiv:2210.09261 (2022).  
Mirac Suzgun 等人。"挑战 Big-Bench 任务：思维链能否解决它们"。载于：arXiv 预印本 arXiv:2210.09261（2022）。

[49]Shawn Tan et al. “Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study”. In: Proceedings of ICLR. 2025.  
Shawn Tan 等人。"扩展 Stick-Breaking 注意力：高效实现与深入研究"。载于：ICLR 会议论文集。2025。

[50]Hugo Touvron et al. Going deeper with Image Transformers. 2021. arXiv: 2103.17239 [cs.CV]. URL: https: //arxiv.org/abs/2103.17239.  
Hugo Touvron 等人。深入探索图像变换器。2021 年。arXiv: 2103.17239 [cs.CV]。网址：https://arxiv.org/abs/2103.17239。

[51]Hugo Touvron et al. LLaMA: Open and Efficient Foundation Language Models. 2023. arXiv: 2302.13971 [cs.CL].  
Hugo Touvron 等人。LLaMA：开放且高效的基础语言模型。2023 年。arXiv: 2302.13971 [cs.CL]。

18

第 18 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

[52]Ashish Vaswani et al. “Attention is All you Need”. In: Advances in NeurIPS. Ed. by I. Guyon et al. Curran Associates, Inc., 2017. URL: [https://proceedings.neurips.cc/paper_files/paper/2017/file/](https://proceedings.neurips.cc/paper_files/paper/2017/file/) 3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf.  
Ashish Vaswani 等人。《注意力机制就是一切》。载于：NeurIPS 进展。由 I. Guyon 等人编辑。Curran Associates, Inc., 2017。网址：https://proceedings.neurips.cc/paper_files/paper/2017/file/ 3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf。

[53]Ashish Vaswani et al. “Attention is All you Need”. In: Advances in NeurIPS. Ed. by I. Guyon et al. Vol. 30. Curran Associates, Inc., 2017. URL: [https://proceedings.neurips.cc/paper_files/paper/2017/](https://proceedings.neurips.cc/paper_files/paper/2017/) file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf.  
Ashish Vaswani 等人。《注意力机制就是一切》。载于：NeurIPS 进展。由 I. Guyon 等人编辑。第 30 卷。Curran Associates, Inc., 2017。网址：https://proceedings.neurips.cc/paper_files/paper/2017/ file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf。

[54]Hongyu Wang et al. DeepNet: Scaling Transformers to 1,000 Layers. 2022. arXiv: 2203.00555 [cs.CL]. URL: [https://arxiv.org/abs/2203.00555](https://arxiv.org/abs/2203.00555).  
王宏宇等人。DeepNet：将 Transformer 扩展至 1000 层。2022 年。arXiv: 2203.00555 [cs.CL]。URL: https://arxiv.org/abs/2203.00555。

[55]Yubo Wang et al. “Mmlu-pro: A more robust and challenging multi-task language understanding benchmark”. In: Advances in NeurIPS 37 (2024), pp. 95266–95290.  
Yubo Wang 等人。"Mmlu-pro：一个更稳健且更具挑战性的多任务语言理解基准"。载于：NeurIPS 37 进展（2024 年），第 95266–95290 页。

[56]Da Xiao et al. “MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections”. In: Proceedings of ICML. 2025.  
Da Xiao 等人。"MUDDFormer：通过多路动态密集连接打破 Transformer 中的残差瓶颈"。载于：ICML 会议论文集。2025 年。

[57]Guangxuan Xiao et al. “Efficient streaming language models with attention sinks”. In: arXiv preprint arXiv:2309.17453 (2023).  
肖广轩等人。"具有注意力汇聚机制的高效流式语言模型"。载于：arXiv 预印本 arXiv:2309.17453（2023 年）。

[58]Tian Xie. Your DeepSeek mHC Might Not Need the “m”. Zhihu blog post. 2026. URL: [https://zhuanlan](https://zhuanlan/). zhihu.com/p/2010852389670908320.  
谢天。你的 DeepSeek mHC 可能不需要那个“m”。知乎博客文章。2026 年。网址：https://zhuanlan.zhihu.com/p/2010852389670908320。

[59]Zhenda Xie et al. mHC: Manifold-Constrained Hyper-Connections. 2026. arXiv: 2512.24880 [cs.CL]. URL: [https://arxiv.org/abs/2512.24880](https://arxiv.org/abs/2512.24880).  
谢振达等人。mHC：流形约束超连接。2026 年。arXiv：2512.24880 [cs.CL]。网址：https://arxiv.org/abs/2512.24880。

[60]Ruibin Xiong et al. On Layer Normalization in the Transformer Architecture. 2020. arXiv: 2002.04745 [cs.LG]. URL: [https://arxiv.org/abs/2002.04745](https://arxiv.org/abs/2002.04745).  
熊瑞斌等人。论 Transformer 架构中的层归一化。2020 年。arXiv：2002.04745 [cs.LG]。网址：https://arxiv.org/abs/2002.04745。

[61]Bowen Yang et al. Rope to Nope and Back Again: A New Hybrid Attention Strategy. 2025. arXiv: 2501.18795 [cs.CL]. URL: [https://arxiv.org/abs/2501.18795](https://arxiv.org/abs/2501.18795).  
Bowen Yang 等人。《从绳到否再回归：一种新的混合注意力策略》。2025 年。arXiv: 2501.18795 [cs.CL]。URL: https://arxiv.org/abs/2501.18795。

[62]Songlin Yang, Jan Kautz, and Ali Hatamizadeh. “Gated Delta Networks: Improving Mamba2 with Delta Rule”. In: Proceedings of ICLR. 2025. URL: [https://openreview.net/forum?id=r8H7xhYPwz](https://openreview.net/forum?id=r8H7xhYPwz).  
Songlin Yang、Jan Kautz 和 Ali Hatamizadeh。《门控 Delta 网络：通过 Delta 规则改进 Mamba2》。载于：ICLR 会议论文集。2025 年。URL: https://openreview.net/forum?id=r8H7xhYPwz。

[63]Songlin Yang et al. “Gated Linear Attention Transformers with Hardware-Efficient Training”. In: Proceedings of ICML. PMLR, 2024.  
宋林杨等人。"具有硬件高效训练的门控线性注意力变换器"。收录于：ICML 会议论文集。PMLR，2024 年。

[64]Yongyi Yang and Jianyang Gao. mHC-lite: You Don’t Need 20 Sinkhorn-Knopp Iterations. 2026. arXiv: 2601. 05732 [cs.LG]. URL: [https://arxiv.org/abs/2601.05732](https://arxiv.org/abs/2601.05732).  
杨永义和高建阳。mHC-lite：你不需要 20 次 Sinkhorn-Knopp 迭代。2026 年。arXiv：2601.05732 [cs.LG]。网址：https://arxiv.org/abs/2601.05732。

[65]Rowan Zellers et al. “HellaSwag: Can a Machine Really Finish Your Sentence?” In: Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics. 2019.  
Rowan Zellers 等人，《HellaSwag：机器真的能完成你的句子吗？》收录于：第 57 届计算语言学协会年会论文集，2019 年。

[66]Biao Zhang and Rico Sennrich. “Root mean square layer normalization”. In: Advances in NeurIPS 32 (2019).  
Biao Zhang 与 Rico Sennrich，《均方根层归一化》收录于：神经信息处理系统进展第 32 卷，2019 年。

[67]Yifan Zhang et al. Deep Delta Learning. 2026. arXiv: 2601.00417 [cs.LG]. URL: [https://arxiv.org/](https://arxiv.org/) abs/2601.00417.  
张一帆等人。深度增量学习。2026 年。arXiv: 2601.00417 [cs.LG]。网址：https://arxiv.org/abs/2601.00417。

[68]Yilang Zhang et al. ANCRe: Adaptive Neural Connection Reassignment for Efficient Depth Scaling. 2026. arXiv: 2602.09009 [cs.LG]. URL: [https://arxiv.org/abs/2602.09009](https://arxiv.org/abs/2602.09009).  
张一郎等人。ANCRe：面向高效深度扩展的自适应神经连接重分配。2026 年。arXiv: 2602.09009 [cs.LG]。网址：https://arxiv.org/abs/2602.09009。

[69]Yu Zhang et al. Kimi Linear: An Expressive, Efficient Attention Architecture. 2025. arXiv: 2510.26692 [cs.CL].  
张宇等人。Kimi Linear：一种表达力强、高效的注意力架构。2025 年。arXiv：2510.26692 [cs.CL]。

[70]Shu Zhong et al. Understanding Transformer from the Perspective of Associative Memory. 2025. arXiv: 2505. 19488 [cs.LG]. URL: [https://arxiv.org/abs/2505.19488](https://arxiv.org/abs/2505.19488).  
钟舒等人。从联想记忆的角度理解 Transformer。2025 年。arXiv：2505.19488 [cs.LG]。网址：https://arxiv.org/abs/2505.19488。

[71]Zhanchao Zhou et al. “Value Residual Learning”. In: Proceedings of ACL. Ed. by Wanxiang Che et al. Vienna, Austria, 2025, pp. 28341–28356. URL: [https://aclanthology.org/2025.acl-long.1375/](https://aclanthology.org/2025.acl-long.1375/).  
周展超等人。“价值残差学习”。载于：ACL 会议论文集。由车万翔等人编辑。奥地利维也纳，2025 年，第 28341–28356 页。网址：https://aclanthology.org/2025.acl-long.1375/。

[72]Defa Zhu et al. Hyper-Connections. 2025. arXiv: 2409.19606 [cs.LG]. URL: [https://arxiv.org/abs/](https://arxiv.org/abs/) 2409.19606.  
Defa Zhu 等人。《超连接》。2025 年。arXiv: 2409.19606 [cs.LG]。URL: https://arxiv.org/abs/2409.19606。

[73]Zhijian Zhuo et al. HybridNorm: Towards Stable and Efficient Transformer Training via Hybrid Normalization. 2025. arXiv: 2503.04598 [cs.CL]. URL: [https://arxiv.org/abs/2503.04598](https://arxiv.org/abs/2503.04598).  
Zhijian Zhuo 等人。《HybridNorm：通过混合归一化实现稳定高效的 Transformer 训练》。2025 年。arXiv: 2503.04598 [cs.CL]。URL: https://arxiv.org/abs/2503.04598。

19

第 19 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

# A Contributions  A 贡献

The authors are listed in order of the significance of their contributions, with those in project leadership roles appearing last.  
作者按贡献大小排序，项目负责人列于最后。

Guangyu Chen∗  陈光宇∗

Yu Zhang∗  张宇∗

Jianlin Su∗  苏剑林∗

Weixin Xu  徐伟新

Siyuan Pan  潘思源

Yaoyu Wang  王耀宇

Yucheng Wang  王宇成

Guanduo Chen  陈冠多

Bohong Yin  尹博宏

Yutian Chen  陈宇天

Junjie Yan  严俊杰

Ming Wei  明伟

Y. Zhang  张毅

Fanqing Meng  孟凡清

Chao Hong  洪超

Xiaotong Xie  谢小童

Shaowei Liu  刘绍伟

Enzhe Lu  卢恩哲

Yunpeng Tai  邰云鹏

Yanru Chen  陈彦如

Xin Men  辛门

Haiqing Guo  郭海清

Y. Charles  Y. 查尔斯

Haoyu Lu  卢浩宇

Lin Sui  隋琳

Jinguo Zhu  朱金国

Zaida Zhou  周再达

Weiran He  何蔚然

Weixiao Huang  黄伟晓

Xinran Xu  徐欣然

Yuzhi Wang  王玉志

Guokun Lai  赖国坤

Yulun Du  杜宇伦

Yuxin Wu  吴雨昕

Zhilin Yang  杨志林

Xinyu Zhou  周新宇

∗ Equal contribution  ∗ 同等贡献

20

第 20 页

Attention Residuals  注意力残差

TECHNICAL REPORT  技术报告

# B Optimized Inference I/O for Full Attention Residuals  
B 针对全注意力残差优化的推理 I/O

A naïve implementation of Full AttnRes scans all preceding layer outputs at every layer, so memory traffic scales linearly with depth. As noted in §4.2, however, the pseudo-query wl​ is a learned parameter independent of both the input and the hidden state. We can therefore batch inter-block accesses across layers in a two-phase schedule, bringing total I/O well below the naïve bound.  
全注意力残差连接的朴素实现会在每一层扫描所有前序层的输出，因此内存流量随深度线性增长。然而如§4.2 所述，伪查询 wl​ 是与输入和隐藏状态均无关的可学习参数。因此我们可以通过两阶段调度方案实现跨层的块间访问批处理，从而将总 I/O 控制在远低于朴素实现的上限。

Note that the block partition introduced below is purely an inference scheduling device. Unlike Block AttnRes, it leaves the model architecture unchanged and does not replace per-layer sources with block summaries; it simply makes the amortization argument concrete.  
请注意，下文引入的区块划分纯粹是一种推理调度机制。与区块注意力残差不同，它不会改变模型架构，也不会用区块摘要替换每层来源；它只是让摊销论证变得具体化。

Setup Let the model have L layers and hidden dimension d , partitioned into N contiguous blocks of size S=L/N . Inference proceeds one block at a time: Phase 1 jointly computes inter-block attention for all S layers in the block against all preceding blocks, and Phase 2 walks through intra-block dependencies sequentially.  
设置 假设模型有 L 层，隐藏维度为 d ，将其划分为 N 个连续块，每个块大小为 S=L/N 。推理过程每次处理一个块：第一阶段联合计算该块中所有 S 层与所有先前块之间的跨块注意力，第二阶段则按顺序处理块内依赖关系。

# Phase 1: Batched Inter-block Attention  
第一阶段：批量跨块注意力

Consider block n with its S layers. The queries {wl​}l∈Bn​​ are all known before execution begins, so the (n−1)S preceding key–value pairs need only be read once from HBM and reused across all S queries. The read cost for block n is therefore  
考虑块 n 及其 S 层。查询 {wl​}l∈Bn​​ 在执行开始前均已确定，因此 (n−1)S 之前的键值对只需从 HBM 读取一次，即可在所有 S 查询中重复使用。块 n 的读取成本因此为

Readi n t e r(n)​=2(n−1)Sd,(11)

where the factor of 2 accounts for both keys and values. Summing over all N blocks and using SN=L :  
其中因子 2 同时考虑了键和值。对所有 N 块求和并使用 SN=L ：

Readi n t e r​=n=1∑N​2(n−1)Sd=2Sd⋅2N(N−1)​=dL(N−1).(12)

d Writeinter(n)​=Sd

Writei n t e r​=Ld(13)

in total.  总计。

# Phase 2: Sequential Intra-block Attention  
第二阶段：顺序块内注意力

Phase 1 covers all sources before the current block. Within the block, however, each layer depends on those before it, so these must be handled in order. Layer t 1≤t≤S ) reads t−1 intra-block key–value pairs at a cost of 2(t−1)d . Summing over one block:  
第一阶段涵盖了当前块之前的所有源。然而，在块内部，每一层都依赖于其前面的层，因此必须按顺序处理这些层。第 t 层读取 1≤t≤S 个块内键值对，成本为 t−1 。对一个块进行求和：

Readi n t r a(n)​=t=1∑S​2(t−1)d=S(S−1)d.(14)

Phase 2 also writes one output per layer, so Writeintra(n)​=Sd .  
第二阶段也为每一层写入一个输出，因此 Writeintra(n)​=Sd 。

# Total Amortized I/O per Layer  
每层总摊销 I/O

Summing both phases over all N blocks:  
对所有 N 个区块的两个阶段求和：

Readt o t a l​=dL(N−1)+N⋅S(S−1)d,Writet o t a l​=2Ld.(15)

Dividing by L and using SN=L :  
除以 L 并使用 SN=L ：

R e a d=(N−1)d+(S−1)d=(S+N−2)d,W r i t e=2d,(16)

T o t a l I / O p e r l a y e r=(S+N)d.​(17)

Batching inter-block reads thus brings per-layer I/O from O(L) down to O(S+N) . The schedule follows the same two-phase split as Block AttnRes: inter-block attention accounts for the bulk of the traffic, while sequential computation stays local within each block.  
通过批量处理区块间读取，每层的 I/O 从 O(L) 降至 O(S+N) 。调度遵循与 Block AttnRes 相同的两阶段划分：区块间注意力占流量的大部分，而顺序计算则保持在每个区块内部本地进行。