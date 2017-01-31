import re

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from user import User


class UserScreen(Screen):
    text = StringProperty('')
    def submit(self):
        dprice = self.ids.dprice.text
        bed = self.ids.bed.text
        bath = self.ids.bath.text
        sqft = self.ids.sqft.text
        self.text = self.returnvalues(dprice, bed, bath, sqft)
        print(self.text)
        self.manager.current = 'ResultsScreen'

    def returnvalues(self, dprice, bed, bath , sqft):
        u = User(dprice, bed, bath, sqft)
        predictioncost = u.linear_regression()
        predictioncost = str(predictioncost)
        return predictioncost


class ResultsScreen(Screen):
    label_text = StringProperty('')


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
    pass


InterfaceApp().run()
