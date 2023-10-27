""" mercado de ações
Cadastrar empresas com valor de mercado / 1000. Ex: a empresa vale 100000, casa ação custa: 100. 
Rodar um índice pelo Randint de -50 a 50. O índice gerado deve acrescentar ou subtrair do valor da empresa em %. Ex: se empresa vale 100000 e o indice dela deu -50, ela perde 50% do seu valor 

Q1: dados da empresa: nome, valor, ações = 1000, quantidade ações vendidas e os dividendos que é 30% do valor da empresa. Cada investidor recebe na conta os dividendos de acordo com a quantidade de ações que tem. E um índice aleatório entre -50 e 50.
Q2: dividir o valor da empresa pelo nº de ações para obter o custo da ação. Toda vez que uma ação é comprada, é adicionada no cadastro do investidor 1 ação e adicionada no número de ações vendidas daquela empresa 1.

O cadastro do investidor deve receber o nome da empresa, a quantidade de ações compradas, saldo, preço pago e quanto aquela ação está valendo com a cotação atual. Ter uma opção de vender a ação pela cotação atual.

Q3: 

"""
import sqlite3
import locale
from random import randint

c = ('\033[m', '\033[31m', '\033[32m', '\033[33m', '\033[2;34m', '\033[35m')

def cor(txt, color=0):
    print(c[color], end='')
    print(txt)
    print(c[0], end='')

def moeda(v):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(v, grouping=True)

def titulo(txt, color=0):
    n = len(txt)
    print('-'*n)
    cor(f'{txt:^{n}}', color)
    print('-'*n)

def addEmpresa(n, v):
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/bolsa-valores/bolsa.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS mercado (id INTEGER PRIMARY KEY, nome TEXT, valor FLOAT, acoes INTEGER, qtdacoesvendidas INTEGER, dividendo FLOAT)''')
    listaDados = []
    cadastro = {}
    cadastro['nome'] = n
    cadastro['valor'] = v
    cadastro['acoes'] = 1000
    cadastro['qtdacoesvendidas'] = 0
    cadastro['dividendo'] = v / (30/100 * v)
    listaDados.append(cadastro)
    for cadastro in listaDados:
        cursor.execute('INSERT INTO mercado (nome, valor, acoes, qtdacoesvendidas, dividendo) VALUES (:nome, :valor, :acoes, :qtdacoesvendidas, :dividendo)', cadastro)
    cor('Dados cadastrados com sucesso!', 2)
    conexao.commit()
    conexao.close()

def delEmpresa(buscaID):
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/bolsa-valores/bolsa.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM mercado WHERE id = ?', (buscaID,))
    cor('Cadastro deletado com sucesso!', 2)
    conexao.commit()
    conexao.close()


#programa principal
while True:
    cor('[A] Avançar', 3)
    cor('[2] Mercado', 2)
    cor('[X] Sair', 1)
    resp = str(input('Escolha: '))
    if resp in 'Xx':
        break
    if resp in 'Aa':
        indice = randint(-5, 5)
        cor(f'Indice: {indice}%', 3)
        conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/bolsa-valores/bolsa.db')
        cursor = conexao.cursor()
        #puxando dados armazenados
        cursor.execute('SELECT nome, valor, dividendo FROM mercado')
        dados_atuais = cursor.fetchall()
       #dividendos dados_atuais[cont][2]

        cont = 0
        for r in dados_atuais:
            nome = dados_atuais[cont][0]
            novo_valor = dados_atuais[cont][1] + (dados_atuais[cont][1] / 100 * indice)
            div = dados_atuais[cont][2] + 30 / 100 * novo_valor
            cursor.execute('UPDATE mercado SET valor = ?, dividendo = ? WHERE nome = ?', (novo_valor, div, nome))
           
            cont += 1            
        cor('Dados atualizados', 2)
        conexao.commit()
        conexao.close()
        
    if resp == '2':
        conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/bolsa-valores/bolsa.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM mercado ORDER BY valor')
        resultados = cursor.fetchall()
        titulo('~~~~~~~~~~~~~~~~~~~~ MERCADO DE AÇÕES ~~~~~~~~~~~~~~~~~~~~', 2)
        for r in resultados:
            print(f'{r["id"]:<3} | {r["nome"]:<15} | {moeda(r["valor"]):<25} | {moeda(r["dividendo"]):>20}')
        conexao.close()
        while True:
            cor('[1] Excluir empresa', 4)
            cor('[2] Adicionar empresa', 5)
            cor('[X] Voltar', 1)
            resp2 = str(input('Escolha: '))
            if resp2 in 'Xx':
                break
            if resp2 == '2':
                nome = str(input('Nome: '))
                valor = int(input('Valor: '))
                addEmpresa(nome, valor)
            if resp2 == '1':
                id = int(input('Digite o ID da empresa: '))
                delEmpresa(id)
            

#VER PORQUE O ÍNDICE NÃO ESTÁ ATUALIZANDO O VALOR DA EMPRESSS
""" histórico de compras mesma lógica, add uma coluna no cadastro do investidor com uma lista com valor da compra, quantidade de ações e o nome da empresa """