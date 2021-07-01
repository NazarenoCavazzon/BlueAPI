import os
import codecs
from datetime import datetime
from flask_caching import Cache
from flask import Flask, send_from_directory, jsonify
from bs4 import BeautifulSoup

version = "1.0"
CACHE_TIMEOUT_SECONDS = os.getenv('CACHE_TIMEOUT', 3600)
GIT_REPO_URL = 'https://github.com/NazarenoCavazzon/BlueAPI'
DOLAR_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-dolar-hoy-argentina.html'
EURO_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-euro-hoy-argentina.html'
REAL_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-real-hoy-argentina.html'

def getValues(url):
    import requests

    html_source = requests.get(url).text
    soup = BeautifulSoup(html_source, 'lxml')

    table = soup.find("table")
    span = table.tbody.text
    splittedSpan = span.split("\n")
    splittedSpan = filter(None, splittedSpan)
    list = []
    for x in splittedSpan:
        value = []
        value = x.split(":")[1].split("$")
        value.pop(0)
        list.append(value)

    return list

def formatResponse(value):
    return {
        "fecha": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        "compra" : f"{value[0]}",
        "venta" : f"{value[1]}"
    }

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route("/")
def getRoot():
    with open('index.html') as html_file:
        html = BeautifulSoup(html_file, 'lxml')
    return html.prettify()

@app.route("/api/ping")
def ping():
    return 'pong'

@app.route("/api/dolar/oficial")
@cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getDolarOficial():
    dolarValues = getValues(DOLAR_URL)
    dolarOficial = formatResponse(dolarValues[0])
    return jsonify(dolarOficial)

@app.route("/api/dolar/blue")
@cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getDolarBlue():
    dolarValues = getValues(DOLAR_URL)
    dolarBlue = formatResponse(dolarValues[1])
    return jsonify(dolarBlue)

@app.route("/api/euro/oficial")
@cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getEuroOficial():
    euroValues = getValues(EURO_URL)
    euroOficial = formatResponse(euroValues[0])
    return jsonify(euroOficial)

@app.route("/api/euro/blue")
@cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getEuroBlue():
    euroValues = getValues(EURO_URL)
    euroBlue = formatResponse(euroValues[1])
    return jsonify(euroBlue)

@app.route("/api/real/oficial")
@cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getRealOficial():
    realValues = getValues(REAL_URL)
    realOficial = formatResponse(realValues[0])
    return jsonify(realOficial)

@app.route("/api/real/blue")
@cache.cached(timeout=CACHE_TIMEOUT_SECONDS)
def getRealBlue():
    realValues = getValues(REAL_URL)
    realBlue = formatResponse(realValues[1])
    return jsonify(realBlue)

if __name__ == '__main__':
    app.run(debug=False, port=os.getenv('PORT', 5000))
