from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
class ScatterTextWidget(BoxLayout):
    def change_label_color(self):
        color = [random.random() for i in range(3)] + [1]
        label = self.ids['my_label']
        label.color = color
    # pass
class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == '__main__':
    TutorialApp().run()
