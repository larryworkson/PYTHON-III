from flask import Flask, make_response, jsonify, request
from bd import Carros
import json
from collections import OrderedDict

app = Flask(__name__) #instância do site
app.config['JSON_SORT_KEYS'] = False #não funcionou

def banco_dados():
    with open('C:/Users/studi/Documents/code/PYTHON-III/API REST/aulas/01-FLASK/banco.json', 'r') as arquivo: 
          data = json.load(arquivo, object_pairs_hook=OrderedDict) #ordenando o response na ordem original e não alfabética
    return data

@app.route('/carros', methods=['GET'])
def get_carros():
    '''make_response: cria um response de API e o jsonify cria um arquivo json com os dados puxados do BD.'''
    dados = banco_dados()
    return  make_response(jsonify(dados))

@app.route('/carros', methods=['POST'])
def create_carro():
    '''função para adicionar dados no banco de dados'''
    novo_carro = request.json #puxando dados enviados pela requisição POST
    #Carros.append(carro)
    dados_existentes = banco_dados()
    
    '''gravando dados no json'''
    nome_arquivo = 'C:/Users/studi/Documents/code/PYTHON-III/API REST/aulas/01-FLASK/banco.json'
    try:
        dados_existentes.append(novo_carro)
        with open(nome_arquivo, 'w') as file:
            json.dump(dados_existentes, file, indent=2)
            status = 'Dados gravados!'
    except Exception as erro:
        status = f'Erro ao gravar dados: {erro}'
    finally:
        print(status)
    return jsonify(status=status)

@app.route('/carros/<int:index>', methods=['DELETE'])
def delete_carro(index):
    '''função deleta o carro pelo índice'''
    nome_arquivo = 'C:/Users/studi/Documents/code/PYTHON-III/API REST/aulas/01-FLASK/banco.json'
    dados_existentes = banco_dados()
    #verificando se o index é válido
    if index >=0 and index < len(dados_existentes):
        carro_removido = dados_existentes.pop(index)
        try:
            with open(nome_arquivo, 'w') as file:
                json.dump(dados_existentes, file, indent=2)
            status = f'Carro {carro_removido} removido!'
        except Exception as erro:
            status = f'Erro ao deletar carro: {erro}'
    else:
        status = 'Índice inválido'
    print(status)
    return jsonify(status=status)


app.run(debug=True) #rodar o app

# python main.py

"""
- add função put
- a ordem dos dados no response está alfabética
"""