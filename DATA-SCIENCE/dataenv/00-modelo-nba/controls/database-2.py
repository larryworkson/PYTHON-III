"""
- ajustar o try except para só criar DB se ele não existir
- pegar todos os jogadores da NBA de uma vez
- gerar salario para os que não forem encontrados
- 
"""
# como contar de 076 até 513?
from database import *
from search import *


def define_url():
    """cria a url com números dos jogadores no site da NBA"""
    n = 76
    urls = []
    while n < 99:
        if n < 99:
            url = f'https://www.nba.com/stats/player/2030{n}'
            urls.append(url)
        else:
            url = f'https://www.nba.com/stats/player/203{n}'
            urls.append(url)
        url = ''
        n += 1
    return urls

#enviando dados para o DB
def enviar_lista(lista):
    """verificando se o jogador já está no DB"""
    try: 
        nomes_db = ativar_db_2('SELECT nome FROM jogadores')
        jog_encontrado = False
        count2 = 0
        for i in nomes_db:
            if lista[count2][0] == i[0]:
                jog_encontrado = True
                print('\033[1;31mAlready registered player\033[m')
                break
            count2 += 1
        
        #adcionando jogadores no DB
        count = 0
        while True:
            if not jog_encontrado:
                nome = lista[count][0]
                ppg = lista[count][1]
                rpg = lista[count][2]
                apg = lista[count][3]
                pie = lista[count][4]
                xp = lista[count][5]
                sal = lista[count][6]
                enviar_db_2(exec='CREATE TABLE IF NOT EXISTS jogadores (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, ppg FLOAT NOT NULL, rpg FLOAT NOT NULL, apg FLOAT NOT NULL, pie FLOAT NOT NULL, xp FLOAT NOT NULL, sal FLOAT NOT NULL)', action='INSERT INTO jogadores (nome, ppg, rpg, apg, pie, xp, sal) VALUES (:nome, :ppg, :rpg, :apg, :pie, :xp, :sal)', nome=nome, ppg=ppg, rpg=rpg, apg=apg, pie=pie, xp=xp, sal=sal)
            if count == len(lista):
                break
            count += 1
    except:
        enviar_db_2(exec='CREATE TABLE IF NOT EXISTS jogadores (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, ppg FLOAT NOT NULL, rpg FLOAT NOT NULL, apg FLOAT NOT NULL, pie FLOAT NOT NULL, xp FLOAT NOT NULL, sal FLOAT NOT NULL)', action='INSERT INTO jogadores (nome, ppg, rpg, apg, pie, xp, sal) VALUES (:nome, :ppg, :rpg, :apg, :pie, :xp, :sal)', nome='0', ppg=0, rpg=0, apg=0, pie=0, xp=0, sal=0)
    

    

c = 0
lista_urls = define_url()
if lista_urls:
    print('Pesquisando...')
lista_jogadores = []
while c < 2:
    nome = verificar_nome(lista_urls[c])
    ppg = verificar_ppg(lista_urls[c])
    rpg = verificar_rpg(lista_urls[c])
    apg = verificar_apg(lista_urls[c])
    pie = verificar_pie(lista_urls[c])
    xp = verificar_xp(lista_urls[c])
    sal = buscando_sal_google(nome) #limite de 20 solicitações / dia
    jogador = [nome, ppg, rpg, apg, pie, xp, sal]
    print(f'{nome} \033[1;32mencontrado\033[m')
    lista_jogadores.append(jogador)
    jogador = []
    c += 1

""" for item in lista_jogadores:
    print(item) """

enviar_lista(lista_jogadores)
print(base_2())

#           python database-2.py


