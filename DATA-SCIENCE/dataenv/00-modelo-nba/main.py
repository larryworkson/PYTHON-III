"""
Q1 = dados estatísticos dos jogadores
Q2 = adicionar no BD para servir de insumo para o modelo de ML.
Q3 = 
Q4 = o sistema deve buscar os dados de um jogador via API do GOOGLE e armazenar no BD, de forma que quando o modelo fizer uma previsão ele sempre faça com os dados atualizados.

Q5:
    1.0 criar função para ativar o BD (fazer em arquivo separado)
    2.0 instalar pacotes google e criar função via API google para buscar dados dos jogadores na web
    3.0 ligar o modelo ao banco de dados para utilizá-lo como base de treinamento.
    4.0 precisa UI?

"""


from controls.search import *
from controls.database import *
from controls.modelo import *

data = ativar_db(exec='SELECT * FROM jogadores ORDER BY nome')

#enviando dados para BD:
while True:
    
    menu = ['Sair', 'Casdastrar', 'Remover', 'Base de dados', 'Prever']
    for c in range(0, len(menu)):
        print(f'[{c}] - {menu[c]}')
    escolha = str(input('Escolha: '))
    if escolha == '1':
        while True:
            print(f'Média de erro: {media_erro():.2f}')
            print('-'*30)
            print('Digite N para finalizar.')
            print('-'*30)
            pesquisa = input(str('Pesquisa por: '))
            query = f'{pesquisa} nba stats'
            if pesquisa.lower() == 'n':
                break
            query = pesquisar(pesquisa)
            print('-'*30)
            print(query)
            """verificando se o jogador já está no DB"""
            nomes_db = ativar_db('SELECT nome FROM jogadores')
            jog_encontrado = False
            for i in nomes_db:
                if query[0] == i[0]:
                    jog_encontrado = True
                    print('Jogador já cadastrado')
                    break
            if not jog_encontrado:
                nome = query[0]
                ppg = query[1]
                rpg = query[2]
                apg = query[3]
                pie = query[4]
                xp = query[5]
                sal = query[6] 
                enviar_db(exec='CREATE TABLE IF NOT EXISTS jogadores (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, ppg FLOAT NOT NULL, rpg FLOAT NOT NULL, apg FLOAT NOT NULL, pie FLOAT NOT NULL, xp FLOAT NOT NULL, sal FLOAT NOT NULL)', action='INSERT INTO jogadores (nome, ppg, rpg, apg, pie, xp, sal) VALUES (:nome, :ppg, :rpg, :apg, :pie, :xp, :sal)', nome=nome, ppg=ppg, rpg=rpg, apg=apg, pie=pie, xp=xp, sal=sal)

    #removendo dados do db
    elif escolha == '2':
        id = int(input('Qual ID?: '))
        ativar_db(exec='DELETE FROM jogadores WHERE id = ?', id=id, commit=True)

    elif escolha == '3':
        print('-'*30)
        print('Base de dados')
        print('-'*30)
        print(base())
        print('-'*30)
        print('Correlação')
        print('-'*30)
        print(correlacao())
    
    elif escolha == '4':
        print('-'*30)
        print('Nova previsão')
        print('-'*30)
        ppg = float(input('PPG: '))
        rpg = float(input('RPG: '))
        apg = float(input('APG: '))
        pie = float(input('PIE: '))
        xp = int(input('XP: '))
        print(prever(ppg, rpg, apg, pie, xp))


        
    elif escolha == '0':
        break
# python main.py

"""
    - add try e except em todas as funções de busca.
    - a média de ERRO AINDA ESTÁ MUITO ALTA 
    - definir um contrato mínimo de um jogador (para não ter nº negativo)
    - o XP está tendo um peso bem algo
    - cadastrar pelo menos 1000 jogadores
"""