from flask import Flask, request, render_template
import sqlite3

aplicativo = Flask(__name__) #iniciando aplicativo

@aplicativo.route('/')
def pag_inicial():
    return render_template('index.html')

def enviarBanco(n='sem nome', i=''):
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex004-CadastroCliente/database/base.db') #estabelece conexão com banco
    cursor = conexao.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes (
                   id INTEGER PRIMARY KEY, nome TEXT NOT NULL, idade INTEGER NOT NULL)''')
    lista_dados = []
    cadastro = {}
    cadastro['nome'] = n
    cadastro['idade'] = i
    lista_dados.append(cadastro)
    for cadastro in lista_dados:
        cursor.execute('INSERT INTO clientes (nome, idade) VALUES (:nome, :idade)', cadastro)
    conexao.commit()
    conexao.close()

@aplicativo.route('/delCadastro/<buscaID>')
def delCadastro(buscaID):
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex004-CadastroCliente/database/base.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM clientes WHERE id = ?', (buscaID,))
    conexao.commit()
    conexao.close()
    return listar_clientes()

@aplicativo.route('/listaClientes.html')
def listar_clientes():
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex004-CadastroCliente/database/base.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conexao.close()
    return render_template('listaClientes.html', clientes=clientes)

@aplicativo.route('/submit', methods=['POST'])
def enviar_form():
    nome = request.form['nome']
    idade = request.form['idade']
    enviarBanco(nome, idade)
    return render_template('index.html', status = 'Dados cadastrados com sucesso!')

aplicativo.run()


"""
ver como atualizar um cadastro
add relatórios
"""