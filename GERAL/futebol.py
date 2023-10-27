from random import randint
from time import sleep
time = ('Palmeiras', 'Corínthians', 'Cruzeiro', 'São Paulo', 'Flamengo')

for c in range (0, len(time)):
    print(f'[{c}] - {time[c]}')
escU = int(input('Escolha seu time: '))
while True:
    escPC = randint(0,4)
    if escPC != escU:
        break
print(f'Você escolheu: {time[escU]}')
print(f'PC escolheu: {time[escPC]}')
print('=-='*10)
print('1ª RODADA')
print('- * -'*6)
sleep(2)
#jogos
vescU = 0
vescPC = 0

for c in range(0, 5):
    t1 = randint(0,3)
    t2 = randint(0,3)
    print(f'{time[escU]} {t1} X {t2} {time[escPC]}')
    sleep(1)
    if t1 > t2:
        vescU = vescU + 3
    elif t2 > t1:
        vescPC = vescPC + 3
    elif t1 == t2:
        vescU = vescU + 1
        vescPC = vescPC + 1
vit = {time[escU]: vescU, time[escPC]: vescPC}
print('\nTABELA DE VITÓRIAS')
print(vit)

#como deixar o dicionário em ordem?
