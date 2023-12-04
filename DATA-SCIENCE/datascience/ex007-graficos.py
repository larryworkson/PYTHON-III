import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('files/dados.csv')

#df = df.drop(df.columns[0], axis=1) #removendo a primeira coluna do df
print(df)
eixo_x = df['Cidade'].value_counts().sort_index().keys() #conta os itens desta coluna e pega os nomes (chaves)
eixo_y = df['Cidade'].value_counts().sort_index().values #conta os itens da coluna e pega os valores.



'''criando grafico'''
plt.bar(eixo_x, eixo_y)
plt.title('Pessoas / cidade')
plt.xlabel('Cidades')
plt.ylabel('Nº pessoas')
plt.xticks(rotation=45)
plt.show()



#python ex007-graficos.py