def escreva(txt):
    linha = len(txt) + 4
    print('=' * (linha))
    print(f'{txt:^{linha}}')
    print('=' * (linha))

escreva(
    txt = str(input('Digite um texto: ').upper())
    )

