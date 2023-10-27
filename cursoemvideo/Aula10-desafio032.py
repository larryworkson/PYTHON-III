#faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
a = int(input('Digite um ano com os 4 dígitos: '))
if a == 0:
    a = date.today().year #pega o ano da máquina
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} é um ano BISSEXTO'.format(a))

else:
    print('O ano de {} NÃO é um ano BISSEXTO'.format(a))