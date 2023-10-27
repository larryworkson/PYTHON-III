from time import sleep
dataBase = []
pessoa = []
dado = []

#MENU GERAL
while True:
    print('=-=' * 20)
    print(' '*10,'SISTEMA DE CADASTROS', ' '*10)
    print('=-=' * 20)
    print('''Escolha uma opção:\n[1] Cadastrar uma pessoa\n[2] Consultar cadastros\n\033[31m[X] Sair do sistema\033[m''')
    menu = str(input('Escolher: '))

    if menu in 'Xx':
        print('*** SAINDO DO SISTEMA ***')
        sleep(1)
        break        
    #CADASTRP DE DADOS
    elif menu == '1':
        print('---- CADASTRAMENTO ----')
        while True:
            dado.append(str(input('Nome: ').upper()))
            pessoa.append(dado[:])
            dado.clear()
            dado.append(int(input('Idade: ')))
            pessoa.append(dado[:])
            dado.clear()
            dado.append(str(input('Cidade: ').upper()))
            pessoa.append(dado[:])
            dado.clear()
            dataBase.append(pessoa[:])
            pessoa.clear()
            print('>>> Dados cadastrados com sucesso!')
            resp = str(input('Deseja outro? [S/N]: '))
            if resp in 'Nn':
                break
    elif menu == '2' and len(dataBase) == 0:
        print('\033[31mNENHUM CADASTRO REGISTRADO. Cadastre uma pessoa [1].\033[m')
        menu = '1'
    
    #CONSULTAS DE DADOS
    elif menu == '2':
        while True:
            print('---- CONSULTA DE CADASTROS ----')
            print('''Selecione uma opção:\n[1] Ver todos os cadastros\n[2] Consulta por nome\n[3] Consulta por cidade\n[4] Consulta por idade\n[X] Para voltar''')
            resp = str(input('Escolher: '))
            if resp in 'Xx':
                break
            elif resp == '1':
                print('\033[32m- - \033[m'*10)
                print('*** CADASTROS NO SISTEMA ***')
                print(f'\033[32m{"Nome":<15} {"Idade":<7}{"Cidade":<20}\033[m')
                for p in dataBase:
                    print(f'{p[0][0]:<16}{p[1][0]:<7}{p[2][0]:<22}')
                print('\033[32m- - \033[m'*10)
            elif resp == '2':
                print('. ' *10)
                print('CONSTULTA POR NOME')
                print('. ' *10)
                pesqNome = str(input('Digite o nome: ').upper())
                encontrado = False
                encontrados = [] #lista de clientes encontrados com o mesmo nome
                print('\033[34mResultado da pesquisa:')
                print('\033[34m- \033[m'*10)
                for p in range(0, len(dataBase)):
                    if pesqNome in dataBase[p][0]:                        
                        encontrado = True
                        encontrados.append(dataBase[p])
                        print(f'\033[32m{"Nome":<15} {"Idade":<7}{"Cidade":<20}\033[m')
                        for cadastro in encontrados:
                            print(f'\033[35m{cadastro[0][0]:<16}\033[m{cadastro[1][0]:<7}{cadastro[2][0]:<22}')                        
                        encontrados.clear()
                        print('\033[34m- \033[m'*10)
                    if encontrado == False: #caso o laço que pesquisa o nome não encontre nenhum cadastro
                        print('\033[31mNenhum cadastro encontrado!\033[m')
                        break
                while True:
                    print('''Escolha uma opção:\n[1] Editar cadastro (em desenvolvimento)\n[X] Voltar ''')
                    resp = str(input('Escolha: '))
                    if resp in 'Xx':
                        break                
            elif resp == '3':
                print('. ' *10)
                print('CONSTULTA POR CIDADE')
                print('. ' *10)
                pesqCidade = str(input('Digite a cidade: ').upper())
                encontrado = False
                encontrados = []
                print('\033[34mResultado da pesquisa:')
                print('- \033[m'*10)
                for p in range(0, len(dataBase)):
                    if pesqCidade in dataBase[p][2]:                        
                        encontrado = True
                        encontrados.append(dataBase[p])
                        for cadastro in encontrados:
                            print(f'Nome: {cadastro[0]} | Idade: {cadastro[1]} | Cidade: \033[35m{cadastro[2]}\033[m')                        
                        encontrados.clear()
                    if encontrado == False: #caso o laço que pesquisa o nome não encontre nenhum cadastro
                        print('\033[31mNenhum cadastro encontrado!\033[m')
                        break
                while True:
                    print('''Opções:\n[1] Editar cadastro (em desenvolvimento)\n[X] Voltar''')
                    resp = str(input('Sua escolha: '))
                    if resp in '1Xx':
                        break                
            elif resp == '4':
                print('. ' *10)
                print('CONSTULTA POR IDADE')
                print('. ' *10)
                pesqIdade1 = int(input('Idade mínima: '))
                pesqIdade2 = int(input('Idade máxima: '))
                encontrado = False
                encontrados = []
                print('\033[34mResultado da pesquisa:')
                print('- \033[m'*10)
                for p in range(0, len(dataBase)):                    
                    if pesqIdade1 <= dataBase[p][1][0] and pesqIdade2 >= dataBase[p][1][0]:
                        encontrado = True
                        encontrados.append(dataBase[p])
                        for cadastro in encontrados:
                            print(f'Nome: {cadastro[0]} | Idade: \033[35m{cadastro[1]}\033[m | Cidade: {cadastro[2]}')
                        encontrados.clear()
                    if encontrado == False:
                        print('\033[31mNenhum cadastro encontrado!\033[m')
                        break
                while True:
                    print('Opções:\n[1] Editar cadastro (em breve)\n[X] Voltar')                    
                    resp = str(input('Sua escolha: '))
                    if resp in '1Xx':
                        break
                

#ERRO PESQUISA POR NOME/CIDADE busca apenas o 1º item da lista >> a última mudança foi a formatação da lista de cadastros na opção (ver todos os cadastros e buscar pelo nome)
# criar opção de editar um cadastro        