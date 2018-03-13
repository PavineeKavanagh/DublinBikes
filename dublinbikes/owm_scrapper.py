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
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?id=7778677&mode=json&units=metric&APPID=26025aec9fb58721adba291f0f3291f2')

    cnx = mysql.connector.connect(**config) # ------------------------- Connecting to RDS
    cursor = cnx.cursor()                   # ------------------------- Cursor to execute all the queries
    weathers = json.loads(response.text)    # ------------------------- Loading JSON Data

    # Insert statement to insert values for dublin bike database in the schema ---- %s is the placeholder for the values
    add_weathers = ("INSERT INTO openweathermap_dublin_bikes_dump "
                   "(weather_id, weather_date, weather_main_temp, weather_main_temp_min, weather_main_temp_max,\
                   weather_main_pressure, weather_main_sea_level,weather_main_grnd_level, weather_main_humidity,weather_main_temp_kf, weather_weather_id,\
                    weather_weather_main, weather_weather_des, weather_clouds_all, weather_wind_speed, weather_wind_deg, weather_snow,\
                     weather_rain, weather_sys_pod, weather_sys_dt_txt) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)")
    # Generating the key for the database
    max_key = ("SELECT max(weather_id) from openweathermap_dublin_bikes_dump")
    cursor.execute(max_key) # ---------------------- Execute the query on the database

    key = 0  # ------------------------------------- Holder for the key value
    for i in cursor:
        key = i[0] # ------------------------------- cursor returns a tuple as (max,) so to get the first element we say i[0] --> max
    if key == None:
        key = 1     # ------------------------------ What if there is no data in the table
    else:
        key = key+1  # ------------------------------ setting the new key
    # print(key)
    for weather in weathers['list']:
        weather_date = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.gmtime(weather['dt'] / 1000.0))
        weather_main_temp = weather['main']['temp']
        weather_main_temp_min = weather['main']['temp_min']
        weather_main_temp_max = weather['main']['temp_max']
        weather_main_pressure = weather['main']['pressure']
        weather_main_sea_level = weather['main']['sea_level']
        weather_main_grnd_level = weather['main']['grnd_level']
        weather_main_humidity = weather['main']['humidity']
        weather_main_temp_kf = weather['main']['temp_kf']
        weather_weather_id = weather['weather'][0]['id']
        weather_weather_main = weather['weather'][0]['main']
        weather_weather_des = weather['weather'][0]['description']
        weather_clouds_all = weather['clouds']['all']
        weather_wind_speed = weather['wind']['speed']
        weather_wind_deg = weather['wind']['deg']
        if 'rain' in weather: # -------------------------------- If the key 'rain' does not exist (If it doesn't rain)
            if '3h' in weather['rain']: # ---------------------- If key 'rain' exists but key '3h' doesnt exist (if it doesn't rain in past 3 hours)
                weather_rain = weather['rain']['3h']
            else:
                weather_rain = 0
        else:
            weather_rain = 0
        if 'snow' in weather: # -------------------------------- If the key 'snow' does not exist (If it doesn't snow)
            if '3h' in weather['snow']: # ---------------------- If key 'snow' exists but key '3h' doesnt exist (if it doesn't snow in past 3 hours)
                weather_snow = weather['snow']['3h']
            else:
                weather_snow = 0
        else:
            weather_snow = 0
        weather_sys_pod = weather['sys']['pod']
        weather_sys_dt_txt = weather['dt_txt']

        data_weathers = (key, weather_date, weather_main_temp, weather_main_temp_min, weather_main_temp_max, weather_main_pressure, weather_main_sea_level,weather_main_grnd_level, weather_main_humidity,
                        weather_main_temp_kf, weather_weather_id, weather_weather_main, weather_weather_des, weather_clouds_all, weather_wind_speed, weather_wind_deg, weather_snow, weather_rain, weather_sys_pod, weather_sys_dt_txt)
        # print("Inserting: ",data_weathers)
        cursor.execute(add_weathers,data_weathers)
        key += 1
    cnx.commit()
    cnx.close()

if __name__=="__main__":
    main()

    

