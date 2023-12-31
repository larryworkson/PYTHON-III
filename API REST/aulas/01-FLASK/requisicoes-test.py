import requests


# Fazer a requisição para o site
url = 'http://localhost:5000/carros'


#enviando um novo carro
""" dados = {
        "id": 8,
        "marca": "Porche",
        "modelo": "Cayene",
        "ano": 2018
        }
try:
    enviar = requests.post(url, json=dados)
    print('Conexão estabelecida com sucesso!')
    print(enviar.status_code)
    print(enviar.json())
except Exception as e:
    print(f'ERRO ao enviar os dados: {e}') """


#puxando dados dos carros
response = requests.get(url)
# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    print('Conexão estabelecida com sucesso!')
    print(response.status_code)
    data = response.json()
    for i in data:
        print(i)
else:
    print('ERRO na requisição')


#deletando dados da api
index = int(input('Qual ID do carro para deletar? '))
del_carro = requests.delete(f'{url}/{index}')



# python requisicoes-test.py