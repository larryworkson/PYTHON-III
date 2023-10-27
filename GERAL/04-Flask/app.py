from flask import Flask, Request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    nome = request.form.get('nome')
    return usarNome(nome) 


def usarNome(v):
    print(v)    


if __name__ == '__main__':
    app.run(debug=False)
