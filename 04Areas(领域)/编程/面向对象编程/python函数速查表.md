
```dataviewjs
const c = dv.container;

// ── CSS ─────────────────────────────────────────────────────
const css = '<style id="pyfn-style">'
+ '.pyfn *{box-sizing:border-box;margin:0;padding:0;}'
+ '.pyfn{font-family:var(--font-interface);padding:4px 0 20px;}'
+ '.pyfn-tabs{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:16px;}'
+ '.pyfn-tab{font-size:11.5px;padding:4px 13px;border-radius:999px;border:1px solid var(--background-modifier-border);background:transparent;color:var(--text-muted);cursor:pointer;transition:all .15s;white-space:nowrap;}'
+ '.pyfn-tab:hover{background:var(--background-secondary);color:var(--text-normal);}'
+ '.pyfn-tab.active{background:var(--interactive-accent);border-color:var(--interactive-accent);color:#fff;font-weight:600;}'
+ '.pyfn-panel{display:none;}'
+ '.pyfn-panel.active{display:block;}'
+ '.pyfn-card{background:var(--background-primary);border:1px solid var(--background-modifier-border);border-radius:8px;padding:12px 16px;margin-bottom:10px;}'
+ '.pyfn-card-title{font-size:10.5px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted);margin-bottom:9px;}'
+ '.pyfn-card-sub{font-size:11px;color:var(--text-faint);font-style:italic;margin-bottom:8px;}'
+ '.pyfn-grid2{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:10px;}'
+ '.pyfn-pre{font-family:var(--font-monospace);font-size:12px;line-height:1.75;color:var(--text-normal);white-space:pre;overflow-x:auto;}'
+ '.pk{color:var(--color-red);font-weight:500;}'
+ '.pf{color:var(--color-green);}'
+ '.ps{color:var(--color-cyan,var(--color-blue));}'
+ '.pc{color:var(--text-faint);font-style:italic;}'
+ '.pn{color:var(--color-orange);}'
+ '.pyfn-tbl{width:100%;font-size:12px;border-collapse:collapse;}'
+ '.pyfn-tbl th{font-size:10px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--text-faint);padding:5px 8px;border-bottom:1px solid var(--background-modifier-border);text-align:left;}'
+ '.pyfn-tbl td{padding:6px 8px;border-bottom:1px solid var(--background-modifier-border);vertical-align:top;}'
+ '.pyfn-tbl td:first-child{font-family:var(--font-monospace);font-size:11px;color:var(--color-purple);white-space:nowrap;width:38%;}'
+ '.pyfn-tbl tr:last-child td{border-bottom:none;}'
+ '.pyfn-note{font-size:12px;font-family:var(--font-monospace);border-left:3px solid var(--interactive-accent);background:var(--background-secondary);padding:8px 12px;border-radius:0 6px 6px 0;color:var(--text-muted);margin-bottom:10px;}'
+ '.pyfn-note.warn{border-color:var(--color-red);}'
+ '.pyfn-note.ok{border-color:var(--color-green);}'
+ '.pyfn-legb{display:flex;flex-direction:column;gap:5px;margin-top:2px;}'
+ '.pyfn-legb-row{display:flex;align-items:center;gap:12px;padding:7px 12px;border-radius:6px;border:1px solid var(--background-modifier-border);background:var(--background-secondary);font-family:var(--font-monospace);font-size:11.5px;}'
+ '.pyfn-ll{font-weight:700;font-size:14px;width:16px;flex-shrink:0;color:var(--interactive-accent);}'
+ '.pyfn-ln{color:var(--color-purple);width:105px;flex-shrink:0;}'
+ '.pyfn-ld{color:var(--text-muted);font-size:11px;}'
+ '.pyfn-practices{display:flex;flex-direction:column;gap:5px;margin-top:2px;}'
+ '.pyfn-pitem{display:flex;align-items:flex-start;gap:8px;font-size:12px;padding:7px 10px;background:var(--background-secondary);border-radius:5px;}'
+ '.pyfn-picon{flex-shrink:0;margin-top:1px;}'
+ '.pyfn-flow{display:flex;flex-wrap:wrap;gap:0;margin-bottom:10px;}'
+ '.pyfn-fstep{flex:1;min-width:100px;background:var(--background-secondary);border:1px solid var(--background-modifier-border);padding:9px 12px;font-family:var(--font-monospace);}'
+ '.pyfn-fstep+.pyfn-fstep{border-left:none;}'
+ '.pyfn-fstep:first-child{border-radius:6px 0 0 6px;}'
+ '.pyfn-fstep:last-child{border-radius:0 6px 6px 0;}'
+ '.pyfn-fl{font-size:9.5px;color:var(--text-faint);margin-bottom:3px;text-transform:uppercase;letter-spacing:.05em;}'
+ '.pyfn-fc{font-size:11px;color:var(--color-purple);}'
+ '@media(max-width:520px){.pyfn-grid2{grid-template-columns:1fr;}}'
+ '</style>';

// ── 辅助函数（纯字符串拼接，无嵌套模板字符串）────────────────
function h(s) {
    s = s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    var kws = 'def|class|return|yield|from|import|if|else|elif|for|while|in|not|and|or|is|None|True|False|pass|raise|with|as|lambda|global|nonlocal|try|except|finally';
    s = s.replace(/(#[^\n]*)/g, '<span class="pc">$1</span>');
    s = s.replace(/("""[\s\S]*?"""|"[^"\n]*"|'[^'\n]*')/g, '<span class="ps">$1</span>');
    s = s.replace(new RegExp('\\b(' + kws + ')\\b', 'g'), '<span class="pk">$1</span>');
    s = s.replace(/(@[\w.]+)/g, '<span class="pf">$1</span>');
    s = s.replace(/\b(\d+)\b/g, '<span class="pn">$1</span>');
    return s;
}
function cd(s)          { return '<pre class="pyfn-pre">' + h(s) + '</pre>'; }
function ca(ti, bo, su) { return '<div class="pyfn-card"><div class="pyfn-card-title">' + ti + '</div>' + (su ? '<div class="pyfn-card-sub">' + su + '</div>' : '') + bo + '</div>'; }
function g2(a, b)       { return '<div class="pyfn-grid2"><div>' + a + '</div><div>' + b + '</div></div>'; }
function nt(t, cl)      { return '<div class="pyfn-note ' + (cl || '') + '">' + t + '</div>'; }

// ── 代码字符串（template literal 赋值给变量，不在 ${} 内嵌套）──

// Panel 1
var s1a = 'def greet(name: str, greeting: str = "你好") -> str:\n'
        + '    """文档字符串：描述函数用途"""          # docstring\n'
        + '    return f"{greeting}, {name}!"\n\n'
        + 'greet("Jun")                               # 使用默认参数\n'
        + 'greet("Jun", "Hi")                         # 覆盖默认值\n'
        + 'greet(greeting="Hi", name="Jun")           # 关键字参数，顺序无关';
var s1b = 'def f(pos_only, /,\n      normal,\n      *args,\n      kw_only,\n      **kwargs): ...';
var s1c = 'lst = [1, 2, 3]\ndct = {"a": 1, "b": 2}\n\nf(*lst)    # 展开为位置参数\nf(**dct)   # 展开为关键字参数';
var s1d = '# * 后面的参数必须用名称传入\ndef create_user(name, *, role, active=True):\n    pass\n\ncreate_user("Jun", role="admin")   # OK\ncreate_user("Jun", "admin")        # TypeError';

// Panel 2
var s2a = 'def nothing():\n    pass           # 隐式返回 None\n\ndef multi():\n    return 1, "a", True   # 实为 tuple\n\nx, y, z = multi()         # 解包接收';
var s2b = 'def add(x: int, y: int) -> int:\n    return x + y\n\n# 可能返回 None（3.10+）\ndef find(name: str) -> str | None:\n    ...';
var s2c = 'from collections.abc import Callable\nfrom typing import TypeVar\n\n# 注解函数类型\ndef apply(func: Callable[[int], str], value: int) -> str:\n    return func(value)\n\n# 泛型函数\nT = TypeVar("T")\ndef first(items: list[T]) -> T:\n    return items[0]';
var s2d = 'from typing import TypeVar, ParamSpec\nfrom collections.abc import Callable\n\nP = ParamSpec("P")\nT = TypeVar("T")\n\ndef add_logging(f: Callable[P, T]) -> Callable[P, T]:\n    def inner(*args: P.args, **kwargs: P.kwargs) -> T:\n        print(f"调用 {f.__name__}")\n        return f(*args, **kwargs)\n    return inner';

// Panel 3
var s3a = 'count = 0\n\ndef increment():\n    global count    # 声明修改全局\n    count += 1\n\nincrement()\nprint(count)    # 1';
var s3b = 'def outer():\n    x = 10\n    def inner():\n        nonlocal x   # 修改外层\n        x += 1\n    inner()\n    return x     # 11';

// Panel 4
var s4a = 'def double(x): return x * 2\n\nf = double              # 赋值给变量\nfuncs = [double, abs]   # 放入列表\n\ndouble.__name__         # \'double\'\ndouble.__doc__          # docstring 内容';
var s4b = 'def apply(func, value):\n    return func(value)\n\napply(double, 5)   # 10\napply(abs, -3)     # 3';
var s4c = 'def make_mult(n):\n    def mult(x):\n        return x * n\n    return mult\n\ntriple = make_mult(3)\ntriple(5)   # 15';

// Panel 5
var s5a = 'lambda 参数: 表达式\n\nsquare = lambda x: x ** 2\nadd    = lambda x, y: x + y';
var s5b = 'nums = [3, 1, 4, 1, 5]\nsorted(nums, key=lambda x: -x)          # 降序\n\npairs = [(1, "b"), (2, "a")]\nsorted(pairs, key=lambda p: p[1])       # 按第二元素\n\nnumbers = [1, 2, 3, 4]\nlist(map(lambda x: x * 2, numbers))    # [2, 4, 6, 8]';

// Panel 6
var s6a = 'def counter(start=0):\n    count = [start]          # 用列表绕过 nonlocal\n\n    def increment():\n        count[0] += 1\n        return count[0]\n\n    return increment\n\nc = counter()\nc()   # 1\nc()   # 2\n\nc.__closure__            # 闭包单元列表\nc.__code__.co_freevars   # (\'count\',)';
var s6b = '# 错误：所有函数最终共享 i=4\nfuncs = [lambda x: i * x for i in range(5)]\nfuncs[0](1)   # 4，不是 0！\n\n# 修复：用默认参数立即绑定\nfuncs = [lambda x, i=i: i * x for i in range(5)]\nfuncs[0](1)   # 0';

// Panel 7
var s7a = 'from functools import wraps\n\ndef log(func):\n    @wraps(func)          # 保留 __name__ / __doc__\n    def wrapper(*args, **kwargs):\n        print(f"调用 {func.__name__}")\n        result = func(*args, **kwargs)\n        return result\n    return wrapper\n\n@log\ndef greet(name): return f"Hi, {name}"';
var s7b = 'def repeat(n):\n    def decorator(func):\n        @wraps(func)\n        def wrapper(*a, **kw):\n            for _ in range(n):\n                func(*a, **kw)\n        return wrapper\n    return decorator\n\n@repeat(3)\ndef say_hi(): print("Hi")';
var s7c = '@decorator_a\n@decorator_b\ndef func(): ...\n\n# 等价于：\nfunc = decorator_a(\n    decorator_b(func)\n)\n# 从下往上应用';

// Panel 8
var s8a = 'def fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a           # 暂停，返回值，保存状态\n        a, b = b, a + b\n\ngen = fibonacci()\nnext(gen)   # 0\nnext(gen)   # 1\n\n# 生成器表达式（内存友好）\nsquares = (x**2 for x in range(1000000))\ntotal = sum(squares)';
var s8b = 'def accumulator():\n    total = 0\n    while True:\n        val = yield total\n        total += val or 0\n\nacc = accumulator()\nnext(acc)        # 必须先 prime\nacc.send(5)      # 5\nacc.send(3)      # 8\nacc.close()      # 抛出 GeneratorExit';
var s8c = 'def chain(*iterables):\n    for it in iterables:\n        yield from it\n        # 比 for x in it: yield x 更好\n        # 且正确传递 send/throw/close\n\nlist(chain([1,2], [3,4]))\n# [1, 2, 3, 4]';

// Panel 9
var s9a = 'from functools import reduce\n\nreduce(lambda x, y: x + y, [1, 2, 3, 4])      # 10\nreduce(lambda x, y: x * y, [1, 2, 3, 4], 1)   # 24（含初始值）\n\n# 生成器表达式比 map/filter 链更 Pythonic\nevens = [x*2 for x in range(10) if x % 2 == 0]\n\n# zip 配对遍历\nfor name, score in zip(["Alice","Bob"], [95, 87]):\n    print(f"{name}: {score}")';

// Panel 10
var s10a = 'from functools import lru_cache, cache\n\n@lru_cache(maxsize=128)      # 缓存最近 128 个调用\ndef fib(n):\n    if n < 2: return n\n    return fib(n-1) + fib(n-2)\n\n@cache                       # 3.9+，无限缓存，更快\ndef fib(n): ...\n\nfib.cache_info()    # CacheInfo(hits=28, misses=16, ...)\nfib.cache_clear()   # 清空缓存';
var s10b = 'from functools import partial\nimport os\n\ndef power(base, exp): return base ** exp\nsquare = partial(power, exp=2)\ncube   = partial(power, exp=3)\nsquare(5)   # 25\n\njoin_home = partial(os.path.join, "/home/user")\njoin_home("docs", "file.txt")  # \'/home/user/docs/file.txt\'';
var s10c = 'from functools import wraps\n\ndef my_decorator(func):\n    @wraps(func)\n    def wrapper(*a, **kw):\n        return func(*a, **kw)\n    return wrapper\n\n# 没有 @wraps：func.__name__ -> \'wrapper\'\n# 有 @wraps： func.__name__ -> 原函数名';
var s10d = 'from functools import singledispatch\n\n@singledispatch\ndef process(data):\n    raise TypeError(type(data))\n\n@process.register(int)\ndef _(data): return data * 2\n\n@process.register(str)\ndef _(data): return data.upper()\n\nprocess(5)     # 10\nprocess("hi")  # \'HI\'';

// Panel 11
var s11a = '# 默认参数在函数定义时求值一次，后续调用共享同一对象\n\n# 错误：list 跨调用共享\ndef append_to(item, to=[]):\n    to.append(item)\n    return to\n\nappend_to(1)   # [1]\nappend_to(2)   # [1, 2]  <- 出乎意料！\n\n# 正确：用 None 作哨兵值\ndef append_to(item, to=None):\n    if to is None:\n        to = []\n    to.append(item)\n    return to';
var s11b = '# 不可变对象：函数内修改不影响外部\ndef f(x):\n    x = 20     # 只是重新绑定局部变量\na = 10; f(a); print(a)    # 10（不变）\n\n# 可变对象：函数内修改会影响外部\ndef f(lst):\n    lst[0] = 99\nitems = [1, 2, 3]; f(items); print(items)  # [99, 2, 3]!\n\n# 如需保护，传入副本\nf(items[:])    # 或 f(list(items))';
var s11c = '# 错误：所有 lambda 最终用 i=4\nfuncs = [lambda x: i * x for i in range(5)]\nfuncs[0](1)   # 4，不是 0\n\n# 修复：用默认参数立即绑定\nfuncs = [lambda x, i=i: i * x for i in range(5)]\nfuncs[0](1)   # 0';

// ── 共用 HTML 片段 ──────────────────────────────────────────
var legb = '<div class="pyfn-legb">'
    + '<div class="pyfn-legb-row"><span class="pyfn-ll">L</span><span class="pyfn-ln">Local</span><span class="pyfn-ld">当前函数内部变量</span></div>'
    + '<div class="pyfn-legb-row"><span class="pyfn-ll">E</span><span class="pyfn-ln">Enclosing</span><span class="pyfn-ld">外层函数（闭包链）</span></div>'
    + '<div class="pyfn-legb-row"><span class="pyfn-ll">G</span><span class="pyfn-ln">Global</span><span class="pyfn-ld">模块顶层命名空间</span></div>'
    + '<div class="pyfn-legb-row"><span class="pyfn-ll">B</span><span class="pyfn-ln">Built-in</span><span class="pyfn-ld">Python 内置（print, len…）</span></div>'
    + '</div>';

var lifecycle = '<div class="pyfn-flow">'
    + '<div class="pyfn-fstep"><div class="pyfn-fl">创建</div><div class="pyfn-fc">gen = my_gen()</div></div>'
    + '<div class="pyfn-fstep"><div class="pyfn-fl">首次 next</div><div class="pyfn-fc">运行到 yield</div></div>'
    + '<div class="pyfn-fstep"><div class="pyfn-fl">后续 next</div><div class="pyfn-fc">从断点继续</div></div>'
    + '<div class="pyfn-fstep"><div class="pyfn-fl">耗尽</div><div class="pyfn-fc">StopIteration</div></div>'
    + '</div>';

var tbl_params = '<table class="pyfn-tbl"><tr><th>写法</th><th>名称</th><th>说明</th></tr>'
    + '<tr><td>def f(x)</td><td>普通参数</td><td>按位置或名称传入</td></tr>'
    + '<tr><td>def f(x=0)</td><td>默认参数</td><td>调用时可省略</td></tr>'
    + '<tr><td>def f(*args)</td><td>可变位置参数</td><td>收集为 tuple</td></tr>'
    + '<tr><td>def f(**kwargs)</td><td>可变关键字参数</td><td>收集为 dict</td></tr>'
    + '<tr><td>def f(x,/,y,*,z)</td><td>位置/关键字限定 3.8+</td><td>/ 前仅位置；* 后仅关键字</td></tr>'
    + '</table>';

var tbl_builtins = '<table class="pyfn-tbl"><tr><th>函数</th><th>说明</th><th>示例</th></tr>'
    + '<tr><td>map(f, it)</td><td>对每个元素应用 f</td><td>map(str, [1,2,3])</td></tr>'
    + '<tr><td>filter(f, it)</td><td>保留 f 返回 True 的元素</td><td>filter(None, [0,1,""])</td></tr>'
    + '<tr><td>sorted(it, key=f)</td><td>排序，key 指定比较依据</td><td>sorted(words, key=len)</td></tr>'
    + '<tr><td>max/min(it, key=f)</td><td>按 key 取极值</td><td>max(items, key=lambda x:x.p)</td></tr>'
    + '<tr><td>zip(a, b)</td><td>打包为 (a_i, b_i) 迭代器</td><td>zip([1,2], ["a","b"])</td></tr>'
    + '<tr><td>enumerate(it, start=0)</td><td>返回 (index, value) 对</td><td>enumerate(items, 1)</td></tr>'
    + '<tr><td>any(it) / all(it)</td><td>任意/全部为真</td><td>any(x &gt; 0 for x in lst)</td></tr>'
    + '</table>';

var tbl_deco = '<table class="pyfn-tbl">'
    + '<tr><td>@log</td><td>记录调用信息、参数、返回值</td></tr>'
    + '<tr><td>@lru_cache</td><td>缓存结果，避免重复计算</td></tr>'
    + '<tr><td>@require_login</td><td>权限验证，未登录时拦截</td></tr>'
    + '<tr><td>@timer</td><td>统计函数执行耗时</td></tr>'
    + '<tr><td>@retry(n)</td><td>失败时自动重试 n 次</td></tr>'
    + '</table>';

var closure_cond = '<div class="pyfn-practices">'
    + '<div class="pyfn-pitem"><span class="pyfn-picon">①</span>必须有嵌套函数（函数内定义函数）</div>'
    + '<div class="pyfn-pitem"><span class="pyfn-picon">②</span>内层函数引用了外层函数的局部变量</div>'
    + '<div class="pyfn-pitem"><span class="pyfn-picon">③</span>外层函数返回内层函数</div>'
    + '</div>';

var best_practices = '<div class="pyfn-practices">'
    + '<div class="pyfn-pitem"><span class="pyfn-picon" style="color:var(--color-green)">✓</span>用 None 替代可变类型（list/dict）作默认参数</div>'
    + '<div class="pyfn-pitem"><span class="pyfn-picon" style="color:var(--color-green)">✓</span>写装饰器时始终加 @functools.wraps</div>'
    + '<div class="pyfn-pitem"><span class="pyfn-picon" style="color:var(--color-green)">✓</span>为公开函数添加类型注解和 docstring</div>'
    + '<div class="pyfn-pitem"><span class="pyfn-picon" style="color:var(--color-green)">✓</span>单函数只做一件事（单一职责原则）</div>'
    + '<div class="pyfn-pitem"><span class="pyfn-picon" style="color:var(--color-green)">✓</span>lru_cache 只用于纯函数（无副作用，参数可哈希）</div>'
    + '<div class="pyfn-pitem"><span class="pyfn-picon" style="color:var(--color-green)">✓</span>用 yield from 替代 for x in sub: yield x</div>'
    + '<div class="pyfn-pitem"><span class="pyfn-picon" style="color:var(--color-green)">✓</span>生成器优先于大列表（内存效率更高）</div>'
    + '<div class="pyfn-pitem"><span class="pyfn-picon" style="color:var(--color-green)">✓</span>闭包循环中用默认参数立即绑定，避免晚绑定</div>'
    + '</div>';

// ── 组装各 Panel ────────────────────────────────────────────
var p1 = ca('函数骨架', cd(s1a))
    + ca('五种参数类型', tbl_params)
    + g2(ca('完整参数顺序', cd(s1b)), ca('解包传参', cd(s1c)))
    + ca('强制关键字参数', cd(s1d), '用 * 强制调用者写明参数名，提升可读性');

var p2 = nt('类型注解在运行时不强制执行，但能帮助 IDE、mypy 等工具做静态检查。')
    + g2(ca('基本返回', cd(s2a)), ca('基础注解', cd(s2b)))
    + ca('Callable / TypeVar', cd(s2c))
    + ca('ParamSpec — 注解装饰器（3.10+）', cd(s2d));

var p3 = ca('LEGB 查找顺序', legb)
    + g2(ca('global — 修改全局变量', cd(s3a)), ca('nonlocal — 修改外层变量', cd(s3b)));

var p4 = nt('Python 函数是对象，可赋值、传递、存储、作为返回值——这是闭包和装饰器的核心基础。')
    + ca('函数即对象', cd(s4a))
    + g2(ca('高阶函数：接收函数', cd(s4b)), ca('高阶函数：返回函数', cd(s4c)));

var p5 = nt('Lambda 是单行表达式的匿名函数，不能包含语句（赋值、循环等）。复杂逻辑请用 def。')
    + ca('语法', cd(s5a))
    + ca('常见用途：作为 key 传入高阶函数', cd(s5b));

var p6 = ca('构成条件', closure_cond)
    + ca('示例：有状态计数器', cd(s6a))
    + ca('⚠️ 晚绑定陷阱', cd(s6b), '循环中创建闭包时，变量在调用时才查找，而非定义时');

var p7 = nt('@decorator 是 func = decorator(func) 的语法糖。装饰器本质是接收函数、返回函数的高阶函数。')
    + ca('基本装饰器', cd(s7a))
    + g2(ca('带参数的装饰器', cd(s7b)), ca('叠加装饰器', cd(s7c)))
    + ca('常见应用场景', tbl_deco);

var p8 = nt('生成器用 yield 替代 return，实现惰性求值——每次只产生一个值，不把整个序列存入内存。')
    + ca('基础用法', cd(s8a))
    + ca('生命周期', lifecycle)
    + g2(ca('send / throw / close', cd(s8b)), ca('yield from', cd(s8c)));

var p9 = ca('函数一览', tbl_builtins)
    + ca('reduce（需导入）+ 实用模式', cd(s9a));

var p10 = ca('lru_cache — 缓存函数结果', cd(s10a))
    + nt('⚠️ 只应用于纯函数（同输入→同输出）；参数必须可哈希（不能是 list/dict）', 'warn')
    + ca('partial — 固定部分参数', cd(s10b))
    + g2(ca('wraps — 保留元信息', cd(s10c)), ca('singledispatch — 函数重载', cd(s10d)));

var p11 = ca('⚠️ 陷阱 1：可变对象作为默认参数', cd(s11a))
    + ca('⚠️ 陷阱 2：参数传递语义', cd(s11b))
    + ca('⚠️ 陷阱 3：闭包晚绑定', cd(s11c))
    + ca('✅ 最佳实践清单', best_practices);

// ── Tabs 定义 ──────────────────────────────────────────────
var tabs = [
    ['p1',  '基本结构',    p1],
    ['p2',  '返回值 & 注解', p2],
    ['p3',  '作用域',     p3],
    ['p4',  '一等函数',   p4],
    ['p5',  'Lambda',    p5],
    ['p6',  '闭包',      p6],
    ['p7',  '装饰器',    p7],
    ['p8',  '生成器',    p8],
    ['p9',  '内置函数',  p9],
    ['p10', 'functools', p10],
    ['p11', '陷阱 & 实践', p11],
];

var tabsHtml = '', panelsHtml = '';
for (var i = 0; i < tabs.length; i++) {
    var id = tabs[i][0], label = tabs[i][1], content = tabs[i][2];
    tabsHtml   += '<button class="pyfn-tab' + (i===0?' active':'') + '" data-id="' + id + '">' + label + '</button>';
    panelsHtml += '<div id="pyfn-' + id + '" class="pyfn-panel' + (i===0?' active':'') + '">' + content + '</div>';
}

// ── 渲染 ────────────────────────────────────────────────────
c.innerHTML = css
    + '<div class="pyfn">'
    + '<div class="pyfn-tabs">' + tabsHtml + '</div>'
    + panelsHtml
    + '</div>';

// Tab 切换
c.querySelectorAll('.pyfn-tab').forEach(function(btn) {
    btn.addEventListener('click', function() {
        c.querySelectorAll('.pyfn-tab').forEach(function(b) { b.classList.remove('active'); });
        c.querySelectorAll('.pyfn-panel').forEach(function(p) { p.classList.remove('active'); });
        btn.classList.add('active');
        c.querySelector('#pyfn-' + btn.dataset.id).classList.add('active');
    });
});
```

