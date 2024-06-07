from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import requests

class FeedScreen(Screen):
    def __init__(self, **kwargs):
        super(FeedScreen, self).__init__(**kwargs)
        self.build()

    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.layout.add_widget(Label(text='Feed Screen', font_size=32, size_hint_y=None, height=50))
        scroll_view = ScrollView()
        self.feed_layout = GridLayout(cols=1, size_hint_y=None)
        self.feed_layout.bind(minimum_height=self.feed_layout.setter('height'))
        scroll_view.add_widget(self.feed_layout)
        self.layout.add_widget(scroll_view)
        self.add_widget(self.layout)
        print("Initialized FeedScreen and added widgets")
    
    def on_enter(self):
        self.fetch_data()

    def fetch_data(self):
        response = requests.get("http://localhost:5000/api/data?category=finance")
        if response.status_code == 200:
            data = response.json()
            self.display_data(data)
        print("Fetched data in FeedScreen")

    def display_data(self, data):
        self.feed_layout.clear_widgets()
        for item in data:
            self.feed_layout.add_widget(Label(text=item.get('headline', 'No headline')))
        print("Displayed data in FeedScreen")
