from flask import Flask, render_template
from dublinbikes.Stations import Station
from flask import json
from dublinbikes import app

# route() decorator tells Flask what URL should trigger our function
@app.route('/')
def main():
    _stations = Station()  # ------------------------------------- Object for stations
    staticStations = _stations.getStation() # -------------------- Get the stations
    coordinates=[]
    for s in staticStations:
        cords = dict(lat=float(s['Latitude']),
                     lng=float(s['Longitude']))
        coordinates.append(cords)
    # - Passing the list for Jinja to render
    return render_template("index.html", items=staticStations, locs=coordinates)

if __name__=="__main__":
    main()

