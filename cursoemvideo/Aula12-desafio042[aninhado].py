'''desenvolva um programa que leia o comprimento de três retas e diga
ao usuario se elas podem ou não formar um triangulo.
A SOMA DAS MEDIDAS DE DOIS LADOS DE UM TRIANGULO DEVE SEMPRE SER MAIOR QUE A MEDIDA DO 3º LADO

equilátero: 3 lados iguais
isósceles: 2 lados iguais e 1 diferente
escaleno: todos os lados diferentes
'''

a = float(input('Medida do lado A: '))
b = float(input('Medida do lado B: '))
c = float(input('Medida do lado C: '))
if a + b > c and b + c > a and c + a > b:
    print('Sim! Estas medidas formam um triangulo ', end='')
    if a  == b and b == c:
        print('EQUILÁTERO')
    elif a != b and b != c and a != c:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não! Estas medidas NÃO formam um triângulo.')