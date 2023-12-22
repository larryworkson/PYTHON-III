from kivy.app import App
from kivy.uix.button import Button


class SimpleApp(App): #simpleApp é nome do meu app (ele está herdando os atributos de App)
    def build(self): #build é o método obrigatório para renderização do app
        button = Button(text='Clique-me', on_press=self.on_button_press, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        return button
    
    def on_button_press(self, instance):
        print('Botão Clicado!')


if __name__ == '__main__':
    SimpleApp().run()

# python teste-app.py