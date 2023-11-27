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

estoque = Produto.listar_produtos()
for i in estoque:
    print(i)

Produto.deletar_produto(11)

for p in estoque:
    print(p)