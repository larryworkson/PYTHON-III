""" O fatorial de um número é o produto dele pelos seus antecessores maiores que 0. O fatorial de um número é a multiplicação desse número por todos os seus antecessores maiores que zero.  """

def fatorial(num=1, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param num: o número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: o valor Fatorial de um número n.
    """
    print('-'*20)
    f = 1
    for c in range(num, 0, -1):
        f = f * c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')        
    return f    


fatorial(5, True)
