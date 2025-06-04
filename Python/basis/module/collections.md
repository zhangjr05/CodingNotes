# collections

---

## Counter

统计可哈希对象出现的次数
两个Counter对象可进行比较

```python
from collections import Counter

c = Counter('abcdabcdabcd')
c = Counter(1, 2, 2, 2, 3, 4, 5, 5)
c = Counter({'red': 2, 'blue': 3})  # Counter({'blue': 3, 'red': 2})
c = Counter(a=1, b=2)  # Counter({'b': 2, 'a': 1})

c['a'] # 直接访问
del c['a'] # 删除

# 返回排序后列表
c.most_common(3) # 获取出现次数最多的n个元素
c.most_common()  # 获取所有元素，按出现次数降序排列

c.items()  # dict_items([('red', 2), ('blue', 3)]) 返回元素与其出现次数
c.values()  # dict_values([2, 3]) 返回出现次数

```

---

## deque 双端队列

```python
d = deque(maxlen=3) # 限制队列长度
d = deque([1, 2, 3])
d.extend()
d.extendleft()
d.append()
d.appendleft()
d.pop()
d.popleft()
```

---

## defaultdict

defaultdict是Python标准库中的字典类型，当访问不存在的键时会自动创建默认值。

```python
from collections import defaultdict

# 基本语法：需要传入工厂函数
d = defaultdict(int)        # 默认值为0
d = defaultdict(list)       # 默认值为[]
d = defaultdict(str)        # 默认值为''
d = defaultdict(set)        # 默认值为set()
```
