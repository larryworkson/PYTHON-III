#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Informe um número: '))
#n = str(num) #converter em str para poder contar os caracteres
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))
# esta solução está limitada a números com 4 dígitos.

#NOVA SOLUÇÃO
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))