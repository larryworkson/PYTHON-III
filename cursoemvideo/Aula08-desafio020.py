from random import shuffle
a1 = input('1º aluno: ')
a2 = input('2º aluno: ')
a3 = input('3º aluno: ')
a4 = input('4º aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem da lista será:')
print(lista)