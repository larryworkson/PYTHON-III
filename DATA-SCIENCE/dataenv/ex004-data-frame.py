import pandas as pd

#criar um dict com produtos, site e preços
produtos = { 'Produtos': ['iPad', 'iPhone', 'Apple Watch', 'AirFry', 'iPhone'],
            'Sites': ['Americanas', 'Amazon', 'Magazine Luiza', 'Americanas', 'Amazon'],
            'Preços': [5000, 8000, 3000, 1000, 8500]}
#cria uma tabela com os dados
df = pd.DataFrame(produtos)
print(df['Sites'][0]) #o 1º param. é a COLUNA e o 2º é a célula

print('-'*30)
print('Média de preços')
print('-'*30)
#mostra a média de preços
print(df['Preços'].mean())

print('-'*30)
print('Filtro por site')
print('-'*30)
#criando um filtro por site
mask_sites = df['Sites'] == 'Amazon'
print(df[mask_sites])

#criando filtro por preços.
print('-'*30)
print('Filtro por preço')
print('-'*30)
mask_preco = df['Preços'] <= 5000
print(df[mask_preco])

print('-'*30)
print('Adicionando novo produto')
print('-'*30)
#adicionando um novo produto
novo_produto = {'Produtos': 'Macbooky', 'Sites': 'Amazon', 'Preços': 11000}
df = df._append(novo_produto, ignore_index = True)
print(df)


print('-'*30)
print('Corrigindo nome produto')
print('-'*30)
#Corrigindo nome produto
mask_correcao = df['Produtos'] == 'Macbooky'
# LOC == 1º busca a linha, 2º busca a coluna
df.loc[mask_correcao, 'Produtos'] = 'Macbook'
print(df)


#python ex004-data-frame.py
