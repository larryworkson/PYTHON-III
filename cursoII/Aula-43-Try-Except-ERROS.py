'''Crie um programa que leia duas notas e calcule a média, mostrando uma msg
no final de acordo com a média:

média abaixo de 5.0 = reprovado
média entre 5.0 e 6.9: recuperação
média 7.0 ou superior: APROVADO'''
resultado = False
while True:
    try: #se acontecer algum erro na tentativa (try) o except 'tentará resolver'
        n1 = float(input('Digite a 1ª nota: '))
        n2 = float(input('Digite a 2ª nota: '))
        m = (n1 + n2) / 2
        if m < 5.0:
            print('-' * 30)
            print('Sua média foi \033[4;31m{:.1f}\033[m'.format(m))
            print('Você foi \033[1;31mREPROVADO!\033[m')
            print('-' * 30)
            resultado = True
        elif m >= 7.0:
            print('-' * 30)
            print('Sua média foi \033[4;32m{:.1f}\033[m'.format(m))
            print('Você foi \033[1;32mAPROVADO\033[m')
            print('-' * 30)
            resultado = True
        else:
            print('-' * 30)
            print('Sua média foi \033[4;34m{}\033[m'.format(m))
            print('Você ficou em \033[1;34mRECUPERAÇÃO!\033[m')
            print('-' * 30)
            resultado = True
        if resultado:
            break
    except ValueError:
        print('Ocorreu algum erro inesperado, Verique sua operação.')