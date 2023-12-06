import pandas as pd
from sklearn.model_selection import train_test_split #função
from sklearn.linear_model import LinearRegression #método de regressão linear
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('files/lebrom.csv')
print(df.head(10))
#print(df.corr())
x = df[['Pontos por Jogo', 'Minutos em Quadra']]
y = df['Salário Anual']

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

modelo = LinearRegression()
modelo.fit(x_treino, y_treino)

y_previsto = modelo.predict(x_teste)

for c in range(0, len(y_previsto)):
    print(f'{c}º Salário previsto: ', y_previsto[c])

print('Média salarial: ', df['Salário Anual'].mean())
print('Média de erro: ', mean_absolute_error(y_previsto, y_teste))


print('-'*30)
print('Nova previsão')
print('-'*30)
ppg = float(input('Pontos por jogo: '))
min_jogo = float(input('Minutos em Quadra: '))
novo_jogador = {
    'Pontos por Jogo': ppg,
    'Minutos em Quadra': min_jogo}

novos_dados = pd.DataFrame([novo_jogador])
previsao = modelo.predict(novos_dados)
print(f'O salário previsto do jogador é: U$ {previsao[0]:.2f}')

# python ex010-ML.py