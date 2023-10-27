count = 0
m = ' '
s = 0
ma = 0
me = 0
while m != '0':    
    n = int(input('Digite um nº: '))
    count = count + 1
    if count == 1:
        ma = n
        me = n
    else:
        if n > ma:
            ma = n
        elif n < me:
            me = n

    s = s + n
    m = str(input('Continuar? \033[1;32m[1] SIM\033[m] / \033[1;31m[0] NÃO:\033[m] '))

print('*'*20)
print(f'Você inseriu {count} número(s)')
print(f'A média entre todos eles é \033[1;35m{round(s / count, 2)}\033[m')
print(f'O MAIOR nº inserido foi o \033[1;34m{ma}\033[m')
print(f'O MENOR nº inserido foi o \033[1;33m{me}\033[m')

