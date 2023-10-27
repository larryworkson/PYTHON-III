import sqlite3
from formatacao import cor
from time import sleep
def delCadastro(buscaID):
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/dataBase.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM pessoas WHERE id = ?', (buscaID,))    
    cor('Cadastro deletado com sucesso!', 2)
    conexao.commit()
    conexao.close()
def addCadastro(n='sem nome', i='', c='desconhecida'):
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/dataBase.db') #estabelecendo conexão com arquivo dataBase.db
    cursor = conexao.cursor() #criando um cursor para navegar no BD.
    #CRIANDO A TABELA pessoas e definindo as colunas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cidade TEXT NOT NULL
                )
    ''')
    listaDados = []
    cadastro = {}
    cadastro['nome'] = n
    cadastro['idade'] = int(i)
    cadastro['cidade'] = c
    listaDados.append(cadastro)


    for cadastro in listaDados:
        cursor.execute('INSERT INTO pessoas (nome, idade, cidade) VALUES (:nome, :idade, :cidade)', cadastro)
    cor('Dados cadastrados com sucesso!', 2)
    #Salvando dados no BD e fechando conexão.
    conexao.commit()
    conexao.close()
def updateCadastro(dado):
   
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/dataBase.db')
    cursor = conexao.cursor()
    id = dado
    #dados armazenados no BD
    cursor.execute('SELECT nome, idade, cidade FROM pessoas WHERE id = ?', (id,))
    dados_atuais = cursor.fetchone()    
    cor(f'Atualizando dados do cadastro {dados_atuais[0]}...', 4)
    sleep(1)
    #solicitando novos dados
    novo_nome = input(f'Nome ({dados_atuais[0]}): ').strip().upper() or dados_atuais[0]
    nova_idade = input(f'Idade ({dados_atuais[1]}): ').strip() or dados_atuais[1]
    nova_cidade = input(f'Cidade ({dados_atuais[2]}): ').strip().upper() or dados_atuais[2]
    #enviando novos dados para o BD
    cursor.execute('UPDATE pessoas SET nome = ?, idade = ?, cidade = ? WHERE id = ?', (novo_nome, nova_idade, nova_cidade, id))
    
    #resposta da atualização
    if novo_nome or nova_idade or nova_cidade:        
        cor('Dados atualizados com sucesso!', 2)

    #salvando dados e fechando conexão
    conexao.commit()
    conexao.close()

def editCadastro():
    while True:
        print('[1] Deletar um cadastro')
        print('[2] Atualizar cadastro')
        print('[3] Adicionar cadastro')
        cor('[X] Voltar', 1)
        resp3 = str(input('Escolha: '))
        if resp3 == '1':
            buscaID = int(input('Digite o ID do cadastro que deseja deletar: '))
            delCadastro(buscaID)
        if resp3 == '2':
            buscaID = int(input('Digite o ID do cadastro que deseja atualizar: '))
            updateCadastro(buscaID)
        if resp3 == '3':
            n = input('Nome: ').upper()
            i = leiaInt('Idade: ').strip()
            c = input('Cidade: ').upper()
            addCadastro(n, i, c)

        if resp3 in 'Xx':
            break

def leiaInt(txt):
    while True:
        n = input(txt)
        if n.isnumeric():
            break
        else:
            print('\033[31mErro! Digite um número inteiro.\033[m')
    return n