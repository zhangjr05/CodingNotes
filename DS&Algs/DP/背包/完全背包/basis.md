# 完全背包

**完全背包问题中，每种物品有无限多个，可重复选取。**

## 算法流程

### 状态定义

**`dp[i][v]` 代表用前i种物品填充体积为v的背包得到的最大价值**

### 状态转移方程

`dp[i][v] = max(dp[i - 1], dp[i - 1][j - k * c[i]] + k * w[i])`

### 空间优化

```python
for i in range(n):
    for j in range(c[i], V + 1):  # 此时需顺序枚举
        dp[j] = max(dp[j], dp[j - c[i]] + w[i])
```
