from worker import Writestops
import sys


Writestops(sys.argv[1]).insert_db()

print(sys.argv[1])
#~ url = "http://soiduplaan.tallinn.ee/gps.txt"
#~ while True:
    #~ print(1)
    #~ data = Datareader(url)
    #~ write = Datawriter(data.retrieve_data())
    #~ write.write_data()
    #~ time.sleep(10)
