#escreva um programa que faça o computar pensar em um número inteiro entre 0 e 5
# peça para o usuário descobrir qual foi o numero escolhido pelo computador.
# o programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
import pygame
s = randint(0, 5)
u = int(input('Adivinhe qual número de 1 a 5 estou pensando: '))
print('Processando...')
sleep(3)
if u == s:
    print('O número que pensei foi {}. Parabéns, você acertou!'.format(s))
    pygame.mixer.init()
    pygame.mixer.music.load('win.mp3')
    pygame.mixer.music.play()
    input()
else:
    print('O número que pensei foi {}. Que pena, você errou!'.format(s))
    pygame.mixer.init()
    pygame.mixer.music.load('lose.mp3')
    pygame.mixer.music.play()
    input()




