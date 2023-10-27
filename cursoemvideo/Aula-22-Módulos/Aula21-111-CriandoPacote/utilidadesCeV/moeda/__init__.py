def metade(n=0, format=False):
    n /= 2
    return n if format == False else real(n)

def dobro(n=0, format=False):
    n *= 2
    return n if format == False else real(n)

def aumenta(n=0, taxa=0, format=False):
    n += taxa / 100 * n #aumenta com base no % (p)
    return n if not format else real(n)

def diminui(n=0, taxa=0, format=False):
    n -= taxa / 100 * n
    return n if format == False else real(n)

def real(p=0, moeda='R$ '):
    return f'\033[32m{moeda}{p:>5.2f}\033[m'.replace('.', ',')


def tit(txt):
    x = len(txt) + 20
    print('-'*x)
    print(f'{txt:^{x}}')
    print('-'*x)

def resumo(p=0, a=10, r=10):
    tit('RESUMO DO VALOR')
    print(f'Preço analisado: \t{real(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{a}% de aumento: \t{aumenta(p, a, True)}')
    print(f'{r}% de redução: \t{diminui(p, r, True)}')
    print('-'*35)
