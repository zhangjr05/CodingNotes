# random

---

## 常用方法

- `random.seed(42)`  # 设置随机种子
- `random.random()`  # 生成[0, 1)随机浮点数
- `random.uniform(a, b)`  # 生成[a, b]范围内随机浮点数
- `random.randint(a, b)`  # 生成[a, b]范围内随机整数（包含端点）
- `random.choice(seq)`  # 返回序列中随机一个元素
- `random.choices(seq, k=n)`  # 有重复地随机选择n个元素
- `random.sample(seq, k=n)`  # 无重复地随机选择n个元素
- `random.shuffle(seq)`  # 就地随机打乱序列
