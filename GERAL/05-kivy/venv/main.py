from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout #empilha os widgets em caixas

'''
on_relase = ativa função quando solta o botão.
'''

class Teste(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        btn1 = Button(text='Btn 1', font_size=30, on_release=self.incrementar)
        self.txt1 = Label(text='1', font_size=30) # o self deixa esta variável global em toda a classe
        box.add_widget(self.txt1)
        box.add_widget(btn1)
        return box
    
    def incrementar(self, btn1):
        self.txt1.text = str(int(self.txt1.text) + 1) #acessa a variável global txt1 e transforma ela em int para incrementar 1, depois transforma em string para jogar no label.
    
Teste().run()

#       python main.py