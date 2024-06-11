import multiprocessing
import logging
import time
from backend.api import app
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from frontend.preferences import PreferencesScreen
from frontend.feed import FeedScreen
from frontend.search import SearchScreen


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def start_flask_server():
    logger.info("Starting Flask server...")
    app.run(debug=True)

def start_scheduler():
    import schedule
    import os
    from subprocess import run, CalledProcessError

    def run_scrapy_spider():
        try:
            logger.info("Starting Scrapy spider...")
            run(['scrapy', 'crawl', 'financial_spider'], check=True, cwd=os.path.join(os.path.dirname(__file__), 'scrapy_spider'))
            logger.info("Scrapy spider finished successfully.")
        except CalledProcessError as e:
            logger.error(f"Scrapy spider failed: {e}")

    schedule.every(15).minutes.do(run_scrapy_spider)

    logger.info("Scheduler started. Running Scrapy spider every 15 minutes.")
    run_scrapy_spider()  # Run once at the start

    while True:
        schedule.run_pending()
        time.sleep(1)

def start_kivy_app():
    class MainApp(App):
        def build(self):
            sm = ScreenManager()
            sm.add_widget(PreferencesScreen(name='preferences'))
            sm.add_widget(FeedScreen(name='feed'))
            sm.add_widget(SearchScreen(name='search'))

            main_layout = BoxLayout(orientation='vertical')

            nav_bar = BoxLayout(size_hint=(1, 0.1))
            btn_preferences = Button(text='Preferences')
            btn_preferences.bind(on_release=lambda x: setattr(sm, 'current', 'preferences'))
            btn_feed = Button(text='Feed')
            btn_feed.bind(on_release=lambda x: setattr(sm, 'current', 'feed'))
            btn_search = Button(text='Search')
            btn_search.bind(on_release=lambda x: setattr(sm, 'current', 'search'))

            nav_bar.add_widget(btn_preferences)
            nav_bar.add_widget(btn_feed)
            nav_bar.add_widget(btn_search)

            main_layout.add_widget(nav_bar)
            main_layout.add_widget(sm)

            return main_layout

    MainApp().run()

if __name__ == '__main__':
    flask_process = multiprocessing.Process(target=start_flask_server)
    scheduler_process = multiprocessing.Process(target=start_scheduler)
    kivy_process = multiprocessing.Process(target=start_kivy_app)

    flask_process.start()
    scheduler_process.start()
    kivy_process.start()

    flask_process.join()
    scheduler_process.join()
    kivy_process.join()
