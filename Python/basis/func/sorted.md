# sorted

```python
a = [3, 2, 1]
sorted(a, key=None, reverse=False)

# 通过key参数可以自定义排序规则，sorted会将每个元素传入key函数计算结果作为排序依据

a = {chr(ord('a') + i) : 5 - i for i in range(5)}
a = dict(sorted(a.items(), key=lambda i : i[1], reverse=False))
print(a)
```
