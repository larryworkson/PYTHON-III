import pandas as pd
from sklearn.model_selection import train_test_split #função
from sklearn.linear_model import LinearRegression #método de regressão linear
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('files/NBA-stats-2.csv')
print(df.head(9))
#seleção das colunas númericas
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
#dataframe contendo apenas as colunas numericas
df_nums = df[num_cols]

#calculando correlação:
print(df_nums.corr())

x = df[['PPG', 'RPG', 'APG', 'PIE']]
y = df['Salário Anual']

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

modelo = LinearRegression()
modelo.fit(x_treino, y_treino)

previsao = modelo.predict(x_teste)
print('-'*30)
print('Média de erro: ', mean_absolute_error(previsao, y_teste))
print('-'*30)

print('-'*30)
print('Nova previsão')
print('-'*30)
ppg = float(input('PPG: '))
rpg = float(input('RPG: '))
apg = float(input('APG: '))
pie = float(input('PIE: '))
xp = int(input('XP: '))
novo_jogador = {
    'ppg': ppg,
    'rpg': rpg,
    'apg': apg,
    'pie': pie,
    'xp': xp}

novos_dados = pd.DataFrame([novo_jogador])
sal_previsto = modelo.predict(novos_dados)
corrigido = sal_previsto[0] + mean_absolute_error(previsao, y_teste)
print(f'O salário previsto do jogador é: U$ {sal_previsto[0]:.2f}')


# python ex011-ml-nba.py

"""o salário está sendo altamente impactado pelo RPG, add mais dados usar a API pesqGoogle que criei."""