
# math.ceil> arredonda pra cima
# math.floor> arredonda para baixo
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

