import re

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


class UserScreen(Screen):
    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
    def submit(self):
        self.manager.current = 'ResultsScreen'
        print(self.id['bath'])
    # def return_values(self, dprice, bed, bath, sqft):
    #     lst = list()
    #     lst.append(dprice)
    #     lst.append(bed)
    #     lst.append(bath)
    #     lst.append(sqft)
    #     print(lst)

class ResultsScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultsScreen, self).__init__(**kwargs)

# sm.current('UserInput')
class FloatInput(TextInput):
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)
class InterfaceApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(UserScreen(name="UserScreen"))
        sm.add_widget(ResultsScreen(name='ResultsScreen'))
        return sm
InterfaceApp().run()
