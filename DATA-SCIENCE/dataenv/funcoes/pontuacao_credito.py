def calcular_pontuacao(linha):
    idade = linha['idade']
    renda = linha['renda']
    divida = linha['divida']

    # Defina pesos para cada variável
    peso_renda = 25
    peso_divida = 20
    
    # Ajuste da pontuação com base na idade
    if int(idade) <= 30:
        pontuacao = (30 - idade) * -10
    else:
        pontuacao = idade * 2
    
    # Ajuste da pontuação com base na renda
    pontuacao += (renda / 100) * peso_renda
    
    # Ajuste da pontuação com base na dívida
    pontuacao -= (divida / 100) * peso_divida
    
    # Garante que a pontuação final esteja dentro de um intervalo específico
    if pontuacao > 850:
        pontuacao = 850
    elif pontuacao <= 300:
        pontuacao = 300
    
    return pontuacao


def definir_historico(linha):
    pts = linha['pontuação']
    if pts >= 700:
        linha['historico'] = 'Bom'
    elif pts >= 500 and pts < 700:
        linha['historico'] = 'Regular'
    elif pts < 500:
        linha['historico'] = 'Ruim'

    return linha['historico']



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



""" while True:
    idade_cliente = int(input('Idade: '))
    renda_cliente = float(input('Renda: '))
    divida_cliente = float(input('Dívida: '))

    pontuacao_final = calcular_pontuacao_teste(idade_cliente, renda_cliente, divida_cliente)
    print(f'A pontuação de crédito é: {pontuacao_final}')
    resp = str(input('N para sair: ')).lower()
    if resp == 'n':
        break """


# python pontuacao_credito.py