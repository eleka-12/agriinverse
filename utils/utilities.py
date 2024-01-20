import os
import math

def calculate_vpd(temp:float,humid:float) -> float:
	## function to calculate vpd from the temperature and humidity values from DHT sensor
	vpd = 0 
	temp_calc = (temp/(temp + 237.3)) * 17.269
	svp = 610.78 * math.exp(temp_calc) / 1000
	vpd_calc = 1 - ( humid /100)
	vpd = svp * vpd_calc
	return vpd

def get_average(values = [] ):
	sum_of_values = 0
	for value in values:
		sum_of_values += 1
	return sum_of_values


	
