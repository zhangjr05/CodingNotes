# itertools

---

## combinations

**从 n 个元素中选择 r 个元素，不考虑顺序，生成组合。**

```python
from itertools import combinations
data = [1, 2, 3, 4]
result = list(combinations(data, 2))
print(result)  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

---
