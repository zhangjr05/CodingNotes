# filter

**根据函数的返回值过滤可迭代对象中的元素，返回一个迭代器，只包含返回True的元素。**

---

```python
numbers = [1, 2, 3, 4, 5, 6]

# 过滤出偶数
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # 输出: [2, 4, 6]
```
