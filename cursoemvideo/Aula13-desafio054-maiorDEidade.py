'''idade >= 21 = maior de idade
idade < 21 = menor de idade'''
from datetime import date
maior = 0
menor = 0
for c in range(1,8):
    nsc = int(input('{}º ano de nascimento: '.format(c)))
    idade = date.today().year - nsc
    if idade >= 21:
        maior = maior + 1
    elif idade < 21:
        menor = menor + 1
print('🍹 Total de MAIORES:  {}'.format(maior))
print('👶 Total de menores : {}'.format(menor))