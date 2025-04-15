import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
data = pd.read_csv('C:\\Users\\33179\\Desktop\\train.csv')
print(data.groupby(['Sex', 'Survived'])['Survived'].count())
sns.countplot(x='Sex', hue='Survived', data=data)
plt.show()
