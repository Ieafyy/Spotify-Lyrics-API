from email import header
import requests
from urllib.parse import urlencode
import base64

def validate(code, redirect_uri, key, secret_key):

    url = 'https://accounts.spotify.com/api/token?'
    url_keys = key + ':' + secret_key
    conv1 = url_keys.encode('ascii')
    conv2 = base64.b64encode(conv1)
    conv2 = conv2.decode('ascii')

    params = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }

    headers = {
        'Authorization' : f'Basic ' + conv2,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    req = requests.post(url, headers = headers, data = params)
    req_bib = req.json()
    token = req_bib['access_token']
    return token


def now_playing(code):
    headers = {
        'Content-Type' : 'application/json',
        'Accept' : 'application/json',
        'Authorization' : f'Bearer {code}'
    }

    url = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
    return url
