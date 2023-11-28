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
        enviar_db(exec='CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, preco FLOAT NOT NULL, estoque INTEGER NOT NULL, img TEXT NOT NULL, categoria TEXT NOT NULL)', action='INSERT INTO produtos (nome, preco, estoque, img, categoria) VALUES (:nome, :preco, :estoque, :img, :categoria)', nome=self.nome.title(), preco=self.preco, estoque=self.estoque, img=self.img, categoria=self.categoria)
    
    def listar_produtos():
        """Esta listagem busca todos os produtos cadastrados"""
        estoque = ativar_db(exec='SELECT * FROM produtos ORDER BY nome')
        return estoque  
    
    def soma_patrimonio():
        itens = Produto.listar_produtos()
        totpatrimonio = 0
        for c in itens:
            multi = c[2] * c[3]
            totpatrimonio += multi
        return f'{totpatrimonio:.2f}'
    
    def soma_estoque():
        itens = Produto.listar_produtos()
        totestoque = 0
        for c in itens:
            totestoque += c[3]
        return totestoque
    
    def busca_produto(v):
        produto = ativar_db(exec='SELECT * FROM produtos WHERE id = ?', id=v)               
        return produto
    
    def deletar_produto(id):
        ativar_db(exec='DELETE FROM produtos WHERE id = ?', id=id, commit=True)


#----------------------
#BANCO DE DADOS
#----------------------
def ativar_db(exec='', id='', commit=False, conteudo = 'all'):
        """esta função abre e fecha o db e retorna valores        
        :exec = é comando que deve ser executado no DB
        :id = caso a execução seja em uma linha específica
        :commit = True para alteração no BD. False para consulta
        :conteudo = 'all' para fetchall ou 'one' para fetchone
        """

        conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')                
        cursor = conexao.cursor()
        
        #verificando se executa em uma linha ou geral
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

def enviar_db(exec='', action='', **kwargs):
    """adiciona e edita itens no DB
    :exec = é comando que deve ser executado no DB
    :id = KEY
    :commit = True para alteração no BD. False para consulta"""
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')

    cursor = conexao.cursor()
    cursor.execute(exec)
    lista = []
    lista.append(kwargs)
    for kwargs in lista:        
            cursor.execute(action, kwargs)
    conexao.commit()
    conexao.close()

def editar_db(exec='', id='', **kwargs):
    """faz updates no BD."""
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
    cursor = conexao.cursor()
    itens = '' #variável armazena os itens passados na kwargs
    for k, i in kwargs.items():
        itens += f'{i}, ' #junta todos os kwargs em uma string separado por ','
    cursor.execute(exec, (itens[0:-2], id)) #envia os itens para serem executados, removendo a última ',' e o último espaço.
    conexao.commit()
    conexao.close()
#----------------------
#FIM BANCO DE DADOS
#----------------------
   

#-------------------
#CARRINHO DE COMPRAS
#-------------------
def add_carrinho(id):
        """esta função vai até o banco de dados produtos e copia as informações do produto para adicionar ao (BD) carrinho"""
        produto = ativar_db(exec='SELECT * FROM produtos WHERE id = ?', id=id, commit=False, conteudo='one')

        def enviar_para_carrinho():
            """envia o produto para a tabela carrinho, verificando se o produto já consta"""
            enviar_db(exec='CREATE TABLE IF NOT EXISTS carrinho (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, preco FLOAT NOT NULL, quantidade INTEGER NOT NULL, img TEXT NOT NULL, categoria TEXT NOT NULL, chave INTEGER NOT NULL)', action='INSERT INTO carrinho (nome, preco, quantidade, img, categoria, chave) VALUES (:nome, :preco, :quantidade, :img, :categoria, :chave)', nome=produto[1], preco=produto[2], quantidade=1, img=produto[4], categoria=produto[5], chave=produto[0])

        #verificando se já tem um produto igual no carrinho.
        carrinho = lista_carrinho() #puxa os itens do carrinho.
        encontrado = False #boolean para condicionar o envio.
        for i in carrinho: #percorre todos os itens do carrinho para verificar se há algum igual.
            if produto[0] == i[6]:
                incrementar_item(i[0])
                encontrado = True #boolean ativado para não executar o if depois do break e evitar duplicidade.
                break
        if not encontrado:
            enviar_para_carrinho()  

def lista_carrinho():
        cart = ativar_db(exec='SELECT * FROM carrinho ORDER BY nome')        
        return cart

def soma_carrinho():
        itens = lista_carrinho()
        soma = 0
        for item in itens:
            soma += item[2] * item[3]
        return f'{soma:.2f}'

def deletar_produto_carrinho(id):
        ativar_db(exec='DELETE FROM carrinho WHERE id = ?', id=id, commit=True)

def incrementar_item(id):
        """buscando quantidade atual"""
        produto = ativar_db(exec='SELECT * FROM carrinho WHERE id = ?', id=id)        

        #verificando disponibilidade de estoque. 
        qtd_estoque = Produto.busca_produto(produto[0][6]) #buscando o produto no estoque com o o identificador do produto que está no carrinho
        if qtd_estoque[0][3] > produto[0][3]:
            nova_quantidade = produto[0][3] + 1 
            editar_db(exec='UPDATE carrinho SET quantidade = ? WHERE id = ?', id=id, quantidade=nova_quantidade)

            #conexao antiga
            """atualizando a quantidade"""
            """ conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
            cursor = conexao.cursor()
            cursor.execute('UPDATE carrinho SET quantidade = ? WHERE id = ?', (nova_quantidade, id,))
            conexao.commit()
            conexao.close() """

def decrementar_item(id):
        """buscando quantidade atual"""
        produto = ativar_db(exec='SELECT * FROM carrinho WHERE id = ?', id=id)
                
        if produto[0][3] > 0:
            nova_quantidade = produto[0][3] - 1 
            
            """atualizando a quantidade"""
            editar_db(exec='UPDATE carrinho SET quantidade = ? WHERE id = ?', id=id, quantidade=nova_quantidade)

            #conexao antiga
            """ conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
            cursor = conexao.cursor()
            cursor.execute('UPDATE carrinho SET quantidade = ? WHERE id = ?', (nova_quantidade, id,))
            conexao.commit()
            conexao.close() """
#-----------------------
#FIM CARRINHO DE COMPRAS
#-----------------------


#------------------------------
# GERENCIAMENTO DA LOJA VIRTUAL
#------------------------------
def listar_produtos_site():
        """Esta listagem busca apenas os produtos cadastrados com pelo menos 1 item no estoque"""
        estoque = ativar_db(exec='SELECT * FROM produtos WHERE estoque > 0 ORDER BY nome')
        return estoque

def atualizar_estoque():
        carrinho = lista_carrinho()
        for item in carrinho:
            key = item[6]
            """buscando quantidade atual"""
            estoque = Produto.busca_produto(key)
            nova_qtd = estoque[0][3] - item[3] #nova quantidade é o estoque atuao - a quantidade comprada no carrinho.
            editar_db(exec='UPDATE produtos SET estoque = ? WHERE id = ?', id=key, estoque=nova_qtd)

            #conexao antiga
            """ conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
            cursor = conexao.cursor()
            cursor.execute('UPDATE produtos SET estoque = ? WHERE id = ?', (nova_qtd, key))
            conexao.commit()
            conexao.close() """
#----------------------------------
# FIM GERENCIAMENTO DA LOJA VIRTUAL
#----------------------------------

def registrar_venda():
    """esta função copia os nomes dos itens comprados no carrinho e adiciona a um tabela com data, hora e valor total da compra."""
    #listando itens do carrinho
    carrinho = lista_carrinho()
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
    cadastro['precotot'] = soma_carrinho()
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