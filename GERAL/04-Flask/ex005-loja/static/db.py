""" comandos para o db """
import sqlite3
conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
cursor = conexao.cursor()
cursor.execute('ALTER TABLE produtos RENAME COLUMN status TO categoria')
estoque = cursor.fetchall()
conexao.close()