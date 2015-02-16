from worker import Datareader, Datawriter 
import time

url = "http://soiduplaan.tallinn.ee/gps.txt"
counter = 0
while True:
    data = Datareader(url)
    write = Datawriter(data.retrieve_data())
    write.write_data()
    counter += 1
    print(counter)
    time.sleep(30)
