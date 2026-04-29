# harness是什么？
**每次agent犯错时，你不能只是告诉它下次做得更好。你要改变系统，使这种特定的错误在结构上更难重复发生。**——Mitchell Hashimoto
# harness和prompt 、context有什么区别？
```dataviewjs
const style = document.createElement('style');
style.textContent = `
.eng-wrap { font-family: var(--font-interface); padding: 0.5rem 0 1rem; }
.eng-header { display: flex; align-items: center; gap: 12px; margin-bottom: 4px; }
.eng-accent { display: inline-block; width: 4px; height: 36px; background: #D85A30; border-radius: 2px; flex-shrink: 0; }
.eng-title { font-size: 17px; font-weight: 600; color: var(--text-normal); line-height: 1.3; }
.eng-subtitle { font-size: 12px; color: var(--text-muted); margin: 4px 0 1.2rem 16px; }
.eng-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin-bottom: 1.2rem; }
.eng-card { border-radius: 10px; padding: 1.2rem 1rem; display: flex; flex-direction: column; gap: 12px; }
.card-title-main { font-size: 14px; font-weight: 600; text-align: center; }
.card-title-sub { font-size: 10px; font-weight: 400; text-align: center; margin-top: 2px; padding-bottom: 9px; border-bottom: 0.5px solid; opacity: 0.75; }
.card-row { font-size: 12px; text-align: center; line-height: 1.5; }
.scope-badge { display: inline-block; font-size: 11px; font-weight: 500; padding: 3px 12px; border-radius: 20px; background: #F1EFE8; color: #444441; border: 1px solid #D3D1C7; }
.limit-box { font-size: 11px; border-radius: 6px; padding: 7px 10px; text-align: center; line-height: 1.5; display: flex; align-items: center; justify-content: center; gap: 5px; background: #F5C4B3; color: #712B13; }
.blue-card { background: #E6F1FB; border: 0.5px solid #B5D4F4; }
.blue-card .card-title-main { color: #0C447C; }
.blue-card .card-title-sub { color: #378ADD; border-color: #B5D4F4; }
.blue-card .card-row { color: #185FA5; }
.green-card { background: #EAF3DE; border: 0.5px solid #C0DD97; }
.green-card .card-title-main { color: #27500A; }
.green-card .card-title-sub { color: #639922; border-color: #C0DD97; }
.green-card .card-row { color: #3B6D11; }
.amber-card { background: #FAEEDA; border: 0.5px solid #FAC775; }
.amber-card .card-title-main { color: #412402; }
.amber-card .card-title-sub { color: #BA7517; border-color: #FAC775; }
.amber-card .card-row { color: #633806; }
.eng-footer { background: var(--background-secondary); border-radius: 10px; padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; border: 0.5px solid var(--background-modifier-border); gap: 12px; }
.eng-footer-text { font-size: 12px; color: var(--text-muted); }
.nest-wrap { display: flex; align-items: center; flex-shrink: 0; }
.nest-box { display: flex; align-items: center; font-size: 10px; font-weight: 600; padding: 5px 8px; border-radius: 5px; border: 1.5px solid; white-space: nowrap; }
.n-harness { background: #FAEEDA; border-color: #EF9F27; color: #633806; }
.n-context { background: #EAF3DE; border-color: #97C459; color: #3B6D11; margin-left: 4px; }
.n-prompt  { background: #E6F1FB; border-color: #85B7EB; color: #185FA5; margin-left: 4px; }
`;
dv.container.appendChild(style);

dv.container.innerHTML += `
<div class="eng-wrap">
  <div class="eng-header">
    <span class="eng-accent"></span>
    <span class="eng-title">提示词工程 vs 上下文工程 vs Harness Engineering</span>
  </div>
  <p class="eng-subtitle">三种方法，解决三类不同问题</p>

  <div class="eng-grid">

    <div class="eng-card blue-card">
      <div>
        <div class="card-title-main">提示词工程</div>
        <div class="card-title-sub">Prompt Engineering</div>
      </div>
      <div class="card-row">设计你对模型说什么</div>
      <div class="card-row">如何获得更好的回答？</div>
      <div style="text-align:center"><span class="scope-badge">单次交互</span></div>
      <div class="limit-box">
        无法阻止智能体执行错误操作
      </div>
    </div>

    <div class="eng-card green-card">
      <div>
        <div class="card-title-main">上下文工程</div>
        <div class="card-title-sub">Context Engineering</div>
      </div>
      <div class="card-row">设计模型所获取的信息</div>
      <div class="card-row">智能体当前需要哪些信息？</div>
      <div style="text-align:center"><span class="scope-badge">单次会话</span></div>
      <div class="limit-box">无法执行边界约束或捕获失败</div>
    </div>

    <div class="eng-card amber-card">
      <div>
        <div class="card-title-main">Harness Engineering</div>
        <div class="card-title-sub" style="border-color:#FAC775;">&nbsp;</div>
      </div>
      <div class="card-row">构建模型运行所处的系统</div>
      <div class="card-row">如何阻止智能体做出错误决策？</div>
      <div style="text-align:center"><span class="scope-badge">整个系统</span></div>
      <div class="limit-box">无法脱离提示词与上下文而独立存在</div>
    </div>

  </div>

  <div class="eng-footer">
    <span class="eng-footer-text">Harness 包含 Context Engineering，Context Engineering 包含 Prompt Engineering</span>
    <div class="nest-wrap">
      <div class="nest-box n-harness">
        Harness
        <div class="nest-box n-context">
          Context
          <div class="nest-box n-prompt">Prompt</div>
        </div>
      </div>
    </div>
  </div>
</div>
`;
```

# harness的组件
```dataviewjs
const svg = `<svg width="100%" viewBox="0 0 680 510" xmlns="http://www.w3.org/2000/svg" style="font-family: var(--font-interface);">
<defs>
  <marker id="he-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="var(--text-muted)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- 标题 -->
<rect x="40" y="12" width="4" height="32" rx="2" fill="#D85A30"/>
<text x="52" y="26" font-size="17" font-weight="600" fill="var(--text-normal)">Harness Engineering 组件</text>
<text x="52" y="42" font-size="11" font-weight="400" fill="var(--text-muted)">Harness Engineering Components</text>

<!-- AI 模型（中心，珊瑚色） -->
<rect x="255" y="215" width="150" height="88" rx="12" fill="#F5C4B3" stroke="#F0997B" stroke-width="0.5"/>
<text x="330" y="259" font-size="14" font-weight="600" fill="#712B13" text-anchor="middle" dominant-baseline="central">AI 模型</text>

<!-- 知识库（顶部，琥珀色）-->
<rect x="175" y="63" width="310" height="78" rx="10" fill="#FAEEDA" stroke="#FAC775" stroke-width="0.5"/>
<text x="330" y="89" font-size="14" font-weight="600" fill="#412402" text-anchor="middle" dominant-baseline="central">知识库 · Knowledge Base</text>
<text x="330" y="109" font-size="12" font-weight="400" fill="#854F0B" text-anchor="middle" dominant-baseline="central">领域文档、约束条件、示例数据</text>

<!-- 反馈循环（左上，蓝色） -->
<rect x="8" y="153" width="232" height="80" rx="10" fill="#E6F1FB" stroke="#B5D4F4" stroke-width="0.5"/>
<text x="124" y="179" font-size="14" font-weight="600" fill="#042C53" text-anchor="middle" dominant-baseline="central">反馈循环 · Feedback Loops</text>
<text x="124" y="199" font-size="12" font-weight="400" fill="#185FA5" text-anchor="middle" dominant-baseline="central">将结果回传以</text>
<text x="124" y="215" font-size="12" font-weight="400" fill="#185FA5" text-anchor="middle" dominant-baseline="central">持续优化智能体</text>

<!-- 架构约束（右上，蓝色） -->
<rect x="420" y="153" width="252" height="78" rx="10" fill="#E6F1FB" stroke="#B5D4F4" stroke-width="0.5"/>
<text x="546" y="179" font-size="14" font-weight="600" fill="#042C53" text-anchor="middle" dominant-baseline="central">架构约束 · Arch. Constraints</text>
<text x="546" y="201" font-size="12" font-weight="400" fill="#185FA5" text-anchor="middle" dominant-baseline="central">智能体必须遵守的规则</text>

<!-- 状态管理（左下，琥珀色） -->
<rect x="8" y="291" width="232" height="68" rx="10" fill="#FAEEDA" stroke="#FAC775" stroke-width="0.5"/>
<text x="124" y="315" font-size="14" font-weight="600" fill="#412402" text-anchor="middle" dominant-baseline="central">状态管理 · State Management</text>
<text x="124" y="335" font-size="12" font-weight="400" fill="#854F0B" text-anchor="middle" dominant-baseline="central">跨步骤的上下文保持</text>

<!-- 工具集（右下，灰色） -->
<rect x="440" y="291" width="232" height="68" rx="10" fill="#F1EFE8" stroke="#D3D1C7" stroke-width="0.5"/>
<text x="556" y="315" font-size="14" font-weight="600" fill="#2C2C2A" text-anchor="middle" dominant-baseline="central">工具集 · Tools</text>
<text x="556" y="335" font-size="12" font-weight="400" fill="#5F5E5A" text-anchor="middle" dominant-baseline="central">智能体可执行的动作</text>

<!-- 验证关卡（底部，绿色） -->
<rect x="175" y="382" width="310" height="68" rx="10" fill="#EAF3DE" stroke="#C0DD97" stroke-width="0.5"/>
<text x="330" y="406" font-size="14" font-weight="600" fill="#173404" text-anchor="middle" dominant-baseline="central">验证关卡 · Verification Gates</text>
<text x="330" y="426" font-size="12" font-weight="400" fill="#3B6D11" text-anchor="middle" dominant-baseline="central">输出结果的检查与校验</text>

<!-- 双向箭头 -->
<!-- 知识库 ↔ AI -->
<line x1="330" y1="141" x2="330" y2="215" stroke="var(--text-muted)" stroke-width="1.5" fill="none" marker-start="url(#he-arrow)" marker-end="url(#he-arrow)"/>
<!-- 反馈循环 ↔ AI -->
<line x1="240" y1="191" x2="255" y2="237" stroke="var(--text-muted)" stroke-width="1.5" fill="none" marker-start="url(#he-arrow)" marker-end="url(#he-arrow)"/>
<!-- 架构约束 ↔ AI -->
<line x1="420" y1="191" x2="405" y2="237" stroke="var(--text-muted)" stroke-width="1.5" fill="none" marker-start="url(#he-arrow)" marker-end="url(#he-arrow)"/>
<!-- 状态管理 ↔ AI -->
<line x1="240" y1="325" x2="255" y2="281" stroke="var(--text-muted)" stroke-width="1.5" fill="none" marker-start="url(#he-arrow)" marker-end="url(#he-arrow)"/>
<!-- 工具集 ↔ AI -->
<line x1="440" y1="325" x2="405" y2="281" stroke="var(--text-muted)" stroke-width="1.5" fill="none" marker-start="url(#he-arrow)" marker-end="url(#he-arrow)"/>
<!-- 验证关卡 ↔ AI -->
<line x1="330" y1="382" x2="330" y2="303" stroke="var(--text-muted)" stroke-width="1.5" fill="none" marker-start="url(#he-arrow)" marker-end="url(#he-arrow)"/>
</svg>`;

dv.container.innerHTML = svg;
```

**知识库（Knowledge Base）** 存储在代码仓库中的文档、架构决策和项目背景信息，agent 在开始任何任务前都会读取这些内容。凡是不在仓库中的信息，agent 就看不到。

**架构约束（Architectural Constraints）** 由 linter 和结构性测试强制执行的规则，从物理层面阻止 agent 接触不该碰的代码或系统。这些不是建议，agent 无法绕过它们。

**工具与集成（Tools and Integrations）** 赋予 agent 执行真实操作能力的 CLI 工具、API 和 MCP 服务。没有合适工具的 agent，只能生成关于任务的文字描述，而无法真正完成任务。

**验证关卡（Verification Gates）** agent 必须通过的测试和检查，只有全部通过才能将任务标记为完成。没有这些关卡，"完成"的含义就由 agent 自己说了算。

**状态管理（State Management）** 跨上下文窗口持久化的进度文件和会话日志，确保 agent 在开启新会话时不会失去对上一次会话的记忆。

**反馈循环（Feedback Loops）** 循环检测与自我纠正机制，当 agent 陷入重复执行某个失败方案时，将其识别并引导回正确路径。

---

以上这些都不是 prompt，也不是 context。它们是结构性的存在——无论 agent 是否"愿意"，它始终在这些约束内部运作。

# harness 如何运行
在harness engineering中，组件被归为3个运行层。
### 1. 上下文工程
- 确保在恰当的时机提供恰当的信息。
	- （在储存库内部维护一个结构化的知识库，编写进度文件和会话交接文档，以便agent能够在不同的上下文窗口之间恢复工作，并根据当前任务动态加载相关文档。）
- Anthropic使用json而非markdown，以及一个`init.sh`脚本

> [!NOTE]- [A社文章：构建长效运行智能体框架的工程文档](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
> **存在的问题：**
> - agent倾向于一次执行过多操作。导致上下文丢失。某个功能实现了一半，新的agent只能靠猜。
> - 在项目后期，在某些功能已经构建完成后，后续的代理实例会检查项目进展，发现已经取得了一些进展，然后宣布任务完成。
> 
> **解决方案：**
> - 搭建一个初始环境、为功能奠定基础。使代理能够逐步、逐个功能地完成任务。
> - 其次，我们应该引导每个代理逐步实现其目标，同时在会话结束时将环境清理干净。所谓“清理干净”的状态，是指代码适合合并到主分支：没有重大错误，代码结构清晰、文档齐全，通常情况下，开发人员可以轻松地开始开发新功能，而无需先清理无关的混乱代码。
> 1. 初始化代理：第一个代理会话使用一个特殊的提示，要求模型设置初始环境：一个`init.sh`脚本、一个记录代理所做工作的 claude-progress.txt 文件，以及一个显示已添加文件的初始 git 提交。
> 2. 编码代理：后续每个会话都要求模型取得增量进展，然后留下结构化的更新信息
> 关键在于找到一种方法，让代理在打开一个全新的上下文窗口时能够快速了解​​工作状态，这可以通过 claude-progress.txt 文件以及 Git 历史记录来实现。这些实践的灵感来源于了解高效软件工程师的日常工作。

> [!NOTE]- [什么是上下文工程？](https://datasciencedojo.com/blog/what-is-context-engineering/)
> 上下文工程（Context Engineering）是指在 AI 模型推理过程中，对其周围的所有信息（包括静态和动态信息）进行系统性的设计、构建和管理。提示词工程（Prompt Engineering）优化的是你对模型**说**什么，而上下文工程决定的是模型在生成响应时**知道**什么。
> 
> 在实际应用中，上下文工程包括以下几个方面：
> 
> - **组装**系统指令、用户偏好和对话历史记录。
>     
> - **动态检索并整合**外部文档或数据。
>     
> - **管理**工具模式（Schemas）和 API 输出结果。
>     
> - **结构化和压缩信息**，使其能够适应模型的上下文窗口限制。
>     
> 简而言之，上下文工程将模型交互的范围进行了扩展，将模型进行准确推理和自主运行所需的一切信息都包含在内。
> 
> ![上下文工程——它包含的内容](https://datasciencedojo.com/wp-content/uploads/2025/07/context.webp)

### 2. 架构约束
上下文层描述的是智能体知道什么，约束层描述的是智能体被允许做什么。
- 强制执行严格的分层架构
