from kivy.app import App
from kivy.uix.boxlayout import BoxLayout #empilha os widgets em caixas

'''
as funções estão no arquivo teste.kv
O NOME DO ARQUIVO DEVE SER O MESMO DO APP.
'''
class Incrementador(BoxLayout):
    pass
class Teste(App):
    def build(self):        
        return Incrementador()
    
Teste().run()

#       python main2.py