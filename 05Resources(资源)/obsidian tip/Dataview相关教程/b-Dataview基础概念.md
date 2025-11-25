# b-Dataview基础概念

## 一、核心概念
Dataview通过查询语法从笔记元数据中提取信息，主要涉及字段、查询类型和过滤条件。

## 二、常用字段（数据来源）
字段用于提取笔记的元数据，常见内置字段包括：
- `file.name`：笔记文件名（不带.md后缀）
- `file.path`：笔记完整路径（如 `Dataview相关教程/a-Dataview概述`）
- `file.ctime`：笔记创建时间（格式：YYYY-MM-DD HH:MM）
- `file.mtime`：笔记最后修改时间
- `file.tags`：笔记标签（如 `#教程` 会被识别为数组 `["教程"]`）
- `file.inlinks`：指向当前笔记的反向链接（其他笔记中的[[链接]]）

[返回a-Dataview概述](a-Dataview概述.md)