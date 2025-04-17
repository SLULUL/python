from sklearn.naive_bayes import GaussianNB
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from matplotlib.colors import ListedColormap

muNB = GaussianNB()
iris = load_iris()
data = iris.data
target = iris.target
sample = data[:, :2]

muNB.fit(sample, target)
xmin, xmax = sample[:, 0].min(), sample[:, 0].max()
ymin, ymax = sample[:, 1].min(), sample[:, 1].max()
x = np.arange(xmin, xmax, 300)
y = np.arange(ymin, ymax, 300)
xx, yy = np.meshgrid(x, y)
x_test = np.c_[xx.ravel(), yy.ravel()]

y_ = muNB.predict(x_test)

colormap = ListedColormap(['#00aaff', '#aa00ff', '#ffaa00'])
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_)
plt.scatter(sample[:, 0], sample[:, 1], c=target, cmap=colormap)
plt.show()
