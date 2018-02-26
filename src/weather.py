import pyowm

owm = pyowm.OWM('18dffc1646058520620999d7b7929e1b') 

# Search for current weather in Eindhoven
observation = owm.weather_at_place('Eindhoven,NL')
w = observation.get_weather()
# Weather details
# print(w.get_wind())                  # {'speed': 4.6, 'deg': 330}
# print(w.get_humidity())              # 87
# print(w.get_temperature('celsius')['temp'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

def getWeather():
	# Search for current weather in Eindhoven
	observation = owm.weather_at_place('Eindhoven,NL')
	w = observation.get_weather()
	return w.get_temperature('celsius')