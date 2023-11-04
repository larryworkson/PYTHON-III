""" arquivo = open('C:/Users/studi/Documents/code/PYTHON-III/cursoII/texto.txt', 'r')
for linha in arquivo:
    print(linha)

arquivo.close() """

texto = ''
while True:
    print('Para finalizar digite n')
    with open('C:/Users/studi/Documents/code/PYTHON-III/cursoII/texto.txt', 'a') as arquivo:
        """
        o 'w' escreve no arquivo deletando o conteúdo original
        o 'a' concatena o conteúdo original com o novo
        """
        texto = input(str('O que deseja escrever: '))
        
        if texto.lower() == 'n':
            break
        else:
            arquivo.write(f'\n{texto}') #write procura o arquivo ou cria e escreve o texto.


with open('C:/Users/studi/Documents/code/PYTHON-III/cursoII/texto.txt', 'r') as arquivo:
    """A instrução with é usada para gerenciar contextos de recursos garantindo que os recursos sejam finalizados após o uso."""
    for linha in arquivo:
        print(linha)

