from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import json
import os

class PreferencesScreen(Screen):
    preferences_file = 'preferences.json'

    def __init__(self, **kwargs):
        super(PreferencesScreen, self).__init__(**kwargs)
        self.build()

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text='Preferences Screen', font_size=32, size_hint_y=None, height=50))
        save_button = Button(text='Save Preferences', size_hint_y=None, height=50)
        save_button.bind(on_release=self.save_preferences)
        layout.add_widget(save_button)
        load_button = Button(text='Load Preferences', size_hint_y=None, height=50)
        load_button.bind(on_release=self.load_preferences)
        layout.add_widget(load_button)
        status_label = Label(id='status', text='', size_hint_y=None, height=50)
        layout.add_widget(status_label)
        self.add_widget(layout)
        print("Initialized PreferencesScreen and added widgets")

    def save_preferences(self, *args):
        preferences = {
            'preference1': 'value1',
            'preference2': 'value2',
        }
        with open(self.preferences_file, 'w') as f:
            json.dump(preferences, f)
        self.ids.status.text = "Preferences saved."
        print("Preferences saved")

    def load_preferences(self, *args):
        if os.path.exists(self.preferences_file):
            with open(self.preferences_file, 'r') as f:
                preferences = json.load(f)
            # Apply loaded preferences
            self.ids.status.text = "Preferences loaded."
            print(preferences)
        else:
            self.ids.status.text = "No preferences found."
        print("Preferences loaded")

    def clear_status(self, *args):
        self.ids.status.text = ""


