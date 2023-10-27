c = ('\033[m', #0 sem cor
         '\033[31m', #1 vermelho
         '\033[32m', #2 verde
         '\033[1;43m', #3 amarelo
         '\033[1;44m', #4 azul
         '\033[47;30m' #5 branco
         )

#def cor():

def tit(txt, cor=0):
    x = len(txt) + 4
    print(c[cor], end='')
    print('-' * x)
    print(f'{txt:^{x}}')
    print('-' * x)
    print(c[0])


def ajuda(n):
    from time import sleep
    while True:
        item = input(n).lower()
        tit('SISTEMA DE AJUDA PyHELP', 3)
        if item == 'fim':
            break            
        else:
            tit(f'Acessando manual do comando "{item}"', 4)
            sleep(1)
            print(c[5])
            help(item)
            print(c[0])
    print(c[1])
    print('Até logo!')
    print(c[0])


ajuda('\033[32m>> Função ou Biblioteca: \033[m')
