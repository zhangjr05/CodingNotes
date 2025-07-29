# 二分搜索

## 二分查找

```python
def binary_search(nums: list[int], key: int) -> int:
    """在升序列表中查找值为key的元素并返回其下标

    Args:
        nums (list[int]): 目标升序列表
        key (int): 目标值

    Returns:
        找到则返回其下标 未找到则返回-1
    """
    i, j = 0, len(nums)
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < key:
            i = mid + 1
        elif nums[mid] > key:
            j = mid - 1
        else:
            return mid
    return -1
```
