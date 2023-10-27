'''
INTERACTIVE HELP
help()
-----------------
DOCSTRING 
para criar uma documentação da função
função(x, y, z):
    """
    Faz contagem e mostra na tela.
    :param x: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
-----------------

PARAMETROS OPCIONAIS
def somar(a, b, c=0): #se o c não receber nada, ele vai receber 0
    s = a+b+c
    print(f'A soma é {s}')

somar(3, 2, 5) = (a, b, c)
somar(8,4) = (a, b) > c = 0

---------------------------
ESCOPO DE VARIÁVEIS
def teste():
    x = 8 #variável local, só funciona dentro da função
    global x #transforma a variável x em global. Ela passa a valer fora da função.
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')

#programa principal
n = 2 #variável global
print(f'No programa principal, n vale {n}')
print(f'No programa principal, x vale {x}')

teste()

******************
def teste(b):
    global a #torna esta variável global, funcionando fora da função.
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {8}') #a função está recebendo o param a. Que é 5.
    print(f'B dentro vale {9}')
    print(f'c dentro vale {2}')
a = 5
teste(a)
print(f'A fora vale {8}') #pq a global foi definida dentro da função

---------------------------

RETORNO DE VALORES
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')


*** é possível ter uma mesma variável local e global.

***********

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Nº: '))
if par(num):
    print('É par')
else:
    print('Não é par')

'''
help(print) #retorna a documentação sobre PRINT
help(input) #retornar a documentação sobre INPUT

def contador(i, f, p):
    """
    Faz contagem e mostra na tela.
    :param x: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    by @larrycrocha
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')
contador(1, 10, 1)
help(contador)

def somar(a=0, b=0, c=0): #se o c não receber nada, ele vai receber 0
    s = a+b+c
    print(f'A soma é {s}')

somar(3, 2, 5)
somar(a=8,c=4)
