---
title: 首页
created: <% tp.date.now("YYYY-MM-DD") %>
tags: [homepage, dashboard]
---

# 🧠 第二大脑首页

欢迎来到你的数字主脑！本页作为第二大脑的仪表盘，汇聚最重要的信息，帮助你快速切换工作、学习和生活各领域。建议将此页设置为 Obsidian 打开后的默认首页。

## 👤 个人简介与愿景

> 用一两句话概括你的使命和长期目标，比如：“通过持续学习与创造，成为更好的工程师和终身学习者。”
>
> 在此部分还可以列出当前的年度主题或座右铭。

## 🔥 当前关注（Active Focus）

使用 Dataview 自动列出所有处于进行状态的项目，助你随时关注重点。

```dataview
TABLE progress, due
FROM "Projects"
WHERE status = "active" OR status = "进行中"
SORT due asc
```

- 如果你按照 PARA 框架分类，可以修改查询路径为 `"02root/Projects"` 或你实际的项目目录。
- 为每个项目笔记在 YAML 中添加 `status: active`、`progress: 80%`、`due: 2025-12-31` 等字段，以便自动显示。

## ✅ 待办任务

结合 Tasks 插件或 Dataview，自动生成四个任务列表：逾期、今天、明天、即将到来。【908323798510052†L16-L33】

### 🔴 逾期

```tasks
not done
due before today
```

### 🟠 今天

```tasks
not done
due today
```

### 🟡 明天

```tasks
not done
due = tomorrow
```

### 🟢 即将到来（未来 7 天）

```tasks
not done
due after tomorrow and due before in 7 days
```

> 根据个人喜好，你还可以加上“购物清单/采购清单”等特殊清单，例如将 `#purchase` 标签用于待买物品，并在此使用 `tags includes purchase` 过滤。

## 📅 日常与回顾

- **今天的日记：**
  点击右侧按钮或使用 Daily Notes 插件快速创建/跳转到今日笔记。
  
- **最近更新：** 以下列表显示最近编辑的 5 个笔记，帮助你返回未完成的思路。

```dataview
LIST 5 FROM ""
WHERE file.mtime >= date(today) - dur(3 days)
SORT file.mtime desc
```

- **习惯与指标：** 如果每日笔记中有习惯打卡、运动时长等 YAML 字段，可以通过 Dataview 统计并在此展示表格或图表。

```dataview
TABLE sum(length) as TotalHours
FROM "03daily"
WHERE type = "daily" AND length
GROUP BY month(date)
```

## 📂 快捷导航

使用 callout 块或按钮（Button 插件）快速跳转到关键区域：

- [📥 收集箱 (Inbox)](01 Inbox)
- [📁 项目 (Projects)](02root/Projects)
- [🌐 领域 (Areas)](Areas)
- [📚 知识库 (Resources)](Resources)
- [🧾 归档 (Archives)](Archives)
- [📝 模板 (Templates)](Templates)

> 建议为每个重要目录创建索引笔记 (MOC)，例如 “Resources MOC.md”，并在此链接，以快速浏览目录下的内容。

## 🧭 学习与参考

这一区块用于存放你正在学习的技能或参考资料。通过 Dataview 自动从 `Resources` 目录中筛选出标记了 `learning: true` 的笔记：

```dataview
LIST FROM "Resources"
WHERE learning = true
```

你也可以嵌入外部插件，如 Map、Kanban 或 Canvas 来可视化知识结构；例如使用 Canvas 嵌入个人知识图谱或正在研究的主题【908323798510052†L69-L77】。

## 🏝️ 旅行/日程（可选）

如果你经常出差或旅行，可以参考 Vladimir Campos 的做法，在首页添加旅行计划列表和地图插件，将即将到来的行程集中展示【908323798510052†L34-L49】。

- 列出未来的旅行笔记或日程：

```dataview
LIST FROM "Trips"
WHERE date >= date(today)
SORT date asc
```

- 嵌入地图或行程链接，方便快速查看酒店、航班信息等。

## 🧰 工具与插件建议

为使首页更智能和美观，你可以启用以下插件：

- **Homepage 插件**：自动将此笔记设为 Obsidian 打开时的首页，并提供刷新按钮；支持将日记、任务等模块写入仪表盘。
- **Tasks 插件**：让上述任务列表自动更新。
- **Dataview**：实现基于 YAML 的数据查询和表格。
- **Buttons / Callout 栏**：制作带图标的快捷按钮。
- **Canvas**：可视化你的知识结构或项目概览，在首页嵌入画布。【908323798510052†L69-L77】
- **Calendar**/**Daily Notes**：快速创建日记并在首页显示节假日和计划。

## 🧹 定期维护与迭代

首页是动态的仪表盘，需要根据你的工作流不断调整：

- **每周检查收集箱**：将 Inbox 中的条目分类移动，保持清爽【859258168403466†L5-L27】。
- **更新项目状态**：在项目笔记的 front matter 中及时调整 `status` 和 `progress`，保证首页数据准确。
- **重组目录结构**：如果采用 PARA/PPAC 框架，在调整目录时记得修改首页中的查询路径。
- **适时增减板块**：当某些栏目不再重要，如暂停项目，可以隐藏相关板块；需要专注新的领域时再添加。

通过以上设计，你的主页不仅是笔记仓库的入口，更是凝聚注意力的仪表盘，兼具信息聚合、快速导航和数据分析功能。欢迎根据个人喜好和具体插件使用情况进行调整。
