def ficha(nome='<desconhecido', gols=0):
    p = print(f'O jogador \033[1;33m{nome}\033[m fez \033[1;32m{gols}\033[m gols no campeonato.')


#programa principal
nome_jog = input('Nome jogador: ')
gols_jog = input('Gols: ')
if gols_jog.isnumeric():
    gols_jog = int(gols_jog)
else:
    gols_jog = 0
if nome_jog.strip() == '':
    ficha(gols=gols_jog)
else:
    ficha(nome_jog, gols_jog)