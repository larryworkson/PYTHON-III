lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {c}: '))) 
print(f'Lista completa: {lista}')
print(f'O maior valor digitado foi {max(lista)}, nas posições...', end=' ')
listab = lista[:] # cria uma cópia da lista para modificá-la no laço abaixo.
for i in range(1, listab.count(max(lista)) + 1): #percorre a lista quantas vezes existir o maior número.
    print(f'{listab.index(max(lista))}...', end=' ') #mostra a posição do maior número
    listab[listab.index(max(lista))] = '0' #transforma o maior número na string '0'. Assim no próximo laço ele irá para o segundo maior número e assim por diante.
print(f'\nO menor valor digitado foi {min(lista)}, nas posições...', end=' ')
listac = lista[:] # cria uma cópia da lista para modificá-la no laço abaixo.
for i in range(1, listac.count(min(lista)) + 1): #percorre a lista quantas vezes existir o menor número.
    print(f'{listac.index(min(lista))}...', end=' ') #mostra a posição do menor número
    listac[listac.index(min(lista))] = '0' #transforma o menor número na string '0'. Assim no próximo laço ele irá para o segundo menor número e assim por diante.