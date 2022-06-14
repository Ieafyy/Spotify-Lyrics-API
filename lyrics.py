import requests

def get_lyrics(artist, music):
    if '-' in music:
        new = music.split('-')
        response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{new[0]}')

    if '/' in music:
        new = music.split('/')
        response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{new[0]}')
    else:
        response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{music}')
    try:
        printable = response.json()['lyrics'].replace('\n', '<br>')
    except:
        printable = 'Letra não encontrada!'
    return printable


def vagalume(artist, music):
    if '-' in music:
        new = music.split('-')
        response = requests.get(f'https://api.vagalume.com.br/search.php?art={artist}&mus={new[0]}&apikey=e0facd0333b3c47b566adefb2575eeee')

    if '/' in music:
        new = music.split('/')
        response = requests.get(f'https://api.vagalume.com.br/search.php?art={artist}&mus={new[0]}&apikey=e0facd0333b3c47b566adefb2575eeee')

    else:
        response = requests.get(f'https://api.vagalume.com.br/search.php?art={artist}&mus={music}&apikey=e0facd0333b3c47b566adefb2575eeee')
    
    try:
        return response.json()['mus'][0]['text'].replace('\n', '<br>')
    except:
        return 'Letra não encontrada!'

    