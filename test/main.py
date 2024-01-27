from SPI import MCP3008 as spi

spi_connection = spi()
ec_values = spi_connection.read_out(0) ## EC sensor
ph_values = spi_connection.read_out(1) ## PH sensor

while(1):
	print("EC values",ec_values)
	print("PH values",ph_values)
