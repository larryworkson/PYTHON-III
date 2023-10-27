def metade(n):
    n /= 2
    return n

def dobro(n):
    n *= 2
    return n

def aumenta(n, taxa):
    n += taxa / 100 * n #aumenta com base no % (p)
    return n

def diminui(n, taxa):
    n -= taxa / 100 * n
    return n
