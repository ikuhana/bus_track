import mysql.connector
import config

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
            print(self.add_data)
            self.cursor.execute(self.query, self.add_data)
        
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()
        
        
#~ url = "http://soiduplaan.tallinn.ee/gps.txt"
#~ data = fetch_data.Datareader(url)
#~ 
#~ write = Datawriter(data.retrieve_data())
#~ write.write_data()
#~ for n in data.retrieve_data():
    #~ add_data = tuple(n)
    #~ print(add_data)
    #~ cursor.execute(query, add_data)
    
