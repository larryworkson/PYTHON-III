import pandas as pd
from sklearn.model_selection import train_test_split #função
from sklearn.linear_model import LinearRegression #método de regressão linear
from sklearn.metrics import mean_absolute_error


df = pd.read_csv('files/dados-casas.csv')
print(df.head())
correlacoes = df.corr()

 
x = df[['Renda média da área', 'Idade média das casas na área', 'Número médio de quartos na área', 'População da área' ]] #características
y = df['Preço'] #alvo
'''a regressão lienar vai buscar na características traçar uma reta para prever o salário''' 

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y) #separa uma fatia dos dados para testar a predição

modelo = LinearRegression()
modelo.fit(x_treino, y_treino) #ajusta a função usando como base os dados do treino

y_previsto = modelo.predict(x_teste)

for i in y_previsto:
    print(f'Previsão: {i:.2f}')
#print(y_previsto) #output [4818.34561286 1361.07501674 8228.46282652]
print('Média de preço: ', df['Preço'].mean())

'''verificando a média de erro da predição'''
print('Média de erro: ', mean_absolute_error(y_previsto, y_teste)) 

# python ex009-Machine-learning.py
