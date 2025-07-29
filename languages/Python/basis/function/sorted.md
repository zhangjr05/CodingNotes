# sorted

**`sorted` 是 Python 的一个内置函数，用于对任何可迭代对象进行排序，返回一个新的已排序的列表，不会修改原对象。**

---

`sorted(iterable, key=None, reverse=False)`

- `iterable`：要排序的可迭代对象（如列表、元组、字符串、字典等）。
- `key`：排序的关键字函数（可选），用于指定排序规则，如 key=len 按长度排序。
- `reverse`：是否倒序排序，默认为 False，若为 True 则降序排列。

```python
a = {chr(ord('a') + i) : 5 - i for i in range(5)}
a = dict(sorted(a.items(), key=lambda i : i[1], reverse=False))
print(a)
```
