from kivy.uix.screenmanager import ScreenManager, Screen
from assets.scripts.screenDirectory.splashFiles.splash import Splash
from assets.scripts.screenDirectory.terrorFiles.terror import Terror
from assets.scripts.screenDirectory.creditsFiles.credits import Credits
from assets.scripts.screenDirectory.introduceFiles.introduce import Introduce
from assets.scripts.screenDirectory.homeFiles.home import Home

class IntroduceScreen(Screen, Introduce):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Introduce.__init__(self, **kwargs)  # Initialize Terror functionality

class CreditsScreen(Screen, Credits):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Credits.__init__(self, **kwargs)  # Initialize Terror functionality

class TerrorScreen(Screen, Terror):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Terror.__init__(self, **kwargs)  # Initialize Terror functionality

class HomeScreen(Screen, Home):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Home.__init__(self, **kwargs)  # Initialize Home functionality

class SplashScreen(Screen, Splash):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Splash.__init__(self, **kwargs)

class WindowManager(ScreenManager): pass