#receber a distância, velocidade média, consumo médio e preço da gasolina para calcular tempo de viagem e custo médio com combustível
d = float(input('Qual a distância a ser percorrida? (Km) '))
v = float(input('Qual a velocidade média? (Km) '))
cm = float(input('Qual o consumo médio do veículo? '))
pg = float(input('Qual o preço da gasolina: R$ '))
min = (d / v) * 60
hr = min / 60
consumo = (d / cm) * pg
print('A viagem de {:.0f} km a uma velocidade média de {:.0f} km/h, deve consumir cerca de R$ {:.2f} de gasolina. E deve levar certe de {:.1f} minutos ({:.1f} horas.)'.format(d, v, consumo, min, hr))