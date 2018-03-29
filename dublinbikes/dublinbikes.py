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
    coordinates=[]
    totalDetails = []
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
    # print(coordinates)
    # - Passing the list for Jinja to render
    return render_template("index.html", items=staticStations, locs=coordinates, tDetails = statDetails)

if __name__=="__main__":
    main()

