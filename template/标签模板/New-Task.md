---
每日亮点: <% tp.system.suggester(["true", "false"], ["true", "false"],false,"是否为每日亮点?") %>
类型: "Task"
状态: <% tp.system.suggester(["To Do(代办)", "Completed(已完成)"], ["To Do(代办)", "Completed(已完成)"], false, "选择任务状态") %>
进度: <% tp.system.suggester(["Inbox(收集箱)", "Someday(待定 / 择日)", "Waiting(等待中)", "Next Action(下一步行动)", "Completed(已完成)", "Delegated(已委派)", "Eliminated(已废弃/已取消)"], ["Inbox(收件箱)", "Someday(待定 / 择日)", "Waiting(等待中)", "Next Action(下一步行动)", "Completed(已完成)", "Delegated(已委派)", "Eliminated(已废弃/已取消)"], false, "选择任务进度") %>
截止日期: <% tp.date.now("YYYY-MM-DD",7) %>
项目: <% tp.system.prompt("输入所属项目,例如:项目名称", "项目") %>
情境: <% tp.system.suggester(["Home Computer", "Laptop", "Phone", "Pad", "Company"], ["Home Computer", "Laptop", "Phone", "Pad", "Company"], false, "选择情境") %>
优先级: <% tp.system.suggester(["Low", "Medium", "High", "Urgent"], ["Low", "Medium", "High", "Urgent"], false, "选择优先级") %>
精力: <% tp.system.suggester(["Low Energy", "Medium Energy", "High Energy", "Extreme Energy"], ["Low Energy", "Medium Energy", "High Energy", "Extreme Energy"], false, "选择所需精力") %>
url: <% tp.system.prompt("输入URL","") %>
描述: <% tp.system.prompt("输入任务描述","") %>
父任务: <% tp.system.prompt("输入父任务,例如:父任务名称","'[[]]'") %>
事件: <% tp.system.prompt("输入关联事件,例如:事件名称","'[[]]'") %>
领域: <% tp.system.prompt("输入所属领域,例如:领域名称","'[[]]'") %>
目标: <% tp.system.prompt("输入关联目标,例如:目标名称","'[[]]'") %>
Edited: <% tp.file.last_modified_date("YYYY-MM-DD HH:mm") %>
Created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
---
 ###### 关联
添加[[Rescources]]       添加[[Notes]]       添加[[Sub-task]]

---
