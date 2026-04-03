---
tags:
  - "#obsidian/yaml"
type: reference
status: 🌿
---

> 基于社区最佳实践、PARA 框架与数字花园理念的调研与设计方案

---

## 一、调研背景

### 1.1 为什么需要 YAML 元数据

Obsidian 中的 YAML frontmatter 是笔记的"结构化描述层"，它让笔记从"纯文本文件"升级为"可查询、可分类、可追踪的知识单元"。核心价值：

- **Bases/Dataview 查询基础**：所有视图的筛选、分组、排序都依赖 frontmatter 字段
- **笔记发现性**：通过 `tags`、`type` 等字段快速定位笔记
- **生命周期管理**：通过 `status` 跟踪笔记的成熟度，避免知识腐化
- **未来兼容**：Obsidian 官方正将 Dataview 功能整合为核心 Bases 插件，YAML frontmatter 是其唯一数据源

### 1.2 调研来源

| 来源                                                                                                                      | 核心观点                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [Obsidian 官方文档 - Properties](https://help.obsidian.md/properties)                                                       | 原生支持 6 种属性类型：text / number / checkbox / date / datetime / list，默认属性为 `tags`、`aliases`、`cssclasses` |
| [Obsidian 论坛 - Properties Best Practices](https://forum.obsidian.md/t/obsidian-properties-best-practices-and-why/63891) | 社区共识：核心分类应包含 `type`、`tags`、`status`；字段不宜超过 5-7 个；避免成为"元数据管理员"                                      |
| [CSDN - 深入解析 Obsidian 元数据属性](https://blog.csdn.net/m0_73640344/article/details/147260246)                               | 推荐常用字段：title / date / tags / category / author / status / priority；强调命名一致性                         |
| [PKMer - Obsidian 的 YAML 和 Frontmatter](https://pkmer.cn/)                                                              | 中文社区实践：建议结合 PARA 原则，使用模板自动填充元数据                                                                    |
| [Rob Coles - 从 Dataview 迁移到 Bases](https://robcoles.net/)                                                               | Dataview 已停止积极开发，建议迁移至 Bases + YAML frontmatter；使用 Meta Bind 插件实现行内元数据可见性                          |
| [Maggie Appleton - Growing the Evergreens](https://maggieappleton.com/evergreens)                                       | 数字花园笔记成熟度模型：Seedling → Budding → Evergreen                                                         |
| [Agile Path - 笔记成熟度模型](https://digital-garden.ontheagilepath.net/)                                                      | 六级成熟度：🌰 Nut → 🌱 Seedling → 🪴 Potted → 🌳 Tree → 🍁 Ancient → 🍂 Fallen                          |
| [Wanderloots - Tags & Topic Notes](https://wanderloots.xyz/)                                                            | 混合策略：用 tags 标记类型和状态，用 topic notes 构建知识网络                                                           |

---

## 二、设计原则

### 2.1 三个核心原则

```
高内聚：每个字段有且仅有一个职责，不交叉
低耦合：字段之间无依赖，与文件夹位置无关
渐进式：最小可用只需 tags，其余按需添加
```

### 2.2 反模式（应避免）

| 反模式 | 问题 | 正确做法 |
|--------|------|----------|
| 在 YAML 中编码文件夹信息 (`category: project`) | 与目录结构重复，搬移文件时需同步修改 | 文件夹已表达归属，不重复编码 |
| 为不同目录设计不同 schema | 维护成本高，跨目录查询困难 | 全仓库统一一套 schema |
| 字段过多（>7个） | 每次新建笔记负担重，沦为"元数据管理员" | 核心字段 ≤ 5 个，其余按需扩展 |
| 嵌套 YAML 结构 | Obsidian Properties UI 不支持嵌套，会被转为 JSON 降低可读性 | 使用扁平结构 |
| 硬编码枚举值过多 | type 值过于细分导致分类困难 | 保持 5-6 个取值，用 tags 补充细粒度 |

---

## 三、字段设计方案

### 3.1 字段总览

| 字段        | 类型   | 必要性    | 职责   | 说明                            |
| --------- | ---- | ------ | ---- | ----------------------------- |
| `tags`    | list | **必要** | 主题分类 | 唯一的内容分类维度，Bases 筛选/分组核心       |
| `type`    | text | 推荐     | 笔记形态 | 描述"这是什么形式的笔记"，与 tags 正交       |
| `status`  | text | 推荐     | 成熟度  | 笔记生命周期阶段，值为 emoji（🌱/🌿/🌳）  |
| `source`  | text | 可选     | 来源追溯 | URL / 书名 / 论文标题，仅外部内容需要       |
| `created` | date | 可选     | 创建时间 | 导入旧笔记时有用，新笔记可由模板自动填充          |
| `aliases` | list | 可选     | 别名   | Obsidian 原生支持，方便搜索和 `[[]]` 链接 |

### 3.2 `type` 取值设计

设计思路：描述笔记的**形态**（它是什么），而非**主题**（它关于什么）。主题交给 `tags` 处理。

| 值           | 含义             | 典型场景                              |
| ----------- | -------------- | --------------------------------- |
| `note`      | 知识笔记 / 概念卡片    | 钩子（hook）.md、向量加法.md               |
| `moc`       | MOC 索引页 / 知识地图 | 00LLM_Map.md、Claude Code Tools.md |
| `reference` | 外部参考资料         | 转载的论文、教程、文档                       |
| `prompt`    | 提示词 / 模板       | 系统指令提示词.md、测试提示词.md               |
| `log`       | 记录 / 日志        | 每日笔记、会议记录                         |

**为什么不再细分？** 社区经验表明，type 值超过 6 个会导致分类犹豫（"这到底算 article 还是 tutorial？"）。用 `tags` 补充细粒度即可。

### 3.3 `status` 取值设计

采用数字花园（Digital Garden）社区广泛认可的成熟度模型，**直接使用 emoji 作为值**，兼顾视觉直觉与输入效率：

| 值   | 含义  | 说明              |
| --- | --- | --------------- |
| 🌱  | 萌芽  | 刚创建的想法碎片，尚未展开   |
| 🌿  | 成长中 | 正在完善，内容可能不完整或有误 |
| 🌳  | 常青  | 成熟稳定，可长期引用和分享   |

写法示例：`status: 🌱`

**为什么用 emoji 而非英文？**
- 在 Bases/Dataview 表格中一目了然，无需额外映射
- Obsidian Properties 面板原生支持 emoji 值
- 输入成本低：设定好输入法快捷短语后，比拼写 `seedling` 更快

**为什么只要 3 级？**
- [Maggie Appleton 的模型](https://maggieappleton.com/evergreens) 使用 3 级（Seedling / Budding / Evergreen），实践证明最易坚持
- 6 级模型（如 Nut → Seedling → Potted → Tree → Ancient → Fallen）过于细致，判定标准模糊
- 3 级的认知负担最低：写的时候一秒就能判断

### 3.4 字段间正交性分析

```
tags  ── 回答 "关于什么主题？"    （LLM/Agent / 数学 / 编程）
type  ── 回答 "什么形式？"        （note / moc / reference / prompt / log）
status── 回答 "什么阶段？"        （🌱 / 🌿 / 🌳）
```

三个维度完全正交，任意组合都有意义：
- `tags: [LLM/Agent]` + `type: moc` + `status: 🌳` → Agent 领域的成熟索引页
- `tags: [编程/Python]` + `type: reference` + `status: 🌱` → 刚收集的 Python 参考资料

---

## 四、Tags 层次化设计（重点）

### 4.1 问题：扁平标签为什么会"失效"

当知识体系还浅时，`tags: [LLM]` 足够用。但随着学习深入：

```
初期：10 篇笔记都标 LLM        → 标签有区分度
中期：50 篇笔记都标 LLM        → 标签退化为噪声，等于没标
后期：RAG/Agent/训练/评估 各成体系 → 需要更细粒度的分类
```

**核心矛盾**：标签粒度固定，但知识粒度在持续细化。

### 4.2 解法：Obsidian 嵌套标签（Nested Tags）

Obsidian 原生支持用 `/` 分隔的嵌套标签：

```yaml
tags: [LLM/Agent]       # Agent 是 LLM 的子领域
tags: [LLM/RAG]         # RAG 是 LLM 的子领域
tags: [编程/Python]      # Python 是编程的子领域
```

**关键特性**：搜索 `#LLM` 会自动匹配所有子标签（`#LLM/Agent`、`#LLM/RAG` 等），兼顾粗粒度和细粒度。

### 4.3 标签树设计

基于当前仓库内容，设计如下标签树。**只定义前两层**，第三层按需自然生长：

```
LLM/                        # 大模型总领域
├── LLM/Agent               # Agent 开发
├── LLM/RAG                 # 检索增强生成
├── LLM/PromptEng           # 提示词工程
├── LLM/Eval                # 模型评估（OpenCompass 等）
├── LLM/Training            # 模型训练（微调、RLHF 等）
└── LLM/DeepLearning        # 深度学习基础

数学/                        # 数学总领域
├── 数学/线性代数
├── 数学/概率论
└── 数学/因果推理             # 含 PCD、SCM 等

编程/                        # 编程总领域
├── 编程/Python
├── 编程/Git
└── 编程/OOP

Obsidian/                   # 工具知识
├── Obsidian/Plugin
└── Obsidian/CSS
```

### 4.4 标签使用规则

| 规则               | 说明                  | 示例                                  |
| ---------------- | ------------------- | ----------------------------------- |
| **能细则细**         | 只要能归入子标签，就不用父标签     | 用 `LLM/Agent` 而非 `LLM`              |
| **不确定就粗**        | 暂时不知归属的，先打父标签，以后再细化 | 先标 `LLM`，日后改为 `LLM/RAG`             |
| **可多标签**         | 跨领域笔记可以打多个标签        | `tags: [LLM/RAG, 编程/Python]`        |
| **不重复父子**        | 不要同时标父和子            | `tags: [LLM, LLM/Agent]` ✗          |
| **用 `/` 不用 `-`** | 层级用斜杠表示，连字符用于复合词    | `LLM/PromptEng` ✓，`LLM-PromptEng` ✗ |

### 4.5 标签演化示例

以 LLM 领域为例，展示知识深入过程中标签的自然演化：

```
阶段 1（入门期）：
  所有笔记 → tags: [LLM]

阶段 2（分化期）：开始区分子方向
  Agent 笔记     → tags: [LLM/Agent]
  RAG 笔记       → tags: [LLM/RAG]
  其他仍然       → tags: [LLM]

阶段 3（成熟期）：子方向进一步分化
  ReAct 笔记     → tags: [LLM/Agent/ReAct]
  向量检索笔记   → tags: [LLM/RAG/Retrieval]
```

**关键点**：不需要提前规划完整标签树。先粗后细，让标签跟着知识生长。

---

## 五、Tag → MOC 升级机制

### 5.1 什么时候创建 MOC

当某个标签下的笔记达到**阈值**时，说明这个主题已经积累了足够的内容，值得创建一个 MOC（Map of Content）来组织它们。

| 信号       | 说明                   |
| -------- | -------------------- |
| **数量阈值** | 某个子标签下有 **7~10 篇**笔记 |
| **导航困难** | 搜索该标签后需要逐条翻找，无法快速定位  |
| **结构涌现** | 笔记之间开始出现明确的层次或依赖关系   |

### 5.2 升级流程

```
1. 发现 tags: [LLM/Agent] 的笔记已有 10+ 篇
2. 创建 MOC 页面（如 LLM工程_Agent_Map.md）
3. MOC 的 frontmatter：
   ---
   tags: [LLM/Agent]
   type: moc
   status: 🌿
   ---
4. 在 MOC 中用 [[]] 双链组织该标签下的笔记
5. 将 MOC 挂载到上级 MOC（如 00LLM_Map.md 中嵌入）
```

### 5.3 MOC 与标签的关系

```
标签 = 自动分类（metadata 驱动，Bases/Dataview 自动聚合）
MOC  = 人工策展（手动组织结构、添加说明、划分层次）
```

两者不冲突，而是互补：
- **标签**负责"找到所有相关笔记"（机器擅长）
- **MOC** 负责"告诉你应该先看什么、怎么看"（人类擅长）

一个标签是否需要升级为 MOC，取决于"自动聚合是否已经不够用了"。

### 5.4 当前仓库已有的 MOC 示例

| 文件 | 标签 | 说明 |
|------|------|------|
| `00LLM_Map.md` | `LLM` | LLM 总入口，嵌入各子领域 Map |
| `LLM工程_Agent_Map.md` | `LLM/Agent` | Agent 子领域索引 |
| `LLM工程_RAG工程_Map.md` | `LLM/RAG` | RAG 子领域索引 |
| `LLM工程_提示词工程_Map.md` | `LLM/PromptEng` | 提示词工程索引 |
| `Claude Code Tools.md` | `编程/ClaudeCode` | Claude Code 工具索引 |

---

## 六、模板集成

### 6.1 Templater 新建笔记模板

```yaml
---
tags: []
type: note
status: 🌱
created: <% tp.date.now("YYYY-MM-DD") %>
---
```

### 6.2 日记模板

```yaml
---
tags:
  - daily
type: log
created: <% tp.date.now("YYYY-MM-DD") %>
focus: <%*promptValue = await tp.system.prompt("输入今日要focus的项目", "[[]]");  tR += promptValue; %>
---
```

### 6.3 MOC 索引页模板

```yaml
---
tags: []
type: moc
status: 🌿
created: <% tp.date.now("YYYY-MM-DD") %>
---
```

### 6.4 外部参考资料模板

```yaml
---
tags: []
type: reference
status: 🌱
source: ""
created: <% tp.date.now("YYYY-MM-DD") %>
---
```

---

## 七、与 Bases 视图的联动

### 7.1 当前 Base 配置如何利用这些字段

| Base 视图   | 可用的 YAML 字段 | 用法                      |
| --------- | ----------- | ----------------------- |
| 所有视图      | `file.tags` | 作为列展示，或作为 groupBy 的替代维度 |
| Project   | `type`      | 区分项目文档 vs 笔记 vs 提示词     |
| Areas     | `status`    | 筛选 🌳 常青笔记，聚焦成熟知识  |
| Resources | `source`    | 展示参考资料来源                |

### 7.2 示例：按 status 筛选的 Base 查询

```yaml
filters:
  and:
    - file.folder.containsAny("04Areas(领域)")
    - status == "🌳"
```

### 7.3 示例：按嵌套标签筛选

```yaml
# Bases 中可通过 tags 字段筛选特定子领域
filters:
  and:
    - file.tags.containsAny("LLM/Agent")
```

---

## 八、渐进式落地策略

### 8.1 不要一次性给所有笔记补全元数据

社区最强烈的建议：**不要试图一口气给几百篇笔记补上 YAML**。

推荐策略：

| 阶段 | 行动 | 预期时间 |
|------|------|----------|
| **立即** | 修改 Templater 模板，新建笔记自动带 YAML | 5 分钟 |
| **按需** | 每次打开旧笔记时，顺手补上 `tags` 和 `type` | 持续进行 |
| **批量** | 对重点目录（如 Areas/LLM/）集中补全 | 按需安排 |

### 8.2 命名规范

| 规则 | 说明 |
|------|------|
| 字段名用英文小写 | `tags` 而非 `Tags` 或 `标签`（Obsidian 大小写敏感） |
| 值用 emoji 或英文小写 | `status: 🌱` 或 `type: note`（便于查询匹配） |
| tags 用嵌套格式 | `tags: [LLM/Agent]`（利用 Obsidian 嵌套标签特性） |
| tags 值可中英混用 | `tags: [LLM/Agent, 数学/线性代数]`（兼顾可读性和检索） |

---

## 九、总结

| 维度        | 选择                                 | 理由                     |
| --------- | ---------------------------------- | ---------------------- |
| 字段数量      | 6 个（3 核心 + 3 可选）                   | 社区共识：≤7 个，避免管理负担       |
| type 取值   | 5 种（note/moc/reference/prompt/log） | 描述形态不描述主题，与 tags 正交    |
| status 模型 | 3 级 emoji（🌱/🌿/🌳）                | 花园模型 + emoji 直觉，认知负担最低 |
| tags 策略   | 嵌套标签 `LLM/Agent`                   | 支持知识细化，搜索自动包含子标签       |
| Tag→MOC   | 7~10 篇阈值触发                         | 标签负责聚合，MOC 负责策展        |
| 落地策略      | 渐进式                                | 模板自动化 + 按需补全，不做一次性迁移   |
| 与文件夹的关系   | 完全解耦                               | YAML 不编码位置信息，笔记可自由移动   |

---

> 参考资料
> - [Obsidian Properties 官方文档](https://help.obsidian.md/properties)
> - [Obsidian 论坛 - Properties Best Practices](https://forum.obsidian.md/t/obsidian-properties-best-practices-and-why/63891)
> - [Maggie Appleton - Growing the Evergreens](https://maggieappleton.com/evergreens)
> - [CSDN - 深入解析 Obsidian 元数据属性](https://blog.csdn.net/m0_73640344/article/details/147260246)
> - [PKMer - Obsidian 的 YAML 和 Frontmatter](https://pkmer.cn/)
> - [Rob Coles - 从 Dataview 迁移到 Bases](https://robcoles.net/posts/dataview-and-inline-to-datacore-bases-and-yaml/)
> - [Agile Path - 笔记成熟度模型](https://digital-garden.ontheagilepath.net/maturity-model-for-my-obsidian-notes)
> - [Wanderloots - Tags & Topic Notes 组织策略](https://wanderloots.xyz/)