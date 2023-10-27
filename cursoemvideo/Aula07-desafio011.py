# crie um programa que leia valor em reais e converta para dolar.
v = float(input('Quanto dinheiro você tem na carteira? R$ '))
d = 3.27
c = v / d
print('Com R$ {:.2f}, você pode comprar US$ {:.2f}'.format(v, c))
