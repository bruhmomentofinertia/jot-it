from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserIconView
from kivy.clock import Clock
import time
from kivy.uix.camera import Camera


#need to import kivy and ffpyplayer and download the kivy extension, kivy[base], opencv-python

class Start(Screen):
    pass

class Cam(Screen):
    def start_camera(self):
        camera = self.ids.cam
        camera.play = not camera.play 
    def take_picture(self):
        camera = self.ids.cam
        if camera.play:  # Ensure camera is on before taking a picture
            timestamp = time.strftime("%Y%m%d-%H%M%S")  # Unique filename
            filepath = f"captured_image_{timestamp}.png"
            camera.export_to_png(filepath)
            print(f"Image saved to {filepath}")


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
