from flask import Flask, request, render_template

aplicativo = Flask(__name__)

nsc = 0

@aplicativo.route('/')
def mostrar_home():
    return render_template('index.html')

@aplicativo.route('/submit', methods=['POST'])
def enviar_form():
    global nsc
    nsc = request.form['nsc']
    idade = 2023 - int(nsc)
    return render_template('index.html', resp = idade) #testar depois retornar apenas o mostrar_home() para ver se funciona


aplicativo.run()