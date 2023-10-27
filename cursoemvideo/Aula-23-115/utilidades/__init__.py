c = ('\033[m', '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[34m')
 
def cor(txt, cor=0):
    print(c[cor], end='')
    print(txt)
    print(c[0], end='')

def titulo(txt, color=0):
    n = len(txt)
    print('-'*n)
    cor(f'{txt:^{n}}', color)
    print('-'*n)

def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
            if type(n) == int:
                break
        except (TypeError, ValueError, KeyboardInterrupt):
            print('\033[31mERRO: por favor, digite uma opção válida.\033[m')

    return n

def leiaStr(txt):
    while True:
        n = input(txt)
        if n == '':
            n = 'Sem nome'
        if type(n) == str:
            break

    return n.strip()

def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m -- \033[34m{item}\033[m')
        c += 1

def cadastro(n, i):
    arquivo = open('C:/Users/Usuario/Transmissão no Google Drive/Meu Drive/_CODE (drive)/PYTHON/cursoemvideo/Aula-23-115/cadastros.txt', 'a')
    arquivo.write(f'{n}, {i}\n')
    arquivo.close()
    cor('Pessoa cadastrada com sucesso!', 2)

def consulta():
    try:
        arquivo = open('C:/Users/Usuario/Transmissão no Google Drive/Meu Drive/_CODE (drive)/PYTHON/cursoemvideo/Aula-23-115/cadastros.txt', 'r')
        conteudo = arquivo.readlines()
        for pessoa in conteudo:
            nome = pessoa.strip().split(',')
            print(f'{nome[0]:<41} {nome[1]:>3} anos ')
        arquivo.close()
    except FileNotFoundError:
        cor('Arquivo não encontrado. Crie o primeiro cadastro na opção [2]', 1)
        