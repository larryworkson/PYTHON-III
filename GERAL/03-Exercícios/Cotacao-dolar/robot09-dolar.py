from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.melhorcambio.com/dolar-hoje')
cotacao = driver.find_element(By.XPATH, "//input[@class='text-verde']")
valor = cotacao.get_attribute('value')
print(valor, type(valor))


#capturando sem bot
import requests
from bs4 import BeautifulSoup

response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Usar BeautifulSoup para analisar o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar o elemento com a classe específica
    elemento = soup.find('p', class_='PlayerSummary_playerStatValue___EDg_')
    if elemento:
        ppg = elemento.text


#       python robot09-dolar.py