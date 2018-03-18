from flask import Flask
from dublinbikes.Stations import Station
import Stations
from dublinbikes import app

def main():
    _stations = Stations.Station()  # ------- Object for stations
    staticStations = _stations.getStation() # ------- Get the stations
    print(staticStations)

if __name__=="__main__":
    main()

