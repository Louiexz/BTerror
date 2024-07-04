import os

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang.builder import Builder

Builder.load_file("./assets/scripts/screenDirectory/terrorFiles/terror.kv")

class Terror(BoxLayout):
    source_image = StringProperty('')

    def __init__(self, wm, sound, **kwargs):
        super().__init__(**kwargs)
        self.source_image = "./assets/images/terror/granny.png"
        self.wm = wm
        self.sound = sound

    def get_random_terror(self):
        # Gera um índice aleatório os.urandom
        archives = os.listdir('./assets/images/terror')
        random = int.from_bytes(os.urandom(4), byteorder='big') % len(archives)

        self.source_image = "assets/images/terror/" + archives[random]

        name = archives[random].split(".")
        self.sound.add_to_playlist(name[0])
        
    def exit(self): self.wm.current = 'home'