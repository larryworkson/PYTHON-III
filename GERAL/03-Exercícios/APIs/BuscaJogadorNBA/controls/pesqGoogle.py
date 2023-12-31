from googleapiclient.discovery import build
import requests
from bs4 import BeautifulSoup
import re

def pesquisar(item):
    """esta função usa a API de pesquisa do google buscar informações do site da NBA"""
    """ try: """
    API_KEY = 'AIzaSyAFsCvURly1-lq-vBndGWyMrRP_PCdy4II'
    CX = '726702180fa3749a9'

    service = build('customsearch', 'v1', developerKey=API_KEY)

    def fazer_pesquisa(query):
        result = service.cse().list(
            q = query,
            cx = CX
        ).execute()
        return result['items']

    resultados = fazer_pesquisa(item)
    encontrado = False
    for item in resultados:
        if 'nba.com' in item["link"]: #se o resultado for do site oficial da nba ele vai buscar o PPG.                 
            encontrado = True
            verificar_nome(item["link"])                
            verificar_ppg(item["link"])
            verificar_rpg(item["link"])
            verificar_apg(item["link"])
            verificar_pie(item["link"])                
            verificar_time(item["link"])                
            verificar_xp(item["link"])
            
            break
    if not encontrado: #se o jogador não for encontrado no site da NBA.
        print('Jogador não encontrado') 
    
"""  except:
    print('Ocorreu algum erro! Tente novamente.') """

    

def verificar_ppg(url):
    """esta função busca o número de PPG do jogador na URL do site oficial encontrado na função pesquisar()"""
    # Fazer a requisição para o site
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Usar BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar o elemento com a classe específica
        elemento = soup.find('p', class_='PlayerSummary_playerStatValue___EDg_')
        if elemento:
            texto = elemento.text
            
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return print(f'PPG: {texto}')

def verificar_nome(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        elemento = soup.find_all('p', class_='PlayerSummary_playerNameText___MhqC')
        nomes = []
        if elemento:
            for nome in elemento:
                nomes.append(nome.text)
            nome_completo = ' '.join(nomes)
        else:
            print('Elemento não encontrado')            
    else:
        print('Erro na requisição')
        
    return print(f'Nome: {nome_completo}')

def verificar_time(url):
    """esta função busca o número de PPG do jogador na URL do site oficial encontrado na função pesquisar()"""
    # Fazer a requisição para o site
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Usar BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar o elemento com a classe específica
        time = soup.find('p', class_='PlayerSummary_mainInnerInfo__jv3LO')
        if time:
            texto = time.text
            partes = texto.split('|')
            texto_fatiado = partes[0].strip()
            
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return print(f'Franquia: {texto_fatiado}')

def verificar_xp(url):
    """busca os anos de experiência na URL do site oficial encontrado na função pesquisar()"""
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Usar BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar o elemento com a classe específica
        time = soup.findAll('p', class_='PlayerSummary_playerInfoValue__JS8_v')
        if time:
            texto = time[7].get_text().replace('p', '')
            
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return print(f'XP: {texto}')

def verificar_rpg(url):
    """busca a média de Rebotes por Jogo na URL do site oficial encontrado na função pesquisar()"""
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Usar BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar o elemento com a classe específica
        elemento = soup.findAll('p', class_='PlayerSummary_playerStatValue___EDg_')
        if elemento:
            texto = elemento[1].get_text().replace('p', '')
            
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return print(f'RPG: {texto}')

def verificar_apg(url):
    """busca a média de Assistências por Jogo: na URL do site oficial encontrado na função pesquisar()"""
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Usar BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar o elemento com a classe específica
        elemento = soup.findAll('p', class_='PlayerSummary_playerStatValue___EDg_')
        if elemento:
            texto = elemento[2].get_text().replace('p', '')
            
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return print(f'APG: {texto}')

def verificar_pie(url):
    """busca a média do impacto geral de um jogador na URL do site oficial encontrado na função pesquisar()"""
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Usar BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar o elemento com a classe específica
        elemento = soup.findAll('p', class_='PlayerSummary_playerStatValue___EDg_')
        if elemento:
            texto = elemento[3].get_text().replace('p', '')
            
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return print(f'PIE: {texto}')

