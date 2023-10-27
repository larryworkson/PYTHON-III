'''
for c in range(1,10): > estrutura de laço (repete 10x)
CONTAGEM REFRESSIVA add ,-1 ex: (5,0,-1):
PULAR NÚMEROS = (0, 7, 2) pula 2 casas na contagem
'''
'''EXEMPLO 1
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')'''
''' EXEMPLO 2
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f, p):
    print(c)
print('fim')'''
s = 0 # uma variável que recebe valores somaods :o
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('A soma total é {}'.format(s))



