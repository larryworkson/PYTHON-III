""" comandos para o db """
import sqlite3
conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
cursor = conexao.cursor()
cursor.execute('SELECT * FROM produtos ORDER BY nome')
estoque = cursor.fetchall()

conexao.close()
for i in estoque:
    for p in i:
        print(f'{p}')

    print('-'*30)