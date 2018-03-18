import mysql.connector
from mysql.connector import errorcode

class Station():
    """ This is a class which provides all the information with respect to Dubline Bike Stations"""

    def __init__(self):
        self.__stations = []

    def getStation(self):

        """This method will call the database for static station data"""

        # Connecting to the MySQL Db
        config = {
            'user': 'root',
            'password': '00001234',
            'host': 'dublinbikescomp30670.c8lbidkpdn4h.us-east-2.rds.amazonaws.com',
            'database': 'dublinbikes',
            'raise_on_warnings': True,
        }

        # Trying to connect to the database
        try:
            cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        # Cursor to perform the executions to the db
        cursor = cnx.cursor()

        # Query to get the station data from the static table
        staticStations = ("Select * from jcdecaux_static_dublin_bikes")

        try:
            # -------- Execute on database and return values in cursor
            cursor.execute(staticStations)
        except mysql.connector.Error as err:
            print("Could not retrieve static stations, Error: {}".format(err))

        # Creating a list for the returned stations
        for i in cursor:
            station = dict(StationNum=i[1], StationName=i[2], StationAddr=i[3], Latitude=float(
                i[4]), Longitude=float(i[5]))
            self.__stations.append(station)
        
        return self.__stations