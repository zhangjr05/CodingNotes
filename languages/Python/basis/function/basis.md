# What is function?

---

## 函数的定义

```python
def f(a:int, b:float) -> str:
    '''这是什么函数'''
    print(type(a), type(b))
    return '类型注解'

from typing import Union
def greeting(name: Union[str, int]) -> str:
    return 'Hello, ' + name
```

---

## lambda函数实例

```python
f = lambda a : a * a

numbers = list(range(1, 11))
squared_numbers = list(map(lambda a : a * a, numbers))
print(squared_numbers)

even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers)
```

---

## 可变参数

```python
def f(*args, **kwargs):
    print(type(args))   # 元组，位置参数
    print(type(kwargs)) # 字典，关键字参数
```

- **\*args 用于接收任意数量的位置参数，并将它们存储在一个元组中。**
- **\*kwargs 用于接收任意数量的关键字参数，并将它们存储在一个字典中。**

```python
def f(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

f(a=1, b=2, c=3)
```
