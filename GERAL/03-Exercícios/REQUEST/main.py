import requests
from bs4 import BeautifulSoup

""" pesquisa = input('Pesquise por: ').lower() """

""" acessando a página """
resposta = requests.get(f'https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/')

""" verificando se o acesso foi bem sucedido """
if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.content, 'html.parser')

    """ encontrando os elementos html que contem os títulos das notícias """
    texto = soup.find_all('div', class_='percentage' )

    print(texto)
    """ extraindo e imprimindo os títulos """
    """ for t in texto:
        print(t) """    
else:
    print(f'Erro ao fazer requisição: {resposta.status_code}')
