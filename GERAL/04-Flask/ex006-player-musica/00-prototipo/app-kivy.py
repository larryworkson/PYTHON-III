from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen, ScreenManager
from controllers.player import Player_Manager
from controllers.DB_manager import consultar_musicas, consultar_artista, registrar_musica


class PlayerFixo(BoxLayout):
    def __init__(self, player, **kwargs):
        super(PlayerFixo, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.player = player #passa a instancia plauer para var tocador
        self.label = Label(text='', size_hint_y=None, height=30)
        self.btn = Button(text='Play', on_press=self.acao_btn, size_hint_y=None, height=100)

        self.add_widget(self.label)
        self.add_widget(self.btn)
    
    def acao_btn(self, instance):
        ''''''
        if self.player:
            self.btn.text = 'Play'
        else:
            self.btn.text = 'Pause'
        
    def atualizar_info_musica(self):
        pass
        


class TelaHome(Screen):
    def __init__(self, player, **kwargs):
        super(TelaHome, self).__init__(**kwargs)


        layout = BoxLayout(orientation='vertical')
        #objetos da tela
        label = Label(text='Home')
        btn01 = Button(text='Playlist01', on_press=self.ir_playlist_01)
        btn02 = Button(text='Playlist02', on_press=self.ir_playlist_02)

        self.player = player #passa a instancia player para var player
        #adição dos objetos
        layout.add_widget(label)
        layout.add_widget(btn01)
        layout.add_widget(btn02)
        self.add_widget(layout)

    
    def ir_playlist_01(self, intance):
        #tela playlist 01
        self.manager.current = 'Playlist01'

    def ir_playlist_02(self, instance):
        #tela playlist 2
        self.manager.current = 'Playlist02'

class Playlist01(Screen):
    def __init__(self, player, **kwargs):
        super(Playlist01, self).__init__(**kwargs)
        """Buscando dados do artista"""
        musicas = consultar_musicas('artista01', 'album01')

        layout = BoxLayout(orientation = 'vertical')
        label = Label(text=musicas[0][2])
        layout.add_widget(label)

        self.tocador = player #passa a instancia plauer para var tocador

        #musicas
        
        for musica in musicas:            
            play = Button(
                text=f'{musica[1]} - {musica[2]}', on_press=lambda instance, file=musica[3]: self.tocador.botao_play(instance, file, info=musica))
            layout.add_widget(play)
        #ui geral
        btn = Button(text='Home', on_press=self.ir_home)
        layout.add_widget(btn) #botap home
        self.add_widget(layout)

    def ir_home(self, instance):
        #voltar para home
        self.manager.current = 'Home'    

    

class Playlist02(Screen):
    def __init__(self, player, **kwargs):
        super(Playlist02, self).__init__(**kwargs)
        """Buscando dados do artista"""
        musicas = consultar_musicas('artista02', 'album01')
        layout = BoxLayout(orientation = 'vertical')
        label = Label(text=musicas[0][2])

        btn = Button(text='Home', on_press=self.ir_home)
        layout.add_widget(label)
        self.tocador = player #passa a instancia plauer para var tocador
        for musica in musicas:            
            play = Button(
                text=f'{musica[1]} - {musica[2]}', on_press=lambda instance, file=musica[3]: self.tocador.botao_play(instance, file, info=musica)) 
            layout.add_widget(play)
        
        layout.add_widget(btn)
        self.add_widget(layout)
    
    def ir_home(self, instance):
        #voltar para home
        self.manager.current = 'Home'

class MeuPlayer(App):
    def build(self):
        '''GERENCIADOR DE TELAS'''
        player = Player_Manager() #passando o objeto player para todas as telas, assim não há sobreposição de músicas
        telas = ScreenManager()
        telas.add_widget(TelaHome(player, name='Home'))
        telas.add_widget(Playlist01(player, name='Playlist01'))
        telas.add_widget(Playlist02(player, name='Playlist02'))

        '''LAYOUT COM TELA FIXA'''
        layout_princial = BoxLayout(orientation='vertical')
        layout_princial.add_widget(telas)
        layout_princial.add_widget(PlayerFixo(player))
        return layout_princial
    

MeuPlayer().run()

# python app-kivy.py

"""
01 - está gerando ERRO ao gravar as informações da música no DB pela função registrar_musica(info)
02 - para usar a função de pausar uma música, vou precisar adaptar trocar o SOUNDLOADER pelo PYGAME.
03 - Mostrar na tela inicial todos os artistas (artistas.lista). Cada artista deve ser um link para os álbuns. Esta deve ser uma classe construtora que gera a tela do artista com os albuns e músicas e adiciona no layout. Bem complexo.
04 - preciso criar uma tela fixa que tenha os dados da música os botões play/pause.
05 - tentar compilar o app pelo Linux mesmo, não tem jeito: https://www.youtube.com/watch?v=6gNpSuE01qE

"""