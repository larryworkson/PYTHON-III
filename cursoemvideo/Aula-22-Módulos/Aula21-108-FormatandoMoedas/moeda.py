def metade(n=0):
    n /= 2
    return n

def dobro(n=0):
    n *= 2
    return n

def aumenta(n=0, taxa=0):
    n += taxa / 100 * n #aumenta com base no % (p)
    return n

def diminui(n=0, taxa=0):
    n -= taxa / 100 * n
    return n

def real(p=0, moeda='R$ '):
    return f'\033[32m{moeda}{p:>5.2f}\033[m'.replace('.', ',')