# reduce

**reduce()通过将一个二元函数作用于序列的元素，迭代地累积成单一结果。**

```python
from functools import reduce

nums = []

the_sum = reduce(lambda x, y: x + y, nums, 0) # 0 为 initial value

print(the_sum)
```
