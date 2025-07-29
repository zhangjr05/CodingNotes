import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.w = None
        self.b = None
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.loss_history = []

    def fit(self, X, y):
        '''使用梯度下降算法训练线性回归模型'''
        X, y = np.asarray(X), np.asarray(y)

        # 初始化参数
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0

        # 梯度下降迭代
        for i in range(self.n_iterations):
            # 计算预测值
            y_pred = self._predict(X)
            
            # 计算误差
            errors = y_pred - y
            
            # 计算梯度
            dw = (1 / n_samples) * (X.T @ errors)
            db = (1 / n_samples) * np.sum(errors)
            
            # 更新参数
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

            # 计算损失
            loss = (1 / (2 * n_samples)) * np.sum(errors ** 2)
            self.loss_history.append(loss)

        return self
    
    def _predict(self, X):
        '''内部预测函数'''
        return X @ self.w + self.b
    
    def predict(self, X):
        return self._predict(X)


diamonds = sns.load_dataset('diamonds')

# 特征工程
cut_rule = {'Ideal': 5, 'Premium': 4, 'Very Good': 3, 'Good': 2, 'Fair': 1}
color_rule = {'D': 7, 'E': 6, 'F': 5, 'G': 4, 'H': 3, 'I': 2, 'J': 1}
clarity_rule = {'IF': 8, 'VVS1': 7, 'VVS2': 6, 'VS1': 5, 'VS2': 4, 'SI1': 3, 'SI2': 2, 'I1': 1}
diamonds['cut'] = diamonds['cut'].map(cut_rule)
diamonds['color'] = diamonds['color'].map(color_rule)
diamonds['clarity'] = diamonds['clarity'].map(clarity_rule)


X = diamonds[['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']].to_numpy()
y = diamonds['price'].to_numpy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
train_X, test_X, train_y, test_y = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

model = LinearRegression(learning_rate=0.1, n_iterations=2000)
model.fit(train_X, train_y)
pred_y = model.predict(test_X)

r2 = r2_score(test_y, pred_y)
print(f"决定系数 R² = {r2:.4f}")