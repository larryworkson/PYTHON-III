from flask import Flask, request, render_template

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


loja = Flask(__name__)

@loja.route('/')
def index():
    return render_template('index.html')


@loja.route('/estoque.html')
def pag_estoque():
    estoque = Produto.listar_produtos()
    totpatrimonio = Produto.soma_patrimonio()
    totestoque = Produto.soma_estoque()
    return render_template('/estoque.html', produtos = estoque, patrimonio = totpatrimonio, totalestoque = totestoque)

"""renderizar página de produtos"""
@loja.route('/cadastro.html')
def pag_cadastro():
    return render_template('/cadastro.html')

""" cadastrar produto na loja """
@loja.route('/cadastro.html/submit', methods=['POST'])
def enviar_form():
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
    Produto.deletar_produto(id)
    return pag_estoque()

@loja.route('/editarproduto.html')
def pag_editar_produto(id):
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex005-loja/database/base.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,))
    estoque = cursor.fetchone()
    conexao.close()
    return render_template('/editarproduto.html', id = id, nome = estoque[1], preco = estoque[2], estoque = estoque[3], img = estoque[4], categoria = estoque[5])

@loja.route('/editar_produto/<id>')
def btn_editar_produto(id):
    return pag_editar_produto(id)

@loja.route('/editarproduto.html/submit', methods=['POST'])
def editar_produto():
    """editar os dados do produto"""
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

@loja.route('/site.html')
def pag_site():
    estoque = Produto.listar_produtos_site()
    return render_template('/site.html', produtos = estoque)

@loja.route('/btn_comprar/<id>')
def btn_comprar(id):
    Produto.add_carrinho(id)
    return pag_carrinho()

@loja.route('/carrinho.html')
def pag_carrinho():
    produtos = Produto.lista_carrinho()
    soma = Produto.soma_carrinho()
    return render_template('/carrinho.html', itens = produtos, total = soma)

@loja.route('/produto.html/<int:produto_id>')
def pag_produto(produto_id):
    produto = Produto.busca_produto(produto_id)
    return render_template('/produto.html', idprod = produto[0][0], nome = produto[0][1], cat = produto[0][5], preco = produto[0][2], img = produto[0][4])

@loja.route('/del_produto_carrinho/<id>')
def del_produto_carrinho(id):
    Produto.deletar_produto_carrinho(id)
    return pag_carrinho()

@loja.route('/aumenta_item/<id>')
def aumenta_item(id):
    Produto.incrementar_item(id)
    return pag_carrinho()
    
@loja.route('/diminui_item/<id>')
def diminui_item(id):
    Produto.decrementar_item(id)
    return pag_carrinho()

@loja.route('/finalizar_compra')
def finalizar_compra():
    Produto.atualizar_estoque()
    carrinho = Produto.lista_carrinho()
    for i in carrinho:
        Produto.deletar_produto_carrinho(i[0])
    return pag_site()

    


loja.run(debug=False)


"""


adicionar regra: o produto só aperece na lista se o estoque dele for > que 0.

criar página de notificações (quando produto tiver menos de 10 unidades gera notificação ao admin)
Notifica quando houver uma nova venda.
Mostrar relatório com dados da última venda, valor, dia e horário.

adicionar total de itens no estoque, por categoria, total do patrimônio (soma dos valores de todos os produtos).

Adicionar máscara para o valor monetário

criar script que gera produtos recomendados, baseados nas preferências do usuário
na loja, integrar com API dos correios para calcular o frete

"""
