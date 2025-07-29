# 多重背包

**多重背包问题中 每种物品有指定的数量限制**
**有n种物品，第i种物品的价值为`w[i]`，体积为`v[i]`，数量为`s[i]`，背包容量为`V`**
**目标：选择物品放入背包，使总价值最大，且总体积不超过背包容量**

## 算法流程

### 状态定义

**`dp[i][j]` 代表前i种物品装入容量为j的背包获得的最大价值**

### 状态转移方程

**`dp[i][j] = max(dp[i - 1][j - k * v[i]] + k * w[i])`其中 0 ≤ k ≤ s[i] 且 k * v[i] ≤ j**

### 一维空间优化

```python
for i in range(n):
    for j in range(V, v[i] - 1, -1):    # 倒序遍历
        for k in range(1, min(s[i] + 1, j // v[i] + 1)):
            dp[j] = max(dp[j], dp[j - k * v[i]] + k * w[i])
```

### 二进制优化

**每种物品的s[i]个拆分成若干"二进制组" 转化为0-1背包问题**

```python
# 二进制拆分
nv, nw = [], []
for i in range(n):
    k = 1
    remaining = s[i]
    while k <= remaining:
        nv.append(v[i] * k)
        nw.append(w[i] * k)
        remaining -= k
        k << 1
    if remaining > 0:
    nv.append(v[i] * remaining)
    nw.append(w[i] * remaining)

# 转化为 0-1 背包求解
```

### 单调队列优化
