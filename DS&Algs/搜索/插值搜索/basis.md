# 插值搜索

## 算法思想

**插值搜索是对二分搜索的改进，特别适合于数据分布相对均匀的有序数组。它的核心思想是根据要查找的关键字与搜索区域端点值的位置关系来确定下一步的搜索位置，而不是像二分搜索那样总是选择中点。**

- **根据要查找的值在已知范围内的大概位置进行猜测**
- **通过线性插值公式估计目标值的位置**
- **缩小搜索范围，重复以上步骤**
- **关键插值公式:** `pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])`

### example

```python

def interpolation_search(arr, target):
    '''在有序数组中查找'''
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            return -1
        
        # 使用插值公式计算探测点  这是插值搜索与二分搜索的关键区别
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1  # 未找到目标
```
