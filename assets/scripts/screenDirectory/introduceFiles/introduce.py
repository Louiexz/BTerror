from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.lang.builder import Builder

Builder.load_file("assets/scripts/screenDirectory/introduceFiles/introduce.kv")

class Introduce(BoxLayout):
    def __init__(self, wm, **kwargs):
        super().__init__(**kwargs)
        self.wm = wm

        Clock.schedule_once(lambda dt:self.trigger_splash(dt), 5)
    
    def trigger_splash(self, dt):
        self.wm.current = "splash"