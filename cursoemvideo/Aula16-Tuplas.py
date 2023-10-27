#TUPLAS são variáveis compostas e IMUTÁVEIS que permitem armazenar valores em uma mesma estrutura, acessíveis por chaves individuais.
#pode usar FOR em TUPLAS


lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#MODELO 1
for comida in lanche: #o RANGE é substituido pela TUPLA e o 'C' é a variável de 'contagem'
    print(f'Eu vou comer {comida}')

#MODELO 2
for cont in range (0, len(lanche)):
   print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#MODELO 3 >> ENUMERATE: mostra mais de um dado, no caso, mostra a posição quanto o valor.
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for pos, comida in enumerate(lanche): #POS é uma variável que armazena a contagem
    print(f'Eu vou comer {comida} na posição {pos}')


#ORDENAR
print(sorted(lanche)) #imprime em ordem alfabética ou numérica

a = (1, 4, 10, 3)
b = (2, 5, 9, 1, 2)
c = a + b
print(c.count(5)) #conta quantas vezes aparece '5' no conjunto a + b
print(sorted(c)) #imprime na ordem crescente
print(b.index(2, 1)) #verifica qual posição está o item 2, iniciando na posição '1' (ou seja, excluindo a posição '0')

del(a) # apaga a variável da memória - não dá para deletar itens, apenas a TUPLA inteira
