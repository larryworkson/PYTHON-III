#faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
v = float(input('Digite o valor: R$ '))
d = float(input('Quantidade de desconto (%): '))
rf = v - (v * d / 100)

print('O preço do produto com {:.1f}% de desconto será de R$ {:.2f}.'.format(d, rf))
