from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Interface(App):
    def build(self):
        a = AnchorLayout(anchor_x='center', anchor_y='top', padding=[10,100,100,100])
        bu=Button(text="Nithish")
        bu.size_hint = (0.5, 0.2)
        a.add_widget(bu)
        return a

