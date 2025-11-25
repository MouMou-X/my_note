---
类型: "Event"
日期: 
持续时间(分钟): 
出席者: <% tp.system.prompt("输入出席者姓名,例如:行嗔", "") %>
Meeting Link: 
描述: <% tp.system.prompt("输入会议描述","") %>
---
###### 关联
添加[[tasks]]

---
# Notes
---
- 项目


# Action Items
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
