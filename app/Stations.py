import mysql.connector
from mysql.connector import errorcode

class Station():
    """ This is a class which provides all the information with respect to Dubline Bike Stations"""

    def __init__(self):
        self.__stations = []
        self.__tDetails = []
        self.__wDetails = []
        self.flag=False
        self.__connectErrorDB = ''
        # Connecting to the MySQL Db
        self.__config = {
            'user': 'root',
            'password': '00001234',
            'host': 'dublinbikescomp30670.c8lbidkpdn4h.us-east-2.rds.amazonaws.com',
            'database': 'dublinbikes',
            'raise_on_warnings': True,
        }
        # Trying to connect to the database
        try:
            self.__cnx = mysql.connector.connect(**self.__config)
            self.flag=True
        except mysql.connector.Error as err:
            self.flag=False
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                self.__connectErrorDB = err

        if self.flag:
            print('Database Connected')
            self.__cursor = self.__cnx.cursor()
            print('Cursor Created')
        else:
            print('Error in Database',self.__connectErrorDB)

        

        
        

    def getStation(self):

        """This method will call the database for static station data"""

        # Query to get the station data from the static table
        staticStations = ("select A.station_number, A.station_name, A.station_pos_lat, A.station_pos_lon,B.station_status,B.station_total_bike_stands, B.station_available_bikes, B.station_available_bike_stands,DATE_FORMAT(DATE_ADD(B.station_data_LUD,INTERVAL 1 HOUR),'%r %d %M %Y') as station_data_LUD from jcdecaux_static_dublin_bikes A, jcdecaux_live_data B where A.station_number=B.station_number")

        try:
            # -------- Execute on database and return values in cursor
            self.__cursor.execute(staticStations)
        except mysql.connector.Error as err:
            print("Could not retrieve static stations, Error: {}".format(err))

        # Creating a list for the returned stations
        for i in self.__cursor:
            station = dict(StationNum=i[0], StationName=i[1], Latitude=float(
                i[2]), Longitude=float(i[3]), Status=i[4], TotalStands = i[5],
                availableBikes = i[6], availableStands=i[7], LUD = i[8])
            self.__stations.append(station)
        
        return self.__stations

    def getStationsById(self,station_num):
        """This method will call the database for static station data"""

        # Query to get the station data from the static table
        query = ("select round(avg(A.station_available_bikes)), A.station_data_LUD from (select *, hour(station_data_LUD) as hours from jcdecaux_dublin_bikes_stations_dump where date(station_data_LUD)=subdate((select distinct date(station_data_LUD) from jcdecaux_live_data), 1) and station_number= %(number)s) A where A.hours >= 6 and A.hours <= 17 group by A.hours")
        try:
            # -------- Execute on database and return values in cursor
            self.__cursor.execute(query, params={"number": int(station_num)})
        except mysql.connector.Error as err:
            print("Could not retrieve stations by id, Error: {}".format(err))

        # Creating a list for the returned stations
        for i in self.__cursor:
            station = dict(availableBikes=int(i[0]), time=i[1])
            self.__stations.append(station)
        return self.__stations

    def getAllDetails(self):

        """This method provides total bikes and stands information"""

        # Query to get the all the data
        totalBikes = ("select sum(station_total_bike_stands), count(*) as totalStations from jcdecaux_live_data")

        try:
            # -------- Execute on database and return values in self.__cursor
            self.__cursor.execute(totalBikes)
        except mysql.connector.Error as err:
            print("Could not retrieve static stations, Error: {}".format(err))
        # Creating a list for the returned stations
        for i in self.__cursor:
            totalDetails = dict(tBikes=int(i[0]), tStations=int(i[1]))
            self.__tDetails.append(totalDetails)

        return self.__tDetails

    def getWeather(self):

        #Query to get the weather data
        weatherData = ("select * from owm_live_data limit 1;")

        try:
            # ------Execute on database and return values in self.__cursor
            self.__cursor.execute(weatherData)
        except mysql.connector.Error as err:
            print("Could not retrieve static stations, Error: {}".format(err))

        # Creating a list for the returned stations
        for i in self.__cursor:
            weatherData = dict(temp = float(i[1]), wDes = (i[4]), wSnow = (i[9]), wRain = (i[10]), wWind = (i[7]))
            self.__wDetails.append(weatherData)
        return self.__wDetails
    
    def closeConn(self):
        self.__cnx.close()
