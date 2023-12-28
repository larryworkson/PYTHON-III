from kivy.core.audio import SoundLoader
class Player_Manager:
    def __init__(self):
        self.musica_atual = None

    def botao_play(self, instance, file):    
        if self.musica_atual:
            self.musica_atual.stop()

        som = SoundLoader.load(file) #carrega e reproduz nova música
        if som:
            som.play()
            self.musica_atual = som
        else:
            print('Erro ao carregar a mídia.')
    
    def reset(self):
        if self.musica_atual:
            self.musica_atual.stop()
            self.musica_atual = None
    




#Instância é um objeto criado a partir de uma class.
        

"""  layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
self.musica_atual = None #var para armazenar nome da música em reprodução
musicas = [
    {'titulo': 'Música 01', 'autor': 'You Tubio', 'file': 'data/01.mp3'},
    {'titulo': 'Música 02', 'autor': 'Gogou', 'file': 'data/02.mp3'}
    ]
for musica in musicas:            
    button = Button(
        text=f'{musica["titulo"]} - {musica["autor"]}', on_press=lambda instance, file=musica["file"]: self.botao_pressionado(instance, file)) #self é aplicado para deixar a variável global
    layout.add_widget(button) """