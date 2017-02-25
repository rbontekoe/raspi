from sense_hat import SenseHat



def name():
	sense = SenseHat()
	pressure = sense.get_pressure()
	return "Luchtdruk in Leusden is " + str(round(pressure, 1)) + " hPa"

print(name())
