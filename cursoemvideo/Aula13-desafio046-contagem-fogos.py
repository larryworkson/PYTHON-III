'''Mostre na tela uma contagem regressiva
para o estouro de fogos, indo de 10 até 0 com uma pausa de 1 seg'''
from time import sleep
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('🎆' * 7)
print('FELIZ ANO NOVO!')
print('🎆' * 7)