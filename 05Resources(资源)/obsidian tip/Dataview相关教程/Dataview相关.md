# Obsidian Dataview插件使用教程

## 一、Dataview简介
**Dataview** 是Obsidian的一款强大数据查询插件，通过自定义查询语言（DQL）可以从笔记中提取元数据（如创建时间、标签、自定义字段），并以列表、表格、任务列表等形式展示，实现笔记内容的高效检索与可视化管理。其核心优势是通过代码化查询替代手动筛选，尤其适合知识管理、项目跟踪等场景。

---

## 二、安装与启用
[查看a-Dataview概述](a-Dataview概述.md)

---

## 三、基础概念
### 1. 查询类型（核心命令）
Dataview通过以下关键字定义查询结果的展示形式：
- `LIST`：列表（默认仅显示标题）
- `TABLE`：表格（可自定义多列字段）
- `TASK`：任务列表（自动识别Obsidian任务语法 `- [ ]`）
- `CALENDAR`：日历视图（按时间轴展示笔记）

## 三、基础概念
[查看b-Dataview基础概念](b-Dataview基础概念.md)

### 3. 操作符（条件过滤）
通过操作符筛选符合条件的笔记，常用操作符：
- `=` / `!=`：等于/不等于（如 `file.tags = "日记"`）
- `contains`：包含（如 `file.content contains "Vim"`）
- `and` / `or`：逻辑与/或（如 `file.ctime > date("2024-01-01") and file.tags = "项目"`）
- `sort`：排序（如 `sort file.ctime asc` 按创建时间升序排列）

---

## 四、常用查询示例
### 示例1：列出最近7天创建的日记
```dataview
LIST file.ctime
FROM #日记
WHERE file.ctime > date(today) - dur(7 days)
SORT file.ctime DESC
```
**效果**：显示最近一周内标签为“日记”的笔记标题及创建时间，按最新到最早排序。

### 示例2：用表格展示项目任务进度
```dataview
TABLE WITHOUT ID
  file.name AS 任务名称,
  "进度：" + progress(file.tasks) AS 完成度
FROM #项目
WHERE contains(file.tags, "任务")
```
**效果**：生成两列表格，第一列为任务名称，第二列显示任务完成百分比（需在笔记中使用 `- [ ]` 标记任务）。

### 示例3：筛选未完成的每日待办
```dataview
TASK
FROM #待办
WHERE !completed
SORT file.ctime ASC
```
**效果**：提取所有标签为“待办”且未完成（`- [ ]`）的任务，按创建时间排序展示。

---

## 五、高级技巧
### 1. 分组查询（GROUP BY）
按标签分组展示笔记数量：
```dataview
LIST length(rows) AS 笔记数
FROM ""
GROUP BY file.tags
```

### 2. 子查询（FLATTEN）
展开嵌套标签（如 `#项目/前端` 会被拆分为 `项目` 和 `前端`）：
```dataview
FLATTEN file.tags AS tag
LIST
FROM ""
WHERE tag != null
GROUP BY tag
```

### 3. 链接到笔记
在查询结果中添加笔记链接（点击可跳转）：
```dataview
LIST [[file.path]] AS 笔记链接
FROM #教程
```

---

## 练习与资源
- **新手建议**：从简单的 `LIST` 查询开始，逐步尝试添加 `WHERE` 过滤条件；
- **速查表**：可收藏 [Dataview官方文档](https://blacksmithgu.github.io/obsidian-dataview/) 作为参考；
- **社区示例**：Obsidian论坛或GitHub上有大量用户分享的查询模板，可直接复制修改使用。
