"""regressão logistica está relacionada a classificação. Exemplo, o tenis é esportivo ou casual, o paciente é positivo ou negativo para doença X"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from mlxtend.plotting import plot_confusion_matrix

df = pd.read_csv('files/breast-cancer.csv')
print(df.head(10))

x = df.drop(['id', 'diagnosis'], axis=1) #drop remove linhas ou colunas do dataframe. axis=1 são as colunas, axis=0 são as linhas.
y = df['diagnosis']

modelo = LogisticRegression(max_iter=10000) #esta regressão precisa ter um limite de iterações
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)
modelo.fit(x_treino, y_treino)
y_previsto = modelo.predict(x_teste)

cm = confusion_matrix(y_previsto, y_teste)
print(classification_report(y_previsto, y_teste))

# python ex012-regressao-logistica.py