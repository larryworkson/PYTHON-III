
import pandas as pd
from sklearn.model_selection import train_test_split #função
from sklearn.linear_model import LinearRegression #método de regressão linear
from sklearn.metrics import mean_absolute_error
from controls.database import *

df = base()

def correlacao():
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df_nums = df[num_cols]
    return df_nums.corr()

x = df[['ppg', 'rpg', 'apg', 'pie', 'xp']]
y = df['sal']

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)
modelo = LinearRegression()
modelo.fit(x_treino, y_treino)
previsao = modelo.predict(x_teste)
print('-'*30)
print('Média de erro: ', mean_absolute_error(previsao, y_teste))
print('-'*30)

def prever(ppg, rpg, apg, pie, xp):
    novo_jogador = {
        'ppg': ppg,
        'rpg': rpg,
        'apg': apg,
        'pie': pie,
        'xp': xp}

    novos_dados = pd.DataFrame([novo_jogador])
    sal_previsto = modelo.predict(novos_dados)
    
    return f'O salário previsto do jogador é: U$ {sal_previsto[0]:.2f}'