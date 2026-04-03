---
tags:
  - 编程/Python
type: note
status: 🌳
created: 2026-03-12
---
# `__init__.py` 详解笔记

## 一、是什么？

`__init__.py` 是 Python **包（package）的初始化文件**。

它的存在告诉 Python 解释器：**"这个文件夹是一个可导入的包"**。

```
my_package/
    __init__.py      ← 有它，才是"包"
    Enhancer.py
    utils.py
```

> 💡 Python 3.3+ 引入了"命名空间包"，允许没有 `__init__.py` 的包存在，但实际项目中仍推荐保留它。

---

## 二、核心作用

### 1. 标识包的存在

没有 `__init__.py`，文件夹只是普通目录，无法被 `import`。

### 2. 提升子模块内容到包的顶层

```python
# __init__.py
from .Enhancer import SimpleEnhancer
```

**效果对比：**

|情况|导入写法|
|---|---|
|没有 `__init__.py` 处理|`from my_package.Enhancer import SimpleEnhancer`|
|有 `__init__.py` 处理|`from my_package import SimpleEnhancer` ✅|

用户无需了解包的内部结构，导入路径更简洁。

### 3. 控制公开接口（`__all__`）

```python
__all__ = ['SimpleEnhancer']
```

- 声明当用户执行 `from my_package import *` 时，**只暴露列表中的内容**
- 是一种"白名单"机制，隐藏内部实现细节

### 4. 包加载时的初始化逻辑

```python
# __init__.py 中可以执行任意初始化代码
print("包已加载")
DEFAULT_CONFIG = {"version": "1.0"}
```

首次 `import` 包时，`__init__.py` 会自动执行一次。

---

## 三、完整示例解析

```python
# my_package/__init__.py

from .Enhancer import SimpleEnhancer   # ① 提升到顶层

__all__ = ['SimpleEnhancer']           # ② 声明公开接口
```

|代码|含义|
|---|---|
|`from .Enhancer`|`.` 表示当前包，即相对导入|
|`import SimpleEnhancer`|从 `Enhancer.py` 中取出这个类|
|`__all__`|控制 `import *` 的行为|

---

## 四、总结

> `__init__.py` 就像包的**门面/入口**，主要做三件事：
> 
> 1. **标识**：让文件夹成为可导入的包
> 2. **整合**：把子模块的内容提升到包顶层，简化导入路径
> 3. **管控**：通过 `__all__` 控制对外暴露的接口