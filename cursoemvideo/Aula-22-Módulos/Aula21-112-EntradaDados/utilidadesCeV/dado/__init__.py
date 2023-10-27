def leiaDinheiro(n):
    valido = False
    while not valido:
        num = input(n).strip().replace(',','.').replace(' ', '')      
        if num.isalpha() or num == "":
            print(f'\033[31mErro: {num} é um preço inválido!\033[m')
        else:
            valido = True
            return float(num)
        
        
