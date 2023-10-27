tot = mil = mb = c = 0
nmb = ' '
while True:
    p = str(input('Nome do produto: '))
    v = float(input('Valor do produto: R$ '))
    tot = tot + v
    c = c + 1
    if c == 1 or v < mb: #se uma das premissas for Verdadeiras ele vai executar o bloco.
        mb = v
        nmb = p
    if v >= 1000:
        mil = mil + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[1;36mDeseja continuar? [S/N] \033[m')).strip().upper()[0]
    if resp == 'N':
        break
print('fim')
print(f'O total da compra é \033[1;34mR$ {tot:.2f}\033[m')
print(f'Produtos que custam mais de R$ 1000: \033[1;35m{mil}\033[m')
print(f'O produto mais barato é \033[1;33m{nmb}\033[m que custa \033[1;33mR$ {mb:.2f}')
