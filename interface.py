
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import escape_markup


class Interface(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        a = BoxLayout(orientation='horizontal')
        a = BoxLayout(spacing=10)
        text="Username"
        l = Label(text='[color #000000]' + escape_markup(text) + '[/b]',  markup = True)
        t=TextInput(focus=True)
        l.size_hint = (0.1, 0.2)
        t.size_hint=(0.1,0.2)
        a.add_widget(l)
        a.add_widget(t)
        return a


Interface().run()
