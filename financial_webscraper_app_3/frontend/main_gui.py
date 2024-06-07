from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.label import Label
import requests
from frontend.preferences import PreferencesScreen
from frontend.feed import FeedScreen
from frontend.search import SearchScreen

# Load the .kv file and add a debug statement
kv_file_path = 'frontend/main_gui.kv'
Builder.load_file(kv_file_path)
print(f"Loaded .kv file: {kv_file_path}")

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PreferencesScreen(name='preferences'))
        sm.add_widget(FeedScreen(name='feed'))
        sm.add_widget(SearchScreen(name='search'))
        print("Initialized ScreenManager and added screens")
        return sm

if __name__ == '__main__':
    MainApp().run()
