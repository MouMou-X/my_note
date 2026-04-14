---
tags: [python, cheatsheet]
---
# Python类速查表

```dataviewjs
const c = dv.container;

const css = `
<style id="py-cheat-style">
.py-cheat *{box-sizing:border-box;margin:0;padding:0;}
.py-cheat{font-family:var(--font-interface);padding:4px 0 16px;}
.py-tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px;}
.py-tab{font-size:12px;padding:4px 12px;border-radius:999px;border:1px solid var(--background-modifier-border);background:transparent;color:var(--text-muted);cursor:pointer;transition:all .15s;}
.py-tab.active{background:var(--background-secondary);color:var(--text-normal);font-weight:500;}
.py-panel{display:none;}
.py-panel.active{display:block;}
.py-card{background:var(--background-primary);border:1px solid var(--background-modifier-border);border-radius:8px;padding:12px 16px;margin-bottom:10px;}
.py-card-title{font-size:11px;font-weight:500;color:var(--text-muted);margin-bottom:8px;letter-spacing:.04em;text-transform:uppercase;}
.py-pre{font-family:var(--font-monospace);font-size:12.5px;line-height:1.7;color:var(--text-normal);white-space:pre;overflow-x:auto;}
.py-kw{color:var(--color-purple);font-weight:500;}
.py-fn{color:var(--color-green);}
.py-cm{color:var(--text-faint);font-style:italic;}
.py-st{color:var(--color-orange);}
.py-grid2{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
.py-tbl{width:100%;font-size:12.5px;border-collapse:collapse;}
.py-tbl td{padding:5px 6px;border-bottom:1px solid var(--background-modifier-border);vertical-align:top;}
.py-tbl td:first-child{font-family:var(--font-monospace);font-size:12px;color:var(--color-purple);white-space:nowrap;width:44%;}
.py-tbl tr:last-child td{border-bottom:none;}
@media(max-width:500px){.py-grid2{grid-template-columns:1fr;}}
</style>`;

const html = `
<div class="py-cheat">
  <div class="py-tabs">
    <button class="py-tab active" data-tab="basic">基本结构</button>
    <button class="py-tab" data-tab="special">魔术方法</button>
    <button class="py-tab" data-tab="inherit">继承</button>
    <button class="py-tab" data-tab="decorators">装饰器</button>
    <button class="py-tab" data-tab="patterns">常用模式</button>
  </div>

  <!-- 基本结构 -->
  <div id="py-basic" class="py-panel active">
    <div class="py-card">
      <div class="py-card-title">类的骨架</div>
      <pre class="py-pre"><span class="py-kw">class</span> <span class="py-fn">MyClass</span>:
    class_var = <span class="py-st">"所有实例共享"</span>   <span class="py-cm"># 类属性</span>

    <span class="py-kw">def</span> <span class="py-fn">__init__</span>(<span class="py-kw">self</span>, x, y=<span class="py-st">0</span>):       <span class="py-cm"># 构造方法</span>
        <span class="py-kw">self</span>.x = x                    <span class="py-cm"># 实例属性</span>
        <span class="py-kw">self</span>.y = y

    <span class="py-kw">def</span> <span class="py-fn">method</span>(<span class="py-kw">self</span>):                 <span class="py-cm"># 实例方法</span>
        <span class="py-kw">return</span> <span class="py-kw">self</span>.x

obj = MyClass(<span class="py-st">10</span>)                    <span class="py-cm"># 创建实例</span>
obj.method()                         <span class="py-cm"># 调用方法</span></pre>
    </div>
    <div class="py-grid2">
      <div class="py-card">
        <div class="py-card-title">访问规范（约定）</div>
        <table class="py-tbl">
          <tr><td>self.name</td><td>公开属性</td></tr>
          <tr><td>self._name</td><td>半私有，不建议外部访问</td></tr>
          <tr><td>self.__name</td><td>强私有，名称改写保护</td></tr>
        </table>
      </div>
      <div class="py-card">
        <div class="py-card-title">实例 / 类 / 静态方法</div>
        <table class="py-tbl">
          <tr><td>def f(self)</td><td>实例方法</td></tr>
          <tr><td>@classmethod<br>def f(cls)</td><td>类方法</td></tr>
          <tr><td>@staticmethod<br>def f()</td><td>静态方法</td></tr>
        </table>
      </div>
    </div>
  </div>

  <!-- 魔术方法 -->
  <div id="py-special" class="py-panel">
    <div class="py-card">
      <div class="py-card-title">常用魔术方法一览</div>
      <table class="py-tbl">
        <tr><td>__init__(self, ...)</td><td>创建实例时调用</td></tr>
        <tr><td>__str__(self)</td><td>print(obj) 显示的字符串</td></tr>
        <tr><td>__repr__(self)</td><td>调试时的字符串表示</td></tr>
        <tr><td>__len__(self)</td><td>len(obj)</td></tr>
        <tr><td>__eq__(self, other)</td><td>obj == other</td></tr>
        <tr><td>__lt__(self, other)</td><td>obj &lt; other（也启用排序）</td></tr>
        <tr><td>__add__(self, other)</td><td>obj + other</td></tr>
        <tr><td>__getitem__(self, key)</td><td>obj[key]</td></tr>
        <tr><td>__contains__(self, x)</td><td>x in obj</td></tr>
        <tr><td>__iter__(self)</td><td>for x in obj 迭代</td></tr>
        <tr><td>__enter__ / __exit__</td><td>with 语句上下文管理器</td></tr>
        <tr><td>__call__(self, ...)</td><td>把实例当函数调用 obj()</td></tr>
      </table>
    </div>
    <div class="py-card">
      <div class="py-card-title">示例</div>
      <pre class="py-pre"><span class="py-kw">class</span> <span class="py-fn">Point</span>:
    <span class="py-kw">def</span> <span class="py-fn">__init__</span>(<span class="py-kw">self</span>, x, y):
        <span class="py-kw">self</span>.x, <span class="py-kw">self</span>.y = x, y

    <span class="py-kw">def</span> <span class="py-fn">__str__</span>(<span class="py-kw">self</span>):
        <span class="py-kw">return</span> <span class="py-st">f"({self.x}, {self.y})"</span>

    <span class="py-kw">def</span> <span class="py-fn">__add__</span>(<span class="py-kw">self</span>, other):
        <span class="py-kw">return</span> Point(<span class="py-kw">self</span>.x + other.x, <span class="py-kw">self</span>.y + other.y)

p = Point(<span class="py-st">1</span>, <span class="py-st">2</span>) + Point(<span class="py-st">3</span>, <span class="py-st">4</span>)
print(p)   <span class="py-cm"># (4, 6)</span></pre>
    </div>
  </div>

  <!-- 继承 -->
  <div id="py-inherit" class="py-panel">
    <div class="py-card">
      <div class="py-card-title">单继承</div>
      <pre class="py-pre"><span class="py-kw">class</span> <span class="py-fn">Animal</span>:
    <span class="py-kw">def</span> <span class="py-fn">__init__</span>(<span class="py-kw">self</span>, name):
        <span class="py-kw">self</span>.name = name

    <span class="py-kw">def</span> <span class="py-fn">speak</span>(<span class="py-kw">self</span>):
        <span class="py-kw">raise</span> NotImplementedError

<span class="py-kw">class</span> <span class="py-fn">Dog</span>(Animal):            <span class="py-cm"># 继承 Animal</span>
    <span class="py-kw">def</span> <span class="py-fn">speak</span>(<span class="py-kw">self</span>):           <span class="py-cm"># 重写方法</span>
        <span class="py-kw">return</span> <span class="py-st">"汪！"</span>

    <span class="py-kw">def</span> <span class="py-fn">fetch</span>(<span class="py-kw">self</span>):           <span class="py-cm"># 新增方法</span>
        <span class="py-kw">return</span> <span class="py-st">"捡回来了"</span></pre>
    </div>
    <div class="py-grid2">
      <div class="py-card">
        <div class="py-card-title">super() 调用父类</div>
        <pre class="py-pre"><span class="py-kw">class</span> <span class="py-fn">Dog</span>(Animal):
  <span class="py-kw">def</span> <span class="py-fn">__init__</span>(<span class="py-kw">self</span>, name, breed):
    <span class="py-kw">super</span>().__init__(name)  <span class="py-cm"># 父类 init</span>
    <span class="py-kw">self</span>.breed = breed</pre>
      </div>
      <div class="py-card">
        <div class="py-card-title">检查继承关系</div>
        <pre class="py-pre">isinstance(d, Dog)      <span class="py-cm"># True</span>
isinstance(d, Animal)   <span class="py-cm"># True</span>
issubclass(Dog, Animal) <span class="py-cm"># True</span>
Dog.__mro__             <span class="py-cm"># 继承链</span></pre>
      </div>
    </div>
    <div class="py-card">
      <div class="py-card-title">抽象基类（强制子类实现方法）</div>
      <pre class="py-pre"><span class="py-kw">from</span> abc <span class="py-kw">import</span> ABC, abstractmethod

<span class="py-kw">class</span> <span class="py-fn">Shape</span>(ABC):
    <span class="py-kw">@abstractmethod</span>
    <span class="py-kw">def</span> <span class="py-fn">area</span>(<span class="py-kw">self</span>) -> float: ...  <span class="py-cm"># 子类必须实现</span>

<span class="py-kw">class</span> <span class="py-fn">Circle</span>(Shape):
    <span class="py-kw">def</span> <span class="py-fn">area</span>(<span class="py-kw">self</span>): <span class="py-kw">return</span> 3.14 * <span class="py-kw">self</span>.r**<span class="py-st">2</span></pre>
    </div>
  </div>

  <!-- 装饰器 -->
  <div id="py-decorators" class="py-panel">
    <div class="py-grid2">
      <div class="py-card">
        <div class="py-card-title">@property — 受控属性</div>
        <pre class="py-pre"><span class="py-kw">class</span> <span class="py-fn">Person</span>:
  <span class="py-kw">def</span> <span class="py-fn">__init__</span>(<span class="py-kw">self</span>, age):
    <span class="py-kw">self</span>._age = age

  <span class="py-kw">@property</span>
  <span class="py-kw">def</span> <span class="py-fn">age</span>(<span class="py-kw">self</span>):       <span class="py-cm"># getter</span>
    <span class="py-kw">return</span> <span class="py-kw">self</span>._age

  <span class="py-kw">@age.setter</span>
  <span class="py-kw">def</span> <span class="py-fn">age</span>(<span class="py-kw">self</span>, v):    <span class="py-cm"># setter</span>
    <span class="py-kw">if</span> v < <span class="py-st">0</span>: <span class="py-kw">raise</span> ValueError
    <span class="py-kw">self</span>._age = v</pre>
      </div>
      <div class="py-card">
        <div class="py-card-title">@classmethod / @staticmethod</div>
        <pre class="py-pre"><span class="py-kw">class</span> <span class="py-fn">User</span>:
  <span class="py-kw">@classmethod</span>
  <span class="py-kw">def</span> <span class="py-fn">from_dict</span>(cls, d):  <span class="py-cm"># 工厂方法</span>
    <span class="py-kw">return</span> cls(d[<span class="py-st">'name'</span>])

  <span class="py-kw">@staticmethod</span>
  <span class="py-kw">def</span> <span class="py-fn">validate</span>(name):    <span class="py-cm"># 工具函数</span>
    <span class="py-kw">return</span> len(name) > <span class="py-st">0</span>

u = User.from_dict({<span class="py-st">'name'</span>: <span class="py-st">'Jun'</span>})</pre>
      </div>
    </div>
    <div class="py-card">
      <div class="py-card-title">@dataclass — 省掉样板代码（Python 3.7+）</div>
      <pre class="py-pre"><span class="py-kw">from</span> dataclasses <span class="py-kw">import</span> dataclass, field

<span class="py-kw">@dataclass</span>
<span class="py-kw">class</span> <span class="py-fn">Point</span>:
    x: float
    y: float = <span class="py-st">0.0</span>                    <span class="py-cm"># 默认值</span>
    tags: list = field(default_factory=list)

<span class="py-cm"># 自动生成 __init__ / __repr__ / __eq__</span>
p = Point(<span class="py-st">1.0</span>, <span class="py-st">2.0</span>)
print(p)   <span class="py-cm"># Point(x=1.0, y=2.0, tags=[])</span></pre>
    </div>
  </div>

  <!-- 常用模式 -->
  <div id="py-patterns" class="py-panel">
    <div class="py-card">
      <div class="py-card-title">上下文管理器（with 语句）</div>
      <pre class="py-pre"><span class="py-kw">class</span> <span class="py-fn">Timer</span>:
    <span class="py-kw">def</span> <span class="py-fn">__enter__</span>(<span class="py-kw">self</span>):
        <span class="py-kw">import</span> time; <span class="py-kw">self</span>.start = time.time()
        <span class="py-kw">return</span> <span class="py-kw">self</span>

    <span class="py-kw">def</span> <span class="py-fn">__exit__</span>(<span class="py-kw">self</span>, *args):
        print(<span class="py-st">f"耗时 {time.time() - self.start:.2f}s"</span>)

<span class="py-kw">with</span> Timer():
    do_something()      <span class="py-cm"># 自动计时</span></pre>
    </div>
    <div class="py-card">
      <div class="py-card-title">单例模式</div>
      <pre class="py-pre"><span class="py-kw">class</span> <span class="py-fn">Singleton</span>:
    _instance = <span class="py-kw">None</span>

    <span class="py-kw">def</span> <span class="py-fn">__new__</span>(cls):
        <span class="py-kw">if</span> cls._instance <span class="py-kw">is None</span>:
            cls._instance = <span class="py-kw">super</span>().__new__(cls)
        <span class="py-kw">return</span> cls._instance

a = Singleton(); b = Singleton()
print(a <span class="py-kw">is</span> b)   <span class="py-cm"># True</span></pre>
    </div>
    <div class="py-card">
      <div class="py-card-title">可迭代对象（自定义 for 循环）</div>
      <pre class="py-pre"><span class="py-kw">class</span> <span class="py-fn">Countdown</span>:
    <span class="py-kw">def</span> <span class="py-fn">__init__</span>(<span class="py-kw">self</span>, n): <span class="py-kw">self</span>.n = n
    <span class="py-kw">def</span> <span class="py-fn">__iter__</span>(<span class="py-kw">self</span>): <span class="py-kw">return self</span>
    <span class="py-kw">def</span> <span class="py-fn">__next__</span>(<span class="py-kw">self</span>):
        <span class="py-kw">if self</span>.n &lt;= <span class="py-st">0</span>: <span class="py-kw">raise</span> StopIteration
        <span class="py-kw">self</span>.n -= <span class="py-st">1</span>; <span class="py-kw">return self</span>.n + <span class="py-st">1</span>

<span class="py-kw">for</span> i <span class="py-kw">in</span> Countdown(<span class="py-st">3</span>): print(i)  <span class="py-cm"># 3 2 1</span></pre>
    </div>
  </div>
</div>`;

c.innerHTML = css + html;

c.querySelectorAll('.py-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const target = tab.dataset.tab;
    c.querySelectorAll('.py-tab').forEach(t => t.classList.remove('active'));
    c.querySelectorAll('.py-panel').forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    c.querySelector('#py-' + target).classList.add('active');
  });
});
```
---
# 基本结构习题

## 第 1 题
下面的代码有什么问题？运行会报什么错？

```python
class Cat:
    def meow():
        return "喵～"

cat = Cat()
cat.meow()
```

<details>
<summary>答案</summary>

`meow` 缺少 `self` 参数。Python 调用 `cat.meow()` 时会自动把 `cat` 作为第一个参数传入，但 `meow` 没有参数来接收，报错：`TypeError: meow() takes 0 positional arguments but 1 was given`

```python
class Cat:
    def meow(self):
        return "喵～"
```

</details>

---

## 第 2 题
下面这段代码想记录一共创建了多少只猫，但运行结果不对。哪里出问题了？应该怎么修？

```python
class Cat:
    count = 0

    def __init__(self, name):
        self.name = name
        count += 1

cat1 = Cat("小白")
cat2 = Cat("旺财")
print(Cat.count)  # 期望输出 2，实际报错
```

<details>
<summary>答案</summary>

`count += 1` 里的 `count` 被 Python 当作局部变量，报 `UnboundLocalError`。要修改类属性，必须通过类本身来操作：

```python
class Cat:
    count = 0

    def __init__(self, name):
        self.name = name
        Cat.count += 1

cat1 = Cat("小白")
cat2 = Cat("旺财")
print(Cat.count)  # 2
```

</details>

---

## 第 3 题
下面的代码想让每只猫都能自我介绍，但运行会报错。你能找到问题在哪里吗？

```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce():
        return f"我叫 {self.name}，今年 {self.age} 岁"

cat = Cat("小白", 3)
print(cat.introduce())
```

<details>
<summary>答案</summary>

`introduce` 缺少 `self` 参数，和第 1 题一样的问题：

```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"我叫 {self.name}，今年 {self.age} 岁"

cat = Cat("小白", 3)
print(cat.introduce())  # 我叫 小白，今年 3 岁
```

</details>

---

## 第 4 题
下面的代码有什么问题？

```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat = Cat("小白")
print(cat.name)
```

<details>
<summary>答案</summary>

`__init__` 定义了两个参数 `name` 和 `age`，但创建实例时只传了 `name`，报错：`TypeError: __init__() missing 1 required positional argument: 'age'`

```python
cat = Cat("小白", 3)  # 补上 age
```

</details>

---

## 第 5 题
下面的代码输出是什么？先别运行，想一想：

```python
class Cat:
    sound = "喵"

    def __init__(self, name):
        self.name = name

cat1 = Cat("小白")
cat2 = Cat("旺财")

cat1.sound = "咪"
print(cat1.sound)
print(cat2.sound)
print(Cat.sound)
```

<details>
<summary>答案</summary>

输出：
```
咪
喵
喵
```

`cat1.sound = "咪"` 只在 `cat1` 上新建了一个实例属性，`cat2` 没有自己的 `sound` 实例属性，读取的仍是类属性 `Cat.sound`，所以不受影响。

</details>

