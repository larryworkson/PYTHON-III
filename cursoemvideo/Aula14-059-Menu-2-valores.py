n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
m = 0
while m != 5:
    print('-' * 10)
    print('\033[32mO QUE DEVO FAZER?\033[m')
    print('''[1] - SOMAR
[2] - MULTIPLICAR
[3] - QUAL MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA''')
    m = int(input('Sua escolha: '))
    print('-' * 10)
    if m == 1:
        print('RESULTADO:')
        print('A soma de {} e {} é {}'.format(n1, n2, n1 + n2))
    elif m == 2:
        print('RESULTADO:')
        print('{} x {} é igual a {}'.format(n1, n2, n1 * n2))
    elif m == 3:
        if n1 > n2:
            print('RESULTADO:')
            print('O maior valor entre {} e {} é {}.'.format(n1, n2, n1))
        elif n1 < n2:
            print('RESULTADO')
            print('O maior valor entre {} e {} é {}'.format(n1, n2, n2))
        else:
            print('Os valores são iguais.')
    elif m == 4:
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite outro valor: '))
    elif m != 5:
        print('\033[31mOpção inválida.\033[m')
print('OPÇÃO [5] SELECIONADA')
print('FIM DO PROGRAMA!')