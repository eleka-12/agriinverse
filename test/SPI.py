import sys
sys.path.append('./Adafruit_CircuitPython_MCP3xxx')
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

class MCP3008:
	def __init__(self):
		self.spi = busio.SPI(clock = board.SCK, MISO=board.MISO, MOSI=board.MOSI)
		self.cs = digitalio.DigitalInOut(board.DS)
		self.mcp = MCP.MCP3008(spi,cs)
	
	def read_out(self,channel_pin:str):
		channel_pin = self._get_pin(channel_pin)
		channel_out = AnalogIn(self.mcp,channel_pin)
		return channel_out.value,channel_out.voltage
	
	def _get_pin(self,pin_from_usr):
		if pin_from_usr > 8:
			return "invalid input pin"
		return "P"+str(pin_from_usr)

	
