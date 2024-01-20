import os
import time
import thresholds.EC as ec
import thresholds.PH as ph
import constants as const
import utils.utilities as util

def ec_logic(ec_obj,motor_obj:list):
	## 2 driver object 1 obj 2 2 obj 1
	if len(motor_obj) < const.ec_motors_size:
		return "unsupported driver objects to enable motors"
	##unloading threshold weights
	thresolds = ec.threshold_dict
	ec_value = ec_obj.query("R")
	diff_rate = None

	if float(ec_value) < 100:
		diff_rate = 100
	elif float(ec_value) > 100 and float(ec_value) < 500:
		diff_rate = 500
	elif float(ec_value) > 500 and float(ec_value) < 850:
		diff_rate = 850
	else:
		diff_rate = None

	if diff_rate != None:
		for idx,obj in enumerate(motor_obj):
			obj.enable(thresholds[diff_rate][i])
	return 0

def ph_logic(ph_obj, motor_obj:list):
	
	acidic_pump_obj , basic_pump_obj = motor_obj
	if len(motor_obj) < const.ph_motors_size:
		return "Unsupported driver objects to enable motor"
	
	thresholds = ph.threshold_dict
	ph_value = ph_obj.query("R")
	ph_diff = None

	if ph_diff < 5.5:
		basic_pump_obj.enable(thresholds[ph_diff][0])

	elif ph_diff > 6.5:
		acidic_pump_obj.enable(thresholds[ph_diff][1])

	else:
		print("PH solution is in good state")

	return 0



def dht_logic(dht_obj:list , relay_humidifier_obj, relay_dehumidifier_obj):
	
	avg_temperature , avg_humidity = 0 , 0

	for obj in dht_obj:
		dht_reading = obj.read()
		avg_temperature += dht_reading[0]
		avg_humidity += dht_reading[1]

	vpd_value = util.calculate_vpd(avg_temperature,avg_humidity)
	if vpd_value > 1.3:
		relay_humidifier_obj.toggle_high()

	elif vpd_value < 0.8:
		relay_dehumidifier_obj.toggle_high()
	else:
		relay_humidifier_obj.toggle_low()
		relay_dehumidifier_obj.toggle_low()

	return 0
	
