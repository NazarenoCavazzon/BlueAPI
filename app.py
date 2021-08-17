import os
import codecs
from ida import lineaUnoIda
from busStops import busStopsDict
from datetime import datetime
from flask_caching import Cache
from flask import Flask, send_from_directory, jsonify
from bs4 import BeautifulSoup

VERSION = "1.0"
CACHE_TIMEOUT_SECONDS = os.getenv('CACHE_TIMEOUT', 3600)
GIT_REPO_URL = 'https://github.com/NazarenoCavazzon/BlueAPI'
DOLAR_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-dolar-hoy-argentina.html'
EURO_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-euro-hoy-argentina.html'
REAL_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-real-hoy-argentina.html'

# Create a class called BusStop that will take line, name, address, latitude and longitude. 
class BusStop:
    def __init__(self, line, name, address, latitude, longitude):
        self.line = line
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

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
    html = ""
    with codecs.open('index.html', "r", "utf-8") as f:
        codeHTML = f.read()
    for element in codeHTML:
        if element == "¡":
            element = VERSION
            html += element
        elif element == "ñ":
            element = GIT_REPO_URL
            html += element
        else:
            html += element
    return html

@app.route("/api/ping")
def ping():
    return "pong"

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

@app.route("/api/busstops")
def getBusStops():
    return jsonify(busStopsDict)

@app.route("/api/line1/ida")
def getBusStops():
    return jsonify(lineaUnoIda)

@app.route("/api/gmaps")
def getGMaps():
    return jsonify("https://www.google.com/maps/d/u/0/viewer?mid=1d5o2MklEFr0DpG_i_mRwcUd9yjc&ll=-31.654431124663883%2C-64.43315245330842&z=15")

if __name__ == '__main__':
    app.run(debug=False, port=os.getenv('PORT', 5000))
