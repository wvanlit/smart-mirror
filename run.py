from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

from modules.clock import clock

# Load kv files
clockFile = Builder.load_file('modules/clock/clock.kv')

class MirrorApp(App):
	def build(self):
		layout = GridLayout(rows = 1, cols = 1)

		# Build Clock
		clockWidget = clock.ClockWidget()
		Clock.schedule_interval(clockWidget.update_time, 0.5)
		layout.add_widget(clockWidget)



		return layout


if __name__ == '__main__':
	# Run App
	MirrorApp().run()
