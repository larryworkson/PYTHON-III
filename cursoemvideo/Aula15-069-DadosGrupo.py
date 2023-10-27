print('- '*10)
print('CADASTRE UMA PESSOA')
print('- '*10)
m18 = 0
h = 0
m20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    menu = ' '    
    if idade >= 18:
        m18 = m18 + 1
    if sexo == 'M':
        h = h + 1
    if sexo == 'F' and idade < 20:
        m20 = m20 + 1
    menu = ' '
    while menu not in 'SN':
        menu = str(input('\033[33mQuer continuar [S/N]: \033[m')).strip().upper()[0]
    if menu == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: \033[1;35m{m18}\033[m')
print(f'Total de homens cadastrados: \033[1;32m{h}\033[m')
print(f'Total de mulheres menores 20 anos: \033[1;33m{m20}\033[m')
    