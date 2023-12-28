import psycopg2

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


def registrar_musica(info):
    '''titulo = info[1]
    artista = info[2]
    file = info[3]
    id_artista = info[4]'''
    #enviando para DB
    try: 
        conexao = psycopg2.connect(
        host="seu_host",
        database="seu_banco_de_dados",
        user="seu_usuario",
        password="sua_senha"
        )
        cursor = conexao.cursor()
        sql_insercao = "INSERT INTO geral.musica_atual (titulo, autor, file) VALUES (%s, %s, %s)"
        dados = (str(info[1]), str(info[2]), str(info[3]))
        cursor.execute(sql_insercao, dados)
        conexao.commit()
        cursor.close()
        conexao.close()
    except Exception as erro:
        print(f'Erro no DB: {erro}')


musica = [('tit musica', 'artistao', 'arquivo')]
registrar_musica(musica)
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
    
    
    """