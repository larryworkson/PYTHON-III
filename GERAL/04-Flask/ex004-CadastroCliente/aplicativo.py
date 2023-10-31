from flask import Flask, request, render_template
import sqlite3

aplicativo = Flask(__name__) #iniciando aplicativo

ordem = ''

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
    cadastro['nome'] = n.title()
    cadastro['idade'] = i
    lista_dados.append(cadastro)
    for cadastro in lista_dados:
        cursor.execute('INSERT INTO clientes (nome, idade) VALUES (:nome, :idade)', cadastro)
    conexao.commit()
    conexao.close()

#renderiza a pagina de edição
@aplicativo.route('/abrirEdicao/<id>')
def abrirEdicao(id):
    """renderiza a página"""
    return lista_cliente(id)

@aplicativo.route('/editarcliente.html')
def lista_cliente(id):
    """mostra qual cadastro está sendo editado"""
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex004-CadastroCliente/database/base.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, idade FROM clientes WHERE id = ?', (id,))
    cliente = cursor.fetchone()
    conexao.close()
    return render_template('/editarCliente.html',id = id, nm = cliente[0].title(), idade = cliente[1])

@aplicativo.route('/editarCliente.html/submit', methods=['POST'])
def alterarBanco():
    """salva os novos dados pelo submit do form"""
    id = request.form['id']
    novo_nome = request.form['nome']
    nova_idade = request.form['idade']
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex004-CadastroCliente/database/base.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, idade FROM clientes WHERE id = ?', (id,))
    #atualizando bd
    cursor.execute('UPDATE clientes SET nome = ?, idade = ? WHERE id = ?', (novo_nome.title(), nova_idade, id))
    conexao.commit()
    conexao.close()
    return listar_clientes()


@aplicativo.route('/delCadastro/<buscaID>')
def delCadastro(buscaID):
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex004-CadastroCliente/database/base.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM clientes WHERE id = ?', (buscaID,))
    conexao.commit()
    conexao.close()
    return listar_clientes()

@aplicativo.route('/ordemIdade')
def ordemIdade():
    global ordem
    ordem = 'idade'
    return listar_clientes()

@aplicativo.route('/ordemNome')
def ordemNome():
    global ordem
    ordem = 'nome'
    return listar_clientes()

@aplicativo.route('/listaClientes.html')
def listar_clientes():
    conexao = sqlite3.connect('C:/Users//studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex004-CadastroCliente/database/base.db')
    cursor = conexao.cursor()
    if ordem == 'idade':
        cursor.execute('SELECT * FROM clientes ORDER BY idade')
    else:
        cursor.execute('SELECT * FROM clientes ORDER BY nome')
    clientes = cursor.fetchall()
    conexao.close()
    return render_template('listaClientes.html', clientes=clientes)

@aplicativo.route('/submit', methods=['POST'])
def enviar_form():
    nome = request.form['nome']
    idade = request.form['idade']
    enviarBanco(nome, idade)
    return render_template('index.html', status = 'Dados cadastrados com sucesso!')

aplicativo.run(debug=False)


"""
add relatórios por idade (menores de idade e maiores) e 
"""