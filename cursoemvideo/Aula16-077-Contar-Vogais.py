palavras = ('pedro', 'andre', 'filipe', 'joao', 'tiago', 'bartolomeu', 'judas', 'mateus')
for c in palavras:
    print(f'\nNa palavra \033[32m{c}\033[m', end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')