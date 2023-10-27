#crie um programa que leia o nome de uma pessoa e diga sela tem 'SILVA' no nome
nome = str(input('Digite seu nome completo: ').strip().upper())
pesquisa = 'SILVA' in nome
print('Seu nome possui o sobrenome Silva? {}'.format(pesquisa))