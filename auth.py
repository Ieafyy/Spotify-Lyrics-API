from urllib.parse import urlencode

def oath2(client_id, scope, uri):
    params = urlencode({
        'client_id':client_id,
        'scope':scope,
        'redirect_uri': uri,
        'response_type': 'code'
    })

    url = 'https://accounts.spotify.com/authorize?' + params
    return url