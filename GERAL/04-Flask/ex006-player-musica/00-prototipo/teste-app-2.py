from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        # Layout principal usando BoxLayout vertical
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        #add um textinput ao layout
        n1 = TextInput(hint_text='Digite um numero: ', multiline=False)
        layout.add_widget(n1)
        n2 = TextInput(hint_text='Digite outro numero: ', multiline=False)
        layout.add_widget(n2)

        #add um botao ao layout
        button = Button(text='Somar', on_press=self.on_button_press)
        layout.add_widget(button)

        #add rótulo (label) para exibir um dado
        self.resultado = Label(text='')
        layout.add_widget(self.resultado)

        return layout
    
    def on_button_press(self, instance):
        #obtem o texto do TextInput quando o botão é pressionado

        n1 = instance.parent.children[2] #assumindo que o TextInput é o primeiro filho do layout
        num1 = int(n1.text)
        n2 = instance.parent.children[3]
        num2 = int(n2.text)
        self.resultado.text = f'Resulado: {num1 + num2}'

MeuApp().run()

# python teste-app-2.py

"""criar dois campos de input e realizar operação matematica para gerar resultado"""