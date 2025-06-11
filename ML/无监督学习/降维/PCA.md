# PCA 主成分分析

PCA是一种常用的数据降维方法。它通过线性变换，把原始数据投影到一组新的正交坐标轴（主成分）上，并且这些新坐标轴按数据方差从大到小排序。PCA的目标是尽量保留原始数据的主要信息，同时减少特征数量。

---

## 算法步骤

- **数据标准化（中心化）**
  每个特征减去均值，使其均值为0。
- **计算协方差矩阵**
  反映各特征之间的相关性。
- **计算协方差矩阵的特征值和特征向量**
  - 特征向量：新坐标轴的方向（主成分）。
  - 特征值：每个主成分能解释的方差大小。
- **选取前k大个特征值对应的特征向量**
  组成降维后的新基。
- **将数据投影到新基上**
  完成降维。

---

## 代码实现

```python
import numpy as np
from sklearn.datasets import load_iris

# 加载数据
iris = load_iris()
X, y = iris.data, iris.target
k = 2  # 降维到2维

# 数据标准化（中心化）
X_centered = X - X.mean(axis=0)  # 中心化
X_norm = X_centered / X.std(axis=0)  # 标准化

# 计算协方差矩阵
cov_matrix = np.cov(X_norm, rowvar=False)
# rowvar=False：每一列代表一个变量（特征），每一行代表一个观测样本。

# 计算协方差矩阵的特征值和特征向量
eig_vals, eig_vecs = np.linalg.eigh(cov_matrix)  # 特征分解

# 选取前k个最大特征值对应的特征向量
sorted_idx = np.argsort(eig_vals)[::-1]  # 按特征值从大到小排序
eig_vecs = eig_vecs[:, sorted_idx]
top_k_pc = eig_vecs[:, :k]  # 取前k个主成分

# 将数据投影到新基上
X_pca = X_norm @ top_k_pc
```

```python
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# 加载数据
iris = load_iris()
X, y = iris.data, iris.target

X_centered = X - X.mean(axis=0)  # 中心化
X_norm = X_centered / X.std(axis=0)  # 标准化

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_norm)
```
