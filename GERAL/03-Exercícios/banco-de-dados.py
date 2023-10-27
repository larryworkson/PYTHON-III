import sqlite3
from time import sleep
from cadastros import addCadastro, editCadastro, leiaInt
from formatacao import titulo, cor

def relatorios():
    #CIDADES / CADASTROS
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/dataBase.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT cidade, COUNT(*) FROM pessoas GROUP BY cidade')
    resultados = cursor.fetchall()
    titulo('RELATÓRIOS')
    cor('PESSOAS POR CIDADE',3)
    for row in resultados:
        cidade, total_cadastros = row
        print(f'{cidade:<15} | {total_cadastros}')
    conexao.close()
    #IDADE / CADASTROS
    print()
    cor('PESSOAS POR IDADE', 3)
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/dataBase.db')
    cursor = conexao.cursor()
    #0 A 15
    query_0_15 = 'SELECT COUNT (*) FROM pessoas WHERE idade >= 0 AND idade <= 15'
    result1 = cursor.execute(query_0_15).fetchone()
    tot_0_15 = result1[0]
    print(f'Pessoas entre 0 a 15 anos: {tot_0_15}')

    #16 a 21
    query_16_21 = 'SELECT COUNT (*) FROM pessoas WHERE idade >= 16 AND idade <=21'
    result2 = cursor.execute(query_16_21).fetchone()
    tot_16_21 = result2[0]
    print(f'Pessoas entre 16 e 21 anos: {tot_16_21}')
    
    #22 a 35
    query_22_35 = 'SELECT COUNT (*) FROM pessoas WHERE idade >= 22 AND idade <= 35'
    result3 = cursor.execute(query_22_35).fetchone()
    tot_22_35 = result3[0]
    print(f'Pessoas entre 22 e 35 anos: {tot_22_35}')

    #36 a 55
    query_36_55 = 'SELECT COUNT (*) FROM pessoas WHERE idade >= 36 AND idade <= 55'
    result4 = cursor.execute(query_36_55).fetchone()
    tot_36_55 = result4[0]
    print(f'Pessoas entre 36 a 55 anos: {tot_36_55}')

    #56 a 65
    query_56_65 = 'SELECT COUNT (*) FROM pessoas WHERE idade >= 56 AND idade <= 65'
    result5 = cursor.execute(query_56_65).fetchone()
    tot_56_65 = result5[0]
    print(f'Pessoas entre 56 a 65 anos {tot_56_65}')

    #+65
    query_mais65 = 'SELECT COUNT (*) FROM pessoas WHERE idade > 65'
    result6 = cursor.execute(query_mais65).fetchone()
    tot_65 = result6[0]
    print(f'Pessoas com mais de 65 anos {tot_65}')
    
    conexao.close()


while True:    
    titulo('SISTEMA DE CADASTROS')
    print('[1] Consultar cadastros')
    print('[2] Cadastrar pessoa')
    cor('[X] Sair', 1)
    resp = str(input(('Sua escolha: ')))
    
    #consulta de cadastros
    if resp == '1':
        while True:
            titulo('CONSULTA DE CADASTROS')
            print('[1] Consultar toda base')
            print('[2] Pesquisar por nome')
            print('[3] Pesquisar por cidade')
            print('[4] Pesquisar por idade')
            print('[5] Relatórios')
            cor('[X] Voltar', 1)
            resp2 = str(input(('Resposta: ')))
            if resp2 == '1':
                # consultando cadastros
                conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/dataBase.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) #configurando o connect() para puxar detectar os dados pelo tipo deles e puxar as colunas pelo nome
                conexao.row_factory = sqlite3.Row
                cursor = conexao.cursor()

                cursor.execute('SELECT * FROM pessoas') #selecinando TODOS(*) os dados da tabela pessoas
                resultados = cursor.fetchall() #pegando TODOS os items encontrados pelo cursor

                #apresentando os itens:
                for r in resultados:
                    print(f'ID: {r["id"]:<10} | {r["nome"]:<25} | {r["idade"]:<10} | {r["cidade"]:<10}')
                conexao.close()
                
                #atualização de cadastro.
                editCadastro()
            
            if resp2 == '2':
                conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/dataBase.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
                conexao.row_factory = sqlite3.Row
                cursor = conexao.cursor()
                buscaNome = str(input('Buscar pelo nome: ').upper().strip())
                cursor.execute('SELECT * FROM pessoas WHERE nome LIKE ?', ('%' + buscaNome + '%',)) #os símbolos de % concatenados a var fazem com que o operador LIKE busque cadastros que contém o que o usuário digitou.
                resultados = cursor.fetchall()
                if len(resultados) == 0:                    
                    cor('Nenhum resultado encontrado.', 1)
                else:
                    for r in resultados:
                        print(f'ID: {r["id"]:<10} | {r["nome"]:<25} | {r["idade"]:<10} | {r["cidade"]:<10}')
                    conexao.commit()
                    conexao.close()

                    #remoção do cadastro.
                    editCadastro()
            
            if resp2 == '3':                
                conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/dataBase.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
                conexao.row_factory = sqlite3.Row
                cursor = conexao.cursor()
                buscaCidade = str(input('Buscar pelo cidade: ').upper())
                cursor.execute('SELECT * FROM pessoas WHERE cidade LIKE ?', ('%' + buscaCidade + '%',)) #os símbolos de % concatenados a var fazem com que o operador LIKE busque cadastros que contém o que o usuário digitou.
                resultados = cursor.fetchall()
                if len(resultados) == 0:
                    cor('Nenhum cadastro encontrado!', 1)
                else:
                    for r in resultados:
                        print(f'ID: {r["id"]:<10} | {r["nome"]:<25} | {r["idade"]:<10} | {r["cidade"]:<10}')
                    conexao.commit()
                    conexao.close()
                    #remoção do cadastro.
                    editCadastro()

            if resp2 == '4':
                conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/GERAL/03-Exercícios/dataBase.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
                conexao.row_factory = sqlite3.Row
                cursor = conexao.cursor()
                buscaIdadeMin = int(input('Idade mínima: '))
                buscaIdadeMax = int(input('Idade máxima: '))
                cursor.execute('SELECT * FROM pessoas WHERE idade BETWEEN ? AND ? ORDER BY idade DESC', (buscaIdadeMin, buscaIdadeMax))
                resultados = cursor.fetchall()
                print(f'Quantidade de registros {len(resultados)}')
                for r in resultados:
                    print(f'ID: {r["id"]:<10} | {r["nome"]:<25} | {r["idade"]:<10} | {r["cidade"]:<10}')
                editCadastro()
                conexao.commit()
                conexao.close()
            
            if resp2 == '5':
                relatorios()
                
            if resp2 in 'Xx':
                break

    #cadastro de pessoas
    titulo('CADASTRAMENTO')
    if resp == '2':
        n = input('Nome: ').upper()
        i = leiaInt('Idade: ').strip()
        c = input('Cidade: ').upper()
        addCadastro(n, i, c)
        
    if resp in 'Xx':
        cor('Saindo do sistema...', 1)
        sleep(1)
        break

#nos relatórios mostrar cidads com parâmetro <desconhecida> ou sem nome