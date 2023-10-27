#crie um programa que leia um numero real qualquer e mostre
#na tela a sua proporção inteira. ex: digite 6,129, aparece 6.
from math import floor
num = float(input('Digite um número: '))
print('O número {} tem a parte intera: {}.'.format(num, floor(num)))

