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
        Builder.load_file('Interface.kv')
        g = GridLayout()
        l = Label()
        t = TextInput()
        l1 = Label()
        t1 = TextInput()
        g.add_widget(l)
        g.add_widget(t)
        g.add_widget(l1)
        g.add_widget(t1)
        return g
Interface().run()
