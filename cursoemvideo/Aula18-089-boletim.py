dado = list()
alunos = []
while True:
    dado.append(str(input('Nome: ').upper()))
    dado.append(float(input('Nota 1: ').replace(',', '.')))
    dado.append(float(input('Nota 2: ').replace(',', '.')))
    alunos.append(dado[:])
    dado.clear()
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('=-'*10)
print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":>9}')
for aluno in alunos:
    media = (aluno[1] + aluno[2]) / 2
    print(f'{alunos.index(aluno):<4} {aluno[0]:<10} {media:>8.2f}')
while True:
    resp2 = int(input('Digite o nº do aluno para ver as notas ou 999 para sair: '))
    if resp2 == 999:
        print('Sistema finalizado!')
        break
    elif resp2 > len(alunos) - 1: #se o número for maior do que os índices da lista gera erro.
        print('Aluno não encontrado.')        
    elif alunos[resp2] in alunos:
        print(f'As notas de {alunos[resp2][0]} são {alunos[resp2][1:]}')


        


'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
