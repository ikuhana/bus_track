from worker import Datareader, Datawriter 

url = "http://soiduplaan.tallinn.ee/gps.txt"
data = Datareader(url)
write = Datawriter(data.retrieve_data())
write.write_data()
