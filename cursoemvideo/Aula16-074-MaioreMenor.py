from random import randint
lista = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Números sorteados foram:', end=' ')
for c in range (0, len(lista)):
    print(lista[c], end=' ')
print(f'\nMaior número: {max(lista)}') #pega o maior valor da lista
print(f'Menor número: {min(lista)}') #pega o menor valor da lista
