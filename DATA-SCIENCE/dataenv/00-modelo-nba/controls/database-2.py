"""
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
    while n < 85:
        n += 1
        url = f'https://www.nba.com/stats/player/2030{n}'
        urls.append(url)
        url = ''
    return urls

c = 0
lista_urls = define_url()
while c < 9:
    nome = verificar_nome(lista_urls[c])
    ppg = verificar_ppg(lista_urls[c])
    rpg = verificar_rpg(lista_urls[c])
    apg = verificar_apg(lista_urls[c])
    pie = verificar_pie(lista_urls[c])
    print(f'''{nome} | {ppg} | {rpg}''')
    c += 1



#           python database-2.py


