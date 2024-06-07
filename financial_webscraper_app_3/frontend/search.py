from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import requests

class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.build()

    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.layout.add_widget(Label(text='Search Screen', font_size=32, size_hint_y=None, height=50))
        search_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.search_input = TextInput(hint_text='Enter search term')
        search_button = Button(text='Search')
        search_button.bind(on_release=self.perform_search)
        search_layout.add_widget(self.search_input)
        search_layout.add_widget(search_button)
        self.layout.add_widget(search_layout)
        scroll_view = ScrollView()
        self.search_layout = GridLayout(cols=1, size_hint_y=None)
        self.search_layout.bind(minimum_height=self.search_layout.setter('height'))
        scroll_view.add_widget(self.search_layout)
        self.layout.add_widget(scroll_view)
        self.add_widget(self.layout)
        print("Initialized SearchScreen and added widgets")

    def perform_search(self, *args):
        search_term = self.search_input.text
       
