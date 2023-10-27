frase = input('Digite uma frase: ').strip().upper()
div = frase.split()
junto = ''.join(div)
inv = junto[::-1]
print('O inverso de {} é {}'.format(junto, inv))
if junto == inv:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase não é um palíndromo.')