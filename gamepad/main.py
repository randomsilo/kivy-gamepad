from kivy.app import App
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


LabelBase.register(name="Aller",
                   fn_regular="fonts/Aller_Rg.ttf",
                   fn_bold="fonts/Aller_Bd.ttf",
                   fn_italic="fonts/Aller_It.ttf",
                   fn_bolditalic="fonts/Aller_BdIt.ttf")

# Builder KV
Builder.load_string("""
<TitleLabel@Label>:
    markup: True
    font_name: 'Aller'
    font_size: 60

<SubTitleLabel@Label>:
    markup: True
    font_name: 'Aller'
    font_size: 40

<CommandButton@Button>:
    font_name: 'Aller'
    font_size: 25
    bold: True
    border: (2, 2, 2, 2)

<HomeScreen>
    name: 'home_screen'
    BoxLayout:
        orientation: 'vertical'

        TitleLabel:
            id: title_label 
            text: 'Game Title'

        SubTitleLabel:
            id: subtitle_label 
            text: 'By Whomever'

        BoxLayout:
            orientation: 'horizontal'

            CommandButton:
                id: start_button
                text: 'Start'
                background_normal: 'images/button_normal.png'
                background_down: 'images/button_down.png'
                on_press: 
                    root.manager.current = 'demo_screen'
            
            CommandButton:
                id: exit_button
                text: 'Exit'
                background_normal: 'images/red_button_normal.png'
                background_down: 'images/red_button_down.png'
                on_press: 
                    app.pressed_exit()

<DemoScreen>
    name: 'demo_screen'
    BoxLayout:
        orientation: 'vertical'

        TitleLabel:
            id: title_label 
            text: 'Demo Game Pad'

        BoxLayout:
            orientation: 'horizontal'
            
            CommandButton:
                id: home_button
                text: 'Go Home'
                background_normal: 'images/red_button_normal.png'
                background_down: 'images/red_button_down.png'
                on_press:
                    root.manager.current = 'home_screen'
""")

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
        return sm

    def pressed_home(self):
        self.root.manager.current = 'home_screen'

    def pressed_start(self):
        self.root.manager.current = 'demo_screen'

    def pressed_exit(self):
        App.get_running_app().stop()

if __name__ == '__main__':
    GamePadApp().run()


