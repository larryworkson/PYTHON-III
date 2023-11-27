import sqlite3
from datetime import datetime
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


    # GERENCIAMENTO DO ESTOQUE
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
        """Esta listagem busca todos os produtos cadastrados"""
        estoque = ativar_db('SELECT * FROM produtos ORDER BY nome')
        return estoque  
    
    def soma_patrimonio():
        itens = Produto.listar_produtos()
        totpatrimonio = 0
        for c in itens:
            totpatrimonio += c[2] * c[3]
        return f'{totpatrimonio:.2f}'
    
    def soma_estoque():
        itens = Produto.listar_produtos()
        totestoque = 0
        for c in itens:
            totestoque += c[3]
        return totestoque
    
    def busca_produto(v):
        produto = ativar_db('SELECT * FROM produtos WHERE id = ?', v)               
        return produto
    
    def deletar_produto(id):
        ativar_db('DELETE FROM produtos WHERE id = ?', id, True)

    # GERENCIAMENTO DA LOJA VIRTUAL

    def listar_produtos_site():
        """Esta listagem busca apenas os produtos cadastrados com pelo menos 1 item no estoque"""
        estoque = ativar_db('SELECT * FROM produtos WHERE estoque > 0 ORDER BY nome')
        return estoque
    
    def add_carrinho(id):
        """esta função vai até o banco de dados produtos e copia as informações do produto para adicionar ao (BD) carrinho"""
        produto = ativar_db('SELECT * FROM produtos WHERE id = ?', id, False, 'one')

        def enviar_para_carrinho():
            """ENVIANDO PARA O CARRINHO"""
            conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
            cursor = conexao.cursor()
            cursor.execute(''' CREATE TABLE IF NOT EXISTS carrinho (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, preco FLOAT NOT NULL, quantidade INTEGER NOT NULL, img TEXT NOT NULL, categoria TEXT NOT NULL, chave INTEGER NOT NULL)''')
            lista = []
            cadastro = {}
            cadastro['nome'] = produto[1]
            cadastro['preco'] = produto[2]
            cadastro['quantidade'] = 1
            cadastro['img'] = produto[4]
            cadastro['categoria'] = produto[5]
            cadastro['chave'] = produto[0]
            lista.append(cadastro)
            for cadastro in lista:
                cursor.execute(' INSERT INTO carrinho (nome, preco, quantidade, img, categoria, chave) VALUES (:nome, :preco, :quantidade, :img, :categoria, :chave)', cadastro)
            conexao.commit()
            conexao.close()
        #verificando se já tem um produto igual no carrinho.
        carrinho = Produto.lista_carrinho() #puxa os itens do carrinho.
        encontrado = False #boolean para condicionar o envio.
        for i in carrinho: #percorre todos os itens do carrinho para verificar se há algum igual.
            if produto[0] == i[6]:
                Produto.incrementar_item(i[0])
                encontrado = True #boolean ativado para não executar o if depois do break e evitar duplicidade.
                break
        if not encontrado:
            enviar_para_carrinho()           
                         
    
    def lista_carrinho():
        carrinho = ativar_db('SELECT * FROM carrinho ORDER BY nome')        
        return carrinho
    
    def soma_carrinho():
        itens = Produto.lista_carrinho()
        soma = 0
        for item in itens:
            soma += item[2] * item[3]
        return f'{soma:.2f}'
    
    def deletar_produto_carrinho(id):
        ativar_db('DELETE FROM carrinho WHERE id = ?', id, True)       
    
    def incrementar_item(id):
        """buscando quantidade atual"""
        produto = ativar_db('SELECT * FROM carrinho WHERE id = ?', id)        

        #verificando disponibilidade de estoque. 
        qtd_estoque = Produto.busca_produto(produto[0][6]) #buscando o produto no estoque com o o identificador do produto que está no carrinho
        if qtd_estoque[0][3] > produto[0][3]:
            nova_quantidade = produto[0][3] + 1 

            """atualizando a quantidade"""

            conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
            cursor = conexao.cursor()
            cursor.execute('UPDATE carrinho SET quantidade = ? WHERE id = ?', (nova_quantidade, id,))
            conexao.commit()
            conexao.close()
    
    def decrementar_item(id):
        """buscando quantidade atual"""
        produto = ativar_db('SELECT * FROM carrinho WHERE id = ?', id)
                
        if produto[0][3] > 0:
            nova_quantidade = produto[0][3] - 1 
            
            """atualizando a quantidade"""
            conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
            cursor = conexao.cursor()
            cursor.execute('UPDATE carrinho SET quantidade = ? WHERE id = ?', (nova_quantidade, id,))
            conexao.commit()
            conexao.close()

    def atualizar_estoque():
        carrinho = Produto.lista_carrinho()
        for item in carrinho:
            key = item[6]
            """buscando quantidade atual"""
            estoque = Produto.busca_produto(key)
            nova_qtd = estoque[0][3] - item[3] #nova quantidade é o estoque atuao - a quantidade comprada no carrinho.
            conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
            cursor = conexao.cursor()
            cursor.execute('UPDATE produtos SET estoque = ? WHERE id = ?', (nova_qtd, key))
            conexao.commit()
            conexao.close()

#FUNÇÕES GERAIS

def ativar_db(exec='', id='', commit=False, conteudo = 'all'):
        """esta função abre e fecha o db e retorna valores        
        :exec = é comando que deve ser executado no DB
        :id = caso a execução seja em uma linha específica
        :commit = True para alteração no BD. False para consulta
        :conteudo = 'all' para fetchall ou 'one' para fetchone
        """

        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')                
        cursor = conexao.cursor()
        
        #verificando se executa em um id ou geral
        if id != '':
            cursor.execute(f'{exec}', (int(id),))
        else:
            cursor.execute(f'{exec}')

        #verificando se pega um item ou todos
        if conteudo == 'one':
            valores = cursor.fetchone()
        else:
            valores = cursor.fetchall()
        
        #verificando se fará alteração no banco
        if commit == True:
            conexao.commit()
        
        conexao.close()
        return valores

def registrar_venda():
    """esta função copia os nomes dos itens comprados no carrinho e adiciona a um tabela com data, hora e valor total da compra."""
    #listando itens do carrinho
    carrinho = Produto.lista_carrinho()
    itens = ''
    for item in carrinho: #estou adicionar o nome de todos os itens do carrinho em uma única célula para saber o que vendeu.
        itens += f'[{item[3]}] {item[1]} + '

    #capturando data e hora da compra
    data_hora = datetime.now()
    formato = '%d/%m/%Y %H:%M'
    data_hora_formatada = data_hora.strftime(formato)

    #conectando ao BD
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
    cursor = conexao.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS vendas (id INTEGER PRIMARY KEY, nomeitens TEXT NOT NULL, precotot FLOAT NOT NULL, data TEXT NOT NULL)''')
    lista = []
    cadastro = {}
    cadastro['nomeitens'] = itens #a soma de todos os nomes dos itens do carrinho
    cadastro['precotot'] = Produto.soma_carrinho()
    cadastro['data'] = data_hora_formatada
    lista.append(cadastro)
    for cadastro in lista:
        cursor.execute(' INSERT INTO vendas (nomeitens, precotot, data) VALUES (:nomeitens, :precotot, :data)', cadastro)
    conexao.commit()
    conexao.close()
    
def listar_vendas():
    vendas = ativar_db('SELECT * FROM vendas ORDER BY data')    
    return vendas

def del_venda(id):
    ativar_db('DELETE FROM vendas WHERE id = ?', id, True)
    
