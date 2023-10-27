'''escreva um programa que leia o salario de calcule o valor do seu aumento
para salarios superiores a 1.250 o aumento será de 10%
para inferiroes ou iguais, o aumento é de 15%'''

s = float(input('Qual seu salário: '))
if s <= 1250:
    novo = s + (s * 15 / 100)
if s > 1250:
    novo = s + (s * 10 / 100)

print('Seu salário de R$ {:.2f} agora será de R$ {:.2f}.'.format(s, novo))