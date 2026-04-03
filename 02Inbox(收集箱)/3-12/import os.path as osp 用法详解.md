---
tags:
  - 编程/Python
type: note
status: 🌱
created: 2026-03-12
---
# `import os.path as osp` 用法详解

## 一、是什么？

`os.path` 是 Python 标准库中用于**处理文件路径**的模块。  
`as osp` 是给它起的短别名，社区约定俗成的写法，在 OpenMMLab 等项目中极为常见。

```python
import os.path as osp

osp.exists(path)   # 等价于 os.path.exists(path)
```

---

## 二、路径判断类

```python
# 判断路径是否存在（文件或文件夹）
osp.exists('/home/user/file.txt')      # True / False

# 判断是否是文件
osp.isfile('/home/user/file.txt')      # True

# 判断是否是文件夹
osp.isdir('/home/user/my_folder')      # True

# 判断是否是绝对路径
osp.isabs('/home/user/file.txt')       # True
osp.isabs('relative/path')            # False
```

---

## 三、路径拼接类

```python
# 拼接路径（自动处理斜杠，跨平台）
osp.join('/home/user', 'project', 'data.txt')
# → '/home/user/project/data.txt'
```

> ⚠️ **不要用字符串拼接路径**，在 Windows/Linux 下斜杠方向不同，有跨平台问题：
> 
> ```python
> '/home/user' + '/' + 'data.txt'    # ❌ 不推荐
> osp.join('/home/user', 'data.txt') # ✅ 推荐
> ```

---

## 四、路径拆分类

```python
path = '/home/user/project/data.txt'

# 拆分为 (目录, 文件名)
osp.split(path)
# → ('/home/user/project', 'data.txt')

# 只取目录部分
osp.dirname(path)
# → '/home/user/project'

# 只取文件名部分
osp.basename(path)
# → 'data.txt'

# 拆分文件名和扩展名
osp.splitext('data.txt')
# → ('data', '.txt')

osp.splitext(path)
# → ('/home/user/project/data', '.txt')
```

---

## 五、路径转换类

```python
# 相对路径 → 绝对路径
osp.abspath('relative/path')
# → '/current/working/dir/relative/path'

# 获取真实路径（解析软链接）
osp.realpath('/some/symlink')

# 展开 ~ 为用户主目录
osp.expanduser('~/project/data.txt')
# → '/home/user/project/data.txt'
```

---

## 六、文件信息类

```python
# 获取文件大小（字节）
osp.getsize('/home/user/data.txt')
# → 2048

# 获取最后修改时间（时间戳）
osp.getmtime('/home/user/data.txt')
# → 1710000000.0

# 获取最后访问时间
osp.getatime('/home/user/data.txt')
```

---

## 七、实际项目常见组合用法

```python
import os.path as osp

# ✅ 场景1：构建输出路径
base_dir = '/home/user/project'
output_path = osp.join(base_dir, 'results', 'output.json')

# ✅ 场景2：检查文件存在再加载
if osp.exists(cache_path) and osp.isfile(cache_path):
    data = load(cache_path)

# ✅ 场景3：提取文件名（不含扩展名）
filename = osp.splitext(osp.basename('/data/model.pth'))[0]
# → 'model'

# ✅ 场景4：基于当前脚本构建路径（常见于配置文件）
current_dir = osp.dirname(osp.abspath(__file__))
config_path = osp.join(current_dir, 'config.yaml')
```

---

## 八、速查表

|方法|作用|
|---|---|
|`osp.exists()`|路径是否存在|
|`osp.isfile()`|是否是文件|
|`osp.isdir()`|是否是文件夹|
|`osp.isabs()`|是否是绝对路径|
|`osp.join()`|拼接路径|
|`osp.split()`|拆分为目录+文件名|
|`osp.dirname()`|取目录部分|
|`osp.basename()`|取文件名部分|
|`osp.splitext()`|分离扩展名|
|`osp.abspath()`|转为绝对路径|
|`osp.realpath()`|解析软链接真实路径|
|`osp.expanduser()`|展开 `~` 符号|
|`osp.getsize()`|获取文件大小（字节）|
|`osp.getmtime()`|获取最后修改时间|
|`osp.getatime()`|获取最后访问时间|