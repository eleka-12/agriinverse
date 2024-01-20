import os
import time
import thresholds.EC as ec
import thresholds.PH as ph

def ec_logic(ec_obj,motor_obj:list):
	## 2 driver object 1 obj 2 2 obj 1
	if len(motor_obj) < 3:
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
			obj.enable(thresholds[diff_rate][i]


