from flask import render_template
from app import app
from flask import json
from flask import jsonify
from app.Stations import Station
import mysql.connector
from mysql.connector import errorcode


# route() decorator tells Flask what URL should trigger our function


@app.route('/',methods=['GET','POST'])
def main():
    print('Initiating Main')
    _stations = Station()  # ------------------------------------- Object for stations
    print('Object Created')
    # -------------------- Get the stations
    staticStations = _stations.getStation()
    print('Stations Fetched')
    statDetails = _stations.getAllDetails()
    weatherDetails = _stations.getWeather()
    _stations.closeConn()
    print('Connections Closed')
    print(weatherDetails)
    mainTemp = weatherDetails[0]['temp']
    mainDesc = weatherDetails[0]['wDes']
    mainSnow = weatherDetails[0]['wSnow']
    mainRain = weatherDetails[0]['wRain']
    mainWind = weatherDetails[0]['wWind']
    coordinates=[]
    totalBikes = statDetails[0]['tBikes']
    totalStations = statDetails[0]['tStations']
    # print('Rendering Template')
    # - Passing the list for Jinja to render
    return render_template("index.html",locs=staticStations, tB=totalBikes, tS=totalStations, mainTemp=mainTemp, mainDesc=mainDesc, mainSnow=mainSnow, mainRain=mainRain, mainWind=mainWind)


@app.route('/maps')
def mapsShow():
    return render_template("stations.html")


@app.route('/stations')
def getStations():
    _stations = Station()
    stations = _stations.getStation()
    _stations.closeConn()
    return jsonify(stations=stations)


@app.route('/stations/<int:station_id>')
def getStationsById(station_id):
    _stations = Station()
    stationsId = _stations.getStationsById(station_id)
    _stations.closeConn()
    return jsonify(stationsId=stationsId)

@app.route('/subscribe')
def subscribeShow():
    return render_template("subscribe.html")

@app.route('/predict')
def showForecast():
    return render_template("predict.html")

if __name__=="__main__":
    main()

