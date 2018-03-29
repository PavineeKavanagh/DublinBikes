from flask import Flask, render_template
from dublinbikes.Stations import Station
from flask import json
from dublinbikes import app

# route() decorator tells Flask what URL should trigger our function


@app.route('/',methods=['GET','POST'])
def main():
    _stations = Station()  # ------------------------------------- Object for stations
    staticStations = _stations.getStation() # -------------------- Get the stations
    statDetails = _stations.getAllDetails()
    weatherDetails = _stations.getWeather()
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
    # - Passing the list for Jinja to render
    return render_template("index.html", items=staticStations, locs=coordinates, tB=totalBikes, tS=totalStations, mainTemp=mainTemp, mainDesc=mainDesc, mainSnow=mainSnow, mainRain=mainRain, mainWind = mainWind)
@app.route('/maps')
def mapsShow():
    return render_template("maps.html")

if __name__=="__main__":
    main()

