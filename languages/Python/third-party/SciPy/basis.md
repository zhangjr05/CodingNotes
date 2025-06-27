# SciPy 是 Python 科学计算的核心库之一，基于 NumPy，提供了数值积分、优化、信号处理、线性代数、统计等大量科学计算功能

---

## 用法简介

1. 数值积分

    ```python
    from scipy import integrate

    # 定积分 f(x) = x^2 从 0 到 1
    result, error = integrate.quad(lambda x, x**2, 0, 1)
    print(result)
    ```

2. 优化（最小化）

    ```python
    from scipy import optimize

    # 求 f(x) = (x-2)^2 最小值
    res = optimize.minimize(lambda x: (x - 2)**2, x0=0)
    print(res.x)
    ```

3. 线性代数

    ```python
    from scipy import linalg
    import numpy as np

    A = np.array([[1, 2], [3, 4]])
    b = np.array([5, 6])
    x = linalg.solve(A, b)
    print(x)  # 解线性方程组
    ```

4. 插值

    ```python
    from scipy import interpolate
    import numpy as np

    x = np.linspace(0, 10, 10)
    y = np.sin(x)
    f = interpolate.interp1d(x, y, kind='cubic')
    print(f(5.5))  # 插值
    ```

5. 统计分布

    ```python
    from scipy import stats

    # 正态分布概率密度
    print(stats.norm.pdf(0))  # 0点的概率密度
    # 随机采样
    samples = stats.norm.rvs(size=5)
    print(samples)
    ```

6. 信号处理（如傅里叶变换）

    ```python
    from scipy import fft
    import numpy as np

    x = np.random.random(10)
    y = fft.fft(x)
    print(y)
    ```
