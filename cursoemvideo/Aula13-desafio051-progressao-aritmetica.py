'''leia o PRIMEIRO TERMO e a RAZÃO de uma PA e mostre os 10 primeiros
termos desta progressão'''
pt = int(input('Digite o nº do primeiro termo: '))
r = int(input('Qual a razão: '))
an = pt + (10 - 1) * r #formula matematica para achar um termo na PA
for c in range(pt, an + r, r):
        print(c, '', end='> ')
print('Fim')