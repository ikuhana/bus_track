import mysql.connector
import config

import csv
import io
import urllib.request

class Datawriter:
    __current_locations = None
    
    def __init__(self, current_locations):
        self.__current_locations = current_locations

    def write_data(self):
        
        self.conn_settings = config.config
        self.cnx = mysql.connector.connect(**self.conn_settings)
        self.cursor = self.cnx.cursor()

        self.query = ("INSERT INTO current_postitions"
                       "(type, number, longitude, latitude, unk, unk2, unk3) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                       
        for n in self.__current_locations:
            self.add_data = tuple(n)
            self.cursor.execute(self.query, self.add_data)
        
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()

class Datareader:
    __url = None
    __content = None

    def __init__(self, url):
        self.__url = url

    def retrieve_data(self):
        self.webpage = urllib.request.urlopen(self.__url)
        self.dataread = csv.reader(io.TextIOWrapper(self.webpage))
        self.__content = list(self.dataread)	
        return(self.__content)

