#INDENTADAÇÃO = quando há comandos condicionais
# condição = em uma condição ou bloco verdadeiro é executado ou o bloco falso, nunca os dois.
# ifcarro.esquerda():
#   blocoTrue
# else:
#   blocoFalse
'''
== igual
"= diferente
and e
or ou

'''
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
#ou print('carro novo' if tempo<=3 else'carro velho')
print('--fim--')