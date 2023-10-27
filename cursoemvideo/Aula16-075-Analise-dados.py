num = (int(input('Digite um nº: ')),
       int(input('Digite outro nº: ')),
       int(input('Digite mais um nº: ')),
       int(input('Digite o último nº: ')))
s9 = par = 0
print(f'Você digitou os valores {num}')
for c in range (0, len(num)):
    if num[c] % 2 == 0:
        par = par + 1
print(f'O valor 9 apareceu {num.count(9)}x')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3,0) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: {par}')