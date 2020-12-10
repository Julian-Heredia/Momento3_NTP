from flask import Flask, render_template, url_for, redirect
from flask.wrappers import Response
import requests
app = Flask(__name__)

app.secret_key = "67q5r9s7rtf3"

def validar():
    return True

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/contact')
def contact():
    if validar() == False:
        return redirect(url_for('medical'))
    else:
        return 'Contact form'

@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username):
    return render_template('index.html', name = username)

@app.route('/medical')
def medical():
    return render_template('medical.html')

@app.route('/api')
def api():
    url = 'https://chroniclingamerica.loc.gov/'
    esp_url = 'search/titles/results/'
    paramss = {'terms':'michigan', 'format':'json'}
    res = requests.request("GET", url + esp_url, params = paramss)
    if res.status_code == 200:
        body = res.json()
        return render_template('index.html', records = body["items"])
    else:
        return "Nooo"

@app.route('/detail/<id>')
def detail(id):
    url = 'https://chroniclingamerica.loc.gov/'
    # falta algo en la url: https://chroniclingamerica.loc.gov/lccn/sn86069873.json
    esp_url = id + '.json'
    res = requests.request("GET", url + esp_url)
    return res.json()


if __name__ == '__main__':
    app.run(debug=True)