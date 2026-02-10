
# Python Import 机制详解

**标签:** #Python #基础语法 #Import #模块化编程

---

## 1. 核心概念：容器与内容

理解 `import` 的关键在于分清**物理文件**和**逻辑对象**的关系。

### 基本术语
- **包 (Package)**: 物理上表现为**文件夹**（通常包含 `__init__.py`）。它是包含模块的容器。
- **模块 (Module)**: 物理上表现为 **`.py` 文件**。它是包含代码（函数、类、变量）的容器。

> [!INFO] 核心逻辑
> Python 的导入机制就是从**容器**中取出**内容**的过程。

---

## 2. 语法结构解析

### 2.1 `from ... import ...` (精准导入)

这是你最困惑的部分。标准公式如下：

$$\text{from } \underbrace{\text{容器 (Package/Module)}}_{\text{去哪里找}} \text{ import } \underbrace{\text{目标 (Module/Class/Function/Var)}}_{\text{拿什么东西}}$$

**判定规则：**
1. **`from` 后面**：只能接**包**或**模块**（即文件夹或文件）。不能接类或函数。
2. **`import` 后面**：接的是**下一级**的内容。

#### 案例分析

| 代码 | `from` 后的身份 | `import` 后的身份 | 物理对应 |
| :--- | :--- | :--- | :--- |
| `from pathlib import Path` | **模块** (pathlib.py) | **类** (Class Path) | 文件 -> 类代码 |
| `from function import save_excel` | **模块** (function.py) | **函数** (Function) | 文件 -> 函数代码 |
| `from sklearn import linear_model` | **包** (sklearn 文件夹) | **子模块** (linear_model.py) | 文件夹 -> 文件 |

---

### 2.2 `import ...` (整体导入)

直接将整个模块或包放入当前的命名空间。

- **语法**: `import module_name`
- **使用**: 必须使用 `module_name.member` 的方式调用。
- **场景**: 当需要使用该库中大量不同的功能，或者为了避免命名冲突时。

---

## 3. 层级结构图解

假设我们有如下文件结构：

```text
project/
│
├── main.py          <-- 我们在这里写代码
├── function.py      <-- 自定义模块
│   ├── def merge_all()
│   └── def save_excel()
│
└── sklearn/         <-- 第三方包 (Package)
    ├── __init__.py
    └── linear_model/    <-- 子包或子模块
        ├── __init__.py
        └── class LinearRegression  <-- 类
````

### 导入路径演示

1. **导入函数**:
    
    `from function import merge_all`
    
    _(路径: project -> function.py -> merge_all)_
    
2. **导入类**:
    
    `from sklearn.linear_model import LinearRegression`
    
    _(路径: sklearn文件夹 -> linear_model模块 -> LinearRegression类)_
    

---

## 4. 最佳实践 (Best Practices)

> [!WARNING] 避坑指南
> 
> 尽量避免使用 `from module import *`。
> 
> **原因**: 这会将模块内所有变量倒在当前空间，极易覆盖已有变量，且难以排查来源。

- **推荐**: 明确列出导入对象。
    
    Python
    
    ```
    from function import (
        flatten_merged_results, 
        merge_all_results
    )
    ```
    
- **推荐**: 如果模块名太长，使用 `as` 起别名。
    
    Python
    
    ```
    import pandas as pd
    import numpy as np
    ```
    

---

## 5. 关联笔记

- [[Python 命名空间与作用域]]
    
- [[Python **init**.py 的作用]]