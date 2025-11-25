---
类型: "Resource"
状态: <% tp.system.suggester(["Inbox(收集箱)","To Review(待审阅)","Reviewed(已审阅)"], ["Inbox(收集箱)","To Review(待审阅)","Reviewed(已审阅)"] ,false, "选择任务状态") %>
url: <% tp.system.prompt("输入URL","") %>
描述: <% tp.system.prompt("输入资源描述","") %>
Files: 
Topics: 
Next Review: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
Favorate: false
归档: false
领域: <% tp.system.prompt("输入所属领域,例如:领域名称","'[[]]'") %>
Edited: <% tp.file.last_modified_date("YYYY-MM-DD HH:mm") %>
Created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
---
