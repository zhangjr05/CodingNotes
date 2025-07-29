# set 集合

---

## basis

- `s = set()`: **{}表示空字典，所以只能用set()创建空集**
- `s.add(object=1)`: **添加元素**
- `s.update(others=?)`: **参数可以是list, tuple, set, dict(key值)**
- `s.remove(object=1)`: **if the element is not a member, raise a KeyError.**
- `s.discard(object=1)`: **does not raise an exception when an element is missing from the set.**
- `s.pop()`: **无参数，随机删除并返回（一般按顺序）**
- `s.clear()`: **清空**
- `set1.difference(set2)`: **返回差集set1-set2**
- `set1.difference_update(set2)`: **set1 = set1 - set2, but set2 still equals to itself**
- `set1.intersection(set2)`: **返回交集**
- `set1.intersection_update(set2)`: **set1 = 交集**
- `set1.union(set2)`: **返回并集**
- `set1.symmetric_difference(set2)`: **返回两个集合中不重复元素的集合**
- `set1.symmetric_difference_update(set2)`: **同上，并更新**
- `set1.isdisjoint(set2)`: **交集为空则返回True**
- `set1.issubset(set2)`: **set1是set2的子集则返回True**

---

## frozenset

**frozenset**是 Python 中的一种**不可变集合**数据类型。

- **不可变**
- **可哈希**
- **支持集合运算**

```python
s = {1, 2, 3}
s.add(4)
fs = frozenset(s)
# fs.add(5)  AttributeError: 'frozenset' object has no attribute 'add'
```
