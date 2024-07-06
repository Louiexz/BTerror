import os

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang.builder import Builder

Builder.load_file("./assets/scripts/screenDirectory/terrorFiles/terror.kv")

class Terror(BoxLayout):
    source_image = StringProperty('')

    def __init__(self, wm, sound, **kwargs):
        super().__init__(**kwargs)
        self.wm = wm
        self.sound = sound
        self.source_image = self.initial_image()

    def get_random_terror(self):
        # Gera um índice aleatório os.urandom
        archives = os.listdir('./assets/images/terror')
        random = int.from_bytes(os.urandom(4), byteorder='big') % len(archives)

        self.source_image = "assets/images/terror/" + archives[random]

        name = archives[random].split(".")
        self.sound.add_to_playlist(f"terror/{name[0]}")
    
    def initial_image(self):
        self.sound.add_to_playlist("terror/granny")
        return "assets/images/terror/granny.png"
        
    def exit(self):
        self.sound.add_to_playlist("home/let's")
        self.wm.current = 'home'