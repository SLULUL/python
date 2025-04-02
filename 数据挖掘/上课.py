import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = pd.read_csv(r'C:\Users\33179\Desktop\train.csv')

f, ax = plt.subplots(1, 2, figsize=(10, 6))
data['Survived'].value_counts().plot.pie(
    explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Survived')
sns.countplot(x='Survived', data=data, alpha=0.75, ax=ax[1])
plt.show()

Age = data.loc[:, 'Age'].values
print(Age[:20])
print(Age.shape)
Age = Age.reshape(-1, 1)

print(Age.shape)
imp_median = 891
data.loc[:, 'Age'] = imp_median
data.info()

x = np.array([[1., -1]])
