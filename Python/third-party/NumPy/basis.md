# NumPy 是 Python 中用于科学计算的基础库

NumPy 提供了高性能的多维数组对象以及相关工具。

---

## Broadcasting

- 当运算的两个操作数矩阵**形状**不同时，运算需要重新定义
  - NumPy通过**广播机制**自动扩展小矩阵，以匹配大矩阵
  - 将不同大小的矩阵转换为**相同大小**，便于进行统一计算
- **从右向左**依次匹配两个矩阵各维度的长度
  - 当两个维度**长度相等**或者**其中一个为1**时，两者**compatible**
  - 当其中一个矩阵**维度不足**时，用**长度为1的新维度**进行补充
- **广播**
  - 将**长度为1的维度**内容复制匹配另一矩阵对应长度

---

## ndarray 数组创建

- **依据现有数据**
  - `np.array([1, 2, 3, 4, 5])` 创建数组
  - `np.asarray()` 当数据源是 ndarray 时，asarray() 不 copy 出新的副本，与原 ndarray 绑定
  - `np.fromfunction(function=lambda i, j: i < j, shape=(3, 4), dtype=int)` 通过在每个坐标上执行函数来构造数组

- **依据填充方式**
  - `np.zeros(5)` 创建全 0 数组，array([0., 0., 0., 0., 0.])
  - `np.ones(5)` 创建全 1 数组，array([1., 1., 1., 1., 1.])
  - `np.empty((3, 4))` 返回空数组，元素为随机数
  - `np.eye(3)` 返回单位矩阵
  - `np.diag([[]])` 提取对角线元素
  - `np.diag([])` 通过一维数组构造对角矩阵
  - `np.full((3, 4), fill_value=7)` 常数数组

- **利用数值范围**
  - `np.arange(0, 10, 2)` [0 2 4 6 8]，创建等差数组
  - `np.linspace(start=0, stop=2, num=9)` 返回指定间隔指定数量的数组
  - `np.random.rand(3, 4)` [0, 1) 随机数组
  - `np.random.random((3, 4))` [0, 1) 随机数组
  - `np.random.randint(2, 5, (3, 4))` 生成 shape=(3, 4) 的随机数组，value 为 [2, 5) 中的随机整数

- **定义结构**
  - `student_type = np.dtype({'names': ['name', 'age'], 'formats': ['U30', 'i8']})` 定义结构化数据类型
  - `students = np.array([('zhangsan', 20), ('lisi', 21)], dtype=student_type)` 创建结构化数组

---

## 索引、切片、迭代

- **副本和视图：数组切片操作返回的是原数组的视图**

  ```python
  a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
  a.copy()  # 创建一个副本
  ```

- **索引与切片**

  ```python
  x = np.array([[4 * i + j + 1 for j in range(4)] for i in range(4)])
  x[2]              # [9 10 11 12]
  x[2][0]           # 9
  x[2, 0]           # 9
  ```

- **切片操作几乎和 list 一样**
  - `x[0:4:2, ::-1]` 步长为 2，逆序切片

- **dots 索引：`...` 表示足够多的冒号来构建完整索引列表**
  - `x[1, 2, ...] == x[1, 2, :, :]` 等价于完整索引

- **整数数组索引**
  - `x[[0, 1, 2]]` 同时选择多个元素

- **布尔索引**

  ```python
  x > 5  # 返回 bool 数组
  x[x > 5]  # 返回符合条件的元素构成的一维数组
  ```

- **迭代**
除了 for 循环，还可以使用以下方法：

  - `np.apply_along_axis(func1d=np.sum, axis=0, arr=x)` np.sum 作用到维度 0
  - `np.apply_along_axis(func1d=np.mean, axis=1, arr=x)` np.mean 作用到维度 1

---

## ndarray 操作

- **变形**
  - `x.shape = (3, 4)` 直接修改 shape 属性
  - `x.flat` 将数组转换为一维迭代器
  - `x.flatten()` 将数组的副本转换为一维数组
  - `np.ravel(x, order='F')` 返回一维视图，order='F' 就是拷贝
  - `np.reshape(x, newshape=(3, 4))` newshape=-1 时降为一维
  - `np.transpose(x)` 数组转置
  - `x.T` 转置

- **更改维度**
  - 升维

    ```python
    x = a[np.newaxis, :]        # axis = 0
    y = a[:, np.newaxis]        # axis = 1
    a = np.expand_dims(a, axis=1)   # 指定位置增加维度
    ```

  - 降维
  `np.squeeze(a, axis=1)` 删除 axis=1 维度

- **合并**

  ```python
  x = np.array([1, 2, 3])
  y = np.array([4, 5, 6])
  np.concatenate([x, y], axis=0)  # 在维度 0 拼接 x 与 y
  np.stack([x, y], axis=1)        # 沿着 axis=1 轴拼接数组 (增加维度)
  np.vstack((x, y))               # 水平堆叠
  np.hstack((x, y))               # 竖直堆叠
  ```

- **拆分**
  - `np.split(a, [1, 3], axis=0)` 按指定索引拆分
  - `np.vsplit(a, 3)` 垂直拆分
  - `np.hsplit(a, 3)` 水平拆分

- **复制**
  - `np.tile(a, (2, 2))` 横向纵向复制
  - `x = np.repeat(3, 4)` [3 3 3 3]
  
    ```python
    x = np.array([[1, 2], [3, 4]])
    np.repeat(x, repeats=2, axis=None)  # axis=0 增加行数，axis=1 增加列数
    np.repeat(x, 2)  # [1 1 2 2 3 3 4 4]
    ```

- **反转**

  ```python
  np.flip(a)                      # 全反转
  np.flip(a, axis=0)              # 反转行
  a[1] = np.flip(a[1])            # 反转第二行
  a[:, 1] = np.flip(a[:, 1])      # 反转第二列
  ```

- **添加/删除元素**

  ```python
  a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  b = np.array([[10, 11, 12]])
  np.append(a, b, axis=0)         # 添加行
  np.append(a, b.T, axis=1)       # 添加列
  np.insert(a, 1, 10, axis=0)     # 在第二行插入元素，一行 10
  np.delete(a, 1, axis=0)         # 删除第二行
  ```

- **排序**

  ```python
  a = np.array([[3, 2, 1], [6, 5, 4]])
  np.sort(a)                      # 对每一行进行排序
  np.sort(a, axis=0)              # 对每一列进行排序
  np.argsort(a)                   # 对每一行进行排序并返回索引构成的数组
  np.argsort(a, axis=0)           # 对每一列进行排序并返回索引构成的数组
  ```
