from assets.scripts.functs.manage import *
from kivy.app import App

from assets.scripts.functs.sound import SoundPlayer

class ScreenApp(App):
    def build(self):
        self.title = "BTerror"
        sound = SoundPlayer()
        
        wm = ScreenManager()
        wm.add_widget(SplashScreen(name='splash', wm=wm, sound=sound))
        wm.add_widget(TerrorScreen(name='terror', wm=wm, sound=sound))
        wm.add_widget(HomeScreen(name='home', wm=wm, sound=sound))
        
        # Set 'home' screen as the initial screen
        wm.current = 'splash'
        
        return wm

if __name__ == '__main__': ScreenApp().run()
