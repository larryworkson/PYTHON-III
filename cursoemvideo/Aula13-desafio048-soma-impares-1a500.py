'''calcule a SOMA entre todos os NUMEROS ÍMPARES que são
MULTIPLOS DE TRÊS e que se encontram no intervalo de 1 até 500'''
s = 0 #soma valores a cada laço
cont = 0 #conta os números ímpares que foram encontrados
for c in range(0, 500, 3):
    if c % 2 == 0:
        c = 0
    else:
        s = s + c
        cont = cont + 1
print('A soma dos {} valores ímpares é {}'.format(cont, s))
