---
tags:
  - CSS
  - Obsidian
  - Snippets
  - Layout
  - Flexbox
creation_date: 2025-07-01
---

# Obsidian 分栏布局探索之旅：从 HTML 到原生 Flexbox 响应式布局

## 1. 最初的目标

我的核心需求是：在 Obsidian 笔记中实现内容分栏，同时希望尽可能使用原生的 Markdown 语法，避免在笔记中充斥大量复杂的 HTML 代码。

## 2. 方案探索与迭代

### 方案一：HTML `div` 块 (已废弃)

最初尝试了使用 HTML 的 `<div>` 标签来创建容器和栏目，并为其添加 CSS 样式。

- **问题**:
    1.  笔记源码中充满了 `<div>`，显得非常杂乱。
    2.  `<div>` 内部的 Markdown 语法默认不被解析，必须手动为每个 `<div>` 添加 `markdown="1"` 属性，非常繁琐。

### 方案二：CSS Grid 与 Callout 嵌套 (一次重要的尝试)

为了追求更原生的体验，我们转向使用 Obsidian 的 Callout 语法，通过嵌套 Callout 来模拟“容器”和“栏目”的结构。

> [!TIP] 核心思路
> - 使用一个父 Callout (例如 `[!columns]`) 作为布局容器。
> - 在其内部嵌套多个子 Callout (例如 `[!column]`) 作为实际的栏目。
> - 通过 CSS 将父 Callout 的视觉样式（背景、边框）隐去，并对其应用布局属性（如 `display: grid`）。

我们基于这个思路，使用 **CSS Grid** 进行了尝试。

## 3. 遇到的挑战与“破案”过程

> [!IMPORTANT] 转折点：反复失败后的诊断
> 无论是 Flexbox 还是 Grid，最初的尝试都失败了，栏目始终无法并排。这表明问题不在于用哪种布局技术，而在于我们的 CSS 选择器没有精确命中正确的 HTML 元素。

**诊断工具**：**开发者工具 (`Ctrl+Shift+I`)** 成为了解决问题的关键。

通过检查元素，我们发现了问题的根源：
Obsidian 渲染 Callout 时，会生成一个 `.callout-content` 的层级。我们想要并排的栏目（子 Callout）实际上是在这个 `.callout-content` 里面，而不是直接在父 Callout 里。

**错误的思路**：命令“大纸箱” (`.callout`) 去排列它里面的东西。
**正确的思路**：命令“纸箱里的内衬” (`.callout-content`) 去排列它里面的“商品”（子 Callout）。

## 4. 最终方案：优化的 Flexbox 响应式布局

在明确了正确的 HTML 结构后，我们最终选择使用 **Flexbox** 来构建一个健壮、响应式且可扩展的最终方案。

### 最终 CSS 代码

这份代码实现了我们所有的优化目标：基于 Flexbox、支持多种布局、且能在移动端自动适配。

```css
/* ======================================================= */
/* 最终方案：使用 Flexbox 实现响应式多布局                 */
/* ======================================================= */

/* 1. 基础容器样式 (适用于所有 "columns-flex" 开头的 callout) */
.callout[data-callout*="columns-flex"] {
    /* 清除容器自身的样式，让它隐形 */
    padding: 0;
    border: none;
    background-color: transparent;
    box-shadow: none;
}
.callout[data-callout*="columns-flex"] > .callout-title {
    display: none;
}

/* 2. 真正的 Flexbox 布局容器 (.callout-content) */
.callout[data-callout*="columns-flex"] > .callout-content {
    display: flex;
    flex-wrap: wrap; /* 允许换行，这是响应式的关键 */
    gap: 20px;
}

/* 3. 基础栏目样式 (子 Callout) */
.callout[data-callout*="columns-flex"] > .callout-content > .callout {
    margin: 0;
    flex-grow: 1;         /* 允许栏目“成长”以填满空间 */
    flex-basis: 0;        /* 基础宽度为0，让 flex-grow 完全控制宽度 */
    min-width: 250px;     /* 每个栏目的最小宽度，当空间不足时会触发换行 */
}

/* 4. [优化] 针对三栏布局的微调 */
.callout[data-callout="columns-flex-3"] > .callout-content > .callout {
    min-width: 220px; /* 三栏时，可以适当减小最小宽度 */
}
```

### 使用方法

#### 两栏布局

```markdown
> [!columns-flex]
>
> > [!column]
> > ### 第一个栏目
> >
>
> > [!column]
> > ### 第二个栏目
> >
```

#### 三栏布局
```markdown
> [!columns-flex-3]
>
> > [!column]
> > ### A栏
> >
>
> > [!column]
> > ### B栏
> >
>
> > [!column]
> > ### C栏
> >
```

> [!columns-flex]
>
> > [!column]
> > ### 第一个栏目
> > 这是基于 Flexbox 的响应式布局。
>
> > [!column]
> > ### 第二个栏目
> > 调整浏览器或Obsidian面板的宽度，观察效果。



> [!columns-flex-3]
>
> > [!column]+ 分栏1
> > #### A栏
> > A
>
> > [!column]+ 分栏2
> > #### B栏
> > B
>
> > [!column]+ 分栏3
> > #### C栏
> 
> > [!column]+ 分栏1
> > #### A栏
> > A
>
> > [!column]+ 分栏2
> > #### B栏
> > B
>
> > [!column]+ 分栏3
> > #### C栏





$$afsddvadvasvad$$