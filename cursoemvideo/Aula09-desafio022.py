#crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras MAIÚSCULAS
# o nome com todas as letras MINÚSCULAS
# quantas letras ao no total (sem os espaços)
# quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip() #split elimina os espaços no inicio e no fim
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #nome - os espaços contados
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #busca o nº do caratere antes do primeiro espaço
