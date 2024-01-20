import os
import time
from src.DHT.DHT import DHT
from src.EC.EC import EC
from src.PH.PH import PH

def initialize_DHT(pins : list) -> list:
	dht_objects = []
	## generating objects for DHT sensors
	for pin in pins:
		dht_objects.append(DHT(pin))
	return dht_objects

def initialize_EC():
	## generating object for EC sensor
	ec_object = EC()
	return ec_object

def initialize_PH():
	## generating object for PH sensor
	ph_object = PH()
	return ph_object


