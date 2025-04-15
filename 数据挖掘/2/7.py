''' 第一步，生成实验数据；'''
from sklearn.preprocessing import KBinsDiscretizer
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import MultinomialNB

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

# print(x.shape)
# print(np.unique(y))
''' 第二步：特征矩阵归一化，确保训练集、测试集里面都没有负值；'''
mms = MinMaxScaler().fit(x_train)
kbs = KBinsDiscretizer(n_bins=10, encode='onehot').fit(x_train)
x_train_ = kbs.transform(x_train)
x_test_ = kbs.transform(x_test)
print(x_train_.shape)
# print(x_train.shape)
mnb = MultinomialNB().fit(x_train_, ytrain)
# print(mnb.class_log_prior_)
# 验证是否存在样本不均衡问题；
# print((ytrain == 1).sum()/ytrain.shape[0])
# print((ytrain == 0).sum()/ytrain.shape[0])
# 如何查看真正的先验概率值？
# print(np.exp(mnb.class_log_prior_))
# 重要属性2——feature_log_prob_：返回一个固定标签类别下的每个特征的对数概率log(P(Xi | y));
# print(mnb.feature_log_prob_)
# 重要属性3——class_count_:在 fit 时每个标签类别下包含的样本数;
# print(mnb.class_count_)
''' 第四步：预测；
 返回测试集的预测结果；
 返回每个样本在每个标签取值下的概率
 返回准确度：'''
print(mnb.score(x_test_, y_test))
# print(mnb.predict(x_test_))
# print(mnb.predict_proba(x_test_))
