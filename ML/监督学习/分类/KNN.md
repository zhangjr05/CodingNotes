# KNN分类（K-Nearest Neighbors）

KNN（K-最近邻）是一种常用的监督学习分类算法，核心思想是：
对于一个待分类样本，找到训练集中距离它最近的K个样本，根据这K个邻居的类别进行投票，票数最多的类别就是预测结果。

---

## 算法步骤

- 计算待分类样本与训练集中所有样本的距离（常用欧氏距离）。
- 选出距离最近的K个邻居。
- 统计这K个邻居的类别，票数最多的类别作为预测结果。

---

## 代码实现

```python
import random
from collections import Counter
import numpy as np

def knn_classify(train_X, train_y, query, k):
    '''KNN简单实现'''
    # 向量化
    train_X, train_y, query = np.asarray(train_X), np.asarray(train_y), np.asarray(query)

    # 计算所有距离
    distances = np.linalg.norm(train_X - query, axis=1)
    
    # 取前k个最近邻
    idx = np.argpartition(distances, k-1)[:k]
    top_k_labels = train_y[idx]
    
    # 投票
    votes = Counter(top_k_labels)
    
    # 返回票数最多的类别，平票时随机返回
    max_count = max(votes.values())
    return random.choice([label for label, count in votes.items() if count == max_count])

if __name__ == '__main__':
    '''测试代码'''
    X = [[1, 2], [2, 1], [3, 3], [6, 5], [7, 7]]
    y = [0, 0, 0, 1, 1]
    print(knn_classify(X, y, [2, 2], 3))  # 0
    print(knn_classify(X, y, [6, 6], 3))  # 1
```

---

## 距离度量的局限性与解决方案

- **替代距离度量**
  - **曼哈顿距离**：适用于特征量纲差异大的情况
  - **余弦距离**：适用于高维稀疏数据（如文本）
  - **马氏距离**：考虑特征间协方差关系
  - **汉明距离**：适用于分类特征数据

- **数据预处理**
  - **特征标准化**：消除量纲影响，使各特征在同一尺度下比较
  - **特征权重**：根据特征重要性分配不同权重
  - **特征选择**：去除噪声特征，保留有区分度的特征

- **自适应方法**
  - **学习距离度量**：基于训练数据自动学习最优距离函数
  - **核方法**：通过核函数将数据映射到高维空间，使用非线性相似度
  - **多距离融合**：组合多种距离度量，提高分类效果

- **应用场景指导**
  - **文本分类**：使用余弦距离或TF-IDF特征
  - **图像识别**：考虑感知特征或深度学习特征提取
  - **时间序列**：使用DTW（动态时间规整）距离
  - **混合数据**：对不同类型特征采用相应距离度量后加权组合
