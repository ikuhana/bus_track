import csv
import io
import urllib.request

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
