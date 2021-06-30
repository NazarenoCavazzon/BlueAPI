from flask import Flask, jsonify

def getValues():
    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.paralelohoy.com.ar/p/cotizacion-euro-hoy-argentina.html'

    html_source = requests.get(url).text
    soup = BeautifulSoup(html_source,'lxml')

    table = soup.find("table")
    span = table.tbody.text
    euros = span.split("\n")
    lista = []
    for euro in euros[1:3]:
        messi = []
        messi = euro.split(":")[1].split("$")
        messi.pop(0)
        lista.append(messi)
    return lista

def main():
    lista = getValues()

    euroNacion = [
        {"Compra" : f"{lista[0][0]}",
        "Venta" : f"{lista[0][1]}"}
    ]

    euroBlue = [
        {"Compra" : f"{lista[1][0]}",
        "Venta" : f"{lista[1][1]}"}
        ]

    return euroBlue, euroNacion

euroBlue, euroNacion = main()

app = Flask(__name__)

@app.route("/ping")
def ping():
    return 'pong'

@app.route("/api/euro/oficial")
def getOficial():
    return jsonify(euroNacion)

@app.route("/api/euro/blue")
def getBlue():
    return jsonify(euroBlue)

if __name__ == '__main__':
    app.run(debug=False,port=5000)
