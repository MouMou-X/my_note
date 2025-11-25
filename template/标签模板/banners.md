<%*
// 1. 调用函数获取完整的 Markdown 图片链接
const markdownImage = await tp.web.random_picture("1280x1920", "Nature,Travel");

// 2. 使用正则表达式从链接中提取 URL
//    这个表达式会匹配形如 ![...](url.md) 的结构，并捕获其中的 URL 部分
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