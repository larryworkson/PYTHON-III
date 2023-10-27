from time import sleep
from funcNBA.cores import *
from random import randint
import sqlite3

def game2(t1, t2):
    #puxando dados jogadores
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, media FROM jogadores WHERE idtime = ?', (t1["id"],))
    resultados = cursor.fetchall()
    players_t1 = []
    player_t1 = {}
    #para cada jogador do t1 vamos colocá-lo em uma lista com pontuação e nome.
    for jog in resultados:
        pts = randint(0, int(round(jog['media'])))
        player_t1['nome'] = jog['nome']
        player_t1['pts'] = pts
        players_t1.append(player_t1.copy())
        player_t1.clear()
    #somando pontuação t1
    ptst1 = 0
    for i in players_t1:
        ptst1 += i['pts']
    #para cada jogador do t2 vamos colocá-lo em uma lista com pontuação e nome.
    cursor.execute('SELECT nome, media FROM jogadores WHERE idtime = ?', (t2["id"],))
    result2 = cursor.fetchall()
    players_t2 = []
    player_t2 = {}
    for player in result2:
        pts2 = randint(0, int(round(player['media'])))
        player_t2['nome'] = player['nome']
        player_t2['pts'] = pts2
        players_t2.append(player_t2.copy())
        player_t2.clear()
    #somando pontuação t2
    ptst2 = 0
    for p in players_t2:
        ptst2 += p['pts']

    #placar
    titulo(f'{"JOGOS":^40}', 2)
    sleep(1)
    print(f'{t1["nome"]:<16} {ptst1:.0f} x {ptst2:.0f} {t2["nome"]:>16}')
    titulo(f'{"Pontuadores":^40}', 4)
    for a in players_t1:
        print(f'{a["nome"]:<20} | {a["pts"]:>10} pts')
    for b in players_t2:
        print(f'{b["nome"]:<20} | {b["pts"]:>10} pts')
    
    #gerando vitórias
    if ptst1 > ptst2:
        updateTime(t1['id'], 1)
    elif ptst2 > ptst1:
        updateTime(t2['id'], 1)
        
    conexao.close()

def game(t1, t2):
    """
    --> t1 = time 1 vs t2 = time 2
    p1, p2 = geram o placar aletório
    Um condição verifica qual time é mais forte. Aquele que é mais forte recebe a diferença de força (int) como percentual de acréscimo a pontuação.
    Ex: se o t1 tem forca = 80 e t2 tem forca = 70, o t1 recebe 10% (80-70) a mais de pontos ao p1.
    depois de printar os placares a condição final faz o update do BD conforme o resultado, acrescentando 1 vitória ao time pela função updateTime()

    """


    while True:
        sleep(1)
        p1 = randint(90, 110)
        p2 = randint(90, 110)
        cor(f'P1: {p1}', 4)
        cor(f'P2: {p2}', 3)
        if t1['forca'] > t2['forca']:
            p1 += (t1['forca'] - t2['forca']) / 100 * p1
        if t2['forca'] > t1['forca']:
            p2 += (t2['forca'] - t1['forca']) / 100 * p2        
        cor('------ JOGOS ------', 2)
        print(f'{t1["nome"]} {p1:.0f} x {p2:.0f} {t2["nome"]}')
        cor('~'*20, 2)        
        if p1 > p2:
            updateTime(t1['id'], 1)
            break
        elif p2 > p1:
            updateTime(t2['id'], 1)
            break

def updateTime(dado, v=0,):
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db')
    cursor = conexao.cursor()
    id = dado
    cursor.execute('SELECT nome, vit FROM times WHERE id = ?', (id,))
    vitAtual = cursor.fetchone()[1]
    novaVit = vitAtual + v
    cursor.execute('UPDATE times SET vit = ? WHERE id = ?', (novaVit, id))
    conexao.commit()
    conexao.close()

def updateJog(dado, nome=''):
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db')
    cursor = conexao.cursor()
    id = dado
    cursor.execute('SELECT nome FROM jogadores WHERE id = ?', (id,))
    novo_nome = nome
    cursor.execute('UPDATE jogadores SET nome = ? WHERE id = ?', (novo_nome, id))
    cor('Jogador editado com sucesso!', 2)
    conexao.commit()
    conexao.close()

def zeroVit():
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db')
    cursor = conexao.cursor()
    cursor.execute('UPDATE times SET vit = 0')
    conexao.commit()
    conexao.close()

def editForca(dado, forca):
    id = dado
    f = forca
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db')
    cursor = conexao.cursor()
    cursor.execute('UPDATE times SET forca = ? WHERE id = ?', (f, id))
    cor('Time atualizado', 2)
    conexao.commit()
    conexao.close()

def zeroTime():
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM times')
    conexao.commit()
    conexao.close()

def addTime(n='sem nome', v=0, f=0):
        conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db')
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS times (id INTEGER PRIMARY KEY, nome TEXT, vit INTEGER, forca INTEGER)''')
        listaDados = []
        cadastro = {}
        cadastro['nome'] = n
        cadastro['vit'] = v
        cadastro['forca'] = f
        listaDados.append(cadastro)
        for cadastro in listaDados:
            cursor.execute('INSERT INTO times (nome, vit, forca) VALUES (:nome, :vit, :forca)', cadastro)
        cor('Dados cadastrados com suceso!', 2)
        conexao.commit()
        conexao.close()

def addJogador(n, m, t):
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db')
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS jogadores (id INTEGER PRIMARY KEY, nome TEXT, media FLOAT, status INTEGER, forca INTEGER, idtime INTEGER)')
    listaDados = []
    cadastro = {}
    cadastro['nome'] = n
    cadastro['media'] = m
    cadastro['status'] = 0
    cadastro['forca'] = 0
    cadastro['idtime'] = t
    listaDados.append(cadastro)
    for cadastro in listaDados:
        cursor.execute('INSERT INTO jogadores (nome, media, idtime) VALUES (:nome, :media, :idtime)', cadastro)
        cor('Jogador cadastrado com sucesso!', 2)
    conexao.commit()
    conexao.close()

def listaJogadores():
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM jogadores ORDER BY idtime')
    resultados = cursor.fetchall()
    for jogador in resultados:
        cursor.execute('SELECT nome FROM times WHERE id = ?', (jogador["idtime"],))
        times = cursor.fetchone()
        print(f'{jogador["id"]:<3} | {jogador["nome"]:<25} | {jogador["media"]:>5} | {times["nome"]:<15} | {jogador["status"]}')
    conexao.close()

def delTime(id):
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM times WHERE id = ?', (id,))
    cor('Time deletado!', 2)
    conexao.commit()
    conexao.close()

def delJog(id):
    conexao = sqlite3.connect('E:/Workspace/_CODE/PYTHON/NBA/gameDataBase.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM jogadores WHERE id = ?', (id,))
    cor('Jogador deletado!', 2)
    conexao.commit()
    conexao.close()