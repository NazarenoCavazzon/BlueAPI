import os
from flask import Flask, jsonify
from datetime import datetime

DOLAR_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-dolar-hoy-argentina.html'
EURO_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-euro-hoy-argentina.html'
REAL_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-real-hoy-argentina.html'

def getValues(url):
    import requests
    from bs4 import BeautifulSoup

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

@app.route("/api/ping")
def ping():
    return 'pong'

@app.route("/api/dolar/oficial")
def getDolarOficial():
    dolarValues = getValues(DOLAR_URL)
    dolarOficial = formatResponse(dolarValues[0])
    return jsonify(dolarOficial)

@app.route("/api/dolar/blue")
def getDolarBlue():
    dolarValues = getValues(DOLAR_URL)
    dolarBlue = formatResponse(dolarValues[1])
    return jsonify(dolarBlue)

@app.route("/api/euro/oficial")
def getEuroOficial():
    euroValues = getValues(EURO_URL)
    euroOficial = formatResponse(euroValues[0])
    return jsonify(euroOficial)

@app.route("/api/euro/blue")
def getEuroBlue():
    euroValues = getValues(EURO_URL)
    euroBlue = formatResponse(euroValues[1])
    return jsonify(euroBlue)

@app.route("/api/real/oficial")
def getRealOficial():
    realValues = getValues(REAL_URL)
    realOficial = formatResponse(realValues[0])
    return jsonify(realOficial)

@app.route("/api/real/blue")
def getRealBlue():
    realValues = getValues(REAL_URL)
    realBlue = formatResponse(realValues[1])
    return jsonify(realBlue)

if __name__ == '__main__':
    app.run(debug=False, port=os.getenv('PORT', 5000))
