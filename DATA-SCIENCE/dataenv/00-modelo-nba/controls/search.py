from googleapiclient.discovery import build
import requests
from bs4 import BeautifulSoup
import re
from controls.database import ativar_db

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
            nome = verificar_nome(item["link"])
            ppg = verificar_ppg(item["link"])
            rpg = verificar_rpg(item["link"])
            apg = verificar_apg(item["link"])
            pie = verificar_pie(item["link"])                
            time = verificar_time(item["link"])                
            xp = verificar_xp(item["link"])
            sal = buscando_sal_google(nome)            
            break
    if not encontrado: #se o jogador não for encontrado no site da NBA.
        print('Jogador não encontrado') 
    return nome, ppg, rpg, apg, pie, xp, sal

    

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
            ppg = elemento.text
            
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return ppg

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
        
    return nome_completo

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
            nome_time = partes[0].strip()
            
        else:
            nome_time = 'Sem time'
            print('Time não encontrado')
    else:
        print('ERRO na requisição')
    return nome_time

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
            xp = time[7].get_text().replace('p', '')
            print(xp)
            xp_final = re.findall("[0-9]+", xp)
            if not xp_final: #se o xp do jogador é < 0, o site define como rookie, que é um string. Esta condição transforma a var em 0 neste caso.
                xp_final = 0
            else:
                xp_final = float(xp_final[0])
               
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return xp_final

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
            rpg = elemento[1].get_text().replace('p', '')
            
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return rpg

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
            apg = elemento[2].get_text().replace('p', '')
            
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return apg




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
            try:            
                pie = elemento[3].get_text().replace('p', '')
            except(IndexError):
                pie = 0            
        else:            
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return pie


def buscando_sal_google(nome_jogador):
        """esta função usa a API de pesquisa do google buscar informações de salário no site da hoops hype"""
        """ try: """
        API_KEY = 'AIzaSyAFsCvURly1-lq-vBndGWyMrRP_PCdy4II'
        CX = '726702180fa3749a9'

        service = build('customsearch', 'v1', developerKey=API_KEY)
        item = f'{nome_jogador} hoopshype salary'
        def fazer_pesquisa(query):
            result = service.cse().list(
                q = query,
                cx = CX
            ).execute()
            return result['items']

        resultados = fazer_pesquisa(item)
        encontrado = False
        for item in resultados:
            if 'hoopshype.com' in item["link"]: #se o resultado for do site hoopshype.                 
                encontrado = True
                salario = verificar_sal(item["link"])  
                break
        if not encontrado: #se o jogador não for encontrado no site da NBA.
            print('Jogador não encontrado')
        return salario

def verificar_sal(url):
    """Esta função busca o salário do jogador no na página encontrada pela função buscando_sal_google"""
    response = requests.get(url)
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Usar BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar o elemento com a classe específica
        elemento = soup.findAll('span', class_='player-bio-text-line-value')
        if elemento:
            sal = elemento[4].get_text().replace('td', '')
            sal_limpo = re.sub(r"[$,()* ]", "", sal) #limpando a string.

            if float(sal_limpo) > 137000000:
                sal_limpo = 0
            else:
                print('Salario em formato incompatível')
            
        else:
            print('Elemento não encontrado')
    else:
        print('ERRO na requisição')
    return sal_limpo
