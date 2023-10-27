pessoas = []
dado = []
maiorPeso = menorPeso = 0
maisPesados = []
maisLeves = []
while True:
    dado.append(str(input('Nome: ').upper()))
    dado.append(float(input('Peso: ').replace(',','.')))
    pessoas.append(dado[:])
    dado.clear()
    # definindo o MAIOR e MENOR peso
    if len(pessoas) == 1:
        maiorPeso = pessoas[0][1] #armazena o peso da primeira pessoa cadastrada em maiorPeso e menorPeso
        menorPeso = pessoas[0][1]
    #verificando se o peso do último item adicionado [-1] na lista é maior que o útimo maiorPeso adicionado.
    else:
        if pessoas[-1][1] > maiorPeso:
            maiorPeso = pessoas[-1][1]
        elif pessoas[-1][1] < menorPeso:
            menorPeso = pessoas[-1][1]            
    #condição de saída do loop
    resp = str(input('Deseja continuar [S/N]: '))
    if resp in 'Nn':
        break
# adicionando as pessoas com maior peso na lista maisPesadas e com menor peso na lista maisLeves.
# tirei o laço for de dentro do while, pois ele estava gerando nomes repetidos nas listas maisPesados  
for c in pessoas:
    if c[1] >= maiorPeso:
        maisPesados.append(c[0])
    elif c[1] <= menorPeso:
        maisLeves.append(c[0])
print(f'Ao todo você cadastou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorPeso}Kg. Peso de {maisPesados}')
print(f'O menor peso foi de {menorPeso}Kg. Peso de {maisLeves}')
