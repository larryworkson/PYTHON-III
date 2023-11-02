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
 """


loja = Flask(__name__)

@loja.route('/')
def index():
    return render_template('index.html')

""" teste """
@loja.route('/teste')
def teste():
    produto = Produto('Celular', 5, 0, 'img', 'disponível')
    return render_template('/index.html', resp = produto.descricao_produto())

@loja.route('/estoque.html')
def pag_estoque():
    estoque = Produto.listar_produtos()
    return render_template('/estoque.html', produtos = estoque)

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
    status = request.form['status']
    Produto.cadastrar(nome, preco, estoque, img, status)
    return render_template('/cadastro.html', resp = 'Produto cadastrado!')

@loja.route('/del_produto/<id>')
def del_produto(id):
    Produto.deletar_produto(id)
    return pag_estoque()


loja.run(debug=False)


