import sqlite3
class Produto():
    def __init__(self, nome, preco, estoque, img, status):
       """inicializa os atributos dos produtos"""
       self.nome = nome
       self.preco = preco
       self.estoque = 0
       self.img = ''
       self.status = 0 #0 == indisponível. 1 == disponível

    def descricao_produto(self):
        nome = f'{self.nome}\n{self.preco}\n{self.estoque}\n{self.img}\n{self.status}'
        return nome
    
    def cadastrar(nome, preco, estoque, img, status):
        """método que cadastra um produto no BD"""
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, preco FLOAT NOT NULL, estoque INTEGER NOT NULL, img TEXT NOT NULL, status INTEGER NOT NULL)''')
        lista = []
        cadastro = {}
        cadastro['nome'] = nome.title()
        cadastro['preco'] = preco
        cadastro['estoque'] = estoque
        cadastro['img'] = img
        cadastro['status'] = status
        lista.append(cadastro)
        for cadastro in lista:
            cursor.execute(' INSERT INTO produtos (nome, preco, estoque, img, status) VALUES (:nome, :preco, :estoque, :img, :status)', cadastro)
        conexao.commit()
        conexao.close()
    
    def listar_produtos():
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos ORDER BY nome')
        estoque = cursor.fetchall()
        conexao.close()
        return estoque
    
    def deletar_produto(id):
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM produtos WHERE id = ?', (id,))
        conexao.commit()
        conexao.close()