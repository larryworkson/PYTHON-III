from random import randint
from time import sleep
jogos = [] #iniciando a lista
geral = []
print('-'*30)
print('     JOGA NA MEGA SENA     ')
print('-'*30)
quantjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*10, end='')
print(f' SORTEANDO {quantjogos} JOGOS ', end='')
print('-='*10)
sleep(1)

j = 0
while j < quantjogos:
    palpites = 0
    #laço para gerar 6 nº
    while palpites < 6:
        num = randint(1, 60)
        if num in jogos: #verificando se o nº já existe na lista para não repetir
            jogos.remove(num)
            palpites -= 1 #caso o nº já exista na lista, ele é removido, logo é necessário que o loop de palpites rode mais uma vez para substituir o nº removido.
        else:
            jogos.append(num)
            palpites += 1
    print(f'Jogo {j + 1}: {sorted(jogos)}')
    jogos.clear()
    j += 1 
    sleep(1)
sleep(1)
print(f'=-'*3, end='')
print(' BOA SORTE! ', end='')
print(f'=-'*3)

'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''