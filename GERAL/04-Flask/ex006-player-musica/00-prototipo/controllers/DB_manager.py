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

def consultar_artista():
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


def registrar_musica(dados):
    nome_arquivo = './data/musica_atual.json'
    try:
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=2)
        #return print(f'Dados: {dados} gravados com sucesso!')
    except Exception as erro:
        return print(f'Erro ao gravar arquivo: {erro}')
    
    """ titulo = tuple[1].encode('utf-8')
    artista = tuple[2].encode('utf-8')
    file = tuple[3].encode('utf-8')
    #id_artista = tuple[4].encode('utf-8')
    #enviando para DB
    #try: 
    conexao = psycopg2.connect(
    host="seu_host",
    database="seu_banco_de_dados",
    user="seu_usuario",
    password="sua_senha",
    encoding = "utf-8"
    )
    cursor = conexao.cursor()
    sql_insercao = "INSERT INTO geral.musica_atual (titulo, autor, file) VALUES (%s, %s, %s)"
    dados = (titulo, artista, file)
    cursor.execute(sql_insercao, dados)
    conexao.commit()
    cursor.close()
    conexao.close()
    #except Exception as erro:
       #print(f'Erro no DB: {erro}') """



""" 
python DB_manager.py
musica = {'id': 2,'titulo': 'musica 2', 'autor': 'quem toca', 'file': 'arquivo/caminho/c:'}
registrar_musica(musica)
    
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