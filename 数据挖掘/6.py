import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
class_1 = 500
class_2 = 500
centers = [[0.0, 0.0], [2.0, 2.0]]
clusters_std = [0.5, 0.5]

x, y = make_blobs(n_samples=[class_1, class_2],
                  centers=centers,
                  cluster_std=clusters_std,
                  random_state=0,
                  shuffle=False)

x_train, x_test, ytrain, y_test = train_test_split(
    x, y, test_size=0.3, random_state=420)

print(x.shape)
print(np.unique(y))
