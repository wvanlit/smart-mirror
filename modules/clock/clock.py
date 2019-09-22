from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from datetime import datetime

class ClockWidget(Widget):
	time = StringProperty()

	def update_time(self, dt):
		self.time = datetime.now().strftime("%H:%M:%S\n%m/%d/%Y")
