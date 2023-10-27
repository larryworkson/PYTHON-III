#faça um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um triangulo retangulo e calcule e mostre o comprimento
#da hipotenusa.
# formuma: teorema de pitágoras
from math import hypot
caad = float(input('Qual o valor do cateto adjacente? '))
caop = float(input('Qual o valor do cateto oposto? '))
#som = (caad ** 2) + (caop ** 2) #ou (caad ** 2) + (caop **2 ) ** (1/2)
hip = hypot(caop, caad)
print('A hipotenusa deste trinagulo retângulo é: {:.2f}'.format(hip))
