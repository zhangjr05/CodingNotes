import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class LogisticRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.w = None
        self.b = 0
    
    def sigmoid(self, z):
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X, y):
        # 向量化
        X, y = np.asarray(X), np.asarray(y)

        # 初始化参数
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0

        # 梯度下降
        for _ in range(self.n_iterations):
            # 预测概率
            linear_model = np.dot(X, self.w) + self.b
            pred_yicted = self.sigmoid(linear_model)

            # 计算交叉熵损失函数的梯度，也是极大似然估计中负对数似然的梯度
            dw = (1 / n_samples) * np.dot(X.T, pred_yicted - y)
            db = (1 / n_samples) * np.sum(pred_yicted - y)

            # 更新参数
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db
    
    def predict_proba(self, X):
        linear_model = np.dot(X, self.w) + self.b
        return self.sigmoid(linear_model)
    
    def predict(self, X, threshold=0.5):
        return self.predict_proba(X) >= threshold

penguins = sns.load_dataset('penguins')

bill_length_median = penguins['bill_length_mm'].median()
bill_depth_median = penguins['bill_depth_mm'].median()
flipper_length_median = penguins['flipper_length_mm'].median()
body_mass_g_median = penguins['body_mass_g'].median()
penguins.fillna({'bill_length_mm': bill_length_median}, inplace=True)
penguins.fillna({'bill_depth_mm': bill_depth_median}, inplace=True)
penguins.fillna({'flipper_length_mm': flipper_length_median}, inplace=True)
penguins.fillna({'body_mass_g': body_mass_g_median}, inplace=True)
penguins = penguins.dropna()

species_rule = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
island_rule = {'Torgersen': 0, 'Biscoe': 1, 'Dream': 2}
sex_rule = {'Male': 1, 'Female': 0}
penguins['species'] = penguins['species'].map(species_rule)
penguins['island'] = penguins['island'].map(island_rule)
penguins['sex'] = penguins['sex'].map(sex_rule)


X = penguins[['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].to_numpy()
y = penguins['sex'].to_numpy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # 标准化
train_X, test_X, train_y, test_y = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(train_X, train_y)

pred_y = model.predict(test_X)
accuracy = (pred_y == test_y).mean()

print(f'预测准确率: {(accuracy * 100):.2f}%')