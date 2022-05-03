from flask import request, render_template
from flask import request, render_template
from flask import Flask , request, redirect, render_template , sessions, session, url_for
import flask
import os


app = Flask(__name__, static_folder='./static')
app.secret_key= os.urandom(24).hex()
movievarlist = []

def check_token(key):
    f = open('keys', 'r')
    for token in f.readlines():
        if key == token:
            f.close()
            return 1
        else:
            f.close()
            return 0

@app.route('/movie/<variable>/<key>', methods=['GET']) 
def movie(variable, key):
    moviedirlist = []

    for moviedir in os.listdir('./static/Movies'):
        moviedirlist.append(moviedir)
        
    for f in os.listdir('./static/Movies/{0}'.format(moviedirlist[int(variable)])):
        if f[-3:] in ['mp4', 'mkv', 'avi']:
            movielink = '/static/Movies/{0}/{1}'.format(moviedirlist[int(variable)], f)
            return render_template('index.html', param1=movielink)

        
app.run(debug=True, host='0.0.0.0', port='5000', threaded=True)
