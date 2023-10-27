from moeda import metade, dobro, aumenta, diminui, real
n = float(input('Digite o preço R$: '))
print(f'A metade de {real(n)} é {metade(n, True)}')
print(f'O dobro de {real(n)} é {dobro(n, True)}')
print(f'Aumentando 10%, temos {aumenta(n, 10, True)}')
print(f'Diminuindo 10%, temos {diminui(n, 10, True)}')
