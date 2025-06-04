# list 列表

## basis

- `a = list(range(5))`: **创建列表**
- `a.count(value=1)`: **计算value=1的元素出现次数**
- `a.index(value=1)`: **返回第一个value=1的元素下标，不存在会报错**
- `a.insert(index=2, value=99)`: **指定位置插入新元素**
- `a.append(value=99)`: **末尾添加新元素**
- `a.extend(list=[5, 6])`: **合并列表**
- `del a[index1=0 : index2=10 : step=2]`: **除去指定index元素，也可以是切片**
- `a.pop(index=-1)`: **除去指定index元素并返回value，默认index=-1**
- `a.remove(value=1)`: **除去指定value的第一个匹配项**
- `a.reverse()`: **反转，返回None**
- `a.sort()`: **升序，返回None**
- `a.sort(reverse=True)`: **降序，返回None**
- `a.clear()`: **清空列表**
- `a.copy()`: **浅拷贝**

## 情景

- **列表解析**

```python
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix_T = [[row[i] for row in matrix]for i in range(4)]    # 转置
```

- **zip函数用于将多个可迭代对象（如列表、元组等）中的元素打包成一个个元组，然后返回由这些元组组成的对象。**

```python
list(zip(*matrix))  # 转置，但为元组
matrix_T = [list(row) for row in zip(*matrix)]
```
