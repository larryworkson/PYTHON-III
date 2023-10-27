''' faça uma tabuada de um número que o usuário escolher utilizando laço'''
n = int(input('Digite um número: '))
print('A tabuada de {} é:'.format(n))
for c in range(0, 11):
    tab = n * c
    print('{} x {} = {}'.format(n, c, tab))
print('fim')