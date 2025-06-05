# Numba

Numba是一个开源的**即时编译器(JIT)**，可以将Python函数编译成优化的机器码，实现接近C语言的执行速度。

---

## 基础用法

```python
from numba import jit

# 添加@jit装饰器加速
@jit(nopython=True)
def square_sum(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

square_sum(100)  # 首次调用，进行预热编译

n = 10000000
result = square_sum(n)
print(result)
```

## 编译模式

1. **object模式（默认）**

    ```python
    @jit  # 默认模式，兼容性好但速度一般
    def mixed_function(x):
        return x + [1, 2, 3]  # 可以使用Python对象
    ```

2. **nopython模式（推荐）**

    ```python
    @jit(nopython=True)  # 或简写为 @njit
    def pure_numeric(x):
        return x * x + 1  # 只能数值计算，但最快
    ```

3. **缓存编译结果**

    ```python
    @jit(nopython=True, cache=True)
    def cached_function(x):
        return x ** 2  # 缓存编译结果，重启程序也不用重新编译
    ```
