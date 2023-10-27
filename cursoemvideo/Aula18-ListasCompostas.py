'''teste = []
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # precisa adicionar o [:] para criar uma cópia da lista
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''


'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

galera = list()
dado = []
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])#cria uma cópia dos dados dentro de 'galera'
    dado.clear()
    
maiores = 0
menores = 0
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é MAIOR de idade')
        maiores += 1
    else:
        print(f'{p[0]} é MENOR de idade')
        menores += 1
print(f'Temos {maiores} maiores e {menores} menor de idade.')
