#fatiamento de cadeias de string = pegar pedaços de uma str
# [0 1 2 3 4 5 6 7 8 9]
# 1:5 = vai fatiar a string do espaço 1 até 4
# 1:5:2 = fatiar a frase pulando a cada 2 espaços.
# :5 = fatiar do 0 até 4
# 3: = fatiar do 3 até o final.
# 9::3 = fatiar do 9 até o final, pulando de 3 em 3.
# ::2 = pega frase inteira pulando de 2 em 2 espaços.
# ::-1 = pega frase interia de trás para frente

# PRINT PARÁGRAFO
# print("""tLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. """)

# ANALISE ('Curso em vídeo Python')
# len(frase) = conta o número de caracteres da str
# frase.count('o') = conta quantas vezes aparece a letra 'o' (minúscula).
# frase.count('o', 0, 13) = conta quantas vezes aparece 'o' entre 0 e 12.
# frase.find('deo') = em qual caractere inicia 'deo' na frase
# frase.find('Android') = se a palavra não existir, o resultado é -1
# 'curso' in frase = existe esta palavra na str? True ou False

#TRANSFORMAÇÃO ('Curso em vídeo Python')
# frase.replace('Python', 'Android') = substitui a palavra 1 pela 2.
# o REPLACE não muda a str, é apenas uma máscara. Para mudar a frase é preciso mudar a variável
# frase = 'Curso em vídeo Python'
# frase = frase.replace('Python', 'Android')

# frase.upper() = ele deixa em MAIÚSCULO o que estava em minúsculo
# frase.upper().count('O')) = deixa tudo em maiuscula e de depois conta quantos 'o' existem
# frase.lower() = deixa o que estava em maiúsculo em MINÚSCULO
# frase.capitalize() = deixa todos os caracteres em minúsculo e deixar apenas a primeira letra em MAIÚSCULA
# frase.title() = deixa todas as palavras com a primeira letra em MAIÚSCULO
# frase.strip() = remove todos os espaços inúteis no início e fim
# frase.rstrip() = remove só os espaços inúteis na direita (ou seja no final da frase)
# frase.lstrip() = remove só os espaços inúteis na esquerda (ou seja no início da frase)
# len(frase.strip()) = conta quantos caracteres tem na str, removendo os espaços

#DIVISÃO 'Curso em vídeo python'
# frase.split() = dividir a frase em pedaços considerando os espaços entre elas. Cada palavra recebe uma contagem singular. Cada palavra se torna uma nova lista de cadeia de caracteres.
# dividido = frase.split()
# print (dividido[0]) = exibe apenas a primeira palavra da frase dividida
# print (dividido[0] [2]) = exibe o segundo caractere (2) da primeira frase (0)
# '-'.join(frase) = juntar as palavras em uma string única, com '-' separando cada palavra
frase = 'Curso em Vídeo Python'
print(frase.split())