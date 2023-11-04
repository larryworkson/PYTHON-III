from googleapiclient.discovery import build

while True:
    try:
        API_KEY = 'AIzaSyAFsCvURly1-lq-vBndGWyMrRP_PCdy4II'
        CX = '726702180fa3749a9'


        service = build('customsearch', 'v1', developerKey=API_KEY)

        def fazer_pesquisa(query):
            result = service.cse().list(
                q = query,
                cx = CX
            ).execute()
            return result['items']
        print('Digite N para sair.')
        pesquisa = input(str('Pesquise por: ').lower())
        if pesquisa.lower() == 'n':
            break
        resultados = fazer_pesquisa(pesquisa)
        for item in resultados:
            print(f'Título: {item["title"]}')
            print(f'Link: {item["link"]}')
            print()
        
        
    except:
        print('Ocorreu algum erro! Tente novamente.')
