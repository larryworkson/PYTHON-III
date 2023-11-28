import sqlite3
from functions import *

""" # Conecte-se ao banco de dados
conn = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
cursor = conn.cursor()

# Execute o comando SQL para adicionar uma nova coluna
cursor.execute('ALTER TABLE carrinho ADD COLUMN chave INTEGER NOT NULL')

# Salve as alterações e feche a conexão
conn.commit()
conn.close()
 """

def funcao(**kwargs):
    return kwargs




lista = funcao(nome='joao', cidade='olaria', key=0, irao='funcionou')
itens = ''
for k, i in lista.items():
    itens += f'{i}, '

print(itens[0:-2])


""" conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
cursor = conexao.cursor()
cursor.execute('UPDATE carrinho SET quantidade = ? WHERE id = ?', (nova_quantidade, id,))
conexao.commit()
conexao.close() """