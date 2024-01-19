import RPI.GPIO as GPIO
import time

class GPIO:
	def __init__(self,pin):
		self.pin = pin
		GPIO.setmode(GPIO.BOARD)
	
	def pin_out(self):
		GPIO.setup(self.pin,GPIO.OUT)
	
	def pin_in(self):
		GPIO.setup(self.pin,GPIO.IN)
	
	def set_high(self):
		GPIO.output(self.pin,True)
	
	def set_low(self):
		GPIO.output(self.pin, False)


