from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

from modules.clock import clock
from modules.calendar import calendar

# Load kv files
clockFile = Builder.load_file('modules/clock/clock.kv')
calendarFile = Builder.load_file('modules/calendar/calendar.kv')

class MirrorApp(App):
	def build(self):
		layout = GridLayout(rows = 2, cols = 1)

		# Build Clock
		clockWidget = clock.ClockWidget()
		Clock.schedule_interval(clockWidget.update_time, 0.5)
		layout.add_widget(clockWidget)

		# Build Calendar
		calendarWidget = calendar.CalendarWidget()
		calendarWidget.setUpCalendar()
		calendarWidget.updateCalendar(0)
		Clock.schedule_interval(calendarWidget.updateCalendar, 600)
		layout.add_widget(calendarWidget)

		return layout


if __name__ == '__main__':
	# Run App
	MirrorApp().run()
