from kivy.core.audio import SoundLoader
class Player_Manager:
    def __init__(self):
        self.musica_atual = None

    def botao_play(self, file):    
        if self.musica_atual:
            self.musica_atual.stop()

        som = SoundLoader.load(file) #carrega e reproduz nova música
        if som:
            som.play()
            self.musica_atual = som
        else:
            print('Erro ao carregar a mídia.')




        


"""     def botao_pressionado(self, instance, file):
        função que executa script quando a música é clicada
        if self.musica_atual: #interrompe se houve uma reprodução em andamento.
            self.musica_atual.stop()
        som = SoundLoader.load(file) #carrega e reproduz nova música
        if som:
            som.play()
            print(f'Tocando... {instance.text}')
            self.musica_atual = som #atualiza a variável som com a musica atual
        else:
            print('Erro ao carregar a mídia.') """