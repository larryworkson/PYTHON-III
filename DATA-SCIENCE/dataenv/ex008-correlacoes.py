import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#print(sns.get_dataset_names()) #puxa os datasets padrão

iris = sns.load_dataset('iris')
print(iris)
print(iris['species'].value_counts())
#sns.pairplot(iris, hue='species') #faz uma comparação entre as variáveis
#plt.show()

titanic = sns.load_dataset('titanic')
print(titanic['sex'].value_counts())
print(titanic.head())
sns.pairplot(titanic, hue='class') #faz uma comparação entre as variáveis
'''outra forma de gerar gráficos'''
#sns.scatterplot(x='age', y='sex', data=titanic, hue='class', palette='viridis', size='pclass')
plt.show()

#python ex008-correlacoes.py