from sklearn.preprocessing import KBinsDiscretizer
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
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

mms = MinMaxScaler().fit(x_train)
x_train_ = mms.transform(x_train)
x_test_ = mms.transform(x_test)
# 不设置二值化
bnl_ = BernoulliNB().fit(x_train_, ytrain)
print(bnl_.score(x_test_, y_test))

# 设置二值化
bnl = BernoulliNB(binarize=0.5).fit(x_train_, ytrain)
print(bnl.score(x_test_, y_test))
