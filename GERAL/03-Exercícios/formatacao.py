def titulo(tit, cor=0):
    global c
    c = ('\033[m', '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m')
    n = len(tit) + 4
    print('-'*n)
    print(c[2], end='')
    print((f'{tit:^{n}}'))
    print(c[0], end='')
    print('-'*n)


def cor(txt, cor=0):
    print(c[cor], end='')
    print(txt)
    print(c[0], end='')