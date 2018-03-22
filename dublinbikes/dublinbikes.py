from flask import Flask, render_template
from dublinbikes.Stations import Station
from flask import json
from dublinbikes import app

# route() decorator tells Flask what URL should trigger our function


@app.route('/maps')
def maps():
    _stations = Station()  # ------------------------------------- Object for stations
    staticStations = _stations.getStation() # -------------------- Get the stations
    coordinates=[]
    for s in staticStations:
        cords = dict(lat=float(s['Latitude']),
                     lng=float(s['Longitude']))
        coordinates.append(cords)
    # - Passing the list for Jinja to render
    return render_template("maps.html", items=staticStations, locs=coordinates)

@app.route('/')
def main():
    returnDist = {}
    returnDist = {'user':'Harsh'}
    return render_template("index.html",**returnDist)

if __name__=="__main__":
    main()

