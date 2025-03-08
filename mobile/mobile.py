from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder

class Start(Screen):
    pass

class Upload(Screen):
    pass

class Cam(Screen):
    pass

class Generated(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("new_window.kv")

class Medical(App):
    def build(self):
        self.window  = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source = "osbone.png"))
        self.greeting = Label(text = "avery when he misses the elementary matrices after being warned TWICE")
        self.window.add_widget(self.greeting)
        return kv
    
if __name__ == "__main__":
    Medical().run()

