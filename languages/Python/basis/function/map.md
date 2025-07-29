# map

**`map` 将函数应用到可迭代对象的每个元素上，返回一个迭代器。**

---

```python
numbers = [1, 2, 3, 4, 5]

# 使用 lambda 函数计算每个数字的平方
squares = map(lambda x: x**2, numbers)
print(list(squares))  # 输出: [1, 4, 9, 16, 25]

# 使用内置函数
strings = ["hello", "world"]
uppercased = map(str.upper, strings)
print(list(uppercased))  # 输出: ['HELLO', 'WORLD']


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(sums)  # 输出: [5, 7, 9]
```
