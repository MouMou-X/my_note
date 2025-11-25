> [!tip] 注意
> - banners已经一年未更新维护
> - 建议使用pixel banner
# question
我现在在调用obsidian中templaer插件的<% tp.web.random_picture("1280x1920","Nature,Travel") %>已经成功加载了图片。

这个templater语法的返回值是
```markdown
![photo by Michelle Spollen(https://unsplash.com/@micki?utm_source=templater_proxy&utm_medium=referral) on Unsplash](https://images.unsplash.com/photo-1541599468348-e96984315921?crop=entropy&cs=srgb&fm=jpg&ixid=M3w2NDU1OTF8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDk1Njk5OTN8&ixlib=rb-4.1.0&q=85&w=1280&h=1920)
```
我想与banners插件联用。但banners插件默认只识别http网址，不能有多余内容。形如：

---

banner: "https://images.unsplash.com/photo-1541599468348-e96984315921?crop=entropy&cs=srgb&fm=jpg&ixid=M3w2NDU1OTF8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDk1Njk5OTN8&ixlib=rb-4.1.0&q=85&w=1280&h=1920"

---

应该如何解决？

# answer
你好！你遇到了一个非常经典且常见的问题，这也是 Templater 强大之处的绝佳体现：**对返回结果进行再处理**。

你说得完全正确，`tp.web.random_picture` 为了方便直接插入笔记中，返回的是一个完整的 Markdown 图片格式 `![描述](链接)`，而 Banners 插件在 frontmatter (笔记最顶部的 `---` 区域) 中只需要纯净的 URL 链接。

要解决这个问题，我们需要用 Templater 的**执行命令** (`<%* ... %>`) 来写一小段 JavaScript 代码，从返回的 Markdown 文本中把 URL “提取”出来。

这里给你提供两个解决方案，根据你的具体需求选用。

---

### 方案一：只生成 Banner Frontmatter

如果你只希望模板在笔记顶部生成 `banner` 属性，不希望在正文里再显示图片，用这个方案。

**原理：**

1. 调用 `tp.web.random_picture` 并将其返回值存入一个变量。
2. 使用正则表达式 (Regular Expression) 从这个变量中匹配并提取出括号 `()` 里的 URL 部分。
3. 将提取出的 URL 格式化为 Banners 插件需要的 frontmatter 格式并输出。

**模板代码：**

JavaScript

```
<%*
// 1. 调用函数获取完整的 Markdown 图片链接
const markdownImage = await tp.web.random_picture("1280x1920", "Nature,Travel");

// 2. 使用正则表达式从链接中提取 URL
//    这个表达式会匹配形如 ![...](URL) 的结构，并捕获其中的 URL 部分
const urlRegex = /!\[.*\]\((.*)\)/;
const match = markdownImage.match(urlRegex);

// 3. 检查是否成功匹配
if (match && match[1]) {
    const imageUrl = match[1]; // 提取到的纯净 URL
    
    // 4. 构建并输出 Banners 插件需要的 frontmatter
    tR += `---
banner: "${imageUrl}"
---`;

} else {
    // 如果因意外情况没能提取出 URL，则输出错误提示
    tR += `---
banner: "Error: Could not extract image URL."
---`;
}
%>
```

**如何使用：**

1. 在你的 Templater 模板文件夹中创建一个新的 `.md` 文件（例如 `banner-template.md`）。
2. 将上面的代码完整地复制粘贴到这个文件中。
3. 在一个新的或已有的笔记中，通过命令面板 (`Ctrl/Cmd + P`) 运行 "Templater: Open Insert Template modal"，然后选择你刚刚创建的 `banner-template`。
4. Templater 就会自动运行代码，获取图片，提取 URL，并插入格式正确的 frontmatter。

---

### 方案二：生成 Banner 并同时在正文插入图片

这个方案更常用：既要在笔记顶部设置好 banner，又希望在笔记正文的某个地方把这张随机图片显示出来。

原理：

与方案一基本相同，只是在最后，我们不仅输出了 frontmatter，还把原始的 Markdown 图片链接也输出了。

**模板代码：**

JavaScript

```
<%*
// 1. 调用函数并存储结果，这样我们只需要请求一次网络
const markdownImage = await tp.web.random_picture("1280x1920", "Nature,Travel");

// 2. 提取 URL
const urlRegex = /!\[.*\]\((.*)\)/;
const match = markdownImage.match(urlRegex);

if (match && match[1]) {
    const imageUrl = match[1];
    
    // 3. 构建 frontmatter
    const frontmatter = `---
banner: "${imageUrl}"
---`;

    // 4. 将 frontmatter 和原始的图片链接一起输出
    //    首先输出 frontmatter
    tR += frontmatter;
    //    然后输出两个换行符（เพื่อสร้างช่องว่าง）和一个原始的图片链接
    tR += "\n\n" + markdownImage;

} else {
    tR += "Error: Failed to fetch and process image.";
}
%>
```

如何使用：

这个模板最适合用于创建新笔记。你可以将这个模板设置到 Templater 插件的 "Folder Templates" 中，这样你在特定文件夹下创建新笔记时，它会自动运行，一篇带有随机 Banner 和正文图片的笔记就瞬间诞生了！

### 总结

核心技巧就是利用 `const a = await some_function()` 把结果存起来，然后用 JavaScript（在这里是正则表达式 `match` 函数）对变量 `a` 进行处理，最后用 `tR +=` 把你想要的最终结果输出到笔记里。

希望这能完美解决你的问题！