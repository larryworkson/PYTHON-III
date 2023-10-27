# soma: +
# subtração: -
# multiplicação: *
# divisão: /
# potência: ** ou pow(4,3) = 4**3
# raiz quadrada:  'X' ** (1/2)
# divisão inteira: // = pega o número mais próximo do valor quebrado (flutuante)
# resto da divisão: % = pega o restante da divisão ex: 5 % 2 == 1.
# ORDEM DE PRECEDÊNCIA: 1º:(); 2º:**; 3º: *, /, //, %; 4º: +, -.

# format
# {:15}.format deixa o valor com 15 espaços
# {:<30}.format deixa o valor alinhado a esquerda
# {:>30}.format deixa o valor alinhado a direita
# {:^30}.format deixa o valor centralizado
# {:=30}.format vai adicionar o '=' nos espaços vazios

# end='' não quebra a linha
# \n quebra a linha

#EXEMPLOS
# 5 + 3 * 2 == 11
# 3 * 5 + 4 ** 2 == 31
# 3 * (5 + 4) ** 2 == 243

#EXERCÍCIOS
# nome = input('Qual o seu nome? ')
# print('Prazer em te conhecer {:=^15}!'.format(nome))

#pratica
n1 = int (input('Um valor: '))
n2 = int (input('Outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
rd = n1 % n2
print('A soma vale {}, \n o produto é {} e a divisão é {:.3f}'.format(s, sub, d), end=' ')
print('Divisão interia {} e potência {}'.format(di, p))

