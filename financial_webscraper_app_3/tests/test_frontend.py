import unittest
from frontend.main_gui import MainApp

class TestFrontend(unittest.TestCase):
    def setUp(self):
        self.app = MainApp()

    def test_app_build(self):
        self.assertIsNotNone(self.app.build())

if __name__ == '__main__':
    unittest.main()
