"""LAMBDA é um tipo de função para operações rápidas e concisas.
é necessário adicionar os argumentos e a operação"""

#exemplo 1
soma = lambda num1, num2: num1 + num2 #num1 e num2 são os argumentos, Após : está a operação de soma
print(soma(5, 2))

#exemplo 2
titulo = lambda txt: f'{print('-'*30)}{print(str(txt).upper())}{print('-'*30)}'
titulo('exemplo 2')

#exemplo 3 - ordenação de listas
titulo('exemplo 3')
#pessoas = [('Alice', 30), ('Bob', 25), ('Carlos', 35)]
pessoas = [{'nome': 'Alice', 'idade': 30}, {'nome': 'Bob', 'idade': 25}, {'nome': 'Carlos', 'idade': 35}]
pessoas_ordendas = sorted(pessoas, key=lambda x: x['idade'], reverse=True) #aqui a função lambda está usando como valor ordenador a idade (x['idade'])
print(pessoas_ordendas)

#exemplo 4 - filtragem de numeros pares
titulo('exemplo 4')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x%2 == 0, nums))
print(pares)