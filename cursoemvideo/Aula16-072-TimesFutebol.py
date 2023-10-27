times = (' ', 'Botafogo', 'Palmeiras', 'Fluminense', 'Atlético-MG', 'Cruzeiro', 'Flamento', 'Atlético-PR', 'São Paulo', 'Santos', 'Grêmio', 'Fortaleza', 'Bragantino', 'Bahia', 'Cuiabá', 'Internacional', 'Goiás', 'Vasco da Gama', 'Corinthians', 'América-MG', 'Coritiba')
print('=-'*11)
print('TABELA BRASILEIRÃO 2023')
print('=-'*11)
print('***TOP 5***')
for c in range(1, 6):
    print(f'{c}º - {times[c]}')
print('\n\033[1;31mZONA DE REBAIXAMENTO\033[m')
for c in range (17,len(times)):
    print(f'{c}º - {times[c]}')
print('\n\033[1;33mTimes em ordem alfabética\033[m')
ordem = sorted(times)
for c in range (1, 21):
    print(f'{ordem[c]}')
print('\n\033[1;34mO São Paulo está na {}ª posição\033[m'.format(times.index('São Paulo',1)))
