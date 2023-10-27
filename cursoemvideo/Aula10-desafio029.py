#escreva um programa que leia a velocidade de um carro
# se ele ultrapssar 80km/h mostra uma msg que ele foi multado
# a multa vai custar R$ 7,00 por cada KM acima do limite.
v = int(input('Qual a velocidade do carro (km/h?) '))
m = (v - 80) * 7
if v > 80:
    print('Você ultrapassou o limite de velocidade.')
    print('Você foi multado em \033[31mR$ {:.2f}\033[m.'.format(m))
else:
    print('Boa viagem! Diriga com segurança!')

