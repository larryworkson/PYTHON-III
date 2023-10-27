nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onde', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        user = int(input('Digite um número entre 0 e 20: '))
        if user > 0 and user <= 20:
            break
        print('Tente novamente')
    print(f'Voccê digitou \033[32m{nums[user]}\033[m')
    menu = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if menu == 'N':
        break
print('Programa encerrado!')