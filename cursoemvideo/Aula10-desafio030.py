#crie um programa que leia um número inteiro e mostre na tela
# se ela é PAR ou IMPAR.
#Consideramos um número como sendo par quando o dividimos por dois e seu resto é zero. Já um número é ímpar quando, na divisão por dois, o resto é diferente de zero.

n = int(input('Digite um número: '))
div = n % 2
if div == 0:
    print('O número {:.0f} é par.'.format(n))
else:
    print('O número {:.0f} é ímpar.'.format(n))
