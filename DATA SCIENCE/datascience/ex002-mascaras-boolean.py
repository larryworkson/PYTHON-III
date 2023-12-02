import numpy as np

is_pos_covid = np.array(['S', 'N', 'N', 'S', 'S', 'N'])
mask = (is_pos_covid == 'S') #verifica se quais elementos do array são iguais a 'Y'
print(is_pos_covid[mask]) #imprime apenas os elementos que passaram na verificação
print('-'*30)
#alterando os dados que deram positivo
is_pos_covid[mask] = 'Infectado' #ele só imprime a primeira letra, porque o array original só tem 1 letra
print(is_pos_covid)
print('-'*30)
#verificando quais notas são maiores que 5
notas = np.array([4.9, 6.5, 7.5, 6.7])
print(notas)
print('Média: ', notas.mean())
print('Desvio padrão: ', notas.std())
print('Maior nota: ', notas.max())
print('Menor nota: ', notas.min())
mask_notas = notas >= 5
aprovados = 0
reprovados = 0
for c in range(0, len(notas)):
    if mask_notas[c] == True:
        aprovados += 1
    else:
        reprovados += 1

print('aprovados: ', aprovados)
print('reprovados: ', reprovados)


print('-'*30)
#criando uma lista de notas e verificando quais foram aprovados
import numpy as np

array = np.array([
    {'nome': 'Tiago','nota': 5.4},
    {'nome': 'Ana', 'nota': 7.4},
    {'nome': 'Ivan', 'nota': 4},
    {'nome': 'Gabriel', 'nota': 9},
    ])
 
print('-'*30)
print('Lista de alunos')
print('-'*30)
alunos_aprovados = []  
for c in range(0, len(array)):
    print(array[c]['nome'], array[c]['nota'])
    aprovados = array[c]['nota'] >= 7
    if aprovados:
        alunos_aprovados.append(array[c])
print('-'*30)
print('Alunos aprovados')
print('-'*30)
for aluno in alunos_aprovados:
    print(aluno['nome'], aluno['nota'])


    

    