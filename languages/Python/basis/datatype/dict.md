# dict 字典

## basis

```markdown
d = dict()  # 空字典
key = 'e'   # key值只能是不可变对象
```

## 操作

- `d.clear()`: **清空字典**
- `d[key] = value`: **添加或修改**
- `d.pop(key)`: **删除指定key返回value**
- `del d[key]`: **仅删除**
- `d.get(key, default='get lost')`: **若key存在，返回对应value，否则返回default内容**
- `d.items()`: **返回一个类似于这样的结构：dict_items([(key1, value1), (key2, value2), ...])，d.items()可用于for循环迭代**
- `d.keys()`: **返回keys**
- `d.values()`: **返回values**

## 情景

- **合并字典**

```python
d1 = {chr(i + ord('a')) : i + 1 for i in range(3)}
d2 = {chr(i + ord('a')) : i + 1 for i in range(3, 5, 1)}
{**d1, **d2}    # 返回d1, d2的合并  如key-value有冲突，以d2为准
d1.update(d2)   # 更新d1
```

- **键值反转**

```python
{value:key for key, value in d.items()}
dict(zip(d.values(), d.keys()))
```

- **配对**

```python
students = ['Zhang San', 'Li Si', 'Wang Wu', 'Zhao Liu']
scores = [90, 85, 61, 70]
zip:    dict(zip(students, scores))
字典解析:   {students[i] : scores[i] for i in range(len(scores))}
```
