'''
QUANDO FOR 3 POSSIBILIDADES
if = se
else = senão
elif = se senão

QUANDO FOR 4 POSSTIBILIDADES
if
elif
elif
else
'''
nome = str(input('Qual é o seu nome: ')).upper().strip()
if nome == 'GUSTAVO':
    print('Que nome bonito!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ANA CLÁUDIA JÉSSICA JULIANA':
    print('Belo nome feminino')
else: #OPCIONAL
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome.capitalize()))