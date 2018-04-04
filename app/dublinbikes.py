from flask import render_template
from app import app
from flask import json
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
    mainTemp = weatherDetails[0]['temp']
    mainDesc = weatherDetails[0]['wDes']
    mainSnow = weatherDetails[0]['wSnow']
    mainRain = weatherDetails[0]['wRain']
    mainWind = weatherDetails[0]['wWind']
    coordinates=[]
    totalBikes = statDetails[0]['tBikes']
    totalStations = statDetails[0]['tStations']
    for s in staticStations:
        cords = dict(lat=float(s['Latitude']),
                     lng=float(s['Longitude']),
                     name=s['StationName'],
                     num=s['StationNum'],
                     tStands=s['TotalStands'],
                     availBikes=s['availableBikes'],
                     availStands=s['availableStands'],
                     status=s['Status'],
                     lud = s['LUD'])
        coordinates.append(cords)
    print('Rendering Template')
    # - Passing the list for Jinja to render
    return render_template("index.html", items=staticStations, locs=coordinates, tB=totalBikes, tS=totalStations, mainTemp=mainTemp, mainDesc=mainDesc, mainSnow=mainSnow, mainRain=mainRain, mainWind = mainWind)
@app.route('/maps')
def mapsShow():
    return render_template("maps.html")

if __name__=="__main__":
    print('In the app')
    main()

