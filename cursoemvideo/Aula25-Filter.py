"""
A função filter retorna um iterador com os elementos da sequencia as quais o teste lógico é True
#sintaxe
filter(funcao_teste, sequencia)
funcao_teste: retorna True ou False para cada elemento da sequencia
sequencia: a sequencia de elementos que deseja filtrar

"""

#exemplo 1 filtrar numeros menores que 10
nums = [1, 3, 5, 11, 22, 4, 18, 10, 9, 21, 14]
maior_10 =  list(filter(lambda x: x > 10, nums))
print(maior_10)
