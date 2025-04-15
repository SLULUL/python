import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import numpy as np
iris = load_iris()
X = iris.data
y = iris.target
# print(X.shape)
pca = PCA(n_components=2)
pca = pca.fit(X)
X_dr = pca.transform(X)
# print(X_dr.shape)
# print(y == 0)
# print(X_dr[y == 0, 0])
# plt.figure()
# plt.scatter(X_dr[y == 0, 0], X_dr[y == 0, 1],
#             c='red', label=iris.target_names[0])
# plt.scatter(X_dr[y == 1, 0], X_dr[y == 1, 1],
#             c='black', label=iris.target_names[1])
# plt.scatter(X_dr[y == 2, 0], X_dr[y == 2, 1],
#             c='orange', label=iris.target_names[2])
# plt.legend()
# plt.title('PCA of IRIS dataset')
# plt.show()
# print(pca.explained_variance_)
# print(pca.explained_variance_ratio_)
# print(pca.explained_variance_ratio_.sum())
pca_line = PCA().fit(X)
# print(pca_line.explained_variance_ratio_)
# print(np.cumsum(pca_line.explained_variance_ratio_))
# plt.plot(np.arange(1, 5), np.cumsum(pca_line.explained_variance_ratio_))
# plt.xticks(np.arange(1, 5))
# plt.xlabel('Number of components after dimensionality reduction')
# plt.ylabel('Cumulative explained variance')
# plt.show()

# n_components的不同取值方式
# 1. 整数方式 - 指定保留的主成分数量
pca_int = PCA(n_components=2)
X_dr_int = pca_int.fit_transform(X)
print("整数方式(2个成分)解释方差比例:", pca_int.explained_variance_ratio_)

# 2. 浮点数方式 - 指定保留的方差百分比
pca_float = PCA(n_components=0.95)  # 保留95%的方差
X_dr_float = pca_float.fit_transform(X)
print("浮点数方式(95%方差)保留成分数:", pca_float.n_components_)

# 3. None - 保留所有成分
pca_all = PCA(n_components=None)
X_dr_all = pca_all.fit_transform(X)
print("None方式保留成分数:", pca_all.n_components_)

# 4. 'mle' - 使用最大似然估计自动选择
try:
    pca_mle = PCA(n_components='mle')
    X_dr_mle = pca_mle.fit_transform(X)
    print("MLE方式保留成分数:", pca_mle.n_components_)
except Exception as e:
    print("MLE方式错误:", str(e))
