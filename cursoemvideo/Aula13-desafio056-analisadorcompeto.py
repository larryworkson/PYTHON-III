'''somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1,5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))'''
hnome = 0
hvelho = 0
sidade = 0
midade = 0
for c in range(1,5):
    print('=-' * 5,'{}º cadastro: '.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).lower()
    sidade = sidade + idade
    if c == 1 and sexo == 'm':
        hvelho = idade
        hnome = nome
    if idade > hvelho and sexo == 'm':
        hvelho = idade
        hnome = nome
    if idade <= 20 and sexo == 'f':
        midade = midade + 1
print('A lista contém {} mulheres com idade igual ou inferior a 20 anos.'.format(midade))
print('O homem mais velho é o {}.'.format(hnome.capitalize()))
print('A média de idade do grupo é de {:.0f} anos'.format(sidade / 4))


