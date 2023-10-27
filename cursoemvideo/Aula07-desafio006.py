#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRA NA TELA O SEU SUCESSO E O SEU ANTECESSOR
n1 = int (input ('Digite um número: '))
s = n1 + 1
a = n1 - 1
print('O sucessor de \033[4;35m{}\033[m é \033[4;32m{}\033[m e o seu antecessor é \033[4;32m{}\033[m.'.format(n1, s, a))