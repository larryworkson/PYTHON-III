from datetime import datetime, timedelta
hoje = datetime.now()
delta15 = timedelta(days=15) #acrescimo de dias
delta30 = timedelta(days=30) #acrescimo de dias
delta37 = timedelta(days=37) #acrescimo de dias

delta90 = timedelta(days=90) #acrescimo de dias
apto = ['101', '102', '103', '201', '202', '203', '301', '302', '303']

indice = 0
#print(hoje.strftime("%d/%m/%Y"))
print('ESCALA LIMPEZA TÉRREO')
print('2x por mês')
for c in range(0, 10):
    print(f'{hoje.strftime("%d/%m/%Y")} | {apto[indice]}')
    indice += 1
    if indice >= len(apto):
        indice = 0
    hoje += delta15



print('-'*30)
hoje = datetime.now()
indice = 0
print('ESCALA LIMPEZA VIDROS')
print('1x por mês')
print('1º andar')
for c in range(0, 6):
    print(f'{hoje.strftime("%d/%m/%Y")} | {apto[indice]}')
    indice += 1
    if indice >= 3:
        indice = 0
    hoje += delta30

print('-'*30)
indice = 3
hoje = datetime.now()
novadata = hoje.replace(day=29, month=8, year=2023)
print('2º andar')
for c in range(0, 6):
    print(f'{hoje.strftime("%d/%m/%Y")} | {apto[indice]}')
    indice += 1
    if indice >= 6:
        indice = 3
    hoje += delta30


print('-'*30)
hoje = datetime.now()
indice = 0
print('ESCALA LIMPEZA GARAGEM')
print('1x a cada 3 meses')
for c in range(0, 10):
    print(f'{hoje.strftime("%d/%m/%Y")} | {apto[indice]}')
    indice += 1
    if indice >= len(apto):
        indice = 0
    hoje += delta90