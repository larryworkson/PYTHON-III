import socket
def internetAcesso():
    try:
        socket.create_connection(("www.pudim.com.br", 80))
        print('\033[32mConectado! Acessei o site.\033[m')
    except OSError:
        print('\033[31mNão consegui acessar o site. Sem acesso a internet.\033[m')


internetAcesso()