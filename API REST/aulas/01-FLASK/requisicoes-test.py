import requests


# Fazer a requisição para o site
url = 'http://localhost:5000/carros'


#enviando um novo carro
""" id_verifica = requests.get(url)
ultimo_id = id_verifica.json()[-1]['id']
prox_id = int(ultimo_id) + 1
dados = {
        "id": prox_id,
        "marca": "Fiat",
        "modelo": "Argo",
        "ano": 2023
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
    print(f'ERRO na requisição:')


#deletando dados da api
""" index = int(input('Qual ID do carro para deletar? '))
pesquisa = requests.get(url)
nome_carro = pesquisa.json()[index]['modelo']
marca = pesquisa.json()[index]['marca']
del_carro = requests.delete(f'{url}/{index}')
print(f'O modelo {nome_carro} da {marca} foi deletado.') """



# python requisicoes-test.py