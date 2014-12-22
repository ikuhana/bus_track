import mysql.connector
from mysql.connector import errorcode
import fetch_data, config

conn_settings = config.config

cnx = mysql.connector.connect(**conn_settings)
  
cursor = cnx.cursor()


query = ("INSERT INTO current_postitions"
               "(type, number, longitude, latitude, unk, unk2, unk3) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")

url = "http://soiduplaan.tallinn.ee/gps.txt"
data = fetch_data.Datareader(url)
for n in data.retrieve_data():
    add_data = tuple(n)
    print(add_data)
    cursor.execute(query, add_data)
    
cnx.commit()
cursor.close()
cnx.close()

