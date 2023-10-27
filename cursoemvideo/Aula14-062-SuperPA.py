#codigo do guanabara
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo = termo + r
        cont = cont + 1
    print('pausa')
    mais = int(input('Quantos termos quer mostrar a mais? [0] Terminar '))
print(f'Progressão finalizada com {total} termos mostrados')