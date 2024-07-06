from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.lang.builder import Builder

Builder.load_file("assets/scripts/screenDirectory/splashFiles/splash.kv")

class Splash(BoxLayout):
    def __init__(self, wm, sound, **kwargs):
        super().__init__(**kwargs)
        self.wm = wm
        sound.add_to_playlist("splash/monster")
        self.sound = sound

        Clock.schedule_once(lambda dt:self.trigger_home(dt), 7)
    
    def trigger_home(self, dt):
        self.sound.add_to_playlist("home/let's")
        self.wm.current = "home"