from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/music_library')
def music_library():
    # Aqui você deve obter dados da biblioteca de músicas do banco de dados e retorná-los como JSON
    music_data = [
        {'nome': 'Musica 1', 'artista': 'Artista 1', 'file': 'C:/Users/studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex006-player-musica/00-prototipo/data/01.mp3'},
        {'nome': 'Musica 2', 'artista': 'Artista 2', 'file': 'C:/Users/studi/Documents/code/PYTHON-III/GERAL/04-Flask/ex006-player-musica/00-prototipo/data/01.mp3'}]
    return jsonify(music_data)

@app.route('/data/<path:filename>')
def download_file(filename):
    return send_file(os.path.join)(app.root_path, 'data', filename)

if __name__ == '__main__':
    app.run(debug=True)

    # python main.py