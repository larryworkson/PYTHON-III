#crie um programa que leia o nome de 4 alunos e escolha
#1 deles aleatóriamente
from random import choice
a1 = input('Nome do 1º aluno: ')
a2 = input('Nome do 2º aluno: ')
a3 = input('Nome do 3º aluno: ')
a4 = input('Nome do 4º aluno: ')
lista = [a1, a2, a3, a4]
escolha = choice(lista)
print('O aluno escolhido foi {}.'.format(escolha))