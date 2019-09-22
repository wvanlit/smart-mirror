from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock

from datetime import datetime

class ClockWidget(Widget):
	time = StringProperty()

	def update_time(self, dt):
		self.time = datetime.now().strftime("[color=#ffffff]%H:%M:%S\n%m/%d/%Y[/color]")

def BuildWidget():
	# Build Clock
	widget = ClockWidget()
	Clock.schedule_interval(widget.update_time, 0.5)
	return widget