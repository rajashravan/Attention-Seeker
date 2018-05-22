username = str(input("What is your Instagram Username?"))
password = str(input("What is your Instagram Password?"))
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.lang import Builder
from kivy.uix.button import Button
from InstagramAPI import InstagramAPI
import pyrebase
import time
import math
import datetime

Builder.load_string('''
<ScannerScreen>:
    rows: 2
    Label:
        id: current_user
        text: ''
        font_size: 78
        halign: 'left'
        valign: 'top'
        padding: (15, 15)
        size: self.texture_size
    Label:
        id: best_time
        text: ''
        font_size: 78
        halign: 'left'
        valign: 'top'
        padding: (15, 15)
        size: self.texture_size
    Camera:
        id: camera
        resolution: (640, 480)
        play: True
    Button:
        text: 'Calculate Best Time to Post'
        bold: True
        font_name: 'Montserrat-Light.otf'
        font_size: 55
        on_press: root.scan()
''')

class ScannerScreen(GridLayout):

    def __init__(self, **kwargs):
        super(ScannerScreen, self).__init__(**kwargs)
        api.getProfileData()
        g = api.LastJson()
        name = g['user']['full_name']
        loggedin_user = self.ids['current_user']
        loggedin_user.text = name
        pass

    def scan(self):
        pass


class MyApp(App):

    def build(self):
        return ScannerScreen()

if __name__ == '__main__':
    api = InstagramAPI(username, password)
    api.login()
    MyApp().run()
