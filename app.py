import os
import codecs
# Importa horarios para seccion INFO. -----------
from manejo import preguntas_manejo
from busSchedules import schedule1B
from busSchedules import schedule2
from busSchedules import schedule3
from busSchedules import schedule4
from busSchedules import schedule5
from busSchedules import schedule6
from busSchedules import horario7
from busSchedules import horario242
from busSchedules import horarioS2
from busSchedules import horariosierras
from busSchedules import horarioSarmientoDif
# Importa horarios habiles de las lineas. ----------- (LINEA 234)
from busZonesTimes import busZonesTimesOne
from busZonesTimes import busZonesTimesOneB
from busZonesTimes import busZonesTimesTwo
from busZonesTimes import busZonesTimesThree
from busZonesTimes import busZonesTimesFour
from busZonesTimes import busZonesTimesFive
from busZonesTimes import busZonesTimesSix
from busZonesTimes import linea7Habiles
from busZonesTimes import busHorarios242
from busZonesTimes import horario125
from busZonesTimes import horario125R
# from busZonesTimes import S2hablies
# Importa horarios de Sabado de las lineas. ----------- (LINEA 302)
from busZonesTimes import busZonesTimesOneSaturday
from busZonesTimes import busZonesTimesOneBSaturday
from busZonesTimes import busZonesTimesTwoSaturday
from busZonesTimes import busZonesTimesThreeSaturday
from busZonesTimes import busZonesTimesFourSaturday
from busZonesTimes import busZonesTimesFiveSaturday
from busZonesTimes import busZonesTimesSixSaturday
from busZonesTimes import linea7Sabado
from busZonesTimes import busHorarios242sabado
from busZonesTimes import horario125sabado
from busZonesTimes import horario125Rsabado
# from busZonesTimes import S2sabados
# Importa horario de Domingo de las lineas. ----------- (LINEA 272)
from busZonesTimes import busZonesTimesOneSunday
from busZonesTimes import busZonesTimesOneBSunday
from busZonesTimes import busZonesTimesTwoSaturday
from busZonesTimes import busZonesTimesThreeSunday
from busZonesTimes import busZonesTimesFourSunday
from busZonesTimes import busZonesTimesFiveSunday
from busZonesTimes import busZonesTimesSixSunday
from busZonesTimes import linea7Domingo
from busZonesTimes import horario125domingo
from busZonesTimes import horario125Rdomingo
# from busZonesTimes import S2domingos
# Importa las rutas para graficarlas. -----------
from busRoutes import lineOne
from busRoutes import lineOneB
from busRoutes import lineTwo
from busRoutes import lineThree
from busRoutes import lineFour
from busRoutes import lineFive
from busRoutes import lineSix
from busRoutes import linea7
from busRoutes import line242
from busRoutes import linea125
from busRoutes import linea125R
from busRoutes import lineaS2
# Importa el numero, color y estado de las lineas. -----------
from busStops import busStopsDict
from busStops import linesDict
# No se que hace. -----------
from datetime import datetime
from flask import Flask, send_from_directory, jsonify
from bs4 import BeautifulSoup

# URLs. -----------
VERSION = "1.0"
CACHE_TIMEOUT_SECONDS = os.getenv('CACHE_TIMEOUT', 3600)
GIT_REPO_URL = 'https://github.com/NazarenoCavazzon/BlueAPI'
DOLAR_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-dolar-hoy-argentina.html'
EURO_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-euro-hoy-argentina.html'
REAL_URL = 'https://www.paralelohoy.com.ar/p/cotizacion-real-hoy-argentina.html'

# Crea una clase que obtiene linea, nombre, direccion, latitud y longitud. -----------
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

# ========================== API Dolar Blue ==========================

def formatResponse(value):
    return {
        "fecha": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        "compra" : f"{value[0]}",
        "venta" : f"{value[1]}"
    }

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

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

# ============================== Paradas de Colectivo ==============================

@app.route("/api/busstops")
def getBusStops():
    return jsonify(busStopsDict)

# ================== Lineas de colectivos =======================

@app.route("/api/1")
def getLine1():
    return jsonify(lineOne)

@app.route("/api/1B")
def getLine1B():
    return jsonify(lineOneB)

@app.route("/api/2")
def getLine2():
    return jsonify(lineTwo)

@app.route("/api/3")
def getLine3():
    return jsonify(lineThree)

@app.route("/api/4")
def getLine4():
    return jsonify(lineFour)

@app.route("/api/5")
def getLine5():
    return jsonify(lineFive)

@app.route("/api/6")
def getLine6():
    return jsonify(lineSix)

@app.route("/api/7")
def getLine7():
    return jsonify(linea7)

@app.route("/api/242")
def getLine242():
    return jsonify(line242)

@app.route("/api/125")
def getLine125():
    return jsonify(linea125)

@app.route("/api/125R")
def getLine125R():
    return jsonify(linea125R)

@app.route("/api/S2")
def getLineS2():
    return jsonify(lineaS2)

# ================ Obtiene las lineas de busStops.py ===============

@app.route("/api/linesDict")
def getLines():
    return jsonify(linesDict)

# ============================== Horarios por ZONA ==============================

@app.route("/api/busZonesTimes/1")
def getBusZonesOne():
    return jsonify(busZonesTimesOne)

@app.route("/api/busZonesTimes/1B")
def getBusZonesOneB():
    return jsonify(busZonesTimesOneB)

@app.route("/api/busZonesTimes/2")
def getBusZonesTwo():
    return jsonify(busZonesTimesTwo)

@app.route("/api/busZonesTimes/3")
def getBusZonesThree():
    return jsonify(busZonesTimesThree)

@app.route("/api/busZonesTimes/4")
def getBusZonesFour():
    return jsonify(busZonesTimesFour)

@app.route("/api/busZonesTimes/5")
def getBusZonesFive():
    return jsonify(busZonesTimesFive)

@app.route("/api/busZonesTimes/6")
def getBusZonesSix():
    return jsonify(busZonesTimesSix)

@app.route("/api/busZonesTimes/7")
def getBusZones7():
    return jsonify(linea7Habiles)

@app.route("/api/busZonesTimes/242")
def getBusZones242():
    return jsonify(busHorarios242)

@app.route("/api/busZonesTimes/125")
def getBusZones125():
    return jsonify(horario125)

@app.route("/api/busZonesTimes/125R")
def getBusZones125R():
    return jsonify(horario125R)

# ============================== Horarios por ZONA (Domingo) ==============================

@app.route("/api/busZonesTimes/1/sunday")
def getBusZonesOneSunday():
    return jsonify(busZonesTimesOneSunday)

@app.route("/api/busZonesTimes/1B/sunday")
def getBusZonesOneBSunday():
    return jsonify(busZonesTimesOneBSunday)

@app.route("/api/busZonesTimes/2/sunday")
def getBusZonesTwoSunday():
    return jsonify(busZonesTimesTwo)

@app.route("/api/busZonesTimes/3/sunday")
def getBusZonesThreeSunday():
    return jsonify(busZonesTimesThreeSunday)

@app.route("/api/busZonesTimes/4/sunday")
def getBusZonesFourSunday():
    return jsonify(busZonesTimesFourSunday)

@app.route("/api/busZonesTimes/5/sunday")
def getBusZonesFiveSunday():
    return jsonify(busZonesTimesFiveSunday)

@app.route("/api/busZonesTimes/6/sunday")
def getBusZonesSixSunday():
    return jsonify(busZonesTimesSixSunday)

@app.route("/api/busZonesTimes/7/sunday")
def getBusZones7Domingos():
    return jsonify(linea7Domingo)

@app.route("/api/busZonesTimes/125/sunday")
def getBusZones125Sunday():
    return jsonify(horario125domingo)

@app.route("/api/busZonesTimes/125R/sunday")
def getBusZones125RSunday():
    return jsonify(horario125Rdomingo)

# ============================== Horarios por ZONA (Sabado) ==============================

@app.route("/api/busZonesTimes/1/saturday")
def getBusZonesOneSaturday():
    return jsonify(busZonesTimesOneSaturday)

@app.route("/api/busZonesTimes/1B/saturday")
def getBusZonesOneBSaturday():
    return jsonify(busZonesTimesOneBSaturday)

@app.route("/api/busZonesTimes/2/saturday")
def getBusZonesTwoSaturday():
    return jsonify(busZonesTimesTwoSaturday)

@app.route("/api/busZonesTimes/3/saturday")
def getBusZonesThreeSaturday():
    return jsonify(busZonesTimesThreeSaturday)

@app.route("/api/busZonesTimes/4/saturday")
def getBusZonesFourSaturday():
    return jsonify(busZonesTimesFourSaturday)

@app.route("/api/busZonesTimes/5/saturday")
def getBusZonesFiveSaturday():
    return jsonify(busZonesTimesFiveSaturday)

@app.route("/api/busZonesTimes/6/saturday")
def getBusZonesSixSaturday():
    return jsonify(busZonesTimesSixSaturday)

@app.route("/api/busZonesTimes/7/saturday")
def getBusZones7Sabado():
    return jsonify(linea7Sabado)

@app.route("/api/busZonesTimes/242/saturday")
def getBusZones242Saturday():
    return jsonify(busHorarios242sabado)

@app.route("/api/busZonesTimes/125/saturday")
def getBusZones125Saturday():
    return jsonify(horario125sabado)

@app.route("/api/busZonesTimes/125R/saturday")
def getBusZones125RSaturday():
    return jsonify(horario125Rsabado)


# ============================== Botones ==============================

@app.route("/api/gmaps")
def getGMaps():
    return jsonify("https://www.google.com/maps/d/u/0/viewer?mid=1d5o2MklEFr0DpG_i_mRwcUd9yjc&ll=-31.654431124663883%2C-64.43315245330842&z=15")

@app.route("/api/donacion")
def getDonationPage():
    return jsonify("https://cafecito.app/paragracia")


# ============================== Horarios de las lineas [Lista] Hábiles ==============================

@app.route("/api/1B/schedule")
def get1Bchedule():
    return jsonify(schedule1B)

@app.route("/api/2/schedule")
def get2chedule():
    return jsonify(schedule2)

@app.route("/api/3/schedule")
def get3chedule():
    return jsonify(schedule3)

@app.route("/api/4/schedule")
def get4chedule():
    return jsonify(schedule4)

@app.route("/api/5/schedule")
def get5chedule():
    return jsonify(schedule5)

@app.route("/api/6/schedule")
def get6chedule():
    return jsonify(schedule6)

@app.route("/api/7/schedule")
def get7chedule():
    return jsonify(horario7)

@app.route("/api/125/schedule")
def get125schedule():
    return jsonify(horariosierras)

@app.route("/api/125R/schedule")
def get125Rschedule():
    return jsonify(horarioSarmientoDif)

@app.route("/api/242/schedule")
def get242chedule():
    return jsonify(horario242)

@app.route("/api/S2/schedule")
def getS2schedule():
    return jsonify(horarioS2)


# ============================== Horarios de las lineas [Lista] (Sabado) ==============================

# @app.route("/api/1B/schedule/saturday")
# def get1Bchedule():
#     return jsonify(schedule1B)

# @app.route("/api/2/schedule/saturday")
# def get2chedule():
#     return jsonify(schedule2)

# @app.route("/api/3/schedule/saturday")
# def get3chedule():
#     return jsonify(schedule3)

# @app.route("/api/4/schedule/saturday")
# def get4chedule():
#     return jsonify(schedule4)

# @app.route("/api/5/schedule/saturday")
# def get5chedule():
#     return jsonify(schedule5)

# @app.route("/api/6/schedule/saturday")
# def get6chedule():
#     return jsonify(schedule6)

# ============================== Horarios de las lineas [Lista] (Domingo) ==============================

# @app.route("/api/1B/schedule/sunday")
# def get1Bchedule():
#     return jsonify(schedule1B)

# @app.route("/api/2/schedule/sunday")
# def get2chedule():
#     return jsonify(schedule2)

# @app.route("/api/3/schedule/sunday")
# def get3chedule():
#     return jsonify(schedule3)

# @app.route("/api/4/schedule/sunday")
# def get4chedule():
#     return jsonify(schedule4)

# @app.route("/api/5/schedule/sunday")
# def get5chedule():
#     return jsonify(schedule5)

# @app.route("/api/6/schedule/sunday")
# def get6chedule():
#     return jsonify(schedule6)


# ================ Preguntas de Manejo ===============

@app.route("/api/preguntas")
def getQuestions():
    return jsonify(preguntas_manejo)

if __name__ == '__main__':
    app.run(debug=False, port=os.getenv('PORT', 5000))
