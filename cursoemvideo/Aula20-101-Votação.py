def voto(n):
    from datetime import date
    ano = date.today().year
    idade = ano - n
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return print('NÃO VOTA.')
    elif 16 <= idade and idade < 18 or idade > 65:
        return print('VOTO OPCIONAL.')
    else:
        return print('VOTO OBRIGATÓRIO.')
    

#programa principal
nsc = int(input('Em que ano você nasceu? '))
voto(nsc)
