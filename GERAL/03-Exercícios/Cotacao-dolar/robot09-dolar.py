from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

def cotacao_dolar():
    """Busca cotação do dolar"""
    driver = webdriver.Chrome()
    driver.get('https://www.melhorcambio.com/dolar-hoje')
    cotacao = driver.find_element(By.XPATH, "//input[@class='text-verde']")
    valor = cotacao.get_attribute('value')
    return valor


def cotacao_dolar_request():
    # Verificar se a requisição foi bem-sucedida
    try:
        response = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-dolar')
        if response.status_code == 200:
            # Usar BeautifulSoup para analisar o conteúdo HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            # Encontrar o elemento com a classe específica
            elemento = soup.find('div', class_='ljisZu').text
    except NameError as e:
        print(e)
    cotacao = elemento[:4].replace(' ','')
    valor = cotacao.replace(',', '.')
    dolar = float(valor)
    return print(dolar)

cotacao_dolar_request()


#       python robot09-dolar.py