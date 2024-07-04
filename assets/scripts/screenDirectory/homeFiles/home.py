from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file("assets/scripts/screenDirectory/homeFiles/home.kv")

class Home(BoxLayout):
    def __init__(self, wm, sound, **kwargs):
        super().__init__(**kwargs)
        self.wm = wm
        sound.add_to_playlist("home/let's")

    def go_to_terror(self): self.wm.current = 'terror'
