# **Pandas** 是 Python 的一个强大**数据分析与处理库**，主要用于**结构化数据**（如表格、时间序列）的处理和分析

---

## Series

- **Series创建**

    ```python
    import pandas as pd

    s = pd.Series([1, 2, 3, 4])  # 从列表/数组创建
    s = pd.Series({'a': 1, 'b': 2, 'c': 3})  # 从字典创建
    s = pd.Series([1, 2, 3], index=['x', 'y', 'z'])  # 指定索引
    s = pd.Series([1, 2, 3], dtype=float, name='score')  # 指定数据类型和名称
    ```

- **Series基本属性**

    ```markdown
    s.index：获取 Series 的索引
    s.values：获取 Series 的数据部分（返回NumPy数组）
    s.dtype：返回 Series 中数据的类型
    s.shape：返回 Series 的形状（行数）
    s.name：返回 Series 的名称
    ```

- **Series索引切片**

    ```markdown
    s[0]  # 按位置
    s['a']  # 按标签
    s.iloc[1]  # 按位置
    s.loc['a']  # 按标签
    s[s > 2]  # 条件筛选
    ```

- **Series基本方法**

    ```markdown
    s.head()  # 返回 Series 的前 n 行（默认为5）
    s.tail()  # 返回 Series 的后 n 行（默认为5）

    s.isnull()  # 返回一个布尔 Series，表示每个元素是否为 NaN
    s.notnull()  # 返回一个布尔 Series，表示每个元素是否不是 NaN

    s.astype(dtype)  # 将 Series 转换为指定的类型
    s.describe()  # 返回 Series 的统计描述（如均值、标准差、最小值等）

    s.unique()  # 返回 Series 中的唯一值（去重）
    s.value_counts()  # 返回 Series 中每个值的出现次数

    s.map(func)  # 将指定函数应用于 Series 中的每个元素
    s.apply(func)  # 将指定函数应用于 Series 中的每个元素，常用于自定义操作

    s.sort_values()  # 对 Series 中的元素进行排序（按值排序）
    s.sort_index()  # 对 Series 的索引进行排序

    s.dropna()  # 删除 Series 中的缺失值（NaN）
    s.fillna()  # 填充 Series 中的缺失值（NaN）
    s.replace(to_replace, value)  # 替换 Series 中指定的值

    s.cumsum()  # 返回 Series 的累计求和
    s.cumprod()  # 返回 Series 的累计乘积

    s.shift(periods=1)  # 将 Series 中的元素按指定的步数进行位移，产生的空位会自动用 NaN 填充。
    s.rank()  # 根据数值的大小为每个元素分配一个排名，默认是从小到大排，数值最小的排名为1。排名相同时会采用平均排名。

    s.to_list()  # 将 Series 转换为 Python 列表
    s.to_frame()  # 将 Series 转换为 DataFrame
    ```

---

## DataFrame

- **DataFrame构建**

    `pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)`

    ```python
    data = [['张三', 18], ['李四', 19], ['王五', 20]]
    df = pd.DataFrame(data, columns=['name', 'age'], index=['帅哥1', '帅哥2', '帅哥3'])

    data = {'name': ['张三', '李四', '王五'], 'age': [18, 19, 20]}
    df = pd.DataFrame(data)
    ```

- **DataFrame基本属性**

    ```markdown
    df.shape  # 返回 DataFrame 的行数和列数（行数，列数）
    df.columns  # 返回 DataFrame 的所有列名
    df.index  # 返回 DataFrame 的行索引
    df.dtypes  # 返回每一列的数值数据类型

- **DataFrame索引切片**

    ```markdown
    df[['name', 'age']]  # 选择列
    df.loc['帅哥2']  # 按标签选择行
    df.iloc[[0, 2]]  # 按位置选择行
    df.at['帅哥1', 'name']  # 访问 DataFrame 中单个元素
    df.iat[0, 0]
    df[df['age'] > 18]  # 布尔索引
    ```

- **DataFrame基本方法**

    ```markdown
    df.head(n)  # 返回 DataFrame 的前 n 行数据（默认前 5 行）
    df.tail(n)  # 返回 DataFrame 的后 n 行数据（默认后 5 行）

    df.info()  # 显示 DataFrame 的简要信息，包括列名、数据类型、非空值数量等
    df.describe()  # 返回 DataFrame 数值列的统计信息，如均值、标准差、最小值等

    df.sort_values(by='age')  # 按照指定列排序
    df.sort_index()  # 按行索引排序
    df.transpose()  # 转置 DataFrame（行列交换）

    df.set_index()  # 设置 DataFrame 的索引
    df.reset_index()  # 重置 DataFrame 的索引

    df.dropna()  # 删除含有缺失值（NaN）的行或列
    df.fillna(value)  # 用指定的值填充缺失值

    df.pivot(index, columns, values)  # 将长表变为宽表，指定行、列和值
    df.melt()  # 将宽表变成长表，适合做反透视

    df.query()  # 使用 SQL 风格的语法查询 DataFrame
    df.pivot_table()  # 创建透视表

    df.isnull()  # 判断缺失值，返回一个布尔值 DataFrame
    df.notnull()  # 判断非缺失值，返回一个布尔值 DataFrame

    df.to_csv()  # 将 DataFrame 导出为 CSV 文件
    df.to_json()  # 将 DataFrame 导出为 JSON 格式
    df.to_excel()  # 将 DataFrame 导出为 Excel 文件
    df.to_sql()  # 将 DataFrame 导出为 SQL 数据库
    ```

- **DataFrame常用方法**

  - `agg()`
    - **执行聚合操作**
    - `df['col'].agg('sum', 'mean', 'max')`: 对单列聚合
    - `df.agg({'col1': ['sum', 'max'], 'col2': ['mean', 'min']})`: 对多列聚合
    - `df.groupby('key').agg({'col1': 'sum', 'col2': ['mean', 'max']})`: groupby 后多列多函数聚合
    - `df.group('key').agg(total_amount=('col1', 'sum'), avg_value=('col2', mean))`: **自定义输出列名**

  - `df.duplicated(subset=None, keep='first')`
    - **判断每一行是否为重复行，返回布尔 Series**
    - `subset`: 指定用于判断重复的列名，默认所有列
    - `keep`: {'first', 'last', False}，保留第一个/最后一个重复项，或全部标记为重复

  - `df.drop_duplicates(subset=None, keep='first', inplace=False)`
    - **删除重复的行，只保留第一次出现的**
    - `subset`: 指定用于判断重复的列名
    - `keep`: {'first', 'last', False}，保留第一个/最后一个重复项，或全部删除
    - `inplace`: 是否在原地修改

  - `df.groupby(by, as_index=True)`
    - **用于分组聚合，可以按一列或多列分组，然后对每组进行统计、聚合、变换等操作**
    - `by`: 分组依据，可以是列名、列表、字典、函数等
    - `as_index`: 是否将分组键作为结果的索引

  - `pd.merge(left, right, on=None, how='inner', left_on=None, right_on=None, suffixes=('_x', '_y'))`
    - **合并多个 DataFrame**
    - `left`, `right`: 要合并的两个DataFrame
    - `on`: 用于连接的列名（两个表都有的列）
    - `how`: 连接方式
      - `'inner'`: 默认，交集，只保留两表都存在的行
      - `'left'`: 左连接，保留左表所有行
      - `'right'`: 右连接，保留右表所有行
      - `'outer'`: 并集，所有行都保留
    - `left_on`, `right_on`: 分别指定左右表用于连接的列名（当两表列名不同时用）
    - `suffixes`: 重名列的后缀，默认 ('_x', '_y')
    - `indicator`: 设为 True，会新增一列 _merge，显示每行来源('left_only', 'right_only', 'both')

  - `pd.concat(objs, axis=0, join='outer', ignore_index=False, keys=None)`
    - **按行或按列连接多个 DataFrame**
    - `objs`: 要拼接的 DataFrame 或 Series 序列（如列表）
    - `axis`: 拼接方向，0 表示按行拼接（默认），1 表示按列拼接
    - `join`: {'outer', 'inner'}，拼接时索引的并集或交集（默认'outer'）
    - `ignore_index`: 是否重置新对象的索引（默认 False）
    - `keys`: 为拼接的各块加分组标签，生成多级索引

---

## 实战

1. **给定两个DataFrame，请合并两个表，并保留所有订单记录（左连接），然后计算每个客户的总消费金额和订单数，并按照消费金额降序排列**

    ```python
    import pandas as pd

    customers = pd.DataFrame({
        'customer_id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie']
    })  
    orders = pd.DataFrame({
        'order_id': [101, 102, 103, 104],
        'customer_id': [1, 2, 2, 3],
        'amount': [50, 30, 20, 40]
    })

    # 左连接，保留所有订单记录
    merged = pd.merge(orders, customers, on='customer_id', how='left')

    # 计算每个客户的总消费金额和订单数，并按消费金额降序排列
    result = merged.groupby(['customer_id', 'name']).agg(
        total_amount=('amount', 'sum'),  # 表示对 amount 列求和，结果列名为 total_amount
        order_count=('order_id', 'count')  # 表示对 order_id 列计数，结果列名为 order_count
    ).reset_index().sort_values(by='total_amount', ascending=False)

    print(result)
    ```
