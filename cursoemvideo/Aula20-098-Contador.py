from time import sleep
def linha(valor):
    print('\033[32m=-\033[m'*valor)

def contador(inicio, fim, passo):   
    c = 0
    for i in range(inicio, fim + 1, passo):
        print(f'{inicio + c} ', end='', flush=True)
        sleep(0.3)
        c += passo
    print('\033[31mFIM!\033[m')
   

#programa principal
print('Contagem de 1 até 10 de 1 em 1')
linha(20)
contador(1, 10, 1)
linha(20)
print('Contagem de 10 até 0 de 2 em 2:')
contador(10, -2, -2)
linha(20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha(20)
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
linha(20)
if passo == 0:
    passo = 1
if fim < inicio:
    passo *= -1
    fim -= 2
contador(inicio, fim, passo)
