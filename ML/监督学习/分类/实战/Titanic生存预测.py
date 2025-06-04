import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split


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
            y_predicted = self.sigmoid(linear_model)

            # 计算交叉熵损失函数的梯度，也是极大似然估计中负对数似然的梯度
            dw = (1 / n_samples) * np.dot(X.T, y_predicted - y)
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # 更新参数
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db
    
    def predict_proba(self, X):
        linear_model = np.dot(X, self.w) + self.b
        return self.sigmoid(linear_model)
    
    def predict(self, X, threshold=0.5):
        return self.predict_proba(X) >= threshold

titanic = sns.load_dataset('titanic')


median_age = titanic['age'].median()
titanic.fillna({'age': median_age}, inplace=True)
mode_embarked = titanic['embarked'].mode()[0]
titanic.fillna({'embarked': mode_embarked}, inplace=True)

embarked_rule = {'S': 0, 'C': 1, 'Q': 2}
titanic['embarked'] = titanic['embarked'].map(embarked_rule)
who_rule = {'man': 0, 'woman': 1, 'child': 2}
titanic['who'] = titanic['who'].map(who_rule)
titanic['adult_male'] = titanic['adult_male'].astype(int)
titanic['alone'] = titanic['alone'].astype(int)

features = ['pclass', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'who', 'adult_male', 'alone']
X = titanic[features].to_numpy()
y = titanic['survived'].to_numpy()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy_rate = np.mean(y_pred == y_test)

print(accuracy_rate)