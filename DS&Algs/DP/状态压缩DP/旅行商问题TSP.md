# 旅行商问题 TSP

**旅行商问题(Traveling Salesman Problem, TSP)是一个经典的组合优化问题 也是计算机科学中的一个NP困难问题。**
**一个旅行商需要访问n个城市，每个城市恰好访问一次，然后返回出发城市，求能够使总行程距离最短的路径。**

- **input:**
  - **n个城市**
  - **城市间的距离矩阵 `dist[i][j]` 表示从城市`i`到城市`j`的距离**
- **output:**
  - **访问所有城市恰好一次并返回起点的最短路径**
  - **最短路径的总长度**

## 算法流程

### 状态定义

**`dp[state][i]` 表示已经访问了状态`state`表示的城市集合，且当前位于城市`i`的最短路径长度。**
**其中`state`是一个二进制数，第`j`位为 1 表示城市`j`已被访问。**

### 状态转移方程

**`dp[state][i] = min(dp[state - {i}][j] + dist[j][i])`**
**其中`j`是`state`中已访问的城市，且 j != i，`state - {i}` 表示从`state`中去掉城市`i`后的状态。**

### Python 实现

```python
def tsp(dist):
    n = len(dist)
    # dp[state][i]: 已访问城市集合为state，当前在城市i的最短路径长度
    dp = [[float('inf')] * n for _ in range(1 << n)]

    # 初始状态 起点为城市0
    dp[1][0] = 0

    # 枚举所有可能状态
    for state in range(1, 1 << n):
        # 如果城市0未被访问，跳过
        if not (state & 1):
            continue
        
        # 枚举当前所在城市
        for i in range(n):
            # 如果城市i不在当前状态中，跳过
            if not (state & (1 << i)):
                continue

            # 上一个状态(去掉城市i)
            prev_state = state & ~(1 << i)

            # 如果上一个状态只有城市0，且当前不在城市0，跳过
            if prev_state == 0 and i != 0:
                continue
            
            # 枚举前一个访问的城市j
            for j in range(n):
                if j == i or not (prev_state & (1 << j)):
                    continue
                
                # 状态转移
                dp[state][i] = min(dp[state][i], dp[prev_state][j] + dist[j][i])
    
    # 最终结果：所有城市都访问过，且当前在城市i，还需要返回城市0的最短路径
    final_state = (1 << n) - 1  # 所有城市都访问过的状态
    result = float('inf')
    for i in range(1, n):  # 从1开始，因为我们需要回到0
        if dp[final_state][i] != float('inf'):
            result = min(result, dp[final_state][i] + dist[i][0])
    
    return result
```
