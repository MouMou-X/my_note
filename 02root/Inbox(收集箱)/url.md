---
url: https://help.obsidian.md/Extending+Obsidian/Obsidian+URI
url编码: https://en.wikipedia.org/wiki/Percent-encoding
---

## Obsidian URL 操作详解：释放你的自动化潜能

Obsidian 作为一款功能强大的双向链接笔记软件，其 URL 操作方案（URL Scheme）为用户提供了超越应用本身的无限可能。通过精确构造的 URL，你可以从任何支持超链接的地方（例如其他应用程序、脚本、甚至是你自己的笔记中）直接控制 Obsidian 的各种行为，极大地提升工作效率和自动化水平。

本文将详细列举并解释 Obsidian 的 URL 用法，从基础操作到高级技巧，助你全面掌握这一强大功能。

### 一、URL 结构基础

Obsidian 的 URL 方案以 `obsidian://` 开头，其后跟随具体的操作指令和参数。一个典型的 Obsidian URL 结构如下：

```
obsidian://<action>?<parameter1>=<value1>&<parameter2>=<value2>
```

- **`obsidian://`**: 这是 Obsidian URL 的协议头，用于向操作系统声明这是一个指向 Obsidian 的链接。
- **`<action>`**: 指定要执行的操作，例如 `open` (打开)、`new` (新建)、`search` (搜索) 等。
- **`?`**: 用于分隔操作和参数。
- **`<parameter>=<value>`**: 参数及其对应的值，用于为操作提供更具体的信息。多个参数之间使用 `&` 分隔。

**重要提示：** URL 中的所有参数值都必须经过 **URL编码**，特别是当值中包含空格、斜杠 (`/`)、`#` 等特殊字符时。例如，空格会被编码为 `%20`。

### 二、核心 URL 操作

以下是 Obsidian 内置支持的核心 URL 操作：

#### 1. 打开 (`open`)

此操作用于打开指定的库、文件、标题或块。

**参数：**

- `vault`: 要打开的库的名称或ID。如果省略，则在当前或上一个活动的库中执行操作。
- `file`: 要打开的文件名或文件的绝对路径。
- `path`: 文件的全局绝对路径。这会覆盖 `vault` 和 `file` 参数。
- `heading`: 要跳转到的文件内标题的名称。
- `block`: 要跳转到的文件内块的ID。
- `line`: 要跳转到的行号。

**示例：**

- **打开指定的库：**
    
    ```
    obsidian://open?vault=我的知识库
    ```
    
- **打开特定文件：**
    
    ```
    obsidian://open?vault=我的知识库&file=项目/2025年计划
    ```
    
    (注意：如果文件名中包含 `/`，则表示文件位于子文件夹中。)
    
- **打开文件并跳转到指定标题：**
    
    ```
    obsidian://open?vault=我的知识库&file=会议记录&heading=周一例会
    ```
    
- **通过文件路径直接打开笔记（无需指定库名）：**
    
    ```
    obsidian://open?path=/Users/用户名/Documents/我的知识库/日常记录.md
    ```
    

#### 2. 新建 (`new`)

此操作用于创建新笔记，或向现有笔记追加内容。

**参数：**

- `vault`: 要在其中创建笔记的库的名称。
- `name`: 新笔记的文件名。
- `file`: 新笔记的完整路径（包括文件名）。如果同时指定了 `name`，`file` 的优先级更高。
- `path`: 新笔记的全局绝对路径。
- `content`: 新笔记的内容。
- `clipboard`: 使用剪贴板中的内容作为新笔记的内容。
- `append`: 如果文件已存在，则将 `content` 或剪贴板内容追加到文件末尾，而不是覆盖。
- `overwrite`: 如果文件已存在，则用新内容覆盖旧内容（`append` 模式下无效）。
- `silent`: 静默创建，即创建后不自动打开该笔记。

**示例：**

- **在指定库中创建一篇新笔记：**
    
    ```
    obsidian://new?vault=我的知识库&name=新的想法
    ```
    
- **创建带有预设内容的新笔记：**
    
    ```
    obsidian://new?vault=我的知识库&name=会议纪要&content=%23%20会议标题%0A%0A-%20议题一
    ```
    
    (注意：`%23` 是 `#` 的编码，`%0A` 是换行符的编码。)
    
- **将剪贴板内容追加到现有笔记：**
    
    ```
    obsidian://new?vault=我的知识库&file=灵感收集&clipboard=true&append=true
    ```
    

#### 3. 搜索 (`search`)

此操作用于在 Obsidian 中执行搜索。

**参数：**

- `vault`: 要在其中搜索的库的名称。
- `query`: 搜索查询的内容。支持 Obsidian 的所有高级搜索语法。

**示例：**

- **在当前库中搜索特定关键词：**
    
    ```
    obsidian://search?query=URL
    ```
    
- **在指定库中搜索包含特定标签的文件：**
    - 使用query时，需要url编码
    > [!example] 使用url搜索`#第二大脑`
    > ```
    > obsidian://search?vault=test&query=%23%E7%AC%AC%E4%BA%8C%E5%A4%A7%E8%84%91
    > ```
    

#### 4. 打开每日笔记 (`daily`)

此操作用于打开或创建当天的每日笔记。

**参数：**

- `vault`: 每日笔记所在的库的名称。
- 所有 `new` 操作的参数（如 `content`, `append` 等）都可以在此处使用，以便在创建每日笔记时添加内容。

**示例：**

- **打开或创建今天的每日笔记：**
    
    ```
    obsidian://daily?vault=我的知识库
    ```
    
- **创建每日笔记并追加一条待办事项：**
    
    ```
    obsidian://daily?vault=我的知识库&content=%0A-%20[ ]%20完成URL操作的文档整理&append=true
    ```
    

### 三、高级用法与 x-callback-url

Obsidian 的 URL 方案还支持 `x-callback-url`，这使得 Obsidian 可以与其他支持该协议的应用程序进行更深度的交互。通过在 URL 中添加 `x-success` 和 `x-error` 参数，可以在 Obsidian 完成操作后，将结果返回给调用它的应用程序。

**参数：**

- `x-success`: 操作成功后要调用的 URL。
- `x-error`: 操作失败后要调用的 URL。

这在自动化工作流（例如使用 iOS 上的“快捷指令”或 macOS 上的 Alfred）中非常有用。

### 四、插件增强：Advanced Obsidian URI

为了进一步扩展 URL 操作的能力，社区开发了名为 **“Advanced Obsidian URI”** 的强大插件。安装并启用该插件后，你可以使用 `obsidian://advanced-uri?` 协议头来执行更多高级操作。

**Advanced URI 插件提供的部分增强功能：**

- **编辑文件 (`edit`)**: 可以对现有文件进行更复杂的操作，例如插入、替换文本。
- **打开工作区 (`workspace`)**: 直接通过 URL 切换到预设的 Obsidian 工作区布局。
- **执行命令 (`command`)**: 触发 Obsidian 的任何命令，包括其他插件提供的命令。
- **更灵活的文件和标题定位**: 提供了更多样的方式来定位文件和标题。

**示例（需安装 Advanced URI 插件）：**

- **打开文件并替换其中的文本：**
    
    ```
    obsidian://advanced-uri?vault=我的知识库&filepath=项目/2025年计划&data=将“初步计划”替换为“最终计划”&mode=overwrite
    ```
    
- **执行“模板：插入模板”命令：**
    
    ```
    obsidian://advanced-uri?vault=我的知识库&commandid=templater:insert-templater
    ```
    

### 五、实际应用场景

- **任务管理集成**: 在你的待办事项应用（如 Things、Todoist）中，为每个任务添加一个指向 Obsidian 相关笔记的 URL，方便随时查阅项目详情。
- **日历联动**: 在日历事件的备注中，放入指向该次会议记录的 Obsidian URL。
- **快速剪藏**: 使用脚本或快捷指令，一键将网页内容、剪贴板文本保存到 Obsidian 的指定笔记中。
- **自动化报告生成**: 编写脚本，定期从其他数据源获取信息，并通过 URL 方案自动在 Obsidian 中创建格式化的周报或月报。
- **跨设备无缝衔接**: 在不同设备上使用相同的 URL 方案，可以确保无论在哪里都能准确地打开你需要的笔记。

通过熟练运用 Obsidian 的 URL 操作，你可以打破应用的边界，将 Obsidian 更紧密地融入到你的数字化工作流中，实现真正高效和个性化的知识管理。


