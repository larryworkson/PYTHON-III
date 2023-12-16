"""criar um modelo que consiga prever se o crédito deve ser aprovado ou negado"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from funcoes.pontuacao_credito import calcular_pontuacao


df = pd.read_csv('files/clientes-2.csv')
num_cols = df.select_dtypes(include=['float64', 'int64']).columns #separando apenas colunas numericas
print(df.head(40))
df_nums = df[num_cols] #craindo DF somente com números
print(df_nums.corr())

#calculando a pontução
for c in range(0, len(df)):
    df['pontuação'] = df.apply(lambda x: calcular_pontuacao(x), axis=1)

#df.to_csv('files/clientes-2.csv', index=False)

x = df.drop(['cliente', 'historico'], axis=1)
y = df['historico']

modelo = LogisticRegression(max_iter=10000)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)
modelo.fit(x_treino, y_treino)
y_previsto = modelo.predict(x_teste)

cm = confusion_matrix(y_previsto, y_teste)
print(classification_report(y_previsto, y_teste))


# python ex014-analise-credito.py

"""a correlação está dizendo que a dívida não gera impacto sobre a pontuação e a idade impacta muito pouco. Precisa ajustar os dados para aprimorar o modelo."""