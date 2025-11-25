---
url: https://help.obsidian.md/callouts
---

# 一、Callouts支持markdown、Wiki links、和嵌入
- 添加`[!info]`到块引用的第一行
```
> [!info]
> Here's a callout block.
> It supports **Markdown**, [[Internal link|Wikilinks]], and [[Embed files|embeds]]!
> ![[Second Brain.png]]
```
> [!info]
> Here's a callout block.
> It supports **Markdown**, [[Internal link|Wikilinks]], and [[Embed files|embeds]]!
> ![[Second Brain.png]]<svg width="200" height="200" viewBox="0 0 200 200"><rect x="50" y="50" width="100" height="100" fill="#FF5733" class="rotating-rect"></rect></svg>
>   

---
# 二、更改标题
- 通过在类型标识符后添加文本来更改标题==(注意空格)==
> [!tip] 标注可以有自定义标题
> Like this one.
```
> [!tip] 标注可以有自定义标题
> Like this one.
```
- 甚至可以省略正文==(注意空格)==
> [!tip] 仅标题标注
```
> [!tip] 仅标题标注
```

---
# 三、可折叠标注
- 在类型标识符后直接添加加号 (+) 或减号 (-) 来使标注可折叠==(注意空格)==
- 默认情况下，加号会展开标注，减号则会折叠标注。
> [!faq]- Are callouts foldable?
> Yes! In a foldable callout, the contents are hidden when the callout is collapsed.
```
> [!faq]- Are callouts foldable?
> Yes! In a foldable callout, the contents are hidden when the callout is collapsed.
```

---
# 四、嵌套标注
- 可以多层嵌套标注
> [!question] Can callouts be nested?
> > [!todo] Yes!, they can.
> > > [!example]  You can even use multiple layers of nesting.
```
> [!question] Can callouts be nested?
> > [!todo] Yes!, they can.
> > > [!example]  You can even use multiple layers of nesting.
```

---

# 五、自定义标注
- [CSS 片段](https://help.obsidian.md/snippets)和[社区插件](https://help.obsidian.md/community-plugins)可以定义自定义标注，甚至可以覆盖默认配置
- 要定义自定义标注，请创建以下 CSS 块：
	- - `--callout-color`使用红色、绿色和蓝色的数字（0-255）定义背景颜色。
	- `--callout-icon`[可以是来自lucide.dev](https://lucide.dev/)的图标 ID ，也可以是 SVG 元素。
```
.callout[data-callout="custom-question-type"] {
    --callout-color: 0, 0, 0;
    --callout-icon: lucide-alert-circle;
}
```

属性的值`data-callout`是您想要使用的类型标识符，例如`[!custom-question-type]`。
- `--callout-color`使用红色、绿色和蓝色的数字（0-255）定义背景颜色。
- `--callout-icon`[可以是来自lucide.dev](https://lucide.dev/)的图标 ID ，也可以是 SVG 元素。
<svg width="200" height="200">
  <circle cx="100" cy="100" r="80" fill="blue" stroke="black" stroke-width="3" />
</svg>
<svg width="200" height="200"viewBox="0 0 58 66" fill="none" stroke="white" xmlns="http://www.w3.org/2000/svg">
  <path d="m1 49v-32l28-16 28 16v32l-28 16z"/>
  <circle cx="29" cy="33" r="20"/>
</svg>
# 支持的类型
> [!note] 笔记
> Lorem ipsum dolor sit amet
```
> [!note]
> Lorem ipsum dolor sit amet
```
---
> [!abstract] 摘要
> Lorem ipsum dolor sit amet
```
> [!abstract]
> Lorem ipsum dolor sit amet
```
- ==别名：==`summary`,`tldr`
---
> [!info] 信息
> Lorem ipsum dolor sit amet
```
> [!info]
> Lorem ipsum dolor sit amet
```
---
> [!todo] 待办事项
> Lorem ipsum dolor sit amet
```
> [!todo]
> Lorem ipsum dolor sit amet
```
---
> [!tip] 提示
> Lorem ipsum dolor sit amet
```
> [!tip]
> Lorem ipsum dolor sit amet
```
- ==别名：==`hint`,`important`
---
> [!success] 成功
> Lorem ipsum dolor sit amet
```
> [!success]
> Lorem ipsum dolor sit amet
```
- ==别名：==`check`,`done`
---
> [!question] 问题
> Lorem ipsum dolor sit amet
```
> [!question]
> Lorem ipsum dolor sit amet
```
- ==别名：==`help`,`faq`
---
> [!warning] 警告
> Lorem ipsum dolor sit amet
```
> [!warning]
> Lorem ipsum dolor sit amet
```
- ==别名：==`caution`,`attention`
---
> [!failure] 失败
> Lorem ipsum dolor sit amet
```
> [!failure]
> Lorem ipsum dolor sit amet
```
- ==别名：==`fail`,`missing`
---
> [!danger] 危险
> Lorem ipsum dolor sit amet
```
> [!danger]
> Lorem ipsum dolor sit amet
```
- ==别名：==`error`
---
> [!bug] 漏洞
> Lorem ipsum dolor sit amet
```
> [!bug]
> Lorem ipsum dolor sit amet
```
---
> [!example] 示例
> Lorem ipsum dolor sit amet
```
> [!example]
> Lorem ipsum dolor sit amet
```
---
> [!quote] 引用
> Lorem ipsum dolor sit amet
```
> [!quote]
> Lorem ipsum dolor sit amet
```
- ==别名：==`cite`
---




<svg version="1.1"
     baseProfile="full"
     width="300" height="200"
     xmlns="http://www.w3.org/2000/svg">

  <rect width="100%" height="100%" fill="white" />

  <circle cx="150" cy="100" r="80" fill="green" />

  <text x="150" y="125" font-size="60" text-anchor="middle" fill="white">SVG</text>

</svg>


<html>
<math>
  <mfrac>
    <mtext>child1</mtext>
    <mtext>child2</mtext>
  </mfrac>
</math>
<br />
<math>
  <msqrt>
    <mtext>child1</mtext>
    <mtext>child2</mtext>
    <mtext>...</mtext>
    <mtext>childN</mtext>
  </msqrt>
</math>
<br />
<math>
  <mroot>
    <mtext>child1</mtext>
    <mtext>child2</mtext>
  </mroot>
</math>
</html>

<img src="Second Brain.png" alt="Image description" style="float: left; margin-right: 15px; margin-bottom: 5px; width: 200px;">
这里的文字将会环绕在图片的右边。请确保有足够的文字内容才能明显地看到环绕效果。这段文字应该足够长，以便演示图片浮动时文本如何围绕它流动。












