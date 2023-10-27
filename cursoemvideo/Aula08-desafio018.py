#faça um programa que leia um ângulo qualquer e
#mostre na tela o valor do seno, consseno e tangente desse ângulo
import math
an = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tang = math.tan(math.radians(an))
print('O ângulo {} tem o SENO de {:.2f}º'.format(an, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}º'.format(an, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}º'.format(an, tang))

