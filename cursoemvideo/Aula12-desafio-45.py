'''crie um jogo qe JOKEMPO entre PC e usuário'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
u = int(input('Qual sua jogada? '))

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')

print('\033[31mPC jogou {}\033[m'.format(itens[pc]))
print('\033[32mVocê jogou {}\033[m'.format(itens[u]))

if pc == 0:
    if u == 0:
        print('Empate, jogue novamente!')
    elif u == 1:
        print('Jogador venceu!')
    elif u == 2:
        print('PC venceu!')
    else:
        print('Opção inválida. Tente novamente!')
elif pc == 1:
    if u == 0:
        print('PC venceu!')
    elif u == 1:
        print('Empate, tente novamente!')
    elif u == 2:
        print('Jogador venceu!')
    else:
        print('Opção inválida. Tente novamente!')

elif pc == 2:
    if u == 0:
        print('Jogador venceu!')
    elif u == 1:
        print('PC venceu!')
    elif u == 2:
        print('Empate, tente novamente!')
    else:
        print('Opção inválida. Tente novamente!')