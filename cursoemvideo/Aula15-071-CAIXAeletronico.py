print('=-='*10)
print('{:^30}'.format('BANCO CEV'))
print('=-='*10)
saque = int(input('Qual valor do saque? '))
total = saque
ced = 50
while total != 0:
    while True:
        if total != 0:
            qced = total // ced #quantidade de cédulas  
            total = saque - (qced * ced) #resto 
            break #saida do laço para printar    
    if qced > 0:        
        print(f'Total de {qced} notas de R$ \033[1;32m{ced}\033[m')    
    if total >= 20:
        ced = 20 #cédulas de 20
        saque = total
    elif total >= 10:
        ced = 10 #cédulas de 10
        saque = total
    elif total >= 1:
        ced = 1 #cédulas de 1
        saque = total
print('Volte sempre ao banco CEV! Tenha um bom dia!')


#solução guanabara
'''valor = int(input('Que valor você sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break'''