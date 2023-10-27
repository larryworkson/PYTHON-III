def metragem(l, c):
    metroQuad = l * c
    print(f'A área do terreno {l:.1f} x {c:.1f} é de \033[1;32m{metroQuad} m²\033[m')

def title(msg):
    print('-'*34)
    print(f'\033[1;32m{msg:^34}\033[m')
    print('-'*34)


#programa principal
title('CONTROLE DE TERRENOS:')
metragem(
    l = float(input('Largura (m): ').replace(',', '.')),
    c = float(input('Comprimento (m): ').replace(',', '.'))    
)

