# Downloads data from JCDeacaux and loads it into Mysql database

from mysql.connector import errorcode
import mysql.connector
import requests
import json
import time

def main():
    # Configuration values for mysql connection
    config = {
        'user': 'root',
        'password': '00001234',
        'host': 'dublinbikescomp30670.c8lbidkpdn4h.us-east-2.rds.amazonaws.com',
        'database': 'dublinbikes',
        'raise_on_warnings': True,
    }

    # Getting json response fro JCDecaux
    url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey='
    apiKey = '72ad8bb012e2e3c42c7d2c9665b3b9f875d03bac'
    apiurl = url+apiKey
    
    try:
        response = requests.get(apiurl, timeout = 3)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as reqErr:
        print("Fatal Error: ",reqErr)
    

    try:
        cnx = mysql.connector.connect(**config) # ------------------------- Connecting to RDS
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    
    cursor = cnx.cursor()                   # ------------------------- Cursor to execute all the queries
    stations = json.loads(response.text)    # ------------------------- Loading JSON Data

    # Insert statement to insert values for dublin bike database in the schema ---- %s is the placeholder for the values
    add_station = ("INSERT INTO jcdecaux_dublin_bikes_stations_dump "
                   "(station_id,station_number,station_name,station_address,station_pos_lat,station_pos_lon,station_banking,station_bonus,\
               station_status,station_contract_name,station_total_bike_stands,station_available_bike_stands,\
               station_available_bikes,station_data_LUD) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)")
    
    # print("Adding Values")

    # Generating the key for the database
    max_key = ("SELECT max(station_id) from jcdecaux_dublin_bikes_stations_dump")
    try:
        cursor.execute(max_key) # ---------------------- Execute the query on the database
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    

    key = 0 # -------------------------------------- Holder for the key value
    for i in cursor:
        key = i[0] # ------------------------------- cursor returns a tuple as (max,) so to get the first element we say i[0] --> max
    if key == None:  
        key = 1     # ------------------------------ What if there is no data in the table
    else:           
        key = key+1 # ------------------------------ setting the new key
    # print("Key: ",key)
    # Getting the values from the json response from JCD
    for station in stations:
        station_number = station['number']
        station_name = station['name']
        station_address = station['address']
        station_pos_lat = station['position']['lat']
        station_pos_lon = station['position']['lng']
        station_banking = station['banking']
        station_bonus = station['bonus']
        station_status = station['status']
        station_contract_name = station['contract_name']
        station_total_bike_stands = station['bike_stands']
        station_available_bike_stands = station['available_bike_stands']
        station_available_bikes = station['available_bikes']
        timestamp = station['last_update']

        station_data_LUD = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.gmtime(timestamp / 1000.0))  # --------- Converting the timestamp in MySQL Format
        
        # Tuple holding the values
        data_station = (key, station_number, station_name, station_address, station_pos_lat, station_pos_lon, station_banking, station_bonus,
                        station_status, station_contract_name, station_total_bike_stands, station_available_bike_stands, station_available_bikes, station_data_LUD)
        # print("Inserting: ",data_station)
        # Executing the query
        try:
            cursor.execute(add_station, data_station)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        
        key+=1 # ------------ Get the next key

    cnx.commit() # ---------------------- Commiting the changes since InnoDB
    cnx.close()     # ---------------------- Close the connection

if __name__=="__main__":
    main()
