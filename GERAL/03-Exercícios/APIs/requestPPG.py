import requests
from bs4 import BeautifulSoup

# Fazer a requisição para o site
url = 'https://www.nba.com/stats/player/2544'
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Usar BeautifulSoup para analisar o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar o elemento com a classe específica
    elemento = soup.find('p', class_='PlayerSummary_playerStatValue___EDg_')
    if elemento:
        texto = elemento.text
        print(texto)
    else:
        print('Elemento não encontrado')
else:
    print('ERRO na requisição')