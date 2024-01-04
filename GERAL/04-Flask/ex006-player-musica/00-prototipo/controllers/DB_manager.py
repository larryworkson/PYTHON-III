import psycopg2
import json

#criando tabela
def consultar_musicas(artista, album):
    db_params = {
        'host': 'localhost',
        'port': '5432',
        'user': 'postgres',
        'password': 'djcr92',
        'database': 'musicteste',
    }
    try:
        conexao = psycopg2.connect(**db_params)
        cursor = conexao.cursor()
        cursor.execute(f'SELECT * FROM {artista}.{album};')
        resultados = cursor.fetchall()
        """ for item in resultados:
            print(f'{item[1]}') """

    except Exception as erro:
        print(f'Erro de conexão ao DB: {erro}')

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
    return resultados

def consultar_lista_artista():
    db_params = {
        'host': 'localhost',
        'port': '5432',
        'user': 'postgres',
        'password': 'djcr92',
        'database': 'musicteste',
    }
    try:
        conexao = psycopg2.connect(**db_params)
        cursor = conexao.cursor()
        cursor.execute(f'SELECT * FROM artistas.lista;')
        resultados = cursor.fetchall()

    except Exception as erro:
        print(f'Erro de conexão ao DB: {erro}')

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
    return resultados

def show_albuns(id):
    print(f'ID do artista: {id}')
    db_params = {
        'host': 'localhost',
        'port': '5432',
        'user': 'postgres',
        'password': 'djcr92',
        'database': 'musicteste',
    }
    try:
        conexao = psycopg2.connect(**db_params)
        cursor = conexao.cursor()
        cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'artista{id}';") 
        
        nomes_albuns = cursor.fetchall() #[row[0] for row in cursor.fetchall()]



    except Exception as erro:
        print(f'Erro de conexão ao DB: {erro}')

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

    return nomes_albuns


def registrar_musica(dados):
    nome_arquivo = './data/musica_atual.json'
    try:
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=2)
        #return print(f'Dados: {dados} gravados com sucesso!')
    except Exception as erro:
        return print(f'Erro ao gravar arquivo: {erro}')
    




""" 
python DB_manager.py
    
SQL
CREATE SCHEMA artistas

CREATE TABLE artistas.musicas (
	id serial PRIMARY KEY,
	titulo VARCHAR(100),
	autor VARCHAR(100),
	file VARCHAR(250)
)

select * from artistas.musicas

INSERT INTO artistas.musicas (
	titulo, autor, file)
	VALUES ('Little Umbrellas', 'TrackTribe',
			'C:/Users/studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex006-player-musica/00-prototipo/data/Little Umbrellas - TrackTribe.mp3')
    
    
            
            (2, 'Limousines', 'TrackTribe', 'C:/Users/studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex006-player-musica/00-prototipo/data/Limousines - TrackTribe.mp3', 2)
    """