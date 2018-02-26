from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

import time

class IncrediblyCrudeClock(Label):
    def update(self, *args):
        self.text = time.strftime("%H:%M:%S")

class TimeApp(App):
    def build(self):
        crudeclock = IncrediblyCrudeClock()
        Clock.schedule_interval(crudeclock.update, 1)
        return crudeclock


TimeApp().run()