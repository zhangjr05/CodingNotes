import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# PCA降维

iris = sns.load_dataset("iris")
X = iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]].to_numpy()
X_centered = X - np.mean(X, axis=0)
X_norm = X_centered / np.std(X, axis=0)

cov_matrix = np.cov(X_norm, rowvar=False)
eig_vals, eig_vecs = np.linalg.eigh(cov_matrix)
sorted_idx = np.argsort(eig_vals)[::-1]
top_2_pc = eig_vecs[:, sorted_idx][:, :2]

X_pca = X_norm @ top_2_pc


# 可视化

plt.figure(figsize=(10, 4))

# 原始数据
plt.subplot(1, 2, 1)
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.title('original data')

# PCA结果
plt.subplot(1, 2, 2)
colors = ['red', 'green', 'blue']
species_list = ['setosa', 'versicolor', 'virginica']
for species, color in zip(species_list, colors):
    mask = iris['species'] == species
    plt.scatter(X_pca[mask, 0], X_pca[mask, 1], 
               c=color, label=species, alpha=0.7)
plt.title('PCA result')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()