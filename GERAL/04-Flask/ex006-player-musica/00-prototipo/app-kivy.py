from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader

class MeuPlayer(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.musica_atual = None #var para armazenar nome da música em reprodução
        musicas = [
            {'titulo': 'Música 01', 'autor': 'You Tubio', 'file': 'data/01.mp3'},
            {'titulo': 'Música 02', 'autor': 'Gogou', 'file': 'data/02.mp3'}
            ]
        for musica in musicas:            
            button = Button(
                text=f'{musica["titulo"]} - {musica["autor"]}', on_press=lambda instance, file=musica["file"]: self.botao_pressionado(instance, file)) #self é aplicado para deixar a variável global
            layout.add_widget(button)
        
        return layout
    
    def botao_pressionado(self, instance, file):
        if self.musica_atual: #interrompe se houve uma reprodução em andamento.
            self.musica_atual.stop()
       

        som = SoundLoader.load(file) #carrega e reproduz nova música
        if som:
            som.play()
            print(f'Tocando... {instance.text}')
            self.musica_atual = som #atualiza a variável som com a musica atual
        else:
            print('Erro ao carregar a mídia.')

MeuPlayer().run()

# python app-kivy.py

"""
- falta entender a class ScreenManager para criar telas diferentes e testar a navegação durante execução de uma música.
- tentar compilar o app pelo Linux mesmo, não tem jeito: https://www.youtube.com/watch?v=6gNpSuE01qE

"""