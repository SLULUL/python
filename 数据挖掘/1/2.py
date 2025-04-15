import pandas as pd
from sklearn.impute import SimpleImputer
data = pd.read_csv('C:\\Users\\33179\\Desktop\\train.csv')
Age = data.loc[:, 'Age'].values
Age = Age.reshape(-1, 1)
print(Age[:20])
print("-" * 20)
imp_mean = SimpleImputer()
imp_median = SimpleImputer(strategy='median')
imp_0 = SimpleImputer(strategy='constant', fill_value=0)
imp_mean = imp_mean.fit_transform(Age)
imp_median = imp_median.fit_transform(Age)
imp_0 = imp_0.fit_transform(Age)


# data.info()
# data.loc[:, 'Age'] = imp_median
# data.info()
# # 下为Embarked字段用众数填补
# Embarked = data.loc[:, 'Embarked'].values
# Embarked = Embarked.reshape(-1, 1)
# imp_most_frequent = SimpleImputer(strategy='most_frequent')
# imp_most_frequent = imp_most_frequent.fit_transform(Embarked)
# data.loc[:, 'Embarked'] = imp_most_frequent
# data.info()
