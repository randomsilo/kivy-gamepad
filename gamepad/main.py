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

<FighterName@Label>:
    markup: True
    font_name: 'Aller'
    font_size: 20

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
        id: screen_container
        orientation: 'vertical'

        Button:
            id: home_button
            text: 'Go Home'
            size_hint: (1, 0.1)
            background_normal: 'images/red_button_normal.png'
            background_down: 'images/red_button_down.png'
            on_press:
                root.manager.current = 'home_screen'
    
        GridLayout:
            id: screen_top
            size_hint: (1, 0.1)
            rows: 1
            cols: 3
            padding: 0
            spacing: 0

            BoxLayout:
                id: screen_top_player
                orientation: 'horizontal'

                FighterName:
                    id: player_character_name
                    text: 'Unknown'

            BoxLayout:
                id: screen_top_round_data
                orientation: 'horizontal'

                FighterName:
                    id: fight_round
                    text: 'Round 1'

            BoxLayout:
                id: screen_top_opponent
                orientation: 'horizontal'

                FighterName:
                    id: player_opponent_name
                    text: 'Mr. Pain'

        BoxLayout:
            id: screen_fight_arena
            size_hint: (1, 0.6)
            orientation: 'vertical'

            TitleLabel:
                text: 'Arena Picture'

        GridLayout:
            id: screen_bottom
            size_hint: (1, 0.3)
            rows: 1
            cols: 3
            padding: 0
            spacing: 0

            GridLayout:
                id: direction_pad
                rows: 3
                cols: 3
                padding: 0
                spacing: 0

                Button:
                    id: direction_pad_left_up
                    text: 'UL'
                
                Button:
                    id: direction_pad_left
                    text: 'ML'

                Button:
                    id: direction_pad_left_down
                    text: 'DL'
                
                Button:
                    id: direction_pad_up
                    text: 'UP'
                
                Button:
                    id: direction_pad_center
                    text: 'CT'

                Button:
                    id: direction_pad_down
                    text: 'DN'

                Button:
                    id: direction_pad_right_up
                    text: 'UR'
                
                Button:
                    id: direction_pad_right
                    text: 'MR'

                Button:
                    id: direction_pad_right_down
                    text: 'DR'

            GridLayout:
                id: control_pad
                rows: 2
                cols: 2
                padding: 0
                spacing: 0

                Button:
                    id: control_pad_left_trigger
                    text: 'LT'

                Button:
                    id: control_pad_right_trigger
                    text: 'RT'

                Button:
                    id: control_pad_left_bumper
                    text: 'LB'
                
                Button:
                    id: control_pad_right_bumper
                    text: 'RB'
                
            GridLayout:
                id: action_pad
                rows: 3
                cols: 3
                padding: 0
                spacing: 0

                Label:
                    text: ''
                
                Button:
                    id: action_pad_action_one
                    text: 'A1'

                Label:
                    text: ''
                
                Button:
                    id: action_pad_action_two
                    text: 'A2'
                
                Label:
                    text: ''

                Button:
                    id: action_pad_action_three
                    text: 'B1'

                Label:
                    text: ''
                
                Button:
                    id: action_pad_action_four
                    text: 'B2'

                Label:
                    text: ''   

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


