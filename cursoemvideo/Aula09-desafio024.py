#crie um programa que leia o nome de uma cidade de diga se ela começa ou não com o nome "santo"
# dapara usar também print(cidade[:5].upper() == 'SANTO')

cidade = str(input('Em que cidade você nasceu?: ').strip().upper())
div = cidade.split()
pesquisa = 'SANTO' in div[0]
print('A cidade informada começa com o nome "Santo"? {}.'.format(pesquisa))


