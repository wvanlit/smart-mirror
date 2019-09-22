from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window
Window.fullscreen = True

from modules.clock import clock
from modules.calendar import calendar
from modules.weather import weather
# Load kv files
clockFile = Builder.load_file('modules/clock/clock.kv')
calendarFile = Builder.load_file('modules/calendar/calendar.kv')
weatherFile = Builder.load_file('modules/weather/weather.kv')


class MirrorApp(App):
	def build(self):
		layout = GridLayout(rows=3, cols=3)

		layout.add_widget(clock.BuildWidget())
		layout.add_widget(Widget())
		layout.add_widget(calendar.BuildWidget())

		layout.add_widget(weather.BuildWidget())
		layout.add_widget(Widget())
		layout.add_widget(Widget())

		layout.add_widget(Widget())
		layout.add_widget(Widget())
		layout.add_widget(Widget())

		return layout


if __name__ == '__main__':
	# Run App
	MirrorApp().run()
