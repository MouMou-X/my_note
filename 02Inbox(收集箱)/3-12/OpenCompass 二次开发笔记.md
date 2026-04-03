# OpenCompass 二次开发笔记

## 1. 开发方式选择

### ❌ 不推荐：直接修改源码

|问题|说明|
|---|---|
|升级困难|每次 opencompass 更新都会覆盖或产生冲突|
|维护成本高|难以区分自定义代码与原始代码|
|协作麻烦|团队成员难以同步改动|
|测试隔离差|无法单独测试扩展逻辑|

### ✅ 推荐：新建独立扩展包

opencompass 基于 `mmengine` 的 Registry 机制，天然支持外部扩展，无需修改源码即可注册新组件。

---

## 2. 扩展包项目结构

```
my_opencompass_ext/
├── pyproject.toml
├── README.md
├── my_ext/
│   ├── __init__.py          # 在这里触发注册
│   ├── evaluators/
│   │   ├── __init__.py
│   │   └── my_evaluator.py  # 新评估器
│   ├── datasets/
│   │   ├── __init__.py
│   │   └── my_dataset.py    # 新数据集
│   ├── augmentation/
│   │   ├── __init__.py
│   │   └── exporter.py      # 数据增强导出工具
│   └── configs/
│       └── my_eval.py       # 评估配置
└── tests/
```

---

## 3. 核心扩展方式

### 注册新评估器

```python
# my_ext/evaluators/my_evaluator.py
from opencompass.registry import ICL_EVALUATORS
from opencompass.openicl.icl_evaluator import BaseEvaluator

@ICL_EVALUATORS.register_module()
class MyCustomEvaluator(BaseEvaluator):
    def score(self, predictions, references):
        # 你的评估逻辑
        ...
        return {"my_score": score}
```

### 触发注册

```python
# my_ext/__init__.py
from .evaluators import my_evaluator
from .datasets import my_dataset
```

### 在配置文件中使用

```python
# configs/my_eval.py（opencompass 的配置文件）
import my_ext  # 触发注册

datasets = [dict(type='MyCustomDataset', ...)]
eval = dict(evaluator=dict(type='MyCustomEvaluator', ...))
```

### 数据增强导出工具

```python
# my_ext/augmentation/exporter.py
class DataAugmentationExporter:
    """独立工具，不依赖 opencompass 注册机制"""
    def augment(self, dataset): ...
    def export(self, output_path): ...
```

---

## 4. 修改已安装包的三种方式

### 方式一：可编辑安装（最推荐）

```bash
git clone https://github.com/open-compass/opencompass.git
cd opencompass
pip install -e .   # 修改源码后立即生效，无需重新安装
```

### 方式二：直接修改安装路径下的文件

```bash
# 查找包的安装路径
pip show opencompass

# 或在 Python 里查找
python -c "import opencompass; print(opencompass.__file__)"
```

> ⚠️ `pip install --upgrade` 会覆盖改动，不推荐长期使用。

### 方式三：Monkey Patching（不改源文件）

```python
import opencompass.some_module as m

def my_fixed_function(self, ...):
    ...  # 新逻辑

m.SomeClass.some_method = my_fixed_function  # 运行时替换
```

### 选择建议

|场景|推荐方式|
|---|---|
|长期开发 / 深度修改|`git clone` + `pip install -e .`|
|临时修复一个 bug|直接找到安装路径改文件|
|不想动源码|Monkey Patching|

---

## 5. `pip install -e .` 原理

### 普通安装 vs 可编辑安装

**普通 `pip install .`**：将源码**复制**到 site-packages

```
源码目录/   →  复制  →  site-packages/
  my_ext/                 my_ext/           ← 拷贝
  pyproject.toml          my_ext.dist-info/
```

> 修改源码目录的文件**不会生效**，Python 读的是 site-packages 里的拷贝。

**`pip install -e .`**：在 site-packages 里放一个**路径指针**

```
源码目录/   →  指针  →  site-packages/
  my_ext/                 __editable__.my_ext.pth  ← 一行路径
  pyproject.toml          my_ext.dist-info/
```

`.pth` 文件内容：

```
/你的项目/源码目录
```

Python 启动时读取所有 `.pth` 文件，将路径加入 `sys.path`，`import my_ext` 时直接读源码目录。

### 执行流程

```
pip install -e . 执行流程：

1. 读取 pyproject.toml / setup.py
   └─ 获取包名、依赖、入口点等元信息

2. 安装依赖
   └─ 把 install_requires 里的依赖正常安装到 site-packages

3. 在 site-packages 放一个 .pth 文件
   └─ 内容就是你源码目录的绝对路径

4. 注册元信息（dist-info）
   └─ 让 pip list / pip show 能认出这个包
```

### 验证方法

```bash
# 查看 .pth 文件内容
cat $(python -c "import site; print(site.getsitepackages()[0])")/__editable__.my_ext.pth
# 输出：/home/yourname/projects/my_ext

# 验证 sys.path 里有你的目录
python -c "import sys; [print(p) for p in sys.path if 'my_ext' in p]"
```

### 对比总结

||普通安装|`-e` 可编辑安装|
|---|---|---|
|site-packages 里放什么|完整代码拷贝|路径指针 `.pth`|
|改源码后是否生效|❌ 需重新安装|✅ 立即生效|
|`pip show` 能识别|✅|✅|
|适合场景|生产部署|开发调试|

> **本质**：`-e` 让 Python 的模块搜索路径直接指向源码目录，中间没有任何拷贝动作。

---

## 6. 推荐的最佳实践组合

1. `git clone` opencompass 源码，`pip install -e .` 安装
2. 新建自己的扩展包，同样用 `pip install -e .` 安装
3. opencompass 的 bug 修复直接在克隆的源码里改
4. 自己的新功能（评估器、数据增强工具等）放在扩展包里