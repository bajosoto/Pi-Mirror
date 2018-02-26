from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

import time
import weather

class ClockFace(Widget):
	def updateTime(self, *args):
		self.ids["clock"].text = time.strftime("%H:%M:%S")

	def updateTemp(self, *args):
		self.ids["temp"].text = str(int(weather.getWeather()['temp'])) + 'c'
		self.ids["mintemp"].text = str(int(weather.getWeather()['temp_min'])) + 'c'
		self.ids["maxtemp"].text = str(int(weather.getWeather()['temp_max'])) + 'c'

class ClockFaceApp(App):
    def build(self):
        crudeclock = ClockFace()
        Clock.schedule_interval(crudeclock.updateTime, 1)
        Clock.schedule_interval(crudeclock.updateTemp, 2)
        return crudeclock

clockFaceApp = ClockFaceApp()
clockFaceApp.run()

