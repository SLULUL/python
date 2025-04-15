import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
data = pd.read_csv('C:\\Users\\33179\\Desktop\\train.csv')
f, ax = plt.subplots(1, 2, figsize=(10, 6))
data['Survived'].value_counts().plot.pie(
    explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Survived')
sns.countplot(x='Survived', data=data, saturation=0.75, ax=ax[1])
plt.show()
