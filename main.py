import auth
from flask import Flask, render_template
import os

app = Flask(__name__)
client_id = '1d804622168c49a89b24816de65be818'
client_id_secret = 'b53748cdb6e7407fb5bd0a66c858936d'
scope = 'user-read-currently-playing'
uri = 'https://autolyricsspotify.herokuapp.com/approval'

@app.route('/')
def index():
    
    global uri
    global client_id
    global scope

    url = auth.oath2(client_id, scope, uri)
    return render_template('index.html', url = url)

@app.route('/approval')
def approval():

    return render_template('lyrics.html')


port = int(os.getenv('PORT', 5000))
app.run(host = '0.0.0.0', port = port)

