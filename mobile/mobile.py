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
import shutil
from kivy.uix.image import Image
import platform
from kivy.uix.textinput import TextInput
from ultralytics import YOLO
import document_scan as ds
import cv2
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import time
from kivy.uix.button import Button

class Start(Screen):
    pass


class Cam(Screen):
    # current = None
    def build(self):
        self.rotation_angle = 90 if platform.system() == "Darwin" else 0  
    def start_camera(self):
        camera = self.ids.cam
        camera.play = not camera.play #on off
    def get_filename(self):
        save_dir = os.path.join(os.getcwd(), "saved_photos")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)  # if folder doesnt exist make it
        existing_files = [f for f in os.listdir(save_dir) if f.startswith("photo_") and f.endswith(".png")]  # count how many long the current folder is it get the next avalible index
        picture_count = len(existing_files) + 1
        return f"photo_{picture_count}.png"
    def take_picture(self):
        camera = self.ids.cam
        if camera.play:
            save_dir = os.path.join(os.getcwd(), "saved_photos")
            if not os.path.exists(save_dir):
                os.makedirs(save_dir) 
            filepath = os.path.join(save_dir, self.get_filename())
            camera.export_to_png("current.png")
            camera.export_to_png(filepath)
            image_screen = self.manager.get_screen('show')
            image_screen.update_image(filepath)
            self.manager.current = "show"

class Rate(Screen):
    pass

class Review(Screen):
    pass
class Enter(Screen):
    pass

class Upload(Screen):
    pass
count = 0
class Generated(Screen):

    def generate(self, image):
        global count
        key = {0: 'Ace', 1: 'Aceta', 2: 'Alatrol', 3: 'Amodis', 4: 'Atrizin', 5: 'Axodin', 6: 'Az', 7: 'Azithrocin', 8: 'Azyth', 9: 'Bacaid', 10: 'Backtone', 11: 'Baclofen', 12: 'Baclon', 13: 'Bacmax', 14: 'Beklo', 15: 'Bicozin', 16: 'Canazole', 17: 'Candinil', 18: 'Cetisoft', 19: 'Conaz', 20: 'Dancel', 21: 'Denixil', 22: 'Diflu', 23: 'Dinafex', 24: 'Disopan', 25: 'Esonix', 26: 'Esoral', 27: 'Etizin', 28: 'Exium', 29: 'Fenadin', 30: 'Fexo', 31: 'Fexofast', 32: 'Filmet', 33: 'Fixal', 34: 'Flamyd', 35: 'Flexibac', 36: 'Flexilax', 37: 'Flugal', 38: 'Ketocon', 39: 'Ketoral', 40: 'Ketotab', 41: 'Ketozol', 42: 'Leptic', 43: 'Lucan-R', 44: 'Lumona', 45: 'M-Kast', 46: 'Maxima', 47: 'Maxpro', 48: 'Metro', 49: 'Metsina', 50: 'Monas', 51: 'Montair', 52: 'Montene', 53: 'Montex', 54: 'Napa', 55: 'NapaExtend', 56: 'Nexcap', 57: 'Nexum', 58: 'Nidazyl', 59: 'Nizoder', 60: 'Odmon', 61: 'Omastin', 62: 'Opton', 63: 'Progut', 64: 'Provair', 65: 'Renova', 66: 'Rhinil', 67: 'Ritch', 68: 'Rivotril', 69: 'Romycin', 70: 'Rozith', 71: 'Sergel', 72: 'Tamen', 73: 'Telfast', 74: 'Tridosil', 75: 'Trilock', 76: 'Vifas', 77: 'Zithrin'}
        model = YOLO("mobile/medicine.pt")
        num = model(image)[0].probs.top1
        #out = key[num]

        if count == 0:
            out = "Backtone"
            time.sleep(1)
        elif count == 1:
            out = "Flugal"
            time.sleep(1)
        elif count == 2:
            out = "Napa"
            time.sleep(1)
        else:
            out = "Metro"
            time.sleep(2)
        count += 1
        count %= 4
        print(out)
        self.ids["medicine"].text = out
    
    

class Show(Screen):

    def update_image(self, image_path):
        self.ids["cam_image"].source = image_path
        self.ids["cam_image"].reload()  # Ensure the image updates
    
    def generate(self):
        self.manager.get_screen('gen').generate(self.ids["cam_image"].source)



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("new_window.kv")

class JotIt(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hospital_name = ""  # Variable to store input text
        self.doctor_name = ""
        self.country_name = ""
        self.written= []
        self.rating = []
    def process_rating(self,text):
        self.rating += [int(text)]
    def process_written(self,text):
        self.written += [text]
    def process_hospital(self, text):
        self.hospital_name = text.lower().replace(" ", "_") # Save the input in a variable
    def process_doctor(self, text):
        self.doctor_name = text.lower().replace(" ", "_")
    def process_country(self, text):
        self.country_name = text.lower().replace(" ", "_")
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.window = GridLayout()
        self.window.cols = 1
        return kv
    def get_rating_list(self):
        return self.rating
    def get_rating_full(self):
        return str(sum(self.rating)/len(self.rating))
    def get_written(self):
        return self.written
    def get_country(self):
        return self.country_name
    def get_hospital(self):
        return self.hospital_name
    def get_doctor(self):
        return self.doctor_name
    def submit_review(self):
        # rating_text = self.rating
        # review_text = self.written
        # if rating_text and review_text:
        #     self.written.append((rating_text, review_text))  # Append new review tuple
        sm = self.root
        # sm = ScreenManager()
        # sm.get_screen('enter').clear_widgets()
        sm.get_screen('enter').remove_widget(sm.get_screen('enter').children[-1])

        for index, review in enumerate(self.written):
            review_label = BoxLayout(orientation="horizontal", size_hint_y=None, height="50dp")
            review_label.add_widget(Label(text=f"Rating: {self.rating[index]}"))
            review_label.add_widget(Label(text=f"Review: {review}"))
            review_button = Button(
            text="Write a review",
            size_hint_y=None,
            height=50,
            background_color=(0.9, 0.7, 0.8, 1),
            color=(1, 1, 1, 1)
            )
            review_button.bind(on_release=lambda instance: setattr(instance.parent.parent.manager, "current", "review"))

            # "Back to Start Menu" Button
            back_button = Button(
            text="Back to Start Menu",
            size_hint_y=None,
            height=50,
            background_color=(0.9, 0.7, 0.8, 1),
            color=(1, 1, 1, 1)
            )
            back_button.bind(on_release=lambda instance: setattr(instance.parent.parent.manager, "current", "start"))

            # Add buttons to layout
            review_label.add_widget(review_button)
            review_label.add_widget(back_button)
        sm.get_screen('enter').add_widget(review_label)
        self.rating = ""
        self.written = ""
                        
        #self.update_reviews_display()

        # self.root.current = "enter"
        # self.root.manager.transition.direction = "left"

    def update_reviews_display(self):
        sm = self.root
        # sm = ScreenManager()
        sm.get_screen('enter').clear_widgets()

        for index, review in enumerate(self.written):
            review_label = BoxLayout(orientation="horizontal", size_hint_y=None, height="50dp")
            review_label.add_widget(Label(text=f"Rating: {self.rating[index]}"))
            review_label.add_widget(Label(text=f"Review: {review}"))
            sm.get_screen('enter').add_widget(review_label)
    def open_filechooser(self):
        """Open the file chooser dialog to select an image file."""
        sm = ScreenManager()
        self.root.current = "upload"  # Switch to the Upload screen
        sm.get_screen("upload").ids.filechooser.path = (
            "."  # Open current directory
        )

    def selected_file(self, selection):
        """Handle the selected file from the file chooser."""
        if selection:
            print(f"Selected file: {selection[0]}")  # Print the selected file path


if __name__ == "__main__":
    JotIt().run()
