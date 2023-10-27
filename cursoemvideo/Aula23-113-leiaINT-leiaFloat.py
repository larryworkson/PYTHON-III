def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
            if type(n) == int:
                break
        except (TypeError, ValueError, KeyboardInterrupt):
            print('\033[31mERRO: por favor, digite um nº ineiro válido.\033[m')

    return n

def leiaFloat(txt):
    while True:
        try:
            f = float(input(txt).replace(',', '.'))
            if type(f) == float:
                break
        except (TypeError, ValueError, KeyboardInterrupt):
            print('\033[31mERRO: por favor, digite um nº real válido.\033[m')
    return f

#programa principal
n = leiaInt('Digite um nº inteiro: ')
f = leiaFloat('Digite um nº real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {f}')
