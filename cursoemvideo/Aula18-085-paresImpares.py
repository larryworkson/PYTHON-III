geral = [list(), list()] #cria 2 listas dentro de uma lista
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0: #verifica se o num é PAR
        geral[0].append(num)
    else:
        geral[1].append(num)
print(f'Os valores PARES são: {sorted(geral[0])}')
print(f'Os valores ÍMPARES são: {sorted(geral[1])}')


