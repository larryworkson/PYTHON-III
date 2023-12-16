def calcular_pontuacao(linha):
    idade = linha['idade']
    renda = linha['renda']
    divida = linha['divida']

    # Defina pesos para cada variável
    peso_renda = 25
    peso_divida = -15
    
    # Ajuste da pontuação com base na idade
    if int(idade) <= 30:
        pontuacao = (30 - idade) * -10
    else:
        pontuacao = idade * 2
    
    # Ajuste da pontuação com base na renda
    pontuacao += (renda / 100) * peso_renda
    
    # Ajuste da pontuação com base na dívida
    pontuacao += (divida / 100) * peso_divida
    
    # Garante que a pontuação final esteja dentro de um intervalo específico
    if pontuacao > 850:
        pontuacao = 850
    elif pontuacao <= 300:
        pontuacao = 300
    
    return pontuacao




# Exemplo de uso

def calcular_pontuacao_teste(idade, renda, divida):
    # Defina pesos para cada variável
    peso_renda = 25
    peso_divida = -18
    
    # Ajuste da pontuação com base na idade
    if int(idade) <= 30:
        pontuacao = (30 - idade) * -10
    else:
        pontuacao = idade * 2
    
    # Ajuste da pontuação com base na renda
    pontuacao += (renda / 100) * peso_renda
    
    # Ajuste da pontuação com base na dívida
    pontuacao += (divida / 100) * peso_divida
    
    # Garante que a pontuação final esteja dentro de um intervalo específico
    if pontuacao > 850:
        pontuacao = 850
    elif pontuacao <= 300:
        pontuacao = 300
    
    return pontuacao


""" idade_cliente = int(input('Idade: '))
renda_cliente = float(input('Renda: '))
divida_cliente = float(input('Dívida: '))

pontuacao_final = calcular_pontuacao_teste(idade_cliente, renda_cliente, divida_cliente)
print(f'A pontuação de crédito é: {pontuacao_final}') """


# python pontuacao_credito.py