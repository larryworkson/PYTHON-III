def soma(a, b):
    s = a + b
    print(s)

soma(4, 3) # ou soma(a=4, b=3) pode declarar os itens explicitamente ou até mudar a ordem.
soma(2, 2)
soma(2, 1)

print('* '*40)

print('\n\n')

#EMPACOTAMENTO
def contador(*num):
    qtd = len(num)
    print(f'Recebi os valores {num} e são ao todo {qtd} números')

contador(2, 1, 7)

print('* '*40)
print('\n\n')
 
# LISTAS
def dobra(lista):
    c = 0
    while c < len(lista):
        lista[c] *= 2
        c += 1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

print('* '*40)
print('\n\n')


#DESEMPACOTAMENTO
def soma(*valores):
    s = 0
    for n in valores:
        s += n
    print(f'A soma de {valores} é = {s}')

soma(1,3,10)
soma(2,2)
soma(30, 2, 22, 1)