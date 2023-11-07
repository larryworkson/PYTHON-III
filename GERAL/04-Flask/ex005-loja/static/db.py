""" comandos para o db """
import sqlite3
""" conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
cursor = conexao.cursor()
cursor.execute('SELECT * FROM produtos ORDER BY nome')
estoque = cursor.fetchall()

conexao.close()
for i in estoque:
    for p in i:
        print(f'{p}')

    print('-'*30) """
conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
cursor = conexao.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS carrinho (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, preco FLOAT NOT NULL, quantidade INTEGER NOT NULL, img TEXT NOT NULL, categoria TEXT NOT NULL)''')
lista = []
cadastro = {}
cadastro['nome'] = 'produto1'
cadastro['preco'] = 1
cadastro['quantidade'] = 1
cadastro['img'] = 'imagem' 
cadastro['categoria'] = 'categoria'
lista.append(cadastro)
for cadastro in lista:
    cursor.execute(' INSERT INTO carrinho (nome, preco, quantidade, img, categoria) VALUES (:nome, :preco, :quantidade, :img, :categoria)', cadastro)
conexao.commit()
conexao.close()