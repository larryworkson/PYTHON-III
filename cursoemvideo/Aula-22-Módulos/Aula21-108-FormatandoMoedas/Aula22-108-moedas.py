from moeda import metade, dobro, aumenta, diminui, real
n = float(input('Digite o preço R$: '))
print(f'A metade de {real(n)} é {real(metade(n))}')
print(f'O dobro de {real(n)} é {real(dobro(n))}')
print(f'Aumentando 10%, temos {real(aumenta(n, 10))}')
print(f'Diminuindo 10%, temos {real(diminui(n, 10))}')
