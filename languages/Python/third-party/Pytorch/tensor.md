# PyTorch 张量

---

- **张量创建**

    ```python
    size = (2, 3)
    data = [[i + 4 * j for i in range(1, 5)] for j in range(3)]
    a = np.array([1, 2, 3, 4])
    torch.tensor(data)  # 从列表或 ndarray 创建张量
    torch.from_numpy(a) # 从 ndarray 创建张量
    torch.zeros(size)    # 全零张量
    torch.ones(size)     # 全一张量
    torch.empty(size)    # 未初始化的张量
    torch.eye(size)      # 单位矩阵 E
    torch.rand(size)     # 服从 [0, 1) 均匀分布的随机张量
    torch.arange(start=0, end=10, step=2)   # 类似 range
    torch.linspace(start=0, end=10, steps=5)    # 等间隔张量
    ```

- **张量属性**

    ```python
    t = torch.tensor(data)
    t.shape             # 张量形状
    t.size()            # 张量大小
    t.dtype             # 数据类型
    t.device            # 张量所在设备
    t.dim()             # 张量维度
    t.requires_grad_    # 是否需要梯度
    t.numel()           # 元素总数
    t.is_cuda           # 是否在 GPU 上
    t.T                 # 转置
    t.t()               # 转置
    t.item()            # 获取单元素张量的值
    ```

- **张量操作**

    ```python
    t1 = torch.tensor(data)
    t2 = t1.T.reshape(size)
    torch.matmul(t1, t2)    # 矩阵乘法
    torch.dot()             # 一维张量的点乘
    torch.sum()             # 元素求和
    torch.mean()            # 元素平均值
    torch.max()             # 最大值
    torch.min()             # 最小值
    t.reshape(shape=size)   # 改变张量形状
    t.unsqueeze(dim=0)      # 添加指定维度
    t.squeeze(dim=0)        # 删除指定维度
    torch.cat((t1, t2), dim=1)  # 按照指定维度合并张量
    ```

- **张量的 GPU 加速**

    ```python
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    t = torch.tensor(data, device=device)  # 将张量创建到指定设备
    t = t.to(device)                       # 转移张量到指定设备
    ```
