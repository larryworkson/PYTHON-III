'''Faça um programa que leia o ANO de nascimento de um jovem e informe:
Se ele ainda vai se alistar e quantos anos faltam para o alistamento
Se está na hora de se alistar
Se já passou o tempo e quantos anos ele está atrasado'''
from datetime import datetime
ano = datetime.now().year
nsc = int(input('Digite seu ano de nascimento (xxxx): '))
idade = ano - nsc
print('Você está com {} anos.'.format(idade))
if idade < 18:
    print('Você \033[1;32mainda não\033[m está na idade para servir.')
    print('Faltam \033[1;32m{} ano(s)\033[m para seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}'.format(nsc + 18))
elif idade == 18:
    print('\033[1;34mEste é o ano do seu alistamento.')
else:
    print('Você \033[1;31mjá passou\033[m da idade do alistamento!')
    print('Seu alistamento deveria ser feito \033[1;31m{} anos\033[m atrás.'.format(idade - 18))
    print('O ano de seu alistamento foi {}'.format(nsc + 18))
