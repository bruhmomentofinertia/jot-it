from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserIconView

from kivy.uix.camera import Camera

# # from kivy.uix.camera import Camera, pip install kivy[base], opencv-python


# from kivy import Config
# Config.set('graphics', 'multisamples', '0')  # Fix potential OpenGL issues

# from kivy.core.camera import Camera,CoreCamera
# Camera._select_camera_backend("ffpyplayer")

#need to import kivy and ffpyplayer and download the kivy extension, kivy[base]

class Start(Screen):
    pass

class Cam(Screen):
    def start_camera(self):
        camera = self.ids.cam
        camera.play = not camera.play  


class Upload(Screen):
    pass


class Generated(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("new_window.kv")


class JotIt(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)

        self.window = GridLayout()
        self.window.cols = 1
        return kv

    def open_filechooser(self):
        """Open the file chooser dialog to select an image file."""
        self.root.current = "upload"  # Switch to the Upload screen
        self.root.get_screen("upload").ids.filechooser.path = (
            "."  # Open current directory
        )

    def selected_file(self, selection):
        """Handle the selected file from the file chooser."""
        if selection:
            print(f"Selected file: {selection[0]}")  # Print the selected file path


if __name__ == "__main__":
    JotIt().run()
