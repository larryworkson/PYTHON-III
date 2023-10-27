'''
programa que você escolhe um time e enfrenta 3 outros times em uma tabela.
cada vitória o time soma 3 pontos e 1 ponto ao empatar.
no final mostra uma tabela com o ranking dos times por pontos.

4 times = [ [{'nome': 'A', 'gols': 0, 'vit': 0, 'pts': 0}], [{'nome': 'B', 'gols': 0, 'vit': 0, 'pts': 0}] ]
print times
jogador escolhe um time
pc gera gols
pc gera confrontos (todos contra todos)
quando time ganha, ele recebe += de vitória ('vit')
mostrar resultado das partidas
mostrar ranking por pontos

'''
from random import randint
from time import sleep
# criar random choice para defirnir os nomes dos times aleatóriamente
times = [
    [{'nome': '\033[1;35mCorinthians\033[m', 'gols': 0, 'vit': 0, 'pts': 0}],
    [{'nome': '\033[1;32mPalmeiras\033[m', 'gols': 0, 'vit': 0, 'pts': 0}],
    [{'nome': '\033[1mSantos\033[m', 'gols': 0, 'vit': 0, 'pts': 0}],
    [{'nome': '\033[1;31mFlamengo\033[m', 'gols': 0, 'vit': 0, 'pts': 0}]
]
jogador = []

print('SELECIONE UM TIME')
for pos, time in enumerate(times):
    print(f'{pos} > {time[0]["nome"]} | V:{time[0]["vit"]}')
escolha = int(input('\033[1;33mSua escolha: \033[m'))
jogador.append(times[escolha])
print(f'Você escolheu o {jogador[0][0]["nome"]}')
print('*'*20)
while True:
    #gerando gols
    for t in times:
        t[0]['gols'] = randint(0,4)
    print('- '*40)
    # Definindo o resultado dos jogos
    # 1º round: time1 vs time2 e time3 vs time4
    # 2º round: time1 vs time3 e time2 vs time4
    # 3º round: time1 vs time4 e time2 vs time3
    print(' < < < CONFRONTOS > > >')
    print('\033[1;31m1ª RODADA\033[m')
    print(f'{times[0][0]["nome"]} {times[0][0]["gols"]} x {times[1][0]["gols"]} {times[1][0]["nome"]}', end='       ')
    #VITÓRIA TIME 1
    if times[0][0]['gols'] > times[1][0]['gols']:
        times[0][0]['vit'] += 1
        times[0][0]['pts'] += 3
        print(f'>>> {times[0][0]["nome"]} venceu!', end='')
    
    #VITÓRIA TIME 2
    elif times[1][0]['gols'] > times[0][0]['gols']:
        times[1][0]['vit'] += 1
        times[1][0]['pts'] += 3
        print(f'>>> {times[1][0]["nome"]} venceu!', end='')
    
    #EMPATE
    elif times[1][0]['gols'] == times[0][0]['gols']:
        times[0][0]['pts'] += 1
        times[1][0]['pts'] += 1
        print('>>> Empate', end='')
    print()

    print(f'{times[2][0]["nome"]} {times[2][0]["gols"]} x {times[3][0]["gols"]} {times[3][0]["nome"]}', end='       ')
    # VITÓRIA TIME 3
    if times[2][0]['gols'] > times[3][0]['gols']:
        times[2][0]['vit'] += 1
        times[2][0]['pts'] += 3
        print(f'>>> {times[2][0]["nome"]} venceu!', end='')

    #VITÓRIA TIME 4
    elif times[3][0]['gols'] > times[2][0]['gols']:
        times[3][0]['vit'] += 1
        times[3][0]['pts'] += 3
        print(f'>>> {times[3][0]["nome"]} venceu!', end='')
    
    #EMPATE
    elif times[3][0]['gols'] == times[2][0]['gols']:
        times[3][0]['pts'] += 1
        times[2][0]['pts'] += 1
        print('>>> Empate', end='')
    print('\n')

    #RANKING
    print('- - '*30)
    print('TABELA DE PONTOS')
    for pos, time in enumerate(times):
        print(f'{pos} > {time[0]["nome"]} | PTS:{time[0]["pts"]} | V: {time[0]["vit"]}')
 
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break

for k, v in enumerate(time):
    print(f'\033[1;32m{k:>3}\033[m', end='')
    for jog in v.values(): #pega somente os valores dos items do dicionario
        print(f' {str(jog):<15}', end='')