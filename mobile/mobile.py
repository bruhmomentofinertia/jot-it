from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserIconView
from kivy.clock import Clock
import time
from kivy.uix.camera import Camera
import os

Window.size = (400, 600)
# need to import kivy and ffpyplayer and download the kivy extension, kivy[base], opencv-python


class Start(Screen):
    pass


class Cam(Screen):
    def start_camera(self):
        camera = self.ids.cam
        camera.play = not camera.play  # on off

    def take_picture(self):
        camera = self.ids.cam
        if camera.play:
            save_dir = os.path.join(os.getcwd(), "saved_photos")
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)  # if folder doesnt exist make it
            existing_files = [
                f
                for f in os.listdir(save_dir)
                if f.startswith("photo_") and f.endswith(".png")
            ]  # count how many long the current folder is it get the next avalible index
            picture_count = len(existing_files) + 1
            filename = f"photo_{picture_count}.png"
            filepath = os.path.join(save_dir, filename)
            camera.export_to_png(filepath)


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
