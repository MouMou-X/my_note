---
tags:
  - CSS
  - Obsidian
  - Snippets
  - SVG
  - Callout
  - Animation
creation_date: 2025-07-02
---

# 

## 1. 目标

我希望能在自定义的 Callout（例如 `[!column]`）中，将默认的 Lucide 图标替换为我自己的 SVG 图标，并且最终能让这个 SVG 图标带有 CSS 动画效果。

## 2. 失败的尝试与原因分析（踩坑记录）

在实现最终效果之前，我遇到了几个典型的失败案例。理解这些失败的原因是掌握正确方法的关键。

### 失败案例一：直接将 SVG 代码作为字符串赋值

我最初尝试将 SVG 的 HTML 代码直接作为字符串赋值给 CSS 变量。

```css
/* ❌ 错误的方法 */
.callout[data-callout="column"] {
   --callout-icon: '<svg width="19.9" ...>...</svg>';
}
```

- **失败原因**: CSS 的 `content` 属性无法将一段 HTML/SVG 文本字符串解析并渲染成一个图像。它只会把这串代码当作普通的文字来对待，因此什么也显示不出来。

### 失败案例二：外部 CSS 无法控制 Data URI 内部的动画

在将 SVG 成功转换为 Data URI 并显示出来后，我尝试用外部的 CSS 代码片段来控制 SVG 内部元素的动画。

```css
/* ❌ 错误的方法 */

/* 我以为这样能让图标动起来 */
.rotating-rect {
  animation: rotate 5s linear infinite;
}

@keyframes rotate { ... }
```

- **失败原因**: 当一个 SVG 作为 Data URI 被用在 `background-image` 中时，它对于外部的 CSS 来说就是一个“黑盒子”。外部的样式无法穿透进去，去控制 SVG 内部某个特定 class（如 `.rotating-rect`）的样式。这就像你无法用 CSS 去改变一张 PNG 图片里某个特定区域的颜色一样。

## 3. 正确的解决方案

正确的流程分为两步：**“封装”与“应用”**。

### 步骤一：创建“自包含”的动画 SVG

我们需要将所有需要的东西——SVG 结构、样式、动画——全部封装进一个 SVG 文件里。

1.  **准备基础 SVG**:
    ```xml
    <svg width="19.9" height="19.9" viewBox="0 0 200 200" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
      <rect x="50" y="50" width="100" height="100" fill="#FF5733" class="rotating-rect"></rect>
    </svg>
    ```

2.  **将动画 CSS 嵌入 SVG**: 使用 `<style>` 标签，将动画规则直接写进 SVG 代码内部。

    ```xml
    <svg width="19.9" height="19.9" viewBox="0 0 200 200" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
      
      <style>
        .rotating-rect {
          transform-origin: 100px 100px; /* 设置旋转中心 */
          animation: rotate 5s linear infinite;
        }
        @keyframes rotate {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
      </style>
      
      <rect x="50" y="50" width="100" height="100" fill="#FF5733" class="rotating-rect"></rect>
    </svg>
    ```

### 步骤二：将“封装好的”SVG 转换为 Data URI 并应用

现在，这个 SVG 已经是一个自带动画的独立文件了。我们只需要将它应用到 Callout 中即可。

1.  **URL 编码**: 将上面那一大段包含 `<style>` 的完整 SVG 代码，通过在线工具（如 [URL-encoder for SVG](https://yoksel.github.io/url-encoder/)）进行编码。

2.  **使用最终的 CSS 代码**: 我们不依赖不稳定的 `--callout-icon` 变量，而是采用更强制、更可靠的“背景图替换法”。

    ```css
    /* 最终、可靠的解决方案 */

    /* 针对 [!column] 这个 callout */
    .callout[data-callout="column"] {
        --callout-color: 255, 255, 155; /* 设置颜色 */
    }

    /* 1. 先将默认的图标隐藏掉 */
    .callout[data-callout="column"] .callout-icon .svg-icon {
       display: none;
    }

    /* 2. 然后在图标容器上，用背景图的方式画上我们自己的动画图标 */
    .callout[data-callout="column"] .callout-icon {
       width: 19.9px;
       height: 19.9px;
       
       /* 将包含内嵌动画的 SVG Data URI 设置为背景图像 */
       background-image: url('data:image/svg+xml,%3Csvg width="19.9" height="19.9" viewBox="0 0 200 200" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)"%3E%3Cstyle%3E.rotating-rect %7B transform-origin: 100px 100px; animation: rotate 5s linear infinite; %7D @keyframes rotate %7B from %7B transform: rotate(0deg); %7D to %7B transform: rotate(360deg); %7D %7D%3C/style%3E%3Crect x="50" y="50" width="100" height="100" fill="%23FF5733" class="rotating-rect"%3E%3C/rect%3E%3C/svg%3E');
       
       background-size: contain;
       background-repeat: no-repeat;
       background-position: center;
    }
    ```

## 4. 总结

- **不要**直接用字符串形式的 SVG 代码赋值给 CSS 变量。
- **要**将 SVG 转换为 **Data URI**。
- **不要**尝试用外部 CSS 去控制 Data URI 内部的动画。
- **要**将动画的 `<style>` **直接嵌入**到 SVG 代码内部，然后再进行编码。
- 为了保证样式能稳定生效，**推荐**使用“隐藏原图标，设置背景图”的方法，而不是依赖主题可能覆盖的 `--callout-icon` 变量。

通过这次探索，我不仅成功实现了目标，还对 CSS 变量、Data URI 以及 SVG 的工作原理有了更深刻的理解。