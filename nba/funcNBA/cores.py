c = ('\033[m', '\033[1;31m', '\033[1;32m', '\033[33m', '\033[34m')
  


def cor(txt, cor=0):
    print(c[cor], end='')
    print(txt)
    print(c[0], end='')

def titulo(txt, color=0):
    n = len(txt)
    print('-'*n)
    cor(f'{txt:^{n}}', color)
    print('-'*n)