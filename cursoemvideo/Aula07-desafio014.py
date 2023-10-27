# leia o salário de um funcionário e mostre o novo salário com 15% de aumento
s = float(input('Qual seu salário atual? '))
a = float(input('Quantos % de aumento? '))
rf = s + (s * a / 100)
print('Seu salário de R$ {:.2f}, com {:.1f}% de aumento ficará em R$ {:.2f}.'.format(s, a, rf))