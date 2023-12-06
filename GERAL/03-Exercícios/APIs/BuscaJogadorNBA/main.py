"""programa pesquisa pelo nome de um jogador da NBA e traz seu nome, PPG e time atual."""

from controls import pesqGoogle
while True:
    print('-'*30)
    print('Digite N para finalizar.')
    print('-'*30)
    pesquisa = input(str('Pesquisa por: '))
    query = f'{pesquisa} nba stats'
    if pesquisa.lower() == 'n':
        break
    pesqGoogle.pesquisar(pesquisa)
    print('-'*30)



"""
não estou conseguindo puxar a minutagem do jogador.  A lista que deveria puxar os itens da tabela retorna vazia.
 ver uma forma de puxar imagens do jogador e o logo do time.
criar uma interface gráfica no flask """