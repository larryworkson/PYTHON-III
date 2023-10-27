#faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o 1º e o ultimo nome separadamente.
#EX: ANA MARIA DE SOUZA
# primeiro = ANA
# ultimo = SOUZA
nome = str(input('Digite seu nome completo: ').strip().upper())
div = nome.split()
print('primeiro = {}'.format(div [0].capitalize()))
print('último = {}'.format(div[len(div)-1].capitalize()))
