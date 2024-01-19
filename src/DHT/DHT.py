import Adafruit_DHT as dht
from time import sleep

class DHT:
	def __init__(self,data_pin):
		self.data_pin = data_pin
	
	def read(self,sensor_type:str):
		humidity, temp = dht.read_retry(dht.sensor_type,DHT)
		return humidity , temp

