import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def KMeans(X, k, max_iters=100, random_state=0):
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

def plot(X, labels, centers):
    '''可视化聚类效果'''
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False

    # 2x2布局显示主要特征组合
    plt.figure(figsize=(10, 8))

    # 萼片特征
    plt.subplot(2, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.7)
    plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, edgecolors='black', linewidth=2, label='聚类中心')
    plt.xlabel('萼片长度 (cm)')
    plt.ylabel('萼片宽度 (cm)')
    plt.title('K-means: 萼片特征')
    plt.legend()
    plt.grid(alpha=0.3)

    # 花瓣特征
    plt.subplot(2, 2, 2)
    plt.scatter(X[:, 2], X[:, 3], c=labels, cmap='viridis', alpha=0.7)
    plt.scatter(centers[:, 2], centers[:, 3], c='red', marker='X', s=200, edgecolors='black', linewidth=2, label='聚类中心')
    plt.xlabel('花瓣长度 (cm)')
    plt.ylabel('花瓣宽度 (cm)')
    plt.title('K-means: 花瓣特征')
    plt.legend()
    plt.grid(alpha=0.3)

    # 真实标签 - 萼片
    plt.subplot(2, 2, 3)
    colors = ['red', 'green', 'blue']
    species = ['setosa', 'versicolor', 'virginica']
    for i, sp in enumerate(species):
        mask = y == sp
        plt.scatter(X[mask, 0], X[mask, 1], c=colors[i], label=sp, alpha=0.7)
    plt.xlabel('萼片长度 (cm)')
    plt.ylabel('萼片宽度 (cm)')
    plt.title('真实标签: 萼片特征')
    plt.legend()
    plt.grid(alpha=0.3)

    # 真实标签 - 花瓣
    plt.subplot(2, 2, 4)
    for i, sp in enumerate(species):
        mask = y == sp
        plt.scatter(X[mask, 2], X[mask, 3], c=colors[i], label=sp, alpha=0.7)
    plt.xlabel('花瓣长度 (cm)')
    plt.ylabel('花瓣宽度 (cm)')
    plt.title('真实标签: 花瓣特征')
    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # 加载数据集
    iris = sns.load_dataset('iris')

    # 特征选取
    X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].to_numpy()
    y = iris['species'].to_numpy()

    # 标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # K-means聚类
    labels, centers = KMeans(X_scaled, k=3, max_iters=100, random_state=42)
    centers = scaler.inverse_transform(centers)

    # 可视化
    plot(X, labels, centers)