'''sex = 0
while sex != 'f' and sex != 'm':
    sex = str(input('Qual seu sexo? [M/F] ')).lower()[0].strip()
    if sex != 'f' and sex != 'm':
        print('\033[31mErro. Sexo inválido.\033[m')
        print('Tente novamente.')
print('\033[32mObrigado! Dado cadastrado!')'''

#solucao do guanabara com not in

sex = str(input('Informe seu sexo [M/F]: ')).strip().lower()[0]
while sex not in 'mf':
    sex = str(input('Dados inválidos, por favor, informe seu sexo: ')).strip().lower()[0]
print(f'Sexo {sex} cadastrado com sucesso!')