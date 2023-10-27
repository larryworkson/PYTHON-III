'''dicionários trabalham com
VALORES values()
CHAVES keys()
ITEM items()'''
'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('\n \n')
del pessoas['sexo'] #deletou o item sexo do dicionario
pessoas['nome'] = 'Leandro' #mudou o nome
pessoas['peso'] = 98.5 #adiciona item no dicionario sem usar append
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])
print('\n \n')


estado = dict()
brasil2 = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil2.append(estado.copy()) #usa-se copy() no lugar de [:] para fazer uma cópia da lista
for e in brasil2: #este laço é para as listas
    for k, v in e.items(): #este laço é para os dicionários [e]
        print(k, v, end=' ')