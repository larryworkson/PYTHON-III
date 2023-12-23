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
        {'nome': 'Musica 1', 'artista': 'Artista 1', 'file': 'https://larryworkson.github.io/PYTHON-III/GERAL/04-Flask/ex006-player-musica/00-prototipo/data/01.mp3'}]
    return jsonify(music_data)

if __name__ == '__main__':
    app.run(debug=False)

    # python main.py


"""
- o player está 'ok', agora preciso gerar uma lista de músicas e jogá-las para o app para quando clicar, tocar. Depois fazer consultas no catálogo sem interromper a música.
- as músicas precisam estar hospedadas na web.
- gerar uma lista de músicas e um único player para que quando usuário clicar na música o player roda a música.
"""

"""GPT recomendou criar os botões de controle do player pelo JS para evitar que o player seja interrompido ao navegar pelo catálogo

<script>
    var currentAudio = null;

    // Função para carregar a biblioteca de músicas via AJAX
    function loadMusicLibrary() {
        $.ajax({
            url: '/api/music_library',
            type: 'GET',
            success: function(data) {
                var musicLibrary = $('#music-library');
                
                // Limpa o conteúdo atual
                musicLibrary.empty();

                // Adiciona o player de áudio único
                musicLibrary.append(`
                    <p id="song-info"></p>
                    <audio id="audio-player" controls>
                        Seu navegador não suporta o elemento de áudio.
                    </audio>
                `);

                // Adiciona eventos de clique para cada música
                data.forEach(function(song) {
                    var songInfo = `${song.nome} | ${song.artista}`;
                    musicLibrary.append(`<p class="song-item" data-src="${song.file}">${songInfo}</p>`);
                });

                // Adiciona evento de clique para as músicas
                $('.song-item').click(function() {
                    var newSrc = $(this).data('src');
                    playNewSong(newSrc);
                    $('#song-info').text($(this).text());
                });
            },
            error: function(error) {
                console.log('Erro ao carregar a biblioteca de músicas:', error);
            }
        });
    }

    // Função para reproduzir uma nova música
    function playNewSong(src) {
        if (currentAudio) {
            // Pára o áudio atual se estiver reproduzindo
            currentAudio.pause();
        }

        // Atualiza a fonte do áudio
        $('#audio-player').attr('src', src);

        // Inicia a reprodução
        $('#audio-player')[0].play();

        // Atualiza a variável currentAudio
        currentAudio = $('#audio-player')[0];
    }

    // Carrega a biblioteca de músicas quando a página for carregada
    $(document).ready(function() {
        loadMusicLibrary();
    });
</script>
"""