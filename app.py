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


@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username):
    return render_template('index.html', name=username)


@app.route('/medical')
def medical():
    return render_template('medical.html')


@app.route('/beers')
def api():
    url = "https://api.punkapi.com/v2/beers"
    paramss = {'page': '2', 'page_page': '80'}
    res = requests.request("GET", url, params=paramss)
    if res.status_code == 200:
        body = res.json()
        return render_template('beers.html', records=body)
    else:
        return "No ha funcionado"


if __name__ == '__main__':
    app.run(debug=True)
