import re

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from user import User


class UserScreen(Screen):
    text = StringProperty('')
    dpricetext = StringProperty('')
    def submit(self):
        try:
            bed = self.ids.bed.text
            bath = self.ids.bath.text
            sqft = self.ids.sqft.text
            dprice = self.ids.dprice.text
            self.text = str(self.returnvalues(dprice, bed, bath, sqft))
            print(self.returnchange(dprice, bed, bath, sqft))
            print("submit:", self.text)
            self.manager.current = 'ResultsScreen'
        except:
            pass

    def returnvalues(self, dprice, bed, bath, sqft):
        u = User(bed, bath, sqft)
        predictioncost = u.linear_regression()
        return predictioncost

    def returnchange(self, dprice, bed, bath, sqft):
        u = User(bed, bath, sqft)
        predictioncost = u.linear_regression()
        # self.dpricetext = dprice
        print("desired", dprice)
        finalcost = abs(int(dprice) - int(predictioncost))
        print(finalcost)
        self.dpricetext = str(finalcost)
        return finalcost


class ResultsScreen(Screen):
    label_text = StringProperty('')
    dpricetext = StringProperty('')


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
