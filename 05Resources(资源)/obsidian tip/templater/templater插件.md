
- 官方手册网站
- https://silentvoid13.github.io/Templater/
- obsidian开发者手册
- https://docs.obsidian.md/Reference/TypeScript+API/App
# 1.简介
## 1.1术语
为了理解templater的工作原理，让我们定义几个术语：
- 模板是一个包含==命令的文件==。
- 以开始标记、结束标记`<% %>`的文本片段成为命令。
- 函数是我们可以在==命令==内部调用的对象，它返回一个值(替换字符串)。
有两种函数类型
- 内部函数：插件内置的预定义函数。例如<% tp.date.now %>是一个返回当前日期的内部函数
- 用户函数：自定义函数。它可以是系统命令，也可以是用户脚本。
> [!example] 示例
> 昨天：<% tp.date.yesterday %>
> 明天：<% tp.date.tomorrow %>

---
## 1.2语法
**Templater 的所有功能都是使用命令**调用的 JavaScript 对象。
### 1.2.1命令语法

命令**必须**同时具有开始标记`<%`和结束标记`%>`。
使用内部函数的完整命令`tp.date.now`如下：`<% tp.date.now() %>`
### 1.2.2函数语法
#### 对象层次结构
Templater 的所有函数，无论是内部函数还是用户函数，都可以在`tp`对象下使用。你可以说，我们所有的函数都是`tp`对象的子级。要访问对象的“子级”，我们必须使用点符号`.`

这意味着 Templater 函数调用总是以`tp.<something>`
##### 函数调用
调用函数，我们需要使用特定于函数调用的语法：在函数名称后面附加一个左括号和一个右括号。
作为示例，我们将使用它`tp.date.now()`来调用`tp.date.now`内部函数。
函数可以包含参数和可选参数。它们位于左括号和右括号之间，如下所示：
`tp.date.now(arg1_value, arg2_value, arg3_value, ...)`

所有参数必须按照正确的顺序传递。
函数的参数可以有不同的**类型**。以下是函数可能类型的非详尽列表：

- 类型`string`意味着值必须放在单引号或双引号内（`"value"`或`'value'`）
- 类型`number`意味着值必须是整数（`15`，，`-5`...）
- 类型`boolean`意味着值必须是或`true`（`false`完全小写），而不能是其他。

调用函数时必须尊重参数的类型，否则它将无法工作。
#### 函数文档语法
Templater 内部函数的文档使用以下语法：
```js
tp.<my_function>(arg1_name: type, arg2_name?: type, arg3_name: type = <default_value>, arg4_name: type1|type2, ...)
```
- `arg_name`代表参数的**符号名称，以了解它是什么。**
- `type`表示参数的预期类型。调用内部函数时必须遵循此类型，否则会抛出错误。
如果参数是可选的，则会附加一个问号?，例如`arg2_name?: type`
如果参数具有默认值，则使用等号指定=，例如`arg3_name: type = <default_value>`。
如果参数可以有不同的类型，则将使用管道指定`|`，例如`arg4_name: type1|type2`
##### 语法警告
调用函数时，无需指定参数的名称、类型或默认值。只需指定参数的值，详情请见[此处](templater插件.md#函数调用)
> [!example] 示例
> `tp.date.now(format?: string = "YYYY-MM-DD", offset?: number|string, reference?: string, reference_format?: string)`
> 
> 此内部函数有 4 个可选参数：
> - type类型的格式`string`，默认值为`"YYYY-MM-DD"`。
> - type类型`number`或类型的偏移量`string`。
> - type类型的引用`string`。
> - type类型的reference_format `string`。
> 
> 这意味着此内部函数的**有效调用**是：
> 
> - `<% tp.date.now() %>`
> - `<% tp.date.now("YYYY-MM-DD", 7) %>`
> - `<% tp.date.now("YYYY-MM-DD", 7, "2021-04-09", "YYYY-MM-DD") %>`
> - `<% tp.date.now("dddd, MMMM Do YYYY", 0, tp.file.title, "YYYY-MM-DD") %>`*假设文件名的格式为：“YYYY-MM-DD”
> 
另一方面，**无效的调用**包括：
> 
> - `tp.date.now(format: string = "YYYY-MM-DD")`
> - `tp.date.now(format: string = "YYYY-MM-DD", offset?: 0)`

## 1.3设置
### 1.3.1常规设置
- `Template folder location`：此文件夹中的文件将可用作模板。
- `Syntax Highlighting on Desktop`[在编辑模式下为模板](https://github.com/SilentVoid13/Templater)命令添加语法高亮显示。
- `Syntax Highlighting on Mobile`[在移动设备的编辑模式下，为Templater](https://github.com/SilentVoid13/Templater)命令添加了语法高亮功能。请谨慎使用：这可能会破坏移动平台上的实时预览。
- `Automatic jump to cursor``tp.file.cursor`插入模板后自动触发。您也可以设置热键手动触发`tp.file.cursor`。
- `Trigger Templater on new file creation`：Templater会监听新文件创建事件，如果匹配您设置的规则，则会替换新文件内容中找到的所有命令。这使得Templater与其他插件兼容，例如每日笔记核心插件、日历插件、评论插件、笔记重构插件等。
    - 确保在下面的文件夹模板或文件正则表达式模板下设置规则。
    - **警告：**如果您创建的文件包含未知/不安全的内容，则可能会很危险。请确保每个新文件的内容在创建时都是安全的。

### 1.3.2模板热键
模板热键允许您将模板绑定到热键。

### 1.3.3文件夹模板
**注意**：此设置默认隐藏。要查看它，请先启用此`Trigger Template on new file creation`设置。由于它与“文件正则表达式模板”互斥，因此启用其中一个会禁用另一个。

您可以指定一个模板，该模板将自动应用于所选文件夹及其子`Folder Templates`文件夹。系统将使用最深匹配，因此规则的顺序无关紧要。

`/`如果您需要全部捕获，请为“ ”添加一条规则。

### 1.3.4文件正则表达式模板
**注意**：此设置默认隐藏。要查看它，请先启用此`Trigger Template on new file creation`设置。由于它与文件夹模板互斥，因此启用其中一个会禁用另一个。

您可以指定用于测试新文件路径的正则表达式声明。如果正则表达式匹配，则自动使用关联的模板。规则将按从上到下的顺序进行测试，并使用第一个匹配项。

`.*`如果您需要一个包罗万象的规则，请以“ ”的规则结尾。

[使用Regex101](https://regex101.com/)之类的工具来验证您的[[正则表达式]]。

### 1.3.5启动模板
启动模板是 Templater 启动时将执行一次的模板。
这些模板不会输出任何东西。
例如，这个功能可以用来设置模板，从而为 Obsidian 的事件添加[[钩子（hook）]]。

### 1.3.6用户脚本函数
> [!danger] 待处理 在3 用户功能处完善
> 此文件夹中的所有 JavaScript 文件都将作为 CommonJS 模块加载，以导入自定义[用户函数](https://silentvoid13.github.io/Templater/user-functions/overview.html)。
该文件夹需要能够从保管库访问。
查看[文档](https://silentvoid13.github.io/Templater/user-functions/script-user-functions.html)以获取更多信息。

### 1.3.7用户系统命令功能
> [!danger] 待处理 在3 用户功能处完善
> 允许您创建与系统命令链接的[用户功能。](https://silentvoid13.github.io/Templater/user-functions/overview.html)
> 查看[文档](https://silentvoid13.github.io/Templater/user-functions/system-user-functions.html)以获取更多信息。
> **警告：从不受信任的来源执行任意系统命令可能非常危险。请仅运行来自受信任来源且您理解的系统命令。**

## 1.4常见问题
### Unicode 字符（表情符号等）在 Windows 上不起作用？
`cmd.exe`并且`powershell`在 Windows 上已知存在 unicode 字符问题。
您可以查看 https://github.com/SilentVoid13/Templater/issues/15#issuecomment-824067020 寻找解决方案。
另一个好的解决方案（可能是最好的）是使用[Windows 终端](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701)并将其设置为 Templater 设置中的默认 shell。
包含可能适合您的解决方案的另一个资源：[https：//stackoverflow.com/questions/49476326/displaying-unicode-in-powershell](https://stackoverflow.com/questions/49476326/displaying-unicode-in-powershell)

# 2.Internal Functions(内置功能)
## 2.1. tp.app
> [!danger] 待处理 
> 此模块公开应用实例。建议使用此模块，而非全局应用实例。
> 这在编写脚本时非常有用。
> 有关更多信息，请参阅 Obsidian[开发者文档。](https://docs.obsidian.md/Reference/TypeScript+API/App)
> > [!example] 示例
## 2.2. tp.config
<% tp.web.random_picture("1920x1280","Nature,Travel") %>
## 2.3. tp.date
## 2.4. tp.file
## 2.5. tp.frontmatter
## 2.6. tp.hooks
## 2.7. tp.obsidian
## 2.8. tp.system
## 2.9. tp.web(web模块)
该模块包含与网络（发出网络请求）相关的每个内部功能。
- [文档](templater插件.md#)
    - [`tp.web.daily_quote()`](templater插件.md#2.9.2tp.web.daily_quote())
    - [`tp.web.random_picture(size?: string, query?: string, include_size?: boolean)`](templater插件.md#2.9.3tp.web.random_picture())
    - [`tp.web.request(url: string, path?: string)`](templater插件.md#2.9.4tp.web.request())
- [示例](templater插件.md#)
### 2.9.1文档
函数文档使用特定的语法。更多信息[请点击此处](templater插件.md#函数文档语法)。
### 2.9.2tp.web.daily_quote()
检索并解析每日报价`https://github.com/Zachatoo/quotes-database`作为标注。
> [!example] 示例
> ```js
> // Daily quote
> <% await tp.web.daily_quote() %>
> ```
### 2.9.3tp.web.random_picture()
从中获取随机图像`https://unsplash.com/`。
#### 参数
- `size`：格式的图像大小`<width>x<height>`。
    
- `query`：将选择范围限定为符合搜索词的照片。多个搜索词可以用逗号分隔。
    
- `include_size`：可选参数，用于在图片链接 Markdown 中包含指定尺寸。默认为 false。
> [!example] 示例
> ```js
> // Random picture
> <% await tp.web.random_picture() %>
> // Random picture with size
> <% await tp.web.random_picture("200x200") %>
> // Random picture with size and query
> <% await tp.web.random_picture("200x200", "landscape,water") %>
> ```
### 2.9.4tp.web.request()
向指定的 URL 发出 HTTP 请求。您也可以选择指定路径，以便从响应中提取特定数据。
#### 参数
- `url`：将向其发出 HTTP 请求的 URL。
    
- `path`：响应 JSON 中的路径，用于提取特定数据。
> [!example] 示例
> ```js
> // Simple request
> <% await tp.web.request("https://jsonplaceholder.typicode.com/todos/1") %>
> // Request with path
> <% await tp.web.request("https://jsonplaceholder.typicode.com/todos", "0.title") %>
> ```
### 示例
> [!example] 示例
> ```js
> // Daily quote
><% await tp.web.daily_quote() %>
>
>// Random picture
><% await tp.web.random_picture() %>
>// Random picture with size
> <% await tp.web.random_picture("200x200") %>
> // Random picture with size and query
> <% await tp.web.random_picture("200x200", "landscape,water") %>
>
> // Simple request
> <% await tp.web.request("https://jsonplaceholder.typicode.com/todos/1") %>
> // Request with path
> <% await tp.web.request("https://jsonplaceholder.typicode.com/todos", "0.title") %>
> ```
## 2.10. Contributing

---

# 关于modified_date的实时更新
- [ ] linter插件

# b站Chris教程(存疑待整理，需要按照官网手册语法)
## tp.file(与文件相关的操作)
- 插入文件标题
	- <% tp.file.title %> 
- 插入文件创建时间
	- <% tp.file.creation_date("YYYY-MM-DD") %> 
- 插入修改日期时间
	- <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
---
## tp.date(与日期相关的操作)
- 插入今天的日期
	- <% tp.date.now("YYYY-MM-DD") %>
	- 现在的日期，格式如：2025-05-29
		- <% tp.date.now() %>
	- 现在的日期，格式如：29日 五月 2025
		- <% tp.date.now("Do MMMM YYYY") %>
	- 上周的日期
		- <% tp.date.now("YYYY-MM-DD", -7) %>
	- 下周的日期
		- <% tp.date.now("YYYY-MM-DD", 7) %>
	- 上个月的日期（30天）
		- <% tp.date.now("YYYY-MM-DD", "P-1M") %>
	- 下一年的日期
		- <% tp.date.now("YYYY-MM-DD", "P1Y") %>
- 插入明天的日期
	- <% tp.date.tomorrow("YYYY-MM-DD") %>
- 插入昨天的日期
	- <% tp.date.yesterday("YYYY-MM-DD") %>
---
## tp.data()
https://gemini.google.com/app/bd609260d57e2183


---
## tp.system(弹出对话框)
- <% tp.system.prompt("请输入作者") %>
- <% tp.system.suggester(["to_read","reading","done"],["待阅读","阅读中","已阅读",ture,'status']) %>
- prompt弹出输入框
- suggester弹出选择框
	- 第一个`[]`是选择框现实的内容
	- 第二个`[]`是选择后，输入的对应文本
	- true代表，如果不选择选项退出笔记的情况下，不创建笔记
	- ''中的内容提示你这个输入框是干什么的
---
## 变量值
- 日期

---



# ~~templater插件设置~~
**Templater** (插件名称)

---

Template folder location

模板文件夹位置

Files in this folder will be available as templates.

此文件夹中的文件将可用作模板。

(右侧有一个搜索框，显示 test/template，表示当前设置的模板文件夹路径。)

---

Internal variables and functions

内部变量和函数

Templater provides multiples predefined variables / functions that you can use.

Templater 提供了多个预定义的变量/函数供你使用。

Check the documentation to get a list of all the available internal variables / functions.

查看文档以获取所有可用的内部变量/函数列表。

(这里的 "documentation" 通常是一个可点击的链接，指向 Templater 的官方文档。)

---

Syntax highlighting on desktop

桌面端语法高亮

Adds syntax highlighting for Templater commands in edit mode.

在编辑模式下为 Templater 命令添加语法高亮。

(右侧有一个开关按钮，目前是启用状态，显示为紫色。)

---

Syntax highlighting on mobile

移动端语法高亮

Adds syntax highlighting for Templater commands in edit mode on mobile. Use with caution: this may break live preview on mobile platforms.

在移动端编辑模式下为 Templater 命令添加语法高亮。请谨慎使用：这可能会导致移动平台上的实时预览功能出现问题。

(右侧有一个开关按钮，目前是禁用状态。)

---

Automatic jump to cursor

自动跳转到光标

Automatically triggers tp.file.cursor after inserting a template. You can also set a hotkey to manually trigger tp.file.cursor.

在插入模板后自动触发 tp.file.cursor。你也可以设置热键手动触发 tp.file.cursor。

(右侧有一个开关按钮，目前是禁用状态。)

---

Trigger Templater on new file creation

在新文件创建时触发 Templater

Templater will listen for the new file creation event, and, if it matches a rule you've set, replace every command it finds in the new file's content. This makes Templater compatible with other plugins like the Daily note core plugin, Calendar plugin, Review plugin, Note refactor plugin, etc.

Templater 将监听新文件创建事件，如果它匹配你设置的规则，它将替换在新文件内容中找到的每一个命令。这使得 Templater 能够兼容其他插件，例如每日笔记核心插件、日历插件、回顾插件、笔记重构插件等。

Warning: This can be dangerous if you create new files with unknown / unsafe content on creation. Make sure that every new file's content is安全 on creation.

警告：如果你在创建时使用未知/不安全的内容创建新文件，这可能会很危险。请确保创建的每个新文件的内容都是安全的。

(右侧有一个开关按钮，目前是禁用状态。)

---

Template hotkeys

模板快捷键

Template hotkeys allows you to bind a template to a hotkey.

模板快捷键允许你将模板绑定到快捷键。

(下方有一个搜索框，显示 Example: folder1/template_file。)

(右侧有添加、删除、上移、下移快捷键的按钮。)

(下方有一个紫色的按钮，显示 Add new hotkey for template，添加新的模板快捷键。)

---

Startup templates

启动模板

Startup templates are templates that will get executed once when Obsidian starts.

启动模板是当 Obsidian 启动时将执行一次的模板。

These templates won't output anything.

这些模板不会输出任何内容。

This can be useful to set up templates adding hooks to Obsidian events for example.

这对于设置添加 Obsidian 事件钩子的模板很有用，例如。

(下方有一个搜索框，显示 Example: folder1/template_file。)

(右侧有一个删除模板的按钮。)

(下方有一个紫色的按钮，显示 Add new startup template，添加新的启动模板。)

---
