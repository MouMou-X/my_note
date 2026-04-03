---
source:
  - https://www.zhihu.com/people/dong-hao-92-56/search?keyword=%E8%A3%85%E9%A5%B0%E5%99%A8&pathBefore=%2Fpeople%2Fdong-hao-92-56
---


**闭包（closure）**——内部函数会把它用到的外部变量"打包"随身携带。
`inner` 函数里用到了 `name`，但 `name` 并不是 `inner` 自己的参数。


```python
def decorator_func(func):
    def inner(*args):       #定义内部函数inner，让它去承接多余的参数。
        print("正在计算")
        result = func(*args)
        print("计算的结果是",result)
        return result
    return inner

#业务函数部分不变。
@decorator_func
def add_func(*args):
    return sum(args)
@decorator_func
def mul_func(*args):
    result = 1
    for i in args:
        result*=i
    return result

#使用方式
add_func(1,5,6,9)
mul_func(1,5,6,9)

```