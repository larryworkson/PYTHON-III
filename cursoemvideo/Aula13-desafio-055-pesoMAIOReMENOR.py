ma = 0
me = 0
for p in range(1,6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        ma = peso
        me = peso
    else:
        if peso > ma:
            ma = peso
        elif peso < me:
            me = peso
print('O maior peso lido foi de {}kg'.format(ma))
print('O menor peso lindo foi de {}kg'.format(me))

