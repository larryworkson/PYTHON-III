#crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = float (input ('Digite um número: '))
d2 = n1 * 2
d3 = n1 * 3
r = n1 ** (1/2)
print('O dobro de {} é {}.\nO triplo é {}.\nA raíz quadrada é {:.2f}'.format(n1, d2, d3, r))