pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
an = pt + (10 - 1) * r
print(pt, end=' > ')
while pt != an:
    pt = pt + r
    print(pt, '', end='> ')
print('fim')
