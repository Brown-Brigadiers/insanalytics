from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class UserInput(BoxLayout):
    values = ListProperty()
    def __init__(self, **kwargs):
        super(UserInput, self).__init__(**kwargs)
    # def on_press(self):
    #         self.values =

class Interface(App):
    def build(self):
        return UserInput()
Interface().run()
