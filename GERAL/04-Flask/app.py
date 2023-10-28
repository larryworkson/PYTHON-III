from flask import Flask, render_template, request

app = Flask(__name__) #__name__ é um valor especial definido pelo python. O valor de __name__ é o nome do arquivo Python que está sendo executado. No caso o valor do __name__ é a variável app

@app.route('/') #route é a ligação entre uma URL e uma função. Neste caso, ao acessar a URL raíz ('/') será chamada a função index()
def index():
    return render_template('index.html')

#o @ (decorador) atribui uma nova funcionalidades para a função que está abaixo dele.
@app.route('/submit', methods=['GET']) #/submit define em qual link a função abaixo será acionada. No caso, /submit é quando clicamos no botão de submissão de um form que tem action="/submit".
def submit_form():
    nome = request.args.get('nome')
    return render_template('index.html', usernome = nome)

if __name__ == '__main__':
    app.run(debug=False)
