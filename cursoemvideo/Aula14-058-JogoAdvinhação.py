'''from random import randint
from time import sleep
s = randint(1, 10)
tt = 1
u = int(input('Adivinhe qual número de 1 a 10 estou pensando: '))
print('Processando...')
sleep(2)
while u != s:
    if u != s:
        print('Que pena, você errou!'.format(s))
        if u < s:
            print(f'\033[1;33mO nº que pensei é MAIOR que {u}\033[m')
        elif u > s:
            print(f'\033[1;33mO nº que pensei é MENOR que {u}\033[m')
        tt = tt + 1
        u = int(input('Tente novamente: '))
print('\033[1;32mParabéns, você acertou!\033[m O número que pensei foi {}.'.format(s))
print('Você fez {} tentativas.'.format(tt))
print('FIM DE JOGO')'''
from random import randint
pc = randint(1,10)
print('Jogo de advinhação!')
print('Pensei em um número de 1 a 10:')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites = palpites + 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... tente novamente!')
        elif jogador > pc:
            print('Menos... tente novamente!')
print(f'Acertou com {palpites} palpites. Parabéns!')