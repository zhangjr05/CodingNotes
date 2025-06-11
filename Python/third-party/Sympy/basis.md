# Sympy

**Sympy 是 Python 的一个符号计算库，可以进行代数、微积分、方程求解等符号运算。**

---

## 用法简介

1. 基本符号定义

    ```python
    import sympy as sp
    from sympy import symbols
    x, y = symbols('x, y')
    ```

2. 表达式构建与化简

    ```python
    from sympy import simplify
    expr = (x**2 + x + 1 + x)
    simplified = simplify(expr)
    print(simplified)
    ```

3. 求导

    ```python
    from sympy import diff
    derivative = diff(x**3 + x, x)
    print(derivative)
    ```

4. 积分

    ```python
    from sympy import integrate
    integral = integrate(x**2, x)
    print(integral)
    ```

5. 方程求解

    ```python
    from sympy import Eq, solve
    eq = Eq(x**2 - 4, 0)
    solutions = solve(eq, x)
    print(solutions)
    ```

6. 代入数值

    ```python
    value = expr.subs(x, 2)
    print(value)
    ```

7. 泰勒展开

    ```python
    from sympy import series
    taylor = series(sympy.sin(x), x, 0, 5)
    ```
