from kivy.app import App
from kivy.uix.boxlayout import BoxLayout #empilha os widgets em caixas
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

'''
as funções estão no arquivo tarefas.kv
O NOME DO ARQUIVO DEVE SER O MESMO DO APP.
'''
class Task(ScrollView):
    def __init__(self, tarefas, **kwargs): #keyword arguments
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Item(text=tarefa)) #self vai add widgets no BoxLayout.

class Item(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text
class Tarefas(App):
    def build(self):        
        return Task(['Fazer compras', 'Buscar filho', 'Molhar calçada', 'Ir médico', 'Comprar arroz', 'Buscar o bolo', 'Reservar passagem', 'Dormir 30 min'])
    
Tarefas().run()

#       python tarefas2.py 