from random import randint
print('PARA OU ÍMPAR')
v = 0
while True:
    g = ' '
    pc = randint(0,10)
    n = int(input('Diga um valor: '))
    pi = ' '
    s = n + pc
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    print(f'Você escolheu {n} e PC escolheu {pc}')
    if s % 2 == 0:
        g = 'PAR'
        if g[0] == pi:                        
            print(f'\033[32mA soma deu {s} > {g}. Você venceu!\033[m')
            v = v + 1
            print('=-='*10)
        else:
            print(f'\033[31mA soma deu {s} > {g}. Você perdeu\033[m')
            print(f'GAME OVER: Você venceu \033[1;36m{v}x!\033[m')
            break
    elif s % 2 != 0:
        g = 'IMPAR'
        if g[0] == pi:
            print(f'\033[32mA soma deu {s} > {g}. Você venceu!\033[m')
            print('=-='*10)
            v = v + 1
        else:
            print(f'\033[31mA soma deu {s} > {g}. Você perdeu\033[m')
            print(f'GAME OVER: Você venceu \033[1;36m{v}x!\033[m')
            break


