import numpy as np
lista = [1, 2, 3]
'''o array é um lista que é manipulada como um dicionário'''
array = np.array(lista)
array[2] = 9
print(array)

#matriz é um array com mais de uma dimensão.
matriz_zeros = np.zeros(5)
print(matriz_zeros)

print('-'*30)
print()
#notas de alunos
lista_notas = [8, 5, 6, 7]
notas = np.array(lista_notas)
print('Máximo', notas.max())
print('Mínimo', notas.min())
print('Desvio padrão', notas.std())
print('Média', notas.mean())
print('Posicão menor', notas.argmin())


'''como preencher uma lista de zeros com valores'''
zeros = np.zeros(5)
zeros[0] = 1
n = 0
for c in range(0, len(zeros)):
    zeros[c] = n + 1
    n += 1
print(zeros)



