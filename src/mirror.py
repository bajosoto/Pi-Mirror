from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

import time
import weather

class ClockFace(Widget):
	def update(self, *args):
		# self.text = time.strftime("%H:%M:%S")
		# self.font_size = 120
		# self.font_name = "../assets/fonts/alarm-clock.ttf"
		self.ids["clock"].text = time.strftime("%H:%M:%S")
		print(weather.getWeather())

# class IncrediblyCrudeClock(Label):
# 	def update(self, *args):
# 		self.text = time.strftime("%H:%M:%S")
# 		self.font_size = 120
# 		self.font_name = "../assets/fonts/alarm-clock.ttf"
# 		print(weather.getWeather())

class ClockFaceApp(App):
    def build(self):
        crudeclock = ClockFace()
        Clock.schedule_interval(crudeclock.update, 1)
        return crudeclock

clockFaceApp = ClockFaceApp()
clockFaceApp.run()

