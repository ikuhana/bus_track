from worker import Datareader, Datawriter 
import time

url = "http://soiduplaan.tallinn.ee/gps.txt"
counter = 0

class bus:
    __position = None
    __speed = None
    __number = None
    __data = None
    __data_dict = None
    
    def __init__(self, __number):
        self.__number = __number
    
    def insert_dot(self, string):
        return string[:2] + '.' + string[2:]

    def distance(self, pos1, pos2):
        from math import sin, cos, sqrt, atan2, radians
        if pos1 == ('', ''):
            return 0
        R = 6373000.0
        lat1 = radians(float(pos1[0]))
        lon1 = radians(float(pos1[1]))
        lat2 = radians(float(pos2[0]))
        lon2 = radians(float(pos2[1]))

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c
        return distance
        
    def get_position(self, data_dict, __number):
        for n in data_dict:
            if n[6] == __number:
                return (self.insert_dot(n[2]), self.insert_dot(n[3]))
                
    def get_speed(self):        
        old_pos = ('', '')
        t1 = time.time()
        while True:
            data = Datareader(url)
            data_dict = data.retrieve_data()
            cur_pos = self.get_position(data_dict, self.__number)
            if old_pos != cur_pos:
                t2 = time.time()
                distance = self.distance(old_pos, cur_pos)
                t = t2 - t1
                print(distance, t)
                print(3.6 * distance / t)
            old_pos = cur_pos
            t1=t2
            time.sleep(1)

cur_bus = bus('405')
cur_bus.get_speed()
    
