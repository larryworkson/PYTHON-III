'''escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem

o valor A é MAIOR ou
o valor B é MAIOR ou
Não existe valor maios, os dois são iguais'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
if n1 > n2:
    print('\033[1;32m{}\033[m é MAIOR que {}'.format(n1, n2))
elif n2 > n1:
    print('\033[1;32m{}\033[m é MAIOR que {}'.format(n2, n1))
else:
    print('Não existe valor maior. Os números são \033[1;34mIGUAIS.')