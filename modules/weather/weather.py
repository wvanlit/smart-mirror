from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock

import requests
import datetime
from dateutil import tz

filepath = 'modules/weather/'
def getKey():
	key = open(filepath+'darksky.key', 'r')
	return key.read()

from_zone = tz.tzutc()
to_zone = tz.tzlocal()

def convertUNIXToLocalHour(unix):
	utc = datetime.datetime.utcfromtimestamp(unix)
	utc = utc.replace(tzinfo=from_zone)

	localTime = utc.astimezone(to_zone)
	return localTime.strftime("%H:00")

def getTemperatureColor(temperature):
	if temperature >= 30:
		return 'd11f1f'
	elif temperature >= 25:
		return 'd16f1f'
	elif temperature >= 20:
		return 'b4d413'
	elif temperature >= 15:
		return '53d413'
	elif temperature >= 10:
		return '13d450'
	elif temperature >= 5:
		return '13d4b1'
	elif temperature >= 0:
		return '13d4ce'
	elif temperature >= -5:
		return '1384d4'
	else:
		return '132dd4'

def getRainColor(percentage):
	if percentage >= 75:
		return '132dd4'
	elif percentage >= 50:
		return '1394d4'
	elif percentage >= 25:
		return '13d45a'
	else:
		return '50d413'

api_url = f'https://api.darksky.net/forecast/{getKey()}/51.8791,4.6296'
def getWeather():
	result = requests.get(api_url)
	json = result.json()

	summary = json['hourly']['summary']

	weatherList = f'[color=#ffffff][u]Weather Summary:[/u]\n{summary}\n\n[u]Weather Per Hour:[/u]\n'
	hourlyWeather = json['hourly']['data']
	for i in range(0,12):
		weather = hourlyWeather[i]
		
		description = weather['summary']
		time = convertUNIXToLocalHour(weather['time'])
		temperature_fahrenheit = float(weather['temperature'])
		temperature = (temperature_fahrenheit - 32) * 5.0/9.0
		rainChance = float(weather['precipProbability'])*100

		weatherList += f'{time} | {description:20s} | [color=#{getTemperatureColor(temperature)}]{temperature:.2f}[/color] degrees | rain [color=#{getRainColor(rainChance)}]{rainChance:.0f}%[/color] \n'

	weatherList += '[/color]'
	return weatherList


class WeatherWidget(Widget):
	weather = StringProperty()

	def updateWeather(self, dt):
		self.weather = getWeather()



def BuildWidget():
	widget = WeatherWidget()
	widget.updateWeather(0)
	Clock.schedule_interval(widget.updateWeather, 600)
	return widget


