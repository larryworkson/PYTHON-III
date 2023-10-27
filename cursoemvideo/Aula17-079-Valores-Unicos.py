'''lista = [] #cria a lista
menu = ''
while menu != 'N':
    n = lista.append(int(input('Digite um valor: ')))
    ultimo = len(lista) - 1
    if ultimo == 0: #se for o primeiro item da lista cadastra normal.
        print('\033[32mValor cadastrado!\033[m')
    else: #se nao for o primeiro item, condições abaixo:
        qtd = lista.count(lista[ultimo]) #conta quantas vezes o ultimo item inserido aparce na lista
        if qtd == 1: #se o item for unico na lista, cadastrar
            print('\033[32mValor cadastrado!\033[m')
        else: #se houver mais um item igual, remover
            print('\033[31mValor duplicado. Input ignorado!\033[m')
            lista.remove(lista[ultimo]) #remove o ultimo item inserido    
    while True: #laço para impedir que o usuário insira um comando errado
        menu = str(input('Deseja continuar (S/N): ')).upper().strip()
        if menu == 'S' or menu == 'N':
            break
        else:
            print('\033[31mComando inválido\033[m')
lista.sort() #ordena a lista em ordem crescente
print(f'Você digitou os valores: {lista}')'''

#solução Guanabara
numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar')
    r = str(input('Quer continuar [S/N]: '))
    if r in 'Nn':
        break
print('-='*15)
numeros.sort()
print(f'Você digitou os valores {numeros}')
