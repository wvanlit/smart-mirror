from kivy.uix.widget import Widget
from kivy.properties import StringProperty


import requests
import datetime

api_url = 'https://api.openweathermap.org/data/2.5/forecast?q=Alblasserdam&APPID='
filepath = 'modules/weather/'

def createAPIurl():
	key = open(filepath+'openWeather.key', 'r')
	return api_url+key.read()

def getWeather():
	result = requests.get(createAPIurl())
	json = result.json()
	weatherArray = json['list']
	city = json['city']['name']

	weatherList = f'The Weather in {city} for the next 12 hours:\n'
	for i in range(4):
		weather = weatherArray[i]
		time = weather['dt_txt']
		time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')	
		temperature = round(int(weather['main']['temp']) - 273.15, 0)
		weatherType = weather['weather'][0]['description']

		weatherList += f'{time.strftime("%H:00")} - {weatherType} - {temperature:.0f} degrees\n'

	return weatherList


class WeatherWidget(Widget):
	weather = StringProperty()

	def updateWeather(self, dt):
		self.weather = getWeather()




