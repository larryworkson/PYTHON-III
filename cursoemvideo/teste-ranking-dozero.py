a = 0
for c in range(1, 6):
    pt = int(input('Pontos do time: '))
    if c == 1:
        a = pt
    elif pt > a:
        a = pt
print('{}º lugar - {}'.format(c, pt))