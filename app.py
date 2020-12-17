from flask import request, Flask, render_template, url_for, redirect
from flask.wrappers import Response
import requests

app = Flask(__name__)

app.secret_key = "67q5r9s7rtf3"


def validar():
    return True


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index')
def index():
        return render_template('index.html')


@app.route('/credits')
def credits():
        return render_template('credits.html')

@app.route('/beers')
def api():
    url = "https://api.punkapi.com/v2/beers"
    paramss = {'page': '1', 'page_page': '80'}
    res = requests.request("GET", url, params=paramss)
    if res.status_code == 200:
        body = res.json()
        return render_template('beers.html', records=body)
    else:
        return "No ha funcionado"

@app.route('/beer/<id>')
def beer(id):
    url = 'https://api.punkapi.com/v2/beers/'
    paramss = id
    res = requests.request("GET", url, params = paramss)
    if res.status_code == 200:
        body = res.json()
        body_list = body[int(id)]
        body_string = str(body_list)
        return body_string
    else:
        return "No ha funcionado"


if __name__ == '__main__':
    app.run(debug=True)
