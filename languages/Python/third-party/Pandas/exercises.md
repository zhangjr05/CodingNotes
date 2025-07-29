# Pandas 实战演练

---

## 学生成绩分析

```csv
student_id,name,gender,math,english,physics,chemistry,biology,history,geography,class
1001,张三,M,85,78,92,88,80,75,90,1
1002,李四,F,90,88,85,95,92,80,85,1
1003,王五,M,76,80,79,85,78,88,82,2
1004,赵六,F,92,91,94,90,89,92,95,2
1005,孙七,M,68,75,70,72,65,70,75,1
1006,周八,F,88,84,90,86,90,85,88,2
1007,钱九,M,95,89,96,94,93,90,91,1
1008,吴十,F,80,77,82,79,81,83,80,2
```

```python
import pandas as pd

df = pd.read_csv('scores.csv')
```

**1. 找出每个班级所有科目总分排名前两名的学生姓名、总分和班级。**

```python
score_cols = ['math', 'english', 'physics', 'chemistry', 'biology', 'history', 'geography']
df['total'] = df[score_cols].sum(axis=1)
top2 = df.sort_values(['class', 'total'], ascending=[True, False]).groupby('class').head(2)[['name', 'total', 'class']]
print(top2)
```

**2. 计算每个班级每门科目的平均分，输出为新 DataFrame（行是班级，列是科目）。**

```python
class_subject_mean = df.groupby('class')[score_cols].mean()
print(class_subject_mean)
```

**3. 找出所有科目成绩均高于本班级平均分的学生姓名和班级。**

```python
class_mean = df.groupby('class')[score_cols].transform('mean')  # 计算每个班级各科平均分
mask = (df[score_cols] > class_mean).all(axis=1)
top_students = df.loc[mask, ['name', 'class']]
print(top_students)
```

---

## 股票数据分析

```csv
date,open,close,high,low,volume
2025-05-01,15.20,15.50,15.60,15.10,1200000
2025-05-02,15.55,15.80,15.90,15.50,1350000
2025-05-05,15.85,16.10,16.20,15.80,1400000
2025-05-06,16.15,16.00,16.30,15.95,1250000
2025-05-07,16.05,16.20,16.25,16.00,1300000
2025-05-08,16.25,16.40,16.50,16.20,1450000
2025-05-09,16.45,16.30,16.55,16.25,1500000
2025-05-12,16.35,16.10,16.70,16.30,1550000
2025-05-13,16.65,16.00,16.90,16.60,1600000
2025-05-14,16.85,15.90,16.95,16.65,1580000
2025-05-15,16.75,15.80,17.00,16.70,1620000
2025-05-16,16.95,15.70,17.20,16.90,1700000
2025-05-19,17.15,15.60,17.25,17.00,1680000
2025-05-20,17.05,15.50,17.40,17.00,1750000
2025-05-21,17.35,16.00,17.60,17.30,1800000
2025-05-22,17.55,16.50,17.65,17.35,1780000
2025-05-23,17.45,17.00,17.70,17.40,1850000
2025-05-26,17.65,17.50,17.90,17.60,1900000
2025-05-27,17.85,18.00,17.95,17.65,1880000
2025-05-28,17.75,18.50,18.00,17.70,1920000
2025-05-29,17.95,19.00,18.20,17.90,1950000
2025-05-30,18.15,19.50,18.40,18.10,2000000
```

```python
import pandas as pd

df = pd.read_csv('stock_2025_05.csv', parse_dates=['date'])  # 读取数据并转换日期
df.set_index('date', inplace=True)
```

**1. 计算2025年5月每周的平均收盘价，并找出收盘价最高的一周是哪一周。**

```python
weekly_mean = df['close'].resample('W').mean()  # 按周重采样，计算每周平均收盘价
print(f'收盘价最高的一周是：{weekly_mean.idxmax()}，平均收盘价为：{weekly_mean.max()}')  # 标签是每周的周日
```

**2. 计算每个交易日的5日和10日移动平均收盘价，并找出所有“金叉”点（即5日均线从下向上穿过10日均线的日期）。**

```python
# 计算每个交易日的5日和10日移动平均收盘价
df['ma5'] = df['close'].rolling(window=5).mean()
df['ma10'] = df['close'].rolling(window=10).mean()

# 找出“金叉”点
golden_cross = (df['ma5'].shift(1) < df['ma10'].shift(1)) & (df['ma5'] >= df['ma10'])
golden_cross_days = df.index[golden_cross]
print("金叉发生在以下日期：")
print(golden_cross_days)
```

**3. 假设你每次在每周的第一个交易日买入100股，并在该周最后一个交易日卖出，计算5月份的总收益率。**

```python
# 按周分组，取每周第一个和最后一个交易日
weekly = df['close'].resample('W')
buy_prices = weekly.first()
sell_prices = weekly.last()
weekly_profit = (sell_prices - buy_prices) * 100

total_invest = (buy_prices * 100).sum()
total_profit = weekly_profit.sum()

total_return = total_profit / total_invest
print(f"5月总收益率为：{total_return:.2%}")
```
