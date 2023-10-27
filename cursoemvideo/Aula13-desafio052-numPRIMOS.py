'''Leia um NUM INTEIRO e diga se ele é o não número primo.'''
n = int(input('Digite um nº: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
       total = total + 1

print('O número {} foi divisível {}x'.format(n, total))
if total == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele NÃO É PRIMO')