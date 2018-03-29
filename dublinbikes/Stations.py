import mysql.connector
from mysql.connector import errorcode

class Station():
    """ This is a class which provides all the information with respect to Dubline Bike Stations"""

    def __init__(self):
        self.__stations = []
        self.__tDetails = []
        self.__wDetails = []

        # Connecting to the MySQL Db
        self.config = {
            'user': 'root',
            'password': '00001234',
            'host': 'dublinbikescomp30670.c8lbidkpdn4h.us-east-2.rds.amazonaws.com',
            'database': 'dublinbikes',
            'raise_on_warnings': True,
        }

        # Trying to connect to the database
        try:
            self.cnx = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        # Cursor to perform the executions to the db
        self.cursor = self.cnx.cursor()

    def getStation(self):

        """This method will call the database for static station data"""

        

        # Query to get the station data from the static table
        staticStations = ("select A.station_number, A.station_name, A.station_pos_lat, A.station_pos_lon,B.station_status,B.station_total_bike_stands, B.station_available_bikes, B.station_available_bike_stands,DATE_FORMAT(B.station_data_LUD, '%r %d %M %Y') as station_data_LUD from jcdecaux_static_dublin_bikes A, jcdecaux_live_data B where A.station_number=B.station_number")

        try:
            # -------- Execute on database and return values in cursor
            self.cursor.execute(staticStations)
        except mysql.connector.Error as err:
            print("Could not retrieve static stations, Error: {}".format(err))

        # Creating a list for the returned stations
        for i in self.cursor:
            station = dict(StationNum=i[0], StationName=i[1], Latitude=float(
                i[2]), Longitude=float(i[3]), Status=i[4], TotalStands = i[5],
                availableBikes = i[6], availableStands=i[7], LUD = i[8])
            self.__stations.append(station)
        
        return self.__stations

    def getAllDetails(self):

        """This method provides total bikes and stands information"""

        # Query to get the all the data
        totalBikes = ("select sum(station_total_bike_stands), count(*) as totalStations from jcdecaux_live_data")

        try:
            # -------- Execute on database and return values in cursor
            self.cursor.execute(totalBikes)
        except mysql.connector.Error as err:
            print("Could not retrieve static stations, Error: {}".format(err))

        # Creating a list for the returned stations
        for i in self.cursor:
            totalDetails = dict(tBikes=int(i[0]), tStations=int(i[1]))
            self.__tDetails.append(totalDetails)

        return self.__tDetails

    def getWeather(self):

        #Query to get the weather data
        weatherData = ("SELECT * FROM dublinbikes.owm_live_data WHERE DATE(weather_sys_dt_txt) = DATE(NOW());")

        try:
            # ------Execute on database and return values in cursor
            self.cursor.execute(weatherData)
        except mysql.connector.Error as err:
            print("Could not retrieve static stations, Error: {}".format(err))

        # Creating a list for the returned stations
        for i in self.cursor:
            weatherData = dict(temp = int(i[0]), wDes = (i[4]), wSnow = (i[10]), wRain = (i[11]))
            self.__wDetails.append(weatherData)
        print(self.cursor)
        return self.__wDetails
