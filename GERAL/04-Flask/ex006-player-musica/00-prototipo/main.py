from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/music_library')
def music_library():
    # Aqui você deve obter dados da biblioteca de músicas do banco de dados e retorná-los como JSON
    music_data = [{'nome': 'Musica 1', 'artista': 'Artista 1'}, {'nome': 'Musica 2', 'artista': 'Artista 2'}]
    return jsonify(music_data)

if __name__ == '__main__':
    app.run(debug=False)