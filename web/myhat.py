from sense_hat import SenseHat
sense = SenseHat()

def name():
	pressure = sense.get_pressure()
	return str(round(pressure, 1))

def temp():
	temp = sense.get_temperature()
	return str(round(temp, 1))

def hum():
	hum = sense.get_humidity()
	return str(round(hum, 1))

print(name())
print(temp())
print(hum())

