# K-means 聚类

K-means 是一种常用的无监督聚类算法，用于将数据集划分为 K 个簇。其目标是最小化簇内样本到簇中心的距离平方和，使同一簇内的数据相似度高，不同簇间的数据相似度低。

---

## 算法步骤

- **选择聚类数 K**
  预先指定要分成的簇的数量K。
- **初始化中心点**
  随机选择K个样本作为初始簇中心。
- **分配样本到最近的中心**
  计算每个样本到各中心的距离，将其分配到最近的中心所属的簇。
- **更新中心点**
  对每个簇，计算所有成员的均值，作为新的中心点。
- **重复分配与更新**
  重复分配与更新的步骤，直到中心点不再变化或达到最大迭代次数。

---

## 代码实现

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def KMeans(X, k, max_iters=100, random_state=42):
    '''K-means聚类'''

    X = np.asarray(X)
    
    # 初始化中心点
    np.random.seed(random_state)
    centers = X[np.random.choice(len(X), k, replace=False)]
    
    for _ in range(max_iters):
        # 分配簇标签
        distances = np.linalg.norm(X[:, None] - centers, axis=2)
        labels = np.argmin(distances, axis=1)
        
        # 更新中心点，处理空簇
        new_centers = []
        for i in range(k):
            cluster_points = X[labels == i]
            if len(cluster_points) > 0:
                new_centers.append(cluster_points.mean(axis=0))
            else:
                new_centers.append(X[np.random.randint(len(X))])
        new_centers = np.asarray(new_centers)
        
        # 检查收敛
        if np.allclose(centers, new_centers):
            break
        centers = new_centers
    
    return labels, centers

def plot_KMeans(X, labels, centers):
    plt.figure(figsize=(10, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.7)
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X', edgecolors='black', linewidth=2, label='Centers')
    plt.title('K-means Clustering Result')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

if __name__ == '__main__':
    # 测试代码
    X, y_true = make_blobs(n_samples=150, centers=3, cluster_std=0.60, random_state=42)
    labels, centers = KMeans(X, k=3)
    plot_KMeans(X, labels, centers)
```
