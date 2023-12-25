from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen, ScreenManager


class TelaHome(Screen):
    def __init__(self, **kwargs):
        super(TelaHome, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Home')
        btn01 = Button(text='Playlist 01', on_press=self.ir_playlist_01)
        btn02 = Button(text='Playlist 02', on_press=self.ir_playlist_02)

        layout.add_widget(label)
        layout.add_widget(btn01)
        layout.add_widget(btn02)
        self.add_widget(layout)

    def botao_pressionado(self, instance, file):
        """função que executa script quando a música é clicada"""
        if self.musica_atual: #interrompe se houve uma reprodução em andamento.
            self.musica_atual.stop()
        som = SoundLoader.load(file) #carrega e reproduz nova música
        if som:
            som.play()
            print(f'Tocando... {instance.text}')
            self.musica_atual = som #atualiza a variável som com a musica atual
        else:
            print('Erro ao carregar a mídia.')
    
    def ir_playlist_01(self, intance):
        #tela playlist 01
        self.manager.current = 'Playlist01'

    def ir_playlist_02(self, instance):
        #tela playlist 2
        self.manager.current = 'Playlist02'

class Playlist01(Screen):
    def __init__(self, **kwargs):
        super(Playlist01, self).__init__(**kwargs)
        layout = BoxLayout(orientation = 'vertical')
        label = Label(text='Playlist 01')
        layout.add_widget(label)
        #musicas
        self.musica_atual = None #var para armazenar nome da música em reprodução
        musicas = [
            {'titulo': 'Música 01', 'autor': 'You Tubio', 'file': 'data/01.mp3'},
            {'titulo': 'Música 02', 'autor': 'Gogou', 'file': 'data/02.mp3'}
            ]
        for musica in musicas:            
            play = Button(
                text=f'{musica["titulo"]} - {musica["autor"]}', on_press=lambda instance, file=musica["file"]: self.botao_pressionado(instance, file)) #self é aplicado para deixar a variável global
            layout.add_widget(play)
        #ui geral
        btn = Button(text='Home', on_press=self.ir_home)
        layout.add_widget(btn) #botap home
        self.add_widget(layout)

    def botao_pressionado(self, instance, file):
        """função que executa script quando a música é clicada"""
        if self.musica_atual: #interrompe se houve uma reprodução em andamento.
            self.musica_atual.stop()
        som = SoundLoader.load(file) #carrega e reproduz nova música
        if som:
            som.play()
            print(f'Tocando... {instance.text}')
            self.musica_atual = som #atualiza a variável som com a musica atual
        else:
            print('Erro ao carregar a mídia.')


    def ir_home(self, instance):
        #voltar para home
        self.manager.current = 'Home'    

    

class Playlist02(Screen):
    def __init__(self, **kwargs):
        super(Playlist02, self).__init__(**kwargs)
        layout = BoxLayout(orientation = 'vertical')

        label = Label(text='Playlist 02')
        btn = Button(text='Home', on_press=self.ir_home)
        layout.add_widget(label)
        
        self.musica_atual = None #var para armazenar nome da música em reprodução
        musicas = [
            {'titulo': 'Música 01', 'autor': 'Ivan Inacio', 'file': 'data/01.mp3'},
            {'titulo': 'Música 02', 'autor': 'Mahamadou', 'file': 'data/02.mp3'}
            ]
        for musica in musicas:            
            play = Button(
                text=f'{musica["titulo"]} - {musica["autor"]}', on_press=lambda instance, file=musica["file"]: self.botao_pressionado(instance, file)) #self é aplicado para deixar a variável global
            layout.add_widget(play)
        
        layout.add_widget(btn)
        self.add_widget(layout)

    def botao_pressionado(self, instance, file):
        """função que executa script quando a música é clicada"""
        if self.musica_atual: #interrompe se houve uma reprodução em andamento.
            self.musica_atual.stop()
        som = SoundLoader.load(file) #carrega e reproduz nova música
        if som:
            som.play()
            print(f'Tocando... {instance.text}')
            self.musica_atual = som #atualiza a variável som com a musica atual
        else:
            print('Erro ao carregar a mídia.')
    
    def ir_home(self, instance):
        #voltar para home
        self.manager.current = 'Home'

class MeuPlayer(App):
    def build(self):
        telas = ScreenManager()
        telas.add_widget(TelaHome(name='Home'))
        telas.add_widget(Playlist01(name='Playlist01'))
        telas.add_widget(Playlist02(name='Playlist02'))
        return telas

"""  layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
    self.musica_atual = None #var para armazenar nome da música em reprodução
    musicas = [
        {'titulo': 'Música 01', 'autor': 'You Tubio', 'file': 'data/01.mp3'},
        {'titulo': 'Música 02', 'autor': 'Gogou', 'file': 'data/02.mp3'}
        ]
    for musica in musicas:            
        button = Button(
            text=f'{musica["titulo"]} - {musica["autor"]}', on_press=lambda instance, file=musica["file"]: self.botao_pressionado(instance, file)) #self é aplicado para deixar a variável global
        layout.add_widget(button) 
    
    
    
def botao_pressionado(self, instance, file):
    if self.musica_atual: #interrompe se houve uma reprodução em andamento.
        self.musica_atual.stop()
    

    som = SoundLoader.load(file) #carrega e reproduz nova música
    if som:
        som.play()
        print(f'Tocando... {instance.text}')
        self.musica_atual = som #atualiza a variável som com a musica atual
    else:
        print('Erro ao carregar a mídia.') """

MeuPlayer().run()

# python app-kivy.py

"""
- ao tocar a musica de uma playlit e depois clicar em outra playlist tocar outra música, elas estão tocando simultaneamente.
- falta entender a class ScreenManager para criar telas diferentes e testar a navegação durante execução de uma música.
- tentar compilar o app pelo Linux mesmo, não tem jeito: https://www.youtube.com/watch?v=6gNpSuE01qE

"""