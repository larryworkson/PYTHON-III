from random import randint
from time import sleep

def sorteia():
    print('Sorteando os 5 valores: ', end='')
    for c in range(1, 6):
        n = randint(0,9)
        lista.append(n)
    for item in lista:
        print(f'{item} ', end='', flush=True)
        sleep(0.4)
    print('>> PRONTO!')

def somaPar():
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    print(f'Somando os valores pares de {lista} temos \033[32m{s}\033[m.')

lista = []
sorteia()
somaPar()