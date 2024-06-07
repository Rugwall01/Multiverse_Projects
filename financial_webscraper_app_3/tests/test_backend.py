import unittest
from backend.data_processor import process_data

class TestBackend(unittest.TestCase):
    def test_process_data(self):
        query = {}
        data = process_data(query)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
