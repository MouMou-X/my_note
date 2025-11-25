---
类型: "Project"
状态: <% tp.system.suggester(["Inbox(收集箱)","Not Started(未开始)","In Progress(进行中)","On Hold(暂缓)","Completed(已完成)"],["Inbox(收件箱)","Not Started(未开始)","In Progress(进行中)","On Hold(暂缓)","Completed(已完成)"], false, "选择任务状态") %>
领域: <% tp.system.prompt("输入所属领域,例如:领域名称","'[[]]'") %>
目标: <% tp.system.prompt("输入关联目标,例如:目标名称","'[[]]'") %>
开始日期: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
截至日期: <% tp.file.creation_date("YYYY-MM-DD HH:mm",7) %>
优先级: <% tp.system.suggester(["Low", "Medium", "High", "Urgent"], ["Low", "Medium", "High", "Urgent"], false, "选择优先级") %>
归档: false
Edited: <% tp.file.last_modified_date("YYYY-MM-DD HH:mm") %>
Created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
---
 ###### 关联
添加[[Rescources]]       添加[[Notes]]       添加[[Tasks]]

---

```dataview
TABLE
  file.link AS "任务名称",
  截止日期 AS "截止日期",
  优先级 AS "优先级",
  进度 AS "进度"
WHERE
  类型 = "Task" OR contains(file.tags, "Task") OR contains(file.tags, "类型/Task")
SORT
  截止日期 ASC, 优先级 DESC
```

