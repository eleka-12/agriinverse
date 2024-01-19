import io
import fcntl
import time
import string

class EC:
	long_timeout = 5
	short_timeout = 5
	default_bus = 1
	default_address = 100

	def __init__(self,address=default_address,bus = default_bus):
		self.file_read = io.open("/dev/i2c-" + str(bus), "rb" , buffering = 0)
		self.file_write = io.open("/dev/i2c-" + str(bus), "wb" , bbuffering =0)
		self.set_i2c_address(address)
	
	def set_i2c_address(self,addr):
		I2C_SLAVE = 0x703
		fcntl.ioctl(self.file_read , I2C_SLAVE, addr)
		fcntl.ioctl(self.file_write, I2C_SLAVE, addr)
	
	def write(self,string):
		string += "0"
		self.file_write.write(string)
	def read(self,num_of_bytes = 31):
		res = self.file_read.read(num_of_bytes)
		response = filter(lambda x:x != 'x00', res)
		if ord(response[0] == 1):
			char_list = map(lambda x:chr(ord(x) & ~0x80),list(response[1:]))
			return "command succeed " + "".join(char_list)
		else:
			return "Error "+str(ord(response[0]))

	def query(self,string):
		self.write(string)
		if ((string.upper().startswith("R")) or (string.upper().startswith("CAL"))):
			time.sleep(self.long_timeout)
		elif ((string.upper().startswith("SLEEP"))):
			return "sleep mode"
		else:
			time.sleep(self.short_timeout)
		return self.read()
	def close(self):
		self.file_read.close()
		self.file_write.close()
