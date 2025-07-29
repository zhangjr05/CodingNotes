# functools

---

## lru_cache

缓存装饰器

```python
from functools import lru_cache

@lru_cache  # LRU算法装饰器 
def f(x, y):
    return x * y

for i in range(10):
    for j in range(10):
        f(i, j)

print(f(5, 5))
```
