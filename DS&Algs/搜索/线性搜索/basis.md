# 线性搜索

**线性搜索是最基础的搜索算法之一。它通过按顺序检查数组中的每个元素，直到找到目标元素或者搜索完整个数组。从数组第一个元素开始，依次检查每个元素。如果当前元素与目标元素匹配，则搜索成功，返回元素索引；如果遍历完整个数组仍未找到目标元素，则搜索失败，通常返回-1或其他特殊值。**

## 带哨兵的线性搜索（优化版本）

**通过在数组末尾添加"哨兵"(目标值的副本)来消除循环中的边界检查，提高效率。**

```python
def sentinel_linear_search(arr, target):
    """带哨兵的线性搜索"""
    n = len(arr)
    temp_arr = arr.copy()
    temp_arr.append(target)
    i = 0
    # 无需检查边界条件
    while temp_arr[i] != target:
        i += 1
    if i < n:
        return i
    else:
        return -1  # 未找到目标
```
