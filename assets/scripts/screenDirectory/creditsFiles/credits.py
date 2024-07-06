import sys

from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file("assets/scripts/screenDirectory/creditsFiles/credits.kv")
class Credits(BoxLayout):
    def __init__(self, wm, sound, **kwargs):
        super().__init__(**kwargs)
        self.wm = wm
        self.sound = sound
    
    def go_to_home(self):
        self.sound.add_to_playlist("home/let's")
        self.wm.current = "home"
    
    def exit(self): sys.exit()