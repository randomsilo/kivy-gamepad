from kivy.app import App
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from managers import IoManager


LabelBase.register(name="Aller",
                   fn_regular="fonts/Aller_Rg.ttf",
                   fn_bold="fonts/Aller_Bd.ttf",
                   fn_italic="fonts/Aller_It.ttf",
                   fn_bolditalic="fonts/Aller_BdIt.ttf")

# Builder KV
Builder.load_file('ui/styles.kv')
Builder.load_file('ui/game-pad.kv')
Builder.load_file('ui/home-screen.kv')
Builder.load_file('ui/demo-screen.kv')

# Screens
class HomeScreen(Screen):
    pass

class DemoScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(HomeScreen(name='home_screen'))
sm.add_widget(DemoScreen(name='demo_screen'))


class GamePadApp(App):
    def build(self):
        self.io_manager_impl = IoManager.IoManagerStock()
        return sm

    def pressed_home(self):
        self.root.manager.current = 'home_screen'

    def pressed_start(self):
        self.root.manager.current = 'demo_screen'

    def pressed_exit(self):
        App.get_running_app().stop()

if __name__ == '__main__':
    GamePadApp().run()


