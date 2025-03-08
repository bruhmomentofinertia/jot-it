from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image

class Medical(App):
    def build(self):
        self.window  = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source = "osbone.png"))
        self.greeting = Label(text = "avery when he misses the elementary matrices after being warned TWICE")
        self.window.add_widget(self.greeting)
        return self.window
    
if __name__ == "__main__":
    Medical().run()

