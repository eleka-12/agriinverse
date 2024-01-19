import time
import GPIO.GPIO as gpio


class Relay:
	def __init__(self,pin):
		self.pin = pin
		gpio.pin_out(pin)
	
	def toggle_high(self):
		

