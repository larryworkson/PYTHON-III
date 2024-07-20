import sqlite3
import pandas as pd

def ativar_db(exec='', id='', commit=False, conteudo = 'all'):
        """esta função abre e fecha o db e retorna valores        
        :exec = é comando que deve ser executado no DB
        :id = caso a execução seja em uma linha específica
        :commit = True para alteração no BD. False para consulta
        :conteudo = 'all' para fetchall ou 'one' para fetchone
        """

        conexao = sqlite3.connect('C:/CODE/PYTHON-III/DATA-SCIENCE/dataenv/00-modelo-nba/data/base.db')                
        cursor = conexao.cursor()
        
        #verificando se executa em uma linha ou geral
        if id != '':
            cursor.execute(f'{exec}', (int(id),))
        else:
            cursor.execute(f'{exec}')

        #verificando se pega um item ou todos
        if conteudo == 'one':
            valores = cursor.fetchone()
        else:
            valores = cursor.fetchall()
        
        #verificando se fará alteração no banco
        if commit == True:
            conexao.commit()
        
        conexao.close()
        return valores

def ativar_db_2(exec='', id='', commit=False, conteudo = 'all'):
        """esta função abre e fecha o db e retorna valores        
        :exec = é comando que deve ser executado no DB
        :id = caso a execução seja em uma linha específica
        :commit = True para alteração no BD. False para consulta
        :conteudo = 'all' para fetchall ou 'one' para fetchone
        """

        conexao = sqlite3.connect('C:/CODE/PYTHON-III/DATA-SCIENCE/dataenv/00-modelo-nba/data/base-2.db')                
        cursor = conexao.cursor()
        
        #verificando se executa em uma linha ou geral
        if id != '':
            cursor.execute(f'{exec}', (int(id),))
        else:
            cursor.execute(f'{exec}')

        #verificando se pega um item ou todos
        if conteudo == 'one':
            valores = cursor.fetchone()
        else:
            valores = cursor.fetchall()
        
        #verificando se fará alteração no banco
        if commit == True:
            conexao.commit()
        
        conexao.close()
        return valores


def enviar_db(exec='', action='', **kwargs):
    """adiciona e edita itens no DB
    :exec = é comando que deve ser executado no DB
    :id = KEY
    :commit = True para alteração no BD. False para consulta"""
    conexao = sqlite3.connect('C:/CODE/PYTHON-III/DATA-SCIENCE/dataenv/00-modelo-nba/data/base.db')

    cursor = conexao.cursor()
    cursor.execute(exec)
    lista = []
    lista.append(kwargs)
    for kwargs in lista:        
            cursor.execute(action, kwargs)
    conexao.commit()
    conexao.close()

def enviar_db_2(exec='', action='', **kwargs):
    """adiciona e edita itens no DB
    :exec = é comando que deve ser executado no DB
    :id = KEY
    :commit = True para alteração no BD. False para consulta"""
    conexao = sqlite3.connect('C:/CODE/PYTHON-III/DATA-SCIENCE/dataenv/00-modelo-nba/data/base-2.db')

    cursor = conexao.cursor()
    cursor.execute(exec)
    lista = []
    lista.append(kwargs)
    for kwargs in lista:        
            cursor.execute(action, kwargs)
    conexao.commit()
    conexao.close()

def base():
    conn = sqlite3.connect('C:/CODE/PYTHON-III/DATA-SCIENCE/dataenv/00-modelo-nba/data/base.db')
    query = "SELECT * FROM jogadores"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def base_2():
    conn = sqlite3.connect('C:/CODE/PYTHON-III/DATA-SCIENCE/dataenv/00-modelo-nba/data/base-2.db')
    query = "SELECT * FROM jogadores"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

""" consulta = base()
print(consulta)
id = int(input('What ID?: '))
if id != 'nN':
    ativar_db(exec='DELETE FROM jogadores WHERE id = ?', id=id, commit=True)
else:
    pass """
