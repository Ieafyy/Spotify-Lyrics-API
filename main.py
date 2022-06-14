import auth
from flask import Flask, request, render_template, jsonify
import spotify
import lyrics
import os

app = Flask(__name__)
client_id = '1d804622168c49a89b24816de65be818'
client_id_secret = 'b53748cdb6e7407fb5bd0a66c858936d'
scope = 'user-read-currently-playing'
uri = 'https://autolyricsspotify.herokuapp.com/approval'
url = auth.oath2(client_id, scope, uri)
init = 0
token = ''
result = ''
time_result = 0
actual_time = 0
image = ''
artist = ''
letra = ''
musica_start = 0
approval_start = 0


result_flag_1 = ''
flag_i_1 = 0
ft_1 = 1

result_flag_2 = ''
flag_i_2 = 0
ft_2 = 1


@app.route('/')
def index():
    global url
    return render_template('index.html', url = url)

@app.route('/approval')
def approval():
    global client_id
    global client_id_secret
    global init
    global token
    global result
    global time_result
    global actual_time
    global image
    global artist
    global letra

    global result_flag_1
    global flag_i_1
    global ft_1

    result_temp = ''

    code = request.url[53:]
    if init == 0:
        token = spotify.validate(code, 'https://autolyricsspotify.herokuapp.com/approval', client_id, client_id_secret)
        print(token)
        init = 1

    now_playing = spotify.now_playing(token)
    try:
        result = now_playing.json()['item']['name']
        if flag_i_1 == 0:
            result_flag_1 = result
            flag_i_1 = 1
        time_result = now_playing.json()['item']['duration_ms']
        actual_time = now_playing.json()['progress_ms']
        image = now_playing.json()['item']['album']['images'][0]['url']
        artist = now_playing.json()['item']['artists'][0]['name']
        if result_flag_1 != result or ft_1 == 1:
            letra = lyrics.vagalume(artist, result)
            flag_i_1 = 0
            ft_1 = 0
        result_temp = result
    except:
        result = 'nm'
        time_result = 0
        actual_time = 0
        image = 'ni'
        artist = 'na'
        result_temp = 'Não está tocando nada'
        letra = 'Letra não encontrada!'

    return render_template('lyrics.html', musica = result_temp, letra = letra)


@app.route('/musica', methods=['GET'])
def musica():
    global client_id
    global client_id_secret
    global init
    global token
    global result
    global time_result
    global actual_time
    global image
    global artist
    global letra
    
    global result_flag_2
    global flag_i_2
    global ft_2

    now_playing = spotify.now_playing(token)

    try:
        result = now_playing.json()['item']['name']
        if flag_i_2 == 0:
            result_flag_2 = result
            flag_i_2 = 1
        time_result = now_playing.json()['item']['duration_ms']
        actual_time = now_playing.json()['progress_ms']
        image = now_playing.json()['item']['album']['images'][0]['url']
        artist = now_playing.json()['item']['artists'][0]['name']
        if result_flag_2 != result or ft_2 == 1:
            letra = lyrics.vagalume(artist, result)
            flag_i_2 = 0
            ft_2 = 0
    except:
        result = 'sem musica no momento'
        time_result = 0
        actual_time = 0
        image = 'ni'
        artist = 'na'
        letra = 'Letra não encontrada!'

    valor = {
        'musica': result,
        'total': time_result,
        'atual': actual_time,
        'image': image,
        'artist': artist,
        'lyrics': letra
    }

    return jsonify(valor)

port = int(os.getenv('PORT', 5000))
app.run(host = '0.0.0.0', port = port)

