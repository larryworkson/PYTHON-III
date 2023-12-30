from flask import Flask, make_response, jsonify, request
from bd import Carros
import json


app = Flask(__name__) #instância do site

def banco_dados():
      with open('C:/Users/studi/Documents/code/PYTHON-III/API REST/aulas/01-FLASK/banco.json', 'r') as arquivo: 
          dados = json.load(arquivo)
          return dados

@app.route('/carros', methods=['GET'])
def get_carros():
    '''make_response: cria um response de API e o jsonify cria um arquivo json com os dados puxados do BD.'''
    dados = banco_dados()
    return dados #make_response(jsonify(Carros))

@app.route('/carros', methods=['POST'])
def create_carro():
    '''função pega os dados e insere no banco de dados'''
    novo_carro = request.json #puxando dados enviados pela requisição POST
    #Carros.append(carro)

    '''gravando dados no json'''
    nome_arquivo = 'C:/Users/studi/Documents/code/PYTHON-III/API REST/aulas/01-FLASK/banco.json'
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados_existentes = json.load(arquivo)
            dados_existentes.append(novo_carro)
    except Exception as e:
        print(f'ERRO: {e}')
    
    try:
        with open(nome_arquivo, 'w') as file:
            json.dump(dados_existentes, file, indent=2)
            status = 'Dados gravados!'
    except Exception as erro:
        status = f'Erro ao gravar dados: {erro}'
    finally:
        print(status)
    return novo_carro


app.run(debug=True) #rodar o app

# python main.py

"""
a requisição POST não está gravando os dados no arquivo json. TALVEZ seja uma questão de segurança ou estas requisições não devem gravar dados.
"""