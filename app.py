import os
from flask import Flask, jsonify
from datetime import datetime

def getEuroValues():
    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.paralelohoy.com.ar/p/cotizacion-euro-hoy-argentina.html'

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

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/api/ping")
def ping():
    return 'pong'

@app.route("/api/euro/oficial")
def getEuroOficial():
    euroValues = getEuroValues()
    euroNacion = {
        "fecha": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        "compra" : f"{euroValues[0][0]}",
        "venta" : f"{euroValues[0][1]}"
    }
    return jsonify(euroNacion)

@app.route("/api/euro/blue")
def getEuroBlue():
    euroValues = getEuroValues()
    euroBlue = {
        "fecha": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        "compra" : f"{euroValues[1][0]}",
        "venta" : f"{euroValues[1][1]}"
    }
    return jsonify(euroBlue)

if __name__ == '__main__':
    app.run(debug=False, port=os.getenv('PORT', 5000))
