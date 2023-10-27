from time import sleep
def linha(n, txt):
    print('\033[32m-=\033[m'*n)
    print(txt)
    print('\033[32m-=\033[m'*n)


def maior(*v):
    linha(20, 'Analisando os valores passados...')
    maior = cont = 0
    sleep(0.5)
    print(f'Foram indormados: {len(v)} valores')
    for i in v:
        print(i, end=' ', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print()
    print(f'O maior valor é \033[1;32m{maior}\033[m')
    sleep(1)

#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

