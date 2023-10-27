'''esenvolva um programa que pergunte a distancia de uma viagem em KM.
calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200km
e R$ 0,45 para viagens mais longes.'''

d = float(input('Qual a distância da viagem? '))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('Sua viagem vai custar R$ {:.2f}'.format(preço))