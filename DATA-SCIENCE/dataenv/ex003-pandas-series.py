import pandas as pd


'''O pandas foi feito baseado no Numpy'''
lista = [12, 23, 4, 40, 2, 0]
serie_pandas = pd.Series(lista)
print(serie_pandas)
print('-'*30)
#ele permite criar series com dicionários
notas = {'Tiago': 6.5, 'Ana': 5.5, 'Matheus': 8, 'Leandro': 3}
serie_notas = pd.Series(notas)
print(serie_notas)
print(serie_notas['Ana']) #posso acessar os elementos pelo nome
print('Média: ', serie_notas.mean())
print('Mediana:', serie_notas.median())
print(serie_notas.describe())
