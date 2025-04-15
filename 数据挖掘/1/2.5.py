import pandas as pd
data = pd.read_csv('C:\\Users\\33179\\Desktop\\train.csv')

Age = data.loc[:, 'Age'].values
print(Age[:20])
print(Age.shape)
Age = Age.reshape(-1, 1)
print(Age.shape)
