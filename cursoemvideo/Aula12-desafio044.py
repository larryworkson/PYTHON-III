'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO'''
p = float(input('Valor do produto: '))
print('Selecione a forma de pagamento:')
print('\033[1;31m[1] À VISTA no dinheiro ou cheque\033[m'
      '\n\033[1;32m[2] À VISTA no cartão\033[m'
      '\n\033[1;33m[3] CRÉDITO 2x\033[m'
      '\n\033[1;34m[4] CRÉDITO 3x ou mais.\033[m')
pg = int(input('Escolha: '))
av = p - (p * 10/100)   #a vista no dinheiro ou cheque
avc = p - (p * 5/100)   #a vista no cartão
x3 = p + (p * 20/100) #20 % de juros
if pg == 1:
    print('\033[1;31mOPÇÃO [1] selecionada\033[m')
    print('O produto no valor de R$ {:.2f} terá um desconto de 10%.'.format(p))
    print('O valor final do produto é de R$ {:.2f}'.format(av))
elif pg == 2:
    print('\033[1;32mOPÇÃO [2] selecionada\033[m')
    print('O produto no valor de R$ {:.2f} terá um desconto de 5%.'.format(p))
    print('O valor final do produto é de {:.2f}'.format(avc))
elif pg == 3:
    print('\033[1;33mOPÇÃO [3] selecionada\033[m')
    x2 = p / 2
    print('Sua compra ficará em 2x de R$ {:.2f}'.format(x2))
    print('O produto no valor de R$ {:.2f} não terá desconto.'.format(p))
elif pg == 4:
    print('\033[1;34mOPÇÃO [4] selecionada\033[m')
    x = int(input('Quantas vezes? '))
    print('Sua compra será parcelada em {}x de R$ {:.2f} com acréscimo de 20%.'.format(x, x3 / x))
    print('O valor final do produto é de {:.2f}'.format(x3))

else:
    print('OPÇÃO INVÁLIDA! Tente novamente.')