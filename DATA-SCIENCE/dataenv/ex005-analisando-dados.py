import pandas as pd

dados = pd.read_csv('files/dados.csv')
print(dados.head(10)) #mostra as 5 primeiras linhas da tabela
print(dados['Cidade'].value_counts()) #contando quantos registros possui cada valor.

print('-'*30)
print('Agrupando dados')
print('-'*30)
print(dados.groupby(['Cidade'])['Salário'].agg(['describe'])) #mostra a média de salários por cidade
#python ex005-analisando-dados.py