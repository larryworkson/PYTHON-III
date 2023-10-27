from time import sleep
from utilidades import *
while True:
    titulo(f'{"MENU PRINCIPAL":^50}')
    menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    resp = leiaInt('Sua opção: ')
    if resp == 3:
        titulo(f'{"Saindo do sistema!":^50}', 1)
        sleep(1)
        break
    elif resp == 1:
        titulo(f'{"PESSOAS CADASTRADAS":^50}')
        consulta()
    elif resp == 2:
        titulo(f'{"Opção 2":^50}')
        nome = leiaStr('Nome: ')
        idade = leiaInt('Idade: ')
        cadastro(nome, idade)
    else:
        cor('ERRO! Digite uma opção válida.', 1)
    sleep(2)