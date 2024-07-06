from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file("assets/scripts/screenDirectory/homeFiles/home.kv")

class Home(BoxLayout):
    def __init__(self, wm, sound, **kwargs):
        super().__init__(**kwargs)
        self.wm = wm
        self.sound = sound

    def go_to_terror(self):
        self.wm.current = 'terror'

    def go_to_credits(self):
        self.sound.add_to_playlist("credits/bterror")
        self.wm.current = 'credits'