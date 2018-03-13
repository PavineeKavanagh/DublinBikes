# Downloads data from Openweathermap and loads it into Mysql database

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

    #Getting json response from OWM
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=7778677&APPID=26025aec9fb58721adba291f0f3291f2'


    cnx = mysql.connector.connect(**config) # ------------------------- Connecting to RDS
    cursor = cnx.cursor()                   # ------------------------- Cursor to execute all the queries
    stations = json.loads(response.text)    # ------------------------- Loading JSON Data

    # Insert statement to insert values for dublin bike database in the schema ---- %s is the placeholder for the values
    add_weather = ("INSERT INTO openweathermap_dublin_bikes_dump "
                   "(weather_date, weather_main_temp,weather_main_temp_min,weather_main_temp_max, \
                   weather_main_pressure, weather_city_coord, weather_main_sea_level, weather_main_grnd_level,\
                    weather_main_temp_kf, weather_weather_id, weather_weather_main, weather_weather_des,\
                     weather_weather_icon, weather_clouds_all, weather_wind_speed, weather_wind_deg, weather_snow, weather_sys_pod,\
                      weather_sys_dt_txt, weather_city_id, weather_city_name, weather_city_coord_lat, weather_city_coord_lan, weather_city_coord_country ) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)")