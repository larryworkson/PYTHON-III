while True:
    print('- - '*10)
    n = int(input('Digite um número: '))
    if n < 0:
        print('#'*20)
        print('Programa encerrado!')
        break        
    else:
        c = 0
        print('-=-'*10)
        print(f'A tabuada de {n} é:')
        print('-=-'*10)
        while c < 11:
            r = n * c                        
            print(f'{n} x {c} = {r}')
            c = c + 1

