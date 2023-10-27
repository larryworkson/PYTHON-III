from math import factorial
'''n = int(input('Digite um número: '))
c = 0
print('{}!={}'.format(n, n), end='')
for c in range (n - 1, 0, -1):
    print('x{}'.format(c), end='')
(print('= {}'.format(factorial(n))))'''
n = int(input('Digite um número: '))
print('{}!={}'.format(n, n), end='')
c = n - 1
while c:
    print('x{}'.format(c), end='')
    c = c - 1
print('= {}'.format(factorial(n)))
