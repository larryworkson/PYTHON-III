'''programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
até 9 ANOS = MIRIM
até 14 ANOS = INFANTIL
até 19 ANOS = JUNIOR
Até 20 ANOS = SÊNIOR
Acima de 20 ANOS = MASTER'''
from datetime import datetime
anoa = 2017 # datetime.now().year
nsc = int(input('Digie o ano do seu nascimento: '))
idade = anoa - nsc
if idade <= 9:
    print('Você tem {} anos'.format(idade))
    print('Classificação: MIRIM')
elif idade > 9 and  idade <= 14:
    print('Você tem {} anos'.format(idade))
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Você tem {} anos'.format(idade))
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Você tem {} anos'.format(idade))
    print('Classificação: SÊNIOR')
else:
    print('Você tem {} anos'.format(idade))
    print('Classificação: MASTER')