from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from controllers.player import Player_Manager
from controllers.DB_manager import consultar_musicas, consultar_lista_artista, show_albuns
from functools import partial


class PlayerFixo(BoxLayout):
    def __init__(self, player, **kwargs):
        super(PlayerFixo, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.btn = Button(text='', on_press=self.acao_btn, size_hint_y=None, height=100)

        #atualizando label
        musica_atual = Player_Manager.atualizar_info_musica(self)
        if musica_atual:
            self.label = Label(text=f'{musica_atual[1]} | {musica_atual[2]}', size_hint_y=None, height=30)
        
        self.player = player #passa a instancia player para var player para acessar a class PLAYER MANAGER.
        #mudança do botão
        if self.player:
            self.btn.text = 'Play'

        else:
            self.btn.text = 'Pause'

        # ITENS DA INTERFACE
        self.add_widget(self.label)
        self.add_widget(self.btn)
        
    
    def acao_btn(self, instance):
        pass
        
            

class TelaHome(Screen):
    def __init__(self, player, **kwargs):
        super(TelaHome, self).__init__(**kwargs)


        layout = BoxLayout(orientation='vertical')
        #objetos da tela
        label = Label(text='Home')
        btn01 = Button(text='Playlist01', on_press=self.ir_playlist_01)
        btn02 = Button(text='Playlist02', on_press=self.ir_playlist_02)
        btn03 = Button(text='Nova Home', on_press=self.nova_home)

        self.player = player #passa a instancia player para var player
        #adição dos objetos
        layout.add_widget(label)
        layout.add_widget(btn01)
        layout.add_widget(btn02)
        layout.add_widget(btn03)
        self.add_widget(layout)

    
    def ir_playlist_01(self, intance):
        #tela playlist 01
        self.manager.current = 'Playlist01'

    def ir_playlist_02(self, instance):
        #tela playlist 2
        self.manager.current = 'Playlist02'

    def nova_home(self, instance):
        #tela artistas (tela inicial)
        self.manager.current = 'TelaInicial'

class Playlist01(Screen):
    def __init__(self, player, **kwargs):
        super(Playlist01, self).__init__(**kwargs)
        """Buscando dados do artista"""
        musicas = consultar_musicas('artista1', 'album01')

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
        musicas = consultar_musicas('artista2', 'album01')
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

class TelaInicial(Screen):
    def __init__(self, **kwargs):
        super(TelaInicial, self).__init__(**kwargs)
        '''Buscando artistas no db'''
        artistas = consultar_lista_artista()
        layout = BoxLayout(orientation='vertical')

        for artista in artistas:
            btn = Button(text=f'{artista[1]}', on_press=lambda instance, x=artista[0]: self.ir_albuns(x))
            layout.add_widget(btn)
        
        btn_home = Button(text='Home', on_press=self.ir_home)
        layout.add_widget(btn_home)
        self.add_widget(layout)
    
    def ir_home(self, instance):
        #voltar para home
        self.manager.current = 'Home'
    def ir_albuns(self, id_artista):
        #tela albuns
        self.manager.current = 'TelaAlbum'
        self.manager.get_screen('TelaAlbum').buscar_albuns(id_artista)

class TelaAlbum(Screen):
    def __init__(self, **kwargs):
        super(TelaAlbum, self).__init__(**kwargs)
        #layout = BoxLayout(orientation = 'vertical')
        layout = GridLayout(cols=1, spacing=5)

        btn_home = Button(text='Voltar', on_press=self.nova_home, size_hint=(1, None), size=(100, 40))
        #btn_home.pos_hint = {'bottom': 1}
        layout.add_widget(btn_home)
        self.add_widget(layout)
    
    def nova_home(self, instance):
        #tela artistas (tela inicial)
        self.manager.current = 'TelaInicial'
    
    def buscar_albuns(self, id_artista):
        albuns = show_albuns(id_artista)
        nome_artista = Label(text='Nome Artista', size_hint=(1, 0.5), size=(100, 40))
        self.add_widget(nome_artista)
        for albun in albuns:
            btn = Button(text=f'{albuns[0][0]}', size_hint=(1, 0.2), size=(100, 40))
            self.add_widget(btn)
#       python app-kivy.py
    """ def buscar_albuns(self, id_artista):
        buttons = BoxLayout(orientation = 'vertical')
        albuns = show_albuns(id_artista)
        print(len(albuns))
        for album in albuns :
            btn = Button(text=f'{album[0]}', size_hint_y=None, height=100)
            buttons.add_widget(btn)
        self.add_widget(buttons) """
    
        




class MeuPlayer(App):
    def build(self):
        '''GERENCIADOR DE TELAS'''
        player = Player_Manager() #passando o objeto player para todas as telas, assim não há sobreposição de músicas

        telas = ScreenManager()
        telas.add_widget(TelaHome(player, name='Home'))
        telas.add_widget(Playlist01(player, name='Playlist01'))
        telas.add_widget(Playlist02(player, name='Playlist02'))
        telas.add_widget(TelaInicial(name='TelaInicial'))
        telas.add_widget(TelaAlbum(name='TelaAlbum'))

        '''LAYOUT COM TELA FIXA'''
        layout_princial = BoxLayout(orientation='vertical')
        layout_princial.add_widget(telas)
        layout_princial.add_widget(PlayerFixo(player))
        return layout_princial
    

MeuPlayer().run()

#       python app-kivy.py                python  main.py

"""
IDEIA: streaming  de música FREE sem anúncios. Ele pega todas as músicas free e organiza em playlists de generos. Organizando também por artistas, albuns etc. As recomendações de músicas são feitas pela IA baseadas no histórico do usuário + os likes dados nas músicas favoritas. O app é para quem quer ouvir uma música qualquer sem pagar nada e sem anúncios. Ideal para concentração no trabalho. Também o app pode ser um canal de divulgação de novas bandas (indie).

00 - Quando entro no artista só mostra o 1 álbum de cada. Devem aparecer todos.
01 - Mostrar na tela inicial todos os artistas (artistas.lista). Cada artista deve ser um link para os álbuns. Esta deve ser uma classe construtora que gera a tela do artista com os albuns e músicas e adiciona no layout. Bem complexo.
A função que gera a tela do artista precisa ser configurada com label esse label vai receber o nome do artista. A função também irá receber o catálago com os álbuns do artista, e cada album deve receber o link das músicas para tocalas. São 3 telas > Artistas > Álbuns > Músicas. Cada um passará as infos para o outro com funções.
    > ARTISTAS: lista com nome de todos eles
    > ÁLBUNS: lista das tabelas (albuns) do artista (puxa o nome do artista da tela anterior)
    > ALBUM: lista de músicas, puxando o nome do álbum da tela anterior. As músicas vão ter o tão play (já configurado)

02 - o botão play não sendo alterado pq a variável play é sempre verdadeira. Preciso jogar um boolean nela para condicionar o botão.
03 - o label da música precisa ser atualizado a cada play, assim como o botão PLAY/PAUSE deve fazer a mudança. Parece que o sistema ainda precisa reconhecer quando tem uma música rodando.
04 - tentar compilar o app pelo Linux mesmo, não tem jeito: https://www.youtube.com/watch?v=6gNpSuE01qE

"""