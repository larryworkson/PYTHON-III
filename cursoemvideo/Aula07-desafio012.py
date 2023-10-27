# faça um programa que leia altura e largura em metros e calcule a sua àrea e a quantidade de tinta necessária para pintá-la.
#cada litro de tinta pinta 2m quadrados.
l = float(input('Quantos metros de largura? '))
a = float(input('Quantos metros de altura? '))
m2 = l * a
lit = 2
r = m2 / lit
print('Uma parede com {:.2f}m² vai precisar de {:.1f} litros de tinta.'.format(m2, r))
