from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

from modules.clock import clock

# Load kv files
clockFile = Builder.load_file('modules/clock/clock.kv')


class MirrorWidget(Widget):
	layout = GridLayout(rows = 2, cols = 1)
	layout.add_widget(clock.ClockWidget())
	layout.add_widget(clock.ClockWidget())


class MirrorApp(App):
	def build(self):
		mirror = MirrorWidget()
		return mirror.layout


if __name__ == '__main__':
	# Run App
	MirrorApp().run()
