from flask import Flask, request, render_template, jsonify

from flask_babel import format_currency, Babel
from static.functions import *
""" 

SISTEMA DE E-COMMERCE: MÓDULO ADMIN e MÓDULO LOJA (stie)

MÓDULO ADMIN:
q1: nome, preço, estoque, imagem, status (disponível / indisponível)
q2: gerar interface para cadastrar, editar e deletar produtos do BD.
q3: itens com quantidade 0 não devem aparecer no site. Itens comprados devem ser sacados do BD.
q4: interface que apresenta uma lista de todos os itens do estoque por categoria e geral.
q5:
    1.0 definir tipo de loja e 6 produtos de 3 categorias diferentes
        1.1 - categorias: TV, celular, notebook (pegar das americanas) Imagens pegar apenas a url
    2.0 gerenciamento de produtos
        2.1 criar class produtos 
        2.2 criar função de cadastro de produto no BD com os atributos (nome, preço, estoque, imagem e status)
        2.3 criar função de deletar produto
        2.4 criar função de editar produto
    3.0 interface admin
        3.1 criar interface HTML para cadastrar produto
        3.2 criar interface HTML para ver a lista de produtos e editar/deletar produtos.

        
MÓDULO LOJA (site)
q1: interface HTML para navegar nas categorias e lista de produtos
q2: site integrado com BD
q3: o usuário pode desistir de um item no carrinho.
q4: um site que permita comprar produtos, adicionando-os em um carrinho de compras.
q5:
    1.0 criar site
        1.1 página geral de produtos
        1.2 página das categorias
        1.3 página do carrinho
        1.4 página de agradecimento
    2.0 carrinho dinâmico
        2.1 mostrar o valor total da compra e quantidade total de itens.
        2.2 opção para aumentar a quantidade de itens
        2.3 botão checkout para finalizar a compra e debitar os itens do estoque.      
 """

"""INICILIAZAÇÃO DO APP"""
loja = Flask(__name__)
babel = Babel(loja) #configuração da lib de conversão de valores em moeda.
loja.config['BABEL_DEFAULT_LOCALE'] = 'pt_BR'



"""--------------------------------------------"""
"""PÁGINAS"""
"""--------------------------------------------"""

@loja.route('/')
def index():
    return render_template('index.html')


#PÁGINAS GERENCIAMENTO DE ESTOQUE"

@loja.route('/estoque.html')
def pag_estoque():
    estoque = Produto.listar_produtos()
    vendas = listar_vendas()
    totvendas = 0
    for i in vendas:
        totvendas += i[2]
    totpatrimonio = Produto.soma_patrimonio()
    totestoque = Produto.soma_estoque()
    return render_template('/estoque.html', produtos = estoque, patrimonio = totpatrimonio, totalestoque = totestoque, vendidos = vendas, somavendas = f'{totvendas:.2f}')

@loja.route('/vendas')
def get_data():
    data = ativar_db(exec='''SELECT data as mes, SUM(precotot) as total_vendas FROM vendas GROUP BY mes ORDER BY mes''')
    meses = [linha[0] for linha in data]
    tot_vendas = [linha[1] for linha in data]
    return jsonify({'meses': meses, 'tot_vendas': tot_vendas})


@loja.route('/cadastro.html')
def pag_cadastro():
    return render_template('/cadastro.html')

@loja.route('/editarproduto.html')
def pag_editar_produto(id):
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,))
    estoque = cursor.fetchone()
    conexao.close()
    return render_template('/editarproduto.html', id = id, nome = estoque[1], preco = estoque[2], estoque = estoque[3], img = estoque[4], categoria = estoque[5])

@loja.route('/del_item_venda/<id>')
def del_item_venda(id):
    """botão que remove um registro de venda"""
    del_venda(id)
    return pag_estoque()

#PÁGINAS DA LOJA VIRTUAL"

@loja.route('/site.html')
def pag_site():
    estoque = listar_produtos_site()
    produtos_formatados = []
    itens_carrinho = lista_carrinho()
    for item in estoque:        
        """criei uma cópia dos produtos que vem do estoque para poder converter o valor do produto em valor monetário"""
        produto_formato = list(item)
        produto_formato[2] = format_currency(item[2], 'BRL')
        produtos_formatados.append(produto_formato)
    return render_template('/site.html', produtos = produtos_formatados, qtd_itenscarrinho = len(itens_carrinho))

@loja.route('/agradecimento.html')
def pag_agradecimento():
    return render_template('/agradecimento.html')

@loja.route('/carrinho.html')
def pag_carrinho():
    produtos = lista_carrinho()
    soma = soma_carrinho()
    return render_template('/carrinho.html', itens = produtos, total = soma)

@loja.route('/produto.html/<int:produto_id>')
def pag_produto(produto_id):
    produto = Produto.busca_produto(produto_id)
    produtos_formatados = []
    for item in produto:
        """criei uma cópia das propriedades do produto converter o valor do produto em valor monetário"""
        produto_formato = list(item)
        produto_formato[2] = format_currency(item[2], 'BRL')
        produtos_formatados.append(produto_formato)
    return render_template('/produto.html', idprod = produto[0][0], nome = produto[0][1], cat = produto[0][5], preco = produto_formato[2], img = produto[0][4])

"""--------------------------------------------"""
"""FIM PÁGINAS"""
"""--------------------------------------------"""


"""--------------------------------------------"""
"""BOTÕES"""
"""--------------------------------------------"""
#BOTÕES DO GERENCIAMENTO DE ESTOQUE"

@loja.route('/cadastro.html/submit', methods=['POST'])
def enviar_form():
    """cadastra um produto na loja"""
    nome = request.form['nome']
    preco = request.form['preco']
    estoque = request.form['estoque']
    img = request.form['img']
    categoria = request.form['categoria']
    cadastro = Produto(nome, preco, estoque, img, categoria)
    cadastro.cadastrar()
    return render_template('/cadastro.html', resp = 'Produto cadastrado!')

@loja.route('/del_produto/<id>')
def del_produto(id):
    """deleta um produto do estoque"""
    Produto.deletar_produto(id)
    return pag_estoque()

@loja.route('/editar_produto/<id>')
def btn_editar_produto(id):
    return pag_editar_produto(id)

@loja.route('/editarproduto.html/submit', methods=['POST'])
def editar_produto():
    """editar os dados do produto no estoque"""
    id = request.form['id']
    novo_nome = request.form['nome']
    novo_preco = request.form['preco']
    novo_estoque = request.form['estoque']
    novo_img = request.form['img']
    novo_categoria = request.form['categoria']
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
    cursor = conexao.cursor()
    cursor.execute('UPDATE produtos SET nome = ?, preco = ?, estoque = ?, img = ?, categoria = ? WHERE id = ?', (novo_nome, novo_preco, novo_estoque, novo_img, novo_categoria, id))
    conexao.commit()
    conexao.close()
    return pag_estoque()

#BOTÕES DA LOJA VIRUTAL

@loja.route('/btn_comprar/<id>')
def btn_comprar(id):
    add_carrinho(id)
    return pag_carrinho()

@loja.route('/del_produto_carrinho/<id>')
def del_produto_carrinho(id):
    deletar_produto_carrinho(id)
    return pag_carrinho()

@loja.route('/del_todo_carrinho')
def del_todo_carrinho():
    produtos = lista_carrinho()
    for item in produtos:
        deletar_produto_carrinho(item[0])
    return pag_carrinho()


@loja.route('/aumenta_item/<id>')
def aumenta_item(id):
    incrementar_item(id)
    return pag_carrinho()
    
@loja.route('/diminui_item/<id>')
def diminui_item(id):
    decrementar_item(id)
    return pag_carrinho()

@loja.route('/finalizar_compra')
def finalizar_compra():
    registrar_venda()
    atualizar_estoque()
    carrinho = lista_carrinho()
    for i in carrinho:
        deletar_produto_carrinho(i[0])
    return pag_agradecimento()

"""--------------------------------------------"""
"""FIM BOTÕES"""
"""--------------------------------------------"""  


loja.run(debug=False)


"""


AJUSTES CRÍTICOS:
    - grafico de vendas (deixar com apenas os 3 últimos meses)
    - add lista de itens mais comprados.
    - organizar o código, tem vários itens na mesma classe. Seprar funções em arquivos. Ex: um arquivo só para gerenciar estoque. Outro só para gererenciar o carrinho, etc.
    - adicionar mascara monetária na página do produto e no carrinho. 

AJUSTES DE MELHORIA:
    - criar função de colocar produtos em promoção (com desconto) tipo black friday... tbm ver uma forma de por produtos em destaque
    - criar script que gera produtos recomendados na página do carrinho, baseados nas preferências do usuário
    
    
    - integrar com API dos correios para calcular o frete
    - criar layout moderno de loja (ver refs de ecommerce, criar logo etc.)

"""
