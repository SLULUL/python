from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

X = np.array([[1., -1., 2.], [2., 0., 0.], [0., 1., -1.]])
min_max_scaler = MinMaxScaler(feature_range=(5, 10))
X_train_minmax = min_max_scaler.fit_transform(X)
print(X_train_minmax)
