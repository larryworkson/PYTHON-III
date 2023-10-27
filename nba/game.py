'''
Q1 = preciso do placar de dois times
Q2 = preciso verificar qual dos dois placares é o maior e adicionar 1 vitória ao vencedor.
Q3 = os times não podem ter placares iguais
Q4 = mostrar qual time venceu e por quantos pontos
Q5...
> adicionar times como dicionários em uma lista.
> adicionar aos times nome e vitórias (para gerar ranking)

'''
import sqlite3
from time import sleep
from funcNBA.cores import *
from funcNBA.funcoes import *
from random import choice

while True:
    print('[1] JOGAR')
    print('[2] TABELA')
    cor('[X] SAIR', 1)
    resp = str(input('Escolha: '))
    if resp in 'Xx':
        break
   
    if resp == '1':
        conexao = sqlite3.connect('C:/Users/studi/Documents/code/PYTHON-III/nba/gameDataBase.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM times')
        resultados = cursor.fetchall()
        if len(resultados) < 2:
            cor('ERRO, é necessário mais de 1 time para jogar.', 1)
        for i in range(0, (len(resultados) // 2)):
            t1 = choice(resultados)
            resultados.remove(t1)
            t2 = choice(resultados)
            resultados.remove(t2)
            game2(t1, t2)
            sleep(1)

        conexao.close()
        
    if resp == '2':
        conexao = sqlite3.connect('C:/Users/studi/Documents/code/PYTHON-III/nba/gameDataBase.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM times ORDER BY vit DESC')
        resultados = cursor.fetchall()
        titulo('~~~~~~ NATIONAL BASCKET ASSOCIATION ~~~~~~', 1)
        cor(f'{"ID:":<5} | {"POS:":<6} | {"Time":<20} | {"Vitórias":<10} | {"Força":<5}', 1)
        for pos, r in enumerate(resultados):
            print(f'\033[30m{r["id"]:<5}\033[m | {pos+1:>5}º | {r["nome"]:<20} | {r["vit"]:<10} | {r["forca"]:<5}') 
        conexao.close()

        while True:
            print('[1] CADASTRAR TIME')            
            print('[2] DELETAR TIME')
            print('[3] EDITAR TIME')
            print('[4] ZERAR VITÓRIAS/TIMES')
            print('[5] JOGADORES')
            cor('[X] SAIR', 1)
            resp2 = str(input('Escolha: '))           
            if resp2 == '1':
                time = {}
                time['nome'] = str(input('Nome: ').capitalize())
                time['forca'] = int(input('Força: '))
                addTime(time['nome'], 0, time['forca'])
                time.clear()
            if resp2 == '2':
                id = int(input('Digite a ID do time: '))
                delTime(id)
            if resp2 == '3':
                id = int(input('Digite o id do time: '))
                f = int(input('Definir força: '))
                editForca(id, f)

            if resp2 == '4':
                pg = str(input('Digite 1 para zerar vitórias ou 2 para excluir \033[1;31mTODOS\033[m os times: '))
                if pg == '1':
                    zeroVit()
                    cor('Vitórias zeradas', 2)
                elif pg == '2':
                    zeroTime()
                    cor('Times zerados', 2)
            if resp2 == '5':
                listaJogadores() #depois add id no () para puxar apenas jogadores de um time específico
                while True:
                    cor('[1] CADASTRAR JOGADOR', 4)
                    cor('[2] EDITAR NOME JOGADOR')
                    cor('[3] DELETAR JOGADOR', 1)
                    cor('[X] VOLTAR', 1)
                    resp3 = str(input('Escolha: '))
                    if resp3 in 'Xx':
                        break
                    if resp3 == '1':                        
                        nome = str(input('Nome jogador: ').strip())
                        media = float(input('Média de pts/jogo: '))
                        id_time = int(input('ID do time: '))
                        addJogador(nome, media, id_time)
                    elif resp3 == '2':
                        id = int(input('Digite o ID do jogador: '))
                        nome = str(input('Digite o novo nome do jogador: '))
                        updateJog(id, nome)
                    elif resp3 == '3':
                        id = int(input('Digite o ID do jogador: '))
                        delJog(id)


            if resp2 in 'Xx':
                break

#validar campos de input com leia int.
#criar menus mais inteligentes com funções e listas


"""
criar uma forma que os times jogem uns contra os outros numa sequência pegando todos os times cadastrados, sem repetir os confrontos.
criar um modo de jogo que eu escolho um time e as vítorias do time me geram dinheiro.
criar um modo de puxar estatícas dos últimos 5 jogos, quantas vítorias e quantas derrotas e contra quem jogou.
adicionar o t1, p1 t2, P2 em uma lista na coluna histórico do BD. 

NOVA DEFINIÇÃO DE PLACAR
O jogador possui uma média de pts/jogo, ex: 20pts. Aí todo game() gera um randint para cada jogador de 0 até a média do jogador. A soma da pontuação de cada jogador é o placar do time. Os jogadores devem ser add numa tabela separada 'jogadores'. E deve ter nome, forca, status, e time. O valor de time será o ID do time na tabela times.

DEFINIÇÃO DE STATUS (estado emocional)
Na tabela de jogadores, adicionar uma coluna 'status' com opção de nº inteiro: (-1)'desmotivado', (0)'normal' e (1)'motivado'. Se o jogador pontuar acima da metade de sua média, seu status sobe 1 degrau, se ele pontuar abaixo da metade da sua média, seu status desce um degrau.
Se um jogador fizer 10 pontos e seu status estiver (-1), ele perde 50% da pontuação. Exemplo: se o randint foi de 10, sua pontuação será 5.
Se o jogador fizer 10 pontos e seu status estiver (1), ele recebe +50% da pontuação. Exemplo: se o randint foi de 10, sua pontuação será 15.

Estratégia de jogo:
estratégias de ataque:
1) long range (3pt) 
2) midrange (2pts) 
3) garrafão (2pts)

estratégias de defesa:
1) perímetro > neutraliza estratégia de ataque 1
2) midrange > neutraliza estratégia de ataque 2
3) garrafão > neutraliza estratégia de ataque 3

O time que tiver uma estratégia de ataque que não seja neutralizada ganha um incremento % na sua pontuação, de acordo com a diferença de força.
ex: se o time A tem 80 de força e o time B tem 90, e se a estratégia de ataque não for neutralizada, o time ganhará um incremente de 10% na pontuação.

força por jogadores:
 jogadores adicionar uma coluna no bd com  uma lista. Dentro da lista, cadastrar os jogadores como dicionários, com nome, ataque, defesa e overal. Fazer a média das habilidades para gerar a força do time
 
 """

