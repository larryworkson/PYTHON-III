def leiaInt(txt):
    while True:
        n = input(txt)
        if n.isnumeric():
            break
        else:
            print('\033[31mErro! Digite um número inteiro.\033[m')
    return n


#programa principal
n = leiaInt('Digite um número: ')
print(f'Você digitou \033[32m{n}\033[m')