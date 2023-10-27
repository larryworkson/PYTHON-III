#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez
# em que posição ela aparece a última vez.

# frase.count('o') = conta quantas vezes aparece a letra 'o' (minúscula).
# frase.count('o', 0, 13) = conta quantas vezes aparece 'o' entre 0 e 12.
# frase.find('deo') = em qual caractere inicia 'deo' na frase
# frase.find('Android') = se a palavra não existir, o resultado é -1

frase = str(input('Escreva uma frase: ').strip().upper())
c1 = frase.count('A')
ultima = frase.rfind('A') +1
prime = frase.find('A') +1

print('Nesta frase a letra "A" aparece {} vezes.'.format(c1))
print('A primeira vez que a letra "A" aparece é na posição {}'.format(prime))
print('A última vez que a letra "A" aparece é na posição {}'.format(ultima))
