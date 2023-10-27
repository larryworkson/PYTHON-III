'''LEIA 6 numeros inteiros e mostre a SOMA apenas dos que forem
pares, desconsiderando os ímpares'''
s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 1:
        n = 0
    elif n % 2 == 0:
        s = s + n
        cont = cont + 1
print('A soma dos {} números pares é {}'.format(cont, s))
