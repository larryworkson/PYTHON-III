'''
\033[0;33;44m #estilo ; cor do texto ; cor do fundo

STYLE
0 = sem estilo
1 = bold
4 = underline
7 = negative

TEXT
30 = branco
31 = vermelho
32 = verde
33 = amarelo
34 = azul
35 = roxo
36 = azul bb
37 = cinza

BACKGROUND
40 = branco
41 = vermelho
42 = verde
43 = amarelo
44 = azul
45 = roxo
46 = azul bebe
47 = cinza
'''
print('\033[7;33;44mOlá Mundo!\033[m')
a = 3
b= 5
print('Os valores são \033[1;41m{}\033[m e \033[1;43m{}\033[m'.format(a, b))

