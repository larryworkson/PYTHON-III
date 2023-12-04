import pandas as pd

dados = pd.read_csv('files/dados.csv')
print(dados.head(10))
anomalia = dados.loc[1]

def limpa_data(linha):
    '''remove os números estranhos no final da data e reorganiza a data'''
    linha['Data da Conversão'] = linha['Data da Conversão'].replace('-0300', '').rstrip()
    hora = linha['Data da Conversão'][11:20]
    dia = linha['Data da Conversão'][8:10]
    mes = linha['Data da Conversão'][5:7]
    ano = linha['Data da Conversão'][0:4]
    linha['Data da Conversão'] = f'{dia}/{mes}/{ano} {hora}'
    return linha

#aplicação da função na linha de teste
limpa_data(anomalia)
print(anomalia)

print('-'*30)
print('Dados tratados')
print('-'*30)
#aplicando função a toda a tabela
nova_tabela = dados.apply(lambda x: limpa_data(x), axis=1) #apply aplica a função na tabela. X é o eixo 0 e axis são as linhas.
print(nova_tabela)


#python ex006-tratando-dados.py