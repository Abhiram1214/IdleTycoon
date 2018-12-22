import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns 
sns.set(color_codes=True)

#EDA 
df = pd.read_csv('iris.data')
df.head()

#Change the column names
df = pd.read_csv('iris.data', header=-1)
df.head()
df.describe()

#adding colums names in pandas
col_name = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
df.columns = col_name
df.head()


#Import Iris dataset from Seaborn
#iris = sns.load_dataset('iris')

#EDA
iris = pd.read_csv('iris.csv')
iris.head()

print(iris.info())
print(iris.groupby('Species').size())

iris.isnull().sum()


#Visualization
sns.pairplot(iris, hue='Species')
iris.hist(edgecolor='black', linewidth=1.2)

#violin plot
plt.subplot(2,2,1)
sns.violinplot(x='Species', y='SepalLengthCm', data=iris)
plt.subplot(2,2,2)
sns.violinplot(x='Species', y='SepalWidthCm', data=iris)
plt.subplot(2,2,3)
sns.violinplot(x='Species', y='PetalLengthCm', data=iris)
plt.subplot(2,2,4)
sns.violinplot(x='Species', y='PetalWidthCm', data=iris)


iris.boxplot(by='Species')

#scatter
pd.plotting.scatter_matrix(iris)
