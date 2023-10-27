#faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Digite mais um: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O maior valor digitado foi {}'.format((maior)))
print('O menor valor digitado foi {}'.format(menor))



