import os

from src.EC.EC import EC
from src.PH.PH import PH
from src.DHT.DHT import DHT
from initializers import *

def setup():
	## initializing all objects and variables for the loop
	ec = initialize_EC()
	ph = initialize_PH()
	DHT = initialize_DHT()


def loop():
	pass

