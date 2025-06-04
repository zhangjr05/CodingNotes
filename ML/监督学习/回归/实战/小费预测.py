import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split


class LinearRegression:
    '''线性回归模型'''
    def __init__(self):
        self.w = None
        self.b = None
    
    def fit(self, X, y):
        '''训练线性回归模型'''
        # 添加偏置项
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        # 使用正规方程求解（解析解）
        theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
        self.b = theta[0].item()
        self.w = theta[1:].reshape(-1, 1)
        return self

    def predict(self, X):
        '''预测新样本'''
        return X @ self.w + self.b


# 加载数据集
tips = sns.load_dataset('tips')

# 特征工程
tips['is_male'] = (tips['sex'] == 'Male').astype(int)
tips['is_smoker'] = (tips['smoker'] == "Yes").astype(int)
tips['is_weekend'] = tips['day'].isin(['Sat', 'Sun']).astype(int)
tips['is_dinner'] = (tips['time'] == 'Dinner').astype(int)

# 划分训练集与测试集
X = tips[['total_bill', 'is_male', 'is_smoker', 'is_weekend', 'is_dinner']].to_numpy()
y = tips['tip'].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 模型训练
model = LinearRegression()
model.fit(X_train, y_train)

# 预测与评估
y_pred = model.predict(X_test).flatten()
mse = np.mean((y_pred - y_test) ** 2)
print(mse)  # 0.6381500702114191