from kivy.core.audio import SoundLoader
from controllers.DB_manager import registrar_musica
import json
import pygame
from pygame import mixer


class Player_Manager:
    def __init__(self):
        self.musica_atual = None

    def botao_play(self, instance, file, info):
        if self.musica_atual:
            mixer.music.stop()
        try:
            mixer.init()
            mixer.music.load(file)
            mixer.music.play()
            #enviado dados da música arquivo json.
            registrar_musica(info)
        except Exception as erro:
            print(f'Erro ao reproduzir a música: {erro}')



        
        
    
    def reset(self):
        if self.musica_atual:
            self.musica_atual.stop()
            self.musica_atual = None
    
    def atualizar_info_musica(self):
        try:
            with open('C:/Users/studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex006-player-musica/00-prototipo/data/musica_atual.json', 'r') as arquivo:
                dados = json.load(arquivo)
        except Exception as erro:
            return print(f'Erro ao ler arquivo: {erro}')
        return dados

    
    




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