import sqlite3
class Produto():
    def __init__(self, nome, preco, estoque, img, categoria):
       """inicializa os atributos dos produtos"""
       self.nome = nome
       self.preco = preco
       self.estoque = estoque
       self.img = img
       self.categoria = categoria #0 == indisponível. 1 == disponível

    def descricao_produto(self):
        nome = f'{self.nome}\n{self.preco}\n{self.estoque}\n{self.img}\n{self.categoria}'
        return nome
    
    def cadastrar(self):
        """método que cadastra um produto no BD"""
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, preco FLOAT NOT NULL, estoque INTEGER NOT NULL, img TEXT NOT NULL, categoria TEXT NOT NULL)''')
        lista = []
        cadastro = {}
        cadastro['nome'] = self.nome.title()
        cadastro['preco'] = self.preco
        cadastro['estoque'] = self.estoque
        cadastro['img'] = self.img
        cadastro['categoria'] = self.categoria
        lista.append(cadastro)
        for cadastro in lista:
            cursor.execute(' INSERT INTO produtos (nome, preco, estoque, img, categoria) VALUES (:nome, :preco, :estoque, :img, :categoria)', cadastro)
        conexao.commit()
        conexao.close()
    
    def listar_produtos():
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos ORDER BY nome')
        estoque = cursor.fetchall()
        conexao.close()
        return estoque
    
    def busca_produto(v):
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos WHERE id = ?', (v,))
        produto = cursor.fetchall()
        conexao.commit()
        conexao.close()
        return produto
    
    def deletar_produto(id):
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM produtos WHERE id = ?', (id,))
        conexao.commit()
        conexao.close()
    
    """botão comprar não está funcionando"""
    def add_carrinho(id):
        """esta função vai até o banco de dados produtos e copia as informações do produto para adicionar ao banco carrinho"""

        """BUSCANDO INFOS DO PRODUTO"""
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,))
        produto = cursor.fetchone()
        conexao.close()
        
        """ENVIANDO PARA O CARRINHO"""
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS carrinho (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, preco FLOAT NOT NULL, quantidade INTEGER NOT NULL, img TEXT NOT NULL, categoria TEXT NOT NULL)''')
        lista = []
        cadastro = {}
        cadastro['nome'] = produto[1]
        cadastro['preco'] = produto[2]
        cadastro['quantidade'] = 1
        cadastro['img'] = produto[4]
        cadastro['categoria'] = produto[5]
        lista.append(cadastro)
        for cadastro in lista:
            cursor.execute(' INSERT INTO carrinho (nome, preco, quantidade, img, categoria) VALUES (:nome, :preco, :quantidade, :img, :categoria)', cadastro)
        conexao.commit()
        conexao.close()
    
    def lista_carrinho():
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM carrinho ORDER BY nome')
        carrinho = cursor.fetchall()
        conexao.close()
        return carrinho
    
    def deletar_produto_carrinho(id):
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM carrinho WHERE id = ?', (id,))
        conexao.commit()
        conexao.close()
    
    def incrementar_item(id):
        """buscando quantidade atual"""
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM carrinho WHERE id = ?', (id,))
        produto = cursor.fetchall()       
        nova_quantidade = produto[0][3] + 1 
        conexao.commit()
        conexao.close()
        """atualizando a quantidade"""
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('UPDATE carrinho SET quantidade = ? WHERE id = ?', (nova_quantidade, id,))
        conexao.commit()
        conexao.close()
    
    def decrementar_item(id):
        """buscando quantidade atual"""
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM carrinho WHERE id = ?', (id,))
        produto = cursor.fetchall()       
        nova_quantidade = produto[0][3] - 1 
        conexao.commit()
        conexao.close()
        """atualizando a quantidade"""
        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
        cursor = conexao.cursor()
        cursor.execute('UPDATE carrinho SET quantidade = ? WHERE id = ?', (nova_quantidade, id,))
        conexao.commit()
        conexao.close()

