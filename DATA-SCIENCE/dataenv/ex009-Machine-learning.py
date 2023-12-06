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

print('-'*30)
print('Nova previsão')
print('-'*30)
renda_media = float(input('Renda média da área: '))
idade_media_casa = float(input('Idade média das casas na área: '))
num_medio_quartos = float(input('Número médio de quartos na área: '))
pop_area = float(input('População da área: '))
nova_casa = {'Renda média da área': renda_media,
             'Idade média das casas na área': idade_media_casa,
             'Número médio de quartos na área': num_medio_quartos,
             'População da área': pop_area}

novos_dados = pd.DataFrame([nova_casa])
previsao = modelo.predict(novos_dados)
print(f'A previsão de preço para a nova casa é: R$ {previsao[0]:.2f}')

# python ex009-Machine-learning.py
