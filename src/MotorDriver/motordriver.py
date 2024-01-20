import os
import time
import GPIO as gpio

class MotorDriver:
	def __init__(self,pina,pinb=None):
		self.pina = pina
		self.pinb = pinb
		#initializing pina and pinb
		self.pin_a = gpio.GPIO(pina)
		self.pin_a.pin_out()
		turn_off_pina()
		if self.pinb != None:
			self.pin_b = gpio.GPIO(pinb)
			self.pin_b.pin_out()
			turn_off_pinb()
	
	def turn_on_pina(self):
		self.pin_a.set_high()
		return 0

	def turn_off_pina(self):
		self.pin_a.set_low()
		return 0

	def turn_on_pinb(self):
		self.pin_b.set_high()
		return 0

	def turn_off_pinb(self):
		self.pin_b.set_low()
		return 0
