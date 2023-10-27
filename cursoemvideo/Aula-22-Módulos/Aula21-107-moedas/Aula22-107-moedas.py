import moeda
n = float(input('Digite o preço R$: '))
print(f'A metade de R$ {n} é {moeda.metade(n):.2f}')
print(f'O dobro de R$ {n} é {moeda.dobro(n):.2f}')
print(f'Aumentando 10%, temos {moeda.aumenta(n, 10):.2f}')
print(f'Diminuindo 10%, temos {moeda.diminui(n, 10):.2f}')
