from kivy.app import App
from kivy.uix.boxlayout import BoxLayout #empilha os widgets em caixas
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

'''
as funções estão no arquivo teste.kv
O NOME DO ARQUIVO DEVE SER O MESMO DO APP.
'''
class Task(ScrollView):
    def __init__(self, tarefas, **kwargs): #keyword arguments
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size=30, size_hint_y=None, height=200)) #self vai add widgets no BoxLayout.
class Tarefas(App):
    def build(self):        
        return Task(['Fazer compras', 'Buscar filho', 'Molhar calçada', 'Ir médico', 'Comprar arroz', 'Buscar o bolo', 'Reservar passagem', 'Dormir 30 min'])
    
Tarefas().run()

#       python tarefas.py 