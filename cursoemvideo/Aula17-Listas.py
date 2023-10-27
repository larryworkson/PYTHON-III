num = [2, 5, 9, 1]
num.append(7) #adiciona o nº 7 na lista
num.insert(2, 0) # adiciona o '0' na posição 2
num.sort() #organiza a lista em ordem crescente
num.sort(reverse=True) #organiza a lista em ordem decrescente
num.pop() #deleta o último elemento da lista
num.pop(3) #deleta o elemento que está na posição 3
num.remove(5) #elimina o conteúdo '5' ## só funciona se o elemento for encontrado na lista
print(num)
print(f'a lista tem {len(num)} elementos')
print('=-='*20)
valores = []
for cont in range(0,3):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na poição {c} encontrei o valor {v}!')
print('=-='*20)
a = [2, 3, 4, 6]
b = a[:] #cria uma cópia original da variável
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')