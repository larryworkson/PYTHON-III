Carros = [
    {
        'id': 1,
        'marca': 'Fiat',
        'modelo': 'Marea',
        'ano': 1999

    },
    {
        'id': 2,
        'marca': 'Fiat',
        'modelo': 'Uno',
        'ano': 1992

    },
    {
        'id': 3,
        'marca': 'Ford',
        'modelo': 'Escrot',
        'ano': 1985

    },
    {
        'id': 4,
        'marca': 'Hyundai',
        'modelo': 'HB20',
        'ano': 2023

    },
    {
        'id': 5,
        'marca': 'Tesla',
        'modelo': 'Model S',
        'ano': 2022

    },
    {
        'id': 6,
        'marca': 'Ferrari',
        'modelo': 'Enzo',
        'ano': 2012

    },
]
import json
nome_arquivo = 'C:/Users/studi/Documents/code/PYTHON-III/API REST/aulas/01-FLASK/banco.json'
try:
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(Carros, arquivo, indent=2)
        status = 'ok'
except Exception as erro:
    status = f'Erro ao gravar arquivo: {erro}'
finally:
    print(status)